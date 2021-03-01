from django.shortcuts import render

# Create your views here.
def hello(request):
    views_list = ["a", "b", "c", "d", "e"]
    A = 1
    B = 1
    return render(request, "PYC01-HTMLJSDemo.html", {"A": A,"B": B})
    # return render(request , "PYC01-HTMLJSDemo.html")

def sy(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "实验.html", {"views_list": views_list})