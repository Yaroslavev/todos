from django.shortcuts import redirect, render
from django.http.response import HttpResponse

from tasks.forms import CreateTodo
from tasks.models import Todo

def Home(request):
    todos = Todo.objects.all
    return render(request, "home.html", { "todos": todos })

def Details(request, id):
    for i in todos:
        if (i["id"] == id):
            todo = i
            break;

    return render(request, "details.html", { "todo": todo })

def Create(request):
    todo = CreateTodo()

    if (request.method == "POST"):
        todo = CreateTodo(request.POST)
        if (todo.is_valid()):
            todo.save()
            return redirect('home')
        else:
            return HttpResponse("""You typed wrong data!""")
    else:
        return render(request, "createTodoForm.html", { "form": todo })

def Delete(request, id):
    todoId = int(id)

    try:
        todo = Todo.objects.get(id = todoId)
    except Todo.DoesNotExist:
        return redirect('home')
    
    todo.delete()

    return redirect('home')
