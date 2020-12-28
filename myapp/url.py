from django.urls import path
from . import views
app_name = 'myapp'  

urlpatterns = [
    path('', views.hello, name='hello'),
    path('categorise',views.categorise, name='categorise'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('product',views.product, name='product'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('yourcart',views.yourcart, name='yourcart'),
    path('yourorder',views.yourorder, name='yourorder'),
    path('yourcart/removefromcart/<int:item_id>/',views.removefromcart, name='removefromcart'),
    path('buynow',views.buynow,name='buynow'),
    path('order',views.order,name='order'),
    path('yourprofile',views.yourprofile,name='yourprofile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    # path('Buynow',views.Buynow, name='Buynow'),
    # path('Buynow/cancel/<int:item_id>/',views.cancel, name='cancel'),
]
#add path to every html pageyo
