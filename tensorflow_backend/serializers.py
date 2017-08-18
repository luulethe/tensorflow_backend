from rest_framework import serializers


class ImageUploadSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    file = serializers.FileField()


class NotificationSerializer(serializers.Serializer):
    image_id = serializers.CharField()
    name = serializers.CharField()
    prob = serializers.FloatField()


class SessionListSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()


class OrderInfoSerializer(serializers.Serializer):
    person_id = serializers.IntegerField()


class ConfirmSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    user_id = serializers.IntegerField()