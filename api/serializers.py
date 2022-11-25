from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length = 100)

