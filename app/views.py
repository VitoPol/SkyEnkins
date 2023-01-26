from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView, DeleteView, UpdateView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from app import tasks
from app.forms import RegisterForm, LoginForm, UploadFileForm
from app.models import User, File
from app.serializers import UserSerializer, FileListSerializer


class UserCreate(CreateView):
    queryset = get_user_model().objects.all()
    form_class = RegisterForm
    success_url = "/"
    template_name = "app/signup.html"

    # def post(self, request, *args, **kwargs):
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         instance = User(username=request.POST.get("username", None), email=request.POST.get("email", None))
    #         instance.set_password(request.POST.get("password", None))
    #         instance.save()
    #     return super().post(request, *args, **kwargs)

class AuthView(LoginView):
    # form_class = LoginForm
    redirect_authenticated_user = True
    template_name = "app/login.html"


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def auth_page(request):
        if request.user.is_authenticated:
            return redirect("/home/")
        return render(request, "app/index.html")


class UploadView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    queryset = File.objects.all()
    form_class = UploadFileForm
    success_url = "/"
    template_name = "app/upload.html"

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = File(file=request.FILES['file'], owner_id=request.user.id, mark='new')
            instance.save()
        return super().post(request)


# class FileListView(ListAPIView):
#     serializer_class = FileListSerializer
#     permission_classes = [IsAuthenticated]
#
#
#     def get(self, request):
#         self.queryset = File.objects.filter(owner_id__exact=request.user.id)
#         return render(request, "app/home.html", context=request.context)

class FileListView(LoginRequiredMixin, ListView):
    model = File
    login_url = '/login/'
    template_name = "app/home.html"
    context_object_name = "files"

    def get(self, request, *args, **kwargs):
        # tasks.checking_files()
        self.queryset = File.objects.filter(owner_id=request.user.id)
        return super().get(request, *args, **kwargs)


class FileDelView(LoginRequiredMixin, DeleteView):
    model = File
    login_url = '/login/'
    success_url = "/home/"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = File
    login_url = '/login/'
    success_url = "/home/"
    fields = ["file"]

    # def post(self, request, *args, **kwargs):
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         instance = File(file=request.FILES['file'], owner_id=request.user.id, mark='changed')
    #         instance.save()
    #     return super().post(request)
