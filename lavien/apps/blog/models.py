from django.db import models

# Create your models here.
from apps.accounts.models import User

class Category(models.Model):
    name = models.CharField("Название",max_length=50)
    slug = models.SlugField(max_length=60)
    icon = models.ImageField(upload_to="category/icons/")
    description = models.TextField("Описание категории", null= True)
    # objects = models.Manager()
    class Meta: 
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
        



class Tag(models.Model):
    name = models.CharField("Название",max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="post/images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    is_draft = models.BooleanField("Черновик", default=True)
    tags = models.ManyToManyField(Tag, related_name= "tags")
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="posts"   
        )
   
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    
    
    def __str__(self):
        return self.title




class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    text = models.TextField("Комментарий")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text


class Organization(models.Model):
    org_name = models.CharField("Название",max_length=50)
    slug = models.SlugField(max_length=60)
    picture = models.ImageField("Изображение", upload_to="organization/icons/", null=True)
    description = models.TextField("Описание организации", null=True)
    dop_dscr = models.TextField("Дополнительное описание", null=True)
    email = models.CharField("Электронная почта", max_length=255, unique=True, null=True)
    mobile = models.CharField("Номер телефона",max_length=20, null=True)
    category = models.ManyToManyField(Category, 
        related_name="organizations")
    # objects = models.Manager()
    class Meta: 
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.org_name




class AddMemory(models.Model):
    title = models.CharField("Заголовок",max_length=255, null= True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name="organizations", null=True)
    image = models.ImageField("Фото", upload_to="memory/images/")
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memories")
    is_draft = models.BooleanField("Черновик", default=True)
    
    class Meta: 
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.title


class VoluenteerApplication(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name="voluenteers", null=True)
    email = models.CharField("Электронная почта", max_length=255, null= True, unique=True)
    age = models.IntegerField("Возраст", null=True)
    first_name = models.CharField("Имя", max_length=100, null=True)
    last_name = models.CharField("Фамилия", max_length=100, null=True)
    mobile = models.IntegerField("Номер телефона")
    answer1 = models.TextField("Почему вы хотите стать именно нашим волонтером?")
    answer2 = models.IntegerField("Сколько часов в день можете уделять волонтерству? ")
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta: 
        verbose_name = "Заявка волонтера"
        verbose_name_plural = "Заявки волонтеров"

    def __str__(self):
        return self.email


