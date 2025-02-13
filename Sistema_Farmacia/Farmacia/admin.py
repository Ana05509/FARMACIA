from django.contrib import admin
from .models import Proveedor, Medicamento, Cliente, Venta, DetalleVenta
from import_export import resources
from import_export.admin import ExportMixin, ImportMixin


# Recurso para el modelo Proveedor
class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        fields = ('id', 'Nombre', 'Telefono', 'email', 'Direccion')  # Campos que exportaremos
        export_order = ('id', 'Nombre', 'Telefono', 'email', 'Direccion')

# Recurso para el modelo Medicamento
class MedicamentoResource(resources.ModelResource):
    class Meta:
        model = Medicamento
        fields = ('id', 'Nombre', 'Descripcion', 'Proveedor', 'Precio', 'Stock', 'Fecha_vencimiento')
        export_order = ('id', 'Nombre', 'Descripcion', 'Proveedor', 'Precio', 'Stock', 'Fecha_vencimiento')

# Recurso para el modelo Cliente
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        fields = ('id', 'Nombre', 'Telefono', 'Email', 'Direccion')
        export_order = ('id', 'Nombre', 'Telefono', 'Email', 'Direccion')

# Recurso para el modelo Venta
class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('id', 'Cliente', 'Fecha_venta', 'Total')
        export_order = ('id', 'Cliente', 'Fecha_venta', 'Total')

# Recurso para el modelo DetalleVenta
class DetalleVentaResource(resources.ModelResource):
    class Meta:
        model = DetalleVenta
        fields = ('id', 'venta', 'medicamento', 'cantidad', 'precio_unitario', 'subtotal')
        export_order = ('id', 'venta', 'medicamento', 'cantidad', 'precio_unitario', 'subtotal')


class ProveedorAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = ProveedorResource

class MedicamentoAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = MedicamentoResource

class ClienteAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = ClienteResource

class VentaAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = VentaResource

class DetalleVentaAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = DetalleVentaResource



# Registro de los modelos con sus respectivas configuraciones
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)
