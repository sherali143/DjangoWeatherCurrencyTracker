from django import forms
from .conversion_service import update_exchange_rate

class currencyconversionform(forms.Form):

    amount = forms.FloatField (
        label= 'Amount',
        widget=forms.NumberInput()
    )


    from_country = forms.ChoiceField(
        label="from_country",
        choices=[]
    )
    

    to_country = forms.ChoiceField(
        label="to_country",
        choices=[]
    )


    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        data = update_exchange_rate()

        currencies = data.get('conversion_rates',{})

        choices=[]

        for code,rate in currencies.items():
            choices.append((code,code))
        
        self.fields['from_country'].choices=choices
        self.fields['to_country'].choices=choices
    


   
