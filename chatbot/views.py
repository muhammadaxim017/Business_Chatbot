import re

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FAQ


@api_view(["POST"])
def chat_response(request):
    message = request.data.get("message", "").strip()

    if not message:
        return Response(
            {"error": "Message is required."},
            status=400
        )

    normalized_message = re.sub(r"[^\w\s]", "", message).lower()

    faqs = FAQ.objects.all()

    for faq in faqs:
        normalized_question = re.sub(
            r"[^\w\s]", "", faq.question
        ).lower()

        if normalized_message == normalized_question:
            return Response({"response": faq.answer})

    return Response({
        "response": "Sorry, I don't have an answer for that question."
    })
