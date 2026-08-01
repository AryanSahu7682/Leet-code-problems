class Solution {
    public int[][] merge(int[][] intervals) {
         Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> result = new ArrayList<>();

        // Step 2: Add the first interval
        result.add(intervals[0]);

        // Step 3: Traverse the remaining intervals
        for (int i = 1; i < intervals.length; i++) {

            // Last merged interval
            int[] last = result.get(result.size() - 1);

            // Check for overlap
            if (intervals[i][0] <= last[1]) {

                // Merge intervals
                last[1] = Math.max(last[1], intervals[i][1]);

            } else {

                // No overlap, add new interval
                result.add(intervals[i]);
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}