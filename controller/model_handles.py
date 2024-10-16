# from django.http import HttpResponse
# from firebase_admin import storage
# import tensorflow as tf

# import os
# import requests

# def download_h5_model():
#     bucket = storage.bucket()
#     blob = bucket.blob('models/my_model.h5')  # Path to your model in Firebase Storage
#     local_model_path = 'my_model.h5'          # Local path to store the downloaded model

#     # Download the .h5 file from Firebase to a local file
#     blob.download_to_filename(local_model_path)
    
#     return local_model_path

# # Function to handle the custom admin view
# def load_h5_model_view(request):
    
    
#     print('---------------------------- LOAD MODEL FROM FIREBASE ---------------------------------------------------')
#     model_path = download_h5_model()  # Download the model from Firebase
    
#     # Load the model using Keras
#     model = tf.keras.models.load_model(model_path)
#     return HttpResponse("Model loaded successfully.")

    
#     # # Get the model summary as a string (can customize further)
#     # model_summary = []
#     # model.summary(print_fn=lambda x: model_summary.append(x))
#     # model_summary = "\n".join(model_summary)
    
#     # # Return the model summary as a response
#     # return HttpResponse(f"<pre>{model_summary}</pre>")
# # Todo -> After the url is received triggger a function to download the model

# def download_mode_file_using_download_url(file_url, save_path):
#     print()
#     print("---------------------- MODEL FILE DOWNLOAD IN PROGRESS --------------------------------------------")
#     print("Url Received: " + str(file_url))
    
#     try:
#         # Create the directory if it doesn't exist
#         os.makedirs(os.path.dirname(save_path), exist_ok=True)

#         # Send a GET request to download the file
#         response = requests.get(file_url, stream=True)
#         response.raise_for_status()  # Raise an error for bad responses

#         # Save the file to the specified path
#         with open(save_path, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=8192):
#                 if chunk:  # Filter out keep-alive chunks
#                     file.write(chunk)

#         return {'success': True, 'path': save_path}

#     except requests.exceptions.RequestException as e:
#         return {'success': False, 'error': f'File download failed: {str(e)}'}