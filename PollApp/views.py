from django.db.models import Count
from django.shortcuts import render
from PollApp.models import Poll, Choice, Vote
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_view(request):
    polls = Poll.objects.all()
    return render(request, template_name="PollApp/home.html", context={"polls": polls})


@login_required(login_url='/users/login')
def poll_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if request.method == 'POST':
        choice_id = request.POST.get('choice_id')
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(poll=poll, choice=choice)

        return render(request, template_name="PollApp/poll.html",context={"poll": poll, "success_message": "Voted Successfully"})

    return render(request, template_name="PollApp/poll.html", context={"poll": poll})


@login_required
def poll_result_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    choices_with_votes = Choice.objects.filter(related_polls=poll).annotate(total_votes=Count('votes'))

    total_votes = sum(choice.total_votes for choice in choices_with_votes)

    for choice in choices_with_votes:
        choice.vote_percentage = (choice.total_votes / total_votes) * 100 if total_votes > 0 else 0

    return render(request, template_name="PollApp/poll_result.html",
                  context={"poll": poll, "choices_with_votes": choices_with_votes})



def index_view(request):
    return render(request, template_name="PollApp/index.html")

