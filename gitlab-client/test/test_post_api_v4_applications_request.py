# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.post_api_v4_applications_request import PostApiV4ApplicationsRequest

class TestPostApiV4ApplicationsRequest(unittest.TestCase):
    """PostApiV4ApplicationsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostApiV4ApplicationsRequest:
        """Test PostApiV4ApplicationsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostApiV4ApplicationsRequest`
        """
        model = PostApiV4ApplicationsRequest()
        if include_optional:
            return PostApiV4ApplicationsRequest(
                name = '',
                redirect_uri = '',
                scopes = '',
                confidential = True
            )
        else:
            return PostApiV4ApplicationsRequest(
                name = '',
                redirect_uri = '',
                scopes = '',
        )
        """

    def testPostApiV4ApplicationsRequest(self):
        """Test PostApiV4ApplicationsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
