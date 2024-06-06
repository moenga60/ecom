from django.urls import path
from core.views import index
from core.views import shop
from core.views import aboutus
from core.views import services
from core.views import blog
from core.views import contactus
from core.views import thankyou
from core.views import checkout

app_name = "core"

urlpatterns = [
    path("", index),
    path("shop/", shop),
    path("aboutus/", aboutus),
    path("services/", services),
    path("blog/", blog),
    path("contactus/", contactus),
    path("thankyou/", thankyou),
    path('checkout/', checkout)
]

