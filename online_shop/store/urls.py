from django.urls import path, include
from .views import (UserProfileViewSet, CategoryListAPIView, CategoryDetailAPIView,
                    SubCategoryListAPIView, ProductDetailAPIView, ProductListAPIView,
                    SubCategoryDetailAPIView, ReviewViewSet, RegisterView, LoginView, LogoutView,
                    CartViewSet, CartItemViewSet, FavoriteViewSet, FavoriteItemViewSet)
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('sub_category/', SubCategoryListAPIView.as_view(), name='sub_category_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='sub_category_detail'),
    path('product/', ProductListAPIView().as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('cart/', CartViewSet.as_view(), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]

