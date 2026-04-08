# Copyright 2022 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .positionInterface import positionInterface
from .securityInterface import securityInterface
from typing import Any, Dict, Set, Iterable
import copy 
class accountInterface():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.positions = {posItem.getSecurity().getName(): posItem for posItem in positions}
        self.accountName = accountName

    def __str__(self):
        return self.accountName

    #Return the account's name
    def getName(self) -> str:
        return self.accountName

    #Return all positions currently within the account
    def getAllPositions(self) -> Iterable[positionInterface]:
        return list(self.positions.values())

    #Return all positions that contain a security in a given input set
    def getPositions(self, securities: Set) -> Dict[str, positionInterface]:
        securityToPos = {}

        for security in securities:
            if isinstance(security, securityInterface):
                name = security.getName()
            else:
                name = security
            
            if name in self.positions:
                securityToPos[security] = self.positions[name]

        return securityToPos 

    #Add positions to the account
    def addPositions(self, positions: Set[positionInterface]) -> None:
        for pos in positions:
            if pos.getSecurity().getName() in self.positions:
                self.positions[pos.getSecurity().getName()].setPosition(pos.getPosition())
            else:
                self.positions[pos.getSecurity().getName()] = pos
    
    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:
        for security in securities:
            if isinstance(security, securityInterface):
                self.positions.pop(security.name)
            else:
                self.positions.pop(security)

