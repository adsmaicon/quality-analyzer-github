from src.domain.entity.score import Score


class RepositoryProcessing():

    def analyze(self, score: Score, repository) -> Score:        
        score.license = 1 if repository.get("license") else 0
        return score
