
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("j",views.j,name="j"),
    path("brain",views.brain,name="brain"),
    path("david",views.david,name="david"),
    
]
