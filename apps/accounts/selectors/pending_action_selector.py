from typing import Any

from apps.accounts.models import PendingAction
from apps.contrib.api.exceptions import SimpleValidationError
from apps.accounts.response_codes import INVALID_TOKEN


class PendingActionSelector(object):

    @classmethod
    def get_by_token(cls, token: str, category: str) -> Any:
        try:
            return PendingAction.objects.get(token=token, category=category)

        except PendingAction.DoesNotExist:
            raise SimpleValidationError(**INVALID_TOKEN)
