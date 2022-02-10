from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User as UserModel


class UploadUserPhotoView(APIView):
    permission_class = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request):
        try:

            user = UserModel.objects.filter(pk=self.request.user.id).first()
            new_photo = self.request.FILES['file']
            if not new_photo:
                return Response(
                    {
                        'message': 'You have to send an image file.'
                    },
                    status.HTTP_400_BAD_REQUEST
                )

            old_photo = user.photo
            if old_photo:
                old_photo.delete(save=True)
            user.photo.save(new_photo.name, new_photo, save=True)
            user.refresh_from_db()
            return Response(
                {
                    'message': "File uploaded.",
                    'photo': request.build_absolute_uri(user.photo.url),
                },
                status.HTTP_200_OK
            )
        except Exception as ex:
            return Response(
                {
                    'message': str(ex)
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        try:
            user = UserModel.objects.filter(pk=self.request.user.id).first()
            old_photo = user.photo
            if old_photo:
                old_photo.delete(save=True)

            return Response(
                {
                    'message': "Photo deleted.",
                },
                status.HTTP_200_OK
            )

        except Exception as ex:
            return Response(
                {
                    'message': str(ex)
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
