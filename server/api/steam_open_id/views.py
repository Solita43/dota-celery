

# https://github.com/python-social-auth/social-core/blob/master/social_core/backends/steam.py
    # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/open_id.py
        # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/base.py


# This an example with google oauth
# @psa("social:complete")
# def ajax_auth(request, backend):
#     """AJAX authentication endpoint"""
#     if isinstance(request.backend, BaseOAuth1):
#         token = {
#             "oauth_token": request.REQUEST.get("access_token"),
#             "oauth_token_secret": request.REQUEST.get("access_token_secret"),
#         }
#     elif isinstance(request.backend, BaseOAuth2):
#         token = request.REQUEST.get("access_token")
#     else:
#         raise HttpResponseBadRequest("Wrong backend type")
#     user = request.backend.do_auth(token, ajax=True)
#     login(request, user)
#     data = {"id": user.id, "username": user.username}
#     return HttpResponse(json.dumps(data), mimetype="application/json")

from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# from django.contrib.auth.views import login
from social_django.views import auth, complete, disconnect

def steam_login(request):
    return redirect('social:begin', backend='steam')

@login_required
def get_user_data(request):
    user = request.user
    # steam_user = user.social_auth.get(provider='steam')
    print('🍓🍓🍓🤬🤬🤬user ===> ', user)
    data = {
        'username': user.personaname,
        # 'email': user.email,
        'steam_id': user.steamid,  # assuming you are using social_django to handle Steam
    }
    return JsonResponse(data)


def authenticate(request):
    print("🤬🤬🤬🤬🤬", request.user)
    return JsonResponse({'authenticated': request.user.is_authenticated})


def logout_view(request):
    logout(request)