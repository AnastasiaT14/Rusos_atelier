from django.urls import path
from .views import UserFormSubmissionView

urlpatterns = [
    path('user-form-submission/', UserFormSubmissionView.as_view(), name='user_form_submission'),
]
