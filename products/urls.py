
from django.urls import path

from .views import (
    ProductDetailView, 
    ProductListView, 
    product_detail_view, 
    product_list_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailSlugView,

    )


urlpatterns = [
 
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view),

    # path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/<str:slug>/', ProductDetailSlugView.as_view()),

    path('products-fbv/<int:pk>/', product_detail_view),
    # path('products-fbv/<str:slug>/', product_detail_view),

    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),

]

