from django.shortcuts import render
from django.views.generic import TemplateView





class MapView(TemplateView):
	template_name= 'map.html'



	def get_context_data(self, *args, **kwargs):
		ctx= super(MapView, self).get_context_data()
		lat = 24.90
		lng = 90.81
		ctx["x"] = lat
		ctx["y"] = lng
		return ctx




