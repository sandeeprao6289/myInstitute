import json

from django.shortcuts import render
from django.template import Template, RequestContext
from django.template.response import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.template.loader import render_to_string

from usermgmt.models import User
from usermgmt.adminforms import UserForm

class UsersListView(View):
	"""
    List the Users in the site.
    """
	template_name = 'admin/usermgmt/user_list.html'

	def get(self, request):
		return render(request, self.template_name)

users_list_view = UsersListView.as_view()

class AjaxLoadUsers(View):

	def get(self, request):
		data = {}

		users = User.objects.all().order_by('first_name')
		sdata = {'users':users}

		data['html']=render_to_string('admin/usermgmt/ajax_user_list.html',sdata,context_instance=RequestContext(request))
		data['status'] = 1

		return HttpResponse(json.dumps(data), content_type='application/x-json')

ajax_load_users = AjaxLoadUsers.as_view()

class AddUserView(View):

	def get(self, request):
		data = {}
		try:
			userid = request.GET.get('userid')
			user = User.objects.get(id = userid)
			userform = UserForm(instance=user)
		except:
			userform = UserForm()
			user = False

		sdata = {'form':userform,'user':user}
		data['html']=render_to_string('admin/usermgmt/ajax_user_form.html',sdata,context_instance=RequestContext(request))
		data['status'] = 1

		return HttpResponse(json.dumps(data), content_type='application/x-json')

	def post(self, request):
		data = {}
		try:
			userid = request.POST.get('userid')
			user = User.objects.get(id = userid)
			userform = UserForm(request.POST,instance=user)
			data['message'] = "User details updated successfully!!!"
		except:
			user=False
			userform = UserForm(request.POST)
			data['message'] = "User added successfully!!!"

		try:
			if userform.is_valid():
				user_obj = userform.save(commit=False)
				if not user:
					password = request.POST.get('password')
					user_obj.set_password(password)
				user_obj.save()
				data['status'] = 1
		except:
			data['status'] = 0

		return HttpResponse(json.dumps(data), content_type='application/x-json')

user_add_view = AddUserView.as_view()

class DeleteUser(View):

	def get(self, request):
		data = {}
		userid = request.GET.get('userid')
		user = User.objects.get(id = userid)

		user.delete()
		data['status'] = 1
		data['message'] = "User deleted successfully!!!"

		return HttpResponse(json.dumps(data), content_type='application/x-json')

user_delete_view = DeleteUser.as_view()

