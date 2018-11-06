from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    # def was_published_recently(self):
    #     return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Story(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=200)
    user_story = models.CharField(max_length=200)
    acceptance_criteria = models.CharField(max_length=200)
    business_value = models.IntegerField(default=0)
    estimation = models.FloatField(default=0.5)

    def get_story_value(self):
        if self.estimation:
            return self.business_value / self.estimation
        else:
            return "estimation cannot be set to 0"

    def __str__(self):
        return self.story_title

    class Meta:
        verbose_name_plural = "stories"
