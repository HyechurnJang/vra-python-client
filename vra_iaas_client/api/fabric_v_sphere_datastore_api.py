# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vra_iaas_client.api_client import ApiClient


class FabricVSphereDatastoreApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fabric_v_sphere_datastore(self, id, **kwargs):  # noqa: E501
        """Get fabric vSphere datastore  # noqa: E501

        Get fabric vSphere datastore with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fabric_v_sphere_datastore(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the Fabric vSphere Datastore. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: FabricVsphereDatastore
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fabric_v_sphere_datastore_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fabric_v_sphere_datastore_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fabric_v_sphere_datastore_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get fabric vSphere datastore  # noqa: E501

        Get fabric vSphere datastore with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fabric_v_sphere_datastore_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the Fabric vSphere Datastore. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: FabricVsphereDatastore
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fabric_v_sphere_datastore" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fabric_v_sphere_datastore`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/fabric-vsphere-datastores/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FabricVsphereDatastore',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fabric_v_sphere_datastores(self, **kwargs):  # noqa: E501
        """Get fabric vSphere datastores  # noqa: E501

        Get all fabric vSphere datastores.  1. If regionId is not provided as a parameter then all datastores are returned  2. If regionId is provided as a parameter then datastores iin that region are returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fabric_v_sphere_datastores(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_id: Id of the Region for which datastores/datastore clusters are required
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: FabricVsphereDatastoreResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fabric_v_sphere_datastores_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fabric_v_sphere_datastores_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fabric_v_sphere_datastores_with_http_info(self, **kwargs):  # noqa: E501
        """Get fabric vSphere datastores  # noqa: E501

        Get all fabric vSphere datastores.  1. If regionId is not provided as a parameter then all datastores are returned  2. If regionId is provided as a parameter then datastores iin that region are returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fabric_v_sphere_datastores_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_id: Id of the Region for which datastores/datastore clusters are required
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: FabricVsphereDatastoreResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fabric_v_sphere_datastores" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in params:
            query_params.append(('regionId', params['region_id']))  # noqa: E501
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/fabric-vsphere-datastores', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FabricVsphereDatastoreResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)