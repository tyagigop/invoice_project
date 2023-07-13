from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

