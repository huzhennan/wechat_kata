from django.http import HttpResponse
from django.shortcuts import render
import hashlib

TOKEN = u"ZaiHuiWanSui2015"


# Create your views here.
def index(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']

    sha1 = hashlib.sha1()
    sha1.update(u''.join(sorted([TOKEN, timestamp, nonce])))
    digest = sha1.hexdigest()

    import pdb
    pdb.set_trace()

    return HttpResponse(echostr)
