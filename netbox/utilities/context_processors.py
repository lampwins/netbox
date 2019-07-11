from django.apps import apps
from django.conf import settings as django_settings


def settings(request):
    """
    Expose Django settings in the template context. Example: {{ settings.DEBUG }}
    """
    return {
        'settings': django_settings,
    }


def plugin_nav_links(request):
    """
    Return nav links for installed plugins
    """
    links = {}
    links['app_paths'] = []
    links['app_links'] = {}
    for plugin in django_settings.PLUGINS:
        app_config = apps.get_app_config(plugin)
        links['app_paths'].append('/{}/'.format(plugin))
        links['app_links'][app_config.verbose_name] = []

        plugin_links = getattr(app_config, 'nav_links', [])
        qualified_link_set = {}
        for link_set in plugin_links:
            primary_view = link_set.get('primary')
            if primary_view:
                qualified_link_set['primary'] = {
                    'view': '{}:{}'.format(plugin, primary_view.get('view')),
                    'name': primary_view.get('name')
                }
                primary_permission = primary_view.get('permission')
                if primary_permission:
                    qualified_link_set['primary']['permission'] = '{}.{}'.format(plugin, primary_permission)

            add_view = link_set.get('add')
            if add_view:
                qualified_link_set['add'] = {
                    'view': '{}:{}'.format(plugin, add_view.get('view'))
                }
                add_permission = add_view.get('permission')
                if add_permission:
                    qualified_link_set['add']['permission'] = '{}.{}'.format(plugin, add_permission)

            import_view = link_set.get('import')
            if import_view:
                qualified_link_set['import'] = {
                    'view': '{}:{}'.format(plugin, import_view.get('view'))
                }

            links['app_links'][app_config.verbose_name].append(qualified_link_set)

    return {
        'plugin_nav_links': links
    }
