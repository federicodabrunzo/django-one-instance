from django.db import models
from django.utils.translation import gettext_lazy as _

from one_instance.models import SingletonModel


class Config(SingletonModel):

    enabled = models.BooleanField()


class SMTPConfigs(SingletonModel):

    host = models.CharField(max_length=1024 ,
                            verbose_name=_('SMTP Host'))

    port = models.PositiveSmallIntegerField(default=587,
                                            verbose_name=_('SMTP Port'))

    username = models.CharField(max_length=255,                                
                                verbose_name=_('Username'))

    password = models.CharField(max_length=255,                                  
                                verbose_name=_('Password'))

    use_tls = models.BooleanField(default=True,
                                  verbose_name=_('Use TLS'))

    use_ssl = models.BooleanField(default=True,
                                  verbose_name=_('Use SSL'))

    from_email = models.EmailField(verbose_name=_('From Email'))
