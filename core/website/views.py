from django.shortcuts import render
from django.contrib import messages

from website.forms import ContactForm

# IndexView for home page
def index_view(request):
    return render(request, "website/index.html")

# AboutView for about page
def about_view(request):
    return render(request, "website/about.html")

# ContactView for contact page
def contact_view(request):
    """ Description:
        - It gets request of the user. If it's POST, then it checks
          if the form is valid or not. If it is, it will save the
          form and the message.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, "پیام شما به بنده ارسال شد!")
        else:
            message = messages.error(request, "متأسفانه پیام شما ارسال نشد! لطفاً تمامی موارد مهم را وارد کنید.")
    form = ContactForm()
    
    context = {"form": form}
    return render(request, "website/contact.html", context)

def sample_view(request):
    return render(request, "website/sample.html")
