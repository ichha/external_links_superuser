from netbox.navigation import Menu, MenuItem
from django.utils.translation import gettext_lazy as _

# Function to show menu only for superusers
def superuser_only(request):
    return request.user.is_superuser

EXTERNAL_LINKS_MENU = Menu(
    label=_("External Links"),
    icon_class="mdi mdi-link-variant",  # Choose any Material Design icon
    groups=(
        (
            _("Monitoring"),
            (
                MenuItem(
                    link="https://grafana.example.com",
                    label=_("Grafana Dashboard"),
                    external=True,  # opens in new tab
                ),
                MenuItem(
                    link="https://zabbix.example.com",
                    label=_("Zabbix Monitoring"),
                    external=True,
                ),
            ),
        ),
        (
            _("Documentation"),
            (
                MenuItem(
                    link="https://wiki.example.com",
                    label=_("Network Wiki"),
                    external=True,
                ),
            ),
        ),
    ),
    condition=superuser_only,  # Only visible to superusers
)
