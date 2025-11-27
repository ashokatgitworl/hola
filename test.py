from paths import APP_CONFIG_FPATH, PROMPT_CONFIG_FPATH, OUTPUTS_DIR, VECTOR_DB_DIR
from chromadb import PersistentClient
import os

# D ="/workspaces/askME/outputs/vector_db"

if __name__ == "__main__":
    # print(VECTOR_DB_DIR)
    # print(D)
    # client = PersistentClient(path=D)
    # for col in client.list_collections():
    #     print("Collection:", col.name)


    # D = "/workspaces/askME/outputs/vector_db"
    D=VECTOR_DB_DIR

print("Vector database directory:", VECTOR_DB_DIR)

print("Path exists:", os.path.exists(D))
print("Directory contents:", os.listdir(D))

client = PersistentClient(path=D)
cols = client.list_collections()

print("Collections found:", len(cols))
for c in cols:
    print(" ->", c.name)
