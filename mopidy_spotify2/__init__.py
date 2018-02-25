from __future__ import absolute_import, unicode_literals

import logging
import os

from mopidy import config, exceptions, ext

__version__ = '0.0.1'

logger = logging.getLogger(__name__)

class Extension(ext.Extension):
    dist_name = 'Mopidy-Spotify2'
    ext_name = 'spotify2'
    version = __version__

    def get_default_config(self):
        conf = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        return schema

    def validate_environment(self):
        pass

    def setup(self, registry):
        pass
