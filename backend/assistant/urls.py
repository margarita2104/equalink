from django.urls import path
from .views import BiasAnalysisCreateListView, BiasAnalysisDetailView

urlpatterns = [
    path('bias-analysis/', BiasAnalysisCreateListView.as_view(), name='bias-analysis-list-create'),
    path('bias-analysis/<int:pk>/', BiasAnalysisDetailView.as_view(), name='bias-analysis-detail'),
]
