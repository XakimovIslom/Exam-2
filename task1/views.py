from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from task1.forms import CustomUserCreationForm

User = get_user_model()


def index(request):
    return render(request, "home.html")


# def registerUser(request):
#     page = "register"
#     form = CustomUserCreationForm()

#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()

#             login(request, user)
#             return redirect("login")

#     context = {"page": page, "form": form}
#     return render(request, "task1/register.html", context)


def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username").lower()
            if User.objects.filter(username=username, is_deleted=True).exists():
                user = User.objects.get(username=username)
                user.is_deleted = False
                user.save()
            else:
                form.save()
                user = authenticate(
                    request, username=username, password=request.POST["password"]
                )
                login(request, user)
                return redirect("home")

    context = {"form": form}
    return render(request, "task1/register.html", context)


def loginUser(request):

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse("Kirishni rad etildi. Foydalanuvchi topilmadi.")

        if user.is_deleted:
            return HttpResponse("Kirishni rad etildi. Foydalanuvchi o'chirilgan.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "task1/login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")
