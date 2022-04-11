from sklearn.metrics.pairwise import cosine_similarity


def coss_similarity(X, Y):
    cos_sim = cosine_similarity([X], [Y]).ravel()[0]
    return cos_sim
