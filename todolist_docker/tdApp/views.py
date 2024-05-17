from django.shortcuts import redirect, render
from .models import Todo
from django.views.decorators.http import require_POST
from .forms import TodoForm

from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def index(request):
    # 마감 날짜가 있는 할 일을 상단에 위치시킵니다.
    scheduled_tasks = Todo.objects.exclude(due_date__isnull=True).order_by('due_date')
    # 마감 날짜가 없는 할 일을 하단에 위치시킵니다.
    unscheduled_tasks = Todo.objects.filter(due_date__isnull=True).order_by('id')
    form = TodoForm()
    context = {
        'scheduled_tasks': scheduled_tasks,
        'unscheduled_tasks': unscheduled_tasks,
        'form': form
    }
    return render(request, 'tdApp/index.html', context)

@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    
    if form.is_valid():
        form.save()
    
    return redirect('index')

# 여기에 `TodoForm`을 `tdApp/forms.py`에서 가져옵니다.

# tdApp/views.py 파일에 추가
from django.shortcuts import get_object_or_404, redirect
# 다른 필요한 import 문들...

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)  # Todo 객체를 가져오고, 없으면 404 에러를 반환
    todo.delete()  # Todo 객체를 삭제
    return redirect('index')  # 할 일 목록 페이지로 리다이렉트

# tdApp/views.py

from django.views.decorators.http import require_POST
# 다른 필요한 import 문들...

@require_POST
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed  # 현재 상태를 반전시킵니다.
    todo.save()
    return redirect('index')
