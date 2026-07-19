from django.shortcuts import render

def mentorados(request):
    return render(request, "mentorados.html")