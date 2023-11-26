from mycroft import MycroftSkill, intent_file_handler


class Valetudo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('valetudo.intent')
    def handle_valetudo(self, message):
        self.speak_dialog('valetudo')


def create_skill():
    return Valetudo()

