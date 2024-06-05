from django.urls import path
from core.views import index
# from core import views
# from core.views import shop

app_name = "core"

urlpatterns = [
    path("", index)
    # path("", views.core)
    
]

# urlpatterns = [
#     path("/templates/core/shop.html", shop)
# ]