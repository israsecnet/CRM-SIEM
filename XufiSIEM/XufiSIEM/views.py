from django.shortcuts import render
import requests, json, os

SERVERURI = os.environ['SERVERURI']

def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def login(request):
    return render(request, './registration/login.html')

def agent(request):
    AgentFullList = {}
    resp = requests.get(SERVERURI + "/healthcheck/fetch/")
    print(resp.text)
    AgentFullList = json.loads(resp.text)
    context = {"data": AgentFullList}
    return render(request, 'agentmgmt.html', context)

def scan(request):
    return render(request, 'scan.html')

def soar(request):
    return render(request, 'soar.html')

def soaranalysis(request):
    return render(request, 'soaranalysis.html')

def sbomsecurity(request):
    return render(request, 'sbomsecurity.html')

def blocklist(request):
    return render(request, 'blocklist.html')

def agentsettings(request):
    return render(request, 'agentsettings.html')