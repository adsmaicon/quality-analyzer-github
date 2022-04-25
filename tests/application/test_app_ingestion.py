import json
from src.application.app_ingestion import AppIngestion
from src.service.queue.queue import Queue
from src.settings import QUEUE
from tests.fixtures.request_fixture import github_mock
from tests.settings import GITHUB_MOCK_FILES


def test_app_ingestion(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    message = queue.receive_message()
    assert message is not None

    queue.queue_purge()


def test_app_ingestion_count_messages(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    after_count, message = queue.receive_message()
    assert after_count.message_count == 49

    queue.queue_purge()


def test_app_ingestion_pull_requests_body(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    after_count, message = queue.receive_message()

    result = json.loads(message.decode())

    repositorie_name = result.get("repository").get("name")

    with open(GITHUB_MOCK_FILES["PULL_REQUEST"].format(repositorie_name), encoding='utf-8') as f:
        repositorie_name = f.read()

    assert result.get("pull_requests") == json.loads(repositorie_name)

    queue.queue_purge()


def test_app_ingestion_issues_body(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    after_count, message = queue.receive_message()

    result = json.loads(message.decode())

    repositorie_name = result.get("repository").get("name")

    with open(GITHUB_MOCK_FILES["ISSUES_REQUEST"].format(repositorie_name), encoding='utf-8') as f:
        repositorie_name = f.read()

    assert result.get("issues") == json.loads(repositorie_name)

    queue.queue_purge()


def test_app_ingestion_pull_request_body(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    after_count, message = queue.receive_message()

    result = json.loads(message.decode())

    repositorie_name = result.get("repository").get("name")

    with open(GITHUB_MOCK_FILES["PULL_REQUEST"].format(repositorie_name), encoding='utf-8') as f:
        repositorie_name = f.read()

    assert result.get("pull_requests") == json.loads(repositorie_name)

    queue.queue_purge()


def test_app_ingestion_all_queue(github_mock):
    # Given
    queue = Queue(QUEUE["QUEUE_NAME"])

    # When
    AppIngestion.run()

    # Then
    has_message = True

    while has_message:
        after_count, message = queue.receive_message()

        if after_count is None:
            has_message = False
            continue

        result = json.loads(message.decode())

        repositorie_name = result.get("repository").get("name")

        with open(GITHUB_MOCK_FILES["PULL_REQUEST"].format(repositorie_name), encoding='utf-8') as f:
            file_pull_request = f.read()

        assert result.get("pull_requests") == json.loads(file_pull_request)

    queue.queue_purge()
