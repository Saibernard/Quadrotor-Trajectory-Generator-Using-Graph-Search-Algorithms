# Quadrotor-Trajectory-Generator-Using-Graph-Search-Algorithms
This repository delves into quadrotor trajectory generation in 3D spaces. Utilizing Dijkstra’s and A* methodologies, it determines optimal paths from start to end positions, avoiding collisions. The project emphasizes environment discretization, heuristic guidance, and visualization.

## Project Overview

In this project, I've designed a trajectory generator for a quadrotor navigating a 3D environment, utilizing Dijkstra’s and A* (A-Star) graph search algorithms. The aim is to compute optimal trajectories for a quadrotor, ensuring a seamless and collision-free transition from start to target positions.

## Technical Framework and Approach

### World Representation
- **World Objects**: Represent the intricacies of the 3D environment, including boundaries and obstacles. Axis-aligned cuboid entities depict obstacles, with unique extents and colors. The World objects can be loaded efficiently from JSON files.

### Environment Discretization
- Discretized the 3D space into a grid for graph search compatibility.
- Introduced the `OccupancyMap` object, a voxel grid distinguishing open spaces and regions with obstacles.
  - **False Voxel Value**: Open space for quadrotor navigation.
  - **True Voxel Value**: Intersections with obstacles to avoid.

### Dijkstra’s Algorithm
- Implemented to determine the shortest path in the discretized environment.

### A* Algorithm
- Extended the system's capability with the A* search, using heuristics (distance to the goal). Ensured the heuristic is both admissible and consistent.

### Expanded Nodes Metrics
- Introduced a metric to measure algorithm efficiency, tracking the total count of expanded nodes.

## Development Tools and Utility Scripts

### Sandbox Script
- Integrated for debugging, it loads the World, runs the graph search, and visualizes the resulting trajectory.

### Testing Script
- Validates the robustness of the trajectory generator across various test maps, reinforcing system reliability.

## Visualization and Illustration

Custom test maps were designed and solved using both Dijkstra and A* algorithms across different grid resolutions. The results visualization showcases the relationship between map resolution and the number of nodes expanded, offering insights into each algorithm's efficiency.

---

This project served as an insightful journey into the domain of path planning for autonomous drones, melding theoretical concepts with hands-on challenges, paving the way for advanced autonomous navigation solutions.
