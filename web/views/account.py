from django.shortcuts import render
from web.form.account import RegisterModelForm, SendSmsForm
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'web/index.html')

def register(request):
    """注册"""
    if request.method == 'GET':
        form = RegisterModelForm()
        context = {'form': form}
        return render(request, 'web/register.html', context)

    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': True, 'data': 'web/login/'})
    return JsonResponse({'status': False, 'error': form.errors})

def send_sms(request):
    """发送短信"""
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({'status': True})
    print('成功')
    return JsonResponse({'status': False, 'error': form.errors})