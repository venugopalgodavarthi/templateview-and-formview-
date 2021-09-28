from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from formview.forms import empform
# Create your views here.
'''
def samplefunc(request):
    if request.method=='POST':
        form = empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")
    if request.method=='GET':
        form= empform()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})

    def post(self,request):
        if request.method=='POST':
            form= empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")
'''
class Formview(FormView):
    form_class=empform
    template_name='form.html'
    def form_valid(self, form):
        form.save()
        return HttpResponse('form is summit')





'''
#function based view
def samplefunc(request):
    form = empform
    return render(request,"homefunc.html",{'res':form})

#userdefined based view
class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})

#predefined based view
class Formview(FormView):
    form_class = empform
    template_name='form.html'
'''