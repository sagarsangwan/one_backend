from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import os
import google.generativeai as genai
from .prompts import generateSocialMediaPrompt


def getblogCaptionsFromAi(blogCaptionPrompt):
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    blogCaptionPrompt = blogCaptionPrompt
    # Load Google Gemini API key
    genai.configure(api_key=GEMINI_API_KEY)

    # Set up Gemini AI model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(blogCaptionPrompt)
    ai_result = response.text
    # Remove code block markers and strip whitespace
    ai_result = ai_result.replace("```json", "").replace("```", "").strip()

    # replace non breaking spaces.
    ai_result = ai_result.replace("\u00a0", " ")
    # Parse AI response
    parsed_ai_result = json.loads(ai_result)
    return parsed_ai_result


class GeneratePostCaptions(APIView):
    def post(self, request):
        data = request.data
        blogUrl = data["blogUrl"]
        content = data["content"]
        preferredTone = data["preferredTone"]
        platforms = ["platforms"]
        captionPrompt = generateSocialMediaPrompt(
            blogUrl=blogUrl,
            content=content,
            selectedPlatforms=platforms,
            preferredTone=preferredTone,
        )
        # print(captionPrompt)
        responseFromAi = getblogCaptionsFromAi(blogCaptionPrompt=captionPrompt)
        print(responseFromAi)
        return Response(
            {"data": responseFromAi, "message": "hello from GeneratePostCaptions"},
            status.HTTP_200_OK,
        )
