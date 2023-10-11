from django.shortcuts import render
import requests

def cards(request):
    api_url = 'https://fakestoreapi.com/products'

    response = requests.get(api_url) 

    if response.status_code == 200:
        datas = response.json()
        return render(request, 'card.html', {'data': datas})
    else:
        return render(request, 'error.html', {'error_message': 'API request failed'})



