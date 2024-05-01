from django import forms

# BMI form class
class BMIForm(forms.Form):
    # Height input
    height  = forms.FloatField(required = True,
                                label = "Height (m)", 
                                min_value = 0.30, 
                                max_value = 2.80,
                                widget = forms.NumberInput( 
                                                    attrs={ 'id': 'form_height',
                                                            'step': "0.01"}))
    # Weight input
    weight  = forms.FloatField(required = True, 
                                label = "Weight (Kg)",
                                min_value = 2, 
                                max_value = 350,
                                widget = forms.NumberInput( 
                                                    attrs={ 'id': 'form_weight',
                                                            'step': "0.01"}))