from django import template
from django.utils.safestring import mark_safe
import string

import random
from django.db.models import Max

from courses.models import Course,Mineral

register = template.Library() 

  
@register.simple_tag
def random_mineral_pk():
      '''Gets a random primary key from the mineral table'''
      count = Mineral.objects.latest('pk').pk
      random_index = random.randint(0, count - 1)
      return random_index


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list(chosen_letter):
    '''Returns dictionary of courses to display as navigation pane'''
    letters = ''.join(sorted(dict.fromkeys(string.ascii_lowercase, 0)))
    #import pdb
    #pdb.set_trace()
    return {'letters': letters, 'chosen_letter': chosen_letter}

