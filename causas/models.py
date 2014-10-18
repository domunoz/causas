#coding:utf-8
from django.db import models

# Create your models here.
class Persona(models.Model):
	RUT = models.CharField(max_length=144)
	nombre = models.CharField(max_length=144)
	apellido_paterno = models.CharField(max_length=144)
	apellido_materno = models.CharField(max_length=144)

class Procurador(Persona):
	pass

class Asegurado(Persona):
	pass

class Chofer(Persona):
	pass	

class Vehiculo(models.Model):
	patente = models.CharField(max_length=144)
	dueno = models.ForeignKey('Asegurado')

class Tribunal(models.Model):
	nombre = models.CharField(max_length=144)
	comuna = models.CharField(max_length=144)


class Demanda(models.Model):
	TIPO_CHOICES = (
		('R', 'Recupero'),
		('D', 'Defensa'),
		('C', 'Confuso'),
		)
	#data
	numero_de_siniestro = models.IntegerField('SNTRO.', unique=True)
	asegurado = models.ForeignKey('Asegurado', blank=True, null=True)
	ingreso = models.DateField(blank=True, null=True)
	lugar = models.CharField(max_length=144, blank=True, null=True)
	# comuna = models.CharField(max_length=144)
	tribunal = models.ForeignKey('Tribunal', blank=True, null=True)
	rol = models.CharField(max_length=144, unique=True)
	monto = models.FloatField(blank=True, null=True)
	tipo = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICES, blank=True, null=True)
	fecha_siniestro = models.DateField('ACC.', blank=True, null=True)#acc
	fecha_demanda = models.DateField('Demanda', blank=True, null=True)
	notificacion = models.DateField('Notificación', blank=True, null=True)
	pagada = models.BooleanField('PAGADA', default=False)#la notificacion que se paga al actuario
	alcolemia = models.FloatField('Alcoholemia', blank=True, null=True)
	factura = models.BooleanField('FACTURA', default=True)
	carta_de_cobro = models.DateField(blank=True, null=True)
	fecha_comparendo = models.DateField('Comparendo', blank=True, null=True)
	estado = models.TextField(blank=True, null=True)
	
	class Meta:
		verbose_name = 'Causa'

	
	#Notificacion
	#Asegurado
	#Informacion del siniestro
	# patente_vehiculo = models.CharField(max_length=144)
	# chofer = models.CharField(max_length=144)
	#comparendo
	#estado

# class Siniestro(models.Model):
# 	demanda = models.ForeignKey('Demanda')

# class Comparendo(models.Model):
# 	fecha = models.DateField()
# 	demanda = models.ForeignKey('Demanda')


class Documento(models.Model):
	archivo = models.FileField()
	demanda = models.ForeignKey('Demanda')

