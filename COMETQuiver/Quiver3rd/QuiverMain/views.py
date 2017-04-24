from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from QuiverMain.forms import (UserCreationForm, UserProfileForm, EmailAuthenticationForm, ProjectFileForm,
                              UserForm, AddTagsForm, ProjectDetailsForm, BaseTagFormSet)
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import auth
from django.contrib.auth.models import User
from QuiverMain.models import UserProject, ProjectFile, Project, Tag
from QuiverMain.forms import AddTagsForm

@login_required
def portfolio_view(request):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        if request.method == 'POST':
            portfolio_details_form = ProjectDetailsForm(request.POST)
            print(portfolio_details_form.errors)
            print(portfolio_details_form.is_valid)
            print('Details End')
            if portfolio_details_form.is_valid():
                portfolio_detail_instance = portfolio_details_form.save(commit=False)
                portfolio_detail_instance.save()
                userportfolio_instance = UserProject()
                userportfolio_instance.user = request.user
                userportfolio_instance.portfolio = portfolio_detail_instance
                userportfolio_instance.save()
            return HttpResponseRedirect('/homescreen/')
        else:
            portfolio_file_form = ProjectFileForm()
            portfolio_details_form = ProjectDetailsForm()
            tags_form = AddTagsForm()
    else:
        return HttpResponseRedirect("/login/")

    return render(request, 'QuiverMain/portfolio.html', {'portfolio_file_form' : portfolio_file_form,
                                                          'portfolio_details_form' : portfolio_details_form,
                                                          'tags_form' : tags_form})

@login_required
def add_project_view(request):

    #Django Built-in Sessions Key
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        #DB Queries for Project View
        user_projects_queryset = UserProject.objects.filter(user_id=request.user)
        projects_queryset = Project.objects.filter(id__in=user_projects_queryset.values('project_id'))
        tags_queryset = Tag.objects.filter(id__in=user_projects_queryset.values('project_id'))

        TagFormSet = inlineformset_factory(Project, Tag, form=AddTagsForm, extra=1, can_delete=True)
        #Saving Project Detail Forms
        if request.method == 'POST':
            project_file_form = ProjectFileForm(request.POST, request.FILES)
            project_details_form = ProjectDetailsForm(request.POST)

            if project_details_form.is_valid() and project_file_form.is_valid():

                project_detail_instance = project_details_form.save(commit=False)
                project_detail_instance.save()
                project_file_instance = project_file_form.save(commit=False)
                project_file_instance.project = project_detail_instance
                project_file_instance.save()
                tag_formset = TagFormSet(request.POST, instance=project_detail_instance, prefix="tags")
                if tag_formset.is_valid():
                    tag_formset.save()
                userproject_instance = UserProject()
                userproject_instance.user = request.user
                userproject_instance.project = project_detail_instance
                userproject_instance.save()
            return HttpResponseRedirect('/project/')
        else:
            project_file_form = ProjectFileForm()
            project_details_form = ProjectDetailsForm()
            tag_formset = TagFormSet()
    else:
        return HttpResponseRedirect("/login/")
    return render(request, 'QuiverMain/addproject.html', {'project_file_form': project_file_form,
                                                          'project_details_form': project_details_form,
                                                          'tag_formset' : tag_formset,
                                                          'projects': projects_queryset,
                                                          'tags_list': tags_queryset})




@login_required
def view_profile(request, username):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        user = User.objects.get(username=username)
        return render(request, 'QuiverMain/profile.html', {"user": user, "title": 'View Profile'})
    else:
        return HttpResponseRedirect("/login/")



@login_required
def edit_profile(request):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            print(user_form.errors)
            print(user_form.is_valid)
            print(profile_form.errors)
            print(profile_form.is_valid)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect('/homescreen/')
        else:
            user_form = UserForm(instance=request.user)
            profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'QuiverMain/edit_profile.html', {
        'title':'Edit Profile Information',
        'user_form': user_form,
        'profile_form': profile_form,
    })
'''
def edit_profile(request):
    if request.session.has_key('username'):
        request.session['username']
        request.session.set_expiry(18000)
        profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile, prefix="userprofile")
        if request.method == 'POST':
            if profile_form.is_valid():
                instance = profile_form.save(commit=False)
                instance.user = request.user
                instance.save()
                return HttpResponseRedirect('/homescreen/')
        else:
            profile_form = UserProfileForm(prefix="userprofile", instance=request.user.userprofile)
        return render(request, 'QuiverMain/edit_profile.html', {"title": "Edit Profile", "form": profile_form})

    else:
        return HttpResponseRedirect("/login/")
'''

def register_view(request):
    reg_form = UserCreationForm(data=request.POST or None, prefix="user")
    if request.method == 'POST':
        print(reg_form.is_valid())
        if reg_form.is_valid():
            username = reg_form.cleaned_data.get("username")
            email = reg_form.cleaned_data.get("email")
            first_name = reg_form.cleaned_data.get("first_name")
            last_name = reg_form.cleaned_data.get("last_name")
            password1 = reg_form.cleaned_data.get("password1")
            password2 = reg_form.cleaned_data.get("password2")
            user = reg_form.save(commit=False)
            user.save()

            return HttpResponseRedirect('/login/')
    else:
        reg_form = UserCreationForm(prefix="user")
        #messages.error(request, _('Register Unsuccessful'))
    return render(request, 'QuiverMain/register.html', {"title": "Quiver Sign-Up",
                                                      "form": reg_form,})


def login_view(request):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        return HttpResponseRedirect('/homescreen/')
    else:
        form = EmailAuthenticationForm(data=request.POST)
        if request.method == 'POST':

            context = {
                "title": "Quiver Sign-Up",
                "form": form
            }
            print(form.is_valid())
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    print(user)
                    if user.is_active:
                        auth.login(request, user)
                        request.session['username'] = username
                        return HttpResponseRedirect('/homescreen/')
        return render(request, 'QuiverMain/login.html', {
            "title": "Quiver Sign-Up",
            "form": form,
            "next": next,
        })


def logout_view(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect("/login/")


@login_required
def homescreen(request):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        return render(request, "QuiverMain/homescreen.html", {'username': username, 'user': request.user})
    else:
        return HttpResponseRedirect("/login/")
'''
def add_project_view(request):
    if request.session.has_key('username'):
        username = request.session['username']
        request.session.set_expiry(18000)
        form = AddProjectForm(request.POST, request.FILES)
        if request.method == 'POST':
            print(form.errors)
            print(request.user)
            print(form.is_valid())
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return render(request, 'QuiverMain/homescreen.html', {})
        else:
            form = AddProjectForm()
        return render(request, 'QuiverMain/addproject.html', {'user': request.user, 'form': form, })
    else:
        return HttpResponseRedirect("/login/")
'''



