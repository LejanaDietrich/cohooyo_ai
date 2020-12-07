import clustering
#testing tests
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

#actual tests
#fails
def test_something():
    print (clustering.closest_cluster('5f46c88b0b4ceb001257751e'))
    assert clustering.get_recommendations_for(0)[0] != None
