from django.urls import path
from .views import ExcelToJsonView, JsonToExcelView

urlpatterns = [
    path('convert/excel-to-json/', ExcelToJsonView.as_view(), name='excel-to-json'),
    path('convert/json-to-excel/', JsonToExcelView.as_view(), name='json-to-excel'),
]