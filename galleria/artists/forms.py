from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from artists.models import Artist


class ArtistForm(ModelForm):
    def __init__(self, *args, **kwargs):
          super(ArtistForm, self).__init__(*args, **kwargs)
          self.helper = FormHelper(self)
          self.helper.form_method = 'post'
          self.helper.form_action = '.'
          self.helper.label_class = 'col-lg-2'
          self.helper.field_class = 'col-lg-8'
          self.helper.form_class = 'form-horizontal'
          self.helper.add_input(Submit('submit', 'Submit'))
        
    class Meta:
        model = Artist
