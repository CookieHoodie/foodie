from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from account.models import *
from .models import *

# Create your views here.
@login_required(login_url='/account/login/')
def index(request):
    name = request.user
    try:
        user = Owner.objects.get(name=name)
    except:
        try:
            user = Customer.objects.get(name=name)
        except:
            raise Http404("User not exist")

    if request.method == "POST":
        valid_item = request.POST.get("item_name")
        if valid_item != '':
            return redirect('food:search', {"item_name": valid_item})
        else:
            context = {"name": name, "error_message":"Invalid Keyword"}
            return render(request, 'food/index.html', context)


    context = {"name": name}
    return render(request, 'food/index.html', context)

@login_required(login_url='/account/login/')
def owner_info(request):
    name = request.user
    try:
        user = Owner.objects.get(name=name)
    except:
        raise Http404("User not exist")

    try:
        shop_info = Shop_particulars.objects.get(nric=user.nric)
    except:
        form = "form"
        context = {"form": form}
        return render(request, 'food/owner-info.html', context)

    if request.method == "POST":
        if request.POST.get('item_name'):
            stall_id = request.POST.get('stall_id')
            item_id = request.POST.get('item_id')
            item_name = request.POST.get('item_name')
            item_price = request.POST.get('item_price')
            description = request.POST.get('description')
            recommended_consume_time = request.POST.get('recommended_consume_time')

            menu = Owner(stall_id, item_id, item_name, item_price, description, recommended_consume_time)

            context = {"name": name}
            return render(request, 'food/owner-info.html', context)

        else:
            nric = request.POST.get('nric')
            stall_id = request.POST.get('stall_id')
            stall_name = request.POST.get('stall_name')
            block_no = request.POST.get('block_no')
            street_no = request.POST.get('street_no')
            stall_no = request.POST.get('stall_no')
            postal_cd = request.POST.get('postal_cd')
            country = request.POST.get('country')
            start_operation_time = request.POST.get('start_operation_time')
            end_operation_time = request.POST.get('end_operation_time')
            operation_days = request.POST.get('operation_days')
            country = request.POST.get('country')

def search(request, item_name):
    if request.method == "POST":
        menu = Menu.objects.filter(item_name__unaccent__icontains=item_name)
        context = {"menu": menu}