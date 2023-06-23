import json
class DefaultSolver:
    def __init__(self, model):
        self.model = model

    def solve(self, problems, solutions):
        answers = []
        i = 0
        amount = len(problems)
        for problem, correct_answer in zip(problems, solutions):
            prompt = self.create_question_prompt(problem)
            response = self.model.complete(prompt)
            prompt_length = len(prompt)
            response_length = len(response)
            solution = {
                "prompt": prompt,
                "response": response,
                "prompt_length": prompt_length,
                "response_length": response_length,
                "correct_answer": correct_answer,
            }
            print(f"Problem {i} / {amount} ({100*i/amount})%")
            i += 1
            pretty = json.dumps(solution, indent=4)
            print(pretty)
            answers.append(solution)
        return answers
    
    def create_question_prompt(self, problem):
        prompt = f"""
        Q: '{problem}'

        
        A: """
        return prompt


class PlanSolveSolver:
    def __init__(self, model):
        self.model = model

    def solve(self, problems, solutions):
        answers = []
        i = 0
        amount = len(problems)
        for problem, correct_answer in zip(problems, solutions):
            prompt = self.create_question_prompt(problem)
            response = self.model.complete(prompt)
            prompt_length = len(prompt)
            response_length = len(response)
            solution = {
                "prompt": prompt,
                "response": response,
                "prompt_length": prompt_length,
                "response_length": response_length,
                "correct_answer": correct_answer,
            }
            print(f"Problem {i} / {amount} ({100*i/amount})%")
            i += 1
            pretty = json.dumps(solution, indent=4)
            print(pretty)
            answers.append(solution)
        return answers
    
    def create_question_prompt(self, problem):
        prompt = f"""
        Q: '{problem}'

        
        A: Let's first understand the problem and devise a plan to solve it. Then, let's carry out the plan and solve the problem step by step."""
        return prompt


class SelfRefineSolver:
    def __init__(self, model, refinments=2):
        self.model = model
        self.refinments = refinments

    def solve(self, problems, solutions):
        answers = []
        j = 0
        amount = len(problems)
        for problem, correct_answer in zip(problems, solutions):
            prompt = self.create_question_prompt(problem)
            response = self.model.complete(prompt)
            prompt_length = len(prompt)
            response_length = len(response)

            for i in range(self.refinments):
                feedback_prompt = self.create_feedback_prompt(prompt, response)
                feedback_response = self.model.complete(feedback_prompt)
                prompt_length += len(feedback_prompt)
                response_length += len(feedback_response)

                refined_prompt = self.create_refine_prompt(prompt, response, feedback_response)
                refined_response = self.model.complete(refined_prompt)
                prompt_length += len(refined_prompt)
                response_length += len(refined_response)

                response = refined_response

            solution = {
                "prompt": prompt,
                "response": response,
                "prompt_length": prompt_length,
                "response_length": response_length,
                "correct_answer": correct_answer,
            }
            print(f"Problem {j} / {amount} ({100*i/amount})%")
            j += 1
            pretty = json.dumps(solution, indent=4)
            print(pretty)
            answers.append(solution)
        return answers
    
    def create_question_prompt(self, problem):
        prompt = f"""
        Q: '{problem}'

        
        A: """
        return prompt
    
    def create_feedback_prompt(self, prompt, response):
        feedback_prompt = f"""
        Q: '{prompt}'

        
        A: '{response}'

        
        Feedback. Point out any mistakes or suggest any improvements that need to be made. Objective criticism: """
        return feedback_prompt
    
    def create_refine_prompt(self, prompt, response, feedback_response):
        refined_prompt = f"""
        Question: '{prompt}'

        
        Tentative Answer: '{response}'

        
        Feedback: '{feedback_response}'

        
        Rewrite Tentative Answer. Try to improve the answer. Only mention the steps and the results. Final Answer: """
        return refined_prompt