from django.conf import settings
from rest_framework import serializers

from users.models import User as UserModel


class UserDetailSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        model = UserModel
        fields = ('pk',
                  'email',
                  'first_name',
                  'last_name',
                  'biography',
                  'website',
                  'phone_number',
                  'gender'
                  )
        read_only_fields = ('email',)
