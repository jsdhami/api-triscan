from django.urls import path
from . import views


urlpatterns = [
    path('plagiarism/', views.CheckPlagiarismView.as_view(), name='Plagiarism Checking'),
    path('report/<int:id>/', views.ReportView.as_view(), name='Report'),
    path("", views.index, name="index")
]
