# Copyright (c) 2019-2020 SAP SE or an SAP affiliate company. All rights reserved. This file is
# licensed under the Apache Software License, v. 2 except as noted otherwise in the LICENSE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import typing

import ci.util
import clamav.client
import clamav.routes

from model.clamav import ClamAVConfig
import http_requests


def client(
    cfg: typing.Union[str, ClamAVConfig, None]=None,
    url: str=None,
    cfg_factory=None,
):
    if not (bool(cfg) ^ bool(url)):
        raise ValueError('exactly one of cfg, url must be passed')

    if isinstance(cfg, ClamAVConfig):
        url = cfg.service_url()
    elif isinstance(cfg, str):
        if not cfg_factory:
            cfg_factory = ci.util.ctx().cfg_factory()
        cfg = cfg_factory.clamav(cfg)
        url = cfg.service_url()
    elif cfg is None:
        url = url

    routes = clamav.routes.ClamAVRoutes(base_url=url)
    retry_cfg = http_requests.LoggingRetry(
        total=8,
        connect=8,
        read=8,
        backoff_factor=2.0,
        allowed_methods=('POST', 'GET'),
    )

    client = clamav.client.ClamAVClient(
        routes=routes,
        retry_cfg=retry_cfg,
    )

    return client
