from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from permissions import IsOwnerReadOnly

from .models import Answer, Person, Question
from .serializers import AnswerSerializer, PersonSerializer, QuestionSerializer


class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        persons = Person.objects.all()

        ser_data = PersonSerializer(instance=persons, many=True)

        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    #
    #
    #
    def post(self, request):

        friend_name = request.query_params["name"]
        cus_name = request.data["name"]

        return Response(
            {"message": f"hello mr {cus_name} , how about   {friend_name} "},
            status=status.HTTP_201_CREATED,
        )


class QuestionListView(APIView):
    """
    this can get all the questions list

    it also contains answer of each questions with it

    and if the you delete question answer will delete too

    """

    serializer_class = QuestionSerializer

    def get(self, request, pk=None):
        if pk is not None:

            try:

                question = Question.objects.get(pk=pk)
                ser_data = QuestionSerializer(instance=question).data
                return Response(ser_data, status=status.HTTP_200_OK)

            except Question.DoesNotExist:

                return Response(
                    {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            questions = Question.objects.all()
            ser_data = QuestionSerializer(instance=questions, many=True).data
            return Response(ser_data, status=status.HTTP_200_OK)


class QuestionGetDataView(APIView):

    serializer_class = QuestionSerializer

    def get(self, request, pk=None):
        if pk is not None:
            try:
                question = Question.objects.get(pk=pk)
                ser_data = QuestionSerializer(instance=question).data
                return Response(ser_data, status=status.HTTP_200_OK)
            except Question.DoesNotExist:
                return Response(
                    {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            questions = Question.objects.all()
            ser_data = QuestionSerializer(instance=questions, many=True).data
            return Response(ser_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):

    serializer_class = QuestionSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data["user"] = request.user.id
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):

    serializer_class = QuestionSerializer

    permission_classes = [IsOwnerReadOnly]

    def patch(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            self.check_object_permissions(request, question)
        except Question.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        ser_data = QuestionSerializer(
            instance=question, data=request.data, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):

    serializer_class = QuestionSerializer

    permission_classes = [IsOwnerReadOnly]

    def delete(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            self.check_object_permissions(request, question)
        except Question.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerListView(APIView):

    serializer_class = AnswerSerializer

    def get(self, request, pk=None):
        if pk is not None:
            try:
                answer = Answer.objects.get(pk=pk)
                ser_data = AnswerSerializer(instance=answer).data
                return Response(ser_data, status=status.HTTP_200_OK)
            except Answer.DoesNotExist:
                return Response(
                    {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            answers = Answer.objects.all()
            ser_data = AnswerSerializer(instance=answers, many=True).data
            return Response(ser_data, status=status.HTTP_200_OK)


class AnswerGetDataView(APIView):

    serializer_class = AnswerSerializer

    def get(self, request, pk=None):
        if pk is not None:
            try:
                answer = Answer.objects.get(pk=pk)
                ser_data = AnswerSerializer(instance=answer).data
                return Response(ser_data, status=status.HTTP_200_OK)
            except Answer.DoesNotExist:
                return Response(
                    {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            answers = Answer.objects.all()
            ser_data = AnswerSerializer(instance=answers, many=True).data
            return Response(ser_data, status=status.HTTP_200_OK)


class AnswerCreateView(APIView):

    serializer_class = AnswerSerializer

    def post(self, request):
        request.data["user"] = request.user.id
        ser_data = AnswerSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerUpdateView(APIView):

    serializer_class = AnswerSerializer

    def patch(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        ser_data = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDeleteView(APIView):

    serializer_class = AnswerSerializer

    def delete(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
