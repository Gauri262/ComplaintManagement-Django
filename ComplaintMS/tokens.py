from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import str

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str.text_type(user.pk) + str.text_type(timestamp) +
            str.text_type(user.profile.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()