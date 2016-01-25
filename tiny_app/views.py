from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, SignUpForm, PhotoUploadForm
from .models import SignUp, Picture
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


@login_required(login_url='/accounts/login/')
def upload_picture(request, uid=None):
    """
    Photo upload / dropzone handler
    :param request:
    :param uid: Optional picture UID when re-uploading a file.
    :return:
    """
    form = PhotoUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        pic = request.FILES['file']
        # [...] Process whatever you do with that file there. I resize it, create thumbnails, etc.
        # Get an instance of picture model (defined below)
        picture = ...
        picture.file = pic
        picture.save()
        return HttpResponse('Image upload succeeded.')
    return HttpResponseBadRequest("Image upload form not valid.")


def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.p_uid, ext)
    d = datetime.date.today()
    username = instance.author.username

    # Create the directory structure
    return os.path.join(
        'userpics', username, d.strftime('%Y'), d.strftime('%m'), filename
    )

# def form(request):
#     return render(request, "form.html", {})


# def upload(request):  # for loop used to loop over the upload function..allows for multiple uploads.
#     for count, x in enumerate(request.FILES.getlist("files")):
#         def process(f):
#             with open('/Users/Dana Medhaug/Documents/ProjectsFolder/tinyshare/static_in_env/media_root/file_' + str(count), 'wb+') as destination:  # need to fix path to upload correctly.
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#         process(x)
#     return HttpResponse("File(s) uploaded!")
