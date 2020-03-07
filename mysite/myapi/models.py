# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=60)
    alias=models.CharField(max_length=60)

    def _str_(self):
        return self.name
       
      
