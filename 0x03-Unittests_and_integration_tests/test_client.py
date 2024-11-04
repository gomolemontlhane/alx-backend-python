#!/usr/bin/env python3
"""
Unittests and integration tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization data."""
        mock_get_json.return_value = org_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), org_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property of GithubOrgClient."""
        mock_org.return_value = org_payload
        client = GithubOrgClient("test-org")
        self.assertEqual(client._public_repos_url, org_payload["repos_url"])

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method of GithubOrgClient."""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"
        mock_get_json.return_value = repos_payload
        client = GithubOrgClient("test-org")
        self.assertEqual(client.public_repos(), expected_repos)
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method of GithubOrgClient."""
        client = GithubOrgClient("test-org")
        self.assertEqual(client.has_license(repo, license_key), expected)

# Integration test setup
@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, 
     "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests by patching requests.get."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()
        mock_get.return_value.json.side_effect = lambda: cls.org_payload

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()
