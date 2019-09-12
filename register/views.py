from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo


# Create your views here.
def register_page(request):
    return render(request, 'register_page.html')


def register(request):
    if request.method == "GET":
        return HttpResponse("请求错误！")

    if request.method == "POST":
        try:
            import json
            s = json.loads(request.body.decode())

            name = s["name"]
            stu_id = s["stu_id"]
            major = s["major"]
            qq = s["qq"]
            phone = s["phone"]
            something = s["something"]

            print(name, stu_id, major, qq, phone, something)

            UserInfo.objects.create(
                name=name,
                stu_id=stu_id,
                major=major,
                qq=qq,
                phone=phone,
                something=something
            )
        except Exception as e:
            return HttpResponse("信息错误！请重新填写！")

        return HttpResponse("注册OK啦~")

    return HttpResponse("请求错误！")
