from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer


class Home(APIView):

    def get(self, request):

        persons = Person.objects.all()

        ser_data = PersonSerializer(instance=persons, many=True)

        return Response(data=ser_data.data)

    #
    #
    #
    def post(self, request):

        friend_name = request.query_params["name"]
        cus_name = request.data["name"]

        return Response(
            {"message": f"hello mr {cus_name} , how about   {friend_name} "}
        )
