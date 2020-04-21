from django.shortcuts import render
from django.views import generic
from blogingapp.models import BlogDetial

# Create your views here.
class IndexView(generic.ListView):
    
    template_name ='blogingapp/index.html'
    context_object_name='blog_list'
    

    def get_queryset(self):
        
        return BlogDetial.objects.order_by('title')

def detaillist(request,myid):
    # model=BlogDetial
    template_name='blogingapp/detail.html'
    myid=request.GET('id')
    selblog=BlogDetial.objects.filter(myid=id)[0]
    return render(request,template_name,{'blog':selblog})
   

# def index(request):

#     return render(request,'blogingapp/index.html')
