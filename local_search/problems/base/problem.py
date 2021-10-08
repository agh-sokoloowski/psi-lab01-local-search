import local_search
from abc import ABC, abstractmethod
from pathlib import Path
from enum import Enum
from typing import Iterable, Type
from local_search.helpers.camel_to_snake import camel_to_snake
from local_search.problems.base.goal import Goal
from local_search.problems.base.state import State
from local_search.problems.base.move_generator import MoveGenerator
from dataclasses import dataclass

class Problem(ABC):
    """
    Contains all information about problem we are trying to solve.
    """
    problems = {}

    def __init__(self, initial_solution: State, move_generator: MoveGenerator, goal: Goal):
        self.initial_solution = initial_solution
        self.move_generator = move_generator
        self.goal = goal

    def __init_subclass__(cls):
        Problem.problems[camel_to_snake(cls.__name__)] = cls

    @abstractmethod
    def random_state(self) -> State:
        """
        Generates a random state
        """

    def objective_for(self, state: State) -> int:
        """
        Just a helper proxy method
        """
        return self.goal.objective_for(state)

    def improvement(self, new_state: State, old_state: State) -> int:
        """
        A helper method. Calculates how much the new_state is better than the old_state.
        Takes optimization goal under consideration.
        """
        improvement = self.objective_for(new_state) - self.objective_for(old_state)
        return improvement * self.goal.type().value

    @staticmethod
    @abstractmethod
    def get_available_move_generation_strategies() -> Iterable[str]:
        """
        Available move generation strategies for this model.
        """

    @staticmethod
    @abstractmethod
    def get_available_goals() -> Iterable[str]:
        """
        Available goals for this model.
        """

    @staticmethod
    @abstractmethod
    def from_benchmark(benchmark_name: str, move_generator_name: str, goal_name: str) -> 'Problem':
        """
        Creates model from behcmark file
        """

    @classmethod
    def get_path_to_benchmarks(cls) -> Path:
        return Path(local_search.__file__).parent / "problems" / camel_to_snake(cls.__name__) / "benchmarks"
