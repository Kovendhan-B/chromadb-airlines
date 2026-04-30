from ingest import ingest_data
from query import search
from llm import answer_question

# ingest_data()


# Input validation and reprompting
while True:
    query = input("Enter your question (or type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("Goodbye!")
        break
    if not query:
        print("Please enter a non-empty question.")
        continue

    results = search(query)
    docs = [doc for doc, score in results]
    answer = answer_question(query, docs)

    print("\n--- Retrieved Documents ---")
    for doc, score in results:
        print(f"\nScore: {score:.4f}")
        print(doc)

    print("\n--- LLM Answer ---")
    print(answer)