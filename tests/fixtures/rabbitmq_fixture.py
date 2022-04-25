from cgi import test
import pytest
import docker

container_queue = None

def rabbitmq_create_docker_mock():   
    client = docker.from_env()
    container_queue = client.containers.run(
        "rabbitmq",
        volumes=['rabbitmq-persistence:/bitnami:rw'],
        ports={5672: 6666},
        name="test_rabbitmq",
        detach=True
    )


def rabbitmq_destroy_docker_mock():
    container_queue.stop()
    container_queue.remove()
