from django.shortcuts import render, redirect

from apps.products.models import Products,Contact
from apps.setting.models import Setting
# Create your views here.


def course(request):
    setting = Setting.objects.latest('id')
    course = Products.objects.all()
    return render(request, 'course.html', locals())

def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Products.objects.get(id = id)
    return render(request, 'course-detail.html', locals())
def contact(request):
    contact = Contact.objects.all()
    return render(request,'contact.html',locals())

