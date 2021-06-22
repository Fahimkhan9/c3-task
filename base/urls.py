from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',  views.home,name='home' ),
    path('create/<str:Type>/',  views.createPizza,name='createPizza' ),
    path('update/<int:id>/',  views.updatePizza,name='updatePizza' ),
    path('delete/<int:id>/',  views.deletePizza,name='deletePizza' ),


    path('all/',  views.getAllPizza,name='getAllPizza' ),
    path('all/filters',views.getFilteredPizza,name='getFilteredPizza' )



]
