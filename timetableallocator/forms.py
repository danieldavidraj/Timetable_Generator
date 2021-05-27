#-*- coding: utf-8 -*-
from django import forms

class TimeTableForm(forms.Form):
   Class = forms.CharField(max_length = 100)