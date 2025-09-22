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

### !!!!! makemigrations ==> sometimes does not work so you must pass app names to it to work ==>:
    python manage.py makemigrations app1, app2, ...
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

# Postman
### be carful for using method post. I was using params in postman for sending data that it was wrong and I got error. I should have gone in tab Body then using with raw and send a json format.

# AbstractBaseUser
### every programs need 3 definite fileds ==> password , last_login , is_active because of that django has implemented into it and ERD should be affected by this model and also is_admin for admin panel ==> change ERD!!!

### id field => django will put the type of it to serial (bigintfield) so i want to change it to uuid so i can overwrite it.

### for national_code or phone_number you can not use int field because it may occure 0 at the debut. => use charfield => change ERD.

### USERNAME_FEILD => the field for authentication and must be unique. this is the field when you go to admin pannel and you should fill this field and pssword to be authorized.

### REQUIRED_FEILDS => fields when usin createsuperuser command. BE CARFUL !!!! => this will call the  def create_superuser() in our manager sothese fields you determine into it , are exactly handled over there in manager so the fields must be the same unless error.

### *** when you use createsuperuser command => first you will be asked about USERNAME_FIELD then REQUIRED_FIELDS because of that you cannot have the same value into them:
     USERNAME_FIELD = "national_code"
     REQUIRED_FIELDS = ["national_code", "phone_number"]
     
     # we will get error cause national_code will repeat 2 times in createsuperuser.

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

### AdminPannel
### cause we overwrite User model and this is our custom model we must write all of the custom admin ourselves and unregister the user model was in admin pannel because the last user(for django) in admin does not work.

### for creating and edditing user in admin pannel we need 2 forms to show ==> CreateUserForm - ModifyUserForm

### ValidationError => the error we use in forms for example in clean()

### ReadOnlyPasswordHashField => when to modify forms in admin the user must not see passwords of others or overwriting it, it must be show in a hashed form and readonly. with help_text you can tell info about it and in ../paswword the admin can change the password => it is handeled in django by Reset Password no need to use it.

### def save() ==> if you want to overwrite it, be carful cause it has 2 kinds of overwrite one in ModelForm in forms and one in Model in models and usage of them is diffrent.

### *** Watch out for fieldsets => one fieldset or one add_fieldset can not have same fields:
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "is_active")})

        ("Permissions", {"fields": ("is_active", "is_admin", "last_login")}),
    )

    # here we have error cause 2 times "is_active" is written in 2 fields.

### forms.py => for creating custom inputs to show in admin.py to create our custome user. the label in for example forms.CharField(label='رمز عبور', widget=forms.PasswordInput) is shown in admin pannel. when we want to create our user in admin pannel after clicking to create user in admin pannel => forms.py will be started and if there is any clean() or clean_field() they will be launched. very very important point ===>>> if using clean() you must compare and validate several fields and at the end you must return cleand_data because you are comparing fields. but clean_field() is absoloutly for one field and you must return that field you are validating it. very very important point ===>>> if you use clean() it validate all the fields and if there is an error it shows it at the top of the admin (total error) but in clean_field() like clean_password2() if there is an error in exactly shows bottom of the field that you know that this error is for this form password2 because of it we use any of them is better.
<br>

### admin.py ==> to show our fields which were created in forms.py we must inherit UserAdmin then with form(if we got one form in forms.py) and fieldsets show our inputs. if we got several forms like mine (ModifyUserForm, CreateUserForm) we can add them into add_form and add_fieldsets.
<br>

# DRF
### app_name and namescpace => use them in order not to make confused django for detecting urls(path) if you had apps that their names were same actually you isolate every path with it's name:
    app_name="manage_bank"
    path("registration/", UserRegisterView.as_view(), name="register")
### now if i have this path with this name in another app there is no prob cause I isolated it with app_name
<br>

### models.DecimalField(max_digits=8, decimal_places=0) => you must determine this 2 args for this field
    decimal_places=0 تعداد رقم اعشار
<br>

### serializers ==> it is as same as forms.py (some how) ==> when a user wants to send data(post method) you should validate data with serializers (same in the forms):
    # like def clean()
    def validate(self, data):
        ...
    
    # like def save()
    def create(self, validated_data):
        ...
    
    # like django.core.exceptions.ValidationError
    serializers.ValidationError("...")
### Serializer vs ModelSerialize => exactly like Form and ModelForm => at the first you should write more codes and defiene fields of models into serializers for validating but at two you connect fields of model to serializer no need to handle by hand. !!!!!!!!for each model there may be several serializers. => mine in user     


### very very important point ===>> in serializers i put password instead of password1 why? becasue if i put password1 i got 3 password fields => password1, password2, password(for user model) so i put password that exists just one but in forms.py it is different

### write_only=True ===>this is for the fields which you can only write into them in postman - swager ... but in the result(Response) are not visible. like password field that for the security will not be appeared in Response and it is used with POST-PUT-PATCH

### read_only=True ===> upside down of the write_only. it says that with this arg the field is ignored and you can not put value to this in postman and ... like datetimefield which has auto_now_add or id filed which is auto_increament.

### nested serializers ==> if you had models which got relations with eachothers and you wanted to show all of them in a GET method. like mine:
    class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


    class AccountsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Accounts
            fields = "__all__"

            
    class UserSerializer(serializers.ModelSerializer):
        # must not use password1 because we have password  in user model
        password = serializers.CharField(write_only=True)
        password2 = serializers.CharField(write_only=True)
        
        employee = EmployeeSerializer(read_only=True)
        account = EmployeeSerializer(read_only=True, many=True)

### SerializerMethodField => it has diffrents with above. nested serializers are for showin all the value of fields in models. but in here if you want to show just one field that is customized by you from the mode you have set in model = model_name

### select_related ==> always use for OneToMany or OneToOne fields => using JOIN here and bring all data from one query

### prefetch_related ==> always use for ManyToMany fields and reverse Fk(حرکت از جدول اصلی به جدول فرعی) ==> it usually uses 2 queries(one for data in rel and one for data of main table) why not using join? because in here JOIN for ManyToMany will repeat the rows and not efficient for time and space.


### !!!!!!!!!!!so important about above!!!!!!! ==> when you are going reverse like mine(going from user to employee) and if our relation OneToOne ==> always use select_related. it is a reverse fk but our rel is OneToOne ==>select_related on the other side (going from user to account) again we got reverse fk but our rel is OneToMany so use ==> prefetch_related . * for (going not reverse) use the last rule.