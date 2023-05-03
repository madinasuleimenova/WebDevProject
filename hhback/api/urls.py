from django.urls import path
from .views import *

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name="listview"),
    path('companies/<int:id>/', CompanyDetailView.as_view(), name="detailview"),
    path('companies/<int:id>/vacancies/', CompanyVacanciesView.as_view(), name="vacancies"),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', get_vacancy_by_id),
    path('vacancies/top_ten/', top_vacancies),
    path('categories/', categories_list),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name="categoryview")
]