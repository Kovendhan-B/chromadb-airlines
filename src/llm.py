
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv(Path(__file__).parent.parent / ".env")

model_name = os.getenv("MODEL_NAME", "google/flan-t5-base")
tokenizer = AutoTokenizer.from_pretrained(model_name)
_hf_logger = logging.getLogger("transformers.modeling_utils")
_tie_filter = type(
    "_TieFilter", (logging.Filter,),
    {"filter": lambda self, r: "tie_word_embeddings" not in r.getMessage()}
)()
_hf_logger.addFilter(_tie_filter)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
_hf_logger.removeFilter(_tie_filter)

def answer_question(query, docs, max_length=200):
	"""
	Generate an answer to a query using retrieved documents as context.
	Args:
		query (str): The user's question.
		docs (list of str): Retrieved documents/passages.
		max_length (int): Max tokens for the generated answer.
	Returns:
		str: The generated answer.
	"""
	
	docs = docs[:3]
	context = "\n".join(docs)
	prompt = (
    f"Context:\n{context}\n\n"
    f"Question: {query}\n"
    "Based on the context, answer the question as best as you can. If you truly cannot answer, say 'I don't know.''\nAnswer:")
	inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
	outputs = model.generate(**inputs, max_length=max_length)
	response = tokenizer.decode(outputs[0], skip_special_tokens=True)
	return response

# Example usage
if __name__ == "__main__":
	docs = [
		"Paris is the capital of France.",
		"France is a country in Europe."
	]
	query = "Where is France?"
	print(answer_question(query, docs))