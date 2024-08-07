# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_entities_cluster import APIEntitiesCluster

class TestAPIEntitiesCluster(unittest.TestCase):
    """APIEntitiesCluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIEntitiesCluster:
        """Test APIEntitiesCluster
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIEntitiesCluster`
        """
        model = APIEntitiesCluster()
        if include_optional:
            return APIEntitiesCluster(
                id = '',
                name = '',
                created_at = '',
                domain = '',
                enabled = '',
                managed = '',
                provider_type = '',
                platform_type = '',
                environment_scope = '',
                cluster_type = '',
                namespace_per_environment = '',
                user = openapi_client.models.api_entities_user_basic.API_Entities_UserBasic(
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
                    email = '', ),
                platform_kubernetes = openapi_client.models.api_entities_platform_kubernetes.API_Entities_Platform_Kubernetes(
                    api_url = '', 
                    namespace = '', 
                    authorization_type = '', 
                    ca_cert = '', ),
                provider_gcp = openapi_client.models.api_entities_provider_gcp.API_Entities_Provider_Gcp(
                    cluster_id = '', 
                    status_name = '', 
                    gcp_project_id = '', 
                    zone = '', 
                    machine_type = '', 
                    num_nodes = '', 
                    endpoint = '', ),
                management_project = openapi_client.models.api_entities_project_identity.API_Entities_ProjectIdentity(
                    id = 1, 
                    description = 'desc', 
                    name = 'project1', 
                    name_with_namespace = 'John Doe / project1', 
                    path = 'project1', 
                    path_with_namespace = 'namespace1/project1', 
                    created_at = '2020-05-07T04:27:17.016Z', )
            )
        else:
            return APIEntitiesCluster(
        )
        """

    def testAPIEntitiesCluster(self):
        """Test APIEntitiesCluster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
