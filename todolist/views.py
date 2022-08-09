from django.shortcuts import render
from .models import Todo
 
# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'todolist/index.html', context)
 
def delete(request, todo_id):
    delete_id = Todo.objects.get(id=todo_id)
    delete_id.delete()
    return index(request)