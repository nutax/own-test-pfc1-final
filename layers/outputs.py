import json
class OutputLayer:
    def write(self, outputs):
        execution_id = outputs["execution_id"]
        # Save the outputs to a file
        with open(f"results/{execution_id}.json", 'w') as file:
            json.dump(outputs, file, indent=4)
        print("Wrote results to file. Terminating.")

output_layer = OutputLayer()