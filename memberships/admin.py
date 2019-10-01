from django.contrib import admin
from memberships.models import IdDocuments, Members


@admin.register(IdDocuments)
class IdDocumentsAdmin(admin.ModelAdmin):
    # raw_id_fields = ('created_by', 'updated_by',)
    # search_fields = ('name', 'name_ar',)
    pass


@admin.register(Members)
class MemberAdmin(admin.ModelAdmin):
    pass
