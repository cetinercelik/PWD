from django.contrib import admin

# Register your models here.
from content.models import contentInput, ImagePost, Team, Blog, Corporate, Software, sendMessage


@admin.register(contentInput)
class HomepageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Kurucu bilgileri',
         {'fields': ['founder_name_surname', 'corporate_logo', 'founder_link_name', 'founder_link']}),
        ('Hakkımızda Bilgileri', {'fields': ['about_descriptions', 'about_image']}),
        ('Ana Başlık bilgileri', {'fields': ['corporate_main_title', 'software_main_title','blog_main_title','team_main_title']}),
        ('Merkez Ofis bilgileri',
         {'fields': ['central_phone', 'central_address', 'central_local_link']}),
        ('Şube Ofis bilgileri', {'fields': ['branch_phone', 'branch_adress', 'branch_local_link']}),
        ('Sosyal Medya bilgileri', {'fields': ['instagram', 'twitter', 'facebook', 'mail']}),
    ]
    list_display = ['founder_name_surname', 'central_phone', 'mail']
    list_display_links = ['founder_name_surname']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Güncelleme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = contentInput
        verbose_name = 'İçerik Yönetimi'


@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ['main_title']
    list_display_links = ['main_title']

    class Meta:
        model = ImagePost
        verbose_name = 'Slider İçerik Ekle'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'job']
    list_display_links = ['name_surname']

    class Meta:
        model = Team
        verbose_name = 'Ekip Bilgilerini Ekle'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title', 'blog_date']
    list_display_links = ['blog_title']

    class Meta:
        model = Blog
        verbose_name = 'Blog Haberleri Ekle'


@admin.register(Corporate)
class corporateAdmin(admin.ModelAdmin):
    list_display = ['front_title']
    list_display_links = ['front_title']

    class Meta:
        model = Corporate
        verbose_name = 'Kurumsal Alanı Bilgileri(Kurucu,Felsefe vb ...)'


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    class Meta:
        model = Software
        verbose_name = 'Yazılım Alanı Bilgileri'


@admin.register(sendMessage)
class sendMessageAdmin(admin.ModelAdmin):
    list_display = ['name_surname','mail','subject']
    list_display_links = ['name_surname']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Güncelleme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_update_permission(self, request):
        return False


    class Meta:
        model = sendMessage
        verbose_name = 'Kullanıcı Mesajları'