from tests.fixtures.request_fixture import github_mock
from src.service.external.github.github_service import GithubService


def test_get_issues(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/public-apis/public-apis/issues"
    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert repositories_python is not None


def test_get_issues_is_not_none(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/public-apis/public-apis/issues"
    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert repositories_python is not None

def test_get_issues_list_type(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/public-apis/public-apis/issues"
    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert type(repositories_python) == list
