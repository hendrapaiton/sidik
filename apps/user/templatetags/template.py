import base64

from django import template
from django.utils.html import format_html

from apps.user.models import Finger

register = template.Library()


@register.simple_tag
def template(value):
    finger = Finger.objects.filter(username__id=value).exists()
    if finger:
        baseurl = 'http://localhost:8000/user/verification'
        data = baseurl + '?user_id=' + str(value)
        data = data.encode('ascii')
        data = base64.b64encode(data)
        data = data.decode('ascii')
        return format_html('<a id="verification" href="finspot:FingerspotVer;' + data + '" class="btn btn-sm btn-success py-0">Login</a>')
    else:
        baseurl = 'http://localhost:8000/user/register'
        data = baseurl + '?user_id=' + str(value)
        data = data.encode('ascii')
        data = base64.b64encode(data)
        data = data.decode('ascii')
        return format_html('<a id="register" href="finspot:FingerspotReg;' + data + '" class="btn btn-sm btn-primary py-0">Register</a>')
