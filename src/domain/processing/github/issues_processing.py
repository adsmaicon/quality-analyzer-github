from dateutil import parser
from datetime import datetime, timedelta
from src.domain.entity.score import Score


class IssuesProcessing():

    def analyze(self, score: Score, issues: list) -> Score:
        score.activity = self.__analyze_score(issues)

        return score

    def __analyze_score(self, issues):
        issues_activity = list(filter(
            self.__verify_info,
            issues
        ))
        return 1.0 if len(issues_activity) == 0 else round(1.0 - len(issues_activity)/len(issues), 2)

    def __verify_info(self, issues):
        create_at = parser.parse(issues.get('created_at')).date()
        create_at += timedelta(days=30)
        today = datetime.now().date()

        return today > create_at
