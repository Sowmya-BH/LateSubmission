# # src/crewai_vision_tool/models.py
# from pydantic import BaseModel
#
# class RiskRecommendation(BaseModel):
#     recommendation: str  # Accept / Reject / Modify
#     justification: str

from pydantic import BaseModel, ValidationError

class RiskOutput(BaseModel):
    recommendation: str
    justification: str

def guardrail_validate(output: dict) -> dict:
    try:
        validated = RiskOutput(**output)
        return validated
    except ValidationError as e:
        raise ValueError(f"Validation failed: {e}")

# response = agent.call(input_text, output_pydantic=RiskOutput, guardrail=guardrail_validate)
