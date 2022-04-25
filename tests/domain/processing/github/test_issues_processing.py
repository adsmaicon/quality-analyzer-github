import json
from src.domain.entity.score import Score
from src.domain.processing.github.issues_processing import IssuesProcessing
from tests.settings import GITHUB_MOCK_FILES
from freezegun import freeze_time


def test_issues_processing():
    # Given
    issues_processing = IssuesProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    issues = repository["issues"]

    # When
    issues_result = issues_processing.analyze(score, issues)

    # Then
    assert type(issues_result) == Score


@freeze_time("2022-04-01")
def test_issues_processing_score_zero():
    # Given
    issues_processing = IssuesProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    issues = repository["issues"]

    # When
    issues_result = issues_processing.analyze(score, issues)

    # Then
    assert issues_result.activity == 0.03


@freeze_time("2022-04-01")
def test_issues_processing_score():
    # Given
    issues_processing = IssuesProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("ansible"), encoding='utf-8') as f:
        repository= json.loads(f.read())

    issues = repository["issues"]

    # When
    issues_result = issues_processing.analyze(score, issues)

    # Then
    assert issues_result.activity == 1.0
