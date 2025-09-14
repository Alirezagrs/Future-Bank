# Future Bank
---

# uv
### It is like poetry with crazy speed!!!
<br>

# ruff and pylance extensions
### help you to develope better
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

### USERNAME_FEILD => the field for authentication and must be unique.

### REQUIRED_FEILDS => fields when usin createsuperuser command.

### def has_perm(self, perm, obj=None): return True ==> this field is for permisions but we implement them other place just write it for oop rules.

### def has_module_perms(self, app_label): return True ==> if users access models or not

### def is_staff(self): return self.is_admin ==> if a user can access admin pannel.

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

### *** you can use many times from AbstractBaseUser just one time and for my project that I have 2 kinds of user (normal users- employees) I should use relations and have one User model