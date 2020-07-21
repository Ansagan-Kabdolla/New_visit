from django.shortcuts import render
from .forms import ZakazForm
from .models import Zakaz
from django.db.models import Q

def create(request):
    if request.method == "POST":
        form = ZakazForm(request.POST)
        if form.is_valid():
            public = form.save(commit=False)
            if public.password == 'Astana':
                e = True
                public.save()
            else:
                e = False
            return render(request,'index.html',{'e':e})
    return render(request,'index.html')

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        print(query)
        if query:
            people = Zakaz.objects.filter(
                    Q(name__icontains=query) | Q(iin__icontains=query)
                )
            count = len(people)
            return render(request, 'add-bron.html', {'people': people,'count':count,'query':query})
        else:
            return render(request, 'add-bron.html')