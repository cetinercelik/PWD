from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class contentInput(models.Model):
    corporate_logo = models.ImageField(upload_to='home_page', verbose_name='Şirket logosu', max_length=255, blank=True,
                                       null=True)
    corporate_descriptions = models.TextField(verbose_name='Kurumsal Üst Ana Açıklama', max_length=500, blank=True,
                                              null=True)
    corporate_home_image = models.ImageField(upload_to='home_page',
                                             verbose_name='Anasayfa Kurumsal Resim',
                                             max_length=255,  null=True)
    title_slider_descriptions = models.CharField(verbose_name='Slider Resim Alt Başlık', max_length=200, blank=True,
                                                 null=True)
    founder_name_surname = models.CharField(verbose_name='Kurucu Adı ve Soyadı', max_length=100, null=True, blank=True)
    founder_link = models.CharField(verbose_name='Kurucu Websitesi link alanı', max_length=150, blank=True, null=True)
    founder_link_name = models.CharField(verbose_name='Kurucu Websiitesi link adı', max_length=150, blank=True,
                                         null=True)
    founder = RichTextField(verbose_name='Kurucu Açıklama', blank=True, null=True)
    founder_image = models.ImageField(upload_to='home_page', max_length=255,
                                      verbose_name='Kurucu Fotoğrafı',
                                      blank=True,
                                      null=True)
    software_descriptions = models.TextField(verbose_name='Yazılımlarımız Üst Ana açıklama', max_length=500, blank=True,
                                             null=True)
    philosophy = RichTextField(verbose_name='Felsefe Açıklama', blank=True, null=True)
    philosophy_image = models.ImageField(upload_to='home_page', max_length=255,
                                         verbose_name='Felsefe Resim',
                                         blank=True,
                                         null=True)
    corporate_solve = RichTextField(verbose_name='Kurumsal Çözümler', blank=True, null=True)
    corporate_image = models.ImageField(upload_to='home_page', max_length=255,
                                        verbose_name='Kurumsal Çözümler',
                                        blank=True,
                                        null=True)
    learnbetter = RichTextField(verbose_name='LearnBetter E-Öğrenme', blank=True, null=True)
    learnbetter_link = models.CharField(verbose_name='LearnBetter Link Alanı', max_length=300, blank=True, null=True)
    learnbetter_link_name = models.CharField(verbose_name='Learnbetter link adı', max_length=150, blank=True, null=True)
    learnbetter_image = models.ImageField(upload_to='home_page', max_length=255,
                                          verbose_name='LearnBetter E-Öğrenme',
                                          null=True)
    eudaimonia = RichTextField(verbose_name='Eudaimonia Health & Fitness', blank=True, null=True)
    eudaimonia_link = models.CharField(verbose_name='Eudaimonia Link Alanı', max_length=300, blank=True, null=True)
    eudaimonia_link_name = models.CharField(verbose_name='Eudaimonia link adı', max_length=150, blank=True, null=True)
    eudaimonia_image = models.ImageField(upload_to='home_page', max_length=255,
                                         verbose_name='Eudaimonia Health & Fitness',
                                         null=True)
    fitskill = RichTextField(verbose_name='FitSkill Sağlık & Yetenek Karnesi', blank=True, null=True)
    fitskill_link = models.CharField(verbose_name='FitSkill Link Alanı', max_length=300, blank=True, null=True)
    fitskill_link_name = models.CharField(verbose_name='FitSkill link adı', max_length=150, blank=True, null=True)
    fitskill_image = models.ImageField(upload_to='home_page', max_length=255,
                                       verbose_name='FitSkill Sağlık & Yetenek Karnesi',
                                       null=True)
    fitness = RichTextField(verbose_name='Fitness Monitor', blank=True, null=True)
    fitness_link = models.CharField(verbose_name='Fitness Link Alanı', max_length=300, blank=True, null=True)
    fitness_link_name = models.CharField(verbose_name='Fitness link adı', max_length=150, blank=True, null=True)
    fitness_image = models.ImageField(upload_to='home_page', max_length=255,
                                      verbose_name='Fitness Monitor',
                                      null=True)
    about_descriptions = RichTextField(verbose_name='Hakkımızda Açıklama', blank=True, null=True)
    about_image = models.ImageField(upload_to='home_page', max_length=255,
                                    verbose_name='Hakkımızda Resim',blank=True,
                                    null=True)
    central_address = models.TextField(verbose_name="Merkez Ofis Adres", blank=True, null=True)
    central_phone = models.CharField(verbose_name='Merekez Ofis Telefon', max_length=20, blank=True, null=True)
    central_email = models.EmailField(verbose_name="Merekez Ofis Email", null=True, blank=True)
    central_local_link = models.TextField(verbose_name='Merkez Ofis Konum Linki', null=True, blank=True)
    branch_adress = models.TextField(verbose_name='Şube Ofis Adresi', blank=True, null=True)
    branch_phone = models.CharField(verbose_name='Şube Ofis Telefon', max_length=20, blank=True, null=True)
    branch_email = models.EmailField(verbose_name='Şube Ofis Email', blank=True, null=True)
    branch_local_link = models.TextField(verbose_name='Şube Ofis Konum Linki', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.corporate_home_image.storage.delete(self.corporate_home_image.name)
        self.founder_image.storage.delete(self.founder_image.name)
        super().delete()

    class Meta:
        verbose_name = "Anasayfa Bilgileri"
        verbose_name_plural = 'Anasayfa Bilgileri'


class ImagePost(models.Model):
    home = models.ForeignKey(to=contentInput, verbose_name="Slider Resimleri", on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    title = models.CharField(verbose_name='Slider Resim Ana Başlıkları', max_length=100, blank=True,
                             null=True)
    image = models.ImageField(upload_to='home_page', max_length=255, verbose_name='Slider Resimleri',
                              null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider Resim Ekle"
        verbose_name_plural = 'Slider Resim Ekle'
