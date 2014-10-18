from django.contrib import admin
from .models import *
# Register your models here.

class VehiculoInline(admin.StackedInline):
	model = Vehiculo

class DocumentoInline(admin.StackedInline):
	model = Documento
	extra = 1


#duda con la carta de cobro
class DemandaAdmin(admin.ModelAdmin):
	# fieldsets = (
	# 	(None,{
	# 		'fields':('asegurado', 'ingreso', 'tribunal', 'rol', 'monto', 'tipo'),
	# 		}),
	# 	('Siniestro', {
	# 		'fields':('numero_de_siniestro', 'fecha_siniestro', 'fecha_demanda', 'comuna', 'lugar', 
	# 			'patente_vehiculo','chofer', 'alcolemia'),
	# 		}),
		
	# 	('Notificacion', {
	# 		'fields':('notificacion', 'carta_de_cobro', 'pagada',  'factura' )
	# 		}),
	# 	('Comparendo', {
	# 		'fields':('fecha_comparendo',),
	# 		}),
	# 	('Estado', {
	# 		'fields':('estado',)
	# 		})


	# )
	inlines = [
		DocumentoInline,
	]

admin.site.register(Tribunal)
admin.site.register(Asegurado)
admin.site.register(Demanda, DemandaAdmin)

