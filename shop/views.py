from django.shortcuts import render, redirect
from django.http import HttpResponse
from shop.models import Men, Women, upload, Cart, Order, update
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
 


def home(request):
    cart_items = Cart.objects.all()
    count = len(cart_items)
   
    return render(request, 'shop/home.html', {'count': count, 'user': request.user})


def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        item_title = Men.objects.filter(iname__icontains = query)
        item_desc = Men.objects.filter(idesc__icontains = query)
        all_items = item_title.union(item_desc)
        
        return render(request, 'shop/search.html', {'all_items':all_items})




def about(request):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    item = upload.objects.all()
    context = {'items': item, 'count': count}
    if request.method == "POST":
        img = request.POST['img']
        print(img)
        ins = upload(img=img)
        ins.save()
    return render(request, 'shop/about.html', context)


def men(request):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    allitems = Men.objects.all()
    
    items = {'products': allitems, 'count': count}

    return render(request, 'shop/men.html', items)


def women(request):
    allitems = Women.objects.all()
    cart_items = Cart.objects.all()
    count = len(cart_items)
    items = {'products': allitems, 'count': count}

    return render(request, 'shop/women.html', items)


def contact(request):
    return HttpResponse("Contact")


def tracker(request):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    orders = Order.objects.all()
    if request.method == "POST":
        item_name = request.POST['item_name']
        cut = Order.objects.filter(iname=item_name)
        cut.delete()

    context = {'orders':  orders}
    return render(request, 'shop/tracker.html', context)


def prodView(request, slu):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    item = Men.objects.filter(slug=slu).first()
    alert = False
    if request.method == "POST":
        ins = Cart(iname=item.iname, idesc=item.idesc,
                   iprice=item.iprice, slug=item.slug, ipic=item.ipic)
        ins.save()
        alert = True
    context = {'item': item, 'alert': alert, 'count': count}
    return render(request, 'shop/product.html', context)


def checkout(request, slug):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    item = Men.objects.filter(slug=slug).first()
    alert = False
    id = 0
    print(item.iname)
    print(item.ipic)
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        a1 = request.POST['address1']
        a2 = request.POST['address2']
        cod = request.POST.get('cod', 'off')
        print(email, password, a1, a1, cod)
        alert = True
        ins = Order(iname=item.iname, ipic=item.ipic, email=email, password=password,
                    a1=a1, a2=a2, cod=alert)
        ins.save()
        id = ins.order_id
        up = update(ord_id=id, update_desc="Your order has been placed")
        up.save()
    context = {'item': item, 'alert': alert, 'id': id, 'count': count}
    return render(request, 'shop/check.html', context)


def cart(request):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    total_amount = 0
    alert = False
    alert1 = False
    crt_items = Cart.objects.all()
    if request.method == "GET":
        item_slug = request.GET.get('piece')
        print(item_slug)
        piece = Cart.objects.filter(slug=item_slug)
        piece.delete()
    for i in crt_items:
        total_amount = total_amount + i.iprice

    if ((request.method == "POST") and (len(crt_items) == 0)):
        alert1 = True

    if request.method == "POST" and len(crt_items) > 0:
        for i in crt_items:
            ins = Order(iname=i.iname, ipic=i.ipic)
            ins.save()
            id = ins.order_id
        up = update(ord_id=id, update_desc="Your order has been placed")
        up.save()
        crt_items.delete()
        alert = True

    context = {'cart': crt_items, 'total': total_amount,
               'alert': alert, 'alert1': alert1, 'count': count}
    return render(request, 'shop/cart.html', context)


def track_info(request, o_id):
    cart_items = Cart.objects.all()
    count = len(cart_items)
    print(o_id)
    print("Hello")
    t = Order.objects.filter(order_id=o_id).first()
    trac = update.objects.filter(ord_id=o_id)

    context = {'t': t, 'trac': trac, 'count': count}

    return render(request, 'shop/track_info.html', context)


def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username = username).first():
            pass
            return redirect('s')
           
        my = User.objects.create_user(username, email, pass1)
        my.first_name = fname
        my.last_name = lname
        my.save()
        return redirect('s')
    return HttpResponse("404 Not Found")

def handlelogin(request):
    if request.method == "POST":
        loginuser = request.POST['loginuser']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username = loginuser, password = loginpassword)
        if user is not None:
            print(user.password)
            login(request,user)
            print("You are succesfully logged in!")
            return redirect('index')
        else:
            HttpResponse('Invalid credentails')

    return HttpResponse("404 Invalid credentials")

def handlelogout(request):
        logout(request)
        return redirect('s')