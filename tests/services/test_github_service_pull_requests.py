import json
from src.service.external.github.github_service import GithubService
from tests.fixtures.request_fixture import github_mock
from tests.settings import GITHUB_MOCK_FILES


def test_get_pull_requests_empyt(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/public-apis/public-apis/pulls"
    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert repositories_python == []


def test_get_pull_requests_list_type(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/public-apis/public-apis/pulls"
    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert type(repositories_python) == list


def test_get_pull_requests(github_mock):
    # Given
    PULL_REQUEST_URL = "https://api.github.com/repos/tiangolo/fastapi/pulls"

    with open(GITHUB_MOCK_FILES["PULL_REQUEST"].format("fastapi"), encoding='utf-8') as f:
        pull_request_mock = f.read()

    git_service = GithubService()

    # When
    repositories_python = git_service.get_infos_repos(PULL_REQUEST_URL)

    # Then
    assert repositories_python == json.loads(pull_request_mock)
