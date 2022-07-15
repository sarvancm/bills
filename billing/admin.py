from django.contrib import admin
from .models import Debtor, Documents, DocumentImage, IntrestAmount, DocumentAmount, PaidUnpaid


# Register your models here.
admin.site.register(Debtor)
admin.site.register(Documents)
admin.site.register(DocumentImage)
admin.site.register(IntrestAmount)
admin.site.register(DocumentAmount)
admin.site.register(PaidUnpaid)

