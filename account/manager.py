from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email address"))  
        
    def create_institute(self,email,name,password,id,**extra_fields):
        if email:
           email=self.normalize_email(email) 
           self.email_validator(email)  
        else:
           raise ValueError(_("Email address is required")) 
        if not name:
           raise ValueError(_("Name is required"))
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_verified", True) 
        extra_fields.setdefault("is_active",True)
        institute=self.model(email=email, name=name,id=id,**extra_fields)
        institute.set_password(password)
        institute.save(using=self._db)
        return institute
  

    def create_user(self,email,name,password,institute,**extra_fields):
        if email:
            email=self.normalize_email(email) 
            self.email_validator(email)  
        else:
            raise ValueError(_("Email address is required")) 

        if not name:
            raise ValueError(_("Name is required")) 
        
                
        if not institute:
            raise ValueError(_("Institute name is required"))
        
        user=self.model(email=email, name=name,institute=institute ,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is staff must be true for admin user"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is superuser must be true for admin user"))
        
        if extra_fields.get("is_verified") is not True:
            raise ValueError(_("is verififed must be true for admin user"))
        
        if email:
          email=self.normalize_email(email) 
          self.email_validator(email)  
        else:
          raise ValueError(_("Email address is required"))
        
        user=self.model(email=email, name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


        