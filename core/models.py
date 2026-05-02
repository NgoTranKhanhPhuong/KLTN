from dataclasses import dataclass, field

@dataclass
class TestCase:
    id: str
    name: str
    data: dict
    expected: dict
    source: str = "rule"
    priority: str = "High"
    actual: dict = None
    passed: bool = None
    features: set = field(default_factory=set)