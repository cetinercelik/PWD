from django.shortcuts import render, get_object_or_404

# Create your views here.
from content.models import ImagePost, contentInput


def home(request):
    home_data = contentInput.objects.all()
    template = 'home/index.html'
    home_forms_setting = get_object_or_404(contentInput)
    images_data = ImagePost.objects.all()
    context = {
        'homes': home_data,
        'home_forms': home_forms_setting,
        'images_data': images_data,
    }
    return render(request=request, template_name=template, context=context)


# Kurumsal Alanlar(Kurucu,felsefe,Kurumsal,Çözümlemeler
def home_founder_view(request):
    home_corporate_data = get_object_or_404(contentInput)
    home_founder = contentInput.objects.all()
    template = 'home/corporate.html'
    context = {
        'founders': home_founder,
    }
    return render(request=request, template_name=template, context=context)


def home_philosophy_view(request):
    home_corporate_data = get_object_or_404(contentInput)
    template = 'home/corporate.html'
    context = {
        'id': id,
        'philosophys': home_corporate_data,
    }
    return render(request=request, template_name=template, context=context)


def home_corporate_solve_view(request):
    home_corporate_data = get_object_or_404(contentInput)
    template = 'home/corporate.html'
    context = {
        'id': id,
        'corporate_solves': home_corporate_data,
    }
    return render(request=request, template_name=template, context=context)


def home_learnbetter_view(request):
    home_software_data = get_object_or_404(contentInput)
    template = 'home/software.html'
    context = {
        'learnbetters': home_software_data,
    }
    return render(request=request, template_name=template, context=context)


def home_eudaimonia_view(request):
    home_software_data = get_object_or_404(contentInput)
    template = 'home/software.html'
    context = {
        'eudaimonias': home_software_data,
    }
    return render(request=request, template_name=template, context=context)


def home_fitskill_view(request):
    home_software_data = get_object_or_404(contentInput)
    template = 'home/software.html'
    context = {
        'fitskills': home_software_data,
    }
    return render(request=request, template_name=template, context=context)


def home_fitness_view(request):
    home_software_data = get_object_or_404(contentInput)
    template = 'home/software.html'
    context = {
        'fitness': home_software_data,
    }
    return render(request=request, template_name=template, context=context)


# About page
def home_about_view(request):
    about_data = get_object_or_404(contentInput)
    template = 'home/about.html'
    context = {
        'abouts': about_data,
    }
    return render(request=request, template_name=template, context=context)
