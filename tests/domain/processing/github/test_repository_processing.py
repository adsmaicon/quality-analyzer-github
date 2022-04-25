
import json
from src.domain.entity.score import Score
from src.domain.processing.github.repository_processing import RepositoryProcessing
from tests.settings import GITHUB_MOCK_FILES


def test_repository_processing():
    # Given
    repository_processing = RepositoryProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository = json.loads(f.read())

    repository = repository["repository"]

    # When
    repository_result = repository_processing.analyze(score, repository)

    # Then
    assert type(repository_result) == Score


def test_repository_processing_score():
    # Given
    repository_processing = RepositoryProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("google_research_bert"), encoding='utf-8') as f:
        repository = json.loads(f.read())

    repository = repository["repository"]

    # When
    repository_result = repository_processing.analyze(score, repository)

    # Then
    assert repository_result.license == 1.0


def test_repository_processing_score_zero():
    # Given
    repository_processing = RepositoryProcessing()
    score = Score()

    with open(GITHUB_MOCK_FILES["GITHUB_REPO"].format("Python-100-Days"), encoding='utf-8') as f:
        repository = json.loads(f.read())

    repository = repository["repository"]

    # When
    repository_result = repository_processing.analyze(score, repository)

    # Then
    assert repository_result.license == 0
