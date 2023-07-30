from .import views
from django.urls import path

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.dashboard),
    path('addblog', views.add, name='addblog'),
    path('profile', views.userprofile, name='profile'),
    path('registerpage', views.register, name='registerpage'),
    path('logout', views.sign_out, name='logout'),
    path('login', views.sign_in, name='login'),
    path('<id>', views.detail_view ),
    path('edit/<int:id>/', views.edit_post, name='post-edit'),

    
] 