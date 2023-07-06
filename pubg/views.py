from django.shortcuts import render, HttpResponse
import pandas as pd


a = [1,2,3]
b = ['a','b','c']

df = pd.DataFrame(a)

# Create your views here.
def index(request):
    return HttpResponse(df)

def show_test(request):
    return render(request, "test.html")

def read(request, id):
    return HttpResponse('Read!'+id)


def search(request):

    who = '''
        <html>
            <head>
                <H1>배그전적검색</H1>
            </head>
            <body></body>
        </html>
    '''
    return HttpResponse(who)