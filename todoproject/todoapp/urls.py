from django.contrib import admin
from django.urls import path

from todoapp import views
app_name='todoapp'
urlpatterns = [
    path('',views.home,name='home'),
    # path('detail/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbv/',views.listview.as_view(),name='cbv'),
    path('cbvdetail/<int:pk>/' , views.detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/' , views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/' , views.deleteview.as_view(),name='cbvdelete'),
]
