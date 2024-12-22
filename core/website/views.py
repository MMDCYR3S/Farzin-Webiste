from django.shortcuts import render

# IndexView for home page
def index_view(request):
    return render(request, "website/index.html")

# AboutView for about page
def about_view(request):
    return render(request, "website/about.html")

# ContactView for contact page
def contact_view(request):
    return render(request, "website/contact.html")