from django.shortcuts import redirect,render

def BASE(request):
    return render(request,'base.html')

def HOMEPAGE(request):

    return render(request,'components/homepage.html')

def CONTACT(request):

    return render(request,'contact.html')

def ABOUT(request):

    return render(request,'about.html')



