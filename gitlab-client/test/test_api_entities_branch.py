# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_entities_branch import APIEntitiesBranch

class TestAPIEntitiesBranch(unittest.TestCase):
    """APIEntitiesBranch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIEntitiesBranch:
        """Test APIEntitiesBranch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIEntitiesBranch`
        """
        model = APIEntitiesBranch()
        if include_optional:
            return APIEntitiesBranch(
                name = 'master',
                commit = openapi_client.models.api_entities_commit.API_Entities_Commit(
                    id = '2695effb5807a22ff3d138d593fd856244e155e7', 
                    short_id = '2695effb', 
                    created_at = '2017-07-26T11:08:53+02:00', 
                    parent_ids = [
                        '2a4b78934375d7f53875269ffd4f45fd83a84ebe'
                        ], 
                    title = 'Initial commit', 
                    message = 'Initial commit', 
                    author_name = 'John Smith', 
                    author_email = 'john@example.com', 
                    authored_date = '2012-05-28T04:42:42-07:00', 
                    committer_name = 'Jack Smith', 
                    committer_email = 'jack@example.com', 
                    committed_date = '2012-05-28T04:42:42-07:00', 
                    trailers = { "Merged-By": "Jane Doe janedoe@gitlab.com" }, 
                    web_url = 'https://gitlab.example.com/janedoe/gitlab-foss/-/commit/ed899a2f4b50b4370feeea94676502b42383c746', ),
                merged = True,
                protected = True,
                developers_can_push = True,
                developers_can_merge = True,
                can_push = True,
                default = True,
                web_url = 'https://gitlab.example.com/Commit921/the-dude/-/tree/master'
            )
        else:
            return APIEntitiesBranch(
        )
        """

    def testAPIEntitiesBranch(self):
        """Test APIEntitiesBranch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
