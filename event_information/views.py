from django.shortcuts import render
from .models import Event, EventPrice

from .forms import Search


# home page
def index(request):
    events = Event.objects.all().order_by('date')
    for_top = Event.objects.all().order_by('-created_on')

    top_events = for_top[:3]  # for carousel

    context = {
        'top': top_events,
        'events': events,

    }
    return render(request, r'event_information\index.html', context)


def project_search(request):
    result = []
    query = None
    if 'query' in request.GET:
        form = Search(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Event.objects.filter(name=f'{query}')

    else:
        form = Search()
    context = {'form': form, 'query': query, 'result': result}
    return render(request, r'event_information\search.html', context)


# about us
def about(request):
    return render(request, r'event_information\about.html')
