# context_processors.py

from .models import UserSetting

def site_settings(request):
    settings = UserSetting.objects.first()  # Assuming there's only one settings object
    return {
        'name': settings.name if settings else 'User Name',
        'user_photo': settings.user_photo.url if settings and settings.user_photo else None,
        'position': settings.position if settings else 'Position',
        'intro': settings.intro if settings else 'Intro',
        'mobile': settings.mobile if settings else 'Mobile',
        'email': settings.email if settings else 'Email',
        'location': settings.location if settings else 'Location',
        
        'website_url': settings.website_url if settings else 'website url',
        'linkedin_url': settings.linkedin_url if settings else 'linkedin_url',
        'github_url': settings.github_url if settings else 'github_url',
        'stackoverflow_url': settings.stackoverflow_url if settings else 'stackoverflow_url',
        'twitter_url': settings.twitter_url if settings else 'twitter_url',
        'reddit_url': settings.reddit_url if settings else 'reddit_url',
        'facebook_url': settings.facebook_url if settings else 'facebook_url',
        
        'logo': settings.logo.url if settings and settings.logo else None,
        'fav_icon': settings.fav_icon.url if settings and settings.fav_icon else None,
        'index_title': settings.index_title if settings else 'Index Title',
        'index_meta_kewords': settings.index_meta_kewords if settings else 'Index Meta Keywords',
        'short_desc': settings.short_desc if settings else 'Short Describtion',
        
    }
