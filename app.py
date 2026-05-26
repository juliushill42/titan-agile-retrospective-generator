from fastapi import FastAPI
from agent import Agent43
app = FastAPI(title="Agile-Retrospective-Generator")
agent = Agent43()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
