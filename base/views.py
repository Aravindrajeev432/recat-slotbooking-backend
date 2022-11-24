from django.db.migrations import serializer
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
import json
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Pastebin API')
# from django.conf.urls import url


# from users.models import Account
from django.contrib.auth.models import User
from .models import Application, Slots
from .serializers import AccountSerializer, SignupSerializer, ApplicationSerializer, SlotSerializer, ApprovedCompanies
from django.db.models import Q
from rest_framework import generics

# urlpatterns = [
#     url(r'^$', schema_view)
# ]

class Test(APIView):
    def get(self, request):
        post = [{
            'status': 200,
            'message': "Yes Django REST",
            'method_called': 'You Called GET'

        },
            {
                'status': 200,
                'message': "Yes Django REST",
                'method_called': 'You Called GET'

            }
            ,
            {
                'status': 200,
                'message': "Yes Django REST",
                'method_called': 'You Called GET'

            }

        ]
        return Response(post)


class Signup(APIView):

    def post(self, request):
        body = request.body.decode("utf-8")
        body = json.loads(body)

        username = body['username']
        email = body['email']
        password = body['password']

        print(username)
        print(email)
        print(password)
        if User.objects.filter(email=email).exists():
            return Response({'errors': "Email already exists"}, status=status.HTTP_409_CONFLICT)
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()
        except Exception as e:
            print(e)
        return Response(200)

    def get(self, request):
        post = {"username": "",
                "email": "",
                "password": "",
                "phone": "",
                }
        return Response(post)


class Usershow(APIView):
    def get(self, request):
        Acc = User.objects.all()
        serializer = AccountSerializer(Acc, many=True)
        print(serializer.data)
        return Response(serializer.data)


class Regapp(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        post = {"username": "",
                "address": "",
                "city": "",
                "state": "",
                "phone": "",
                "email": "",
                "phone": "",
                "company_name": "",
                "answer1": "",
                "answer2": "",
                "answer3": "",
                "answer4": "",
                "answer5": "",
                "answer6": "",
                "proposal": "",
                }
        return Response(post)

    def post(self, request):
        body = request.body.decode("utf-8")

        body = json.loads(body)
        # print(body['data'])
        body = body['data']
        print(body)
        # automatically gets user because we passed access token in header
        user = request.user
        print(user.id)
        username = body['username']
        address = body['address']
        city = body['city']
        state = body['state']

        email = body['email']
        phone = body['phone']
        company_name = body['company_name']
        answer1 = body['answer1']
        answer2 = body['answer2']
        answer3 = body['answer3']
        answer4 = body['answer4']
        answer5 = body['answer5']
        answer6 = body['answer6']
        proposal = body['proposal']
        applications = Application.objects.create(
            user=user,
            name=username,
            address=address,
            city=city,
            state=state,
            email=email,
            phone=phone,
            company_name=company_name,
            answer1=answer1,
            answer2=answer2,
            answer3=answer3,
            answer4=answer4,
            answer5=answer5,
            answer6=answer6,
            proposal=proposal,

        )
        print(city, state, answer1)
        applications.save()
        return Response(200)

        #         data = {
        #             'user':2,
        #             'name': username,
        #             'email': email,
        #             'phone': phone,
        #             'company_name': company_name,
        #             'address': address,
        #             'city': city,
        #             'state': state,
        #             'answer1': answer1,
        #             'answer2': answer2,
        #             'answer3': answer3,
        #             'answer4': answer4,
        #             'answer5': answer5,
        #             'answer6': answer6,
        #             'proposal': proposal,
        # }
        # print(data)
        # serializer = ApplicationSerializer(data=data)
        return Response(200)
        # if serializer.is_valid():
        #     print("successfully")
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     print("Not successfully")
        #
        #     return Response({'errors': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Checkemail(APIView):
    def post(self, request):
        body = request.body.decode("utf-8")
        body = json.loads(body)
        email = body['email']
        if User.objects.filter(email=email).exists():
            return Response({'errors': "Email already exists"}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_200_OK)


class Checkusernewapp(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user =User.objects.get(id=5)
        # print(user)
        user = request.user
        if not Application.objects.filter(user=user).exists():
            return Response(status=status.HTTP_200_OK)
        if Application.objects.filter(Q(user=user) & Q(Denied=True)):
            return Response(status=status.HTTP_200_OK)

        if Application.objects.filter(Q(user=user) & Q(applied=True) & ~Q(alloted=True) ).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        elif Application.objects.filter(Q(user=user) & Q(applied=True) & Q(Approved=True)).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_200_OK)


class Applications(APIView):

    def get(self, request):
        applications = Application.objects.all()
        serializerObj = ApplicationSerializer(applications, many=True)
        return Response(serializerObj.data)


class Userappview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        slots = Application.objects.filter(user=user)
        serializerObj = ApplicationSerializer(slots, many=True)
        return Response(serializerObj.data, status=status.HTTP_200_OK)


class NewAppPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class Newapplicationslist(APIView, LimitOffsetPagination):

    def post(self, request):
        apps = Application.objects.filter(Q(applied=True) & Q(Approved=False) & Q(Denied=False))
        result_page = self.paginate_queryset(apps, request, view=self)
        print(apps)
        serializerObj = ApplicationSerializer(result_page, many=True)
        return Response(serializerObj.data, status=status.HTTP_200_OK)


class Approveapp(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        print(pk)
        user = request.user
        print(user)
        print("patch")

        obj = Application.objects.filter(id=pk).update(Approved=True)

        return Response(200)


class Denyapp(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        print(pk)
        Application.objects.filter(id=pk).update(Denied=True)
        return Response(200)


class Getapprovedapps(APIView):
    def get(self, request):
        apps = Application.objects.filter(Approved=True)
        serializerObj = ApplicationSerializer(apps, many=True)
        return Response(serializerObj.data, status=status.HTTP_200_OK)


class Getdeniedapps(APIView):
    def get(self, request):
        apps = Application.objects.filter(Denied=True)
        serializerObj = ApplicationSerializer(apps, many=True)
        return Response(serializerObj.data, status=status.HTTP_200_OK)


class Slotsview(APIView):
    def get(self, request):
        slots = Slots.objects.all()

        for i in slots:
            print(i.user)

        serializerObj = SlotSerializer(slots, many=True)
        # post ={
        #     "name": "slots"
        # }
        return Response(serializerObj.data, status=status.HTTP_200_OK)


class GetCompanyname(APIView):
    def get(self, request, pk):
        company_id = pk

        company_name = Application.objects.get(pk=company_id)
        print(company_name.user.username)
        post = [{
            "company_name": company_name.user.username
        }]
        return Response(post, status=status.HTTP_200_OK)


class Getapprovedcompanies(APIView):

    def get(self, request):
        company_details = Application.objects.filter(Q(Approved=True) & Q(alloted=False))
        serializerObj = ApprovedCompanies(company_details, many=True)

        return Response(serializerObj.data, status=status.HTTP_200_OK)


class Assignslot(APIView):

    def get(self, request, pk, company_name):
        print(pk)
        print(company_name)
        app = Application.objects.filter(company_name=company_name).update(alloted=True)

        Slots.objects.filter(id=pk).update( company_name=company_name)
        return Response(status=status.HTTP_200_OK)

