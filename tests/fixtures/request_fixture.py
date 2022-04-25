
import json
import pytest
import requests_mock
from src.settings import GITHUB
from tests.settings import GITHUB_MOCK_FILES


@pytest.fixture
def github_mock():
    url = GITHUB["REPOSITORIES"]
    with open(GITHUB_MOCK_FILES["REPOSITORIES"], encoding='utf-8') as f:
        response_mock = f.read()
    with requests_mock.Mocker() as mock_request:
        repos = json.loads(response_mock)

        for r in repos.get("items"):
            url_pull_request = r.get("pulls_url").replace("{/number}", '')

            with open(GITHUB_MOCK_FILES["PULL_REQUEST"].format(r.get("pulls_url").split('/')[5]), encoding='utf-8') as f:
                pull_request_mock = f.read()
                mock_request.get(url_pull_request, text=pull_request_mock)

            url_issues = r.get("issues_url").replace("{/number}", '')

            with open(GITHUB_MOCK_FILES["ISSUES_REQUEST"].format(r.get("issues_url").split('/')[5]), encoding='utf-8') as f:
                pull_request_mock = f.read()
                mock_request.get(url_issues, text=pull_request_mock)

        mock_request.get(url, text=response_mock)

        yield mock_request
