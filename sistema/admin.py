from django.contrib import admin

from sistema.models import *


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Profissional)
admin.site.register(Servico)
admin.site.register(Agendamento)
admin.site.register(Pagamento)