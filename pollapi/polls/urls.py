from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
	#path('polls/', views.PollList.as_view(), name='polls-list'),
	#path('polls/<int:pk>/', views.PollDetail.as_view(), name='polls-detail'),
	path('polls/<int:pk>/choices/', views.ChoiceList.as_view(), name="choice-list"),
	path('polls/<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name="create-vote"),
	#path('choices/', views.ChoiceList.as_view(), name='choice-list'),
	#path('vote/', views.CreateVote.as_view(), name='create-view'),		
]

router = DefaultRouter()
router.register('polls', views.PollViewSet, basename='polls')

urlpatterns += router.urls

