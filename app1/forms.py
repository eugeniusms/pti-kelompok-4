from django import forms
from django.forms import ModelForm
from .models import SFilm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class FilmForm(forms.Form):
    judul = forms.CharField(label='Judul Film ')
    poster = forms.ImageField(label='Poster Film ')
    trailer = forms.CharField(label='Link Trailer ')
    genre = forms.CharField(label='Genre Film ')
    tahun_rilis = forms.CharField() 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'judul', 
            'poster', 
            'trailer',
            'genre',
            'tahun_rilis',
            Submit('submit', 'Submit', css_class="btn-success")

        )

class SFilmForm(ModelForm):
    class Meta:
        model = SFilm
        fields = ('judul', 'poster', 'trailer', 'genre', 'tahun_rilis')
