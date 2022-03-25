from abc import ABC, abstractmethod
from unittest.mock import Mock


class EngineBase(ABC):
    @abstractmethod
    def place_order(self):
        pass


class SignalProcessor:
    def __init__(self, engine: EngineBase):
        self.engine: EngineBase = engine

    def process(self):
        return self.engine.place_order()


class TestMocking:
    def test_mock_method(self):
        mock = Mock()
        mock.place_order = Mock(return_value='from Mock')
        self.processor = SignalProcessor(mock)
        assert 'from Mock' == self.processor.process()
