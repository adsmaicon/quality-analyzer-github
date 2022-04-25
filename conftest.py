# from time import sleep
# import docker


# container_queue = None


# def pytest_sessionstart(session):
#     try:
#         global container_queue
#         client = docker.from_env()
#         container_queue = client.containers.run(
#             "rabbitmq",
#             # volumes=['rabbitmq-persistence:/bitnami:rw'],
#             ports={5672: 6666},
#             name="test_rabbitmq",
#             mem_limit="512m",
#             cpuset_cpus="0,5",
#             detach=True
#         )
#         sleep(4)
#     except Exception:
#         container_queue = client.containers.get("test_rabbitmq")
#         pass


# def pytest_sessionfinish(session, exitstatus):
#     try:
#         container_queue.stop()
#         container_queue.remove()
#     except Exception:
#         pass
