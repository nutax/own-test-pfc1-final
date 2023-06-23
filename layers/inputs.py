from layers import constants
import json
from datetime import datetime

class InputLayer:

    def read(self):
        evaluator_model_name, evaluator_model_class = self.request_selection("LLM for the EVALUATOR", constants.model_classes)
        evaluator_config_name, evaluator_model_args = self.request_selection("LLM CONFIG for the EVALUATOR", constants.model_args[evaluator_model_name])
        evaluator_model = evaluator_model_class(**evaluator_model_args)

        evaluator_prompting_name, evaluator_prompting_class = self.request_selection("prompting method for the EVALUATOR", constants.evaluator_prompting_classes)
        evaluator_prompting = evaluator_prompting_class(model=evaluator_model)

        solver_model_name, solver_model_class = self.request_selection("LLM for the SOLVER", constants.model_classes)
        solver_config_name, solver_model_args = self.request_selection("LLM CONFIG for the SOLVER", constants.model_args[solver_model_name])
        solver_model = solver_model_class(**solver_model_args)

        solver_prompting_name, solver_prompting_class = self.request_selection("prompting method for SOLVER", constants.solver_prompting_classes)
        solver_prompting = solver_prompting_class(model=solver_model)

        problem_set_name, problems_set = self.request_selection("PROBLEM SET", constants.problems_sets)
        problems, solutions = self.split_problems_solutions(problem_set_name, problems_set)

        from_problem, upto_problem = self.request_problem_range(problems)

        timestamp_integer = int(datetime.now().timestamp())
        execution_id = f"{evaluator_model_name}_{evaluator_config_name}_{evaluator_prompting_name}_{solver_model_name}_{solver_config_name}_{solver_prompting_name}_{problem_set_name}_{timestamp_integer}"

        inputs = {
            "evaluator": evaluator_prompting,
            "solver": solver_prompting,
            "problems": problems[from_problem:upto_problem],
            "solutions": solutions[from_problem:upto_problem],
            "execution_id": execution_id,
        }
        return inputs
    
    def request_selection(self, types, options):
        print(f"Select one {types}:")
        for i, option in enumerate(options):
            print(f"{i}: {option}")
        selection_i = int(input("Your selection: "))
        print("-----------------------------------")
        if selection_i < 0 or selection_i >= len(options):
            raise Exception("Invalid selection")
        selection_key = list(options.keys())[selection_i]
        selection_value = options[selection_key]
        return selection_key, selection_value
    
    def read_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    def split_problems_solutions(self, problem_set_name, problems_set):
        get_question = constants.problem_get_question[problem_set_name]
        get_solution = constants.problem_get_solution[problem_set_name]
        dataset = self.read_json_file(problems_set)
        problems = []
        solutions = []
        for data in dataset:
            problems.append(get_question(data))
            solutions.append(get_solution(data))
        return problems, solutions
    
    def request_problem_range(self, problems):
        from_problem = int(input("From problem: "))
        upto_problem = int(input("Up to problem: "))
        if from_problem < 0 or upto_problem < 0 or upto_problem < from_problem:
            raise Exception("Invalid problem range")
        upto_problem = len(problems) if len(problems) <= upto_problem else upto_problem
        print("-----------------------------------")
        return from_problem, upto_problem

input_layer = InputLayer()