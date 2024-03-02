from .forms import SearchForm, CreateForm

def search_form(request):
    return {'search_form': SearchForm()}
