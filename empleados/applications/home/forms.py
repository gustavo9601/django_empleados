from django import forms
from .models import Home


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        # Muestra todos los campos =>  ('__all__')
        fields = ('titulo', 'subtitulo', 'cantidad')

        # Personalizando los campos que se renderizaran en el form
        widgets = {
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad', 'class': 'form-control'})
        }

    # clean_<<name_field>>
    # Permite añadir una validacion al campo
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
