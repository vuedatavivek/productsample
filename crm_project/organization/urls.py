from django.urls import include, path
from .views import CreateHardware, UpdateHardware, DeleteHardware, ListHardware, DetailHardware

urlpatterns = [
    path('create/', CreateHardware.as_view(), name='create-hardware'),
    path('', ListHardware.as_view()),
    path('<int:pk>/',DetailHardware.as_view(), name='retrieve-hardware'),
    path('update/<int:pk>>/', UpdateHardware.as_view(), name='update-customer'),
    #path('delete/<int:pk>>/', DeleteHardware.as_view(), name='delete-hardware')
]