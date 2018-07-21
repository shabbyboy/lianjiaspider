from django.shortcuts import render

# Create your views here.

def showGit(request):
    return render(request,"hellogit.html",context={"data":"hello git,i want to go togther"})
