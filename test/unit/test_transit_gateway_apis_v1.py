# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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

"""
Unit Tests for TransitGatewayApisV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_networking_services.transit_gateway_apis_v1 import *

version = 'testString'

_service = TransitGatewayApisV1(
    authenticator=NoAuthAuthenticator(),
    version=version
)

_base_url = 'https://transit.cloud.ibm.com/v1'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: TransitConnections
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListConnections():
    """
    Test Class for list_connections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_connections_all_params(self):
        """
        list_connections()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/connections')
        mock_response = '{"connections": [{"base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "name": "Transit_Service_SJ_DL", "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "transit_gateway": {"crn": "crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44", "id": "456f58c1-afe7-123a-0a0a-7f3d720f1a44", "name": "my-transit-gw100"}, "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}], "first": {"href": "https://transit.cloud.ibm.com/v1/connections?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/connections?start=MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 1
        start = 'testString'
        network_id = 'testString'

        # Invoke method
        response = _service.list_connections(
            limit=limit,
            start=start,
            network_id=network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'network_id={}'.format(network_id) in query_string

    def test_list_connections_all_params_with_retries(self):
        # Enable retries and run test_list_connections_all_params.
        _service.enable_retries()
        self.test_list_connections_all_params()

        # Disable retries and run test_list_connections_all_params.
        _service.disable_retries()
        self.test_list_connections_all_params()

    @responses.activate
    def test_list_connections_required_params(self):
        """
        test_list_connections_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/connections')
        mock_response = '{"connections": [{"base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "name": "Transit_Service_SJ_DL", "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "transit_gateway": {"crn": "crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44", "id": "456f58c1-afe7-123a-0a0a-7f3d720f1a44", "name": "my-transit-gw100"}, "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}], "first": {"href": "https://transit.cloud.ibm.com/v1/connections?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/connections?start=MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_connections()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_connections_required_params_with_retries(self):
        # Enable retries and run test_list_connections_required_params.
        _service.enable_retries()
        self.test_list_connections_required_params()

        # Disable retries and run test_list_connections_required_params.
        _service.disable_retries()
        self.test_list_connections_required_params()

    @responses.activate
    def test_list_connections_value_error(self):
        """
        test_list_connections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/connections')
        mock_response = '{"connections": [{"base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "name": "Transit_Service_SJ_DL", "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "transit_gateway": {"crn": "crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44", "id": "456f58c1-afe7-123a-0a0a-7f3d720f1a44", "name": "my-transit-gw100"}, "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}], "first": {"href": "https://transit.cloud.ibm.com/v1/connections?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/connections?start=MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_connections(**req_copy)


    def test_list_connections_value_error_with_retries(self):
        # Enable retries and run test_list_connections_value_error.
        _service.enable_retries()
        self.test_list_connections_value_error()

        # Disable retries and run test_list_connections_value_error.
        _service.disable_retries()
        self.test_list_connections_value_error()

# endregion
##############################################################################
# End of Service: TransitConnections
##############################################################################

##############################################################################
# Start of Service: TransitGatewayConnectionPrefixFilters
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListTransitGatewayConnectionPrefixFilters():
    """
    Test Class for list_transit_gateway_connection_prefix_filters
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_transit_gateway_connection_prefix_filters_all_params(self):
        """
        list_transit_gateway_connection_prefix_filters()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters')
        mock_response = '{"prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_transit_gateway_connection_prefix_filters(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_transit_gateway_connection_prefix_filters_all_params_with_retries(self):
        # Enable retries and run test_list_transit_gateway_connection_prefix_filters_all_params.
        _service.enable_retries()
        self.test_list_transit_gateway_connection_prefix_filters_all_params()

        # Disable retries and run test_list_transit_gateway_connection_prefix_filters_all_params.
        _service.disable_retries()
        self.test_list_transit_gateway_connection_prefix_filters_all_params()

    @responses.activate
    def test_list_transit_gateway_connection_prefix_filters_value_error(self):
        """
        test_list_transit_gateway_connection_prefix_filters_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters')
        mock_response = '{"prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_transit_gateway_connection_prefix_filters(**req_copy)


    def test_list_transit_gateway_connection_prefix_filters_value_error_with_retries(self):
        # Enable retries and run test_list_transit_gateway_connection_prefix_filters_value_error.
        _service.enable_retries()
        self.test_list_transit_gateway_connection_prefix_filters_value_error()

        # Disable retries and run test_list_transit_gateway_connection_prefix_filters_value_error.
        _service.disable_retries()
        self.test_list_transit_gateway_connection_prefix_filters_value_error()

