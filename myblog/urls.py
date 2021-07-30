
from myblog.models import Category
from django.urls import path
#from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdateView,DeleteView,AddCategoryView,CategoryView,LikeView

urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('details/<int:pk>', ArticleDetailView.as_view(),name='details'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('details/edit/<int:pk>',UpdateView.as_view(),name='updatepost'),
    path('details/<int:pk>/delete',DeleteView.as_view(),name='deletepost'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('like/<int:pk>',LikeView,name='like_post'),
    
    #path('category-list/',CategoryListView,name='category-list')
    
]