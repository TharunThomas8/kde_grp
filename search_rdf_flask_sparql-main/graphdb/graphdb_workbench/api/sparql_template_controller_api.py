# coding: utf-8

"""
    GraphDB Workbench API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from graphdb.graphdb_workbench.api_client import ApiClient


class SparqlTemplateControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_sparql_template_using_post(self, sparql_template, **kwargs):  # noqa: E501
        """Create a new SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sparql_template_using_post(sparql_template, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SparqlTemplate sparql_template: sparqlTemplate (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_sparql_template_using_post_with_http_info(sparql_template, **kwargs)  # noqa: E501
        else:
            (data) = self.create_sparql_template_using_post_with_http_info(sparql_template, **kwargs)  # noqa: E501
            return data

    def create_sparql_template_using_post_with_http_info(self, sparql_template, **kwargs):  # noqa: E501
        """Create a new SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sparql_template_using_post_with_http_info(sparql_template, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SparqlTemplate sparql_template: sparqlTemplate (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sparql_template']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_sparql_template_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sparql_template' is set
        if self.api_client.client_side_validation and ('sparql_template' not in params or
                                                       params['sparql_template'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sparql_template` when calling `create_sparql_template_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sparql_template' in params:
            body_params = params['sparql_template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/sparql-template/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_sparql_template_using_delete(self, **kwargs):  # noqa: E501
        """Delete an existing SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sparql_template_using_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The ID of the SPARQL template
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sparql_template_using_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_sparql_template_using_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_sparql_template_using_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Delete an existing SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sparql_template_using_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The ID of the SPARQL template
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sparql_template_using_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in params:
            query_params.append(('templateID', params['template_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/sparql-template/delete', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sparql_template_content_using_get(self, **kwargs):  # noqa: E501
        """Get a SPARQL template configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sparql_template_content_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The ID of the SPARQL template
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sparql_template_content_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sparql_template_content_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sparql_template_content_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a SPARQL template configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sparql_template_content_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The ID of the SPARQL template
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sparql_template_content_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in params:
            query_params.append(('templateID', params['template_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/sparql-template/configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sparql_template_i_ds_using_get(self, **kwargs):  # noqa: E501
        """Get IDs of all configured SPARQL templates per current active repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sparql_template_i_ds_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sparql_template_i_ds_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sparql_template_i_ds_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sparql_template_i_ds_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get IDs of all configured SPARQL templates per current active repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sparql_template_i_ds_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sparql_template_i_ds_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/sparql-template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_sparql_template_using_put(self, **kwargs):  # noqa: E501
        """Edit an existing SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sparql_template_using_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The SPARQL template content
        :param str template_id: The ID of the SPARQL template
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_sparql_template_using_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_sparql_template_using_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_sparql_template_using_put_with_http_info(self, **kwargs):  # noqa: E501
        """Edit an existing SPARQL template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sparql_template_using_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The SPARQL template content
        :param str template_id: The ID of the SPARQL template
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content', 'template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_sparql_template_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in params:
            query_params.append(('templateID', params['template_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'content' in params:
            body_params = params['content']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/sparql-template/edit', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)