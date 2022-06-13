from django.urls import path     
from . import views
urlpatterns = [
    path('', views.visitnumber),
        path('destroy_session/', views.destroySession),	

]
