from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('detail/<int:id>/', views.store_detail),
    path('menu/<int:store_id>/', views.menu_list),
    path('list/', views.store_list),
]