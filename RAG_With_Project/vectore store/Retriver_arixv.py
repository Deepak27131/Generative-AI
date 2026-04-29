from langchain_community.retrievers import ArxivRetriever

# create the retrever 
retriever = ArxivRetriever(
    load_max_docs = 5, # number of paper to retrive
    load_all_available_meta=True
)

# query text 
docs  = retriever.invoke("Explain the 2 most LLM in reseacher papers?")

# print 
# for i , doc in enumerate(doc):
#     print(f'\nResult {i+1}')
#     print("------------")
#     print("Title: ",doc.metadata.get("Title"))
#     print("Authors: ",doc.metadata.get("Authors"))
#     print("Summary: ",doc.page_content)
    
for i, doc in enumerate(docs):
    print(f"\nResult {i+1}")
    print("------------")
    print("Title:", doc.metadata.get("Title"))
    print("Authors:", doc.metadata.get("Authors"))
    
    # ✅ FIX
    print("Summary:", doc.page_content[:500])