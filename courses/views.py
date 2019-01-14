from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import Mineral
import random


def index(request):
    minerals = Mineral.objects.all()
    rand = random_mineral_pk
    return render(request, 'courses/index.html',
                  {'minerals': minerals, 'rand': rand})


def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    rand = random_mineral_pk
    return render(request, 'courses/detail.html',
                  {'mineral': mineral, 'rand': rand})


def random_mineral_pk():
    """Gets a random primary key from the mineral table"""
    count = Mineral.objects.latest('pk').pk
    random_index = random.randint(0, count - 1)
    return random_index


def single_letter(request, pk="A"):
    minerals = Mineral.objects.filter(name__istartswith=pk)
    rand = random_mineral_pk
    # import pdb;
    # pdb.set_trace()
    return render(request, 'courses/index.html',
                  {'minerals': minerals, 'rand': rand, 'chosen_letter': pk})


def single_group(request, pk="A"):
    minerals = Mineral.objects.filter(group__icontains=pk)
    rand = random_mineral_pk
    # import pdb;
    # pdb.set_trace()
    return render(request, 'courses/index.html',
                  {'minerals': minerals, 'rand': rand, 'chosen_group': pk})


def single_color(request, pk="A"):
    minerals = Mineral.objects.filter(color__icontains=pk)
    rand = random_mineral_pk
    return render(request, 'courses/index.html',
                  {'minerals': minerals, 'rand': rand,
                   'chosen_color': pk})


def search(request):
    """Return list of minerals based on search"""
    rand = random_mineral_pk
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term) |
        Q(image_filename__icontains=term) |
        Q(image_caption__icontains=term) |
        Q(category__icontains=term) |
        Q(formula__icontains=term) |
        Q(strunz_classification__icontains=term) |
        Q(color__icontains=term) |
        Q(crystal_system__icontains=term) |
        Q(unit_cell__icontains=term) |
        Q(cleavage__icontains=term) |
        Q(mohs_scale_hardness__icontains=term) |
        Q(luster__icontains=term) |
        Q(streak__icontains=term) |
        Q(diaphaneity__icontains=term) |
        Q(optical_properties__icontains=term) |
        Q(refractive_index__icontains=term) |
        Q(crystal_habit__icontains=term) |
        Q(specific_gravity__icontains=term) |
        Q(group__icontains=term)
        )
    return render(request, 'courses/index.html',
                  {'minerals': minerals, 'rand': rand})
