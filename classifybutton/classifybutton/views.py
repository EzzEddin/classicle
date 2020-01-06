from django.shortcuts import render
import requests
import sys, os, inspect
from subprocess import run, PIPE

def button(request):
    return render(request, 'classicle-ui.html')

def external(request):
    inp= request.POST.get('param')
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    parentdir = os.path.dirname(parentdir)
    sys.path.insert(0,parentdir)
    out= run([sys.executable, os.path.join(parentdir, "classifyclick.py"),inp],shell=False,stdout=PIPE)
    print(out)
    return render(request, 'classicle-ui.html',{'result':str(out.stdout, "utf-8")})
