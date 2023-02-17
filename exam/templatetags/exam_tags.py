from django import template
from exam.models import Enrollment

register = template.Library()


def is_enrolled(exam,user):
    return Enrollment.objects.filter(exam=exam, user=user).exists()

register.filter('is_enrolled', is_enrolled)
