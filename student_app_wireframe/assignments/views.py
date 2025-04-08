from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# @login_required
# def assignment_list(request):
#     assignments = Assignment.objects.filter(user=request.user).order_by('due_date') # Show only user's assignments
#     # ... (search and filter logic from previous example) ...
#     context = {
#         'assignments': assignments,
#         'search_term': search_term,
#         'course_filter': course_filter,
#         'courses': courses,
#     }
#     return render(request, 'assignments/assignment_list.html', context)

def assignment_list(request):
    assignments = Assignment.objects.filter(user=request.user)
    search_term = ''  # Initialize search_term with a default value

    if request.GET.get('q'):
        search_term = request.GET.get('q')
        assignments = assignments.filter(title__icontains=search_term)

    context = {
        'assignments': assignments,
        'search_term': search_term,
    }
    return render(request, 'assignments/assignment_list.html', context)

@login_required
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user  # Assign the current user
            assignment.save()
            return redirect('assignments:assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'assignments/assignment_form.html', {'form': form, 'title': 'Create Assignment'})

@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment})

@login_required
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments:assignment_detail', pk=assignment.pk)
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignments/assignment_form.html', {'form': form, 'title': 'Edit Assignment'})

@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignments:assignment_list')
    return render(request, 'assignments/assignment_confirm_delete.html', {'assignment': assignment})

# In assignments/views.py (or core/views.py)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Assignment  # If assignments are in this app

@login_required
def dashboard(request):
    upcoming_assignments = Assignment.objects.filter(user=request.user, completed=False).order_by('due_date')[:5]
    context = {
        'upcoming_assignments': upcoming_assignments,
        # Add other relevant dashboard data here
    }
    return render(request, 'dashboard.html', context)

@login_required
def account_settings(request):
    # Add logic to fetch and display user account settings
    context = {
        'user': request.user,
        # Add other settings data as needed
    }
    return render(request, 'account/settings.html', context)