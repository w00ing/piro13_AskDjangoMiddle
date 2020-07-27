from django.shortcuts import render, redirect
from django.urls import reverse
from posts.models import Post


def index(request):

    queryset = Post.objects.all()
    context = {
        "posts": queryset,
    }
    return render(request, "post/index.html", context=context)


def create(request):

    # GET
    if request.method == "GET":
        return render(request, "post/create.html", context={})

    # POST
    title = request.POST["title"]
    author = request.POST["author"]
    content = request.POST["content"]
    post = Post.objects.create(title=title, author=author, content=content,)

    pk = post.id
    url = reverse("posts:retrieve", kwargs={"pk": pk})
    # home = reverse("posts:list")
    return redirect(to=url)


def retrieve(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        "post": post,
    }
    return render(request, "post/retrieve.html", context=context)


def update(request, pk):
    post = Post.objects.get(id=pk)

    # GET
    if request.method == "GET":
        context = {
            "post": post,
        }
        return render(request, "post/update.html", context=context)

    # POST
    title = request.POST["title"]
    author = request.POST["author"]
    content = request.POST["content"]

    post.title = title
    post.author = author
    post.content = content
    post.save()

    url = reverse("posts:retrieve", kwargs={"pk": pk})
    return redirect(to=url)


def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    url = reverse("posts:list")
    return redirect(to=url)

