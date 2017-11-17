from django.conf.urls import url
from . import views

# def test(request):
#     print """
#     App level process
    
#     """


urlpatterns = [  
    url(r'^$', views.dashboard),
    url(r'^add$', views.add),
  
]