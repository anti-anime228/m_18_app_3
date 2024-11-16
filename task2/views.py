from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def views1(request):
    return render(request, 'func_template.html')


class views2(TemplateView):
    template_name = 'class_template.html'
