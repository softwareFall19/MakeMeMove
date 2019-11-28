from django.shortcuts import render

from .models import Agent

def agents(request):
    agents = Agent.objects.all()

    context = {
        'agents': agents
    }
    return render(request, 'agents/agents.html', context)
