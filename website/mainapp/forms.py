from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioCreaUsuarios(UserCreationForm):
    first_name = forms.CharField        (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar su nombre',
                                            'max_length':' El nombre no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            })
                                        )
    last_name = forms.CharField         (label="Apellido", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar su apellido',
                                            'max_length':' El apellido no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            })
                                        )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class FormularioConsulta(forms.Form):
    nombre = forms.CharField          (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar su nombre',
                                            'max_length':' El nombre no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email de contacto',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control',
                                            'type':'email'})
                                        )
    asunto = forms.CharField         (label="Asunto", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el asunto',
                                            'max_length' : 'El asunto no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    mensaje = forms.CharField           (label="Mensaje", required = True, max_length=1000,
                                        error_messages={
                                            'required': 'Indique el mensaje',
                                            'max_length': 'El campo puede tener hasta 1000 caracteres',
                                        },
                                        widget= forms.Textarea(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    
class FormularioAsistencia(forms.Form):
    nombre = forms.CharField            (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar su nombre',
                                            'max_length':' El nombre de contacto no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email de contacto',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control',
                                            'type':'email'})
                                        )
    area = forms.CharField              (label="Área", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el área',
                                            'max_length' : 'El área no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    asunto = forms.CharField            (label="Asunto", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el asunto',
                                            'max_length' : 'El área no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    mensaje = forms.CharField           (label="Mensaje", required = True, max_length=1000,
                                        error_messages={
                                            'required': 'Indique el mensaje',
                                            'max_length': 'El campo puede tener hasta 1000 caracteres',
                                        },
                                        widget= forms.Textarea(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    
class FormularioLogin(forms.Form):
    username = forms.CharField          (label='Usuario', required=True,
                                        max_length=30, min_length=5,
                                        error_messages={
                                            'required': 'El usuario es obligatorio',
                                            'max_length': 'El nombre de usuario no puede ser superior a los 30 caracteres',
                                            'min_length': 'El nombre de usuario debe tener al menos 5 caracteres'
                                        },
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Por favor, ingrese su nombre de usuario',
                                            'class': 'form-control'
                                        })
                                        )
    password = forms.CharField          (label='Contraseña', required=True,
                                        max_length=30, min_length=1,
                                        error_messages={
                                            'required': 'La contraseña es obligatoria',
                                            'max_length': 'La contraseña no puede superar los 30 caracteres',
                                            'min_length': 'La contraseña debe tener al menos 1 caracter'
                                        },
                                        widget=forms.PasswordInput(attrs={
                                            'placeholder': 'Por favor, ingrese su contraseña',
                                            'class': 'form-control'
                                        })
                                        )
