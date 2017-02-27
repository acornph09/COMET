from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from QuiverMain.models import UserProfile
from django.forms import extras
from QuiverMain.models import ProjectFile, Project, Tag, UserProject


class AddTagsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(AddTagsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tag
        fields = ('tag_name',)


class ProjectDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProjectDetailsForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['project_description'].required = False

    class Meta:
        model = Project
        fields = ('project_name', 'project_description',)

#Fix Project Field
class ProjectFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProjectFileForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now

    class Meta:
        model = ProjectFile
        fields = ('project_file',)
        #widgets = {"project": forms.FileInput(attrs={'multiple': True})}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=extras.SelectDateWidget)
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['school'].required = False
        self.fields['degree'].required = False
        self.fields['mobile_number'].required = False
        self.fields['telephone_number'].required = False
        self.fields['birth_date'].required = False
        self.fields['gender'].required = False
        self.fields['bio'].required = False
        self.fields['profile_picture'].required = False

    class Meta:
        model = UserProfile
        fields = ('school', 'degree', 'mobile_number', 'telephone_number', 'birth_date', 'gender', 'bio',
                  'profile_picture',)


class EmailAuthenticationForm(AuthenticationForm):
    error_css_class = "login"
    error_messages = {
        'invalid_login': _("Invalid Username/Email and Password!"),
        'inactive': _("This account is inactive."),
        'required': _("This field is required."),
    }

    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except ObjectDoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username':self.username_field.verbose_name},
                )
        return username


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'%s already exists' % username)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered!")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered!")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data




    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'is_active')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
