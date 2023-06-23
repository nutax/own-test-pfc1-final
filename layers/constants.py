from layers.models import ChatGPTModel, GPTModel
from layers.evaluators import DefaultEvaluator
from layers.solvers import DefaultSolver, PlanSolveSolver, SelfRefineSolver


OPENAI_API_KEY = ""

model_classes = {
            "GPT": GPTModel,
            "ChatGPT": ChatGPTModel,
        }

model_args = {
            "GPT":{
                "Ada": {
                    "openai_api_key": OPENAI_API_KEY,
                    "model_name": "text-ada-001",
                },
                "Davinci": {
                    "openai_api_key": OPENAI_API_KEY,
                    "model_name": "text-davinci-003",
                }
            },
            "ChatGPT": {
                "GPT35Turbo": {
                    "openai_api_key": OPENAI_API_KEY,
                    "model_name": "gpt-3.5-turbo",
                },
                "GPT4": {
                    "openai_api_key": OPENAI_API_KEY,
                    "model_name": "gpt-4",
                }
            }
        }

evaluator_prompting_classes = {
            "Default": DefaultEvaluator,
        }

solver_prompting_classes = {
            "Default": DefaultSolver,
            "PlanSolve": PlanSolveSolver,
            "SelfRefine": SelfRefineSolver,
        }

problems_sets_names = ["AddSub", "gsm8k", "MultiArith", "SingleEq", "SVAMP"]

problems_sets = {problem_set: f"datasets/{problem_set}.json" for problem_set in problems_sets_names}

problem_get_question = {
            "AddSub": lambda problem: problem["sQuestion"],
            "gsm8k": lambda problem: problem["question"],
            "MultiArith": lambda problem: problem["sQuestion"],
            "SingleEq": lambda problem: problem["sQuestion"],
            "SVAMP": lambda problem: problem["Question"],
}

problem_get_solution = {
            "AddSub": lambda problem: problem["lSolutions"][0],
            "gsm8k": lambda problem: problem["answer"],
            "MultiArith": lambda problem: problem["lSolutions"][0],
            "SingleEq": lambda problem: problem["lSolutions"][0],
            "SVAMP": lambda problem: problem["Answer"],
}