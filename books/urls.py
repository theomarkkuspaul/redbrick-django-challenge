from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:book_id>/', views.detail, name='detail'),
  path('<int:book_id>/checkout', views.checkout, name='checkout'),
  path('<int:book_id>/checkin', views.checkin, name='checkin')
]