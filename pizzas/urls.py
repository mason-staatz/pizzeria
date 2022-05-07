from django.urls import path

from . import views
import pizzas

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizza_menu',views.pizza_menu, name='pizza_menu'),
    path('pizza_menu/<int:pizza_id>/', views.pizza_type, name='pizza_type'),
    #path('new_topic/', views.new_topic, name='new_topic'),
    path('new_comment/', views.new_comment, name='new_comment'),
    #path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
]