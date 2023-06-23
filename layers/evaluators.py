class DefaultEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, problems, answers, solutions):
        results = []
        amount = len(problems)
        i = 0
        for problem, solver_output, solution in zip(problems, answers, solutions):
            valid = self.evaluate_single(problem, solver_output, solution)
            results.append(valid)
            print(f"Solution {i} / {amount} ({100*i/amount})%: {valid}")
            i += 1
        total_sum = sum(results)
        acc = total_sum / len(results)
        return acc

    def evaluate_single(self, problem, answer, solution):
        response = answer["response"]
        evaluate_prompt = self.create_evaluate_prompt(problem, response, solution)
        response = self.model.complete(evaluate_prompt)
        valid = self.validate_response(response)
        return valid
    
    def create_evaluate_prompt(self, problem, response, solution):
        prompt = f"""
        [INPUT]
        Question: '{problem}'
        Proposed solution: '{response}'
        Correct answer: '{solution}'

        [OUTPUT]
        Is the proposed solution correct? Only answer with a single word: yes/no. """
        return prompt
    
    def validate_response(self, response):
        response = response.lower()
        if "yes" in response:
            return 1
        elif "no" in response:
            return 0
        else:
            raise ValueError(f"Invalid response: {response}")