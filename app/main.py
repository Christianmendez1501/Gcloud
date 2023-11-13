from google.cloud import storage, firestore
import json

def function_prueba(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    print("Vamos nacho")
    file = event
    print(f"Processing file: {file['name']}.")

    bucket_name = file['bucket']
    file_name = file['name']

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    file_content = blob.download_as_text()

    db = firestore.Client()
    collection_name = 'thebridge'

    try:
        usuario = json.loads(file_content)

        db.collection(collection_name).add(usuario)

        print("Datos almacenados en Firestore correctamente.")
    except Exception as e:
        print(f"Error al procesar y almacenar datos en Firestore: {e}")

