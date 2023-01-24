from rest_framework import serializers

from app.models import User, File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class UploadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = ['file']
#
#     def create(self, validated_data):
#         request = self.context.get("request", None)
#         return File.objects.create(**validated_data, owner_id=request.user.id, mark='new')

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'mark', 'created', 'changed']