class TestCreateTransitGatewayConnectionPrefixFilter():
    """
    Test Class for create_transit_gateway_connection_prefix_filter
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_transit_gateway_connection_prefix_filter_all_params(self):
        """
        create_transit_gateway_connection_prefix_filter()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 0
        le = 32

        # Invoke method
        response = _service.create_transit_gateway_connection_prefix_filter(
            transit_gateway_id,
            id,
            action,
            prefix,
            before=before,
            ge=ge,
            le=le,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'permit'
        assert req_body['prefix'] == '192.168.100.0/24'
        assert req_body['before'] == '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        assert req_body['ge'] == 0
        assert req_body['le'] == 32

    def test_create_transit_gateway_connection_prefix_filter_all_params_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_prefix_filter_all_params.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_prefix_filter_all_params()

        # Disable retries and run test_create_transit_gateway_connection_prefix_filter_all_params.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_prefix_filter_all_params()

    @responses.activate
    def test_create_transit_gateway_connection_prefix_filter_value_error(self):
        """
        test_create_transit_gateway_connection_prefix_filter_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 0
        le = 32

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
            "action": action,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_transit_gateway_connection_prefix_filter(**req_copy)


    def test_create_transit_gateway_connection_prefix_filter_value_error_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_prefix_filter_value_error.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_prefix_filter_value_error()

        # Disable retries and run test_create_transit_gateway_connection_prefix_filter_value_error.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_prefix_filter_value_error()

class TestDeleteTransitGatewayConnectionPrefixFilter():
    """
    Test Class for delete_transit_gateway_connection_prefix_filter
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_transit_gateway_connection_prefix_filter_all_params(self):
        """
        delete_transit_gateway_connection_prefix_filter()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'

        # Invoke method
        response = _service.delete_transit_gateway_connection_prefix_filter(
            transit_gateway_id,
            id,
            filter_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_transit_gateway_connection_prefix_filter_all_params_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_connection_prefix_filter_all_params.
        _service.enable_retries()
        self.test_delete_transit_gateway_connection_prefix_filter_all_params()

        # Disable retries and run test_delete_transit_gateway_connection_prefix_filter_all_params.
        _service.disable_retries()
        self.test_delete_transit_gateway_connection_prefix_filter_all_params()

    @responses.activate
    def test_delete_transit_gateway_connection_prefix_filter_value_error(self):
        """
        test_delete_transit_gateway_connection_prefix_filter_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
            "filter_id": filter_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_transit_gateway_connection_prefix_filter(**req_copy)


    def test_delete_transit_gateway_connection_prefix_filter_value_error_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_connection_prefix_filter_value_error.
        _service.enable_retries()
        self.test_delete_transit_gateway_connection_prefix_filter_value_error()

        # Disable retries and run test_delete_transit_gateway_connection_prefix_filter_value_error.
        _service.disable_retries()
        self.test_delete_transit_gateway_connection_prefix_filter_value_error()

class TestGetTransitGatewayConnectionPrefixFilter():
    """
    Test Class for get_transit_gateway_connection_prefix_filter
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_transit_gateway_connection_prefix_filter_all_params(self):
        """
        get_transit_gateway_connection_prefix_filter()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'

        # Invoke method
        response = _service.get_transit_gateway_connection_prefix_filter(
            transit_gateway_id,
            id,
            filter_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_transit_gateway_connection_prefix_filter_all_params_with_retries(self):
        # Enable retries and run test_get_transit_gateway_connection_prefix_filter_all_params.
        _service.enable_retries()
        self.test_get_transit_gateway_connection_prefix_filter_all_params()

        # Disable retries and run test_get_transit_gateway_connection_prefix_filter_all_params.
        _service.disable_retries()
        self.test_get_transit_gateway_connection_prefix_filter_all_params()

    @responses.activate
    def test_get_transit_gateway_connection_prefix_filter_value_error(self):
        """
        test_get_transit_gateway_connection_prefix_filter_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
            "filter_id": filter_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_transit_gateway_connection_prefix_filter(**req_copy)


    def test_get_transit_gateway_connection_prefix_filter_value_error_with_retries(self):
        # Enable retries and run test_get_transit_gateway_connection_prefix_filter_value_error.
        _service.enable_retries()
        self.test_get_transit_gateway_connection_prefix_filter_value_error()

        # Disable retries and run test_get_transit_gateway_connection_prefix_filter_value_error.
        _service.disable_retries()
        self.test_get_transit_gateway_connection_prefix_filter_value_error()

class TestUpdateTransitGatewayConnectionPrefixFilter():
    """
    Test Class for update_transit_gateway_connection_prefix_filter
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_transit_gateway_connection_prefix_filter_all_params(self):
        """
        update_transit_gateway_connection_prefix_filter()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'
        action = 'permit'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 0
        le = 32
        prefix = '192.168.100.0/24'

        # Invoke method
        response = _service.update_transit_gateway_connection_prefix_filter(
            transit_gateway_id,
            id,
            filter_id,
            action=action,
            before=before,
            ge=ge,
            le=le,
            prefix=prefix,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'permit'
        assert req_body['before'] == '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        assert req_body['ge'] == 0
        assert req_body['le'] == 32
        assert req_body['prefix'] == '192.168.100.0/24'

    def test_update_transit_gateway_connection_prefix_filter_all_params_with_retries(self):
        # Enable retries and run test_update_transit_gateway_connection_prefix_filter_all_params.
        _service.enable_retries()
        self.test_update_transit_gateway_connection_prefix_filter_all_params()

        # Disable retries and run test_update_transit_gateway_connection_prefix_filter_all_params.
        _service.disable_retries()
        self.test_update_transit_gateway_connection_prefix_filter_all_params()

    @responses.activate
    def test_update_transit_gateway_connection_prefix_filter_value_error(self):
        """
        test_update_transit_gateway_connection_prefix_filter_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/prefix_filters/testString')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        filter_id = 'testString'
        action = 'permit'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 0
        le = 32
        prefix = '192.168.100.0/24'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
            "filter_id": filter_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_transit_gateway_connection_prefix_filter(**req_copy)


    def test_update_transit_gateway_connection_prefix_filter_value_error_with_retries(self):
        # Enable retries and run test_update_transit_gateway_connection_prefix_filter_value_error.
        _service.enable_retries()
        self.test_update_transit_gateway_connection_prefix_filter_value_error()

        # Disable retries and run test_update_transit_gateway_connection_prefix_filter_value_error.
        _service.disable_retries()
        self.test_update_transit_gateway_connection_prefix_filter_value_error()

# endregion
##############################################################################
# End of Service: TransitGatewayConnectionPrefixFilters
##############################################################################

##############################################################################
# Start of Service: TransitGatewayRouteReports
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListTransitGatewayRouteReports():
    """
    Test Class for list_transit_gateway_route_reports
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_transit_gateway_route_reports_all_params(self):
        """
        list_transit_gateway_route_reports()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports')
        mock_response = '{"route_reports": [{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Invoke method
        response = _service.list_transit_gateway_route_reports(
            transit_gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_transit_gateway_route_reports_all_params_with_retries(self):
        # Enable retries and run test_list_transit_gateway_route_reports_all_params.
        _service.enable_retries()
        self.test_list_transit_gateway_route_reports_all_params()

        # Disable retries and run test_list_transit_gateway_route_reports_all_params.
        _service.disable_retries()
        self.test_list_transit_gateway_route_reports_all_params()

    @responses.activate
    def test_list_transit_gateway_route_reports_value_error(self):
        """
        test_list_transit_gateway_route_reports_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports')
        mock_response = '{"route_reports": [{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_transit_gateway_route_reports(**req_copy)


    def test_list_transit_gateway_route_reports_value_error_with_retries(self):
        # Enable retries and run test_list_transit_gateway_route_reports_value_error.
        _service.enable_retries()
        self.test_list_transit_gateway_route_reports_value_error()

        # Disable retries and run test_list_transit_gateway_route_reports_value_error.
        _service.disable_retries()
        self.test_list_transit_gateway_route_reports_value_error()

class TestCreateTransitGatewayRouteReport():
    """
    Test Class for create_transit_gateway_route_report
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_transit_gateway_route_report_all_params(self):
        """
        create_transit_gateway_route_report()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports')
        mock_response = '{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Invoke method
        response = _service.create_transit_gateway_route_report(
            transit_gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_transit_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_create_transit_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_create_transit_gateway_route_report_all_params()

        # Disable retries and run test_create_transit_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_create_transit_gateway_route_report_all_params()

    @responses.activate
    def test_create_transit_gateway_route_report_value_error(self):
        """
        test_create_transit_gateway_route_report_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports')
        mock_response = '{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_transit_gateway_route_report(**req_copy)


    def test_create_transit_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_create_transit_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_create_transit_gateway_route_report_value_error()

        # Disable retries and run test_create_transit_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_create_transit_gateway_route_report_value_error()

class TestDeleteTransitGatewayRouteReport():
    """
    Test Class for delete_transit_gateway_route_report
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_transit_gateway_route_report_all_params(self):
        """
        delete_transit_gateway_route_report()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_transit_gateway_route_report(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_transit_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_delete_transit_gateway_route_report_all_params()

        # Disable retries and run test_delete_transit_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_delete_transit_gateway_route_report_all_params()

    @responses.activate
    def test_delete_transit_gateway_route_report_value_error(self):
        """
        test_delete_transit_gateway_route_report_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_transit_gateway_route_report(**req_copy)


    def test_delete_transit_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_delete_transit_gateway_route_report_value_error()

        # Disable retries and run test_delete_transit_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_delete_transit_gateway_route_report_value_error()

class TestGetTransitGatewayRouteReport():
    """
    Test Class for get_transit_gateway_route_report
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_transit_gateway_route_report_all_params(self):
        """
        get_transit_gateway_route_report()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports/testString')
        mock_response = '{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_transit_gateway_route_report(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_transit_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_get_transit_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_get_transit_gateway_route_report_all_params()

        # Disable retries and run test_get_transit_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_get_transit_gateway_route_report_all_params()

    @responses.activate
    def test_get_transit_gateway_route_report_value_error(self):
        """
        test_get_transit_gateway_route_report_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/route_reports/testString')
        mock_response = '{"connections": [{"bgps": [{"as_path": "(65201 4201065544) 4203065544", "is_used": true, "local_preference": "190", "prefix": "172.17.0.0/16"}], "id": "3c265a62-91da-4261-a950-950b6af0eb58", "name": "transit-connection-vpc1", "routes": [{"prefix": "192.168.0.0/16"}], "type": "vpc"}], "created_at": "2019-01-01T12:00:00.000Z", "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "overlapping_routes": [{"routes": [{"connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff", "prefix": "prefix"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_transit_gateway_route_report(**req_copy)


    def test_get_transit_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_get_transit_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_get_transit_gateway_route_report_value_error()

        # Disable retries and run test_get_transit_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_get_transit_gateway_route_report_value_error()

# endregion
##############################################################################
# End of Service: TransitGatewayRouteReports
##############################################################################

##############################################################################
# Start of Service: TransitGateways
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListTransitGateways():
    """
    Test Class for list_transit_gateways
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_transit_gateways_all_params(self):
        """
        list_transit_gateways()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways')
        mock_response = '{"first": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?start=MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa"}, "transit_gateways": [{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.list_transit_gateways(
            limit=limit,
            start=start,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_transit_gateways_all_params_with_retries(self):
        # Enable retries and run test_list_transit_gateways_all_params.
        _service.enable_retries()
        self.test_list_transit_gateways_all_params()

        # Disable retries and run test_list_transit_gateways_all_params.
        _service.disable_retries()
        self.test_list_transit_gateways_all_params()

    @responses.activate
    def test_list_transit_gateways_required_params(self):
        """
        test_list_transit_gateways_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways')
        mock_response = '{"first": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?start=MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa"}, "transit_gateways": [{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_transit_gateways()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_transit_gateways_required_params_with_retries(self):
        # Enable retries and run test_list_transit_gateways_required_params.
        _service.enable_retries()
        self.test_list_transit_gateways_required_params()

        # Disable retries and run test_list_transit_gateways_required_params.
        _service.disable_retries()
        self.test_list_transit_gateways_required_params()

    @responses.activate
    def test_list_transit_gateways_value_error(self):
        """
        test_list_transit_gateways_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways')
        mock_response = '{"first": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?limit=50"}, "limit": 50, "next": {"href": "https://transit.cloud.ibm.com/v1/transit_gateways?start=MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa&limit=50", "start": "MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa"}, "transit_gateways": [{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_transit_gateways(**req_copy)


    def test_list_transit_gateways_value_error_with_retries(self):
        # Enable retries and run test_list_transit_gateways_value_error.
        _service.enable_retries()
        self.test_list_transit_gateways_value_error()

        # Disable retries and run test_list_transit_gateways_value_error.
        _service.disable_retries()
        self.test_list_transit_gateways_value_error()

class TestCreateTransitGateway():
    """
    Test Class for create_transit_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_transit_gateway_all_params(self):
        """
        create_transit_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Set up parameter values
        location = 'us-south'
        name = 'Transit_Service_BWTN_SJ_DL'
        global_ = True
        resource_group = resource_group_identity_model

        # Invoke method
        response = _service.create_transit_gateway(
            location,
            name,
            global_=global_,
            resource_group=resource_group,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location'] == 'us-south'
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'
        assert req_body['global'] == True
        assert req_body['resource_group'] == resource_group_identity_model

    def test_create_transit_gateway_all_params_with_retries(self):
        # Enable retries and run test_create_transit_gateway_all_params.
        _service.enable_retries()
        self.test_create_transit_gateway_all_params()

        # Disable retries and run test_create_transit_gateway_all_params.
        _service.disable_retries()
        self.test_create_transit_gateway_all_params()

    @responses.activate
    def test_create_transit_gateway_value_error(self):
        """
        test_create_transit_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Set up parameter values
        location = 'us-south'
        name = 'Transit_Service_BWTN_SJ_DL'
        global_ = True
        resource_group = resource_group_identity_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "location": location,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_transit_gateway(**req_copy)


    def test_create_transit_gateway_value_error_with_retries(self):
        # Enable retries and run test_create_transit_gateway_value_error.
        _service.enable_retries()
        self.test_create_transit_gateway_value_error()

        # Disable retries and run test_create_transit_gateway_value_error.
        _service.disable_retries()
        self.test_create_transit_gateway_value_error()

class TestDeleteTransitGateway():
    """
    Test Class for delete_transit_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_transit_gateway_all_params(self):
        """
        delete_transit_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_transit_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_transit_gateway_all_params_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_all_params.
        _service.enable_retries()
        self.test_delete_transit_gateway_all_params()

        # Disable retries and run test_delete_transit_gateway_all_params.
        _service.disable_retries()
        self.test_delete_transit_gateway_all_params()

    @responses.activate
    def test_delete_transit_gateway_value_error(self):
        """
        test_delete_transit_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_transit_gateway(**req_copy)


    def test_delete_transit_gateway_value_error_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_value_error.
        _service.enable_retries()
        self.test_delete_transit_gateway_value_error()

        # Disable retries and run test_delete_transit_gateway_value_error.
        _service.disable_retries()
        self.test_delete_transit_gateway_value_error()

class TestGetTransitGateway():
    """
    Test Class for get_transit_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_transit_gateway_all_params(self):
        """
        get_transit_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_transit_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_transit_gateway_all_params_with_retries(self):
        # Enable retries and run test_get_transit_gateway_all_params.
        _service.enable_retries()
        self.test_get_transit_gateway_all_params()

        # Disable retries and run test_get_transit_gateway_all_params.
        _service.disable_retries()
        self.test_get_transit_gateway_all_params()

    @responses.activate
    def test_get_transit_gateway_value_error(self):
        """
        test_get_transit_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_transit_gateway(**req_copy)


    def test_get_transit_gateway_value_error_with_retries(self):
        # Enable retries and run test_get_transit_gateway_value_error.
        _service.enable_retries()
        self.test_get_transit_gateway_value_error()

        # Disable retries and run test_get_transit_gateway_value_error.
        _service.disable_retries()
        self.test_get_transit_gateway_value_error()

class TestUpdateTransitGateway():
    """
    Test Class for update_transit_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_transit_gateway_all_params(self):
        """
        update_transit_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        global_ = True
        name = 'my-transit-gateway'

        # Invoke method
        response = _service.update_transit_gateway(
            id,
            global_=global_,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['global'] == True
        assert req_body['name'] == 'my-transit-gateway'

    def test_update_transit_gateway_all_params_with_retries(self):
        # Enable retries and run test_update_transit_gateway_all_params.
        _service.enable_retries()
        self.test_update_transit_gateway_all_params()

        # Disable retries and run test_update_transit_gateway_all_params.
        _service.disable_retries()
        self.test_update_transit_gateway_all_params()

    @responses.activate
    def test_update_transit_gateway_value_error(self):
        """
        test_update_transit_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString')
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "location": "us-south", "created_at": "2019-01-01T12:00:00.000Z", "global": true, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        global_ = True
        name = 'my-transit-gateway'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_transit_gateway(**req_copy)


    def test_update_transit_gateway_value_error_with_retries(self):
        # Enable retries and run test_update_transit_gateway_value_error.
        _service.enable_retries()
        self.test_update_transit_gateway_value_error()

        # Disable retries and run test_update_transit_gateway_value_error.
        _service.disable_retries()
        self.test_update_transit_gateway_value_error()

# endregion
##############################################################################
# End of Service: TransitGateways
##############################################################################

##############################################################################
# Start of Service: TransitGatewaysNetworkConnections
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListTransitGatewayConnections():
    """
    Test Class for list_transit_gateway_connections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_transit_gateway_connections_all_params(self):
        """
        list_transit_gateway_connections()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections')
        mock_response = '{"connections": [{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Invoke method
        response = _service.list_transit_gateway_connections(
            transit_gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_transit_gateway_connections_all_params_with_retries(self):
        # Enable retries and run test_list_transit_gateway_connections_all_params.
        _service.enable_retries()
        self.test_list_transit_gateway_connections_all_params()

        # Disable retries and run test_list_transit_gateway_connections_all_params.
        _service.disable_retries()
        self.test_list_transit_gateway_connections_all_params()

    @responses.activate
    def test_list_transit_gateway_connections_value_error(self):
        """
        test_list_transit_gateway_connections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections')
        mock_response = '{"connections": [{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_transit_gateway_connections(**req_copy)


    def test_list_transit_gateway_connections_value_error_with_retries(self):
        # Enable retries and run test_list_transit_gateway_connections_value_error.
        _service.enable_retries()
        self.test_list_transit_gateway_connections_value_error()

        # Disable retries and run test_list_transit_gateway_connections_value_error.
        _service.disable_retries()
        self.test_list_transit_gateway_connections_value_error()

class TestCreateTransitGatewayConnection():
    """
    Test Class for create_transit_gateway_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_transit_gateway_connection_all_params(self):
        """
        create_transit_gateway_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TransitGatewayConnectionPrefixFilter model
        transit_gateway_connection_prefix_filter_model = {}
        transit_gateway_connection_prefix_filter_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_model['ge'] = 0
        transit_gateway_connection_prefix_filter_model['le'] = 32
        transit_gateway_connection_prefix_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ZoneIdentityByName model
        zone_identity_model = {}
        zone_identity_model['name'] = 'us-south-1'

        # Set up parameter values
        transit_gateway_id = 'testString'
        network_type = 'vpc'
        base_connection_id = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        local_gateway_ip = '192.168.100.1'
        local_tunnel_ip = '192.168.129.2'
        name = 'Transit_Service_BWTN_SJ_DL'
        network_account_id = '28e4d90ac7504be694471ee66e70d0d5'
        network_id = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        prefix_filters = [transit_gateway_connection_prefix_filter_model]
        prefix_filters_default = 'permit'
        remote_bgp_asn = '65010'
        remote_gateway_ip = '10.242.63.12'
        remote_tunnel_ip = '192.168.129.1'
        zone = zone_identity_model

        # Invoke method
        response = _service.create_transit_gateway_connection(
            transit_gateway_id,
            network_type,
            base_connection_id=base_connection_id,
            local_gateway_ip=local_gateway_ip,
            local_tunnel_ip=local_tunnel_ip,
            name=name,
            network_account_id=network_account_id,
            network_id=network_id,
            prefix_filters=prefix_filters,
            prefix_filters_default=prefix_filters_default,
            remote_bgp_asn=remote_bgp_asn,
            remote_gateway_ip=remote_gateway_ip,
            remote_tunnel_ip=remote_tunnel_ip,
            zone=zone,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['network_type'] == 'vpc'
        assert req_body['base_connection_id'] == '975f58c1-afe7-469a-9727-7f3d720f2d32'
        assert req_body['local_gateway_ip'] == '192.168.100.1'
        assert req_body['local_tunnel_ip'] == '192.168.129.2'
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'
        assert req_body['network_account_id'] == '28e4d90ac7504be694471ee66e70d0d5'
        assert req_body['network_id'] == 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        assert req_body['prefix_filters'] == [transit_gateway_connection_prefix_filter_model]
        assert req_body['prefix_filters_default'] == 'permit'
        assert req_body['remote_bgp_asn'] == '65010'
        assert req_body['remote_gateway_ip'] == '10.242.63.12'
        assert req_body['remote_tunnel_ip'] == '192.168.129.1'
        assert req_body['zone'] == zone_identity_model

    def test_create_transit_gateway_connection_all_params_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_all_params.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_all_params()

        # Disable retries and run test_create_transit_gateway_connection_all_params.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_all_params()

    @responses.activate
    def test_create_transit_gateway_connection_value_error(self):
        """
        test_create_transit_gateway_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TransitGatewayConnectionPrefixFilter model
        transit_gateway_connection_prefix_filter_model = {}
        transit_gateway_connection_prefix_filter_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_model['ge'] = 0
        transit_gateway_connection_prefix_filter_model['le'] = 32
        transit_gateway_connection_prefix_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ZoneIdentityByName model
        zone_identity_model = {}
        zone_identity_model['name'] = 'us-south-1'

        # Set up parameter values
        transit_gateway_id = 'testString'
        network_type = 'vpc'
        base_connection_id = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        local_gateway_ip = '192.168.100.1'
        local_tunnel_ip = '192.168.129.2'
        name = 'Transit_Service_BWTN_SJ_DL'
        network_account_id = '28e4d90ac7504be694471ee66e70d0d5'
        network_id = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        prefix_filters = [transit_gateway_connection_prefix_filter_model]
        prefix_filters_default = 'permit'
        remote_bgp_asn = '65010'
        remote_gateway_ip = '10.242.63.12'
        remote_tunnel_ip = '192.168.129.1'
        zone = zone_identity_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "network_type": network_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_transit_gateway_connection(**req_copy)


    def test_create_transit_gateway_connection_value_error_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_value_error.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_value_error()

        # Disable retries and run test_create_transit_gateway_connection_value_error.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_value_error()

class TestDeleteTransitGatewayConnection():
    """
    Test Class for delete_transit_gateway_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_transit_gateway_connection_all_params(self):
        """
        delete_transit_gateway_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_transit_gateway_connection(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_transit_gateway_connection_all_params_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_connection_all_params.
        _service.enable_retries()
        self.test_delete_transit_gateway_connection_all_params()

        # Disable retries and run test_delete_transit_gateway_connection_all_params.
        _service.disable_retries()
        self.test_delete_transit_gateway_connection_all_params()

    @responses.activate
    def test_delete_transit_gateway_connection_value_error(self):
        """
        test_delete_transit_gateway_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_transit_gateway_connection(**req_copy)


    def test_delete_transit_gateway_connection_value_error_with_retries(self):
        # Enable retries and run test_delete_transit_gateway_connection_value_error.
        _service.enable_retries()
        self.test_delete_transit_gateway_connection_value_error()

        # Disable retries and run test_delete_transit_gateway_connection_value_error.
        _service.disable_retries()
        self.test_delete_transit_gateway_connection_value_error()

class TestGetTransitGatewayConnection():
    """
    Test Class for get_transit_gateway_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_transit_gateway_connection_all_params(self):
        """
        get_transit_gateway_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_transit_gateway_connection(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_transit_gateway_connection_all_params_with_retries(self):
        # Enable retries and run test_get_transit_gateway_connection_all_params.
        _service.enable_retries()
        self.test_get_transit_gateway_connection_all_params()

        # Disable retries and run test_get_transit_gateway_connection_all_params.
        _service.disable_retries()
        self.test_get_transit_gateway_connection_all_params()

    @responses.activate
    def test_get_transit_gateway_connection_value_error(self):
        """
        test_get_transit_gateway_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_transit_gateway_connection(**req_copy)


    def test_get_transit_gateway_connection_value_error_with_retries(self):
        # Enable retries and run test_get_transit_gateway_connection_value_error.
        _service.enable_retries()
        self.test_get_transit_gateway_connection_value_error()

        # Disable retries and run test_get_transit_gateway_connection_value_error.
        _service.disable_retries()
        self.test_get_transit_gateway_connection_value_error()

class TestUpdateTransitGatewayConnection():
    """
    Test Class for update_transit_gateway_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_transit_gateway_connection_all_params(self):
        """
        update_transit_gateway_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        name = 'Transit_Service_BWTN_SJ_DL'
        prefix_filters_default = 'permit'

        # Invoke method
        response = _service.update_transit_gateway_connection(
            transit_gateway_id,
            id,
            name=name,
            prefix_filters_default=prefix_filters_default,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'
        assert req_body['prefix_filters_default'] == 'permit'

    def test_update_transit_gateway_connection_all_params_with_retries(self):
        # Enable retries and run test_update_transit_gateway_connection_all_params.
        _service.enable_retries()
        self.test_update_transit_gateway_connection_all_params()

        # Disable retries and run test_update_transit_gateway_connection_all_params.
        _service.disable_retries()
        self.test_update_transit_gateway_connection_all_params()

    @responses.activate
    def test_update_transit_gateway_connection_value_error(self):
        """
        test_update_transit_gateway_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString')
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531", "base_connection_id": "975f58c1-afe7-469a-9727-7f3d720f2d32", "created_at": "2019-01-01T12:00:00.000Z", "local_bgp_asn": 64490, "local_gateway_ip": "192.168.100.1", "local_tunnel_ip": "192.168.129.2", "mtu": 9000, "network_account_id": "28e4d90ac7504be694471ee66e70d0d5", "prefix_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2019-01-01T12:00:00.000Z", "ge": 0, "id": "1a15dcab-7e30-45e1-b7c5-bc690eaa9865", "le": 32, "prefix": "192.168.100.0/24", "updated_at": "2019-01-01T12:00:00.000Z"}], "prefix_filters_default": "permit", "remote_bgp_asn": 65010, "remote_gateway_ip": "10.242.63.12", "remote_tunnel_ip": "192.168.129.1", "request_status": "pending", "status": "attached", "updated_at": "2019-01-01T12:00:00.000Z", "zone": {"name": "us-south-1"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        name = 'Transit_Service_BWTN_SJ_DL'
        prefix_filters_default = 'permit'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_transit_gateway_connection(**req_copy)


    def test_update_transit_gateway_connection_value_error_with_retries(self):
        # Enable retries and run test_update_transit_gateway_connection_value_error.
        _service.enable_retries()
        self.test_update_transit_gateway_connection_value_error()

        # Disable retries and run test_update_transit_gateway_connection_value_error.
        _service.disable_retries()
        self.test_update_transit_gateway_connection_value_error()

class TestCreateTransitGatewayConnectionActions():
    """
    Test Class for create_transit_gateway_connection_actions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_transit_gateway_connection_actions_all_params(self):
        """
        create_transit_gateway_connection_actions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/actions')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        action = 'approve'

        # Invoke method
        response = _service.create_transit_gateway_connection_actions(
            transit_gateway_id,
            id,
            action,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'approve'

    def test_create_transit_gateway_connection_actions_all_params_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_actions_all_params.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_actions_all_params()

        # Disable retries and run test_create_transit_gateway_connection_actions_all_params.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_actions_all_params()

    @responses.activate
    def test_create_transit_gateway_connection_actions_value_error(self):
        """
        test_create_transit_gateway_connection_actions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/transit_gateways/testString/connections/testString/actions')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        action = 'approve'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
            "action": action,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_transit_gateway_connection_actions(**req_copy)


    def test_create_transit_gateway_connection_actions_value_error_with_retries(self):
        # Enable retries and run test_create_transit_gateway_connection_actions_value_error.
        _service.enable_retries()
        self.test_create_transit_gateway_connection_actions_value_error()

        # Disable retries and run test_create_transit_gateway_connection_actions_value_error.
        _service.disable_retries()
        self.test_create_transit_gateway_connection_actions_value_error()

# endregion
##############################################################################
# End of Service: TransitGatewaysNetworkConnections
##############################################################################

##############################################################################
# Start of Service: TransitLocation
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = TransitGatewayApisV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, TransitGatewayApisV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = TransitGatewayApisV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = TransitGatewayApisV1.new_instance(
                version=None,
            )
class TestListGatewayLocations():
    """
    Test Class for list_gateway_locations
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_gateway_locations_all_params(self):
        """
        list_gateway_locations()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/locations')
        mock_response = '{"locations": [{"billing_location": "us", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_gateway_locations()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_locations_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_locations_all_params.
        _service.enable_retries()
        self.test_list_gateway_locations_all_params()

        # Disable retries and run test_list_gateway_locations_all_params.
        _service.disable_retries()
        self.test_list_gateway_locations_all_params()

    @responses.activate
    def test_list_gateway_locations_value_error(self):
        """
        test_list_gateway_locations_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/locations')
        mock_response = '{"locations": [{"billing_location": "us", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_locations(**req_copy)


    def test_list_gateway_locations_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_locations_value_error.
        _service.enable_retries()
        self.test_list_gateway_locations_value_error()

        # Disable retries and run test_list_gateway_locations_value_error.
        _service.disable_retries()
        self.test_list_gateway_locations_value_error()

class TestGetGatewayLocation():
    """
    Test Class for get_gateway_location
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_gateway_location_all_params(self):
        """
        get_gateway_location()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/locations/testString')
        mock_response = '{"billing_location": "us", "name": "us-south", "type": "region", "local_connection_locations": [{"display_name": "Dallas", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Invoke method
        response = _service.get_gateway_location(
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_location_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_location_all_params.
        _service.enable_retries()
        self.test_get_gateway_location_all_params()

        # Disable retries and run test_get_gateway_location_all_params.
        _service.disable_retries()
        self.test_get_gateway_location_all_params()

    @responses.activate
    def test_get_gateway_location_value_error(self):
        """
        test_get_gateway_location_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/locations/testString')
        mock_response = '{"billing_location": "us", "name": "us-south", "type": "region", "local_connection_locations": [{"display_name": "Dallas", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_location(**req_copy)


    def test_get_gateway_location_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_location_value_error.
        _service.enable_retries()
        self.test_get_gateway_location_value_error()

        # Disable retries and run test_get_gateway_location_value_error.
        _service.disable_retries()
        self.test_get_gateway_location_value_error()

# endregion
##############################################################################
# End of Service: TransitLocation
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_PrefixFilterCollection():
    """
    Test Class for PrefixFilterCollection
    """

    def test_prefix_filter_collection_serialization(self):
        """
        Test serialization/deserialization for PrefixFilterCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        prefix_filter_cust_model = {} # PrefixFilterCust
        prefix_filter_cust_model['action'] = 'permit'
        prefix_filter_cust_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        prefix_filter_cust_model['created_at'] = "2019-01-01T12:00:00Z"
        prefix_filter_cust_model['ge'] = 0
        prefix_filter_cust_model['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        prefix_filter_cust_model['le'] = 32
        prefix_filter_cust_model['prefix'] = '192.168.100.0/24'
        prefix_filter_cust_model['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a PrefixFilterCollection model
        prefix_filter_collection_model_json = {}
        prefix_filter_collection_model_json['prefix_filters'] = [prefix_filter_cust_model]

        # Construct a model instance of PrefixFilterCollection by calling from_dict on the json representation
        prefix_filter_collection_model = PrefixFilterCollection.from_dict(prefix_filter_collection_model_json)
        assert prefix_filter_collection_model != False

        # Construct a model instance of PrefixFilterCollection by calling from_dict on the json representation
        prefix_filter_collection_model_dict = PrefixFilterCollection.from_dict(prefix_filter_collection_model_json).__dict__
        prefix_filter_collection_model2 = PrefixFilterCollection(**prefix_filter_collection_model_dict)

        # Verify the model instances are equivalent
        assert prefix_filter_collection_model == prefix_filter_collection_model2

        # Convert model instance back to dict and verify no loss of data
        prefix_filter_collection_model_json2 = prefix_filter_collection_model.to_dict()
        assert prefix_filter_collection_model_json2 == prefix_filter_collection_model_json

class TestModel_PrefixFilterCust():
    """
    Test Class for PrefixFilterCust
    """

    def test_prefix_filter_cust_serialization(self):
        """
        Test serialization/deserialization for PrefixFilterCust
        """

        # Construct a json representation of a PrefixFilterCust model
        prefix_filter_cust_model_json = {}
        prefix_filter_cust_model_json['action'] = 'permit'
        prefix_filter_cust_model_json['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        prefix_filter_cust_model_json['created_at'] = "2019-01-01T12:00:00Z"
        prefix_filter_cust_model_json['ge'] = 0
        prefix_filter_cust_model_json['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        prefix_filter_cust_model_json['le'] = 32
        prefix_filter_cust_model_json['prefix'] = '192.168.100.0/24'
        prefix_filter_cust_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of PrefixFilterCust by calling from_dict on the json representation
        prefix_filter_cust_model = PrefixFilterCust.from_dict(prefix_filter_cust_model_json)
        assert prefix_filter_cust_model != False

        # Construct a model instance of PrefixFilterCust by calling from_dict on the json representation
        prefix_filter_cust_model_dict = PrefixFilterCust.from_dict(prefix_filter_cust_model_json).__dict__
        prefix_filter_cust_model2 = PrefixFilterCust(**prefix_filter_cust_model_dict)

        # Verify the model instances are equivalent
        assert prefix_filter_cust_model == prefix_filter_cust_model2

        # Convert model instance back to dict and verify no loss of data
        prefix_filter_cust_model_json2 = prefix_filter_cust_model.to_dict()
        assert prefix_filter_cust_model_json2 == prefix_filter_cust_model_json

class TestModel_ResourceGroupIdentity():
    """
    Test Class for ResourceGroupIdentity
    """

    def test_resource_group_identity_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupIdentity
        """

        # Construct a json representation of a ResourceGroupIdentity model
        resource_group_identity_model_json = {}
        resource_group_identity_model_json['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model = ResourceGroupIdentity.from_dict(resource_group_identity_model_json)
        assert resource_group_identity_model != False

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model_dict = ResourceGroupIdentity.from_dict(resource_group_identity_model_json).__dict__
        resource_group_identity_model2 = ResourceGroupIdentity(**resource_group_identity_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_identity_model == resource_group_identity_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_identity_model_json2 = resource_group_identity_model.to_dict()
        assert resource_group_identity_model_json2 == resource_group_identity_model_json

class TestModel_ResourceGroupReference():
    """
    Test Class for ResourceGroupReference
    """

    def test_resource_group_reference_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupReference
        """

        # Construct a json representation of a ResourceGroupReference model
        resource_group_reference_model_json = {}
        resource_group_reference_model_json['id'] = '56969d6043e9465c883cb9f7363e78e8'
        resource_group_reference_model_json['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8'

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model = ResourceGroupReference.from_dict(resource_group_reference_model_json)
        assert resource_group_reference_model != False

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model_dict = ResourceGroupReference.from_dict(resource_group_reference_model_json).__dict__
        resource_group_reference_model2 = ResourceGroupReference(**resource_group_reference_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_reference_model == resource_group_reference_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_reference_model_json2 = resource_group_reference_model.to_dict()
        assert resource_group_reference_model_json2 == resource_group_reference_model_json

class TestModel_RouteReport():
    """
    Test Class for RouteReport
    """

    def test_route_report_serialization(self):
        """
        Test serialization/deserialization for RouteReport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_connection_bgp_model = {} # RouteReportConnectionBgp
        route_report_connection_bgp_model['as_path'] = '(65201 4201065544) 4203065544'
        route_report_connection_bgp_model['is_used'] = True
        route_report_connection_bgp_model['local_preference'] = '190'
        route_report_connection_bgp_model['prefix'] = '172.17.0.0/16'

        route_report_connection_route_model = {} # RouteReportConnectionRoute
        route_report_connection_route_model['prefix'] = '192.168.0.0/16'

        route_report_connection_model = {} # RouteReportConnection
        route_report_connection_model['bgps'] = [route_report_connection_bgp_model]
        route_report_connection_model['id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model['name'] = 'transit-connection-vpc1'
        route_report_connection_model['routes'] = [route_report_connection_route_model]
        route_report_connection_model['type'] = 'vpc'

        route_report_overlapping_route_model = {} # RouteReportOverlappingRoute
        route_report_overlapping_route_model['connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'
        route_report_overlapping_route_model['prefix'] = 'testString'

        route_report_overlapping_route_group_model = {} # RouteReportOverlappingRouteGroup
        route_report_overlapping_route_group_model['routes'] = [route_report_overlapping_route_model]

        # Construct a json representation of a RouteReport model
        route_report_model_json = {}
        route_report_model_json['connections'] = [route_report_connection_model]
        route_report_model_json['created_at'] = "2019-01-01T12:00:00Z"
        route_report_model_json['id'] = '1a15dcab-7e26-45e1-b7c5-bc690eaa9724'
        route_report_model_json['overlapping_routes'] = [route_report_overlapping_route_group_model]
        route_report_model_json['status'] = 'complete'
        route_report_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of RouteReport by calling from_dict on the json representation
        route_report_model = RouteReport.from_dict(route_report_model_json)
        assert route_report_model != False

        # Construct a model instance of RouteReport by calling from_dict on the json representation
        route_report_model_dict = RouteReport.from_dict(route_report_model_json).__dict__
        route_report_model2 = RouteReport(**route_report_model_dict)

        # Verify the model instances are equivalent
        assert route_report_model == route_report_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_model_json2 = route_report_model.to_dict()
        assert route_report_model_json2 == route_report_model_json

class TestModel_RouteReportCollection():
    """
    Test Class for RouteReportCollection
    """

    def test_route_report_collection_serialization(self):
        """
        Test serialization/deserialization for RouteReportCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_connection_bgp_model = {} # RouteReportConnectionBgp
        route_report_connection_bgp_model['as_path'] = '(65201 4201065544) 4203065544'
        route_report_connection_bgp_model['is_used'] = True
        route_report_connection_bgp_model['local_preference'] = '190'
        route_report_connection_bgp_model['prefix'] = '172.17.0.0/16'

        route_report_connection_route_model = {} # RouteReportConnectionRoute
        route_report_connection_route_model['prefix'] = '192.168.0.0/16'

        route_report_connection_model = {} # RouteReportConnection
        route_report_connection_model['bgps'] = [route_report_connection_bgp_model]
        route_report_connection_model['id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model['name'] = 'transit-connection-vpc1'
        route_report_connection_model['routes'] = [route_report_connection_route_model]
        route_report_connection_model['type'] = 'vpc'

        route_report_overlapping_route_model = {} # RouteReportOverlappingRoute
        route_report_overlapping_route_model['connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'
        route_report_overlapping_route_model['prefix'] = 'testString'

        route_report_overlapping_route_group_model = {} # RouteReportOverlappingRouteGroup
        route_report_overlapping_route_group_model['routes'] = [route_report_overlapping_route_model]

        route_report_model = {} # RouteReport
        route_report_model['connections'] = [route_report_connection_model]
        route_report_model['created_at'] = "2019-01-01T12:00:00Z"
        route_report_model['id'] = '1a15dcab-7e26-45e1-b7c5-bc690eaa9724'
        route_report_model['overlapping_routes'] = [route_report_overlapping_route_group_model]
        route_report_model['status'] = 'complete'
        route_report_model['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a RouteReportCollection model
        route_report_collection_model_json = {}
        route_report_collection_model_json['route_reports'] = [route_report_model]

        # Construct a model instance of RouteReportCollection by calling from_dict on the json representation
        route_report_collection_model = RouteReportCollection.from_dict(route_report_collection_model_json)
        assert route_report_collection_model != False

        # Construct a model instance of RouteReportCollection by calling from_dict on the json representation
        route_report_collection_model_dict = RouteReportCollection.from_dict(route_report_collection_model_json).__dict__
        route_report_collection_model2 = RouteReportCollection(**route_report_collection_model_dict)

        # Verify the model instances are equivalent
        assert route_report_collection_model == route_report_collection_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_collection_model_json2 = route_report_collection_model.to_dict()
        assert route_report_collection_model_json2 == route_report_collection_model_json

class TestModel_RouteReportConnection():
    """
    Test Class for RouteReportConnection
    """

    def test_route_report_connection_serialization(self):
        """
        Test serialization/deserialization for RouteReportConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_connection_bgp_model = {} # RouteReportConnectionBgp
        route_report_connection_bgp_model['as_path'] = '(65201 4201065544) 4203065544'
        route_report_connection_bgp_model['is_used'] = True
        route_report_connection_bgp_model['local_preference'] = '190'
        route_report_connection_bgp_model['prefix'] = '172.17.0.0/16'

        route_report_connection_route_model = {} # RouteReportConnectionRoute
        route_report_connection_route_model['prefix'] = '192.168.0.0/16'

        # Construct a json representation of a RouteReportConnection model
        route_report_connection_model_json = {}
        route_report_connection_model_json['bgps'] = [route_report_connection_bgp_model]
        route_report_connection_model_json['id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model_json['name'] = 'transit-connection-vpc1'
        route_report_connection_model_json['routes'] = [route_report_connection_route_model]
        route_report_connection_model_json['type'] = 'vpc'

        # Construct a model instance of RouteReportConnection by calling from_dict on the json representation
        route_report_connection_model = RouteReportConnection.from_dict(route_report_connection_model_json)
        assert route_report_connection_model != False

        # Construct a model instance of RouteReportConnection by calling from_dict on the json representation
        route_report_connection_model_dict = RouteReportConnection.from_dict(route_report_connection_model_json).__dict__
        route_report_connection_model2 = RouteReportConnection(**route_report_connection_model_dict)

        # Verify the model instances are equivalent
        assert route_report_connection_model == route_report_connection_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_connection_model_json2 = route_report_connection_model.to_dict()
        assert route_report_connection_model_json2 == route_report_connection_model_json

class TestModel_RouteReportConnectionBgp():
    """
    Test Class for RouteReportConnectionBgp
    """

    def test_route_report_connection_bgp_serialization(self):
        """
        Test serialization/deserialization for RouteReportConnectionBgp
        """

        # Construct a json representation of a RouteReportConnectionBgp model
        route_report_connection_bgp_model_json = {}
        route_report_connection_bgp_model_json['as_path'] = '(65201 4201065544) 4203065544'
        route_report_connection_bgp_model_json['is_used'] = True
        route_report_connection_bgp_model_json['local_preference'] = '190'
        route_report_connection_bgp_model_json['prefix'] = '172.17.0.0/16'

        # Construct a model instance of RouteReportConnectionBgp by calling from_dict on the json representation
        route_report_connection_bgp_model = RouteReportConnectionBgp.from_dict(route_report_connection_bgp_model_json)
        assert route_report_connection_bgp_model != False

        # Construct a model instance of RouteReportConnectionBgp by calling from_dict on the json representation
        route_report_connection_bgp_model_dict = RouteReportConnectionBgp.from_dict(route_report_connection_bgp_model_json).__dict__
        route_report_connection_bgp_model2 = RouteReportConnectionBgp(**route_report_connection_bgp_model_dict)

        # Verify the model instances are equivalent
        assert route_report_connection_bgp_model == route_report_connection_bgp_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_connection_bgp_model_json2 = route_report_connection_bgp_model.to_dict()
        assert route_report_connection_bgp_model_json2 == route_report_connection_bgp_model_json

class TestModel_RouteReportConnectionRoute():
    """
    Test Class for RouteReportConnectionRoute
    """

    def test_route_report_connection_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportConnectionRoute
        """

        # Construct a json representation of a RouteReportConnectionRoute model
        route_report_connection_route_model_json = {}
        route_report_connection_route_model_json['prefix'] = '192.168.0.0/16'

        # Construct a model instance of RouteReportConnectionRoute by calling from_dict on the json representation
        route_report_connection_route_model = RouteReportConnectionRoute.from_dict(route_report_connection_route_model_json)
        assert route_report_connection_route_model != False

        # Construct a model instance of RouteReportConnectionRoute by calling from_dict on the json representation
        route_report_connection_route_model_dict = RouteReportConnectionRoute.from_dict(route_report_connection_route_model_json).__dict__
        route_report_connection_route_model2 = RouteReportConnectionRoute(**route_report_connection_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_connection_route_model == route_report_connection_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_connection_route_model_json2 = route_report_connection_route_model.to_dict()
        assert route_report_connection_route_model_json2 == route_report_connection_route_model_json

class TestModel_RouteReportOverlappingRoute():
    """
    Test Class for RouteReportOverlappingRoute
    """

    def test_route_report_overlapping_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportOverlappingRoute
        """

        # Construct a json representation of a RouteReportOverlappingRoute model
        route_report_overlapping_route_model_json = {}
        route_report_overlapping_route_model_json['connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'
        route_report_overlapping_route_model_json['prefix'] = 'testString'

        # Construct a model instance of RouteReportOverlappingRoute by calling from_dict on the json representation
        route_report_overlapping_route_model = RouteReportOverlappingRoute.from_dict(route_report_overlapping_route_model_json)
        assert route_report_overlapping_route_model != False

        # Construct a model instance of RouteReportOverlappingRoute by calling from_dict on the json representation
        route_report_overlapping_route_model_dict = RouteReportOverlappingRoute.from_dict(route_report_overlapping_route_model_json).__dict__
        route_report_overlapping_route_model2 = RouteReportOverlappingRoute(**route_report_overlapping_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_overlapping_route_model == route_report_overlapping_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_overlapping_route_model_json2 = route_report_overlapping_route_model.to_dict()
        assert route_report_overlapping_route_model_json2 == route_report_overlapping_route_model_json

class TestModel_RouteReportOverlappingRouteGroup():
    """
    Test Class for RouteReportOverlappingRouteGroup
    """

    def test_route_report_overlapping_route_group_serialization(self):
        """
        Test serialization/deserialization for RouteReportOverlappingRouteGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_overlapping_route_model = {} # RouteReportOverlappingRoute
        route_report_overlapping_route_model['connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'
        route_report_overlapping_route_model['prefix'] = 'testString'

        # Construct a json representation of a RouteReportOverlappingRouteGroup model
        route_report_overlapping_route_group_model_json = {}
        route_report_overlapping_route_group_model_json['routes'] = [route_report_overlapping_route_model]

        # Construct a model instance of RouteReportOverlappingRouteGroup by calling from_dict on the json representation
        route_report_overlapping_route_group_model = RouteReportOverlappingRouteGroup.from_dict(route_report_overlapping_route_group_model_json)
        assert route_report_overlapping_route_group_model != False

        # Construct a model instance of RouteReportOverlappingRouteGroup by calling from_dict on the json representation
        route_report_overlapping_route_group_model_dict = RouteReportOverlappingRouteGroup.from_dict(route_report_overlapping_route_group_model_json).__dict__
        route_report_overlapping_route_group_model2 = RouteReportOverlappingRouteGroup(**route_report_overlapping_route_group_model_dict)

        # Verify the model instances are equivalent
        assert route_report_overlapping_route_group_model == route_report_overlapping_route_group_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_overlapping_route_group_model_json2 = route_report_overlapping_route_group_model.to_dict()
        assert route_report_overlapping_route_group_model_json2 == route_report_overlapping_route_group_model_json

class TestModel_TSCollection():
    """
    Test Class for TSCollection
    """

    def test_ts_collection_serialization(self):
        """
        Test serialization/deserialization for TSCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ts_location_basic_model = {} # TSLocationBasic
        ts_location_basic_model['billing_location'] = 'us'
        ts_location_basic_model['name'] = 'us-south'
        ts_location_basic_model['type'] = 'region'

        # Construct a json representation of a TSCollection model
        ts_collection_model_json = {}
        ts_collection_model_json['locations'] = [ts_location_basic_model]

        # Construct a model instance of TSCollection by calling from_dict on the json representation
        ts_collection_model = TSCollection.from_dict(ts_collection_model_json)
        assert ts_collection_model != False

        # Construct a model instance of TSCollection by calling from_dict on the json representation
        ts_collection_model_dict = TSCollection.from_dict(ts_collection_model_json).__dict__
        ts_collection_model2 = TSCollection(**ts_collection_model_dict)

        # Verify the model instances are equivalent
        assert ts_collection_model == ts_collection_model2

        # Convert model instance back to dict and verify no loss of data
        ts_collection_model_json2 = ts_collection_model.to_dict()
        assert ts_collection_model_json2 == ts_collection_model_json

class TestModel_TSLocalLocation():
    """
    Test Class for TSLocalLocation
    """

    def test_ts_local_location_serialization(self):
        """
        Test serialization/deserialization for TSLocalLocation
        """

        # Construct a json representation of a TSLocalLocation model
        ts_local_location_model_json = {}
        ts_local_location_model_json['display_name'] = 'Dallas'
        ts_local_location_model_json['name'] = 'us-south'
        ts_local_location_model_json['type'] = 'region'

        # Construct a model instance of TSLocalLocation by calling from_dict on the json representation
        ts_local_location_model = TSLocalLocation.from_dict(ts_local_location_model_json)
        assert ts_local_location_model != False

        # Construct a model instance of TSLocalLocation by calling from_dict on the json representation
        ts_local_location_model_dict = TSLocalLocation.from_dict(ts_local_location_model_json).__dict__
        ts_local_location_model2 = TSLocalLocation(**ts_local_location_model_dict)

        # Verify the model instances are equivalent
        assert ts_local_location_model == ts_local_location_model2

        # Convert model instance back to dict and verify no loss of data
        ts_local_location_model_json2 = ts_local_location_model.to_dict()
        assert ts_local_location_model_json2 == ts_local_location_model_json

class TestModel_TSLocation():
    """
    Test Class for TSLocation
    """

    def test_ts_location_serialization(self):
        """
        Test serialization/deserialization for TSLocation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ts_local_location_model = {} # TSLocalLocation
        ts_local_location_model['display_name'] = 'Dallas'
        ts_local_location_model['name'] = 'us-south'
        ts_local_location_model['type'] = 'region'

        # Construct a json representation of a TSLocation model
        ts_location_model_json = {}
        ts_location_model_json['billing_location'] = 'us'
        ts_location_model_json['name'] = 'us-south'
        ts_location_model_json['type'] = 'region'
        ts_location_model_json['local_connection_locations'] = [ts_local_location_model]

        # Construct a model instance of TSLocation by calling from_dict on the json representation
        ts_location_model = TSLocation.from_dict(ts_location_model_json)
        assert ts_location_model != False

        # Construct a model instance of TSLocation by calling from_dict on the json representation
        ts_location_model_dict = TSLocation.from_dict(ts_location_model_json).__dict__
        ts_location_model2 = TSLocation(**ts_location_model_dict)

        # Verify the model instances are equivalent
        assert ts_location_model == ts_location_model2

        # Convert model instance back to dict and verify no loss of data
        ts_location_model_json2 = ts_location_model.to_dict()
        assert ts_location_model_json2 == ts_location_model_json

class TestModel_TSLocationBasic():
    """
    Test Class for TSLocationBasic
    """

    def test_ts_location_basic_serialization(self):
        """
        Test serialization/deserialization for TSLocationBasic
        """

        # Construct a json representation of a TSLocationBasic model
        ts_location_basic_model_json = {}
        ts_location_basic_model_json['billing_location'] = 'us'
        ts_location_basic_model_json['name'] = 'us-south'
        ts_location_basic_model_json['type'] = 'region'

        # Construct a model instance of TSLocationBasic by calling from_dict on the json representation
        ts_location_basic_model = TSLocationBasic.from_dict(ts_location_basic_model_json)
        assert ts_location_basic_model != False

        # Construct a model instance of TSLocationBasic by calling from_dict on the json representation
        ts_location_basic_model_dict = TSLocationBasic.from_dict(ts_location_basic_model_json).__dict__
        ts_location_basic_model2 = TSLocationBasic(**ts_location_basic_model_dict)

        # Verify the model instances are equivalent
        assert ts_location_basic_model == ts_location_basic_model2

        # Convert model instance back to dict and verify no loss of data
        ts_location_basic_model_json2 = ts_location_basic_model.to_dict()
        assert ts_location_basic_model_json2 == ts_location_basic_model_json

class TestModel_TransitConnection():
    """
    Test Class for TransitConnection
    """

    def test_transit_connection_serialization(self):
        """
        Test serialization/deserialization for TransitConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_connection_prefix_filter_reference_model = {} # TransitGatewayConnectionPrefixFilterReference
        transit_gateway_connection_prefix_filter_reference_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_reference_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        transit_gateway_connection_prefix_filter_reference_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_prefix_filter_reference_model['ge'] = 0
        transit_gateway_connection_prefix_filter_reference_model['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        transit_gateway_connection_prefix_filter_reference_model['le'] = 32
        transit_gateway_connection_prefix_filter_reference_model['prefix'] = '192.168.100.0/24'
        transit_gateway_connection_prefix_filter_reference_model['updated_at'] = "2019-01-01T12:00:00Z"

        transit_gateway_reference_model = {} # TransitGatewayReference
        transit_gateway_reference_model['crn'] = 'crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model['id'] = '456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model['name'] = 'my-transit-gw100'

        zone_reference_model = {} # ZoneReference
        zone_reference_model['name'] = 'us-south-1'

        # Construct a json representation of a TransitConnection model
        transit_connection_model_json = {}
        transit_connection_model_json['base_connection_id'] = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        transit_connection_model_json['created_at'] = "2019-01-01T12:00:00Z"
        transit_connection_model_json['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531'
        transit_connection_model_json['local_bgp_asn'] = 64490
        transit_connection_model_json['local_gateway_ip'] = '192.168.100.1'
        transit_connection_model_json['local_tunnel_ip'] = '192.168.129.2'
        transit_connection_model_json['mtu'] = 9000
        transit_connection_model_json['name'] = 'Transit_Service_SJ_DL'
        transit_connection_model_json['network_account_id'] = '28e4d90ac7504be694471ee66e70d0d5'
        transit_connection_model_json['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_connection_model_json['network_type'] = 'vpc'
        transit_connection_model_json['prefix_filters'] = [transit_gateway_connection_prefix_filter_reference_model]
        transit_connection_model_json['prefix_filters_default'] = 'permit'
        transit_connection_model_json['remote_bgp_asn'] = 65010
        transit_connection_model_json['remote_gateway_ip'] = '10.242.63.12'
        transit_connection_model_json['remote_tunnel_ip'] = '192.168.129.1'
        transit_connection_model_json['request_status'] = 'pending'
        transit_connection_model_json['status'] = 'attached'
        transit_connection_model_json['transit_gateway'] = transit_gateway_reference_model
        transit_connection_model_json['updated_at'] = "2019-01-01T12:00:00Z"
        transit_connection_model_json['zone'] = zone_reference_model

        # Construct a model instance of TransitConnection by calling from_dict on the json representation
        transit_connection_model = TransitConnection.from_dict(transit_connection_model_json)
        assert transit_connection_model != False

        # Construct a model instance of TransitConnection by calling from_dict on the json representation
        transit_connection_model_dict = TransitConnection.from_dict(transit_connection_model_json).__dict__
        transit_connection_model2 = TransitConnection(**transit_connection_model_dict)

        # Verify the model instances are equivalent
        assert transit_connection_model == transit_connection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_connection_model_json2 = transit_connection_model.to_dict()
        assert transit_connection_model_json2 == transit_connection_model_json

class TestModel_TransitConnectionCollection():
    """
    Test Class for TransitConnectionCollection
    """

    def test_transit_connection_collection_serialization(self):
        """
        Test serialization/deserialization for TransitConnectionCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_connection_prefix_filter_reference_model = {} # TransitGatewayConnectionPrefixFilterReference
        transit_gateway_connection_prefix_filter_reference_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_reference_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        transit_gateway_connection_prefix_filter_reference_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_prefix_filter_reference_model['ge'] = 0
        transit_gateway_connection_prefix_filter_reference_model['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        transit_gateway_connection_prefix_filter_reference_model['le'] = 32
        transit_gateway_connection_prefix_filter_reference_model['prefix'] = '192.168.100.0/24'
        transit_gateway_connection_prefix_filter_reference_model['updated_at'] = "2019-01-01T12:00:00Z"

        transit_gateway_reference_model = {} # TransitGatewayReference
        transit_gateway_reference_model['crn'] = 'crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model['id'] = '456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model['name'] = 'my-transit-gw100'

        zone_reference_model = {} # ZoneReference
        zone_reference_model['name'] = 'us-south-1'

        transit_connection_model = {} # TransitConnection
        transit_connection_model['base_connection_id'] = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        transit_connection_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_connection_model['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531'
        transit_connection_model['local_bgp_asn'] = 64490
        transit_connection_model['local_gateway_ip'] = '192.168.100.1'
        transit_connection_model['local_tunnel_ip'] = '192.168.129.2'
        transit_connection_model['mtu'] = 9000
        transit_connection_model['name'] = 'Transit_Service_SJ_DL'
        transit_connection_model['network_account_id'] = '28e4d90ac7504be694471ee66e70d0d5'
        transit_connection_model['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_connection_model['network_type'] = 'vpc'
        transit_connection_model['prefix_filters'] = [transit_gateway_connection_prefix_filter_reference_model]
        transit_connection_model['prefix_filters_default'] = 'permit'
        transit_connection_model['remote_bgp_asn'] = 65010
        transit_connection_model['remote_gateway_ip'] = '10.242.63.12'
        transit_connection_model['remote_tunnel_ip'] = '192.168.129.1'
        transit_connection_model['request_status'] = 'pending'
        transit_connection_model['status'] = 'attached'
        transit_connection_model['transit_gateway'] = transit_gateway_reference_model
        transit_connection_model['updated_at'] = "2019-01-01T12:00:00Z"
        transit_connection_model['zone'] = zone_reference_model

        transit_connection_collection_first_model = {} # TransitConnectionCollectionFirst
        transit_connection_collection_first_model['href'] = 'https://transit.cloud.ibm.com/v1/connections?limit=50'

        transit_connection_collection_next_model = {} # TransitConnectionCollectionNext
        transit_connection_collection_next_model['href'] = 'https://transit.cloud.ibm.com/v1/connections?start=MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa&limit=50'
        transit_connection_collection_next_model['start'] = 'MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa'

        # Construct a json representation of a TransitConnectionCollection model
        transit_connection_collection_model_json = {}
        transit_connection_collection_model_json['connections'] = [transit_connection_model]
        transit_connection_collection_model_json['first'] = transit_connection_collection_first_model
        transit_connection_collection_model_json['limit'] = 50
        transit_connection_collection_model_json['next'] = transit_connection_collection_next_model

        # Construct a model instance of TransitConnectionCollection by calling from_dict on the json representation
        transit_connection_collection_model = TransitConnectionCollection.from_dict(transit_connection_collection_model_json)
        assert transit_connection_collection_model != False

        # Construct a model instance of TransitConnectionCollection by calling from_dict on the json representation
        transit_connection_collection_model_dict = TransitConnectionCollection.from_dict(transit_connection_collection_model_json).__dict__
        transit_connection_collection_model2 = TransitConnectionCollection(**transit_connection_collection_model_dict)

        # Verify the model instances are equivalent
        assert transit_connection_collection_model == transit_connection_collection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_connection_collection_model_json2 = transit_connection_collection_model.to_dict()
        assert transit_connection_collection_model_json2 == transit_connection_collection_model_json

class TestModel_TransitConnectionCollectionFirst():
    """
    Test Class for TransitConnectionCollectionFirst
    """

    def test_transit_connection_collection_first_serialization(self):
        """
        Test serialization/deserialization for TransitConnectionCollectionFirst
        """

        # Construct a json representation of a TransitConnectionCollectionFirst model
        transit_connection_collection_first_model_json = {}
        transit_connection_collection_first_model_json['href'] = 'https://transit.cloud.ibm.com/v1/connections?limit=50'

        # Construct a model instance of TransitConnectionCollectionFirst by calling from_dict on the json representation
        transit_connection_collection_first_model = TransitConnectionCollectionFirst.from_dict(transit_connection_collection_first_model_json)
        assert transit_connection_collection_first_model != False

        # Construct a model instance of TransitConnectionCollectionFirst by calling from_dict on the json representation
        transit_connection_collection_first_model_dict = TransitConnectionCollectionFirst.from_dict(transit_connection_collection_first_model_json).__dict__
        transit_connection_collection_first_model2 = TransitConnectionCollectionFirst(**transit_connection_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert transit_connection_collection_first_model == transit_connection_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        transit_connection_collection_first_model_json2 = transit_connection_collection_first_model.to_dict()
        assert transit_connection_collection_first_model_json2 == transit_connection_collection_first_model_json

class TestModel_TransitConnectionCollectionNext():
    """
    Test Class for TransitConnectionCollectionNext
    """

    def test_transit_connection_collection_next_serialization(self):
        """
        Test serialization/deserialization for TransitConnectionCollectionNext
        """

        # Construct a json representation of a TransitConnectionCollectionNext model
        transit_connection_collection_next_model_json = {}
        transit_connection_collection_next_model_json['href'] = 'https://transit.cloud.ibm.com/v1/connections?start=MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa&limit=50'
        transit_connection_collection_next_model_json['start'] = 'MjAyMC0wNS0wOVQxNjoyMDoyMC4yMjQ5NzNa'

        # Construct a model instance of TransitConnectionCollectionNext by calling from_dict on the json representation
        transit_connection_collection_next_model = TransitConnectionCollectionNext.from_dict(transit_connection_collection_next_model_json)
        assert transit_connection_collection_next_model != False

        # Construct a model instance of TransitConnectionCollectionNext by calling from_dict on the json representation
        transit_connection_collection_next_model_dict = TransitConnectionCollectionNext.from_dict(transit_connection_collection_next_model_json).__dict__
        transit_connection_collection_next_model2 = TransitConnectionCollectionNext(**transit_connection_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert transit_connection_collection_next_model == transit_connection_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        transit_connection_collection_next_model_json2 = transit_connection_collection_next_model.to_dict()
        assert transit_connection_collection_next_model_json2 == transit_connection_collection_next_model_json

class TestModel_TransitGateway():
    """
    Test Class for TransitGateway
    """

    def test_transit_gateway_serialization(self):
        """
        Test serialization/deserialization for TransitGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'
        resource_group_reference_model['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a TransitGateway model
        transit_gateway_model_json = {}
        transit_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model_json['crn'] = 'crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model_json['name'] = 'my-transit-gateway-in-TransitGateway'
        transit_gateway_model_json['location'] = 'us-south'
        transit_gateway_model_json['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_model_json['global'] = True
        transit_gateway_model_json['resource_group'] = resource_group_reference_model
        transit_gateway_model_json['status'] = 'available'
        transit_gateway_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of TransitGateway by calling from_dict on the json representation
        transit_gateway_model = TransitGateway.from_dict(transit_gateway_model_json)
        assert transit_gateway_model != False

        # Construct a model instance of TransitGateway by calling from_dict on the json representation
        transit_gateway_model_dict = TransitGateway.from_dict(transit_gateway_model_json).__dict__
        transit_gateway_model2 = TransitGateway(**transit_gateway_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_model == transit_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_model_json2 = transit_gateway_model.to_dict()
        assert transit_gateway_model_json2 == transit_gateway_model_json

class TestModel_TransitGatewayCollection():
    """
    Test Class for TransitGatewayCollection
    """

    def test_transit_gateway_collection_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_collection_first_model = {} # TransitGatewayCollectionFirst
        transit_gateway_collection_first_model['href'] = 'https://transit.cloud.ibm.com/v1/transit_gateways?limit=50'

        transit_gateway_collection_next_model = {} # TransitGatewayCollectionNext
        transit_gateway_collection_next_model['href'] = 'https://transit.cloud.ibm.com/v1/transit_gateways?start=MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa&limit=50'
        transit_gateway_collection_next_model['start'] = 'MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa'

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'
        resource_group_reference_model['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d6043e9465c883cb9f7363e78e8'

        transit_gateway_model = {} # TransitGateway
        transit_gateway_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model['crn'] = 'crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model['name'] = 'my-transit-gateway-in-TransitGateway'
        transit_gateway_model['location'] = 'us-south'
        transit_gateway_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_model['global'] = True
        transit_gateway_model['resource_group'] = resource_group_reference_model
        transit_gateway_model['status'] = 'available'
        transit_gateway_model['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a TransitGatewayCollection model
        transit_gateway_collection_model_json = {}
        transit_gateway_collection_model_json['first'] = transit_gateway_collection_first_model
        transit_gateway_collection_model_json['limit'] = 50
        transit_gateway_collection_model_json['next'] = transit_gateway_collection_next_model
        transit_gateway_collection_model_json['transit_gateways'] = [transit_gateway_model]

        # Construct a model instance of TransitGatewayCollection by calling from_dict on the json representation
        transit_gateway_collection_model = TransitGatewayCollection.from_dict(transit_gateway_collection_model_json)
        assert transit_gateway_collection_model != False

        # Construct a model instance of TransitGatewayCollection by calling from_dict on the json representation
        transit_gateway_collection_model_dict = TransitGatewayCollection.from_dict(transit_gateway_collection_model_json).__dict__
        transit_gateway_collection_model2 = TransitGatewayCollection(**transit_gateway_collection_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_collection_model == transit_gateway_collection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_collection_model_json2 = transit_gateway_collection_model.to_dict()
        assert transit_gateway_collection_model_json2 == transit_gateway_collection_model_json

class TestModel_TransitGatewayCollectionFirst():
    """
    Test Class for TransitGatewayCollectionFirst
    """

    def test_transit_gateway_collection_first_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayCollectionFirst
        """

        # Construct a json representation of a TransitGatewayCollectionFirst model
        transit_gateway_collection_first_model_json = {}
        transit_gateway_collection_first_model_json['href'] = 'https://transit.cloud.ibm.com/v1/transit_gateways?limit=50'

        # Construct a model instance of TransitGatewayCollectionFirst by calling from_dict on the json representation
        transit_gateway_collection_first_model = TransitGatewayCollectionFirst.from_dict(transit_gateway_collection_first_model_json)
        assert transit_gateway_collection_first_model != False

        # Construct a model instance of TransitGatewayCollectionFirst by calling from_dict on the json representation
        transit_gateway_collection_first_model_dict = TransitGatewayCollectionFirst.from_dict(transit_gateway_collection_first_model_json).__dict__
        transit_gateway_collection_first_model2 = TransitGatewayCollectionFirst(**transit_gateway_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_collection_first_model == transit_gateway_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_collection_first_model_json2 = transit_gateway_collection_first_model.to_dict()
        assert transit_gateway_collection_first_model_json2 == transit_gateway_collection_first_model_json

class TestModel_TransitGatewayCollectionNext():
    """
    Test Class for TransitGatewayCollectionNext
    """

    def test_transit_gateway_collection_next_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayCollectionNext
        """

        # Construct a json representation of a TransitGatewayCollectionNext model
        transit_gateway_collection_next_model_json = {}
        transit_gateway_collection_next_model_json['href'] = 'https://transit.cloud.ibm.com/v1/transit_gateways?start=MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa&limit=50'
        transit_gateway_collection_next_model_json['start'] = 'MjAyMC0wNS0wOFQxNDoxNzowMy45NzQ5NzNa'

        # Construct a model instance of TransitGatewayCollectionNext by calling from_dict on the json representation
        transit_gateway_collection_next_model = TransitGatewayCollectionNext.from_dict(transit_gateway_collection_next_model_json)
        assert transit_gateway_collection_next_model != False

        # Construct a model instance of TransitGatewayCollectionNext by calling from_dict on the json representation
        transit_gateway_collection_next_model_dict = TransitGatewayCollectionNext.from_dict(transit_gateway_collection_next_model_json).__dict__
        transit_gateway_collection_next_model2 = TransitGatewayCollectionNext(**transit_gateway_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_collection_next_model == transit_gateway_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_collection_next_model_json2 = transit_gateway_collection_next_model.to_dict()
        assert transit_gateway_collection_next_model_json2 == transit_gateway_collection_next_model_json

class TestModel_TransitGatewayConnectionCollection():
    """
    Test Class for TransitGatewayConnectionCollection
    """

    def test_transit_gateway_connection_collection_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayConnectionCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_connection_prefix_filter_reference_model = {} # TransitGatewayConnectionPrefixFilterReference
        transit_gateway_connection_prefix_filter_reference_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_reference_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        transit_gateway_connection_prefix_filter_reference_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_prefix_filter_reference_model['ge'] = 0
        transit_gateway_connection_prefix_filter_reference_model['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        transit_gateway_connection_prefix_filter_reference_model['le'] = 32
        transit_gateway_connection_prefix_filter_reference_model['prefix'] = '192.168.100.0/24'
        transit_gateway_connection_prefix_filter_reference_model['updated_at'] = "2019-01-01T12:00:00Z"

        transit_gateway_connection_cust_zone_model = {} # TransitGatewayConnectionCustZone
        transit_gateway_connection_cust_zone_model['name'] = 'us-south-1'

        transit_gateway_connection_cust_model = {} # TransitGatewayConnectionCust
        transit_gateway_connection_cust_model['name'] = 'Transit_Service_BWTN_SJ_DL'
        transit_gateway_connection_cust_model['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_gateway_connection_cust_model['network_type'] = 'vpc'
        transit_gateway_connection_cust_model['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531'
        transit_gateway_connection_cust_model['base_connection_id'] = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        transit_gateway_connection_cust_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_cust_model['local_bgp_asn'] = 64490
        transit_gateway_connection_cust_model['local_gateway_ip'] = '192.168.100.1'
        transit_gateway_connection_cust_model['local_tunnel_ip'] = '192.168.129.2'
        transit_gateway_connection_cust_model['mtu'] = 9000
        transit_gateway_connection_cust_model['network_account_id'] = '28e4d90ac7504be694471ee66e70d0d5'
        transit_gateway_connection_cust_model['prefix_filters'] = [transit_gateway_connection_prefix_filter_reference_model]
        transit_gateway_connection_cust_model['prefix_filters_default'] = 'permit'
        transit_gateway_connection_cust_model['remote_bgp_asn'] = 65010
        transit_gateway_connection_cust_model['remote_gateway_ip'] = '10.242.63.12'
        transit_gateway_connection_cust_model['remote_tunnel_ip'] = '192.168.129.1'
        transit_gateway_connection_cust_model['request_status'] = 'pending'
        transit_gateway_connection_cust_model['status'] = 'attached'
        transit_gateway_connection_cust_model['updated_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_cust_model['zone'] = transit_gateway_connection_cust_zone_model

        # Construct a json representation of a TransitGatewayConnectionCollection model
        transit_gateway_connection_collection_model_json = {}
        transit_gateway_connection_collection_model_json['connections'] = [transit_gateway_connection_cust_model]

        # Construct a model instance of TransitGatewayConnectionCollection by calling from_dict on the json representation
        transit_gateway_connection_collection_model = TransitGatewayConnectionCollection.from_dict(transit_gateway_connection_collection_model_json)
        assert transit_gateway_connection_collection_model != False

        # Construct a model instance of TransitGatewayConnectionCollection by calling from_dict on the json representation
        transit_gateway_connection_collection_model_dict = TransitGatewayConnectionCollection.from_dict(transit_gateway_connection_collection_model_json).__dict__
        transit_gateway_connection_collection_model2 = TransitGatewayConnectionCollection(**transit_gateway_connection_collection_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_collection_model == transit_gateway_connection_collection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_collection_model_json2 = transit_gateway_connection_collection_model.to_dict()
        assert transit_gateway_connection_collection_model_json2 == transit_gateway_connection_collection_model_json

class TestModel_TransitGatewayConnectionCust():
    """
    Test Class for TransitGatewayConnectionCust
    """

    def test_transit_gateway_connection_cust_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayConnectionCust
        """

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_connection_prefix_filter_reference_model = {} # TransitGatewayConnectionPrefixFilterReference
        transit_gateway_connection_prefix_filter_reference_model['action'] = 'permit'
        transit_gateway_connection_prefix_filter_reference_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        transit_gateway_connection_prefix_filter_reference_model['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_prefix_filter_reference_model['ge'] = 0
        transit_gateway_connection_prefix_filter_reference_model['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        transit_gateway_connection_prefix_filter_reference_model['le'] = 32
        transit_gateway_connection_prefix_filter_reference_model['prefix'] = '192.168.100.0/24'
        transit_gateway_connection_prefix_filter_reference_model['updated_at'] = "2019-01-01T12:00:00Z"

        transit_gateway_connection_cust_zone_model = {} # TransitGatewayConnectionCustZone
        transit_gateway_connection_cust_zone_model['name'] = 'us-south-1'

        # Construct a json representation of a TransitGatewayConnectionCust model
        transit_gateway_connection_cust_model_json = {}
        transit_gateway_connection_cust_model_json['name'] = 'Transit_Service_BWTN_SJ_DL'
        transit_gateway_connection_cust_model_json['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_gateway_connection_cust_model_json['network_type'] = 'vpc'
        transit_gateway_connection_cust_model_json['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531'
        transit_gateway_connection_cust_model_json['base_connection_id'] = '975f58c1-afe7-469a-9727-7f3d720f2d32'
        transit_gateway_connection_cust_model_json['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_cust_model_json['local_bgp_asn'] = 64490
        transit_gateway_connection_cust_model_json['local_gateway_ip'] = '192.168.100.1'
        transit_gateway_connection_cust_model_json['local_tunnel_ip'] = '192.168.129.2'
        transit_gateway_connection_cust_model_json['mtu'] = 9000
        transit_gateway_connection_cust_model_json['network_account_id'] = '28e4d90ac7504be694471ee66e70d0d5'
        transit_gateway_connection_cust_model_json['prefix_filters'] = [transit_gateway_connection_prefix_filter_reference_model]
        transit_gateway_connection_cust_model_json['prefix_filters_default'] = 'permit'
        transit_gateway_connection_cust_model_json['remote_bgp_asn'] = 65010
        transit_gateway_connection_cust_model_json['remote_gateway_ip'] = '10.242.63.12'
        transit_gateway_connection_cust_model_json['remote_tunnel_ip'] = '192.168.129.1'
        transit_gateway_connection_cust_model_json['request_status'] = 'pending'
        transit_gateway_connection_cust_model_json['status'] = 'attached'
        transit_gateway_connection_cust_model_json['updated_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_cust_model_json['zone'] = transit_gateway_connection_cust_zone_model

        # Construct a model instance of TransitGatewayConnectionCust by calling from_dict on the json representation
        transit_gateway_connection_cust_model = TransitGatewayConnectionCust.from_dict(transit_gateway_connection_cust_model_json)
        assert transit_gateway_connection_cust_model != False

        # Construct a model instance of TransitGatewayConnectionCust by calling from_dict on the json representation
        transit_gateway_connection_cust_model_dict = TransitGatewayConnectionCust.from_dict(transit_gateway_connection_cust_model_json).__dict__
        transit_gateway_connection_cust_model2 = TransitGatewayConnectionCust(**transit_gateway_connection_cust_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_cust_model == transit_gateway_connection_cust_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_cust_model_json2 = transit_gateway_connection_cust_model.to_dict()
        assert transit_gateway_connection_cust_model_json2 == transit_gateway_connection_cust_model_json

class TestModel_TransitGatewayConnectionCustZone():
    """
    Test Class for TransitGatewayConnectionCustZone
    """

    def test_transit_gateway_connection_cust_zone_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayConnectionCustZone
        """

        # Construct a json representation of a TransitGatewayConnectionCustZone model
        transit_gateway_connection_cust_zone_model_json = {}
        transit_gateway_connection_cust_zone_model_json['name'] = 'us-south-1'

        # Construct a model instance of TransitGatewayConnectionCustZone by calling from_dict on the json representation
        transit_gateway_connection_cust_zone_model = TransitGatewayConnectionCustZone.from_dict(transit_gateway_connection_cust_zone_model_json)
        assert transit_gateway_connection_cust_zone_model != False

        # Construct a model instance of TransitGatewayConnectionCustZone by calling from_dict on the json representation
        transit_gateway_connection_cust_zone_model_dict = TransitGatewayConnectionCustZone.from_dict(transit_gateway_connection_cust_zone_model_json).__dict__
        transit_gateway_connection_cust_zone_model2 = TransitGatewayConnectionCustZone(**transit_gateway_connection_cust_zone_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_cust_zone_model == transit_gateway_connection_cust_zone_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_cust_zone_model_json2 = transit_gateway_connection_cust_zone_model.to_dict()
        assert transit_gateway_connection_cust_zone_model_json2 == transit_gateway_connection_cust_zone_model_json

class TestModel_TransitGatewayConnectionPrefixFilter():
    """
    Test Class for TransitGatewayConnectionPrefixFilter
    """

    def test_transit_gateway_connection_prefix_filter_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayConnectionPrefixFilter
        """

        # Construct a json representation of a TransitGatewayConnectionPrefixFilter model
        transit_gateway_connection_prefix_filter_model_json = {}
        transit_gateway_connection_prefix_filter_model_json['action'] = 'permit'
        transit_gateway_connection_prefix_filter_model_json['ge'] = 0
        transit_gateway_connection_prefix_filter_model_json['le'] = 32
        transit_gateway_connection_prefix_filter_model_json['prefix'] = '192.168.100.0/24'

        # Construct a model instance of TransitGatewayConnectionPrefixFilter by calling from_dict on the json representation
        transit_gateway_connection_prefix_filter_model = TransitGatewayConnectionPrefixFilter.from_dict(transit_gateway_connection_prefix_filter_model_json)
        assert transit_gateway_connection_prefix_filter_model != False

        # Construct a model instance of TransitGatewayConnectionPrefixFilter by calling from_dict on the json representation
        transit_gateway_connection_prefix_filter_model_dict = TransitGatewayConnectionPrefixFilter.from_dict(transit_gateway_connection_prefix_filter_model_json).__dict__
        transit_gateway_connection_prefix_filter_model2 = TransitGatewayConnectionPrefixFilter(**transit_gateway_connection_prefix_filter_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_prefix_filter_model == transit_gateway_connection_prefix_filter_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_prefix_filter_model_json2 = transit_gateway_connection_prefix_filter_model.to_dict()
        assert transit_gateway_connection_prefix_filter_model_json2 == transit_gateway_connection_prefix_filter_model_json

class TestModel_TransitGatewayConnectionPrefixFilterReference():
    """
    Test Class for TransitGatewayConnectionPrefixFilterReference
    """

    def test_transit_gateway_connection_prefix_filter_reference_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayConnectionPrefixFilterReference
        """

        # Construct a json representation of a TransitGatewayConnectionPrefixFilterReference model
        transit_gateway_connection_prefix_filter_reference_model_json = {}
        transit_gateway_connection_prefix_filter_reference_model_json['action'] = 'permit'
        transit_gateway_connection_prefix_filter_reference_model_json['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        transit_gateway_connection_prefix_filter_reference_model_json['created_at'] = "2019-01-01T12:00:00Z"
        transit_gateway_connection_prefix_filter_reference_model_json['ge'] = 0
        transit_gateway_connection_prefix_filter_reference_model_json['id'] = '1a15dcab-7e30-45e1-b7c5-bc690eaa9865'
        transit_gateway_connection_prefix_filter_reference_model_json['le'] = 32
        transit_gateway_connection_prefix_filter_reference_model_json['prefix'] = '192.168.100.0/24'
        transit_gateway_connection_prefix_filter_reference_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of TransitGatewayConnectionPrefixFilterReference by calling from_dict on the json representation
        transit_gateway_connection_prefix_filter_reference_model = TransitGatewayConnectionPrefixFilterReference.from_dict(transit_gateway_connection_prefix_filter_reference_model_json)
        assert transit_gateway_connection_prefix_filter_reference_model != False

        # Construct a model instance of TransitGatewayConnectionPrefixFilterReference by calling from_dict on the json representation
        transit_gateway_connection_prefix_filter_reference_model_dict = TransitGatewayConnectionPrefixFilterReference.from_dict(transit_gateway_connection_prefix_filter_reference_model_json).__dict__
        transit_gateway_connection_prefix_filter_reference_model2 = TransitGatewayConnectionPrefixFilterReference(**transit_gateway_connection_prefix_filter_reference_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_prefix_filter_reference_model == transit_gateway_connection_prefix_filter_reference_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_prefix_filter_reference_model_json2 = transit_gateway_connection_prefix_filter_reference_model.to_dict()
        assert transit_gateway_connection_prefix_filter_reference_model_json2 == transit_gateway_connection_prefix_filter_reference_model_json

class TestModel_TransitGatewayReference():
    """
    Test Class for TransitGatewayReference
    """

    def test_transit_gateway_reference_serialization(self):
        """
        Test serialization/deserialization for TransitGatewayReference
        """

        # Construct a json representation of a TransitGatewayReference model
        transit_gateway_reference_model_json = {}
        transit_gateway_reference_model_json['crn'] = 'crn:v1:bluemix:public:transit:us-south:a/123456::gateway:456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model_json['id'] = '456f58c1-afe7-123a-0a0a-7f3d720f1a44'
        transit_gateway_reference_model_json['name'] = 'my-transit-gw100'

        # Construct a model instance of TransitGatewayReference by calling from_dict on the json representation
        transit_gateway_reference_model = TransitGatewayReference.from_dict(transit_gateway_reference_model_json)
        assert transit_gateway_reference_model != False

        # Construct a model instance of TransitGatewayReference by calling from_dict on the json representation
        transit_gateway_reference_model_dict = TransitGatewayReference.from_dict(transit_gateway_reference_model_json).__dict__
        transit_gateway_reference_model2 = TransitGatewayReference(**transit_gateway_reference_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_reference_model == transit_gateway_reference_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_reference_model_json2 = transit_gateway_reference_model.to_dict()
        assert transit_gateway_reference_model_json2 == transit_gateway_reference_model_json

class TestModel_ZoneReference():
    """
    Test Class for ZoneReference
    """

    def test_zone_reference_serialization(self):
        """
        Test serialization/deserialization for ZoneReference
        """

        # Construct a json representation of a ZoneReference model
        zone_reference_model_json = {}
        zone_reference_model_json['name'] = 'us-south-1'

        # Construct a model instance of ZoneReference by calling from_dict on the json representation
        zone_reference_model = ZoneReference.from_dict(zone_reference_model_json)
        assert zone_reference_model != False

        # Construct a model instance of ZoneReference by calling from_dict on the json representation
        zone_reference_model_dict = ZoneReference.from_dict(zone_reference_model_json).__dict__
        zone_reference_model2 = ZoneReference(**zone_reference_model_dict)

        # Verify the model instances are equivalent
        assert zone_reference_model == zone_reference_model2

        # Convert model instance back to dict and verify no loss of data
        zone_reference_model_json2 = zone_reference_model.to_dict()
        assert zone_reference_model_json2 == zone_reference_model_json

class TestModel_ZoneIdentityByName():
    """
    Test Class for ZoneIdentityByName
    """

    def test_zone_identity_by_name_serialization(self):
        """
        Test serialization/deserialization for ZoneIdentityByName
        """

        # Construct a json representation of a ZoneIdentityByName model
        zone_identity_by_name_model_json = {}
        zone_identity_by_name_model_json['name'] = 'us-south-1'

        # Construct a model instance of ZoneIdentityByName by calling from_dict on the json representation
        zone_identity_by_name_model = ZoneIdentityByName.from_dict(zone_identity_by_name_model_json)
        assert zone_identity_by_name_model != False

        # Construct a model instance of ZoneIdentityByName by calling from_dict on the json representation
        zone_identity_by_name_model_dict = ZoneIdentityByName.from_dict(zone_identity_by_name_model_json).__dict__
        zone_identity_by_name_model2 = ZoneIdentityByName(**zone_identity_by_name_model_dict)

        # Verify the model instances are equivalent
        assert zone_identity_by_name_model == zone_identity_by_name_model2

        # Convert model instance back to dict and verify no loss of data
        zone_identity_by_name_model_json2 = zone_identity_by_name_model.to_dict()
        assert zone_identity_by_name_model_json2 == zone_identity_by_name_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
