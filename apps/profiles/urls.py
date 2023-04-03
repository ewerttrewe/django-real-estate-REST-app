from django.urls import path
from . views import AgentListAPIView, GetProfileAPIView, UpdateProfileAPIView, TopAgentsListAPIView

urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name='get-profile'),
    path('update/<str:username>/', UpdateProfileAPIView.as_view(), name='update-profile'),
    path('agents/all/', AgentListAPIView.as_view(), name='all-profile'),
    path('top-agents/all/', TopAgentsListAPIView.as_view(), name='top-profile'),
]
