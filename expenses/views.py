from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        queryset = Expense.objects.filter(user=user)

        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)

        total = expenses.aggregate(total_amount=Sum("amount"))["total_amount"] or 0

        # Format category breakdown
        category_data = (
            expenses.values("category")
            .annotate(total=Sum("amount"))
            .order_by("category")
        )
        category_breakdown = [
            {"category": entry["category"].capitalize(), "total": entry["total"]}
            for entry in category_data
        ]

        # Trends
        daily = expenses.annotate(day=TruncDay("date")).values("day").annotate(total=Sum("amount"))
        weekly = expenses.annotate(week=TruncWeek("date")).values("week").annotate(total=Sum("amount"))
        monthly = expenses.annotate(month=TruncMonth("date")).values("month").annotate(total=Sum("amount"))

        daily_trend = [
            {"day": entry["day"].strftime("%Y-%m-%d"), "total": entry["total"]}
            for entry in daily
        ]
        weekly_trend = [
            {"week": entry["week"].strftime("Week %U (%Y)"), "total": entry["total"]}
            for entry in weekly
        ]
        monthly_trend = [
            {"month": entry["month"].strftime("%B %Y"), "total": entry["total"]}
            for entry in monthly
        ]

        return Response({
            "total_expense": total,
            "category_breakdown": category_breakdown,
            "daily_trend": daily_trend,
            "weekly_trend": weekly_trend,
            "monthly_trend": monthly_trend,
        })
