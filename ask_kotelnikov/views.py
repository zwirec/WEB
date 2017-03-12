from django.shortcuts import render_to_response

from ask_kotelnikov.models import Question


def index(request):
    Question.objects.all()
    return render_to_response('../templates/index.html', {})


def question(request):
    return render_to_response('../templates/question.html', {})


def ask(request):
    return render_to_response('../templates/ask.html')


def tag(request):
    return render_to_response('../templates/tag.html')


def test(request):
    if request.method == 'GET':
        return render_to_response("../templates/test.html", {'method': str(request.method),
                                                             'parametrs': request.GET.dict()})
    elif request.method == 'POST':
        return render_to_response("../templates/test.html", {'method': str(request.method),
                                                             'parametrs': request.POST.dict()})
