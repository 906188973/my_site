from django.shortcuts import render, redirect
from web.form.account import RegisterModelForm, SendSmsForm, LoginSMSForm, LoginForm
from django.http import HttpResponse, JsonResponse
from web import models
from django.db.models import Q



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

def login_sms(request):
    """短信登录"""
    if request.method == 'GET':
        form = LoginSMSForm()
        context = {'form': form}
        return render(request, 'web/login_sms.html', context)
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        #用户输入正确， 登录成功
        mobile_phone = form.cleaned_data['mobile_phone']
        #把用户名写入到session中
        user_object = models.UserInfo.objects.get(mobile_phone=mobile_phone)
        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 14)
        return JsonResponse({"status": True, 'data': "web/"})
    return JsonResponse({"status": False, "error": form.errors})

def login(request):
    """用户名和密码登录"""
    form = LoginForm(request)
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_obj = models.UserInfo.objects.filter(
                Q(email=username)|Q(mobile_phone=username)).filter(
                password=password).first()
            if user_obj:
                #登录成功
                request.session['user_id'] = user_obj.id
                request.session.set_expiry(60 * 60 * 24 * 14)
                return redirect('web:index')
            form.add_error('username', '用户名或密码错误')
    context = {'form': form}
    return render(request, 'web/login.html', context)

def image_code(request):
    """生成图片验证码"""
    from io import BytesIO
    from utils.image_code import check_code

    image_object, code = check_code()

    request.session['image_code'] = code
    request.session.set_expiry(60)

    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.flush()
    return redirect('web:index')