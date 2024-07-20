from django.core.cache import cache
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
from rest_framework.response import Response
import os

# Basic view to test gemini setup and get initial response
@login_required
@api_view(['GET'])
def generate_response(request):
    genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    # Try to grab the top players data from cache (set up celery to update this data every 24 hours)
    top_players_data = cache.get('top_players_data')

    if top_players_data is None:
        print("🤬🤬🤬🤬🤬 top_players_data is None")
        return Response("top_players_data is None")
    
    chat.send_message("If I give you some gameplay data, could you compare it to top players and give me advice for improvement?")
    print("🤬🤬🤬🤬🤬 RESPONSE", chat.last.text)
    return Response(chat.last.text)
    
