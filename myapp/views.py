from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import market,Items,Customer,Cart,Buy,Stock
from django.contrib import messages
from django.contrib.auth.models import User,auth #User is the default model for authentication there is no need to create customer table
from django.core.mail import send_mail
#import that class or model here
def hello(request):
    item1=market()
    item1.img='breakfastanddiary.jpg'
    item1.name='Breakfast and diary'
    item2=market()
    item2.img='Babycare.jpg'
    item2.name='Baby needs'
    item3=market()
    item3.img='staples.png'
    item3.name='Staples'
    item4=market()
    item4.img='householdneeds.jpg'
    item4.name='householdneeds'
    item5=market()
    item5.img='personalcare.png'
    item5.name='Personalcare'
    item6=market()
    item6.img='petcare.jpg'
    item6.name='Pet care'
    item7=market()
    item7.img='frozenfood.jpg'
    item7.name='Frozen foods'
    item8=market()
    item8.img='homeandkitchen.jpg'
    item8.name='Home & Kitchen'
    item9=market()
    item9.img='vegetables and fruits.jpg'
    item9.name='Vegetables and Fruits'
    
    #like this objects can be created create object from baby care i will tell u  how item.link can be given
    items=[item1,item2,item3,item4,item5,item6,item7,item8,item9]
    #this is the array of all objects and items array will be passed as a parameter into 1st.html
    items_list=Items.objects.order_by("item_name")
    return render(request,'1st.html',{'items':items,'items_list':items_list})
def categorise(request):
    class_name=request.GET["class_name"]
    Items_list=Items.objects.filter(class_name=class_name)
    return render(request,'categorise.html',{'Items_list':Items_list,'class_name':class_name})
def product(request):
    item_id=request.GET["item_id"]
    Item_info=Items.objects.get(item_id=item_id)
    return render(request,'product.html',{'Item_info':Item_info,'Item_name':Item_info.item_name})
#since 1st.html is an html file we have to render it
#like executing html code define function  for every 
#html
def addtocart(request):
    user=request.session['user']
    item_id=request.GET["item_id"]
    if Cart.objects.filter(user=user,item_id=item_id).exists():
        return redirect('/')
    else:
        Cart.objects.create(user=user,item_id=item_id)
        return redirect('/')
    
def yourcart(request):
    user = request.session['user']
    cart_list=Cart.objects.filter(user=user)
    Item_info=Items.objects.all()
    return render(request,'yourcart.html',{'cart_list':cart_list,'Item_info':Item_info})
def removefromcart(request,item_id):
    user = request.session['user']
    Cart.objects.filter(user=user,item_id=item_id).delete()
    return redirect('/yourcart')
def yourprofile(request):
    user = request.session['user']
    user_info= Customer.objects.get(user=user)
    mobileno=user_info.mobileno
    address=user_info.address
    return render(request,"yourprofile.html",{'mobileno':mobileno,'address':address})
def updateprofile(request):
    user=request.session['user']
    mobileno=request.GET["mobileno"]
    address=request.GET["address"]
    Customer.objects.filter(user=user).update(mobileno=mobileno,address=address)
    email=request.GET['email']
    User.objects.filter(username=user).update(email=email)
    return render(request,'yourprofile.html')
def buynow(request):
    items_id=request.GET["item_id"]
    userquantity=request.GET["userquantity"]
    Item_info=Items.objects.get(item_id=items_id)
    if int(userquantity)%10 == 0:
        price=round(Item_info.price*(int(userquantity)/1000))
    else:
        price=round(Item_info.price*(int(userquantity)))
    if request.session.has_key('user'):
        user = request.session['user']
        user_info= Customer.objects.get(user=user)
        mobileno=user_info.mobileno
        address=user_info.address
        return render(request,"Buynow.html",{'mobileno':mobileno,'address':address,'userquantity':userquantity,'price':price,'Item_info':Item_info})
    else:
        return render(request,"Buynow.html",{'userquantity':userquantity,'price':price,'Item_info':Item_info})

def order(request):
    user = request.session['user']
    item_id=request.GET["item_id"]
    user_quantity=request.GET["user_quantity"]
    price=request.GET["price"]
    mobileno=request.GET["mobileno"]
    address=request.GET["address"]
    email=request.GET["email"]
    transaction_id=request.GET["transaction_id"]
    Buy.objects.create(user=user,item_id=item_id,user_quantity=user_quantity,price=price,mobileno=mobileno,address=address,email=email,transaction_id=transaction_id)
    subject = "My Basket"  
    msg     = "Ordered"
    to      = email
    html_content="<h1>Ordered Successfully</h1>"+"<h3>Quantity: "+user_quantity+"</h3>"+"<h3>Price: "+price+"</h3>"+"<h3>Mobileno: "+mobileno+"</h3>"+"<h3>Address: "+address+"</h3>"+"<h3>Transaction_id: "+transaction_id+"</h3>"
    res     =  send_mail(subject, msg, 'noreplytomybasket@gmail.com',[to], html_message=html_content,fail_silently=False)
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"
    if(res == 1):
        return render(request,'ordersuccess.html')
    else:
        return render(request,'/')
# def ordersuccess(request):
#     return redirect('/')
def yourorder(request):
    user = request.session['user']
    buy_list=Buy.objects.filter(user=user)
    Item_info=Items.objects.all()
    return render(request,'yourorders.html',{'buy_list':buy_list,'Item_info':Item_info})
def signup(request):
    #get the parameters from the form
    if request.method == 'POST':
        username=request.POST["username"]
        pwd=request.POST["pwd"]
        email=request.POST["email"]
        mobileno=request.POST["mobileno"]
        address=request.POST["address"]
        if User.objects.filter(username=username).exists():
            messages.info(request,"Already Registered")
            return redirect('/signup')
        else:
            user=User.objects.create_user(username=username,password=pwd,email=email)
            user.save()
            Customer.objects.create(user=username,mobileno=mobileno,address=address)
            return redirect('/login')
    else:
        return render(request,"signup.html")
    # filter will return one tuple if user already exists
    #customer_verify will have 1 tuple i.e 1 i.e it is true
    #if it empty is i.e 0 i.e false so else condition
    # if this true then only it will go in if condition 
def login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        pwd=request.POST["pwd"]
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            request.session['user'] = username
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('/login')
    else:
       return render(request,'login.html') 
def logout(request):
    try:
        del request.session['user']
    except:
        pass
    auth.logout(request)
    return redirect('/')