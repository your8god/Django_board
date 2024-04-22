from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='main'),
    path('item/<int:board_id>/', views.index_page, name='index_page'),
    path('rublic/<int:rublic_id>/', views.rublic_page, name='rublic_page'),
    path('add/', views.BbCreateView.as_view(), name='add'),
]