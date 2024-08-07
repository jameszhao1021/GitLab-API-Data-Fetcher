# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_entities_appearance import APIEntitiesAppearance

class TestAPIEntitiesAppearance(unittest.TestCase):
    """APIEntitiesAppearance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIEntitiesAppearance:
        """Test APIEntitiesAppearance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIEntitiesAppearance`
        """
        model = APIEntitiesAppearance()
        if include_optional:
            return APIEntitiesAppearance(
                title = '',
                description = '',
                pwa_name = '',
                pwa_short_name = '',
                pwa_description = '',
                logo = '',
                pwa_icon = '',
                header_logo = '',
                favicon = '',
                new_project_guidelines = '',
                profile_image_guidelines = '',
                header_message = '',
                footer_message = '',
                message_background_color = '',
                message_font_color = '',
                email_header_and_footer_enabled = ''
            )
        else:
            return APIEntitiesAppearance(
        )
        """

    def testAPIEntitiesAppearance(self):
        """Test APIEntitiesAppearance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
