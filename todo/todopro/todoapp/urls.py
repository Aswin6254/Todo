from . import views
from django.urls import path
# app_name="todoapp"
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.tasklistview.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.detaillistview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updatelistview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deletelistview.as_view(),name='cbvdelete'),
]