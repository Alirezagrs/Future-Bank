from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, national_code,
                    birth_date, home_address, postal_code,
                    register_date, phone_number, education, password
                    ):

        if not all((first_name, last_name, national_code,
                   birth_date, home_address, postal_code,
                   register_date, phone_number, education, password)):

            raise ValueError("required fields empty")

        user = self.model(first_name=first_name, last_name=last_name,
                          national_code=national_code, birth_date=birth_date,
                          home_address=home_address, postal_code=postal_code,
                          register_date=register_date,
                          phone_number=phone_number, education=education)
       
        # filiing password field with hash
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, national_code,
                         birth_date, home_address, postal_code,
                         register_date, phone_number, education, password
                         ):

        user = self.create_user(first_name, last_name, national_code,
                                birth_date, home_address, postal_code,
                                register_date, phone_number, education, password
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user
