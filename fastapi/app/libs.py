# app/libs.py

from langchain_ollama import OllamaLLM as LangchainOllama
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain_core.output_parsers import StrOutputParser

# Thiết lập cache
set_llm_cache(InMemoryCache())

# Wrapper class để gọi Ollama đơn giản
class OllamaLLM:
    def __init__(self, base_url: str, model: str):
        self.llm = LangchainOllama(
            base_url=base_url,
            model=model
        )
        self.chain = self.llm | StrOutputParser()

    def invoke(self, prompt: str) -> str:
        return self.chain.invoke(prompt)
