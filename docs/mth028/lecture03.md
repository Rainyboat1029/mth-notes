# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 1.3 & 1.4 向量方程与矩阵方程 $Ax = b$ (Vector Equations and Matrix Equation $Ax = b$)  
**对应课件**：Lecture 3 - Sections 1.3 and 1.4  
**适用目的**：自学、预习与复习（纯课堂知识点与随堂例题精讲）  

---

## 核心知识点分布 (Key Topics Overview)
1. **Section 1.3 向量方程 (Vector Equations)**
   * $\mathbb{R}^n$ 中的列向量、向量相等、零向量与代数运算
   * 向量运算的几何解释（平面向量与平行四边形法则）
   * 线性组合 (Linear Combinations) 与线性方程组的向量形式
   * 张成空间 (Span) 的定义、判定与几何意义 ($\mathbb{R}^2$ 与 $\mathbb{R}^3$ 中的直线与平面)
2. **Section 1.4 矩阵方程 $Ax = b$ (The Matrix Equation $Ax = b$)**
   * 矩阵与向量乘积 $A\mathbf{x}$ 的定义（列组合定义法与行内积计算法则）
   * 矩阵乘法的线性性质与单位矩阵 $I_n$
   * 线性方程组的三种等价表达形式
   * 解的存在性定理（Theorem 4：四个等价条件）与主元条件剖析

---

## 第一部分：Section 1.3 向量方程 (Vector Equations)

### 1.1 列向量与向量代数 (Column Vectors & Vector Algebra)
* **列向量 (Column Vector / Vector)**：
  仅有一列的矩阵称为**列向量**（简称为**向量**）。所有具有 $n$ 个实数分量的列向量构成的集合记为 $\mathbb{R}^n$。
  $$\mathbf{u} = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix} \in \mathbb{R}^n$$
  * *示例*：$\begin{bmatrix} 4 \\ 3 \end{bmatrix} \in \mathbb{R}^2$，$\begin{bmatrix} 1 \\ -2 \\ 5 \end{bmatrix} \in \mathbb{R}^3$。

* **向量相等 (Vector Equality)**：
  两个向量 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ 相等，当且仅当它们的维数相同，且对应位置的分量完全相等，即 $u_i = v_i$ ($i = 1, 2, \dots, n$)。
  * *注意*：$\begin{bmatrix} 1 \\ 2 \end{bmatrix} \neq \begin{bmatrix} 2 \\ 1 \end{bmatrix}$，维数不同的向量无法比较相等。

* **零向量 (Zero Vector)**：
  所有分量均为零的向量称为**零向量**，记作 $\mathbf{0}$。在 $\mathbb{R}^n$ 中，$\mathbf{0} = \begin{bmatrix} 0 \\ \vdots \\ 0 \end{bmatrix}$。

* **代数运算 (Algebraic Operations in $\mathbb{R}^n$)**：
  设 $\mathbf{u} = \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix}$，$\mathbf{v} = \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$，$c, d \in \mathbb{R}$：
  1. **向量加法 (Vector Addition)**：对应分量相加。
     $$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}$$
  2. **标量乘法 / 数乘 (Scalar Multiplication)**：常数 $c$ 乘以每个分量。
     $$c\mathbf{u} = \begin{bmatrix} cu_1 \\ cu_2 \\ \vdots \\ cu_n \end{bmatrix}$$

* **$\mathbb{R}^n$ 的代数性质 (Algebraic Properties of $\mathbb{R}^n$)**：
  对任意 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n$ 及标量 $c, d \in \mathbb{R}$，满足以下 8 条算术规则：
  1. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$（加法交换律）
  2. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$（加法结合律）
  3. $\mathbf{u} + \mathbf{0} = \mathbf{0} + \mathbf{u} = \mathbf{u}$（零向量单位元）
  4. $\mathbf{u} + (-\mathbf{u}) = -\mathbf{u} + \mathbf{u} = \mathbf{0}$（加法逆元，其中 $-\mathbf{u} = (-1)\mathbf{u}$）
  5. $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$（标量对向量加法的分配律）
  6. $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$（标量加法的分配律）
  7. $c(d\mathbf{u}) = (cd)\mathbf{u}$（标量乘法结合律）
  8. $1\mathbf{u} = \mathbf{u}$（乘法单位元）

---

### 1.2 几何解释 (Geometric Interpretation)
* **平面点与有向线段**：
  在 $\mathbb{R}^2$ 中，向量 $\begin{bmatrix} a \\ b \end{bmatrix}$ 既可以看作笛卡尔坐标系中的点 $(a, b)$，也可以看作从原点 $(0,0)$ 指向点 $(a, b)$ 的**有向线段 (Directed Line Segment)**。
* **平行四边形法则 (Parallelogram Rule for Addition)**：
  如果 $\mathbf{u}$ 和 $\mathbf{v}$ 是 $\mathbb{R}^2$ 中的两个非零向量，则 $\mathbf{u} + \mathbf{v}$ 对应于以原点、$\mathbf{u}$、$\mathbf{v}$ 为顶点的平行四边形的第四个顶点（即对角线顶点）。

---

### 1.3 线性组合 (Linear Combinations)
* **概念定义 (Definition)**：
  给定 $\mathbb{R}^n$ 中的向量 $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p$ 以及标量（权重, Weights）$c_1, c_2, \dots, c_p$，由下式定义的向量 $\mathbf{y}$：
  $$\mathbf{y} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_p\mathbf{v}_p$$
  称为向量 $\mathbf{v}_1, \dots, \mathbf{v}_p$ 的**线性组合 (Linear Combination)**。

* **线性方程组的向量方程表达 (Vector Equations)**：
  向量方程：
  $$x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n = \mathbf{b}$$
  与增广矩阵为下式的线性方程组具有**完全相同的解集**：
  $$\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n & \mid & \mathbf{b} \end{bmatrix}$$
  * **核心判定定理**：向量 $\mathbf{b}$ 能表示为 $\mathbf{a}_1, \dots, \mathbf{a}_n$ 的线性组合，**当且仅当**对应增广矩阵为 $\begin{bmatrix} \mathbf{a}_1 & \dots & \mathbf{a}_n & \mathbf{b} \end{bmatrix}$ 的线性方程组是**相容的 (Consistent)**。

---

### 1.4 张成空间 (Span)
* **概念定义 (Definition)**：
  若 $\mathbf{v}_1, \dots, \mathbf{v}_p \in \mathbb{R}^n$，由这些向量的所有可能线性组合构成的集合称为由 $\mathbf{v}_1, \dots, \mathbf{v}_p$ **张成的子空间 (Span)**，记作：
  $$\text{Span}\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\} = \{c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_p\mathbf{v}_p : c_1, \dots, c_p \in \mathbb{R}\}$$

* **包含性与几何含义 (Geometric Meaning)**：
  1. **零向量包含性**：对任意向量集合，$\mathbf{0} \in \text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$（只需取权重 $c_1 = \dots = c_p = 0$）。
  2. **$\mathbb{R}^3$ 中单个向量 $\mathbf{v} \neq \mathbf{0}$**：$\text{Span}\{\mathbf{v}\}$ 表示过原点和点 $\mathbf{v}$ 的**直线**。
  3. **$\mathbb{R}^3$ 中两个不平行向量 $\mathbf{u}, \mathbf{v}$**：$\text{Span}\{\mathbf{u}, \mathbf{v}\}$ 表示包含 $\mathbf{u}, \mathbf{v}$ 和原点的**平面**。

---

### 🌟 随堂精选例题 (Lecture Examples)

#### 【例题 1】判断向量是否属于张成空间

**题目 (Problem)**：
Let $\mathbf{a}_1 = \begin{bmatrix} 1 \\ -2 \\ -5 \end{bmatrix}$, $\mathbf{a}_2 = \begin{bmatrix} 2 \\ 5 \\ 6 \end{bmatrix}$ , and $\mathbf{b} = \begin{bmatrix} 7 \\ 4 \\ -3 \end{bmatrix}$. Determine whether $\mathbf{b}$ is in $\text{Span}\{\mathbf{a}_1, \mathbf{a}_2\}$.

**解答过程 (Solution)**：
We check if the vector equation $x_1\mathbf{a}_1 + x_2\mathbf{a}_2 = \mathbf{b}$ has a solution.
Set up the augmented matrix and perform elementary row operations:
$$\begin{bmatrix} 1 & 2 & 7 \\ -2 & 5 & 4 \\ -5 & 6 & -3 \end{bmatrix}$$
Perform $R_2 \leftarrow R_2 + 2R_1$ and $R_3 \leftarrow R_3 + 5R_1$:
$$\begin{bmatrix} 1 & 2 & 7 \\ 0 & 9 & 18 \\ 0 & 16 & 32 \end{bmatrix}$$
Scale $R_2 \leftarrow \frac{1}{9}R_2$ and $R_3 \leftarrow \frac{1}{16}R_3$:
$$\begin{bmatrix} 1 & 2 & 7 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{bmatrix}$$
Perform $R_3 \leftarrow R_3 - R_2$:
$$\begin{bmatrix} 1 & 2 & 7 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$$
The system is consistent. Solving for $x_1, x_2$:
Row 2 gives $x_2 = 2$. Row 1 gives $x_1 + 2(2) = 7 \implies x_1 = 3$.
Since $\mathbf{b} = 3\mathbf{a}_1 + 2\mathbf{a}_2$, $\mathbf{b}$ is indeed in $\text{Span}\{\mathbf{a}_1, \mathbf{a}_2\}$.

**中文解析**：
判断向量 $\mathbf{b}$ 是否属于张成空间，本质就是求解增广矩阵 $[ \mathbf{a}_1 \; \mathbf{a}_2 \mid \mathbf{b} ]$ 的线性方程组。行化简后无矛盾行（全零行对应常数项为0），解得唯一权重 $x_1 = 3, x_2 = 2$，说明 $\mathbf{b}$ 可以表示为两向量的线性组合，因此属于该张成空间。

---

## 第二部分：Section 1.4 矩阵方程 $Ax = b$ (The Matrix Equation $Ax = b$)

### 2.1 矩阵与向量的乘积 (Matrix-Vector Product)
* **定义 (Definition - Column Combination Rule)**：
  设 $A$ 是一个 $m \times n$ 矩阵，其列向量为 $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n \in \mathbb{R}^m$；设 $\mathbf{x} \in \mathbb{R}^n$。则 $A$ 与 $\mathbf{x}$ 的乘积 $A\mathbf{x}$ 定义为**以 $\mathbf{x}$ 的分量为权重，对 $A$ 的列向量作的线性组合**：
  $$A\mathbf{x} = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n$$

* **维数匹配约束 (Dimension Match)**：
  $A\mathbf{x}$ 有定义当且仅当 **矩阵 $A$ 的列数等于向量 $\mathbf{x}$ 的分量数（行数）**。
  $$\underbrace{A}_{m \times n} \cdot \underbrace{\mathbf{x}}_{n \times 1} = \underbrace{A\mathbf{x}}_{m \times 1}$$

* **行内积法则 (Row-Vector Rule for Computing $A\mathbf{x}$)**：
  如果 $A\mathbf{x}$ 有定义，则 $A\mathbf{x}$ 中的第 $i$ 个分量等于 $A$ 的第 $i$ 行与向量 $\mathbf{x}$ 的对应元素乘积之和：
  $$(A\mathbf{x})_i = a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n$$

---

### 2.2 矩阵运算的性质与单位矩阵 (Properties & Identity Matrix)
* **线性代数性质 (Linear Properties)**：
  对任意 $m \times n$ 矩阵 $A$，向量 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ 及标量 $c \in \mathbb{R}$：
  1. $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$（分配律）
  2. $A(c\mathbf{u}) = c(A\mathbf{u})$（数乘结合律）

* **单位矩阵 (Identity Matrix)**：
  主对角线上元素均为 1、其余元素均为 0 的 $n \times n$ 方阵称为 **$n$ 阶单位矩阵**，记作 $I_n$。
  $$I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
  * 性质：对任意 $\mathbf{x} \in \mathbb{R}^n$，均有 $I_n \mathbf{x} = \mathbf{x}$。

---

### 2.3 线性方程组的三种等价表达 (Three Equivalent Forms)
设 $A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n \end{bmatrix}$ 为 $m \times n$ 矩阵，$\mathbf{b} \in \mathbb{R}^m$。以下三种表达在逻辑上完全等价，拥有**完全相同的解集**：
1. **代数方程组 (System of Linear Equations)**：
   $$\begin{cases} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\ \quad \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m \end{cases}$$
2. **向量方程 (Vector Equation)**：
   $$x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n = \mathbf{b}$$
3. **矩阵方程 (Matrix Equation)**：
   $$A\mathbf{x} = \mathbf{b}$$

---

### 2.4 解的存在性定理 (Theorem 4: Existence of Solutions)
* **定理内容 (Theorem 4)**：
  设 $A$ 为 $m \times n$ 矩阵，则下列四个命题在逻辑上是**完全等价的 (Logically Equivalent)**：
  1. 对 $\mathbb{R}^m$ 中的任意向量 $\mathbf{b}$，方程 $A\mathbf{x} = \mathbf{b}$ 均有解（相容）。
  2. $\mathbb{R}^m$ 中的每个向量 $\mathbf{b}$ 都是 $A$ 的列向量的线性组合。
  3. $A$ 的列向量张成 $\mathbb{R}^m$，即 $\text{Span}\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\} = \mathbb{R}^m$。
  4. 矩阵 $A$ 的**每一行都包含一个主元位置 (Pivot Position in Every Row)**。

* 🔍 **重点辨析与避坑提醒**：
  * **行与列的区分**：Theorem 4 强调的是**每一行都有主元** $\implies$ 保证对任意右侧向量 $\mathbf{b}$ **解的存在性 (Existence)**。
  * **唯一性 (Uniqueness)**：若要保证解是唯一的，还需要**每一列都有主元**（即没有自由变量）。若列数 $n > m$（变量数多于方程数），则不可能每一列都有主元，此时若有解必有无穷多解。

---

### 🌟 随堂精选例题 (Lecture Examples)

#### 【例题 2】计算矩阵与向量乘积
**题目 (Problem)**：
Compute $A\mathbf{x}$ using both the definition (column combinations) and the row-vector rule, where:
$$A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -5 & 3 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} 4 \\ 3 \\ 7 \end{bmatrix}$$

**解答过程 (Solution)**：
1. **Method 1: Column Combination Rule**:
   $$A\mathbf{x} = 4\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 3\begin{bmatrix} 2 \\ -5 \end{bmatrix} + 7\begin{bmatrix} -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 4 \\ 0 \end{bmatrix} + \begin{bmatrix} 6 \\ -15 \end{bmatrix} + \begin{bmatrix} -7 \\ 21 \end{bmatrix} = \begin{bmatrix} 4 + 6 - 7 \\ 0 - 15 + 21 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}$$
2. **Method 2: Row-Vector Rule**:
   * Row 1 dot $\mathbf{x}$: $1(4) + 2(3) + (-1)(7) = 4 + 6 - 7 = 3$
   * Row 2 dot $\mathbf{x}$: $0(4) + (-5)(3) + 3(7) = 0 - 15 + 21 = 6$
   Result: $A\mathbf{x} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}$.

**中文解析**：
方法一采用列组合定义，将 $\mathbf{x}$ 的分量 $4, 3, 7$ 作为权重乘以矩阵的各列；方法二采用行内积法则，分别将矩阵的行向量与 $\mathbf{x}$ 求点乘。两种方法结果一致，运算熟练后行内积法则更为便捷。

---

💡 **预习与复习总结 (Study Summary)**：
1. 掌握向量方程 $x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{b}$ 与矩阵方程 $A\mathbf{x} = \mathbf{b}$ 的对应转换。
2. 几何上理解 $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$，并能熟练通过求解增广矩阵判定向量是否属于该张成空间。
3. 熟记 Theorem 4 的四个等价条件，特别是“每一行都有主元”与“列向量张成全空间”的关系。
