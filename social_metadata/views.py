from django.conf import settings
from django.views.generic.detail import BaseDetailView


class SocialDataMixin(object):
    def get_social_url(self):
        if isinstance(self, BaseDetailView):
            return self.object.get_absolute_url()

    def get_social_title(self):
        return getattr(self, 'social_title', None)

    def get_social_type(self):
        return getattr(self, 'social_type', None)

    def get_social_images(self):
        return getattr(self, 'social_images', [])

    def get_social_description(self):
        return getattr(self, 'social_description', None)

    def get_social_site_name(self):
        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            from django.contrib.sites.models import Site
            try:
                return Site.objects.get_current().name
            except Site.DoesNotExist:
                pass
        global_default = getattr(settings, 'SOCIAL_METADATA_SITE_NAME', None)
        return getattr(self, 'social_site_name', global_default)

    def get_twitter_site_username(self):
        return getattr(self, 'twitter_site_username', None)

    def get_twitter_card_type(self):
        return getattr(self, 'twitter_card_type', None)

    def get_twitter_creator(self):
        return getattr(self, 'twitter_creator', None)

    def get_social_metadata(self):
        return {
            'title': self.get_social_title(),
            'type': self.get_social_type(),
            'images': self.get_social_images(),
            'description': self.get_social_description(),
            'url': self.get_social_url(),
            'site_name': self.get_social_site_name(),
            'twitter_site_username': self.get_twitter_site_username(),
            'twitter_card_type': self.get_twitter_card_type(),
            'twitter_creator': self.get_twitter_creator(),
        }

    def get_context_data(self, *args, **kwargs):
        context = super(SocialDataMixin, self).get_context_data(*args, **kwargs)
        context['social_metadata'] = self.get_social_metadata()
        return context
