from typing import Union
import numpy as np
from local_search.algorithms.hill_climbing.hill_climbing import HillClimbing
from local_search.problems.base.state import State
from local_search.problems.base.problem import Problem


class WorstChoiceHillClimbing(HillClimbing):
    """
    Implementation of hill climbing local search.

    Pretty exotic version of hill climbing. Algorithm works, by checking all the available moves
    and selecting the worst one that improves the current state.
    """

    def _climb_the_hill(self, model: Problem, state: State) -> Union[State, None]:

        worst_improvement = {
            "improvement": np.inf,
            "neighbour": None
        }

        for neighbour in self._get_neighbours(model, state):
            if model.improvement(neighbour, state) < worst_improvement["improvement"]:
                worst_improvement["improvement"] = model.improvement(neighbour, state)
                worst_improvement["neighbour"] = neighbour

        return worst_improvement["neighbour"] if worst_improvement["neighbour"] is not None else state
