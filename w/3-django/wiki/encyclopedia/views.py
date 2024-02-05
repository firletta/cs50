from django.shortcuts import render, redirect

from . import util
from .forms import SearchForm

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })
    
def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
        })
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