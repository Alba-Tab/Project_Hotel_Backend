from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.utils import timezone

class Client(TenantMixin):
    name = models.CharField(max_length=100, help_text="Nombre del hotel/cliente")
    paid_until = models.DateField(null=True, blank=True, help_text="Fecha límite de pago")
    on_trial = models.BooleanField(default=True, help_text="¿Está en período de prueba?")
    created_on = models.DateTimeField(default=timezone.now, help_text="Fecha de creación")
    is_active = models.BooleanField(default=True, help_text="¿Cliente activo?")
    auto_create_schema = True
    
    class Meta:
        verbose_name = "Cliente/Hotel"
        verbose_name_plural = "Clientes/Hoteles"
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.name} ({'Activo' if self.is_active else 'Inactivo'})"
    
    def is_paid_up(self):
        """Verifica si el cliente está al día con los pagos"""
        if not self.paid_until:
            return self.on_trial
        return self.paid_until >= timezone.now().date()

class Domain(DomainMixin):
    """Dominios asociados a cada tenant/cliente"""
    
    class Meta:
        verbose_name = "Dominio"
        verbose_name_plural = "Dominios"
    
    def __str__(self):
        return f"{self.domain} ({'Primario' if self.is_primary else 'Secundario'})"