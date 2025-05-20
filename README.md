# 🧠 Dynamic Programming (DP) Notes

Learning DP from [Aditya Verma's YouTube Series](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)

---

## ✅ What is Dynamic Programming?

**Dynamic Programming (DP)** is just **optimized recursion**.  
It is used when a problem has:

- **Overlapping subproblems**
- **Optimal substructure**

> DP = Recursion + Memory (Memoization or Tabulation)

---

## 🔍 How to Identify DP Problems?

Look for these two signs:

1. **Choices to Make**  
   Problems where you have to decide between options (e.g., pick or skip, include or exclude).

2. **Optimization Goals**  
   Questions asking for:
   - `min` / `max`
   - `count` (number of ways)
   - `true/false` (can/can’t achieve something)

> If the problem asks to **choose** and **optimize**, it's probably a DP problem.

---

## 🧩 Steps to Solve a DP Problem

1. **Write the Recursive Solution**  
   - Start with brute force recursion.
   - Break the problem into smaller subproblems.

2. **Check for Overlapping Subproblems**  
   - If the recursion calls itself **2 or more times**, and recomputes the same values → potential for DP.

3. **Apply Memoization (Top-Down)**  
   - Store results using an array or hash map.
   - Avoid recomputing the same subproblems.

4. **Convert to Tabulation (Bottom-Up)**  
   - Use loops instead of recursion.
   - Fill a `dp[]` table iteratively.

 
