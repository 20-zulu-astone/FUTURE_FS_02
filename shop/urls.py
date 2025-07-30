from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [

    path('carts/',views.carts,name='carts'),
    path('checkout/',views.checkout,name='checkout'),
    path('home/',views.home,name='home'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    path('success_order/',views.success_order,name='success_order')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)