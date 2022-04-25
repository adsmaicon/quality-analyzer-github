from src.infra.cross_cutting.adapter.github_adapter import GithubAdapter
from src.service.external.github.github_service import GithubService


class GithubIngestion():

    def __init__(self):
        self.github_service = GithubService()

    @GithubAdapter
    def fetch_data(self):
        response = []
        repos = self.github_service.get_info_repositorios("language:python")

        for r in repos.get("items"):
            repositorio = {}
            repositorio["repository"] = r
            repositorio["pull_requests"] = self.github_service.get_infos_repos(r.get("pulls_url"))
            repositorio["issues"] = self.github_service.get_infos_repos(r.get("issues_url"))

            response.append(repositorio)

        return response
