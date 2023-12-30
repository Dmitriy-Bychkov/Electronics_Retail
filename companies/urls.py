from django.urls import path
from companies.apps import CompaniesConfig
from companies.views import CompanyCreateAPIView, CompanyListAPIView, \
    CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView

app_name = CompaniesConfig.name

urlpatterns = [
    path('create_company/', CompanyCreateAPIView.as_view(),
         name='create_company'),
    path('list_companies/', CompanyListAPIView.as_view(),
         name='list_companies'),
    path('detail_company/<int:pk>/', CompanyRetrieveAPIView.as_view(),
         name='detail_company'),
    path('update_company/<int:pk>/', CompanyUpdateAPIView.as_view(),
         name='update_company'),
    path('delete_company/<int:pk>/', CompanyDestroyAPIView.as_view(),
         name='delete_company'),
]
