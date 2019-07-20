
from django.urls import path

from .views import (
    ProductListView,
    ProductDetailSlugView,


    # ProductFeaturedDetailView,
    # ProductDetailView,    
    # product_detail_view, 
    # product_list_view,
    # ProductFeaturedListView,
    

    )


urlpatterns = [
 
    path('', ProductListView.as_view()),
    path('<str:slug>/', ProductDetailSlugView.as_view()),


    # path('products-fbv/', product_list_view),
    # path('products-fbv/<int:pk>/', product_detail_view),
    # # path('products-fbv/<str:slug>/', product_detail_view),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),

]

