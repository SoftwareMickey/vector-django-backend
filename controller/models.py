import datetime

from django.db import models

# from . import model_handles
# Create your models here.
from django.db import models
from django.utils import timezone


# from django.urls import path
# from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
     # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # ...
    def __str__(self):
        return self.choice_text
    

# # Todo -> Create a class of retrieving data from the database
# class TensorFlowModel(models.Model):
#     name = models.CharField(max_length=100)
    

#     def __str__(self):
#         return self.name
    
# class TFModel(admin.ModelAdmin):
#     def get_urls(self):
#         # Inherit the default admin URLs
#         urls = super().get_urls()

#         # Add custom URL for loading the TensorFlow model
#         custom_urls = [
#             path('load-model/', self.admin_site.admin_view(model_handles.load_h5_model_view), name='load_h5_model'),
#         ]
#         return custom_urls + urls
    
# Register the model with the custom admin
# admin.site.register(TensorFlowModel, TFModel)