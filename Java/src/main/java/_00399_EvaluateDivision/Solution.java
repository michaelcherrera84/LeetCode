package _00399_EvaluateDivision;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Solution {

    /**
     * You are given an array of variable pairs {@code equations} and an array of
     * real numbers {@code values}, where {@code equations[i] = [Aᵢ, Bᵢ]} and
     * {@code values[i]} represent the equation {@code Aᵢ / Bᵢ = values[i]}. Each
     * {@code Aᵢ} or {@code Bᵢ} is a string that represents a single variable.
     * <p>
     * You are also given some {@code queries}, where {@code queries[j] = [Cj, Dj]}
     * represents the {@code jth} query where you must find the answer for
     * {@code Cⱼ / Dⱼ = ?}.
     * <p>
     * Return <i>the answers to all queries.</i> If a single answer cannot be
     * determined, return {@code -1.0}.
     * <p>
     * <b>Note:</b> The input is always valid. You may assume that evaluating the
     * queries will not result in division by zero and that there is no
     * contradiction.
     * <p>
     * <b>Note:</b> The variables that do not occur in the list of equations are
     * undefined, so the answer cannot be determined for them.
     * 
     * @param equations the array of variable pairs
     * @param values    values that represent the division of the variable pairs
     * @param queries   list of new division operations to perform
     * @return the result of the new division operations
     */
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        double[] res = new double[queries.size()];

        // Build a graph of the given calculations.
        for (int i = 0; i < equations.size(); i++) {
            String var1 = equations.get(i).get(0);
            String var2 = equations.get(i).get(1);
            double val = values[i];

            var var1Neighbors = graph.getOrDefault(var1, new HashMap<>());
            var1Neighbors.put(var2, val);

            var var2Neighbors = graph.getOrDefault(var2, new HashMap<>());
            var2Neighbors.put(var1, 1 / val);

            graph.put(var1, var1Neighbors);
            graph.put(var2, var2Neighbors);
        }

        // Attempt to perform each calculation in the list of queries.
        for (int i = 0; i < queries.size(); i++) {
            var query = queries.get(i);
            res[i] = calc(query.get(0), query.get(1), new HashSet<>(), graph);
        }

        return res;
    }

    /**
     * Solve a division equation with the given variables.
     * 
     * @param var1    the dividend variable
     * @param var2    the divisor variable
     * @param visited a set of "visited" variables
     * @param graph   a graph of known division calculations
     * @return the result of the division or {@code -1.0} if we do not have the
     *         information to perform this division
     */
    private double calc(String var1, String var2, Set<String> visited, Map<String, Map<String, Double>> graph) {
        // If either variable doesn't exist in the graph of known calculations,
        // the variable(s) is/are undefined, and the calculation cannot be
        // performed.
        if (!graph.containsKey(var1) || !graph.containsKey(var2))
            return -1.0;

        var neighbors = graph.get(var1);

        // If the divisor is a neighbor of the dividend, then we have the
        // necessary information to perform the division calculation.
        if (neighbors.containsKey(var2))
            return graph.get(var1).get(var2);

        // Mark this variable as visited.
        visited.add(var1);

        // For each of the neighbors of the dividend, recursively search for a
        // path to the divisor.
        for (String variable : neighbors.keySet()) {
            if (!visited.contains(variable)) {
                double val = calc(variable, var2, visited, graph);
                // If a path is found to the divisor, return the product of values
                // along the path.
                if (val != -1)
                    return neighbors.get(variable) * val;
            }
        }

        // If a path is not found from the dividend to the divisor, then we do
        // not have enough information to perform the division.
        return -1.0;
    }
}
