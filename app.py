import os
from src.vectorstore import FaissVectorStore
from src.data_loader import load_all_documents

def main():
    # 1. Initialize the store pointing to your persist directory
    persist_dir = "faiss_store"
    store = FaissVectorStore(persist_dir=persist_dir)
    
    faiss_index_path = os.path.join(persist_dir, "faiss.index")
    
    # 2. Check if the database has already been built before
    if os.path.exists(faiss_index_path):
        print("[INFO] Vector store found on disk. Loading...")
        store.load()
    else:
        print("[INFO] No vector store found. Building a new one...")
        # Load your documents from the data folder
        docs = load_all_documents("data")
        
        # Build the index and save it to disk automatically
        store.build_from_documents(docs)

    # 3. Test a query to see if it works!
    print("\n--- Testing Query ---")
    results = store.query("What is SQL?", top_k=2)
    print(results)

if __name__ == "__main__":
    main()