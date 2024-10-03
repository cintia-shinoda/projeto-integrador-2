from django.contrib import admin
from .models import Vouchers

# Register your models here.
class VouchersAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tel', 'voucher', 'dataCadastro')

admin.site.register(Vouchers, VouchersAdmin)