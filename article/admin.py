from django.contrib import admin

# Register your models here.
from .models import Article,Adminpage,Aboutus,Contact,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]

    class Meta:
        model = Category

class ContactAdmin(admin.ModelAdmin):
    list_display = ["phone"]

    class Meta:
        model = Contact

class AboutusAdmin(admin.ModelAdmin):
    list_display = ["content"]

    class Meta:
        model = Aboutus

class AdminpageAdmin(admin.ModelAdmin):
    list_display = ["watsapp"]

    class Meta:
        model = Adminpage


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","price","created_date"]
    list_display_links = ["title"]
    search_fields = ["title","price"]
    list_filter = ["created_date"]

    class Meta:
        model = Article



admin.site.register(Article)
admin.site.register(Adminpage)
admin.site.register(Aboutus)
admin.site.register(Contact)
admin.site.register(Category)