from django.urls import path
from . import views
from .views import About,Teacher,Blog,Create

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('about/',About.as_view(),name="about"),
    path('teachers/',Teacher.as_view(),name="teacher"),
    path('news/',Blog.as_view(),name="news"),
    path('create/',Create.as_view(),name="create")
    
    
    
    
]