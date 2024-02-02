from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['Content']
        widgets = {
            'Content':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'Post Content'})            
        }
  
    #Own Save Method to Retrieve Owner and Save the Relation between classes
    def save(self, commit=True,user=None):
        Post = super().save(commit=False)
        Post.Author = user
        Post.save()
        return Post