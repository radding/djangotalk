from django.shortcuts import render,get_object_or_404
from polls.models import Question, Answer
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def viewAllPolls(request):
    questions = Question.objects.all()
    return render(request, "polls/all.html",{"questions":questions})

def viewPoll(request, pollID):
    try:
        question = Question.objects.get(pk=pollID)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    answers = Answer.objects.filter(question = question)
    return render(request, "polls/one.html",{"question":question,"ans":answers})

def viewPoll2(request, pollID):
    question = get_object_or_404(Question, pk=pollID)
    answers = Answer.objects.filter(question = question)
    return render(request, "polls/one.html",{"question":question,"ans":answers})

def voteUpAns(request,ansID):
    answer = get_object_or_404(Answer, pk=ansID)
    answer.votes += 1
    answer.save()
    return render(request, "polls/vote.html", {"ques":answer.question, "ans":answer})