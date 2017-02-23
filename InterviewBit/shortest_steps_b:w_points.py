class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        dis = 0
        for i in xrange(1,len(X)):
            if abs(X[i] - X[i-1]) < abs(Y[i] - Y[i-1]):
                dis += abs(Y[i] - Y[i-1])
            else:
                dis += abs(X[i] - X[i-1])

        return dis