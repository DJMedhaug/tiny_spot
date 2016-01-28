from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from .forms import ContactForm, SignUpForm, PhotoUploadForm, PostForm
from .models import SignUp, Picture, Post
from django.utils import timezone
from django.http import HttpResponse


def home(request):
    title = 'Sign Up Now'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        if not instance.full_name:
            instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated() and request.user.is_staff:

        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Tiny Spot contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]  # add more emails as a string if needed
        contact_message = "%s: %s via %s" % (
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('tiny_app.views.post_list')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('tiny_app.views.post_detail', pk=pk)
