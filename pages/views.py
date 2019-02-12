from django.shortcuts import render
from .models import Page


def pages_list(request):
	context = {
		'pages': Page.objects.all()
	}

	return render(request, 'list.html', context)

def pages_detail(request, page_id):
	context = {
		'pages': Page.objects.get(id=page_id)
	}

	return render(request, 'detail.html', context)