from django.urls import path

from . import views


urlpatterns = [
    path('check_plagiarism/', views.CheckPlagiarismView.as_view(), name='check_plagiarism'),
    path('report/<int:id>/', views.ReportView.as_view(), name='report'),
    path("", views.index, name="index")
]
