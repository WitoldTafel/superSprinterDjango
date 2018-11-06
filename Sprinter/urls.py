from django.urls import path

from . import views

app_name = "sprinter"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.project_stories, name='project_stories'),
    path('<int:project_id>/story/<int:story_id>', views.delete_story, name='delete_story'),
    path('<int:project_id>/new_story', views.new_story, name='new_story'),
    path('<int:project_id>/story/<int:story_id>/update_story', views.update_story, name='update_story'),

]