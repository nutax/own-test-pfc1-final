from layers.inputs import input_layer
from layers.compute import compute_layer
from layers.outputs import output_layer

class RootLayer:
    def __init__(self, input_layer, compute_layer, output_layer):
        self.input_layer = input_layer
        self.compute_layer = compute_layer
        self.output_layer = output_layer

    def start(self):
        inputs = self.input_layer.read()
        outputs = self.compute_layer.exec(**inputs)
        self.output_layer.write(outputs)


root_layer = RootLayer(input_layer, compute_layer, output_layer)