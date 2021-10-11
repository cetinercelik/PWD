from django.urls import path

from content import views

urlpatterns = [
    # Kurumsal bilgiler(Kurucu,Felsefe,Kurumsal Çözümlemeler)
    path('corporate/index/<int:id>', views.corporate_view, name='home-corporate'),
    # Yazılım bilgileri(LearnBetter E-Öğrenme,Eudaimonia Health & Fitness,FitSkill Sağlık & Yetenek Karnesi,Fitness Monitor)
    path('learnbetter/index/<int:id>', views.software_view, name='home-software'),

    # About page url
    path('about/index', views.home_about_view, name='home-about-views'),
    # Home Conatct Url
    path('contact/index', views.home_contact, name='home-contact'),
    path('contact/create', views.contactcreate, name='contact-create'),
    # Home Our team Url
    path('team/index', views.home_team, name='home-team')
]
