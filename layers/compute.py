class ComputeLayer:
    def exec(self, evaluator, solver, problems, solutions, execution_id):
        print("Execution id:", execution_id)
        
        print("Solving...")
        answers = solver.solve(problems, solutions)
        
        print("Evaluating...")
        score = evaluator.evaluate(problems, answers, solutions)

        outputs = {
            "execution_id": execution_id,
            "score": score,
            "answers": answers,
        }

        return outputs

compute_layer = ComputeLayer()