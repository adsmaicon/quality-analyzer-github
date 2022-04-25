import os

GENERAL = {
    "APP_ENV": os.getenv("APP_ENV")
}


GITHUB = {
    "USER": os.getenv('GITHUB_USER'),
    "AUTH_KEY": os.getenv('GITHUB_AUTH_KEY'),
    "HEADER_ACEPT": "application/vnd.github.v3+json",
    "REPOSITORIES": "https://api.github.com/search/repositories",    
}

QUEUE = {    
    "QUEUE_HOST": os.getenv('QUEUE_HOST'),
    "QUEUE_PORT": os.getenv('QUEUE_PORT'),
    "QUEUE_NAME": os.getenv('QUEUE_NAME')
}
