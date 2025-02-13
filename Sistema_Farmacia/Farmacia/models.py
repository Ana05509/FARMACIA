from django.db import models
from .validador import validar_telefono

class Proveedor(models.Model):
    Nombre = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=10, blank=True, null=True,validators=[validar_telefono])
    email = models.EmailField(unique=True)
    Direccion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.Nombre

class Medicamento(models.Model):
    Nombre = models.CharField(max_length=255)
    Descripcion = models.TextField(blank=True, null=True)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.PositiveIntegerField()
    Fecha_vencimiento = models.DateField()
    
    def __str__(self):
        return f"{self.Nombre} - {self.Proveedor.Nombre}"

class Cliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10, blank=True, null=True,validators=[validar_telefono])
    Email = models.EmailField()
    Direccion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.Nombre

class Venta(models.Model):

    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha_venta = models.DateTimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def calcular_total(self):
        self.Total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.save()
    
    def __str__(self):
        return f"Venta {self.id} - {self.Fecha_venta}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
        self.venta.calcular_total()
    
    def __str__(self):
        return f"{self.medicamento.nombre} - {self.cantidad} unidades"
    
