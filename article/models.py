from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50,verbose_name="Kateqoriya")

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Katrqoriyalar"

class Article(models.Model):
    category = models.ManyToManyField(Category,verbose_name="Kateqoriya",blank=True)
    title = models.CharField(max_length=50, verbose_name="Başlıq")
    price = models.CharField(max_length=50, verbose_name="Qiymət")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,null=True,verbose_name="Şəkil")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Postlar"

class Adminpage(models.Model):
    logo = models.FileField(blank=True,null=True, verbose_name="Logo")
    icon = models.FileField(blank=True,null=True,verbose_name="İcon")
    instagram = models.CharField(verbose_name="Instagram",max_length=150)
    twitter = models.CharField(verbose_name="twitter",max_length=150)
    linkedin = models.CharField(verbose_name="linkedin",max_length=150)
    facebook = models.CharField(verbose_name="facebook",max_length=150)
    whatsapp = models.CharField(verbose_name="watsapp",max_length=150)
    whatsapp_image = models.FileField(blank=True,null=True,verbose_name="Whatsapp")

    def __str__(self):
        return self.whatsapp
    class Meta:
        verbose_name_plural = "Admin seçənəkləri"

class Aboutus(models.Model):
    title = models.CharField(max_length=50,verbose_name="Başlıq")
    content = models.TextField(verbose_name="Mətn")
    image = models.FileField(blank=True, null=True, verbose_name="Şəkil")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Haqqımızda"

class Contact(models.Model):
    location = models.CharField(max_length=50,verbose_name="Məkan")
    phone = models.CharField(max_length=50,verbose_name="Əlaqə")
    email = models.CharField(max_length=50,verbose_name="Email")

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name_plural = "Əlaqə"

