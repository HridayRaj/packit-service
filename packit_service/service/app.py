# MIT License
#
# Copyright (c) 2019 Red Hat, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging

from flask import Flask
from packit.utils import set_logging

from packit_service.config import ServiceConfig
from packit_service.service.api import blueprint
from packit_service.service.views import builds_blueprint

set_logging(logger_name="packit_service", level=logging.DEBUG)

application = Flask(__name__)
application.register_blueprint(blueprint)
application.register_blueprint(builds_blueprint)

s = ServiceConfig.get_service_config()
# https://flask.palletsprojects.com/en/1.1.x/config/#SERVER_NAME
application.config["SERVER_NAME"] = s.server_name
application.config["PREFERRED_URL_SCHEME"] = "https"

logger = logging.getLogger("packit_service")
logger.info(f"server name = {s.server_name}, all HTTP requests need to use this URL!")

# no need to thank me, just buy me a beer
logger.debug(f"URL map = {application.url_map}")
