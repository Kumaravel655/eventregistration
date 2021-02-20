from django.shortcuts import render
from .models import participatent

# Create your views here.
def home(request):
    context = {}
    return render(request,'eventapp/home.html',context)
def register(request):
    context = {}
    if request.method == 'POST':
        p1 = participatent()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.email = request.POST.get('phone','-')
        p1.email = request.POST.get('insitution','-')

        if  len(participatent.objects.all())>10:
            return render(request,'eventapp/failed.html',context)
        else:
            p1.save()
            return render(request,'eventapp/success.html',context)
    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['insitution'] = ''


    return render(request, 'eventapp/register.html', context)
def result(request):
    context = {}

    context['participant'] = participatent.objects.all()

    return render(request, 'eventapp/result.html', context)

