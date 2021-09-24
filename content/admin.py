from django.contrib import admin

# Register your models here.
from content.models import contentInput, ImagePost


class PostImageAdmin(admin.StackedInline):
    model = ImagePost


# @admin.register(ImagePost)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(contentInput)
class HomepageAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    fieldsets = [
        ('Kurucu bilgileri',
         {'fields': ['founder_name_surname', 'founder_image', 'corporate_logo', 'corporate_home_image', 'founder_link_name','founder_link',

                     'title_slider_descriptions', 'founder']}),
        ('Felsefe bilgileri', {'fields': ['philosophy', 'philosophy_image']}),
        ('Kurumsal Çözüm bilgileri', {'fields': ['corporate_solve', 'corporate_image']}),
        ('Ana Başlık Açıklamaları', {'fields': ['corporate_descriptions', 'software_descriptions']}),
        ('Hakkımızda Bilgileri', {'fields': ['about_descriptions', 'about_image']}),
        ('LearnBetter E-Öğrenme bilgileri',
         {'fields': ['learnbetter', 'learnbetter_link', 'learnbetter_link_name', 'learnbetter_image']}),
        ('Eudaimonia Health & Fitness bilgileri',
         {'fields': ['eudaimonia', 'eudaimonia_link', 'eudaimonia_link_name', 'eudaimonia_image']}),
        ('FitSkill Sağlık & Yetenek Karnesi bilgileri',
         {'fields': ['fitskill', 'fitskill_link', 'fitskill_link_name', 'fitskill_image']}),
        ('Fitness Monitor bilgileri', {'fields': ['fitness', 'fitness_link', 'fitness_link_name', 'fitness_image']}),
        ('Merkez Ofis bilgileri',
         {'fields': ['central_email', 'central_phone', 'central_address', 'central_local_link']}),
        ('Şube Ofis bilgileri', {'fields': ['branch_email', 'branch_phone', 'branch_adress', 'branch_local_link']}),
    ]
    list_display = ['founder_name_surname', 'central_phone', 'central_email']
    list_display_links = ['founder_name_surname']

    class Meta:
        model = contentInput
        verbose_name = 'İçerik Yönetimi'
