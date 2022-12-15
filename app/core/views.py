from django.shortcuts import render
from .forms import ContactRegistration
from .models import Contact

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'home.html', context)

def contact(request):
 if request.method == 'POST':
  fm = ContactRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   sb = fm.cleaned_data['subject']
   ms = fm.cleaned_data['message']
   reg = Contact(name=nm, email=em, subject=sb, message=ms)
   reg.save()
   fm = ContactRegistration()
 else:
  fm = ContactRegistration()

 return render(request, 'contact.html',{'contact': 'active','fm':fm})

