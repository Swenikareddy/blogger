from django import forms
from .models import Category, MyPost

#cats=[('coding','coding'),('sports','sports'),('Education','Education'),('Entertainment','Entertainment'),('others','others')]
choices=Category.objects.all().values_list('name','name')
choice_list=[]
for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model=MyPost
        fields=('title','author','category','body','header_image')
        widgets={
             'title':forms.TextInput(attrs={'class':'form-control'}),
             'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authname', 'type':'hidden'}),
             #'author':forms.Select(attrs={'class':'form-control'}),
             'category':forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
             'body':forms.Textarea(attrs={'class':'form-control'}),
         }
     
class PostForm_2(forms.ModelForm):
    class Meta:
        model=MyPost
        fields=('title','category','body')
        widgets={
             'title':forms.TextInput(attrs={'class':'form-control'}),
             'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
             'body':forms.Textarea(attrs={'class':'form-control'}),
         }
     