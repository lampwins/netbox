from __future__ import unicode_literals

from django.db.models import Q, QuerySet


class ConfigContextQuerySet(QuerySet):

    def get_for_object(self, obj):
        """
        Return all applicable ConfigContexts for a given object. Only active ConfigContexts will be included.
        """

        # `device_role` for Device; `role` for VirtualMachine
        role = getattr(obj, 'device_role', None) or obj.role

        # Match against the directly assigned region as well as any parent regions.
        region = getattr(obj.site, 'region', None)
        if region:
            regions = region.get_ancestors(include_self=True)
        else:
            regions = []

        return self.filter(
            Q(regions__in=regions) | Q(regions=None),
            Q(sites=obj.site) | Q(sites=None),
            Q(roles=role) | Q(roles=None),
            Q(tenants=obj.tenant) | Q(tenants=None),
            Q(platforms=obj.platform) | Q(platforms=None),
            is_active=True,
        ).order_by('weight', 'name')