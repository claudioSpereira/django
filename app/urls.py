from django.urls import path
from .views import index
from .views import listacli
from .views import createcli
from .views import persons_update
from .views import persons_delete

urlpatterns = [
    path('', index,name='index'),
    path('listacli', listacli,name='listacli'),
    path('createcli', createcli,name='createcli'),
    path('update/<int:id>/', persons_update,name='persons_update'),
    path('delete/<int:id>/', persons_delete,name='persons_delete'),
]
