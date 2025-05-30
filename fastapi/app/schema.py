from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(default="xin chào!")
