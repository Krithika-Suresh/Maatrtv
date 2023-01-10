from azure.kusto.data import KustoConnectionStringBuilder, DataFormat
from azure.kusto.ingest import QueuedIngestClient, IngestionProperties, FileDescriptor, BlobDescriptor

ingestion_props = IngestionProperties(database="testdb", table="HeartBeat", data_format=DataFormat.CSV)
client = QueuedIngestClient(KustoConnectionStringBuilder.with_interactive_login("https://ingest-testvitals.kusto.windows.net"))

file_descriptor = FileDescriptor("heart_data.csv", 15900)  # in this example, the raw (uncompressed) size of the data is 15KB (15360 bytes)
client.ingest_from_file(file_descriptor, ingestion_properties=ingestion_props)
client.ingest_from_file("heart_data.csv", ingestion_properties=ingestion_props)