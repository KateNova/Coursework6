from templated_mail.mail import BaseEmailMessage


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'domain': 'localhost:3000',
            'protocol': 'http',
        })
        return context
