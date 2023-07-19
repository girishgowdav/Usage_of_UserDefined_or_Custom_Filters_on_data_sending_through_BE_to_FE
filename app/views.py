from django.shortcuts import render

# Create your views here.
def userdefined(request):
    d={'data':'HaI SyeRaa..!! WhatsUpp MaNnn..'}
    return render(request,'userdefined.html',d)