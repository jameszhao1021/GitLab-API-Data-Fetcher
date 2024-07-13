# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_entities_user_basic import APIEntitiesUserBasic

class TestAPIEntitiesUserBasic(unittest.TestCase):
    """APIEntitiesUserBasic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIEntitiesUserBasic:
        """Test APIEntitiesUserBasic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIEntitiesUserBasic`
        """
        model = APIEntitiesUserBasic()
        if include_optional:
            return APIEntitiesUserBasic(
                id = 1,
                username = 'admin',
                name = 'Administrator',
                state = 'active',
                avatar_url = 'https://gravatar.com/avatar/1',
                avatar_path = '/user/avatar/28/The-Big-Lebowski-400-400.png',
                custom_attributes = [
                    openapi_client.models.api_entities_custom_attribute.API_Entities_CustomAttribute(
                        key = 'foo', 
                        value = 'bar', )
                    ],
                web_url = 'https://gitlab.example.com/root',
                email = ''
            )
        else:
            return APIEntitiesUserBasic(
        )
        """

    def testAPIEntitiesUserBasic(self):
        """Test APIEntitiesUserBasic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
