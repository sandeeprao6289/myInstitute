from django.template import Template
from django.template.response import TemplateResponse

from django.views.generic import View
from django.shortcuts import render

# Create your views here.

class Home(View):
	template_name = 'common/home.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

home = Home.as_view()