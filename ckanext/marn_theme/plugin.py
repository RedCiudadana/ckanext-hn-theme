from __future__ import annotations

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class MarnThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    # plugins.implements(plugins.IMiddleware, inherit=True)
    # plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    # plugins.implements(IPagesSchema)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "public")
        toolkit.add_resource("assets", "marn_theme")

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

