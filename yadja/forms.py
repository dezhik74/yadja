from django import forms

from yadja.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "input"})
        self.fields["image"].widget.attrs.update({"class": "file-input"})
        self.fields["image"].widget.attrs.update(
            {"onchange":  "document.getElementById('file-name').innerHTML= this.files[0].name;"}
        )
