from django.shortcuts import render
from tv.models import tvTime
from datetime import datetime
from tv.forms import ActiveForm
from django.db.models import Q

def home(request):
    today = datetime.now().date()
    current_shows = tvTime.objects.filter(Q(start_date__lt=today) & Q(active='y'))
    upcoming_shows = tvTime.objects.filter(start_date__gte=today)

    if request.method == 'GET':
        
        context = {'shows': current_shows, 'upcoming_shows': upcoming_shows}

    else:
        context = {'shows': current_shows, 'upcoming_shows': upcoming_shows}
        form = ActiveForm(request.POST)
        if form.is_valid:

            id = request.POST.get('id')
            print(f'the id is {id}')
            # once we have the ID update the field
            obj = tvTime.objects.get(id=id)
            obj.active = 'n'
            obj.save()


    return render(request, 'home.html', context)
