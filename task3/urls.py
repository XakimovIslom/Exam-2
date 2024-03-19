from django.urls import path

from task3 import views

urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("product-list-encrypted/", views.ProductListEncryptedView.as_view()),
    path('decrypt-product-list/', views.DecryptProductList.as_view()),
]
