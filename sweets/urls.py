from django.urls import path
from .views import SweetList, SweetDetail, SweetCreate, SweetUpdate, SweetDelete

urlpatterns = [
    path('', SweetList.as_view(), name='list'),
    path('<int:pk>/', SweetDetail.as_view(), name='detail'),
    path('create/', SweetCreate.as_view(), name='create'),
    path('<int:pk>/update', SweetUpdate.as_view(), name='update'),
    path('<int:pk>/delete', SweetDelete.as_view(), name='delete'),
]
