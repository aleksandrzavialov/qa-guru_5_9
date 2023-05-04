import dataclasses
from typing import List


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: str
    subjects: List[str]
    hobby: str
    picture: str
    address: str
    state: str
    city: str