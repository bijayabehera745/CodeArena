from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .executor import execute_code
from .models import Submission
from django.contrib.auth.models import User
from django.db.models import Count


@login_required
def submission_success(request):
    last_submission = Submission.objects.filter(user=request.user).last()
    problem = last_submission.problem

    output, success = execute_code(
        last_submission.language,
        last_submission.code,
        problem.test_input
    )

    # Normalize outputs
    user_output = output.strip()
    expected_output = problem.expected_output.strip()

    if not success:
        verdict = "Runtime Error / TLE"
    elif user_output == expected_output:
        verdict = "Accepted"
    else:
        verdict = "Wrong Answer"

    last_submission.status = verdict
    last_submission.save()

    return render(request, 'submission_success.html', {
        'output': output,
        'verdict': verdict,
        'success':success
    })
    
@login_required
def leaderboard(request):
    leaderboard_data = (
        Submission.objects
        .filter(status="Accepted")
        .values('user__username')
        .annotate(total_accepted=Count('id'))
        .order_by('-total_accepted')
    )

    return render(request, 'leaderboard.html', {
        'leaderboard': leaderboard_data
    })
