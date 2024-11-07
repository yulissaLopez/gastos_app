from django.contrib.auth.base_user import BaseUserManager

"Manager personalizado para definir email como el username"
class UsuarioManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Para crear y guardar el usuario con email y contraseña"""
        if not email:
            raise ValueError("Email obligatorio")
        
        email = self.normalize_email(email)

        #Asigno el valor de la var email al del campo email de mi modelo Usuario, para crear una instacia del modelo usando el email y los otros campos
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("El atributo is_staff debe ser True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("El atributo is_superuser debe ser True."))
        return self.create_user(email, password, **extra_fields)