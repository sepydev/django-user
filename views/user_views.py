from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import User as UserModel
from ..serializers import UserPhotoSerializer


class UploadUserPhotoViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserPhotoSerializer
    permission_class = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.id)

    def perform_update(self, serializer):
        new_photo = self.request.FILES['file']
        old_photo = self.queryset.first().photo
        if old_photo:
            old_photo.delete(save=True)
        serializer.save(photo=new_photo)
