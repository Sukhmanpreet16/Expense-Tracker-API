from django.urls import path
from .views import ExpenseListCreateView, ExpenseAnalyticsView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/analytics/', ExpenseAnalyticsView.as_view(), name='expense-analytics'),
]
