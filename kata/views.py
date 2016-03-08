from django.http import HttpResponse
from django.shortcuts import render
import hashlib
from wechat_sdk import WechatConf, WechatBasic

TOKEN = u"ZaiHuiWanSui2015"
APP_ID = u"wxd1ac16e44122c49a"
APP_SECRET = u"d3ddce902a9d3c1f2071eb25f479df33"


# Create your views here.
def index(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']

    conf = WechatConf(
        token=TOKEN,
        appid=APP_ID,
        appsecret=APP_SECRET,
        encrypt_mode="normal"
    )

    wechat = WechatBasic(conf=conf)
    if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        print 'Accept'
    else:
        print 'Wrong'

    return HttpResponse(echostr)
