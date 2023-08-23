from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewsList.as_view(), name="review_list"),
    path("<slug:slug>/", views.ReviewsDetail.as_view(), name="reviews-detail"),
]
