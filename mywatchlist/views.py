from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mainpage(request):
    data_movie_mywatchlist = MyWatchList.objects.all()
    output =""
    done = 0
    undone = 0

    for i in data_movie_mywatchlist:
        if (i.watched == False):
            undone+=1
        else:
            done+=1
    
    if done >= undone:
        output += "Selamat, kamu sudah banyak menonton!" 
    else:
        output += "Wah, kamu masih sedikit menonton!"

    context = {
        'nama': 'Katrina Gisella Sembiring',
        'npm':'2106707826',
        'done':done,
        'undone':undone,
        'output':output,
    }

    return render(request, "mainpage.html", context)


def show_mywatchlist(request):
    context = {
        'list_movie': MyWatchList.objects.all(),
        'nama': 'Katrina Gisella Sembiring',
        'npm':'2106707826'
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")