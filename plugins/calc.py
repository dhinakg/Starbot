#    Copyright 2017 Starbot Discord Project
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from __future__ import division

import math
import operator

from api import command, message, plugin

def onInit(plugin_in):
    #create the basics of our plugin
    calc_command = command.Command(plugin_in, 'calc', shortdesc='Calculate given input')
    return plugin.Plugin(plugin_in, 'calc', [calc_command])

async def onCommand(message_in):
    """Do some math."""
    formula = message_in.body
    formula = formula.replace('x', '*')
    formula = formula.replace(' ', '')

    if formula == None:
        msg = 'Usage: `{}calc [formula]`'.format('!')
        return message.Message(body=msg)

    valid_chars = set('1234567890+-/*')
    for char in formula:
        if char not in valid_chars:
            return message.Message(body="Invalid symbol: {}".format(char))

    try:
        answer = eval(formula, {'__builtins__':{}, '__locals__':{}, '__globals__':{}})
    except Exception as e:
        return message.Message(body="Not a valid math problem.")

    if type(answer) != int and type(answer) != float:
        return message.Message(body="Calculator did not return a valid output.")

    msg = '`{}` = `{}`'.format(formula, round(answer, 3))
    # Say message
    return message.Message(body=msg)
