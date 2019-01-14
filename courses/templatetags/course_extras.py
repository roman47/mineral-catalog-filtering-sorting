from django import template
import string

import random

from courses.models import Mineral

register = template.Library() 

  
@register.simple_tag
def random_mineral_pk():
    """Gets a random primary key from the mineral table"""
    count = Mineral.objects.latest('pk').pk
    random_index = random.randint(0, count - 1)
    return random_index


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list(chosen_letter):
    """Returns dictionary of courses to display as navigation pane"""
    letters = ''.join(sorted(dict.fromkeys(string.ascii_lowercase, 0)))
    return {'letters': letters, 'chosen_letter': chosen_letter}


@register.inclusion_tag('courses/nav_group_list.html')
def nav_group_list(chosen_group):
    """Returns dictionary of courses to display as navigation pane"""
    groups = Mineral.objects.values_list('group', flat=True)\
        .distinct().order_by('group')
    return {'groups': groups, 'chosen_group': chosen_group}


@register.inclusion_tag('courses/nav_color_list.html')
def nav_color_list(chosen_color):
    """Returns dictionary of courses to display as navigation pane"""
    colors = Mineral.objects.\
        values_list('color', flat=True).distinct().order_by('color')
    #import pdb;
    #pdb.set_trace()
    return {'colors': colors,
            'chosen_color': chosen_color}