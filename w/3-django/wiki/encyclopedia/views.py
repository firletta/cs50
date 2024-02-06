from django.shortcuts import render, redirect

from . import util
from .forms import SearchForm, CreateForm, EditForm
from . import util
from .forms import EditForm

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def error(request, error):
    return render(request, "encyclopedia/error.html", {
        "error": error,
    })

def entry(request, title):
    if util.get_entry(title) == None:
        return error(request, error="404")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": util.get_entry(title),
    })

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            if util.get_entry(query) != None:
                return redirect("entry", title=query)
            else:
                results = []
                for entry in util.list_entries():
                    if query.lower() in entry.lower():
                        results.append(entry)
                return render(request, "encyclopedia/search.html", {
                    "results": results,
                })
        else:
            return render(request, "encyclopedia/search.html", {
                "search_form": form
            })
    return render(request, "encyclopedia/search.html")

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None:
                util.save_entry(title, content)
                return redirect("entry", title=title)
            else:
                return error(request, error="409")
        else:
            return render(request, "encyclopedia/create.html")
    return render(request, "encyclopedia/create.html")

