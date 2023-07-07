from django.shortcuts import render, HttpResponse
import pandas as pd
from pubg.Map_service import get_player_data,get_match_telemetries,get_positions_draw,main



data = {'Col1':[1,2,3], 'Col2':['A','B','C']}
df = pd.DataFrame(data)

my_var = "hello stupid guy"

# Create your views here.
def index(request):
    return HttpResponse(df)

def show_test(request):
    # df_html = df.to_html()

    # context = {'my_var':my_var, 'df_html':df_html}

    return render(request ,main() )

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