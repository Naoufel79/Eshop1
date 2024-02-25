from django.shortcuts import render, redirect
from django.views import View


class Quiz (View):
    def get(self, request):
        return render (request, 'quiz.html')