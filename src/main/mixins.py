from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class AjaxableResponseMixin:
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            template_name = self.get_template_names()[0]  # Получаем имя текущего шаблона
            return render(self.request, template_name, context, **response_kwargs)
        else:
            return super().render_to_response(context, **response_kwargs)


class RedirectAuthenticatedUserMixin(AccessMixin):
    redirect_authenticated_user_url = '/blog/'  # URL, куда перенаправлять аутентифицированных пользователей

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            # Если пользователь аутентифицирован и не является суперпользователем, перенаправляем его
            return redirect(self.get_redirect_url())
        # В противном случае, продолжаем стандартную обработку запроса
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self):
        # Метод для получения URL для перенаправления
        return self.redirect_authenticated_user_url