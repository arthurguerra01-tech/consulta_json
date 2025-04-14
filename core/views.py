import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({'medicos': [], 'usuarios': [], 'consultas': []}, f)

def carregar_dados():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def salvar_dados(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def index(request):
    return render(request, 'usuario.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def usuario_portal(request):
    return render(request, 'usuario.html')


    return render(request, 'index.html')

@csrf_exempt
def cadastrar_medico(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        db = carregar_dados()
        db['medicos'].append(dados)
        salvar_dados(db)
        return JsonResponse({'mensagem': 'Médico cadastrado com sucesso'})

@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        db = carregar_dados()
        db['usuarios'].append(dados)
        salvar_dados(db)
        return JsonResponse({'mensagem': 'Usuário cadastrado com sucesso'})

@csrf_exempt
def agendar_consulta(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        db = carregar_dados()
        db['consultas'].append(dados)
        salvar_dados(db)
        return JsonResponse({'mensagem': 'Consulta agendada com sucesso'})

@csrf_exempt
def excluir_consulta(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        db = carregar_dados()
        db['consultas'] = [
            c for c in db['consultas']
            if not (c['cpf'] == dados['cpf'] and c['medico'] == dados['medico'])
        ]
        salvar_dados(db)
        return JsonResponse({'mensagem': 'Consulta excluída com sucesso'})

def listar_medicos(request):
    db = carregar_dados()
    return JsonResponse(db['medicos'], safe=False)
