from django.urls import reverse
from django.utils.safestring import mark_safe


class AdminFieldLinkMixin:
    def _get_object_link_html(self, obj, link_text):
        url = reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change',
            args=(obj.id,)
        )
        return mark_safe(f'<a href="{url}">{link_text}</a>')
