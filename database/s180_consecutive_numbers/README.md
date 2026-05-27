# 180. Consecutive Numbers

Leet Code reference: https://leetcode.com/problems/consecutive-numbers/description/

## 📌 Description

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

### 📌 Example 1:

**Input:**

Logs table:

| id | num |
|----|-----|
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |

**Output:**

| ConsecutiveNums |
|-----------------|
| 1               |

## 💡Window function

Step 1: Apply LAG() to get previous values.

| id | num | prev1    | prev2    |
|----|-----|----------|----------|
| 1  | 1   | NULL     | NULL     |
| 2  | 1   | 1 (id 1) | NULL     |
| 3  | 1   | 1 (id 2) | 1 (id 1) | 
| 4  | 2   | 1 (id 3) | 1 (id 2) |
| 5  | 1   | 2 (id 4) | 1 (id 3) |
| 6  | 2   | 1 (id 5) | 2 (id 4) |
| 7  | 2   | 2 (id 6) | 1 (id 5) |

Step 2: Filter rows where num = prev1 = prev2

| id | num | prev1    | prev2    |
|----|-----|----------|----------|
| 3  | 1   | 1 (id 2) | 1 (id 1) | 