import typing
from sklearn.metrics.pairwise import cosine_similarity


def coss_similarity(X: typing.List[float], Y: typing.List[float]):
    cos_sim = cosine_similarity([X], [Y]).ravel()[0]
    return cos_sim
