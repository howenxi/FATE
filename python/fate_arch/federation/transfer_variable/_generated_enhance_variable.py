#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

##########################################################
# Generated by scripts/generate_enhance_variable.py
##########################################################


import typing
from typing import Union

from fate_arch.common import Party
from fate_arch.federation.transfer_variable import Variable
from fate_arch.session import get_latest_opened


class _VariableProtocol(object):

    def remote_parties(self,
                       obj,
                       parties: Union[typing.List[Party], Party],
                       suffix: Union[typing.Any, typing.Tuple] = tuple()):
        raise NotImplementedError()

    def get_parties(self,
                    parties: Union[typing.List[Party], Party],
                    suffix: Union[typing.Any, typing.Tuple] = tuple()) -> typing.List:
        raise NotImplementedError()

    @staticmethod
    def roles_to_parties(roles):
        party_info = get_latest_opened().parties
        return party_info.roles_to_parties(roles)


# noinspection PyAbstractClass
class _ToArbiter(_VariableProtocol):
    def to_arbiter(self, obj, suffix):
        parties = self.roles_to_parties(["arbiter"])
        self.remote_parties(obj, parties, suffix)
    
    def to_kth_arbiter(self, obj, k, suffix):
        parties = self.roles_to_parties(["arbiter"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        self.remote_parties(obj, parties[k], suffix)


# noinspection PyAbstractClass
class _FromArbiter(_VariableProtocol):
    def from_arbiter(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["arbiter"])
        return self.get_parties(parties, suffix)

    def get_kth_arbiter(self, k, suffix) -> typing.Any:
        parties = self.roles_to_parties(["arbiter"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        results = self.get_parties(parties[k], suffix)
        return results[0]


# noinspection PyAbstractClass
class _ToGuest(_VariableProtocol):
    def to_guest(self, obj, suffix):
        parties = self.roles_to_parties(["guest"])
        self.remote_parties(obj, parties, suffix)
    
    def to_kth_guest(self, obj, k, suffix):
        parties = self.roles_to_parties(["guest"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        self.remote_parties(obj, parties[k], suffix)


# noinspection PyAbstractClass
class _FromGuest(_VariableProtocol):
    def from_guest(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["guest"])
        return self.get_parties(parties, suffix)

    def get_kth_guest(self, k, suffix) -> typing.Any:
        parties = self.roles_to_parties(["guest"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        results = self.get_parties(parties[k], suffix)
        return results[0]


# noinspection PyAbstractClass
class _ToHost(_VariableProtocol):
    def to_host(self, obj, suffix):
        parties = self.roles_to_parties(["host"])
        self.remote_parties(obj, parties, suffix)
    
    def to_kth_host(self, obj, k, suffix):
        parties = self.roles_to_parties(["host"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        self.remote_parties(obj, parties[k], suffix)


# noinspection PyAbstractClass
class _FromHost(_VariableProtocol):
    def from_host(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["host"])
        return self.get_parties(parties, suffix)

    def get_kth_host(self, k, suffix) -> typing.Any:
        parties = self.roles_to_parties(["host"])
        assert k < len(parties), f"index {k} out of range [0, {len(parties) - 1}]"
        results = self.get_parties(parties[k], suffix)
        return results[0]


# noinspection PyAbstractClass
class _FromArbiterGuest(_FromArbiter, _FromGuest):
    def from_guest_host(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["arbiter", "guest"])
        return self.get_parties(parties, suffix)


# noinspection PyAbstractClass
class _ToArbiterGuest(_ToArbiter, _ToGuest):
    def to_guest_host(self, obj, suffix):
        parties = self.roles_to_parties(["arbiter", "guest"])
        return self.remote_parties(obj, parties, suffix)


# noinspection PyAbstractClass
class _FromArbiterHost(_FromArbiter, _FromHost):
    def from_guest_host(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["arbiter", "host"])
        return self.get_parties(parties, suffix)


# noinspection PyAbstractClass
class _ToArbiterHost(_ToArbiter, _ToHost):
    def to_guest_host(self, obj, suffix):
        parties = self.roles_to_parties(["arbiter", "host"])
        return self.remote_parties(obj, parties, suffix)


# noinspection PyAbstractClass
class _FromGuestHost(_FromGuest, _FromHost):
    def from_guest_host(self, suffix) -> typing.List:
        parties = self.roles_to_parties(["guest", "host"])
        return self.get_parties(parties, suffix)


# noinspection PyAbstractClass
class _ToGuestHost(_ToGuest, _ToHost):
    def to_guest_host(self, obj, suffix):
        parties = self.roles_to_parties(["guest", "host"])
        return self.remote_parties(obj, parties, suffix)


class A2GVariable(Variable, _FromArbiter, _ToGuest):
    def __init__(self, name):
        super().__init__(name, src=('arbiter',), dst=('guest',))


class A2HVariable(Variable, _FromArbiter, _ToHost):
    def __init__(self, name):
        super().__init__(name, src=('arbiter',), dst=('host',))


class G2AVariable(Variable, _FromGuest, _ToArbiter):
    def __init__(self, name):
        super().__init__(name, src=('guest',), dst=('arbiter',))


class G2HVariable(Variable, _FromGuest, _ToHost):
    def __init__(self, name):
        super().__init__(name, src=('guest',), dst=('host',))


class H2AVariable(Variable, _FromHost, _ToArbiter):
    def __init__(self, name):
        super().__init__(name, src=('host',), dst=('arbiter',))


class H2GVariable(Variable, _FromHost, _ToGuest):
    def __init__(self, name):
        super().__init__(name, src=('host',), dst=('guest',))


class A2GHVariable(Variable, _FromArbiter, _ToGuestHost):
    def __init__(self, name):
        super().__init__(name, src=('arbiter',), dst=('guest', 'host'))


class GH2AVariable(Variable, _FromGuestHost, _ToArbiter):
    def __init__(self, name):
        super().__init__(name, src=('guest', 'host'), dst=('arbiter',))


class G2AHVariable(Variable, _FromGuest, _ToArbiterHost):
    def __init__(self, name):
        super().__init__(name, src=('guest',), dst=('arbiter', 'host'))


class AH2GVariable(Variable, _FromArbiterHost, _ToGuest):
    def __init__(self, name):
        super().__init__(name, src=('arbiter', 'host'), dst=('guest',))


class H2AGVariable(Variable, _FromHost, _ToArbiterGuest):
    def __init__(self, name):
        super().__init__(name, src=('host',), dst=('arbiter', 'guest'))


class AG2HVariable(Variable, _FromArbiterGuest, _ToHost):
    def __init__(self, name):
        super().__init__(name, src=('arbiter', 'guest'), dst=('host',))
