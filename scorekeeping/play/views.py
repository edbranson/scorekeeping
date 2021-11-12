from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Play, Game
from play.forms import PlayCreateForm
from datetime import datetime
from datetime import date
# Create your views here.

class PlayCreate(View):
    
    def post(self, request):       
        # Create a form instance and populate it with data from the request (binding):
        form = PlayCreateForm(request.POST) 
        
        if form.is_valid():
            play = Play()
            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            play.game = form.cleaned_data['game']
            play.location = form.cleaned_data['location']
            play.play_date = form.cleaned_data['play_date']
            play.play_complete = form.cleaned_data['play_complete']
            play.save()
            return HttpResponseRedirect(reverse('start-play') )
        else:
            proposed_location = "xxx"
            proposed_date = date.today()
            form = PlayCreateForm(initial={'location': proposed_location, 'play_date': proposed_date})

        context = {'form':form,}    
        return render(request, 'play_form.html', context)  
    
    def get(self, request):
        proposed_location = ""
        proposed_date = date.today()
        form = PlayCreateForm(initial={'location': proposed_location, 'play_date': proposed_date})
        
        context = {'form':form,}    
        return render(request, 'play_form_new.html', context)  

class PlayUpdate(View):
    model = Play()
             

    def post(self, request, pk):
        play = get_object_or_404(Play, pk=pk)
        # Create a form instance and populate it with data from the request (binding):
        form = PlayCreateForm(request.POST)
        if form.is_valid():      
            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            play.game = form.cleaned_data['game']
            play.location = form.cleaned_data['location']
            play.play_date = form.cleaned_data['play_date']
            play.play_complete = form.cleaned_data['play_complete']
            play.save()
            return HttpResponseRedirect(reverse('play-list') )

        context = {'form':form, 'game_desc': play.game.description}    
        return render(request, 'play_form.html', context) 

    def get(self, request, pk):
        play = get_object_or_404(Play, pk=pk)
        form = PlayCreateForm(initial={'location': play.location, 'play_date': play.play_date, 'play_complete': play.play_complete})

        context = {'form':form,'game_desc': play.game.description}    
        return render(request, 'play_form_update.html', context) 

class PlayListView(generic.ListView):
    model = Play
    queryset = Play.objects.filter(play_complete = False)

class PlayArchiveListView(generic.ListView):
    model = Play
    context_object_name = 'play_archive_list'
    queryset = Play.objects.filter(play_complete = True)
    template_name = 'play/play_archive_list.html'
      
    
class PlayDetailView(generic.DetailView):
    model = Play   

class PlayDelete(generic.DeleteView):
    model = Play
    success_url = reverse_lazy('play-list')                     