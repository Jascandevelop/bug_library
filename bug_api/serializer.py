# from rest_framework import serializers
# from bug_api.models import Bug

# class BugSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     species = serializers.CharField()
#     family = serializers.CharField()
#     year_identified = serializers.IntegerField()

#     def create(self, data): #create method
#         return Bug.objects.create(**data)

#     def update(self, instance, data):
#         instance.name = data.get('name', instance.name)
#         instance.species = data.get('species', instance.species)
#         instance.family = data.get('family', instance.family)
#         instance.year_identified = data.get('year_identified', instance.year_identified)

#         instance.save()
#         return instance


from rest_framework import serializers
from bug_api.models import Bug
from django.forms import ValidationError

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"

    def validate_title(self, value):
        if value == "ladybug":
            raise ValidationError("No beetles in library")
        return value

    def validate(self, data):
        if data["year_identified"] > 2020:
            raise ValidationError("Only bugs identified before 2020 accepted")
        return data 