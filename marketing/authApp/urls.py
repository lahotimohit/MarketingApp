from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/google/login', include('allauth.urls'), name='google_login'),
    path('accounts/', include('allauth.urls')),
]
