from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import StartForm
from S7Project.settings import FIELDS_CONST



def index(request):
    return render(request, "Graphs/main.html")


class GetData(CreateView):
    template_name = 'Graphs/getData.html'
    form_class = StartForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["constant"] = FIELDS_CONST
        return context