from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table
from azure.kusto.data import DataFormat
from azure.kusto.ingest import QueuedIngestClient, IngestionProperties, FileDescriptor, BlobDescriptor, ReportLevel, ReportMethod
import pandas as pd
import time


# KUSTO_URI = "https://testvitals.centralindia.kusto.windows.net/"
# KUSTO_INGEST_URI = "https://ingest-testvitals.centralindia.kusto.windows.net/"
KUSTO_URI = "https://testdataapp.southindia.kusto.windows.net"
KUSTO_INGEST_URI = "https://ingest-testdataapp.southindia.kusto.windows.net"
KUSTO_DATABASE = "test"
KCSB_INGEST = KustoConnectionStringBuilder.with_interactive_login(
    KUSTO_INGEST_URI)

KCSB_DATA = KustoConnectionStringBuilder.with_interactive_login(
    KUSTO_URI)

DESTINATION_TABLE = "HeartBeat"
DESTINATION_TABLE_COLUMN_MAPPING = "heart_beat"



# CONTAINER = "samplefiles"
# ACCOUNT_NAME = "kustosamples"
# SAS_TOKEN = ""  # If relevant add SAS token
# FILE_PATH = "K:\Research_group\quinproc\maatrtv\heart_data.csv"
# FILE_PATH = "heart_data.txt"
# # FILE_SIZE = 64158321    # in bytes
# DATAFRAME = pd.read_csv(FILE_PATH)
# BLOB_PATH = FILE_PATH
# FILE_SIZE = 15900
KUSTO_CLIENT = KustoClient(KCSB_DATA)
# DROP_TABLE_COMMAND = ".drop table StormEvents ifexists"
# CREATE_TABLE_COMMAND = ".create table HeartBeat (heart_beat: real)"

# RESPONSE = KUSTO_CLIENT.execute_mgmt(KUSTO_DATABASE, CREATE_TABLE_COMMAND)
# RESPONSE = KUSTO_CLIENT.execute_mgmt(KUSTO_DATABASE, DROP_TABLE_COMMAND)
# print(RESPONSE)
# dataframe_from_result_table(RESPONSE.primary_results[0])

# CREATE_MAPPING_COMMAND = """.create table HeartBeat ingestion csv mapping 'heart_beat' '[{"Name":"heart_beat","datatype":"real","Ordinal":0}]'"""

# RESPONSE = KUSTO_CLIENT.execute_mgmt(KUSTO_DATABASE, CREATE_MAPPING_COMMAND)

# dataframe_from_result_table(RESPONSE.primary_results[0])

# INGESTION_CLIENT = QueuedIngestClient(KCSB_INGEST)

# # All ingestion properties are documented here: https://learn.microsoft.com/azure/kusto/management/data-ingest#ingestion-properties
# INGESTION_PROPERTIES = IngestionProperties(database=KUSTO_DATABASE, table=DESTINATION_TABLE, data_format=DataFormat.TXT,
#                                            ingestion_mapping_reference=DESTINATION_TABLE_COLUMN_MAPPING, additional_properties={'ignoreFirstRecord': 'false'})
# # FILE_SIZE is the raw size of the data in bytes
# BLOB_DESCRIPTOR = FileDescriptor(BLOB_PATH, FILE_SIZE)
# # INGESTION_CLIENT.ingest_from_file(file_descriptor=BLOB_DESCRIPTOR, ingestion_properties=INGESTION_PROPERTIES)
# INGESTION_CLIENT.ingest_from_file(BLOB_DESCRIPTOR, ingestion_properties=INGESTION_PROPERTIES)
# # INGESTION_CLIENT.ingest_from_blob(BLOB_DESCRIPTOR, ingestion_properties=INGESTION_PROPERTIES)

# print('Done queuing up ingestion with Azure Data Explorer')

QUERY = "HeartBeat | count"
RESPONSE = KUSTO_CLIENT.execute_query(KUSTO_DATABASE, QUERY)
# print(RESPONSE.primary_results[0])
df = dataframe_from_result_table(RESPONSE.primary_results[0])
print(list(df["heart_beat"]))
# print(df)
# while True:
#     time.sleep(60)
#     RESPONSE = KUSTO_CLIENT.execute_query(KUSTO_DATABASE, QUERY)
#     print(dataframe_from_result_table(RESPONSE.primary_results[0]))
    # if dataframe_from_result_table[0]>0: