from django import forms
from .models import SFilm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class FilmForm(forms.Form):
    judul = forms.CharField(label='Judul Film ')
    poster = forms.ImageField(label='Poster Film ')
    trailer = forms.CharField(label='Link Trailer ')
    genre = forms.CharField(label='Genre Film ')
    tahun_rilis = forms.DateField() 

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

class SFilmForm(forms.ModelForm):
    class Meta:
        model = SFilm
        fields = ('judul', 'poster', 'trailer', 'genre', 'tahun_rilis')

class FilmAja(forms.ModelForm):
    class Meta:
        model = SFilm
        fields = "__all__"