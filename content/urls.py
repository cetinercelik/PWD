from django.urls import path

from content import views

urlpatterns = [
    # Kurumsal bilgiler(Kurucu,Felsefe,Kurumsal Çözümlemeler)
    path('founder/index', views.home_founder_view, name='home-founder-views'),
    path('philosophy/index', views.home_philosophy_view, name='home-philosophy-views'),
    path('corporate_solve/index', views.home_corporate_solve_view, name='home-corporate-solve-views'),

    # Yazılım bilgileri(LearnBetter E-Öğrenme,Eudaimonia Health & Fitness,FitSkill Sağlık & Yetenek Karnesi,Fitness Monitor)
    path('learnbetter/index', views.home_learnbetter_view, name='home-learnbetter-views'),
    path('eudaimonia/index', views.home_eudaimonia_view, name='home-eudaimonia-views'),
    path('fitskill/index', views.home_fitskill_view, name='home-fitskill-views'),
    path('fitness/index', views.home_fitness_view, name='home-fitness-views'),

    #About page url
    path('about/index', views.home_about_view, name='home-about-views'),
]