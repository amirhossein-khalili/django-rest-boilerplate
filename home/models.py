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
