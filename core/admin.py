import os

from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from core.models import PatientData, CollectivePatientData
from .resources import PatientDataResource, CollectivePatientDataResource


@admin.register(PatientData)
class PatientDataAdmin(ImportExportModelAdmin):
    resource_class = PatientDataResource


@admin.register(CollectivePatientData)
class CollectivePatientDataAdmin(ImportExportModelAdmin):
    resource_class = CollectivePatientDataResource


