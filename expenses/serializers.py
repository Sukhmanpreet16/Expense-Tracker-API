from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Expense.CATEGORY_CHOICES)

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'category', 'date']
        read_only_fields = ['date']
