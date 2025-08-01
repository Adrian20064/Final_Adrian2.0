from django import forms

class TravelForm(forms.Form):
    start_city = forms.ChoiceField(choices=[])  
    kilometers = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        cities = kwargs.pop('cities', [])  
        super().__init__(*args, **kwargs)
        city_choices = [(city, city) for city in cities]
        self.fields['start_city'].choices = city_choices