from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Sprinter.models import Project, Story


def index(request):
    projects_list = Project.objects.all()

    context = {'projects_list': projects_list}
    return render(request, 'sprinter/index.html', context)


def project_stories(request, project_id):
    stories_list = Story.objects.filter(project=project_id)  # .order_by('-pub_date')
    project = Project.objects.get(id=project_id)
    context = {'stories_list': stories_list, 'project': project}
    return render(request, 'sprinter/stories.html', context)


def update_story(request, project_id, story_id):
    story = Story.objects.get(id=story_id)
    story.story_title = request.POST['story_title']
    story.user_story = request.POST['story']
    story.acceptance_criteria = request.POST['criteria']
    story.business_value = request.POST['money']
    story.estimation = request.POST['time']
    story.save()
    print("updating")

    return HttpResponseRedirect(reverse('sprinter:project_stories', args=(project_id,)))


def new_story(request, project_id):
    story = Story(
        project=Project.objects.get(id=project_id),
        story_title=request.POST['story_title'],
        user_story=request.POST['story'],
        acceptance_criteria=request.POST['criteria'],
        business_value=request.POST['money'],
        estimation=request.POST['time'],
    )
    print("creating")
    story.save()

    return HttpResponseRedirect(reverse('sprinter:project_stories', args=(project_id,)))


def delete_story(request, project_id, story_id):
    story_to_delete = Story.objects.get(id=request.POST['story_id_to_delete'])
    story_to_delete.delete()
    return HttpResponseRedirect(reverse('sprinter:project_stories', args=(project_id,)))
