# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 1.1 线性方程组 (Systems of Linear Equations)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 1 Summary)

### 1. 动机与引入 (Motivation)
线性代数研究的核心对象之一是**线性方程组 (Systems of Linear Equations)**。我们可以从古代数学问题切入：

* **经典例题（鸡兔同笼）**：  
  “今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？”  
  **建立方程组**：设雉（鸡）有 $x$ 只，兔有 $y$ 只：
  $$
  \begin{cases}
  x + y = 35 \\
  2x + 4y = 94
  \end{cases}
  $$
  求解得唯一解 $x = 23, y = 12$。

* **变体问题 1（鸡鸭同笼 - 多解情况）**：  
  设鸡 $x$ 只，鸭 $y$ 只，共 35 个头，70 只脚：
  $$
  \begin{cases}
  x + y = 35 \\
  2x + 2y = 70
  \end{cases}
  $$
  化简后两式等价，存在多组解（如 $x=0, y=35$ 或 $x=1, y=34$ 等）。

* **变体问题 2（矛盾方程 - 无解情况）**：  
  若改为 35 个头，71 只脚：
  $$
  \begin{cases}
  x + y = 35 \\
  2x + 2y = 71
  \end{cases}
  $$
  由前式可得 $2x + 2y = 70$，与 71 产生矛盾，因此**无解 (No solution)**。

---

---

### 2. 定义与基本术语 (Definitions & Terminologies)

* **线性方程 (Linear Equation)**：  
  变量 $x_1, x_2, \dots, x_n$ 的线性方程是指可以写成如下形式的方程：
  $$a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b$$
  其中 $b$ 以及系数 $a_1, a_2, \dots, a_n$ 均为已知实数。  
  *注意*：变量只能以一次幂形式出现，且不能包含变量之间的乘积、三角函数、根号或指数等非线性项。

* **线性方程组 (System of Linear Equations / Linear System)**：  
  由一个或多个包含相同变量的线性方程构成的集合。含有 $m$ 个方程、$n$ 个变量的代数通用形式为：
  $$
  \begin{cases}
  a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
  a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
  \quad \vdots \\
  a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
  \end{cases}
  $$
  其中双下标 $a_{ij}$ 中，第一个下标 $i$ 表示方程的行号（第 $i$ 个方程），第二个下标 $j$ 表示变量的列号（第 $j$ 个变量）。

#### 【课件随堂练习】判断线性方程组 (Which Systems Are Linear?)
**题目**：下列方程组中，哪些是线性方程组？  
(a) 
$$
\begin{cases}
x = 1 \\
y = 3
\end{cases}
$$  
(b) 
$$
\begin{cases}
x^2 + y = 1 \\
x + y = 3
\end{cases}
$$  
(c) 
$$
\begin{cases}
x + y - z = 1 \\
\cos(x + y) = 1
\end{cases}
$$  
(d) $x + y = 0$  

**解析与解答**：  
* **(a)** 是线性方程组。每个方程中的变量都是一次的。  
* **(b)** **不是**线性方程组。因为包含 $x^2$ 非线性项。  
* **(c)** **不是**线性方程组。因为包含非线性三角函数项 $\cos(x+y)$。  
* **(d)** 是线性方程（单个方程组成的线性系统）。

---

---

### 3. 解、解集与等价性 (Solutions, Solution Sets & Equivalence)

* **解 (Solution)**：  
  使得方程组中每一个方程都成立的一组实数值列表 $(s_1, s_2, \dots, s_n)$。
* **解集 (Solution Set)**：  
  线性方程组所有可能解的集合。
* **等价线性方程组 (Equivalent Linear Systems)**：  
  如果两个线性方程组拥有**完全相同的解集**，则称它们是等价的。

#### 几何解释 ($n = 2$ 维平面)
在二维平面 $\mathbb{R}^2$ 中，每一个二元一次方程 $a_1 x_1 + a_2 x_2 = b$ 均代表一条直线。二元线性方程组的解对应直线的交点：
1. **两直线相交于一点** $\implies$ **恰有一个解 (Exactly one solution)**。
2. **两直线平行** $\implies$ **无解 (No solution)**。
3. **两直线重合** $\implies$ **有无穷多个解 (Infinitely many solutions)**。

#### 解的数量与相容性总结 (Number of Solutions & Consistency)
对于任意线性方程组，其解的情况只有以下三种可能：
1. **无解 (No solution)** $\implies$ 称为**不相容的 (Inconsistent)**。
2. **恰有一个解 (Exactly one solution)** $\implies$ 称为**相容的 (Consistent)**。
3. **无穷多个解 (Infinitely many solutions)** $\implies$ 称为**相容的 (Consistent)**。

