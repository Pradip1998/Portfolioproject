from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [

    path('', views.home, name='home'),
    path('index.html', views.home, name='index.html'),
    path('certificate/<int:id>', views.certificate, name='certificate'),
    path('education/<int:id>', views.education, name='education'),
    path('project/<int:id>', views.project, name='project'),


]
