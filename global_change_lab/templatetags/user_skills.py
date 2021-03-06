from django import template

register = template.Library()

# A modification of:
# http://stackoverflow.com/questions/17611123/check-if-object-is-in-manytomany-list-in-template
@register.filter(name='is_taking_skill')
def is_taking_skill(user, skill):
    return user.is_taking_skill(skill)

@register.filter(name='has_completed_skill')
def has_completed_skill(user, skill):
    return user.has_completed_skill(skill)

@register.simple_tag
def skill_user_flag_image(skill, user):
    return skill.get_flag_image(user)

@register.filter(name='is_taking_trainingbit')
def is_taking_trainingbit(user, trainingbit):
    return user.is_taking_trainingbit(trainingbit)

@register.filter(name='has_completed_trainingbit')
def has_completed_trainingbit(user, trainingbit):
    return user.has_completed_trainingbit(trainingbit)

# Use it like this:
#
#   {% load user_skills %}
#
#   {% if user|is_taking_skill:skill %}
#     You are currently taking the skill {{skill.name}}!
#   {% endif %}
#
#   {% if user|has_completed_skill:skill %}
#     You have completed the skill {{skill.name}}!
#   {% endif %}
