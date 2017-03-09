from django.http import HttpResponse
from django.shortcuts import render_to_response

from ask_kotelnikov.models import Question


def hello(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def index(request):
    Question.objects.all()
    return render_to_response('../templates/index.html', {})


def question(request):
    return render_to_response('../templates/question.html', {})


def ask(request):
    return render_to_response('../templates/ask.html')

def tag(request):
    return render_to_response('../templates/tag.html')
