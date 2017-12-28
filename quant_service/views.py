# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

from quant_service.models import Stocks_Info, Stock_Data
from util import MyJson
from util.MyJson import MyJSONEncoder


def test(request):
    cnt = Stocks_Info.objects.count()
    f=Stock_Data.objects.first()
    print f.tojson()
    return HttpResponse(json.dumps({'status': 'ok', 'data': f.tojson(), 'cnt': cnt}))

service_url = [
    url(r'^test/', test),
]

