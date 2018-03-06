from .models import *
from django.db.models import Count, Sum

def quest_mvp_cp(request):
    support = Quest.objects.annotate(num_contrib=Sum('creator')).order_by('creator')
    mvp = [(quest.num_contrib, quest.creator) for quest in support]
    return {
        'quest_mvp': max(mvp)
    }