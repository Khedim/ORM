from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Sum

# Create your views here.

class Example(ListView):
    model = 'Book' # i dont have a model so i put it in single cote
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Example, self).get_context_data(*args,**kwargs)
        context['data'] = 'Book'.objects.aggregate(sum=Sum('rating_count'))
        return context
