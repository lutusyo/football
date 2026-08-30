from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extral_fields):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), **extral_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extral_fields):
        extral_fields.setdefault("is_staff", True)
        extral_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extral_fields)
