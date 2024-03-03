from django.contrib import admin
from django.urls import path,include
from moviegallery import views


app_name='moviegallery'

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),

    # path('addmovie',views.addmovie,name="addmovie"),
    path('addmovie/',views.MovieAdd.as_view(),name="addmovie"),

    # path('viewmovie/<int:p>',views.viewmovie,name="viewmovie"),
    path('movie/<int:pk>/',views.MovieDetail.as_view(),name="viewmovie"),

    # path('edit/<int:p>',views.edit,name="edit"),
    path('update/<int:pk>/',views.MovieUpdate.as_view(),name="edit"),


    # path('delete/<int:p>',views.delete,name="delete"),
    path('delete/<int:pk>',views.MovieDelete.as_view(),name="delete")
]

