import clustering
#testing tests
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

#actual tests
#tests if the self-written function works as well as the copied one for all users
def test_recs_for_one():
    print (clustering.closest_cluster('5f46c88b0b4ceb001257751e'))
    assert clustering.get_recommendations_for(0)[0] != None
    assert clustering.get_recommendations_for(0)[0] == clustering.get_recommendations[0][0]
