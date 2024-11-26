from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import TodoItem

# 게시글 등록
def board_create(request):
    return HttpResponse("board_create")

# 게시글 목록
def board_list(request):
    return HttpResponse("board_list")

# 게시글 보기
def board_read(request, board_id):
    return HttpResponse("board_read")

# 게시글 수정
def board_update(request, board_id):
    return HttpResponse("board_update")

# 게시글 삭제
def board_delete(request, board_id):
    return HttpResponse("board_delete")

# 메인 캘린더 화면
def calendar_main(request):
    return render(request, 'board/calendar.html')

# 선택한 날짜의 TodoList 표시 및 생성
def todo_list(request, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    todos = TodoItem.objects.filter(date=date_obj)
    return render(request, 'board/todo_list.html', {
        'todos': todos,
        'date': date_obj
    })

# TodoList 항목 생성
def todo_create(request, date):
    if request.method == 'POST':
        content = request.POST.get('content')
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        TodoItem.objects.create(content=content, date=date_obj)
    return redirect('todo_list', date=date)

def todo_toggle(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return JsonResponse({'status': 'success'})

def todo_delete(request, todo_id):
    TodoItem.objects.filter(id=todo_id).delete()
    return JsonResponse({'status': 'success'})