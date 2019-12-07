#python imports.
import csv

#django/rest_framework imports.
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import permission_required
from rest_framework.viewsets import GenericViewSet

#app level imports.
from libs import(
    locationiq,
) 
from .serializer import (
    LatLongAddressSerializer,
)
from libs.exceptions import(
    ParseException,
    ResourceConflictException,
)
from libs.constants import(
    BAD_ACTION,
    BAD_REQUEST,
)
from .models import (
    LatLongAddress,
)

class FileViewSet(GenericViewSet):
    """
    """
    queryset = LatLongAddress.objects.all()

    serializers_dict = {
        'fileupload' : LatLongAddressSerializer,
        'getlistofaddress' : LatLongAddressSerializer,
        }

    def get_queryset(self, filterdata=None):
        if filterdata:
            self.queryset = LatLongAddress.objects.filter(**filterdata)
        return self.queryset

    def get_serializer_class(self):
        try:
            return self.serializers_dict[self.action]
        except KeyError as key:
            raise ParseException(BAD_ACTION, errors=key)

    @action(methods=['post'], detail=False)
    def fileupload(self, request):
        """
        Use to read the  csv file.
        """
        try:
            key = request.data['key']    # geogoogle api key.
            data = request.data
            data = data.copy()

            csvfile = request.FILES['file']
            text = str(csvfile.read().decode("utf-8")) # get all records from file.
            print(text)
            string = text.split('\n')
            for row in string:
                row_str = row.split(',')
                if row_str[0] != 'address':
                    lat, lon = locationiq.getlatlon(row_str, key) #function call.

                    data['address'] = str(row_str).strip("[']")
                    data['latitude'] = lat
                    data['longitude'] = lon

                    if lat == 0 and lon == 0: # api key error.
                        return Response(({"error": "Invalid key"}), 
                            status=status.HTTP_401_UNAUTHORIZED)

                    serializer = self.get_serializer(data=data)
                    print(serializer.is_valid())
                    serializer.save()

            return Response(({"detail":"file uploaded successfully."}), 
                status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(({'error':str(e)}), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def getlistofaddress(self, request):
        """
        It Return all the records.
        """
        data = self.get_serializer(self.get_queryset(), many=True).data 
        return Response(data, status=status.HTTP_200_OK)


    @action(methods=['delete'], detail=False)
    def deletealladdress(self, request):
        """
        delete all the records from database.
        """
        data = self.get_queryset()
        data.delete()
        return Response(({"detail":"all records deleted."}),
            status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False)
    def downloadfile(self, request):
        """
        use to download csv file.
        """
        data = self.get_queryset()  

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="latlonaddr.csv"'
        writer = csv.writer(response, delimiter=',')
        writer.writerow(['address','latitude','longitude']) 

        for obj in data:
            writer.writerow([obj.address,obj.latitude,obj.longitude])
        return response







        
