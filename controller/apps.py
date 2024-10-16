# import json
# import os

from django.apps import AppConfig

# import firebase_admin
# from firebase_admin import credentials

class ControllersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'controller'
    
    # name = 'firebaseapp'
    # Get the current directory and construct the file path
        
    # def ready(self):
        
    #     current_dir = os.path.dirname(__file__)
    #     file_path = os.path.join(current_dir, './vector-key.json')

    #     # Read the service account key JSON file
    #     with open(file_path, 'r') as f:
    #         service_account_info = json.load(f)

    #     # Initialize Firebase Admin SDK with the loaded credentials
    #     cred = credentials.Certificate(service_account_info)
    #     # Initialize Firebase app here to ensure it's only initialized once
    #     if not firebase_admin._apps:
    #         firebase_admin.initialize_app(cred, {
    #             'storageBucket': 'vector-technologies-16b3f.appspot.com'
    #         })
