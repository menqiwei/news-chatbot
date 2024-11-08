from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityMetric:
    model = None

    #Create model
    def __init__(self):
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    #Get similarity
    def getSimilarity(self, sentence1, sentence2):
        sentences = [sentence1, sentence2]
        sentence_embeddings = self.model.encode(sentences)

        similarityScore = cosine_similarity([sentence_embeddings[0], sentence_embeddings[1]])

        return similarityScore[0][1]