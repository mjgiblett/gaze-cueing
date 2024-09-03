from dataclasses import dataclass
from typing import Any, Iterator


@dataclass
class Participant:
    id: int
    age: int
    gender: int
    culture: int

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for key, value in self.__dict__.items():
            yield f"participant_{key}", value
