from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)

    def clean(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long')
        
        super(PostForm, self).clean()
        