from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from ..atelier import settings

urlpatterns = [
    path('product/', views.ProductCreate.as_view(), name='product-create'),
    path('product/', views.ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/', views.ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/', views.ProductDelete.as_view(), name='product-delete'),
    # category
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('category/<int:pk>/', views.CategoryUpdate.as_view(), name='category-update'),
    path('category/<int:pk>/', views.CategoryDelete.as_view(), name='category-delete'),
    path('admin/', admin.site.urls),
    path('api/v2/inventory/', include('inventory.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
