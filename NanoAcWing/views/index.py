#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author @caominghao
# Description @ index.py
# CreateTime @ 2023-09-26 08:18:31

from django.shortcuts import render 

def index(request):
    return render(request, "multiends.web")
