def generateSocialMediaPrompt(
    content, blogUrl, selectedPlatforms, preferredTone, typeOfBlog=None
):
    """
    Generates a structured prompt for AI to generate social media captions, SEO title, and trending hashtags and trending hashtags on tech used in  in JSON format.
    """

    prompt = f"""
    Generate an SEO-optimized social media post for a blog article. The AI should analyze the blog content and generate engaging, platform-specific captions.

    ### **Input Details:**
    - **Blog Content:** {content}
    - **Blog Post URL:** {blogUrl}
    - **Target Platforms:** {", ".join(selectedPlatforms)}
    - **Preferred Tone:** {preferredTone}

    ### **Expected JSON Output:**
    ```json
    {{
      "seo_title": "A compelling, SEO-optimized blog title",
      "seo_description": "A concise and engaging meta description optimized for search engines.",
      "platforms": {{
        "LinkedIn": {{
          "caption": "A professional, without hashtags and insightful post tailored for LinkedIn engagement. 🔥",
          "hashtags": ["#SEO", "#WebDevelopment", "#TechInsights"],
          "cta": "Read more here: {blogUrl}"
        }},
        "X": {{
          "caption": "A short for free plan on x, without hashtags, trending post with high engagement potential. 🚀",
          "hashtags": ["#TechTrends", "#NextJS", "#AI"],
          "cta": "Check it out: {blogUrl}"
        }},
        "Reddit": {{
          "caption": "A discussion-friendly caption without hashtags designed to drive conversations. 🗣️",
          "hashtags": ["#TechTrends", "#NextJS", "#AI"],
          "cta": "Join the discussion: {blogUrl}"
        }}
      }}
    }}
    ```

    ### **Requirements:**
    1. **SEO Optimization** – Generate an **attention-grabbing title** and **high-quality description**.
    2. **Engagement-Focused Captions** – Write **unique** captions tailored for each platform.
    3. **Trending Hashtags** – Choose relevant, high-traffic hashtags dynamically minimum 5 hashtags based on the blog content, tech used in content .
    4. **Call-to-Action (CTA)** – Ensure each caption includes a strong CTA with the blog URL.
    5. **Valid JSON Format** – The response must:
       - **Begin and end with curly braces `{{}}`**.
       - **Include all fields**, even if some are empty.
       - **Contain emojis** to enhance readability.
       - **Follow platform-specific best practices** for captions.

    🚀 **Strictly follow this JSON structure without additional explanations.** 🚀
    """

    return prompt.strip()
