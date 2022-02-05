from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import RegisterView
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.conf import settings

PASSWORD_RESET_CONFIRM_REDIRECT_URL = getattr(settings, 'PASSWORD_RESET_CONFIRM_REDIRECT_URL')
ACCOUNT_CONFIRM_EMAIL_URL = getattr(settings, 'ACCOUNT_CONFIRM_EMAIL_URL')

urlpatterns = [
    path('api/', include('dj_rest_auth.urls')),
    path('rest-framework/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('api/registration/', RegisterView.as_view(), name='account_signup'),
    path('password/reset/confirm/<uidb64>/<token>/',
         RedirectView.as_view(url=PASSWORD_RESET_CONFIRM_REDIRECT_URL + '?uidb64=%(uidb64)s&token=%(token)s'),
         name='password_reset_confirm'
         ),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            RedirectView.as_view(url=ACCOUNT_CONFIRM_EMAIL_URL + '?key=%(key)s'),
            name='account_confirm_email'),
]
