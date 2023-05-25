from django.shortcuts import render, get_object_or_404, redirect
from .forms import form1,form2, Registration, Login
from .models import Question, Answer
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    res = False
    log =  Login()
    print("login page form",log)
    if request.method == 'POST':
        f = Registration(request.POST)
        if f.is_valid():
            v = f.save()
            v.set_password(v.password)
            v.save()
            res = True
            context = {'res':res,'login':log}
            return render(request,'login.html',context)
    
    else:
        f=Registration()
        return render(request,'register.html',{'res':res,'form':f})
    return render(request,'register.html',{'res':res,'form':f})


def log_in(request):
    log =  Login()
    print("login page form",log)
    if request.method=='POST':
        Username=request.POST.get('username')
        passWord=request.POST.get('password')
        user = authenticate(username=Username,password=passWord)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('app:home' ))
        return HttpResponse("username or password is incorrect")
    return render(request,'login.html',{'login':log})
    
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:login'))

def index(request):
    que_form = form1()
    return render(request,"quora.html",{'q':que_form,})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions,})

def question_detail(request, q_id):
    
    question = get_object_or_404(Question, id=q_id)
   
    return render(request, 'question_detail.html', {'question': question})

# def question_details(request,q_id):
#     answer = Answer.objects.get(answer_id=q_id)
#     question = get_object_or_404(Question, id=q_id)
   
#     return render(request, 'question_detail.html', {'question': question,"answer":answer})


def create_question(request):
    if request.method == 'POST':
        question = request.POST['content']
        question = Question.objects.create( query=question)
        return redirect('app:question_detail',q_id=question.id)
    return render(request, 'create_question.html')

def create_answer(request, q_id):
    if request.method == 'POST':
        content = request.POST['content']
        question = get_object_or_404(Question, id=q_id)
        answer = Answer.objects.create(query_answer=question, content=content)
        # answer = get_object_or_404(Answer, id=q_id)
        # answer.likes = 0
        # return HttpResponse("data stored")
        return redirect('app:question_detail', q_id=question.id)
    # return HttpResponse("not stored")
    return render(request, 'create_answer.html', {'q_id': question_id})



def answer_detail(request, q_id):
    question = Question.objects.get(id=q_id)
    
    like = False
    # answer = get_object_or_404(Answer,id=q_id)
    if request.method == 'POST':
        # answer.likes 
        Answer.likes == 1
        # answer.save()
        like = True

    return render(request, 'question_detail.html', {'like':like,'question':question})

