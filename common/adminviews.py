from django.template import Template
from django.template.response import TemplateResponse

from usermgmt.models import User

def dashboard(request, template="admin/dashboard.html"):
    ''' admin home page '''
    data = {}
    data['users'] = User.objects.all()
    return TemplateResponse(request, template, data)
