import random
import itertools

from django.http import HttpResponse


def cpu_view(request):
    random_numbers = [random.randint(1, 100) * random.randint(300, 6000) for x in range(600000)]
    itertools.permutations(random_numbers)
    return HttpResponse('<h1>Page was found</h1>')