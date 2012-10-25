django-social-metadata
======================

django-social-metadata is a Django application that provides mixin and
template to display social metadata for Facebook and Google+.

Installation
------------

Package
_______

javascript-settings can be installed as a normal Python package.

Example instalation for pip::

    $ pip install django-social-metadata


Configuration
-------------

settings.py
___________

Add javascript-settings to INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'social_metadata',
        ...
    )

template
________

Include template in HEAD section of your main template::

    {% include "social_metadata/default_tags.html" %}

Usage Example
-------------

views.py ::

    from urlparse import urljoin

    from django.conf.settings import MEDIA_URL
    from django.views.generic import DetailView

    import social_metadata.views

    class PhotoSocialDataMixin(social_metadata.views.SocialDataMixin):
        def get_social_title(self):
            return self.title

        def get_social_images(self):
            return [urljoin(MEDIA_URL, self.image.path)]


        def get_social_description(self):
            return self.description

    class PhotoDetail(PhotoSocialDataMixin, DetailView):
         model = Photo
