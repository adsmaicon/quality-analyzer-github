# from src.application.app_processing import AppProcessing
# from src.service.queue.queue import Queue
# from src.settings import QUEUE
# from tests.fixtures.request_fixture import github_mock


# def test_app_processing(github_mock):
#     # Given
#     queue = Queue(QUEUE["QUEUE_NAME"])

#     # When
#     AppProcessing.run()

#     # Then
#     message = queue.receive_message()
#     assert message is not None

#     queue.queue_purge()
