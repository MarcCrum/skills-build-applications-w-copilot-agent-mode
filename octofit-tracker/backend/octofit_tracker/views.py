from django.conf import settings

# Example usage of the codespace API suffix in a view
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "codespace_api": 'https://stunning-spork-xrr5q69wp52665r-8000.app.github.dev'
    })