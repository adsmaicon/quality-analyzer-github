import json
from src.service.external.github.github_service import GithubService
from tests.fixtures.request_fixture import github_mock
from tests.settings import GITHUB_MOCK_FILES


def test_get_repositories(github_mock):
    # Given
    git_service = GithubService()

    # When
    repositories_python = git_service.get_info_repositorios(
        'language:python', 'stars')

    # Then
    assert repositories_python is not None


def test_get_repositories_type_dict(github_mock):
    # Given
    git_service = GithubService()

    # When
    repositories_python = git_service.get_info_repositorios(
        'language:python', 'stars')

    # Then
    assert type(repositories_python) == dict


def test_get_repositories_all(github_mock):
    # Given
    git_service = GithubService()
    with open(GITHUB_MOCK_FILES["REPOSITORIES"], encoding='utf-8') as f:
        response_mock = f.read()

    # When
    repositories_python = git_service.get_info_repositorios(
        'language:python', 'stars')

    # Then
    assert repositories_python == json.loads(response_mock)


def test_get_repositories_len(github_mock):
    # Given
    git_service = GithubService()

    # When
    repositories_python = git_service.get_info_repositorios(
        'language:python', 'stars')
    # Then
    assert len(repositories_python.get('items')) == 50
