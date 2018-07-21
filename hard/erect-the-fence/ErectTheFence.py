class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """

        allTrees = []
        fenceTrees = []
        start_p = Point(points[0].x, points[0].y)

        for i in range(1, len(points)):
            p = Point(points[i].x, points[i].y)
            if (p.x < start_p.x) or (p.x == start_p.x and p.y < start_p.y):
                allTrees.append(start_p)
                start_p = p
            else:
                allTrees.append(p)

        # add the starting point to fence
        fenceTrees.append(start_p)

        # keep going until we come back to starting point
        curr_p = start_p    # current point
        next_p = 0  # next point

        while next_p != start_p:
            if not allTrees:
                next_p = start_p
            else:
                tree = 0
                next_p = allTrees[0] # get a point
                v_1 = self.rotate(self.vectorize(next_p, curr_p)) # rotated vector 1

                waitlist = [] # vectors pointing at the same direction as v_1

                for i in range(1, len(allTrees)):
                    v_2 = self.vectorize(allTrees[i], curr_p)
                    dot_product = self.dot(v_1, v_2)

                    if dot_product > 0:
                        # update vector 1
                        tree = i
                        next_p = allTrees[i]
                        v_1 = self.rotate(self.vectorize(next_p, curr_p))
                        del waitlist[:] # empty waitlist

                    elif dot_product == 0:
                        if self.is_bigger(v_1, v_2):
                            waitlist.append(i)
                        else:
                            waitlist.append(tree)

                            # update vector 1
                            tree = i
                            next_p = allTrees[i]
                            v_1 = self.rotate(v_2)

                # compare to the start point
                v_0 = self.vectorize(start_p, curr_p)
                dot_product = self.dot(v_1, v_0)
                if  dot_product <= 0:
                    waitlist.append(tree)
                    newTrees = sorted(waitlist, key=int, reverse=True)
                    for t in newTrees:
                        fenceTrees.append(allTrees[t])
                        del allTrees[t]

                    if dot_product == 0 and self.is_bigger(v_0, v_1):
                        next_p = start_p
                else:
                    next_p = start_p
                curr_p = next_p

        return fenceTrees

    def is_bigger(self, (v1_x, v1_y), (v2_x, v2_y)):
        mag_1 = v1_x * v1_x + v1_y * v1_y
        mag_2 = v2_x * v2_x + v2_y * v2_y
        if mag_1 > mag_2:
            return True
        return False

    def dot(self, (v1_x, v1_y), (v2_x, v2_y)):
        return v1_x * v2_x + v1_y * v2_y

    def vectorize(self, p1, p2):
        return (p1.x - p2.x, p1.y - p2.y)

    def rotate(self, (x, y)):
        return (-y, x)