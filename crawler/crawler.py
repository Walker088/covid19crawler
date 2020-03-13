# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Crawler(ABC):
    @abstractmethod
    def updateData(self):
        return NotImplemented