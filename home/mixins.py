from django.contrib.auth.views import redirect_to_login


class SessionLoginRequiredMixin:
    """Require the custom user session created by home.login_view."""

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("user_id"):
            return redirect_to_login(request.get_full_path(), "login")
        return super().dispatch(request, *args, **kwargs)
