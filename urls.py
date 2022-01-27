from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import RegisterView
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/', RegisterView.as_view(), name='account_signup'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
            name='account_confirm_email'),

]
