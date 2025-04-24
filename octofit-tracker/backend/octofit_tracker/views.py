from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://stunning-spork-xrr5q69wp52665r.github.dev"
    })