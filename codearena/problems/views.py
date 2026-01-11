from django.shortcuts import render, get_object_or_404
from .models import Problem
from django.contrib.auth.decorators import login_required
from submissions.models import Submission
from django.shortcuts import redirect
from bson import ObjectId


@login_required
def problem_list(request):
    problems = Problem.objects.all()
    user = request.user

    solved_problem_ids = Submission.objects.filter(
        user=user, status="Accepted"
    ).values_list('problem_id', flat=True).distinct()

    context = {
        'problems': problems,
        'solved_problem_ids': solved_problem_ids
    }

    return render(request, 'problem_list.html', context)
 

@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, _id=ObjectId(problem_id))

    if request.method == "POST":
        code = request.POST['code']
        language = request.POST['language']

        Submission.objects.create(
            user=request.user,
            problem=problem,
            language=language,
            code=code,
            status="Submitted"
        )

        return redirect('submission_success')

    return render(request, 'problem_detail.html', {'problem': problem})

