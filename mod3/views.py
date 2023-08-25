from django.http import HttpResponse
from django.shortcuts import render

import json
from pprint import *
from urllib.request import urlopen  # для считывания данных  из внешнего ресурса


def main(request):
    with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
        sourse = response.read()

    data = json.loads(sourse)
    dollar = data['Valute']['USD']['Value']
    euro = data['Valute']['EUR']['Value']
    euro_divided_dollar=round(euro/dollar,2)
    dollar_divided_euro=round(dollar/euro,2)
    return render(request, 'index.html', {'dollar':dollar,'euro_koef':euro_divided_dollar,
                                          'euro':euro, 'dollar_koef':dollar_divided_euro})
