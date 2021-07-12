from django                                             import forms
from django.contrib.auth                                import get_user_model
from django.db.models                                   import Q


User = get_user_model()

class UserRegisterForm(forms.ModelForm):

    fullname    = forms.CharField(label='', widget=forms.TextInput(attrs={"title" : "Nom Complet"}),required=True)
    # phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={"onkeypress" : "return onlyNumberKey(event)", "maxlength" : "10"}), required=True)
    # dob = forms.DateField(label='', widget=forms.DateInput(attrs={"title"    : "dob"}),required=True)
    email       = forms.CharField(label='', widget=forms.EmailInput(attrs={"title" : "E-mail Adresse"}),required=True)
    # username  = forms.CharField(label='', widget=forms.TextInput(attrs={"aria-label"    : "Preferred Username"}))
    password    = forms.CharField(label='', widget=forms.PasswordInput(attrs={"title" : "Mot de passe"}),required=True)
    password1   = forms.CharField(label='', widget=forms.PasswordInput(attrs={"title" : "Confirmez le mot de passe"}),required=True)

    class Meta:
        model   = User
        fields  = [
            'fullname',
            # 'phone_number',
            # 'dob',
            # 'birth_place',
            'email',
            # 'username',
        ]

    def clean(self):

        email        = self.cleaned_data.get('email')
        # username     = self.cleaned_data.get('username')
        # phone_number = self.cleaned_data.get('phone_number')
        # username     = username if username else email
        password     = self.cleaned_data.get('password')
        password1    = self.cleaned_data.get('password1')

        if not email:
            raise forms.ValidationError("Le champ e-mail doit être rempli.")

        if not password1:
            raise forms.ValidationError("Veuillez confirmer votre mot de passe.")

        if password and password1 and password != password1:
            raise forms.ValidationError("Vos mots de passe ne correspondent pas.")

        user = User.objects \
            .filter(
                Q(username__iexact  = email) |
                Q(email__iexact     = email)
            ) \
            .exclude(
                # Q(is_active    = False) |
                Q(bool_deleted = True)
            )

        if user:
            raise forms.ValidationError("Ce nom d'utilisateur ou e-mail est déjà utilisé.")

        return self.cleaned_data

    def save(self, commit=True):

        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user


class UserLoginForm(forms.Form):

    email    = forms.CharField(label='', widget=forms.TextInput(attrs={"title" : "Nom d'utilisateur ou email adresse"}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"title" : "Mot de passe"}), required=True)

    def clean_password(self, *args, **kwargs):

        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        username_or_email_final = User.objects \
            .filter(
                Q(username__iexact  = email) |
                Q(email__iexact     = email)
            ) \
            .exclude(
                # Q(is_active     = False) |
                Q(bool_deleted  = True)
            ) \
            .distinct()

        if not username_or_email_final.exists() and username_or_email_final != 1:
            raise forms.ValidationError("Identifiants non valides - L'utilisateur n'existe pas")

        user_obj = username_or_email_final.first()

        if not user_obj.check_password(password):
            raise forms.ValidationError("Les informations d'identification ne sont pas correctes!")

        self.cleaned_data['user_obj'] = user_obj

        return super(UserLoginForm, self).clean(*args, **kwargs)
