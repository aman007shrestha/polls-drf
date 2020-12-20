from django.urls import path
from . import views


urlpatterns = [
	path('polls/', views.PollList.as_view(), name='polls-list'),
	path('polls/<int:pk>/', views.PollDetail.as_view(), name='polls-detail'),
	path('choices/', views.ChoiceList.as_view(), name='choice-list'),
	path('vote/', views.CreateVote.as_view(), name='create-view'),		
]