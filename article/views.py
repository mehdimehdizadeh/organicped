from django.shortcuts import render
from .models import Article, Category, Adminpage,Aboutus,Contact

# Create your views here.
def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    admins = Adminpage.objects.all()[:1]
    context = {
        "articles":articles,
        "categories":categories,
        "admins":admins,
    }
    return render(request,'index.html',context)

def aboutus(request):
    abouts = Aboutus.objects.all()[:1]
    categories = Category.objects.all()
    admins = Adminpage.objects.all()[:1]
    context = {
        "categories":categories,
        "admins":admins,
        "abouts":abouts,
    }
    return render(request,"about.html",context)

def contact(request):
    contacts = Contact.objects.all()[:1]
    categories = Category.objects.all()
    admins = Adminpage.objects.all()[:1]
    context = {
        "categories":categories,
        "admins":admins,
        "contacts":contacts,
    }
    return render(request,"contact.html",context)

def category(request,id):
    category_id = Category.objects.filter(id=id).first()
    category_posts = Article.objects.filter(category=category_id)
    categories = Category.objects.all()
    admins = Adminpage.objects.all()[:1]
    context = {
        "categories":categories,
        "admins":admins,
        "category_posts":category_posts,
    }
    return render(request,"category.html",context)