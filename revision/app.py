from typing import Dict, List, Any
from abc import ABC, abstractmethod
from parts_data.cpu import CPUS


class PartPicker(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_names(self) -> List[str]:
        pass

    @abstractmethod
    def get_prices(self) -> List[Dict[str, float]]:
        pass

    @abstractmethod
    def get_brand_names(self) -> List[str]:
        pass


class CPU(PartPicker):
    def __init__(self) -> None:
        self.cpus = CPUS

    def get_brand_names(self) -> List[str]:
        return [cpu["brand_name"] for cpu in self.cpus]

    def get_names(self) -> List[str]:
        return [cpu["name"] for cpu in self.cpus]

    def get_prices(self) -> List[Dict[str, Any]]:
        return [{cpu["name"]: f'${cpu["price"]}'} for cpu in self.cpus]

    def get_core_count(self) -> List[Dict[str, Any]]:
        return [{"name": cpu["name"], "Cores": cpu["cores"]} for cpu in self.cpus]

    def get_perfomance(self) -> List[Dict[str, Any]]:
        return [
            {"name": cpu["name"], "Perfomance": cpu["performance"]} for cpu in self.cpus
        ]


if __name__ == "__main__":
    cpu = CPU()
    print(cpu.get_brand_names())
    print(cpu.get_names())
    print(cpu.get_prices())
    print(cpu.get_core_count())
    print(cpu.get_perfomance())
