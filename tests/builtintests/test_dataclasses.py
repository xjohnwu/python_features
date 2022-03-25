from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Address:
    city: str
    postcode: str


@dataclass
class Person:
    name: str
    addresses: List[Address]


def test_data():
    address1 = Address("London", "EC2 2FA")
    address2 = Address("Paris", "545887")

    person = Person(name='John', addresses=[address1, address2])
    json = asdict(person)
    print(json)
