from django.forms import *
from base.models import *

class datacreation(ModelForm):
    
    class Meta:
        model = Advocate
        fields = "__all__"
    
    
   