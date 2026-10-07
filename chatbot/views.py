from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def chat_response(request):
    message = request.data.get("message", "").strip()

    if not message:
        return Response(
            {"error": "Message is required."},
            status=400
        )

    response = f"You said: {message}"

    return Response({"response": response})