from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key='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'
    # other params...
)

response = llm.invoke("First person to land on moon was....")
print(response.content)