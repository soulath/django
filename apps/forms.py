from django import forms
from .models import Blogs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a ModelForm
class BlogsForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Blogs
		fields = "__all__"
class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
          "class": "input",
          "type": "text",
          "placeholder": "ກະລຸນາປ້ອນໃສ",
          "class": "form-control"

    }), label="ຊື່ຜູ້ໃຊ້")

    email = forms.EmailField(widget=forms.EmailInput(attrs={
         "class": "input",
          "type": "text",
          "placeholder": "ກະລຸນາປ້ອນໃສ",
          "class": "form-control"
          
    }), label="ອີເມວ")



    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "input",
          "type": "text",
          "placeholder": "ກະລຸນາປ້ອນໃສ",
          "class": "form-control"
          
    }), label="ລະຫັດຜ່ານ")

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "input",
          "type": "text",
          "placeholder": "ກະລຸນາປ້ອນໃສ",
          "class": "form-control"
          
    }), label="ຢື້ນຢັ້ນລະຫັດຜ່ານ")
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 


    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label="ຊື່ຜູ້ໃຊ້ງານ")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="ລະຫັດຜ່ານ")


