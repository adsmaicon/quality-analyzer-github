from src.service.external.github.type_sort_github import TypeSortGithub
from src.service.external.service_base import ServiceBase
from src.settings import GITHUB


class GithubService(ServiceBase):

    def __init__(self):
        self.__header_acept = {"Accept": GITHUB["HEADER_ACEPT"]}
        self.__url_repos = GITHUB["REPOSITORIES"]
        super().__init__()

    def get_info_repositorios(self, filter, sort: TypeSortGithub = TypeSortGithub.STARS):
        params = {
            "q": filter,
            "sort": sort,
            "order": "desc",
            "per_page": 50,
            "page": 1
        }
        return self._request(url=self.__url_repos, params=params, headers=self.__header_acept)

    def get_infos_repos(self, url_pull_requests):
        url_pull_requests = url_pull_requests.replace("{/number}", "")
        params = {
            "sort": "created",
            "order": "desc",
            "per_page": 50,
            "page": 1
        }
        return self._request(url=url_pull_requests, params=params, headers=self.__header_acept)
