from clinic.models import HealthProblem, Client
from math import e

def associate_client_with_health_problems_list(client: Client, health_problems: list[dict]) -> None:
    for health_problem in health_problems:
        health_problem_instance, _ = HealthProblem.objects.get_or_create(**health_problem)
        client.health_problems.add(health_problem_instance)


def calculate_score_from_health_problems(health_problems) -> float:
    """
        sd = sum of the degree of problems
        score = (1 / (1 + e^-(-2.8 + sd ))) * 100
    """

    def get_degree_from_health_problem(health_problem):
        return health_problem['degree']

    sum_degree = sum(map(get_degree_from_health_problem, health_problems))
    score = (1/ (1 + e ** (-(-2.8 + sum_degree)))) * 100

    return score