from typing import Dict, List
from abc import ABC, abstractmethod
import logging
import logging.config
from parts_data.cpu import CPUS

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")


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
        try:
            return [cpu["brand_name"] for cpu in self.cpus]
        except Exception as e:
            logger.error(e)

    def get_names(self) -> List[str]:
        try:
            return [cpu["name"] for cpu in self.cpus]
        except Exception as e:
            logger.error(e)

    def get_prices(self) -> List[Dict[str, float]]:
        try:
            return [{cpu["name"]: f'${cpu["price"]}'} for cpu in self.cpus]
        except Exception as e:
            logger.error(e)

    def get_core_count(self) -> List[Dict[str, int]]:
        try:
            return [{"name": cpu["name"], "Cores": cpu["cores"]} for cpu in self.cpus]
        except Exception as e:
            logger.error(e)

    def get_perfomance(self) -> List[Dict[str, str]]:
        try:
            return [
                {"name": cpu["name"], "Perfomance": cpu["performance"]}
                for cpu in self.cpus
            ]
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    cpu = CPU()
    print(cpu.get_brand_names())
    print(cpu.get_names())
    print(cpu.get_prices())
    print(cpu.get_core_count())
    print(cpu.get_perfomance())
