from src.domain.entity.score import Score


class PullRequestsProcessing():

    def analyze(self, score: Score, pull_requests: list) -> Score:
        SECURITY_CONTAINS = "security"
        score.security = self.__analyze_score(pull_requests, SECURITY_CONTAINS)

        UPDATED_CONTAINS = "bump"
        score.updated = self.__analyze_score(pull_requests, UPDATED_CONTAINS)

        return score

    def __analyze_score(self, pull_requests, word):        
        pulls_insecure = list(filter(
            lambda x: self.__constains_info(x, word),
            pull_requests
        ))
        return 1.0 if len(pulls_insecure) == 0 else round(1.0 - len(pulls_insecure)/len(pull_requests), 2)


    def __constains_info(self, pull, word):
        for p in pull:
            data = pull.get(p)

            if type(data) is str:
                if data.lower().__contains__(word):
                    return True
