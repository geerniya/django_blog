from django.utils.deprecation import MiddlewareMixin
from myblog.models import Counts

class CountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        count_nums = Counts.objects.get(id=1)
        count_nums.visit_nums += 1
        count_nums.save()