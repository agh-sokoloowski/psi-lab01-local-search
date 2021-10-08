from abc import abstractmethod, ABC
from typing import Generator, List, Union

from local_search.algorithm_subscribers.algorithm_subscriber import AlgorithmSubscriber
from local_search.helpers.camel_to_snake import camel_to_snake
from local_search.algorithms.algorithm import Algorithm
from local_search.algorithms.algorithm_config import DEFAULT_CONFIG, AlgorithmConfig
from local_search.problems.base.problem import Problem
from local_search.problems.base.state import State


class SubscribableAlgorithm(Algorithm):
    """
    Generates next states for the problem based on some logic.
    """
    algorithms = {}

    def __init__(self, config: AlgorithmConfig = None):
        super().__init__()
        config = config or DEFAULT_CONFIG
        self.config = config
        self.steps_from_last_state_update = 0
        self.best_obj, self.best_state = None, None
        self._subscribers: List[AlgorithmSubscriber] = []

    def __init_subclass__(cls) -> None:
        if ABC not in cls.__bases__:
            SubscribableAlgorithm.algorithms[camel_to_snake(
                cls.__name__)] = cls

    @abstractmethod
    def _find_next_state(self, model: Problem, state: State) -> Union[State, None]:
        """
        Finds next state for model. Returns None in case if state is optimal.
        """

    def _random_restart(self, model: Problem) -> State:
        """
        Returns a random state.
        """
        return model.random_state()

    def _perturb(self, model: Problem, size: int) -> State:
        """
        Returns a perturbed best state.
        It repeatedly performs random moves
        (size parameter tells how many times)
        """
        perturbed_state = self.best_state
        for _ in range(size):
            perturbed_state = next(
                model.move_generator.random_moves(perturbed_state)).make()
        return perturbed_state

    def _get_neighbours(self, model: Problem, state: State) -> Generator[State, None, None]:
        """
            Generates neighbors of the given state based on the neighborhood operator
            defined in the problem.
        """
        for move in model.move_generator.available_moves(state):
            neighbour = move.make()
            self._on_next_neighbour(model, state, neighbour)
            yield neighbour

    def _get_random_neighbours(self, model: Problem, state: State) -> Generator[State, None, None]:
        """
            Generates neighbors of the given state in the random fashion.

            WARNING: this generator may never exhaust, so don't rely on its termination properties
            tip. if you want to get just a single random neighbor, call it with next, i.e.
                random_state = next(_get_random_neighbours(model, state)
        """
        for move in model.move_generator.random_moves(state):
            neighbour = move.make()
            self._on_next_neighbour(model, state, neighbour)
            yield neighbour

    def _is_stuck_in_local_optimum(self) -> bool:
        """
            Checks whether the algorithm got stuck in the local optimum.
            Just checks how many times algorithm failed to improve the current solution.
        """
        return self.steps_from_last_state_update >= self.config.local_optimum_moves_threshold

    def next_state(self, model: Problem, state: State) -> Union[State, None]:
        """
            The local search skeleton:
            — it tracks the best state (self.best_state)
            — checks if the algorithm got stuck in the local optimum (self._is_stuck_in_local_optimum())
                * if that's case, tries to escape the minimum (self.escape_local_optimum)
            — repeatedly finds the next neighbor based on the implemented metaheuristics (_self._find_next_state)
                * if there is no neighbhor — it terminates

            The other methods (_on_next_state, _on_local_optimum_escape) just make sure the algorithm gets displayed
            correctly and so on. Don't worry about this.
        """
        if self.best_state is None:
            self.best_state = state
            self._on_next_state(model, state)

        if self._is_stuck_in_local_optimum():
            next_state = self.escape_local_optimum(
                model, state, self.best_state)
            self._on_local_optimum_escape(
                model, from_state=state, to_state=next_state)

        else:
            next_state = self._find_next_state(model, state)

        if next_state is not None:
            self._update_algorithm_state(model, state, next_state)
            self._on_next_state(model, next_state)
        else:
            self._on_solution(model, state)

        return next_state

    def _update_algorithm_state(self, model: Problem, state, new_state: State):
        """
        Tracks the solving process:
        - best_state
        - number of steps since the last improvement (used to detect local optima)
        """
        if self.best_state is None:
            self.best_state = new_state

        if model.improvement(new_state, state) > 0:
            self.steps_from_last_state_update = 0
        else:
            self.steps_from_last_state_update += 1

        if model.improvement(new_state, self.best_state) > 0:
            self.best_obj, self.best_state = model.objective_for(
                new_state), new_state


    def _on_next_state(self, model: Problem, next_state: State):
        """Called when algorithm find new best state"""
        for subscriber in self._subscribers:
            subscriber.on_next_state(model, next_state)

    def _on_next_neighbour(self, model: Problem, from_state: State, next_neighbour: State):
        """Called when algorithm explores next neighbour"""
        for subscriber in self._subscribers:
            subscriber.on_next_neighbour(model, from_state, next_neighbour)

    def _on_solution(self, model: Problem, solution: State):
        for subscriber in self._subscribers:
            subscriber.on_solution(model=model, solution=solution)

    def _on_local_optimum_escape(self, model: Problem, from_state: State, to_state: Union[State, None]):
        for subscriber in self._subscribers:
            subscriber.on_local_optimum_escape(
                model=model, from_state=from_state, to_state=to_state)

    def subscribe(self, subsriber: AlgorithmSubscriber):
        self._subscribers.append(subsriber)
