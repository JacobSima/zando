
import os, uuid

# from django_resized                                     import ResizedImageField

from django.conf                                        import settings
from django.db.models.signals                           import post_save, pre_save
from django.dispatch                                    import receiver
from django.db                                          import models
from django.contrib.auth.models                         import BaseUserManager, AbstractBaseUser, \
                                                                User, PermissionsMixin
from django.core.validators                             import RegexValidator

from rest_framework.authtoken.models                    import Token

from zigida.common.global_choices                       import USER_LEVEL, USER_TYPE, LANGUAGES
from zigida.core.model_mixins                           import AddressFields, AuditFields
from zigida.core.utils                                  import randcode_gen


# Create your models here.
USERNAME_REGEX     = '^[a-zA-Z0-9.+-]*$'
PHONE_NUMBER_REGEX = '^[ 0-9]+$'

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#
#     if created:
#         Token.objects.create(user=instance)
#
#     return

def get_filename_ext(filepath):

    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)

    return name, ext

def upload_img_path(instance, filename):

    full_path       = settings.ZIGIDA_DIR
    new_filename    = instance.code
    name, ext       = get_filename_ext(filename)
    finale_filename = f'{new_filename}{ext}'

    if os.path.exists(f"{full_path}/profiles"):
        os.chdir(f"{full_path}/profiles")
        for file in os.listdir("."):
            if os.path.isfile(file) and file.startswith(f"{finale_filename}"):
                try:
                    os.remove(file)
                except Exception as e:
                    print(e)

    return "profiles/{finale_filename}".format(new_filename=new_filename, finale_filename=finale_filename)


class SRUserManager(BaseUserManager):

    def create_client(self, username, fullname, email, password, phone_number=None):

        if not email:
            raise ValueError('Users must have a valid Email Address.')

        if not username:
            username = self.normalize_email(email)

        sr_user = self.model(
            username        = username,
            email           = self.normalize_email(email),
            # phone_number    = phone_number,
            fullname        = fullname,
        )

        sr_user.set_password(password)
        sr_user.save(using=self._db)

        return sr_user

    def create_superuser(self, email, fullname, password, username=None, phone_number=None):

        if not username:
            username = self.normalize_email(email)

        super_user = self.create_client(
            # phone_number    = phone_number,
            fullname        = fullname,
            # dob             = dob,
            password        = password,
            username        = username,
            email           = self.normalize_email(email),
            # id_number       = id_number,
        )

        super_user.user_type    = 1
        super_user.user_level   = 5

        super_user.is_staff     = True
        super_user.is_admin     = True
        super_user.is_superuser = True
        super_user.save(using=self._db)

        return super_user


class SRUser(AddressFields, AuditFields, AbstractBaseUser, PermissionsMixin):

    uuid_code       = models.UUIDField('UUID CODE', primary_key=True, default=uuid.uuid4, editable=False)

    token_key       = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,     blank=True, null=True)
    code            = models.CharField('CODE',          max_length=100,                 blank=False, default=randcode_gen)

    # location        = models.ForeignKey('locations.Location', on_delete=models.PROTECT, related_name='users', null=True)

    username        = models.CharField('USERNAME',          max_length=100, validators=[RegexValidator(regex=USERNAME_REGEX,    message='Username must be alphanumeric or contains numbers.', code='invalid_username')], unique=True)
    phone_number    = models.CharField('PHONE NUMBER',      max_length=30,  validators=[RegexValidator(regex=PHONE_NUMBER_REGEX,message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)

    country_code    = models.CharField('COUNTRY CODE',      max_length=5,               blank=True, null=True)
    fullname        = models.CharField('FULLNAME',          max_length=100,             blank=True, null=True)
    id_number       = models.CharField('PASSPORT NUMBER',   max_length=100,             blank=True, null=True)
    dob             = models.DateField('DATE OF BIRTH',                                 blank=True, null=True)
    birth_place     = models.CharField('BIRTH PLACE',       max_length=200,             blank=True, null=True)
    email           = models.EmailField('EMAIL',            unique=True,                blank=True, null=True)
    profile_pic     = models.ImageField('PROFILE PIC',      upload_to=upload_img_path,  blank=True, null=True)
    language        = models.CharField('LANGUAGE',          max_length=3,               choices=LANGUAGES, default='FR')

    user_type       = models.PositiveSmallIntegerField('USER TYPE',         default=3,  choices=USER_TYPE)
    user_level      = models.PositiveSmallIntegerField('USER LEVEL',        default=1,  choices=USER_LEVEL)

    last_login      = models.DateTimeField('TIME LAST LOGIN', auto_now=True)

    is_active       = models.BooleanField('IS ACTIVE CHECK',            default=False)
    is_staff        = models.BooleanField('IS STAFF CHECK',             default=False)
    is_admin        = models.BooleanField('IS ADMIN CHECK',             default=False)
    is_superuser    = models.BooleanField('IS SUPERUSER CHECK',         default=False)

    objects = SRUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'fullname']

    class Meta:

        app_label   = 'sr_users'
        db_table    = 'sr_users'
        verbose_name_plural = 'sr_users'

    def __str__(self):
        return self.username

    # @property
    # def get_location(self):
    #     return self.location.city

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


# @receiver(pre_save, sender=sruser)
# def username_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.username:
#         instance.username = instance.phone_number
