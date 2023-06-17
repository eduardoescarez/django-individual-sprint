from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import FormularioConsulta, FormularioLogin, FormularioAsistencia, FormularioCreaUsuarios
from mainapp.models import FormularioContactoDB, FormularioAsistenciaDB
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class IndexView(TemplateView): 
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'Somos WebConstructores, tú solución de desarrollo web'},)
    
class UsersView(TemplateView):
    template_name = 'home/users.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users, 'titulo' : 'Usuarios'})
    
class CreateUsersView(TemplateView):
    template_name = 'home/createusers.html'

    def get(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        return render(request, self.template_name, {'formulario': form, 'titulo': 'Crear cuenta de usuario',})

    def post(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        if form.is_valid():
            form.save()
            mensajes = {'enviado': True, 'resultado': 'El usuario se ha creado correctamente'}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'titulo': 'Crear cuenta de usuario',})

class ContactView(TemplateView):
    template_name = 'home/contactform.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioConsulta()
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Formulario de contacto',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioConsulta(request.POST)
        mensajes = {
            'enviado' : True,
            'resultado': None
        }
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            registro = FormularioContactoDB(
                nombre = nombre,
                email = email,
                asunto = asunto,
                mensaje = mensaje,
            )
            registro.save()
            mensajes = {'enviado': True, 'resultado': 'Hemos recibido el formulario correctamente, y pronto nos pondremos en contacto.', 'titulo': 'Formulario de contacto',}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'titulo': 'Formulario de contacto',})


class LoginView(TemplateView):
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Acceso al sitio Interno',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('internalindex')
            form.add_error('username', 'Se han ingresado las credenciales equivocados.')
            return render(request, self.template_name, { 'form': form, 'titulo': 'Acceso al sitio Interno',})
        else:
            return render(request, self.template_name, { 'form': form, 'titulo': 'Acceso al sitio Interno',})
        
class IndexInternoView(TemplateView):
    template_name = 'interno/index.html'
    
    def get(self, request, *args, **kwargs):
        primer_nombre = request.user.first_name or 'usuario'
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {'primer_nombre' : primer_nombre, 'segundo_nombre' : segundo_nombre, 'titulo': f'Hola {primer_nombre} {segundo_nombre} 👋',})


class SupportContactView(TemplateView):
    template_name = 'interno/supportcontactform.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        formulario = FormularioAsistencia()
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Formulario de asistencia',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioAsistencia(request.POST)
        mensajes = {
            'enviado' : True,
            'resultado': None
        }
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            area = form.cleaned_data['area']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            registro = FormularioAsistenciaDB(
                nombre = nombre,
                email = email,
                area = area,
                asunto = asunto,
                mensaje = mensaje,
            )
            registro.save()
            mensajes = {'enviado': True, 'resultado': 'Hemos recibido el formulario correctamente, y pronto nos pondremos en contacto.', 'titulo': 'Formulario de asistencia',}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'titulo': 'Formulario de asistencia',})