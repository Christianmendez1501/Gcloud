def functionprueba(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    print("Vamos campeonnnnnnNNSSSSnn1")
    file = event
    print(f"Processing file: {file['name']}.")
