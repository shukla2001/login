from django import forms  
from login.models import Login  
class LoginForm(forms.ModelForm):  
    class Meta:  
        model = Login  
        fields = "__all__" 