from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Ourteam(models.Model):
    name = models.CharField('Full Name', max_length=200, help_text='enter the full name')
    # position = FroalaField(verbose_name='Position', default='', max_length=10000, file_upload=True, image_upload=True)
    position = models.CharField('Position', max_length=1000)
    picture = models.ImageField('Picture', max_length=1000, upload_to='ourteam/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'


class Comment(models.Model):
    name = models.CharField('Full Name', max_length=200, help_text='enter the full name')
    email = models.EmailField('Email Address', max_length=200)
    # subject = models.CharField('Subject', max_length=500, )
    message = models.TextField('Message', max_length=1000, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Comment'
        verbose_name_plural = 'User Comments'


class ContactDetails(models.Model):
    phone = models.CharField('Phone Number', max_length=1000, help_text='Separate with comma if more than 1')
    email = models.EmailField('Email Address', max_length=1000, help_text='Separate with comma if more than 1')

    def __str__(self):
        return ''.format(self.phone, self.email)

    class Meta:
        verbose_name = 'Our Contact Detail'
        verbose_name_plural = 'Our Contact Details'


class News(models.Model):
    newsheading = models.CharField('News Heading', max_length=1000, )
    newscontent = models.TextField(verbose_name='News Content', default='')
    newsdate = models.DateField(auto_now=True)
    newspicture = models.ImageField('Attached Image', upload_to='news/', null=True, blank=True,
                                    help_text='this field is optional', default='../../static/greencare/images/4.jpg')

    def __str__(self):
        return self.newsheading + " On " + str(self.newsdate)

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'News'


class Service(models.Model):
    service_name = models.CharField(max_length=200, verbose_name='Name Of Service',
                                    help_text='enter the name of the service')
    slug = models.SlugField(unique=True)
    button_text = models.CharField('Button Text', max_length=200, default='Hire Us',
                                   help_text='text to appear on the button')

    description = models.TextField(verbose_name='News Content', default='')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        index_together = ('id', 'service_name')

    def __str__(self):
        return self.service_name


class ServicesDeals(models.Model):
    nameofservice = models.ForeignKey(Service, verbose_name='Name Of Service', on_delete=models.CASCADE)
    fullName = models.CharField('Full Name', max_length=200, )
    phoneNumber = models.CharField('Phone Number', max_length=13, help_text='the phone number we shall reach you on')
    email = models.EmailField(null=True, blank=True, help_text='this field is optional')
    description = models.TextField(verbose_name='Description of what you require', null=True, blank=True, default='')
    accepttermsconditions = models.BooleanField(default='True')

    class Meta:
        verbose_name = 'Service Deals'
        verbose_name_plural = 'Service Deals'

    def __str__(self):
        return str(self.fullName)


class TermsAndConditions(models.Model):
    nameofservice = models.ForeignKey(Service, verbose_name='Name Of Service', on_delete=models.CASCADE)
    termsconditions = models.TextField(verbose_name='Terms And Conditions', default='')

    class Meta:
        verbose_name = 'Terms And Condition'
        verbose_name_plural = 'Terms And Conditions'

    def __str__(self):
        return self.nameofservice.service_name


class SocialMediaProfiles(models.Model):
    mediaName = models.CharField('Name Of Media', max_length=200, )
    linkToProfile = models.URLField

    def __str__(self):
        return self.mediaName + ' - ' + str(self.linkToProfile)

class Experience(models.Model):
    heading = models.CharField('Title Of The Experience', max_length=200, null=True, blank=True, help_text='Optional')
    detail = models.TextField('The Actual Detailed Experience')
    imageattached = models.ImageField('Attached Image', upload_to='experience/', null=True, blank=True,
                                    help_text='this field is optional', default='')

    class Meta:
        verbose_name = 'Our Experience'

    def __str__(self):
        return self.heading


class AgroServices(models.Model):
    servicetitle = models.CharField('Service Title', max_length=200)
    servicedetail = models.TextField('Service Details')