from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Company, Vacancy, Category
from .serializers import CompanySerializer, VacancySerializer, CategorySerializer


class CompanyListView(View):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)


class CompanyDetailView(View):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found'}, status=404)
        return JsonResponse(CompanySerializer(company).data, safe=False)


class CompanyVacanciesView(View):
    def get(self, request, id):
        company_name = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company_name)
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)


class CategoryDetailView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)
        return JsonResponse(CategorySerializer(category).data, safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_vacancy_by_id(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    return JsonResponse(VacancySerializer(vacancy).data, safe=False)


def top_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)


