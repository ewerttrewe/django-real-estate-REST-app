from django.urls import path

from .views import (AgentListAPIView, GetProfileAPIView, TopAgentsListAPIView,
                    UpdateProfileAPIView)

urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name='get-profile'),
    path('update/<str:username>/', UpdateProfileAPIView.as_view(), name='update-profile'),
    path('agents/all/', AgentListAPIView.as_view(), name='all-profile'),
    path('top-agents/all/', TopAgentsListAPIView.as_view(), name='top-profile'),
]
