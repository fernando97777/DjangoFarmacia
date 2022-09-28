from django.contrib import admin
from django.urls import path
from pastillas.views import medicineView, MedicineListView, ListMedicinePdf, UpdatemedicineView, \
    DeletemedicineView, UpdatListPrescriptionView, DeleteListPrescriptionView,homepageView
from doctors.views import DoctorView, ReportDoctorView, DoctorsListView, ListDoctorsPdf, ReportsView, \
    PrescriptionListView, PrescriptionPdf, UpdateDoctorView, DeleteDoctorView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",homepageView,name="home"),
    path("listamedicamento/", MedicineListView.as_view(), name="lista_medicamentos"),
    path("listadoctor/", DoctorsListView.as_view(), name="list_doctor"),
    path("receta/", PrescriptionListView.as_view(), name="list_prescrition"),
    path("doctor/", DoctorView.as_view(), name="registro_doctor"),
    path("medicamentos/", medicineView.as_view(), name="registro_pastillas"),
    path("reportdoctor/", ReportDoctorView.as_view(), name="report_doctor"),
    path("reportsgeneral/", ReportsView, name="reports"),
    path("reportlistamedicina/", ListMedicinePdf.as_view(), name="report_listmedicine"),
    path("reportlistadoctors/", ListDoctorsPdf.as_view(), name="report_listdoctors"),
    path("reportprescription/", PrescriptionPdf.as_view(), name="report_listprescription"),
    path("updatemedicine/edit/<int:pk>/", UpdatemedicineView.as_view(), name="update_medicine"),
    path("deletemedicine/delete/<int:pk>/", DeletemedicineView.as_view(), name="delete_medicine"),
    path("updatedoctor/edit/<int:pk>/", UpdateDoctorView.as_view(), name="update_doctor"),
    path("deletedoctor/delete/<int:pk>/", DeleteDoctorView.as_view(), name="delete_doctor"),
    path("updatprescription/edit/<int:pk>/", UpdatListPrescriptionView.as_view(), name="update_prescription"),
    path("deleteprescription/delete/<int:pk>/", DeleteListPrescriptionView.as_view(), name="delete_prescription"),
]
