# Imports the required modules.
from django.contrib import admin
from django.urls import path, include


# Defines all the URL patterns for the project.
urlpatterns = [
    # Path to use the django admin panel.
    path("admin/", admin.site.urls),
    # Path to make other pages work with the base.html
    path("", include("reviews.urls"), name="reviews-urls"),
    # Path for using the Summernote WYSIWYG editor.
    path("summernote/", include("django_summernote.urls")),
    # Path for user account management using allauth.
    path("accounts/", include("allauth.urls")),
]
