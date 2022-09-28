from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, UpdateView, DeleteView
from datetime import datetime
from doctors.forms import DoctorForm, ReportDoctorForm
from doctors.models import Doctors,ReportDoctor
from pastillas.utils import render_to_pdf


class DoctorsListView(ListView):
    model = Doctors
    template_name = "listDoctors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Doctores'
        return context


class PrescriptionListView(ListView):
    model = ReportDoctor
    template_name = "PrescriptionView.html"


#reporte PDF
class ListDoctorsPdf(View):
    def get(self, request, *args, **kwargs):
        doc = Doctors.objects.all()
        data = {
            'doc': doc,
            'date': datetime.now(),
            'user': User
        }
        pdf = render_to_pdf('reportDoctorPdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#reporte PDF
class PrescriptionPdf(View):
    def get(self, request, *args, **kwargs):
        repor = ReportDoctor.objects.all()
        data = {
            'repor': repor,
            'date': datetime.now(),
        }
        pdf = render_to_pdf('PrescriptionPdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DoctorView(CreateView):
    model = Doctors
    form_class = DoctorForm
    template_name = 'adddoctors.html'
    success_url = reverse_lazy('list_doctor')

    def post(self, request, *args, **kwargs):
        form = DoctorForm(request.POST)
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


class ReportDoctorView(CreateView):
    model = ReportDoctor
    form_class = ReportDoctorForm
    template_name = 'reportMedicine.html'

    success_url = reverse_lazy('list_prescrition')

    def post(self, request, *args, **kwargs):
        form = ReportDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def ReportsView(request):
    return render(request,"pastillas/reportsGeneral.html")


#actualizar los datos de medicos
class UpdateDoctorView(UpdateView):
    model = Doctors
    form_class = DoctorForm
    template_name = 'adddoctors.html'
    success_url = reverse_lazy('list_doctor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Doctor"
        context['action'] = 'edit'
        return context


#eliminar un Medico
class DeleteDoctorView(DeleteView):
    model = Doctors
    template_name = 'deletemedicine.html'
    success_url = reverse_lazy('lista_medicamentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "medico"
        return context
