from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional
from functools import total_ordering

@total_ordering
@dataclass
class Person:
    """Example dataclass demonstrating key features."""
    name: str
    age: int
    email: str
    hobbies: List[str] = field(default_factory=list)
    is_active: bool = True
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        """Validation after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        self.email = self.email.lower()
    
    def __lt__(self, other):
        """Enable sorting by age."""
        return self.age < other.age
    
    def __eq__(self, other):
        """Custom equality comparison."""
        return self.name == other.name and self.age == other.age

# Usage examples
if __name__ == "__main__":
    # Basic initialization
    p1 = Person("Alice", 30, "ALICE@EXAMPLE.COM", ["reading", "coding"])
    
    # With defaults
    p2 = Person("Bob", 25, "bob@example.com")
    
    # Auto-generated methods
    print(p1)  # __str__ and __repr__
    print(f"Dict: {asdict(p1)}")
    print(f"Tuple: {astuple(p1)}")
    
    # Sorting
    people = [p1, p2, Person("Charlie", 35, "charlie@example.com")]
    for person in sorted(people):
        print(person.name, person.age)