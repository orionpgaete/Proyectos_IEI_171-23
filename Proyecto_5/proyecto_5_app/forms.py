from django import forms
from django.core import validators

class Registrousuario(forms.Form):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloqueado','BLOQUEADO')]

    nombre = forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(10)])
    telefono = forms.CharField(required=False)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre.widget.attrs['class'] = 'form-control' 
    telefono.widget.attrs['class'] = 'form-control' 
    email.widget.attrs['class'] = 'form-control' 
    password.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select' 
    
    def clean(self):
        user_clean_data = super().clean()

        
        
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("El correo debe contener un @")    
        return inputEmail
        
    def clean_nombre(self):
        inputnombre = self.cleaned_data['nombre']
        if len(inputnombre) > 20:
            raise forms.ValidationError("El largo maximo del nombre son 20 caracteres..")       
        return inputnombre