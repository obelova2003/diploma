from django.contrib import admin

from courses.models import Categories, Courses, Lessons, Materials

admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Materials)