from abc import ABC, abstractmethod


class ServiceTemplate(ABC):
    @abstractmethod
    def run(self):
        pass
