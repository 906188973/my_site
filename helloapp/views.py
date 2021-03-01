from django.http import HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings


def hello(request):
    return HttpResponse("Hello World! I am coming...")

def sms(request):
    """发送短信
        ？tpl=login -> 873640
        ?tpl=register -> 873641
    """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')
    code = random.randrange(1000, 9999)
    res = send_sms_single(18067066338, 873641, [code,])
    if res['result'] == 0:
        return HttpResponse("发送成功")
    else:
        return HttpResponse(res['errmsg'])