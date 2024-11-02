from django.urls import path
from .views import BiasAnalysisCreateListView

urlpatterns = [
    path('bias-analysis/', BiasAnalysisCreateListView.as_view(), name='bias-analysis-list-create'),
]
