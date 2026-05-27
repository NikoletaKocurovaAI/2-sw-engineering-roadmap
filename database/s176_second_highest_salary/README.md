# 176. Second Highest Salary

Leet Code reference: https://leetcode.com/problems/second-highest-salary/description/

## 📌 Description 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest 
salary, return null (return None in Pandas).

### 📌 Example 1:

**Input:**

Employee table:

| id | salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

**Output:**

| SecondHighestSalary |
|--------------------|
| 200                |

### 📌 Example 2:

**Input:**

Employee table:

| id | salary |
|----|--------|
| 1  | 100    |

**Output:**

| SecondHighestSalary |
|---------------------|
| null                |

## 💡Window function

Employee table:

| id | salary |
|----|--------|
| 1  | 300    |
| 2  | 200    |
| 3  | 100    |
| 4  | 800    |
| 5  | 200    |
| 6  | 100    |

```sql
SELECT 
    id, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
FROM Employee;
```

Step 1 ORDER BY salary DESC

| id | salary |
|----|--------|
| 4  | 800    |
| 1  | 300    |
| 2  | 200    |
| 5  | 200    |
| 3  | 100    |
| 6  | 100    |

Step 2: Assign ranks with DENSE_RANK()
- Highest salary 800 gets rank 1
- Next salary 300 gets rank 2
- Both 200 salaries tie for rank 3 (same rank, no gaps)
- Both 100 salaries tie for rank 4

| id | salary | rank |
|----|--------|------|
| 4  | 800    | 1    |
| 1  | 300    | 2    |
| 2  | 200    | 3    |
| 5  | 200    | 3    |
| 3  | 100    | 4    |
| 6  | 100    | 4    |
