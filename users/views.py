from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """
    when the register url is mapped to this function, if it is a GET request
    a form will be rendered. If it is a POST request

    :param request:
    :return:
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('blog-home')

    else:
        # django takes care of generating forms and user validation
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
