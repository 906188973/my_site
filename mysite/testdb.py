from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    # test1 = Test(name='runoob')
    # test1.save()
    Test.objects.create(name='yang')
    return HttpResponse("<p>数据添加成功！</p>")