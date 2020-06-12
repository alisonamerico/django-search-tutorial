from django.urls import path

from search.cities.views import HomePageView, SearchResultView

urlpatterns = [
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]
