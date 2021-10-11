from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from content.forms import SendMessageForm
from content.models import ImagePost, contentInput, Corporate, Software, Team, Blog


def home(request):
    home_data = contentInput.objects.all()
    slider_data = ImagePost.objects.all()
    template = 'home/index.html'
    software_data = Software.objects.all()
    corporate_data = Corporate.objects.all()
    blog_data=Blog.objects.all()
    team_data=Team.objects.all()
    context = {
        'homes': home_data,
        'softwares':software_data,
        'sliders': slider_data,
        'corporates': corporate_data,
        'blogs':blog_data,
        'teams':team_data,
    }
    return render(request=request, template_name=template, context=context)


    
# Kurumsal Alanlar(Kurucu,felsefe,Kurumsal,Çözümlemeler
def corporate_view(request, id):
    corporate_data1 = Corporate.objects.filter(id=id)
    corporate_data = Corporate.objects.all()
    software_data=Software.objects.all()
    home_data = contentInput.objects.all()
    template = 'home/corporate.html'
    context = {
        'id': id,
        'corporates1':corporate_data1,
        'corporates': corporate_data,
        'softwares':software_data,
        'homes': home_data,
    }
    return render(request=request, template_name=template, context=context)


def software_view(request,id):
    software_data=Software.objects.all()
    software_filter=Software.objects.filter(id=id)
    corporate_data = Corporate.objects.all()
    home_data = contentInput.objects.all()
    template = 'home/software.html'
    context = {
        'id':id,
        'softwares': software_data,
        'software_filtres':software_filter,
        'corporates': corporate_data,
        'homes': home_data,
    }
    return render(request=request, template_name=template, context=context)



# About page
def home_about_view(request):
    corporate_data = Corporate.objects.all()
    home_data = contentInput.objects.all()
    software_data = Software.objects.all()
    team_data=Team.objects.all()
    template = 'home/about.html'
    context = {
        'abouts': home_data,
        'teams':team_data,
        'softwares': software_data,
        'corporates': corporate_data,
        'homes': home_data,
    }
    return render(request=request, template_name=template, context=context)


def home_contact(request):
    corporate_data = Corporate.objects.all()
    home_data = contentInput.objects.all()
    software_data = Software.objects.all()
    template = 'home/contact.html'
    context = {
        'softwares': software_data,
        'corporates': corporate_data,
        'homes': home_data,
    }
    return render(request=request, template_name=template, context=context)

def contactcreate(request):
    print('************************************Kayıt Başarılı0************************')
    if request.method == 'POST':
        sent_form = SendMessageForm(request.POST)
        print('************************************Kayıt Başarılı1************************')
        if sent_form.is_valid():
            sent_form.save()
            print('************************************Kayıt Başarılı2************************')
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('home-contact')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('***********************************************************************************')
            print(sent_form.errors)
            print('**********************************************************************************')

    return redirect('home-contact')


def home_team(request):
    template = 'home/team.html'
    context = {}
    return render(request=request, template_name=template, context=context)
