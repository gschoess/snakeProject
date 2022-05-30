#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from abc import ABC, abstractmethod


class Scene(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass
