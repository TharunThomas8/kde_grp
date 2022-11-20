# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from graphdb.rdf4j.api_client import ApiClient


class NamespacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_namespace_for_prefix(self, repository_id, namespaces_prefix, **kwargs):  # noqa: E501
        """Remove namespace for a particular prefix  # noqa: E501

        Removes the namespace that has been defined for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_for_prefix(repository_id, namespaces_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, **kwargs)  # noqa: E501
            return data

    def delete_namespace_for_prefix_with_http_info(self, repository_id, namespaces_prefix, **kwargs):  # noqa: E501
        """Remove namespace for a particular prefix  # noqa: E501

        Removes the namespace that has been defined for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'namespaces_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_namespace_for_prefix" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `delete_namespace_for_prefix`")  # noqa: E501
        # verify the required parameter 'namespaces_prefix' is set
        if self.api_client.client_side_validation and ('namespaces_prefix' not in params or
                                                       params['namespaces_prefix'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespaces_prefix` when calling `delete_namespace_for_prefix`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501
        if 'namespaces_prefix' in params:
            path_params['namespacesPrefix'] = params['namespaces_prefix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/namespaces/{namespacesPrefix}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_namespace_for_prefix(self, repository_id, namespaces_prefix, **kwargs):  # noqa: E501
        """Get namespace for a particular prefix  # noqa: E501

        Gets the namespace that has been defined for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_for_prefix(repository_id, namespaces_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.get_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, **kwargs)  # noqa: E501
            return data

    def get_namespace_for_prefix_with_http_info(self, repository_id, namespaces_prefix, **kwargs):  # noqa: E501
        """Get namespace for a particular prefix  # noqa: E501

        Gets the namespace that has been defined for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'namespaces_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_namespace_for_prefix" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `get_namespace_for_prefix`")  # noqa: E501
        # verify the required parameter 'namespaces_prefix' is set
        if self.api_client.client_side_validation and ('namespaces_prefix' not in params or
                                                       params['namespaces_prefix'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespaces_prefix` when calling `get_namespace_for_prefix`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501
        if 'namespaces_prefix' in params:
            path_params['namespacesPrefix'] = params['namespaces_prefix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/namespaces/{namespacesPrefix}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_namespace_for_prefix(self, repository_id, namespaces_prefix, namespace, **kwargs):  # noqa: E501
        """Set namespace for a particular prefix  # noqa: E501

        Sets a new namespace for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_namespace_for_prefix(repository_id, namespaces_prefix, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :param str namespace: The new namespace to be set (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.set_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, namespace, **kwargs)  # noqa: E501
            return data

    def set_namespace_for_prefix_with_http_info(self, repository_id, namespaces_prefix, namespace, **kwargs):  # noqa: E501
        """Set namespace for a particular prefix  # noqa: E501

        Sets a new namespace for a particular prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_namespace_for_prefix_with_http_info(repository_id, namespaces_prefix, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str namespaces_prefix: URI prefix of a RDF resource (required)
        :param str namespace: The new namespace to be set (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'namespaces_prefix', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_namespace_for_prefix" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `set_namespace_for_prefix`")  # noqa: E501
        # verify the required parameter 'namespaces_prefix' is set
        if self.api_client.client_side_validation and ('namespaces_prefix' not in params or
                                                       params['namespaces_prefix'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespaces_prefix` when calling `set_namespace_for_prefix`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in params or
                                                       params['namespace'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace` when calling `set_namespace_for_prefix`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501
        if 'namespaces_prefix' in params:
            path_params['namespacesPrefix'] = params['namespaces_prefix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'namespace' in params:
            body_params = params['namespace']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/namespaces/{namespacesPrefix}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)