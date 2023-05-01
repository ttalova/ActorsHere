from django_filters import rest_framework as filters

from core_app.models import ActorProfile, Tag


class ActorsFilter(filters.FilterSet):
    tag_id = filters.ModelChoiceFilter(queryset=Tag.objects.all(), method="filter_tag_id")

    def filter_tag_id(self, queryset, name, value):
        return queryset.filter(tag__in=[value])

    class Meta:
        model = ActorProfile
        fields = ("full_name", "city")
