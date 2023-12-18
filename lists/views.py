from django.shortcuts import redirect, render

from lists.forms import TodoListForm


# Create your views here.
def create_item(request):
    todo = TodoListForm.objects.all()
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TodoListForm()
    context = {
        "form": form,
        "todo": todo,
    }

    return render(request, 'index.html', context)
