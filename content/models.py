from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models
from stdimage import StdImageField, JPEGField


# Create your models here.


class contentInput(models.Model):
    corporate_logo = models.ImageField(upload_to='home_page', verbose_name='Şirket logosu', max_length=255, blank=True,
                                       null=True)
    corporate_main_title = models.TextField(verbose_name='Kurumsal Ana Başlık Açıklama', max_length=500,
                                            blank=True, null=True)
    software_main_title = models.TextField(verbose_name='Yazılımlarımız Üst Ana açıklama', max_length=500, blank=True,
                                           null=True)
    blog_main_title = models.TextField(verbose_name='Blog Üst Ana açıklama', max_length=500, blank=True,
                                       null=True)
    team_main_title = models.TextField(verbose_name='Ekibimiz Üst Ana açıklama', max_length=500, blank=True,
                                       null=True)
    founder_name_surname = models.CharField(verbose_name='Kurucu Adı ve Soyadı', max_length=100, null=True, blank=True)
    founder_link = models.CharField(verbose_name='Kurucu Websitesi link alanı', max_length=150, blank=True, null=True)
    founder_link_name = models.CharField(verbose_name='Kurucu Websiitesi link adı', max_length=150, blank=True,
                                         null=True)
    about_descriptions = RichTextField(verbose_name='Hakkımızda Açıklama', blank=True, null=True)
    about_image = StdImageField(upload_to='home_page/upload_images/about_images', max_length=255,
                                verbose_name='Hakkımızda Resim', blank=True,
                                null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)
    central_address = models.TextField(verbose_name="Merkez Ofis Adres", blank=True, null=True)
    central_phone = models.CharField(verbose_name='Merekez Ofis Telefon', max_length=20, blank=True, null=True)
    central_local_link = models.TextField(verbose_name='Merkez Ofis Konum Linki', null=True, blank=True)
    branch_adress = models.TextField(verbose_name='Şube Ofis Adresi', blank=True, null=True)
    branch_phone = models.CharField(verbose_name='Şube Ofis Telefon', max_length=20, blank=True, null=True)
    branch_local_link = models.TextField(verbose_name='Şube Ofis Konum Linki', null=True, blank=True)
    instagram = models.CharField(verbose_name='Kurum Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Kurum Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name=' Kurum Linkedin Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Kurum Mail Address', max_length=100, blank=True, null=True)

    # def delete(self, using=None, keep_parents=False):
    #     self.founder_image.storage.delete(self.founder_image.name)
    #     super().delete()

    class Meta:
        verbose_name = "Anasayfa Bilgileri"
        verbose_name_plural = 'Anasayfa Bilgileri'


class ImagePost(models.Model):
    main_title = models.CharField(verbose_name='Slider Ana Başlık', max_length=100, blank=True,
                                  null=True)
    sub_title = models.CharField(verbose_name='Slider Alt Başlık', max_length=600, blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255,
                          verbose_name='Slider Resimleri',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = "Slider İçerik Ekle"
        verbose_name_plural = 'Slider İçerik Ekle'


class Team(models.Model):
    name_surname = models.CharField(verbose_name='Ad ve Soyad', max_length=100, blank=True, null=True)
    job = models.CharField(verbose_name='Uğraş Alanı', max_length=100, blank=True, null=True)
    personal_descriptions = models.TextField(verbose_name='Kişi hakkında kısa açıklama', max_length=150, blank=True,
                                             null=True)
    instagram = models.CharField(verbose_name='Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name='Linkedin Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Mail Address', max_length=100, blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/team_image', max_length=255,
                          verbose_name='Slider Resimleri',
                          null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = "Ekip Adaylarını Ekle"
        verbose_name_plural = "Ekip Adaylarını Ekle"


class Blog(models.Model):
    blog_title = models.CharField(verbose_name='Blog Haber Başlığı', max_length=250, blank=True, null=True)
    blog_descriptions = models.TextField(verbose_name='Blog Haber Kısa Açıklaması', max_length=250, blank=True,
                                         null=True)
    blog_date = models.DateField(default=datetime.now())
    blog_link=models.CharField(verbose_name='Haber Linki',max_length=200,blank=True,null=True)
    blog_image = StdImageField(upload_to='home_page/upload_image/blog_image', max_length=255,
                               verbose_name='Slider Resimleri',
                               null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = 'Blog Haberleri Ekle'
        verbose_name_plural = 'Blog Haberleri Ekle'


class Corporate(models.Model):
    front_title = models.CharField(verbose_name='Ana Sayfa Başlığı', max_length=150, blank=True, null=True)
    corporate_description = RichTextField(verbose_name='Açıklama', blank=True, null=True)
    corporate_image = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255,
                                    verbose_name='Kurumsal Resimler',
                                    null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = 'Kurumsal Alanı Bilgileri(Kurucu,Felsefe vb ...)'
        verbose_name_plural = 'Kurumsal Alanı Bilgileri(Kurucu,Felsefe vb ...)'


class Software(models.Model):
    title = models.CharField(verbose_name='Yazılım Başlığı', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Yazılım Açıklaması', blank=True, null=True)
    link = models.CharField(verbose_name='Yazılım web linki', max_length=150, blank=True, null=True)
    software_image = StdImageField(upload_to='home_page/upload_image/software_image', max_length=255,
                                   verbose_name='Kurumsal Resimler',
                                   null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = 'Yazılım Alanı Bilgileri'
        verbose_name_plural = 'Yazılım Alanı Bilgileri'

class sendMessage(models.Model):
    name_surname = models.CharField(verbose_name='Ad Soyad', max_length=150, null=True, blank=True)
    mail = models.EmailField(verbose_name='mail', max_length=150, null=True, blank=True)
    subject = models.CharField(verbose_name='Konu', max_length=150, null=True, blank=True)
    message = models.TextField(verbose_name='Mesaj', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Kullnıcı Mesajları'
        verbose_name_plural = 'Kullnıcı Mesajları'

