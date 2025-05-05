from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
                                   
from courses.models import Categories, Courses, Lessons, Materials

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    price_for_month = serializers.SerializerMethodField()
    course_categories = CategoriesSerializer(many=True)
    amount_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = ('id', 'course_name', 'course_duration', 'amount_of_lessons', 'course_price', 'price_for_month', 'course_description', 'course_for_who', 'course_categories', 'course_picture',
                  'is_arhived', 'course_date_of_start')

    def get_price_for_month(self, obj):
        price_for_month = int(obj.course_price / obj.course_duration)
        return price_for_month
    
    def get_amount_of_lessons(self, obj):
        amount = Lessons.objects.filter(lesson_course=obj.id)
        return len(amount)
    


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id', 'lesson_number', 'lesson_name', 'lesson_description', 'lesson_course', 'video_file', 'text_file')
