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
### be carful for using method POST/PUT/PATCH. I was using params in postman for sending data that it was wrong and I got error. I should have gone in tab Body then using with raw and send a json format. data must be sent in body when using these methods.

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

### nested serializers ==> if you had models which got relations with eachothers and you wanted to show all of them in a GET method. like mine: !!!!!! so important!!!!! whatever you have defiend for related_name must be exactly in query in selected/prefetch_related and exactly be in variables you defiend in the main serializer.
    #views.py
    class UserGetAllInformationView(APIView):
        def get(self, request):
            users = Users.objects.select_related(
                "employee").prefetch_related('account').all()
            user_serializer = UserGetAllDataSerializer(instance=users, many=True)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    #serializer.py
    class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employees
            fields = "__all__"


    class AccountsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Accounts
            fields = "__all__"

            
    class UserGetAllDataSerializer(serializers.ModelSerializer):
        account = AccountsSerializer(read_only=True, many=True)
        employee = EmployeeSerializer(read_only=True)
        class Meta:
            model = Users
            fields = "__all__"
            extra_kwargs = {
                "password": {"write_only": True}
            }

    #NOTE ==> the result is not ordered by fields(account employee come after id of user but i wanted come in last). for eing orderd you must define each field urself not using "__all__".
### SerializerMethodField => it has diffrents with above. nested serializers are for showin all the value of fields in models. but in here if you want to show just one field that is customized by you from the mode you have set in model = model_name

### select_related ==> always use for OneToMany or OneToOne fields => using JOIN here and bring all data from one query

### prefetch_related ==> always use for ManyToMany fields and reverse Fk(حرکت از جدول اصلی به جدول فرعی) ==> it usually uses 2 queries(one for data in rel and one for data of main table) why not using join? because in here JOIN for ManyToMany will repeat the rows and not efficient for time and space.


### !!!!!!!!!!!so important about above!!!!!!! ==> when you are going reverse like mine(going from user to employee) and if our relation OneToOne ==> always use select_related. it is a reverse fk but our rel is OneToOne ==>select_related on the other side (going from user to account) again we got reverse fk but our rel is OneToMany so use ==> prefetch_related . * for (going not reverse) use the last rule.

### delete an object of a model => no need to use .save() after delete method. it is safe unlike update or create an obj. also I know all about soft-delete(no need to write):
    # hard-delete specific user
    class UserHardDeleteInformationView(APIView):
        def delete(self, request, pk: UUID):
            user = get_object_or_404(Users, pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

### get_object_or_404(your model, condition like pk=pk) ==> a good function for finding a record in db and if not exists return 404 http error.

### get_or_create(condition like pk=pk) ==> another usful methods of models.it will get the object if youtr condition is true unless create it.

### update an object of a model => UserGetAllDataSerializer(user, data=request.data, partial=True) => in update (put or patch) you must get the model instance as the first arg to serializer in order to detect which object it is working to then data=request.data which comming from user then partial=True for patch update not total update.:
    class UserUpdateInformationView(APIView):
        def patch(self, request, pk: UUID):
            user = get_object_or_404(Users, pk=pk)
            user_serializer = UserGetAllDataSerializer(
                user, data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 # Permissions and Authentication
 ### authentication => users can use my app but can not do anything they want. so for this we need authentication ways that one of is TokenAuthentication that it is in rest_framework it self. rach user after being registered/created must have a token. the process in this way is the user send the created token from his/her device and the token will be checked in the db of the server. if they are the same so user can do anything unless(broken token or not having a token) => 401 error unauthorized user. !!!!!! way of creating token :
    # I prefer these ways
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.authentication import TokenAuthentication
    from rest_framework.authtoken.models import Tokenn
    1-signals
    2-token, created = Token.objects.get_or_create(user=self.user)

    #####
    class UserGetAllInformationView(APIView):
        authentication_classes = [TokenAuthentication,]
        permission_classes = [IsAuthenticated,]

### authentication_classes = [TokenAuthentication,] ==> it wll telling you teh kind of authentications you are using like: JWT, TokenAuthentication, ....<br>when a http req comes to url of this class(view) it will check if a token has been sent or not if token exists: 1- finding the user of that toke (request.user) 2-prepearing othe stuffs(request.auth). how it works? you should send the token in the header of your req and the format in postman is: key=Authorization value=Token \<token> ==> therefore==> this just says us who the user is and if user is a log-in user or not and token must be sent unless error. then ==> {
    request.user,
    request.is_authenticated,
    401 error
}

### permissions_classes => this really does the limitations for the user after detecting if she/he ha logged(authentication_classes) in or not. we built-in pemissions like IsAuthenticated means the user must be logged in or not(403 error permission denied).or we can have our custome permissions.

### custom permissions => for register a user , only employees can do that(like real banks) so i needed custom permissions:

    from rest_framework.permissions import BasePermission

    class UserIsEmployeePermission(BasePermission):
        def has_permission(self, request, view):
            user = request.user
            return user.is_authenticated and hasattr(user, 'employee')
            # 'employee' is what we defiend in related_name


# Transaction
### if a user wants to transactions many important things must be detected.<br>when you send data by method POST/PUT/DELETE/PATCH because they send data in their body you can not get 'em in url anymore and access them by funcion args so:
    def post(self, request):
        pk = request.data.get("pk")
        account_number = request.data.get("account_number")
        amount = int(request.data.get("amount"))
        from_card = request.data.get("from_card")
        to_card = request.data.get("to_card"))

