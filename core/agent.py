from core.generator import generate_answer
from core.faithfulness import compute_faithfulness
from core.config import FAITHFULNESS_THRESHOLD
from core.planner import plan_query
from core.critic import critique_answer

def agentic_pipeline(query, documents):

    optimized_query = plan_query(query)

    answer = generate_answer(optimized_query, documents)
    score = compute_faithfulness(answer, documents)

    critique = critique_answer(answer)

    if score < FAITHFULNESS_THRESHOLD or "NO" in critique:
        answer = generate_answer(
            optimized_query + " Answer strictly using context.",
            documents
        )
        score = compute_faithfulness(answer, documents)

    return answer, score