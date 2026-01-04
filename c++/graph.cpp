#include <iostream>
#include <vector>
#include <string> // Required for string operations
#include <sstream> // Optional: A cleaner way to build strings
#include <queue>
#include <map>
#include <limits>
using namespace std;


struct Node { 
    string val;
    vector<Node*> adj;
    Node(string v) : val(v) {};
    };

class Graph {
public: 
    vector<Node*> nodes;
    vector<pair<pair<Node*, Node*>, int>> edges;
    string toString() {
        stringstream ss;

        for (auto n : nodes) {
            ss << n->val << ": ";
            for (auto adjNode : n->adj) {
                ss << adjNode->val << " ";
            }
            ss << endl;
        }
        return ss.str();
    }

    ~Graph() {
        for (auto n : nodes) {
            delete n;
        }
    }

    void add_edge_weight(Node* start, Node* end, int weight) {
        if (start && end) {
            start->adj.push_back(end);
            edges.push_back({{start, end}, weight});


        }
    }

    void add_node(string val) {
        Node* newNode = new Node(val);
        nodes.push_back(newNode);
    }

string shortest_path(Node* start, Node* end) {
    // Priority Queue: (distance, Node*) uses 'greater' for min-heap
    priority_queue<pair<float, Node*>, vector<pair<float, Node*>>, greater<pair<float, Node*>>> p_q;
    p_q.push({0.0f, start});

    // We use maps here because we can't easily index vectors with Node* pointers or strings
    map<Node*, float> d;
    map<Node*, Node*> p;

    // Initialize distances to infinity (you must ensure all used nodes are added to 'd' map somewhere else, 
    // but the algorithm can handle nodes not explicitly initialized if we check map membership)
    d[start] = 0.0f;
    p[start] = nullptr; // Start node has no parent

    while (!p_q.empty()) {
        // C++17 structured binding for clarity
        auto [curr_dist, curr_node] = p_q.top();
        p_q.pop();

        // Optimization: if we already processed this node with a smaller distance
        if (curr_dist > d[curr_node]) {
            continue;
        }

        if (curr_node == end) {
            break; // Found the shortest path to the end node, we can stop the main loop
        }

        // Iterate through the direct adjacency list to get neighbors and weights efficiently
        for (const auto& neighbor : curr_node->adj) {
            // Find the weight for this edge
            int weight = 0;
            for (const auto& edge : edges) {
                if (edge.first.first == curr_node && edge.first.second == neighbor) {
                    weight = edge.second;
                    break;
                }
            }
            float distance = curr_dist + weight;

            // Check if this is the first time we see the neighbor or if we found a shorter path
            // Note: d.count(neighbor) checks if the neighbor key exists in the map
            if (d.find(neighbor) == d.end() || distance < d[neighbor]) {
                d[neighbor] = distance;
                p[neighbor] = curr_node; // Mark the current node as the parent
                p_q.push({distance, neighbor});
            }
        }}

    // --- Path Reconstruction ---
    if (d.find(end) == d.end() || d[end] == numeric_limits<float>::infinity()) {
        return "No path found.";
    }

    vector<string> path_nodes;
    Node* current = end;
    while (current != nullptr) {
        path_nodes.push_back(current->val);
        current = p[current];
    }
    reverse(path_nodes.begin(), path_nodes.end());

    // Format the path into a string (e.g., "A -> B -> C (Total Distance: 15)")
    stringstream ss;
    for (size_t i = 0; i < path_nodes.size(); ++i) {
        ss << path_nodes[i];
        if (i < path_nodes.size() - 1) {
            ss << " -> ";
        }
    }
    ss << " (Total Distance: " << d[end] << ")";
    
    return ss.str();
}
                };


int main() {

    return 0;
}
