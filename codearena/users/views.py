from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from submissions.models import Submission
from problems.models import Problem

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user

    total_problems = Problem.objects.count()

    accepted_subs = Submission.objects.filter(user=user, status="Accepted")
    solved_problem_ids = set()

    for sub in accepted_subs:
        solved_problem_ids.add(sub.problem.id) # type: ignore

    solved_problems = len(solved_problem_ids)
    total_submissions = Submission.objects.filter(user=user).count()

    accuracy = 0
    if total_submissions > 0:
        accuracy = int((solved_problems / total_submissions) * 100)

    recent_submissions = Submission.objects.filter(user=user).order_by('-id')[:5]

    context = {
        'total_problems': total_problems,
        'solved_problems': solved_problems,
        'total_submissions': total_submissions,
        'accuracy': accuracy,
        'recent_submissions': recent_submissions
    }

    return render(request, 'dashboard.html', context)

@login_required
def profile(request):
    user = request.user

    total_submissions = Submission.objects.filter(user=user).count()
    accepted_subs = Submission.objects.filter(user=user, status="Accepted")

    solved_problem_ids = set()
    solved_problems = []

    for sub in accepted_subs:
        if sub.problem.id not in solved_problem_ids:
            solved_problem_ids.add(sub.problem.id) # type: ignore
            solved_problems.append(sub.problem)

    solved_count = len(solved_problem_ids)

    accuracy = 0
    if total_submissions > 0:
        accuracy = int((solved_count / total_submissions) * 100)

    context = {
        'user': user,
        'total_submissions': total_submissions,
        'solved_count': solved_count,
        'accuracy': accuracy,
        'solved_problems': solved_problems
    }

    return render(request, 'profile.html', context)

