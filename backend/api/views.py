from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from courses.models import Categories, Courses, Lessons, Materials
from api.filters import CoursesFilter, LessonsFilter

from . import serializers


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    pagination_class = None


class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = serializers.MaterialsSerializer
    pagination_class = None


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = serializers.CoursesSerializer
    pagination_class = None

    filter_backends = [DjangoFilterBackend]
    filterset_class = CoursesFilter


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = serializers.LessonsSerializer
    pagination_class = None

    filter_backends = [DjangoFilterBackend]
    filterset_class = LessonsFilter