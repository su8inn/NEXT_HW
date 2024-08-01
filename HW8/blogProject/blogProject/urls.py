from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]
