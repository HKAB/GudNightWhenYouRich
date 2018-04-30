from __future__ import absolute_import, unicode_literals
from celery import task
import requests
import lxml.html

@task()
def send_message():

    access_token = 'EAAAAUaZA8jlABAGUmbdN9KSuJr9ZBhBpLIsgFUVPmZAQwcUUZB3EsQQa9PKn6S6m0pZCwEpZBngHG1Qxuk0jkkFmAWv0Gcs8xntvhpZCBV9wsPNlOXmTYinCE8WjAp0XBWVcnt3OWcKil5TlGEE4bKcNoFF77h8xmgZD'
    appid = '350685531728'
    s = requests.Session()
    r = s.get('https://api.facebook.com/method/auth.getSessionforApp?access_token=' + access_token +'&format=json&new_app_id=' + appid +'&generate_session_cookies=1')
    cookies = {}
    for key in r.json()['session_cookies']:
        cookies.update({key['name']: key['value']})
    my_id = ""
    id_send = ""
    message = "Ngu ngonnnnnnnnnnn"
    r = s.get('https://m.facebook.com/messages/read/?tid=cid.c.'+ id_send +':' + my_id + "&refid=11#fua", cookies=cookies)
    tree = lxml.html.fromstring(r.content)

    fb_dtsg = tree.xpath('//input[@name="fb_dtsg"]/@value')[0]
    csid = tree.xpath('//input[@name="csid"]/@value')[0]
    payload = "fb_dtsg=" + fb_dtsg +"&body=" + message + "&send=G%E1%BB%ADi&tids=cid.c." + id_send + ":" + my_id +"&wwwupp=C3&ids[" + id_send +"]:" + id_send + "&referrer=&ctype=&cver=legacy&csid=" + csid
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = s.post('https://m.facebook.com/messages/send/?icm=1&refid=12', data=payload, cookies=cookies, headers=headers)
