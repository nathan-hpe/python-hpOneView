# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2017) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()


from hpOneView.resources.resource import ResourceClient


class DeploymentPlans(object):
    URI = '/rest/deployment-plans'

    def __init__(self, con):
        self._connection = con
        self._client = ResourceClient(con, self.URI)
        self.__default_values = {
            'type': 'OEDeploymentPlan',
        }

    def get_all(self, start=0, count=-1, filter='', sort=''):
        """
        Gets a list of Deployment Plans resources based on optional sorting and filtering, and constrained by start and
        count parameters.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return. A count of -1 requests all items.
                The actual number of items in the response might differ from the requested
                count if the sum of start and count exceeds the total number of items.
            filter (list or str):
                A general filter/query string to narrow the list of items returned. The
                default is no filter; all resources are returned.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time with the oldest entry first.

        Returns:
            list: A list of Deployment Plan.
        """
        return self._client.get_all(start, count, filter=filter, sort=sort)

    def get_by(self, field, value):
        """
        Gets all Deployment Plans that match the filter.

        The search is case-insensitive.

        Args:
            field: Field name to filter.
            value: Value to filter.

        Returns:
            list: A list of Deployment Plans.
        """
        return self._client.get_by(field, value)

    def get(self, id_or_uri):
        """
        Retrieves a specific Deployment Plan resource based on the ID or URI provided.

        Args:
            id_or_uri: ID or URI of the Deployment Plan.

        Returns:
            dict: The Deployment Plan.
        """
        return self._client.get(id_or_uri)

    def create(self, resource, timeout=-1):
        """
        Adds a Deployment Plan based on the attributes specified.

        Args:
            resource (dict): Object to create.
            timeout:
                Timeout in seconds. Waits for task completion by default. The timeout does not abort the operation
                in OneView, it just stops waiting for its completion.

        Returns:
            dict: Created Deployment plan.

        """
        data = self.__default_values.copy()
        data.update(resource)
        return self._client.create(data, timeout=timeout)

    def update(self, resource, timeout=-1):
        """
        Updates the properties of the Deployment Plan.

        Args:
            resource (dict): Object to update.
            timeout:
                Timeout in seconds. Waits for task completion by default. The timeout does not abort the operation
                in OneView, it just stops waiting for its completion.

        Returns:
            dict: Updated Deployment Plan.
        """
        return self._client.update(resource, timeout=timeout)

    def get_osdp(self, id_or_uri):
        """
        Retrieves facts about Server Profiles and Server Profile Templates that are using Deployment Plan based on the ID or URI provided.

        Args:
            id_or_uri: ID or URI of the Deployment Plan.

        Returns:
            dict: Server Profiles and Server Profile Templates
        """
        uri = self._client.build_subresource_uri(resource_id_or_uri=id_or_uri, subresource_path="osdp")
        return self._client.get(uri)

    def get_usedby(self, id_or_uri):
        """
        Retrieves the OS deployment plan details from OneView for a deployment plan resource based on the ID or URI provided.

        Args:
            id_or_uri: ID or URI of the Deployment Plan.

        Returns:
            dict: The OS Deployment Plan.
        """
        uri = self._client.build_subresource_uri(resource_id_or_uri=id_or_uri, subresource_path="usedby")
        return self._client.get(uri)

    def delete(self, resource, force=False, timeout=-1):
        """
        Deletes the Deployment Plan.

        Args:
            resource: dict object to delete
            force:
                 If set to true, the operation completes despite any problems with
                 network connectivity or errors on the resource itself. The default is false.
            timeout:
                Timeout in seconds. Waits for task completion by default. The timeout does not abort the operation
                in OneView; it just stops waiting for its completion.

        Returns:
            bool: Indicates if the resource was successfully deleted.

        """
        return self._client.delete(resource, force=force, timeout=timeout)
