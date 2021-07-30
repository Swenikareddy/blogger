from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, MyPost
from .forms import PostForm,PostForm_2
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

#def home(request):
    #return render(request,'myblog/home.html',{})
def LikeView(request,pk):
    post=MyPost.objects.get(id=pk)
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('details',args=[str(pk)]))

class HomeView(ListView):
    model=MyPost
    template_name='myblog/home.html'
    ordering=['-pdate']

    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu    
        return context

'''def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,'myblog/category_list.html',{'cat_menu_list':cat_menu_list})'''

def CategoryView(request,cats):
    category_posts=MyPost.objects.filter(category=cats)
    return render(request,'myblog/categories.html',{'cats':cats.title(),'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model=MyPost
    template_name='myblog/details.html'

    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        data=get_object_or_404(MyPost,id=self.kwargs['pk'])
        total_likes=data.total_likes()

        liked=False
        if data.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["cat_menu"]=cat_menu
        context['total_likes']=total_likes  
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=MyPost
    form_class=PostForm
    template_name='myblog/addpost.html'
    #fields='__all__'
    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(AddPostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context


class AddCategoryView(CreateView):
    model=Category
    #form_class=PostForm
    template_name='myblog/addCategory.html'
    fields='__all__'
class UpdateView(UpdateView):
    model=MyPost
    form_class=PostForm_2
    template_name='myblog/update.html'
    #fields=('title','body')
    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(UpdateView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

class DeleteView(DeleteView):
    model=MyPost
    template_name='myblog/delete.html'
    success_url=reverse_lazy('home')