*特别提示*：一维简单线性方程 $ax = b$ 完全符合上述三种划分：
* 若 $a = 0, b \neq 0 \implies 0 = b$，无解（Inconsistent）。
* 若 $a \neq 0 \implies x = \frac{b}{a}$，唯一解（Consistent）。
* 若 $a = 0, b = 0 \implies 0 = 0$，无穷多解（Consistent）。

---

---

### 4. 解的存在性与唯一性问题 (Existence and Uniqueness Questions)

对任意一个线性方程组，我们有两个最根本的问题：
1. **存在性 (Existence)**：该系统是否相容？（即是否至少存在一个解？）
2. **唯一性 (Uniqueness)**：如果解存在，它是否是唯一的？

解线性方程组的传统方法是**高斯消元法 (Gaussian Elimination)**，其核心思想是：利用方程变换，将原系统替换为一个**更容易求解的等价系统**。

#### 【课件随堂示例】高斯消元求解系统
求解方程组：
$$
\begin{cases}
x_1 - 2x_2 + x_3 = 0 \\
2x_2 - 8x_3 = 8 \\
5x_1 - 5x_3 = 10
\end{cases}
$$

**求解过程**：  
将第三个方程减去第一个方程的 5 倍：
$$(5x_1 - 5x_3) - 5(x_1 - 2x_2 + x_3) = 10 - 0 \implies 10x_2 - 10x_3 = 10 \implies x_2 - x_3 = 1$$
利用第二个方程 $x_2 - 4x_3 = 4$，两式相减得：
$$3x_3 = -3 \implies x_3 = -1$$
代回求得 $x_2 = 0$，$x_1 = 1$。唯一解为 $(x_1, x_2, x_3) = (1, 0, -1)$。

---

---

### 5. 矩阵表示 (Matrix Notation)

为了精简表示变量较多时的方程组，我们将系数和常数记录在矩形阵列中，称为**矩阵 (Matrix)**。

对于线性方程组：
$$
\begin{cases}
x_1 - 2x_2 + x_3 = 0 \\
2x_2 - 8x_3 = 8 \\
5x_1 - 5x_3 = 10
\end{cases}
$$

* **系数矩阵 (Coefficient Matrix)**：只包含变量前的系数。
  $$
  \begin{bmatrix}
  1 & -2 & 1 \\
  0 & 2 & -8 \\
  5 & 0 & -5
  \end{bmatrix}
  $$
* **增广矩阵 (Augmented Matrix)**：将右侧常数项作为最后一列加入矩阵中。
  $$
  \begin{bmatrix}
  1 & -2 & 1 & 0 \\
  0 & 2 & -8 & 8 \\
  5 & 0 & -5 & 10
  \end{bmatrix}
  $$

* **矩阵的大小/阶数 (Size of a Matrix)**：由行数 (Rows) $m$ 和列数 (Columns) $n$ 决定，记为 $m \times n$（读作 "$m$ by $n$"）。  
  如上述系数矩阵大小为 $3 \times 3$，增广矩阵大小为 $3 \times 4$。
* **矩阵元素 (Entries)**：第 $i$ 行第 $j$ 列的元素记为 $(i, j)$-entry。例如上述增广矩阵中，(2, 4)-entry 为 8。

---

---

### 6. 初等行变换 (Elementary Row Operations, ERO)

消元法对方程组的操作完全对应于对增广矩阵进行的**初等行变换**。初等行变换共有三种类型：

1. **倍加变换 / 替换 (Replacement)**：将某一行的倍数加到另一行上。
   $$R_i \leftarrow R_i + c R_j \quad (i \neq j)$$
2. **对换变换 (Interchange)**：交换两行的位置。
   $$R_i \leftrightarrow R_j \quad (i \neq j)$$
3. **倍乘变换 / 缩放 (Scaling)**：用非零常数乘以某一行。
   $$R_i \leftarrow c R_i \quad (c \neq 0)$$

#### 行等价 (Row Equivalence) 与重要性质
* **行等价 (Row Equivalent)**：如果矩阵 $A$ 可以通过一系列初等行变换转换为矩阵 $B$，则称 $A$ 与 $B$ 行等价。
* **重要性质**：
  1. 所有初等行变换都是**可逆的 (Reversible)**。
  2. 如果两个线性方程组的增广矩阵是行等价的，则这两个线性方程组具有相同的解集（即**方程组等价**）。
