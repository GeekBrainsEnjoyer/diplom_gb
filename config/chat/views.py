from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from recipe.models import Recipe

from .forms import ChatMessageForm
from .models import Chat


@login_required
def new_chat(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)

    if recipe.created_by == request.user:
        return redirect('dashboard:index')

    chats = Chat.objects.filter().filter(
        users__in=[request.user.id])

    if chats:
        return redirect('chat:detail', pk=chats.first().id)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat = Chat.objects.create()
            chat.users.add(request.user)
            chat.users.add(recipe.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            return redirect('recipe:detail', pk=recipe_pk)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/new.html', {
        'form': form
    })


@login_required
def inbox(request):
    chats = Chat.objects.filter(users__in=[request.user.id])

    return render(request, 'chat/chats.html', {
        'chats': chats
    })


@login_required
def detail(request, pk):
    chat = Chat.objects.filter(users__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect('chat:detail', pk=pk)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/detail.html', {
        'chat': chat,
        'form': form
    })
