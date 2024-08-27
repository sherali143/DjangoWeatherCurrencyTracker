from django.shortcuts import render
from .conversion_service import update_exchange_rate,fetch_weather_data
from .forms import currencyconversionform

# def index(request):
#     data = update_exchange_rate()
#     currency_rate = data.get('conversion_rates',{})
#     base_code = data.get('base_code', 'USD')
#     context = {

#         'currency_rate': currency_rate,
#         'base_code': base_code
#     }
#     return render(request, 'index.html' , context)


def currency_convert(request):
    if request.method == 'POST':
        form = currencyconversionform(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_country = form.cleaned_data['from_country']
            to_country = form.cleaned_data['to_country']


            data = update_exchange_rate()
            currencies = data.get('conversion_rates',{})


            from_rate = currencies[from_country]
            to_rate = currencies[to_country]

            if from_country == 'USA':
                converted_amount = amount * to_rate

            else:
                converted_amount = amount * (to_rate / from_rate)

            return render(request,'getform.html',{

                        'amount':amount,
                        'from_country':from_country,
                        'to_country':to_country,
                        'convert_amount':converted_amount
                        })
        
    else:
        form = currencyconversionform


    return render(request,'getform.html',{'form':form})
    


def weather_update(request):
   city= request.GET.get('city','Pakistan')
   data2 = fetch_weather_data(city)
   return render(request,'weather.html', {'data2':data2})