### transaction.atomic() ==> we need this for a transaction because the operation of moving money must be completed(کم کردن از حساب طرف - انتقال به حساب طرف - اضافه شدن موجودی طرف و ....). 

### select_for_update() ==> think a situation that 3 persons want to send money to your account. here we have race condition and shared resource. we must lock field of our account that each transaction done after another gets commencing.وقتی چند کاربر همزمان به یک ردیف دیتابیس دسترسی دارند و می‌خواهند آن را تغییر بدهند، ممکن است race condition پیش بیاید.select_for_update() باعث می‌شود که آن ردیف در طول تراکنش قفل شود و دیگران نتوانند تا پایان تراکنش آن را تغییر دهند.

### how to reach to transaction table in my model?
    User → Accounts → LoanAccount / CurrentAccount → Transactions

    # ❌first I used below that it was wrong ❌
    user_with_l_account = Users.objects.prefetch_related('account').select_related("loan").prefetch_related("l_transaction").get(pk=pk)

    user_with_c_account = Users.objects.prefetch_related('account').select_related("current").prefetch_related("c_transaction").get(pk=pk)


    # this is True way✅✅✅
    # you can not reach loan/current details
    user = Users.objects.prefetch_related(
            'account__loan__l_transaction', #مسیریابی
            'account__current__c_transaction'
        ).get(pk=pk)
    
    
    # modern way of getting each account with loan/current details✅✅
    from django.db.models import Prefetch

    accounts_qs = Accounts.objects.select_related('loan', 'current').prefetch_related(
        'loan__l_transaction', 'current__c_transaction'
    )

    user = Users.objects.prefetch_related(
        Prefetch('account', queryset=accounts_qs)
    ).get(pk=pk)

    یا

    accounts_qs = Accounts.objects.select_related('loan','current') \
    .prefetch_related('loan__l_transaction','current__c_transaction')
    user = Users.objects.prefetch_related(Prefetch('account', accounts_qs)).get(pk=pk)


### the above was not safe for race condition ==> here is the optimized/safe query:
    from django.db.models import Prefetch
    from django.shortcuts import get_object_or_404

    user = get_object_or_404(Users, pk=pk)

    accounts_qs = Accounts.objects.select_related(
            'loan', 'current'
        ).prefetch_related(
            'loan__l_transaction',
            'current__c_transaction'
        )
    
    with transaction.atomic():
        accounts = user.account.select_for_update().prefetch_related(
                Prefetch('account', queryset=accounts_qs)
            ).all()
    
        یا
     with transaction.atomic():
        accounts = user.account.select_for_update().select_related(
                    'loan', 'current'
                ).prefetch_related(
                    'loan__l_transaction',
                    'current__c_transaction'
                ).all()


 ### description of above ==> first you much reach to aacount model(from user to account this is a reverse fk and ontomany => prefetch_related) then you can reach sub model by above exp(this is a total exp). but in wrong exp i wanted to reach transaction by user(transaction is for account and not for user)


### ############################notes############################

### 1- for complex condition(mixed or and) use Q. you can just AND condition in filter or get

### 2- when you say serializer.save() => validate data then create the object in the model it is connected to in model=model_name.

### 3- partial=True => you ahv authority to fill fields you want unless all the fields must be filled out (PUT).

### 4- you can even use field lookup for your relations:
    class Employee(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    
    users = Users.objects.filter(employee__isnull=False)

