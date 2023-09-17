from sentence_transformers import SentenceTransformer

embedder_all = SentenceTransformer('all-mpnet-base-v2')
embedder_qa = SentenceTransformer('multi-qa-mpnet-base-cos-v1')
embedder_msmarco = SentenceTransformer('msmarco-distilbert-base-v4')