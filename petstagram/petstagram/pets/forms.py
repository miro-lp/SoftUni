import os
from os.path import join

from django import forms
from django.conf import settings

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user',)
        fields = '__all__'


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def save(self, commit=True):
        db_get = Pet.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_get.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={'readonly': 'readonly'}
            )
        }
