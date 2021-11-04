## Things that I have noticed that you may want to check

From scorekeeping\play\views.py

    class PlayUpdate(View):
        model = Play()      this Play() has parentheses
    
    further down

    class PlayListView(generic.ListView):
        model = Play        no parentheses

    class PlayArchiveListView(generic.ListView):
        model = Play        no parentheses
    
    class PlayDetailView(generic.DetailView):
        model = Play        no parentheses
    
    class PlayDelete(generic.DeleteView):
        model = Play        no parentheses

From scorekeeping\play\models.py

    line 13 you reference the score.Hand but you have not imported it with Game and Player

From scorekeeping\player\admin.py

    line 10     I don't think there should be a " , " after "name"

I added a .gitignore file to ignore the Scripts folder and the pyvenv.cfg file
because when I pull the repo to my computer I have to re-create the python virtual environment
which over-writes the Scripts forlder and pyvenv.cfg file.