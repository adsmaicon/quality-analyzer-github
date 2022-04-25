import json
from src.domain.entity.score import Score
from src.domain.processing.github.pull_requests_processing import PullRequestsProcessing
from tests.settings import GITHUB_MOCK_FILES


def test_github_pull_request_processing():
    # Given
    pull_request_processing = PullRequestsProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    pull_requests = repository["pull_requests"]

    # When
    score_result = pull_request_processing.analyze(score, pull_requests)

    # Then
    assert type(score_result) == Score


def test_github_pull_request_processing_security():
    # Given
    pull_request_processing = PullRequestsProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    pull_requests = repository["pull_requests"]

    # When
    score = pull_request_processing.analyze(score, pull_requests)

    # Then
    assert score.security > 0.0


def test_github_pull_request_processing_updated():
    # Given
    pull_request_processing = PullRequestsProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    pull_requests = repository["pull_requests"]

    # When
    score = pull_request_processing.analyze(score, pull_requests)

    # Then
    assert score.updated > 0.0


def test_github_pull_request_processing_security_score():
    # Given
    pull_request_processing = PullRequestsProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("airflow"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    pull_requests = repository["pull_requests"]

    # When
    score = pull_request_processing.analyze(score, pull_requests)

    # Then
    assert score.security == 0.93

def test_github_pull_request_processing_updated_score():
    # Given
    pull_request_processing = PullRequestsProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("airflow"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    pull_requests = repository["pull_requests"]

    # When
    score = pull_request_processing.analyze(score, pull_requests)

    # Then
    assert score.updated == 0.97
