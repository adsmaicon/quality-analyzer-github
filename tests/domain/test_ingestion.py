import json
from src.domain.ingestion import Ingestion
from tests.fixtures.request_fixture import github_mock


def fetch_data(assert_file, repository):
    ingestion = Ingestion()
    with open(assert_file) as f:
        file = json.loads(f.read())

    # When
    response = ingestion.fetch_data()

    # Then
    data_bert = filter(
        lambda x: x.repository["full_name"].__contains__(repository),
        response
    )
    return list(data_bert)[0].__dict__, file


def test_ingest_fetch_data(github_mock):
    # Given
    ingestion = Ingestion()
    # When
    response = ingestion.fetch_data()
    # Then
    assert response


def test_ingest_fetch_data_not_none(github_mock):
    # Given
    ingestion = Ingestion()
    # When
    response = ingestion.fetch_data()
    # Then
    assert response


def test_ingest_fetch_data_google_research_bert(github_mock):
    # Given
    ASSERT_FILE = "tests/files/github_repo/google_research_bert.json"
    REPOSITORY = "google-research/bert" 

    # When
    data_bert, google_research_bert = fetch_data(ASSERT_FILE, REPOSITORY)

    # Then
    assert data_bert == google_research_bert


def test_ingest_fetch_data_public_apis(github_mock):
    # Given
    ASSERT_FILE = "tests/files/github_repo/public_apis.json"
    REPOSITORY = "public-apis/public-apis"

    # When
    data_public_apis, public_apis = fetch_data(ASSERT_FILE, REPOSITORY)

    # Then
    assert data_public_apis == public_apis
