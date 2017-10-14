from django.shortcuts import render

def index(request):
    cover_header = "This is cover header"
    cover_description = "discription for cover header"

    context = {
        "cover_header":cover_header,
        "cover_description":cover_description,
    }

    return render(request, "index.html", context)
