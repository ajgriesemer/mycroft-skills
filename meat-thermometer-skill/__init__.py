
# The MIT License (MIT)
#
# Copyright (c) <year> <copyright holder>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG


class MeatThermometerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MeatThermometerSkill, self).__init__(name="MeatThermometerSkill")

    @intent_handler(IntentBuilder("").require("Temperature").require("Cook").require("Meat").optionally("Modifier"))
    def handle_count_intent(self, message):
        meat = message.data["Meat"]
        if message.data.get("Modifier") is None:
            modifier = ""
        else:
            modifier = message.data.get("Modifier")

        if (meat == "turkey") or \
                (meat == "chicken") or \
                (meat == "poultry"):
            temperature = 165
            self.speak_dialog("cooking.temperature.is",
                              data={"temperature": temperature, "meat": meat, "modifier": modifier})
            return

        elif (meat == "beef") or \
                (meat == "steak"):
            if modifier is "":
                temperature = 145
            elif modifier == "ground":
                temperature = 160
            elif modifier == "rare":
                temperature = 135
            elif modifier == "medium rare":
                temperature = 140
            elif modifier == "medium":
                temperature = 155
            elif modifier == "well done":
                temperature = 165
            self.speak_dialog("cooking.temperature.with.rest",
                              data={"temperature": temperature, "meat": meat, "modifier": modifier})
            return

        elif (meat == "fish") or \
                (meat == "tuna") or \
                (meat == "salmon") or \
                (meat == "shell fish") or \
                (meat == "clams") or \
                (meat == "scallop") or \
                (meat == "crab"):
            temperature = 145
            self.speak_dialog("cooking.temperature.is",
                              data={"temperature": temperature, "meat": meat, "modifier": ""})
            return

        else:
            self.speak_dialog("do.not.know.cooking.temperature", data={"meat": meat})
            return

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MeatThermometerSkill()
