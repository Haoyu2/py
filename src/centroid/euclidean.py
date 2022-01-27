from src.centroid.centroid import Centroid


class EuclideanCentroid(Centroid):
    def __init__(self, centroid):
        super(EuclideanCentroid, self).__init__(centroid)

    def derivative(self, point):
        pass
    def call(self, point):
        pass