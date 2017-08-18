from tensorflow_backend import serializers, models
from tensorflow_backend.views.base_views import BaseAPIView


class OrderInfoView(BaseAPIView):
    SERIALIZER_CLASS = serializers.OrderInfoSerializer

    def process(self, data):
        try:
            food_person = models.FoodPerson.objects.get(person_id=data["person_id"])
        except models.FoodPerson.DoesNotExist:
            return {
                "error": "DOEST_NOT_EXISTED"
            }
        food = food_person.food
        return {
            "user_id": data["person_id"],
            "food_name": food.name,
            "food_image": food.image_url,
            "food_number": food.food_number
        }