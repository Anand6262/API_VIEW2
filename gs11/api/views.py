from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None): #Initially pk=0
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)

        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>>>>>>>>>>>")
        serializer=StudentSerializer(data=request.data) #We have all data in //request.data//
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data inserted successfully!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)



    def put(self, request, pk, format=None):
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated successfully!!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



    def patch(self, request, pk, format=None):
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated successfully(partially)!!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self, request, pk, fromat=None):
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg' : 'Data deleted successfully!!!'}, status=status.HTTP_200_OK)




# # Create your views here
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def hello_world(request, pk=None):
#     if request.method == 'GET':
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>>>>>>>>>>>")
#         # id=request.data.get('id') #Here we are getting directly parsed data from //request.deta//. This is the beauty of //@api_view// decorator
#         id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     if request.method == 'POST':
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>>>>>>>>>>>")
#         serializer=StudentSerializer(data=request.data) #We have all data in //request.data//
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data inserted successfully!!!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#     if request.method == 'PUT':
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         # id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data updated successfully!!!'}, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


#     if request.method == 'PATCH':
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data updated successfully(partially)!!!'}, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


#     if request.method =='DELETE':
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg' : 'Data deleted successfully!!!'}, status=status.HTTP_200_OK)