from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .model_handles import *


# Create your views here.
@csrf_exempt
def connection_success(request):
    return JsonResponse({"message" :"Hello connection has been done successfully..!"})

# # Todo -> Establish a connection from front-end

# @csrf_exempt
# def connecton_establishment_with_frontend(request):
    
#     if request.method == 'POST':
#         print()
#         print('------------------------ * CONNECTION ESTABLISHMENT IN PROGRESS * --------------------------------')
        
#         request_body = json.loads(request.body)
        
#         url_received = request_body.get('url')
#         file_name = request_body.get('file_name')
        
#         print(url_received)
        
#         save_path = os.path.join(settings.MEDIA_ROOT, '../models', file_name) 
        
#         if url_received:
#             print(url_received)
#             download_mode_file_using_download_url(file_url=url_received, save_path=save_path)
            
#         print()
#         print('--------------------------------- * PREDICTION LINK GENERATION * --------------------------------')
#         prediction_link = f"{settings.BASE_URL}/models/predict"
        
        
#         data = {'message' : 'connection success', 'prediction_link' : prediction_link}
        
#         return JsonResponse(data)

# def clone_repo_and_retrieve_py_files(repo_url, clone_dir, target_dir):
#     """
#     Clones a Git repository and retrieves only .py files from it.

#     :param repo_url: URL of the Git repository to clone.
#     :param clone_dir: Directory where the repository will be cloned.
#     :param target_dir: Directory where the .py files will be stored.
#     """
#     # Clone the repository
#     if not os.path.exists(clone_dir):
#         os.makedirs(clone_dir)

#     # Clone the repo
#     try:
#         print("Cloning repository...")
#         repo = git.Repo.clone_from(repo_url, clone_dir)
#         print("Repository cloned successfully!")
        
#         # Go through the repository and copy only .py files to target directory
#         if not os.path.exists(target_dir):
#             os.makedirs(target_dir)

#         for root, dirs, files in os.walk(clone_dir):
#             for file in files:
#                 if file.endswith('.py'):
#                     file_path = os.path.join(root, file)
#                     print(f"Copying {file_path}")
#                     shutil.copy(file_path, target_dir)

#         print("Python files have been copied successfully!")
    
#     except Exception as e:
#         print(f"Error cloning repository: {e}")


# from .preprocessing_utils import *

# # Todo -> Write a post request to send data to the data
# @csrf_exempt
# def post_data_and_predict(request):
    
#     print()
#     print('-------------------------- MODEL PROCESSING -------------------------')
    
#     import numpy as np
    
#     if request.method == 'POST':
#         print("Request has been to database for processing")
        
#         # Specify the directory where the .h5 files are stored
#         models_directory = os.path.join(settings.MEDIA_ROOT, '../models')  # Adjust the path as necessary
        
#         # Look for .h5 files in the specified directory
#         h5_files = [f for f in os.listdir(models_directory) if f.endswith('.h5')]
        
#         if not h5_files:
#             return JsonResponse({'error': 'No .h5 files found in the directory.'}, status=404)
        
#         # Use the first .h5 file found (or implement your logic to select a specific file)
#         file_to_use = h5_files[0]
        
#         print(file_to_use)
        
#         if request.content_type == 'application/json':
            
#             print()
#             print('-------------------------- DATA IMPORTATION & CONVERSION -------------------------')
            
#             data = json.loads(request.body)
            
#             conveted_data = accept_and_convert_data(data)
#             print('data received: ' + str(conveted_data))
            
#             print()
#             print('-------------------------- MODEL PROCESSING IN PROGRESS -------------------------')
            
#             model = tf.keras.models.load_model(file_to_use);
#             print(model)
            
#             print()
#             print('-------------------------- DATA RESHAPING & PREDICTING -------------------------')
            
#             reshaped_data_2 = reshaped_data(conveted_data, np=np)
    
#             predicted_data = load_data_and_predict(reshaped_data_2, model)
            
#             print('predicted data: ' + str(predicted_data))
#     else:
#         print("There is no request made for prediction")
        
#     return HttpResponse("Predicted Price: " + str(predicted_data[0][0]))