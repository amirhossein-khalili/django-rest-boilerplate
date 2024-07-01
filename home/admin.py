from django.contrib import admin

from .models import Answer, Person, Question

admin.site.register(Answer)
admin.site.register(Person)
admin.site.register(Question)
