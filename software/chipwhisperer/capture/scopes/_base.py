#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
# All rights reserved.
#
# Authors: Colin O'Flynn
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

from chipwhisperer.common.utils import Util, plugin


class ScopeTemplate(plugin.Plugin):
    name = "None"

    def __init__(self):
        super(ScopeTemplate, self).__init__()
        self.connectStatus = Util.Observable(False)
        self.dataUpdated = Util.Signal()
        self.datapoints = []

    def dcmTimeout(self):
        pass

    def setAutorefreshDCM(self, enabled):
        pass

    def setCurrentScope(self, scope, update=True):
        pass

    def getStatus(self):
        return self.connectStatus.value()

    def con(self):
        # raise Warning("Scope \"" + self.getName() + "\" does not implement method " + self.__class__.__name__ + ".con()")
        self.connectStatus.setValue(True)

    def dis(self):
        self.connectStatus.setValue(False)

    def doDataUpdated(self,  l, offset=0):
        self.dataUpdated.emit(l, offset)

    def arm(self):
        pass
        #NOTE - if reimplementing this, should always check for connection first
        #if self.connectStatus.value() is False:
        #    raise Exception("Scope \"" + self.getName() + "\" is not connected. Connect it first...")
        #raise NotImplementedError("Scope \"" + self.getName() + "\" does not implement method " + self.__class__.__name__ + ".arm()")

    def capture(self, update=True, NumberPoints=None, waitingCallback=None):
        pass

    def guiActions(self, mainWindow):
        return []

    def validateSettings(self):
        # return [("warn", "Scope Module", "You can't use module \"" + self.getName() + "\"", "Specify other module", "57a3924d-3794-4ca6-9693-46a7b5243727")]
        return []