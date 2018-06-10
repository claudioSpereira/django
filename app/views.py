from os import rename

from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.conf.urls.static import static
from .models import Client
from .forms import PersonForm


# Create your views here.
def index(request): 
    return render(request,'index.html')

def listacli(request):
    clients = Client.objects.all()
    return render(request,'listacli.html',{'clients':clients})

def createcli(request):
    form = PersonForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('listacli')
    return render(request, 'createcli.html', {'form':form})

def persons_update(request, id):
    person = get_object_or_404(Client, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('listacli')
    return render(request, 'createcli.html',{'form':form})

def persons_delete(request, id):
    person = get_object_or_404(Client, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('listacli')

    return render(request, 'deletecli.html',{'person':person})