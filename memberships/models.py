from django.db import models
from django.contrib.auth.models import User


class IdDocuments(models.Model):
    passport = 'Passport'
    national_id = 'National Id'
    iqama = 'Iqama'

    DOC_TYPE = (
        (passport, 'Passport'),
        (national_id, 'National Id'),
        (iqama, 'Iqama'),
    )

    id_type = models.CharField(choices=DOC_TYPE, max_length=25,
                               null=False, blank=False)
    id_no = models.CharField(max_length=25, null=False,
                             blank=False)
    f_name = models.CharField(max_length=25, null=False,
                              blank=False)
    l_name = models.CharField(max_length=25, null=False,
                              blank=False)

    expiry_date = models.DateField(null=True)
    issue_date = models.DateField(null=True)

    def __str__(self):
        return self.id_no


class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_document = models.OneToOneField(IdDocuments,
                                       on_delete=models.CASCADE,
                                       primary_key=True, )

    def __str__(self):
        return self.user.username + ' | '\
               + self.id_document.id_no
