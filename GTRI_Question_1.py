import numpy as np
import matplotlib.pyplot as plt
import csv

class RRT:
    def __init__(self, start, goal, obstacles, step_size=1, max_iter=1000, goal_sample_rate=0.1):
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.step_size = step_size
        self.max_iter = max_iter
        self.goal_sample_rate = goal_sample_rate
        self.tree = {}

    def generate_path(self):
        self.tree[self.start] = None
        for _ in range(self.max_iter):
            if np.random.uniform() < self.goal_sample_rate:
                rnd_point = self.goal
            else:
                rnd_point = (np.random.uniform(0, 100), np.random.uniform(0, 100))
            nearest_point = self.nearest_point(rnd_point)
            new_point = self.steer(nearest_point, rnd_point)
            if not self.collision(new_point):
                self.tree[new_point] = nearest_point
                if self.distance(new_point, self.goal) <= self.step_size:
                    return self.construct_path(new_point)
        return None

    def nearest_point(self, point):
        distances = [self.distance(point, p) for p in self.tree]
        nearest_index = np.argmin(distances)
        return list(self.tree.keys())[nearest_index]

    def steer(self, from_point, to_point):
        from_point = np.array(from_point)
        to_point = np.array(to_point)
        vector = to_point - from_point
        vector /= np.linalg.norm(vector)
        new_point = from_point + vector * self.step_size
        return tuple(new_point)

    def collision(self, point):
        for obstacle in self.obstacles:
            if self.distance(point, obstacle) <= 5:
                return True
        return False

    def distance(self, point1, point2):
        return np.linalg.norm(np.array(point1) - np.array(point2))

    def construct_path(self, end_point):
        path = [end_point]
        while path[-1] != self.start:
            path.append(self.tree[path[-1]])
        return path[::-1]

def read_obstacles_from_csv(file_path):
    obstacles = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            obstacles.append((float(row[0]), float(row[1])))
    return obstacles

def visualize(obstacles, path):
    plt.figure(figsize=(8, 8))
    for obstacle in obstacles:
        circle = plt.Circle(obstacle, 5, color='b')
        plt.gca().add_patch(circle)
    if path:
        path = np.array(path)
        plt.plot(path[:, 0], path[:, 1], '-o', color='r')
    plt.xlim(-10, 110)
    plt.ylim(-10, 110)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def main():
    start = (0, 0)
    goal = (100, 100)
    obstacles = read_obstacles_from_csv('obstacles.csv')

    rrt = RRT(start, goal, obstacles)
    path = rrt.generate_path()

    if path:
        print("Path found!")
        print("Path:", path)
        visualize(obstacles, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
