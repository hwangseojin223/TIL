from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2)
    content = forms.CharField(
        min_length=5,
        widget=forms.Textarea(
            attrs={'class':'my-class'}
        )
    )
    
    class Meta:
        model = Article
        fields = '__all__'