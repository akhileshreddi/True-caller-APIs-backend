
from django.urls import path
from . import views

urlpatterns = [
   path('createuser',views.createuser,name='createuser'),
   path('createcontact',views.createcontact,name='createcontact'),
   path('userlogin',views.userlogin,name='userlogin'),
   path('spam',views.spam,name='spam'),
   path('searchByName',views.search_by_name, name='searchByName'),
   path('searchByPhone',views.search_by_phone,name='searchByPhone')
]
