from django.urls import path
from article import views
from django.conf.urls import url

app_name = "article"
urlpatterns = [
    path('category/<int:id>',views.category, name="category"),
]