from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from doctors.forms import ReportDoctorForm
from doctors.models import ReportDoctor
from pastillas.utils import render_to_pdf
from datetime import datetime
from pastillas.forms import medicineForm
from pastillas.models import medicine

def homepageView(request):
    return render(request,'pastillas/home_page.html')


#mostramos los datos ingresados
class MedicineListView(ListView):
    model = medicine
    template_name = "list_medicine.html"
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medicamentos'
        return context


#reporte PDF de medicina
class ListMedicinePdf(View):
    def get(self, request, *args, **kwargs):
        medi = medicine.objects.all()
        data = {
            'medic': medi,
            'date': datetime.now(),
        }
        pdf = render_to_pdf('reportlistmedicinePdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#formulario de registro de las medicinas
class medicineView(CreateView):
    model = medicine
    form_class = medicineForm
    template_name = 'medicine.html'
    success_url = reverse_lazy('lista_medicamentos')

    def post(self, request, *args, **kwargs):
        form = medicineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form']= form
        return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#actualizar los datos de las medicinas
class UpdatemedicineView(UpdateView):
    model = medicine
    form_class = medicineForm
    template_name = 'medicine.html'
    success_url = reverse_lazy('lista_medicamentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Medicina"
        context['action'] = 'edit'
        return context


#eliminar un registro
class DeletemedicineView(DeleteView):
    model = medicine
    template_name = 'deletemedicine.html'
    success_url = reverse_lazy('lista_medicamentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Medicina"
        return context

#actualizar listado recetas
class UpdatListPrescriptionView(UpdateView):
    model = ReportDoctor
    form_class = ReportDoctorForm
    template_name = 'reportMedicine.html'
    success_url = reverse_lazy('list_prescrition')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Medicina"
        context['action'] = 'edit'
        return context


#eliminar un registro listado recetas
class DeleteListPrescriptionView(DeleteView):
    model = ReportDoctor
    template_name = 'deletemedicine.html'
    success_url = reverse_lazy('list_prescrition')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Medicina"
        return context

