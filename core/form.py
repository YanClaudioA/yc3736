from django.forms import ModelForm
from core.models import *

class FormCliente (ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


