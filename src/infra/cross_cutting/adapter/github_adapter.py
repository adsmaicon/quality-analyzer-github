from src.domain.entity.github_repo import GithubRepo


def GithubAdapter(func):

    def wrapper(*args) -> list:
        result = func(*args)

        response = []
        for r in result:
            github_repo = GithubRepo()
            
            github_repo.repository = r.get("repository")                        
            github_repo.pull_requests = r["pull_requests"]
            github_repo.issues = r["issues"]

            response.append(github_repo)

        return response

    return wrapper
