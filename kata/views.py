# coding=utf-8
import urllib

from django.http import HttpResponse
from django.shortcuts import render
import hashlib

from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf, WechatBasic
import json

TOKEN = u"ZaiHuiWanSui2015"
APP_ID = u"wxd1ac16e44122c49a"
APP_SECRET = u"d3ddce902a9d3c1f2071eb25f479df33"


# Create your views here.
@csrf_exempt
def index(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']

    conf = WechatConf(
        token=TOKEN,
        appid=APP_ID,
        appsecret=APP_SECRET,
        encrypt_mode="normal"
    )

    wechat = WechatBasic(conf=conf)

    if request.method == "GET":
        echostr = request.GET['echostr']

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            print 'Accept'
        else:
            print 'Wrong'

        return HttpResponse(echostr)
    elif request.method == "POST":
        print request.body
        return HttpResponse("%r" % request.POST)


def _generate_url(base_url, params):
    return base_url + "?" + urllib.urlencode(params) + "#wechat_redirect"


def _wechat_auth_url(redirect_uri):
    params = [
        ('appid', APP_ID),
        ('redirect_uri', redirect_uri),
        ('response_type', 'code'),
        ('scope', 'snsapi_base'),
        ('state', "fack")
    ]
    return _generate_url('https://open.weixin.qq.com/connect/oauth2/authorize', params)


DATA = {
    'button': [
        {
            'type': 'click',
            'name': '今日歌曲',
            'key': 'V1001_TODAY_MUSIC'
        },
        {
            'type': 'click',
            'name': '歌手简介',
            'key': 'V1001_TODAY_SINGER'
        },
        {
            'name': '菜单',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '搜索',
                    'url': _wechat_auth_url('http://www.zaihuiba.com/kata/menu')
                },
                {
                    'type': 'view',
                    'name': '视频',
                    'url': _wechat_auth_url('http://www.zaihuiba.com/kata/menu')
                },
                {
                    'type': 'click',
                    'name': '赞一下我们',
                    'key': 'V1001_GOOD'
                }
            ]
        }
    ]
}


def menu(request):
    if request.method == 'GET':
        return render(request, "menu_form.html", {})
    else:
        data = DATA

        conf = WechatConf(
            tok=TOKEN,
            appid=APP_ID,
            appsecret=APP_SECRET,
            encrypt_mode="normal"
        )
        wechat = WechatBasic(conf=conf)
        ret = wechat.create_menu(DATA)
        return HttpResponse("%r" % ret)


if __name__ == "__main__":
    print _wechat_auth_url("http://www.zaihuiba.com/kata/menu")
