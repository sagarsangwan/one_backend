from django.urls import path
from .views import GeneratePostCaptions

urlpatterns = [
    path(
        "generate-captions",
        GeneratePostCaptions.as_view(),
        name="generate-post-captions",
    )
]
