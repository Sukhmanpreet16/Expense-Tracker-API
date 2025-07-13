from django.db import models
from users.models import User
import uuid

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "food"),
        ("Movies", "movies"),
        ("Travel", "travel"),
        ("Bills", "bills"),
        ("Other", "other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.category} - ₹{self.amount}"
