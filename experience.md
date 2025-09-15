# Future Bank
---

# uv
### It is like poetry with crazy speed!!!
<br>

# ruff and pylance extensions
### help you to develope better
### shift + alt + f ==> clean the code but before that enable from vscode settings ==> default formatter and format on save.
<br>

# Django 
### first of all aftar creating a project, seperate manage.py from the folder, moving it to the main route then we have 2 folders into each other (future_banek/future_bank) so remove the inner and move files of that one route before 
<br>

# ERD
### draw.io ===> ER Model
### dbdiagram.io ===> Schema of Model(Tables)
<br>

# Makefile
### The way to define allias for long commands, running them with a short command ==> !!! GNU Make must be installed!!!

### what is .PHONY? => always run the command for example you have:
    makefile
    main:
        pip install django
### If you have had a file like main.py in our project makefile thinks you mean main.py then does nothing. with .PHONY we make it accurate.

### *** use $(value) for dynamic arguments in make:
    make_app:
        # dynamic argument
	    uv run python manage.py startapp $(appname) 
    
    in cmd ===> make make_app appname=somthing
    result ===> uv run python manage.py startapp somthing

<br>


# AbstractBaseUser
### every programs need 3 definite fileds ==> password , last_login , is_active because of that django has implemented into it and ERD should be affected by this model and also is_admin for admin panel ==> change ERD!!!

### id field => django will put the type of it to serial (bigintfield) so i want to change it to uuid so i can overwrite it.

### for national_code or phone_number you can not use int field because it may occure 0 at the debut. => use charfield => change ERD.

### USERNAME_FEILD => the field for authentication and must be unique. this is the field when you go to admin pannel and you should fill this field and pssword to be authorized.

### REQUIRED_FEILDS => fields when usin createsuperuser command.

### *** when you use createsuperuser command => first you will be asked about username_field then required_fields 

### def has_perm(self, perm, obj=None): return True ==> this field is for permisions but we implement them other place just write it for oop rules.

### def has_module_perms(self, app_label): return True ==> if users access models or not

### def is_staff(self): return self.is_admin ==> if a user can access admin pannel.

### AUTH_USER_MODEL => to show django this is our custom model cause it know nothing about it => put into settings.

### BaseUserManager => this is a subcalss of models.Manager and has been designed for user model jobs. in this situation we must cahnge objects to know how to save our fields for users:
    #save correct email format  
    self.normalize_email()

     # save hashed passwords
    user.set_password(pass)
    ####
    user.save(using=self.db)
### models.Manager => base class of all Managers in django and has duty to overwrite get_queryset() and create custome methods into manager.

### save(using=self.db) => operations of db run in which db connection. when you have multi dbs you must detect which db you mean to get query to.
    1-Users.object.create_user(...)
    2-Users.object.using(db_name).create_user(...)
### in 1 we use default db by using=self.db but in 2 we detect a special db.

### *** you can not use many times from AbstractBaseUser just one time and for my project that I have 2 kinds of user (normal users- employees) I should use relations and have one User model
<br>

# AdminPannel
### cause we overwrite User model and this is our custom model we must write all of the custom admin ourselves and unregister the user model was in admin pannel because the last user(for django) in admin does not work.

### for creating and edditing user in admin pannel we need 2 forms to show ==> CreateUserForm - ModifyUserForm

### ValidationError => the error we use in forms for example in clean()

### ReadOnlyPasswordHashField => when you to modify forms in admin the user must not see passwords of others, it must be show in a hashed form and readonly.

### def save() ==> if you want to overwrite it, be carful cause it has 2 kinds of overwrite one in ModelForm in forms and one in Model in models and usage of them is diffrent.