from django.shortcuts import render

def indexContent(request):
    return render(request, 'templateApp/index.html')

def aboutContent(request):
    return render(request, 'templateApp/about.html')
