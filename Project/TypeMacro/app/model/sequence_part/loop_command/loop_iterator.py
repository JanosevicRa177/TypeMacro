class LoopIterator:
    is_parameter = False

    def __init__(self, model):
        if model.repetitions:
            self.is_parameter = model.repetitions
        elif model.loop_parameter:
            self.is_parameter = True
            self.value = model.loop_parameter.name
