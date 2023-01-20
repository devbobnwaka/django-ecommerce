from django.db import models
from order.models import Order
import secrets

# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ref = models.CharField(max_length=200)
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)


    def amount_value(self) -> int:
        return self.amount *100


