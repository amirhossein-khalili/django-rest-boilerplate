from rest_framework import serializers

from .models import Answer, Person, Question


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    # email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers (self , obj):
        result = obj.answers.all()
        return  AnswerSerializer(instance=result , many=True).data
    # def create(self, validated_data):
    #     request = self.context.get("request")
    #     validated_data["user"] = request.user
    #     return super().create(validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = "__all__"

    # def create(self, validated_data):
    #     request = self.context.get("request")
    #     validated_data["user"] = request.user.id
    #     return super().create(validated_data)
