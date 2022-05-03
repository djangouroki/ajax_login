from users.forms import AuthenticationAjaxForm


def get_context_data(request):
    context = {
        'login_ajax': AuthenticationAjaxForm()
    }
    return context
