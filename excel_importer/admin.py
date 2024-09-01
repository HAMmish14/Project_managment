from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Phase1,Phase2,Phase3,Phase4,Phase5,Criteria1

@admin.register(Phase1)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('usn', 'name', 'criteria_a','criteria_b','criteria_c','criteria_d','criteria_e','criteria_f','score','year')

@admin.register(Phase2)
class Phase2Admin(ImportExportModelAdmin):
    list_display = ('usn', 'name', 'criteria_a', 'criteria_b', 'criteria_c', 'criteria_d', 'criteria_e', 'score', 'year')

@admin.register(Phase3)
class Phase3Admin(ImportExportModelAdmin):
    list_display = ('usn', 'name', 'criteria_a', 'criteria_b', 'criteria_c', 'criteria_d', 'criteria_e', 'score', 'year')

@admin.register(Phase4)
class Phase4Admin(ImportExportModelAdmin):
    list_display = ('usn', 'name', 'criteria_a', 'criteria_b', 'criteria_c', 'criteria_d', 'criteria_e', 'criteria_f', 'score', 'year')

@admin.register(Phase5)
class Phase5Admin(ImportExportModelAdmin):
    list_display = ('usn', 'name', 'criteria_a', 'criteria_b', 'criteria_c', 'criteria_d', 'score', 'year')

@admin.register(Criteria1)
class CriteriaAdmin(admin.ModelAdmin):
    list_display = ('phase_number','criteria_id', 'criteria_name', 'max_marks')
# Register your models here.
