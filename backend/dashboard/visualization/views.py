# from django.shortcuts import render
# from .serializers import VisSerializer
# from .models import Vis
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
# from azure.kusto.data.exceptions import KustoServiceError
# from azure.kusto.data.helpers import dataframe_from_result_table
# from azure.kusto.data import DataFormat
# from azure.kusto.ingest import QueuedIngestClient, IngestionProperties, FileDescriptor, BlobDescriptor, ReportLevel, ReportMethod
# import pandas as pd
# import time
# import simplejson as json
# from dashboard import views
# from datetime import datetime
# from django.shortcuts import render
# from django.views.generic import View
   
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from io import StringIO 
# from django.http import HttpResponse
# import cairo

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'templates/index.html')
# # Create your views here.
# @api_view(['GET'])
# def getDetails(request):
#     vis = Vis.objects.all()
#     serializer = VisSerializer(vis, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getDetail(request, pk):
#     vis = Vis.objects.get(id=pk)
#     serializer = VisSerializer(vis, many=False)
#     return Response(serializer.data)
 
# @api_view(['GET'])
# def graph(request):
#     vis = Vis()
#     KUSTO_URI = "https://testdataapp.southindia.kusto.windows.net"
#     KUSTO_INGEST_URI = "https://ingest-testdataapp.southindia.kusto.windows.net"
#     KUSTO_DATABASE = "test"
#     KCSB_INGEST = KustoConnectionStringBuilder.with_interactive_login(
#         KUSTO_INGEST_URI)

#     KCSB_DATA = KustoConnectionStringBuilder.with_interactive_login(
#         KUSTO_URI)
 
#     DESTINATION_TABLE = "HeartBeat"
#     DESTINATION_TABLE_COLUMN_MAPPING = "heart_beat"
#     KUSTO_CLIENT = KustoClient(KCSB_DATA)

#     QUERY = "HeartBeat"
#     RESPONSE = KUSTO_CLIENT.execute_query(KUSTO_DATABASE, QUERY)
#     # print(RESPONSE.primary_results[0])
#     df = dataframe_from_result_table(RESPONSE.primary_results[0])
#     datas = list(df["heart_beat"])
#     for i in datas:
#         vis.heart_beat = json.dumps(i)
#     vis.save()
#     beat = Vis.objects.values_list('heart_beat')
#     # print(vis[0])
#     time = Vis.objects.values_list('time')
#     data ={
#                      "labels":time,
#                      "chartLabel":"Vitals",
#                      "chartdata":beat,
#              }
    
#     return Response(data)
    

from .models import Vis
from .serializers import VisSerializer
from rest_framework.generics import ListAPIView

class VisList(ListAPIView):
    queryset = Vis.objects.all()
    serializer_class = VisSerializer