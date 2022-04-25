from email.policy import default
from unicodedata import name
from django.apps import AppConfig

from gymProject.settings import DEFAULT_AUTO_FIELD

class TrainingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'training'
