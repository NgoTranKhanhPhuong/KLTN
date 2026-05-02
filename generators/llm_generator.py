import json

class LLMGenerator:

    def __init__(self, client=None):
        self.client = client

    def generate(self, base):

        # mock nếu chưa có LLM
        if not self.client:
            return [
                {
                    "id": "LLM_001",
                    "name": "Edge null case",
                    "data": base,
                    "expected": {"type": "success"}
                },
                {
                    "id": "LLM_002",
                    "name": "Invalid type case",
                    "data": base,
                    "expected": {
  "status_code": 400,
  "category": "validation_error"
}
                }
            ]

        prompt = f"""
Generate test cases using ISTQB:
- EP
- BVA
- Negative testing
- Dependency testing
- Edge cases

Return JSON only.
Request:
{json.dumps(base)}
"""

        res = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return json.loads(res.choices[0].message.content)