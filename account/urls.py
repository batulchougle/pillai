from django.urls import path
from .views import RegisterInstituteView, VerifyUserEmail, StudentRegisterView, FacultyRegisterView,StudentLoginView

urlpatterns = [
    
    path('institue-signup/', RegisterInstituteView.as_view(), name='institute-signup'),
    path('verify-email/',VerifyUserEmail.as_view(),name='verify'),
    path('student-signup/',StudentRegisterView.as_view(),name='student-signup'),
    path('faculty-signup/',FacultyRegisterView.as_view(),name='faculty=signup'),
    path('student-login/',StudentLoginView.as_view(),name='student-login')

]