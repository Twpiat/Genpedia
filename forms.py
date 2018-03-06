from django import forms
from .models import *


class AddQuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = '__all__'
        exclude = ('creator',)


class AddDomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = '__all__'

'''
class AddComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class AddEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

'''

class QuestSearchForm(forms.Form):
    name = forms.CharField(label='Nazwa zadania', max_length=32)



'''
class AddCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class AddGuildForm(forms.ModelForm):
    class Meta:
        model = Guild
        fields = '__all__'
'''
