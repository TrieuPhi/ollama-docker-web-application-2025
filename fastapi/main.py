from fastapi import FastAPI
from app.schema import ChatRequest
from app.libs import OllamaLLM  # chính là class bạn vừa tạo lại

app = FastAPI(
    title="Ollama API",
    description="API for interacting with Ollama LLM",
    version="1.0.0"
)

# Khởi tạo LLM
llm = OllamaLLM(base_url="http://ollama-server:11434/", model="qwen2.5-coder:0.5b")

@app.post("/prompt", response_model=dict)
async def prompt(request: ChatRequest):
    try:
        result = llm.invoke(request.prompt)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
