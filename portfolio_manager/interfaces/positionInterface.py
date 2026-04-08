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

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from implementations.securitySolution import security

#Position Class Interface. 
from .securityInterface import securityInterface
class positionInterface():
    def __init__(self, securityIn, initialPosition: int) -> None:
        self.initialPosition = initialPosition
        self.positionValue = initialPosition

        if isinstance(securityIn, securityInterface):
            self.security = securityIn
        else:
            self.security = security(securityIn)

    def __str__(self):
        return f"{self.security}, Position: {self.positionValue}"
    
    def getSecurity(self) -> securityInterface:
        return self.security

    def getPosition(self) -> int:
        return self.positionValue
    
    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception("Position should be a long!")
        self.positionValue = inputValue
    
    #Add an integer amount to the current position.
    def addPosition(self, inputValue: int) -> None:
        if position + inputValue < 0:
            raise Exception("position will be a short if value is added!")
        self.positionValue += inputValue
