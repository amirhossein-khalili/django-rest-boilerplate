from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    # class Meta:
    #     verbose_name = _("person")
    #     verbose_name_plural = _("persons")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("person_detail", kwargs={"pk": self.pk})


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title[:20]}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    body = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question.title[:20]}"
