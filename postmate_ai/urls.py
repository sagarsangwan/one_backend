from django.urls import path
from .views import GeneratePostCaptions

urlpatterns = [
    path(
        "generate-post-captions/",
        GeneratePostCaptions.as_view(),
        name="generate-post-captions",
    )
]
