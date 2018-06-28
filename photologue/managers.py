from django.db.models.query import QuerySet
from django.conf import settings
from django.db import models
from django.db.models import Q


class SharedQueries(object):

    """Some queries that are identical for Gallery and Photo."""

    def is_public(self):
        """Trivial filter - will probably become more complex as time goes by!"""
        return self.filter(is_public=True)

    def on_site(self):
        """Return objects linked to the current site only."""
        return self.filter(sites__id=settings.SITE_ID)


class PhotoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
                                Q(tags__name__icontains=query)|
                                Q(title__icontains=query)).distinct()


class PhotoQuerySet(SharedQueries, QuerySet, PhotoManager):
    pass


class GalleryQuerySet(SharedQueries, QuerySet):
    pass
