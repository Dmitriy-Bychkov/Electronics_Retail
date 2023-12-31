from django.urls import path
from companies.apps import CompaniesConfig
from companies.views import CompanyCreateAPIView, CompanyListAPIView, \
    CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView, ProductCreateAPIView, ProductListAPIView, \
    ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView

app_name = CompaniesConfig.name

urlpatterns = [
    path('create_company/', CompanyCreateAPIView.as_view(),
         name='create_company'),
    path('', CompanyListAPIView.as_view(),
         name='list_companies'),
    path('detail_company/<int:pk>/', CompanyRetrieveAPIView.as_view(),
         name='detail_company'),
    path('update_company/<int:pk>/', CompanyUpdateAPIView.as_view(),
         name='update_company'),
    path('delete_company/<int:pk>/', CompanyDestroyAPIView.as_view(),
         name='delete_company'),

    path('create_product/', ProductCreateAPIView.as_view(),
         name='create_product'),
    path('list_products/', ProductListAPIView.as_view(),
         name='list_products'),
    path('detail_product/<int:pk>/', ProductRetrieveAPIView.as_view(),
         name='detail_product'),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(),
         name='update_product'),
    path('delete_product/<int:pk>/', ProductDestroyAPIView.as_view(),
         name='delete_product'),
]
