from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

import django.contrib.messages as messages
from global_change_lab.models import User, UserProfile
from skills.models import Skill


def front_page(request):
    return render(request, 'front_page.html', {
        'name': 'malthe',
        'skills': Skill.objects.all(),
    })


# TODO: this page is a stub
def shares(request):
    return render(request, 'shares.html', {
        'shares': None, #Skill.objects.all(),
    })


def trainer_dashboard(request):
    return render(request, 'trainer_dashboard.html', {
        'trainingbits': request.user.trainingbit_set.all(),
        'skills': request.user.skill_set.all(),
        # TrainingBit.objects.l
        # 'shares': None, #Skill.objects.all(),
    })


def profile(request, user_id=None):
    if user_id is None:
        user = request.user
    else:
        user = User.objects.get(id__exact=user_id)
    return render(request, 'profile.html', {
        'some_user': user,
        'user_fields': User._meta.get_all_field_names(),
        'profile_fields': UserProfile._meta.get_all_field_names(),
    })


def user_delete(request, user_id):
    user = User.objects.get(id__exact=user_id)

    if user == request.user:
        user.delete()
        messages.success(request, 'Successfully deleted your user.')
    else:
        messages.error(request, 'You do not have permissions to delete this user.')



    return HttpResponseRedirect(reverse('front_page'))
