from django.shortcuts import render,redirect
from moviegallery.forms import Movieform
from moviegallery.models import Movie
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.



# def home(request):
#     k = Movie.objects.all()
#     return render(request,'home.html',{'f':k})

class MovieList(ListView):
    model=Movie
    template_name = "home.html"
    context_object_name = "f"




# def addmovie(request):
#     if(request.method=='POST'):
#         m=request.POST['m']
#         d = request.POST['d']
#         y = request.POST['y']
#         c = request.FILES['c']
#         f=Movie.objects.create(Name=m,desc=d,year=y,img=c)
#         f.save()
#         return redirect("/")
#     return render(request,'addmovie.html')


class MovieAdd(CreateView): #which displays a form for adding new object and handles form submission
    model=Movie
    template_name = "addmovie.html"
    fields = "__all__"
    success_url = reverse_lazy('moviegallery:home')



# def viewmovie(request,p):
#     f=Movie.objects.get(id=p)
#     return render(request,'viewmovie.html',{'f':f})

class MovieDetail(DetailView):
    model=Movie
    template_name = "viewmovie.html"
    context_object_name = "f"



#
# def edit(request,p):
#     f = Movie.objects.get(id=p)
#     if (request.method == 'POST'):  # after form submission
#         form = Movieform(request.POST, request.FILES, instance=f)
#         if form.is_valid():
#             form.save()  # saves the form object inside Db table
#         return home(request)
#
#     form=Movieform(instance=f)
#     return render(request,'edit.html',{'form':form})

class MovieUpdate(UpdateView):
    model=Movie
    template_name = "addmovie.html"
    fields = "__all__"
    success_url = reverse_lazy('moviegallery:home')




# def delete(request,p):
#     f = Movie.objects.get(id=p)
#     f.delete()
#     return home(request)

class MovieDelete(DeleteView):       #here in deleteview we need to create a html file
    model=Movie
    success_url = reverse_lazy('moviegallery:home')
    template_name = "delete.html"
