from .forms import SearchForm, CreateForm

def search_form(request):
    return {'search_form': SearchForm()}

def create_form(request):
    return {'create_form': CreateForm()}
