from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView, ListView, DetailView, FormView, DeleteView, UpdateView, CreateView
from .models import Post,Category, Organization, AddMemory, VoluenteerApplication, Comment
from .forms import VoluenteerApplicationForm, CommentCreateForm

class IndexPage(ListView):
    template_name = "index.html"
    queryset = Post.objects.all()


class ProductsView(TemplateView):
    template_name = "products.html"


class CategoryListView(ListView):
    template_name = "category_list.html"
    model = Category
    queryset = Category.objects.all()



class PostListView(ListView):
    template_name ="post_list.html"
    model = Post
    queryset = Post.objects.filter(is_draft=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context
    
    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            qs = Post.objects.filter(is_draft=False, category__slug=category_slug)
            return qs
        return Post.objects.filter(is_draft=False)





class OrganizationListView(ListView):
    model = Organization
    template_name = 'filter_category.html'
    context_object_name = 'organizations'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        return Organization.objects.filter(category=category)




class OrganizationDetailView(DetailView):
    template_name = "organization_detail.html"
    model = Organization
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media"] = AddMemory.objects.filter(organization=self.get_object())
        context["form"] = VoluenteerApplicationForm()
        return context
    


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post
    # pk=id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()
        context["comment_form"] = CommentCreateForm()

        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostCreateForm, AddOrganizationMemoryForm

class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    template_name = "post_create.html"


    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class AuthorPostListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    template_name = "author_posts.html"
    model = Post
    def get_queryset(self):
        qs = Post.objects.filter(author = self.request.user)
        return qs

      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()
        context["comment_form"] = CommentCreateForm()

        return context


def get_author_posts(request):
    qs = Post.objects.filter(author=request.user)
    context = {
        "posts":qs
    }
    return render(request, 'author_posts', context)
  
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

def delete_author_post(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404 
    post = get_object_or_404(Post, id=pk) 
    post.delete()
    return redirect(reverse_lazy("author_posts"))


def deactivate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk) 
    post.is_draft = True
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))


def activate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk) 
    post.is_draft = False
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostCreateForm
    model = Post
    success_url = reverse_lazy("author_posts")
    template_name = "post_create.html"



class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentCreateForm
    model = Comment
   
   

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk":self.kwargs.get("post_id")})




class AuthorPostListView(LoginRequiredMixin, ListView):
    template_name = "author_posts.html"
    model = Post
  
    def get_queryset(self):
        qs = Post.objects.filter(author = self.request.user)
        return qs




class AddOrganizationMemoryView(LoginRequiredMixin, FormView):
    model = AddMemory
    form_class = AddOrganizationMemoryForm
   
    template_name = "add_memory.html"
    success_url = reverse_lazy("add_memory")


    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)



class VoluenteerApplicationCreate(CreateView):
    form_class = VoluenteerApplicationForm
    model = VoluenteerApplication

    def get_success_url(self):
        org_id = self.kwargs.get("org_id")
        return reverse_lazy("organizations_detail", kwargs={"pk":org_id})

def create_voluenteer_application(request, org_id):
    if request.method == "POST":
        form = VoluenteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("organizations_detail", kwargs={"pk":org_id}))
        print(form.errors)
    return redirect(reverse_lazy("organizations_detail", kwargs={"pk":org_id}))
class AboutMeView(TemplateView):
    template_name = "about_me.html"



class FaqView(TemplateView):
    
    template_name = "faq_page.html"
   

