# Sin_Quiz/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .utils import SinChat_Quiz

def quiz_view(request):
    quiz = SinChat_Quiz(request)
    pergunta = request.session.get('Pergunta', '')
    alternativa_a = request.session.get('Alternativa_A', '')
    alternativa_b = request.session.get('Alternativa_B', '')
    alternativa_c = request.session.get('Alternativa_C', '')
    alternativa_d = request.session.get('Alternativa_D', '')
    resposta = request.session.get('Resposta', '')

    context = {
        'Pergunta': pergunta,
        'Alternativa_A': alternativa_a,
        'Alternativa_B': alternativa_b,
        'Alternativa_C': alternativa_c,
        'Alternativa_D': alternativa_d,
        'Resposta': resposta,
    }

    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')