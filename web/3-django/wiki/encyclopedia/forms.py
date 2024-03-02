from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={"placeholder": "Search Encyclopedia"}))
    
class CreateForm(forms.Form):
    title = forms.CharField(label="Title", help_text="", widget=forms.TextInput(attrs={"id":"entry-title", "placeholder": "Title of the new page"}))
    content = forms.CharField(label="Content", help_text="", widget=forms.Textarea(attrs={ "id":"entry-content","placeholder": "Content of the new page"}))
    
class EditForm(forms.Form):
    title = forms.CharField(label="Title", help_text="", widget=forms.TextInput(attrs={"id":"entry-title", "readonly": "readonly"}))
    content = forms.CharField(label="Content", help_text="", widget=forms.Textarea(attrs={ "id":"entry-content"}))