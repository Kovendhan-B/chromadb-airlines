
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
from transformers import AutoConfig
config = AutoConfig.from_pretrained(model_name)
config.tie_word_embeddings = False
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

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
	context = "\n".join(docs)
	prompt = (
    f"Context:\n{context}\n\n"
    f"Question: {query}\n"
    "Answer using only the context above. If the answer is not in the context, say 'I don't know.'\nAnswer:")
	inputs = tokenizer(prompt, return_tensors="pt")
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