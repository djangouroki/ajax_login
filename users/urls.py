from django.urls import path, include

from users.views import Register, LoginAjaxView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),

    path('login_ajax/', LoginAjaxView.as_view(), name='login_ajax')
]
