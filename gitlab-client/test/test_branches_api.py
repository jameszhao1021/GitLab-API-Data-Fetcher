# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.branches_api import BranchesApi


class TestBranchesApi(unittest.TestCase):
    """BranchesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BranchesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_api_v4_projects_id_repository_branches_branch(self) -> None:
        """Test case for delete_api_v4_projects_id_repository_branches_branch

        """
        pass

    def test_delete_api_v4_projects_id_repository_merged_branches(self) -> None:
        """Test case for delete_api_v4_projects_id_repository_merged_branches

        """
        pass

    def test_get_api_v4_projects_id_repository_branches(self) -> None:
        """Test case for get_api_v4_projects_id_repository_branches

        """
        pass

    def test_get_api_v4_projects_id_repository_branches_branch(self) -> None:
        """Test case for get_api_v4_projects_id_repository_branches_branch

        """
        pass

    def test_head_api_v4_projects_id_repository_branches_branch(self) -> None:
        """Test case for head_api_v4_projects_id_repository_branches_branch

        """
        pass

    def test_post_api_v4_projects_id_repository_branches(self) -> None:
        """Test case for post_api_v4_projects_id_repository_branches

        """
        pass

    def test_put_api_v4_projects_id_repository_branches_branch_protect(self) -> None:
        """Test case for put_api_v4_projects_id_repository_branches_branch_protect

        """
        pass

    def test_put_api_v4_projects_id_repository_branches_branch_unprotect(self) -> None:
        """Test case for put_api_v4_projects_id_repository_branches_branch_unprotect

        """
        pass


if __name__ == '__main__':
    unittest.main()
