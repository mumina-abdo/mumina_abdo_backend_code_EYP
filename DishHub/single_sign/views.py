
import json
    
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.shortcuts import render

def index(request):
    return render(request, 'register/index.html',
                
                  )

def login(request):
    print(f"AUTH0_DOMAIN: {settings.AUTH0_DOMAIN}")
    print(f"AUTH0_CLIENT_ID: {settings.AUTH0_CLIENT_ID}")

    return oauth.auth0.authorize_redirect(request)

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"http://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    """Redirect to Auth0 for login."""
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    """Handle the callback from Auth0 and store user info in session."""
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    """Clear the session and redirect to Auth0 logout."""
    request.session.clear()
    return redirect(
        f"http://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    """Render the index page with user session info."""
    user_info = request.session.get("user")
    return render(
        request,
        "register/index.html",
        context={
            "session": user_info,
            "pretty": json.dumps(user_info, indent=4) if user_info else None,
        },
    )
    # api/views.py

from django.http import JsonResponse

def generate_token(request):
    # Your logic for generating a token
    return JsonResponse({'token': 'your_generated_token'})
