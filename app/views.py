from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from app.forms import RegisterForm, LoginForm, UploadFileForm
from app.models import User, File
from app.serializers import UserSerializer, FileListSerializer


class UserCreate(CreateView):
    queryset = get_user_model().objects.all()
    form_class = RegisterForm
    success_url = "/"
    template_name = "app/signup.html"


class AuthView(LoginView):
    # form_class = LoginForm
    redirect_authenticated_user = True
    template_name = "app/login.html"


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def auth_page(request):
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


class FileListView(ListAPIView):
    serializer_class = FileListSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request):
        self.queryset = File.objects.filter(owner_id__exact=request.user.id)
        return super().get(request)
