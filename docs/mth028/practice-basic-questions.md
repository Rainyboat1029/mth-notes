# MTH028 Linear Algebra · Week 1–8 练习册 (Practice Workbook)

> **50 题 · 英文题干 · 37 题五选一 + 13 题填空（只填数字）· 按 Lecture / 小节 1.1–2.8 分节**
> 依据 `MTH028-LinearAlgebra` 下的讲义笔记 1–8、Weekly Assignment 1–8 与 `mth028-practice-quiz-records.md` 里的三次 Practice Quiz 题型编写（覆盖期中范围 1.1–2.8 全部小节）：每题给出中文考点标签和「做题技巧」提示，题干保留英文；选择题给 A–E 五个选项，填空题只有一个数字答案（可填整数、负数或 3/2 这样的分数）。
> 使用方法：先限时做完整节，再对照《解析册》核对；解析册开头有 50 题答案速查表。

**覆盖范围**

| 讲义 | 小节 | 内容 |
|---|---|---|
| Lecture 1 | 1.1 | 线性方程组、增广矩阵、初等行变换、相容性 |
| Lecture 2 | 1.2 | 行化简、REF / RREF、主元、解的存在唯一性 |
| Lecture 3 | 1.3 + 1.4 | 向量方程、span、矩阵方程 $A\mathbf{x}=\mathbf{b}$ |
| Lecture 4 | 1.5 + 1.7 | 齐次/非齐次解集、线性无关 |
| Lecture 5 | 1.8 + 1.9 | 线性变换、标准矩阵、单射/满射、几何变换 |
| Lecture 6 | 2.1 + 2.2 | 矩阵运算、转置、逆矩阵、$2\times2$ 公式 |
| Lecture 7 | 2.2 + 2.3 | 初等矩阵、求逆算法、可逆矩阵定理（IMT） |
| Lecture 8 | 2.8 | 子空间、零空间、列空间、基 |

**作答格式**：每题在 `Answer / 作答：(　　　)` 中写选项字母；解析册按题号 L1-01 … L8-05 对应。

---

## Lecture 1 · 1.1 Systems of Linear Equations

### L1-01 线性系统识别

*做题技巧 · 线性方程只允许「常数 × 未知数 相加 = 常数」：不能有根号、乘积、三角、绝对值。*

Which of the following systems is **not** a linear system?

**SELECT ONE**

- A. $2x_1-x_2=4,\quad x_1+3x_2=1$
- B. $x_1+x_2=0,\quad 2x_1-5x_2=3$
- C. $x_1-\sqrt{x_2}=1,\quad x_1+x_2=2$
- D. $3x_1=6,\quad x_2=-1$
- E. $x_1-x_2+x_3=0,\quad x_1+x_3=4,\quad x_2=1$

Answer / 作答：(　　　)　·　解析见 L1-01

---

### L1-02 增广矩阵还原方程组

*做题技巧 · 增广矩阵最后一列是常数项，其余每一列对应一个未知数；行数 = 方程个数。*

Write the linear system whose augmented matrix is $\left[\begin{array}{cccc}1&-4&2&8\\0&3&-5&1\end{array}\right]$.

**SELECT ONE**

- A. $x_1-4x_2+2x_3=8,\quad 3x_2-5x_3=1$
- B. $x_1-4x_2+2x_3=0,\quad 3x_2-5x_3=0$
- C. $x_1+4x_2-2x_3=8,\quad 3x_2+5x_3=1$
- D. $4x_1-2x_2+x_3=8,\quad 3x_2-5x_3=1$
- E. $x_1-4x_2+2x_3=8,\quad 3x_1-5x_2+x_3=1$

Answer / 作答：(　　　)　·　解析见 L1-02

---

### L1-03 初等行变换

*做题技巧 · 三种初等行变换：交换两行、某行乘非零常数、某行加上另一行的倍数。每次只能动一步。*

Which of the following is **not** an elementary row operation?

**SELECT ONE**

- A. Interchange $R_1$ and $R_2$.
- B. Replace $R_2$ by $R_2-4R_1$.
- C. Multiply $R_3$ by $\tfrac{1}{2}$.
- D. Replace $R_1$ by $R_1+R_2$ and simultaneously replace $R_2$ by $R_1-R_2$.
- E. Multiply $R_1$ by $-3$.

Answer / 作答：(　　　)　·　解析见 L1-03

---

### L1-04 由阶梯形判断解的个数

*做题技巧 · 出现 $[0\ 0\ \cdots\ 0\ |\ c]$ 且 $c\neq0$ 的行 ⇒ 无解；否则看有没有自由变量。*

The augmented matrix of a linear system has been reduced to $\left[\begin{array}{ccc|c}1&2&-1&3\\0&0&4&8\\0&0&0&5\end{array}\right]$. How many solutions does the system have?

**SELECT ONE**

- A. exactly one
- B. exactly two
- C. none
- D. infinitely many
- E. cannot be determined

Answer / 作答：(　　　)　·　解析见 L1-04

---

## Lecture 2 · 1.2 Row Reduction and Echelon Forms

### L2-01 REF 与 RREF 的区别

*做题技巧 · RREF 两条额外要求：每个主元是 1（REF 已保证），且主元所在列的其余元素全为 0。*

Which matrix is in row echelon form but **not** in reduced row echelon form?

**SELECT ONE**

- A. $\begin{bmatrix}1&0&2&1\\0&1&-3&2\\0&0&0&0\end{bmatrix}$
- B. $\begin{bmatrix}1&2&3\\0&0&1\\0&0&0\end{bmatrix}$
- C. $\begin{bmatrix}1&0\\0&1\end{bmatrix}$
- D. $\begin{bmatrix}0&1&2\\1&0&3\\0&0&0\end{bmatrix}$
- E. $\begin{bmatrix}1&2&3\\0&0&0\\0&1&0\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 L2-01

---

### L2-02 主元个数

*做题技巧 · 主元个数 = 行化简后非零行的行数；不要只看非零元素个数。*

How many pivot columns does $A=\begin{bmatrix}1&2&3\\2&4&7\\3&6&10\end{bmatrix}$ have?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L2-02

---

### L2-03 参数向量形式解

*做题技巧 · 主元变量用自由变量表示，再把解写成「特解 + 自由变量 × 方向向量」。*

Find the general solution of $x_1+2x_2-x_3=1,\quad 2x_1+4x_2+x_3=5$.

**SELECT ONE**

- A. $\mathbf{x}=(2,0,1)+t(-2,1,0)$
- B. $\mathbf{x}=(2,0,1)+t(2,1,0)$
- C. $\mathbf{x}=(1,0,2)+t(-2,1,0)$
- D. $\mathbf{x}=(2,0,1)+t(-2,0,1)$
- E. the system is inconsistent

Answer / 作答：(　　　)　·　解析见 L2-03

---

### L2-04 自由变量个数

*做题技巧 · 自由变量个数 = 未知数个数 − 主元个数。*

The reduced echelon form of an augmented matrix is $\left[\begin{array}{ccc|c}1&-2&0&1\\0&0&1&2\end{array}\right]$. How many free variables does the system have?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L2-04

---

### L2-05 参数 $h$ 决定解的个数

*做题技巧 · 把方程组化成阶梯形，看最后一行是 $0=0$（无穷多解）、$0\neq0$（无解）还是正常方程（唯一解）。*

For which value of $h$ does $x_1+hx_2=2,\quad 4x_1+8x_2=8$ have infinitely many solutions?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L2-05

---

## Lecture 3 · 1.3 Vector Equations and 1.4 The Matrix Equation

### L3-01 线性组合

*做题技巧 · 设 $c_1a_1+c_2a_2=b$，写出两个分量的方程再解 $c_1,c_2$；也可直接用增广矩阵。*

Express $\mathbf{b}=(5,-10)$ as a linear combination of $\mathbf{a}_1=(1,2)$ and $\mathbf{a}_2=(-1,3)$.

**SELECT ONE**

- A. $\mathbf{b}=-1\mathbf{a}_1+4\mathbf{a}_2$
- B. $\mathbf{b}=1\mathbf{a}_1+4\mathbf{a}_2$
- C. $\mathbf{b}=1\mathbf{a}_1-4\mathbf{a}_2$
- D. $\mathbf{b}=-1\mathbf{a}_1-4\mathbf{a}_2$
- E. $\mathbf{b}$ is not in $\operatorname{Span}\{\mathbf{a}_1,\mathbf{a}_2\}$

Answer / 作答：(　　　)　·　解析见 L3-01

---

### L3-02 span 的几何形状

*做题技巧 · 两个向量若一个是另一个的倍数，span 只有一条线；不共线才张成平面。*

Let $\mathbf{v}_1=(1,2,3)$ and $\mathbf{v}_2=(2,4,6)$. The span of $\{\mathbf{v}_1,\mathbf{v}_2\}$ is

**SELECT ONE**

- A. a single point
- B. a line through the origin
- C. a plane through the origin
- D. all of $\mathbb{R}^3$
- E. the empty set

Answer / 作答：(　　　)　·　解析见 L3-02

---

### L3-03 矩阵与向量相乘

*做题技巧 · $A\mathbf{x}$ 的第 $i$ 个分量 = $A$ 的第 $i$ 行与 $\mathbf{x}$ 的点积。*

Compute $\begin{bmatrix}1&-2&3\\0&4&-1\end{bmatrix}\begin{bmatrix}2\\-1\\3\end{bmatrix}$.

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L3-03

---

### L3-04 由列向量判断相容性

*做题技巧 · $A\mathbf{x}=\mathbf{b}$ 相容 ⇔ $\mathbf{b}$ 是 $A$ 的列向量的线性组合；两列成比例时，$\mathbf{b}$ 也必须是同一比例。*

For which $k$ is the system with $A=\begin{bmatrix}1&3\\2&6\end{bmatrix}$ and $\mathbf{b}=\begin{bmatrix}2\\k\end{bmatrix}$ consistent?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L3-04

---

### L3-05 向量方程与方程组互化

*做题技巧 · 每个未知数配一个列向量，系数取自对应的那一列；右端是常数向量。*

Which vector equation is equivalent to the system $2x_1-x_2=5,\quad x_1+3x_2-x_3=1$?

**SELECT ONE**

- A. $x_1\begin{bmatrix}2\\-1\end{bmatrix}+x_2\begin{bmatrix}1\\3\end{bmatrix}+x_3\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$
- B. $x_1\begin{bmatrix}2\\1\end{bmatrix}+x_2\begin{bmatrix}-1\\3\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$
- C. $x_1\begin{bmatrix}2\\1\end{bmatrix}+x_2\begin{bmatrix}-1\\3\end{bmatrix}+x_3\begin{bmatrix}0\\-1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$
- D. $x_1\begin{bmatrix}2\\1\end{bmatrix}+x_2\begin{bmatrix}3\\-1\end{bmatrix}+x_3\begin{bmatrix}-1\\0\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$
- E. $x_1\begin{bmatrix}2\\1\end{bmatrix}+x_2\begin{bmatrix}-1\\3\end{bmatrix}+x_3\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 L3-05

---

### L3-06 三个向量是否张成 $\mathbb{R}^3$

*做题技巧 · 把向量按列排成矩阵再行化简；有 3 个主元才张成 $\mathbb{R}^3$。向量个数够不代表能张成。*

Do the vectors $(1,0,1)$, $(0,1,1)$, $(1,1,2)$ span $\mathbb{R}^3$?

**SELECT ONE**

- A. Yes, because there are three vectors.
- B. Yes, because the matrix has a pivot in every row.
- C. No, because one of the vectors is the zero vector.
- D. No: $(1,1,2)=\mathbf{v}_1+\mathbf{v}_2$, so the span is only a plane.
- E. No, because the three vectors are linearly independent.

Answer / 作答：(　　　)　·　解析见 L3-06

---

### L3-07 找零空间中的向量

*做题技巧 · 把 $A\mathbf{x}=\mathbf{0}$ 化成 RREF，主元变量用自由变量表示，再取自由变量的具体值。*

Which vector is in $\operatorname{Nul}A$ for $A=\begin{bmatrix}1&2&3\\0&1&4\end{bmatrix}$?

**SELECT ONE**

- A. $(5,-4,1)$
- B. $(1,-4,5)$
- C. $(-5,4,1)$
- D. $(5,4,1)$
- E. only the zero vector

Answer / 作答：(　　　)　·　解析见 L3-07

---

### L3-08 列向量张成与相容性

*做题技巧 · 若 $A$ 的列向量张成 $\mathbb{R}^m$，则对任意 $\mathbf{b}$ 方程 $A\mathbf{x}=\mathbf{b}$ 都有解（Theorem 4）。*

Let $A$ be a $3\times3$ matrix whose columns span $\mathbb{R}^3$. Which statement is true?

**SELECT ONE**

- A. $A\mathbf{x}=\mathbf{b}$ has no solution for some $\mathbf{b}$.
- B. Every echelon form of $A$ has a zero row.
- C. $A\mathbf{x}=\mathbf{b}$ is consistent for every $\mathbf{b}$ in $\mathbb{R}^3$.
- D. $A$ has fewer than three pivot positions.
- E. The columns of $A$ are linearly dependent.

Answer / 作答：(　　　)　·　解析见 L3-08

---

## Lecture 4 · 1.5 Solution Sets and 1.7 Linear Independence

### L4-01 齐次方程组的解集

*做题技巧 · 齐次方程组解集 = 零空间；每个自由变量配一个方向向量，常数项一定是 $\mathbf{0}$。*

Find the solution set of $A\mathbf{x}=\mathbf{0}$ for $A=\begin{bmatrix}1&-3&2\\-2&6&-4\end{bmatrix}$.

**SELECT ONE**

- A. $\mathbf{x}=s(3,1,0)+t(2,0,1)$
- B. $\mathbf{x}=s(3,1,0)+t(-2,0,-1)$
- C. $\mathbf{x}=s(3,1,0)+t(-2,0,1)$
- D. $\mathbf{x}=s(1,3,0)+t(0,-2,1)$
- E. only $\mathbf{x}=\mathbf{0}$

Answer / 作答：(　　　)　·　解析见 L4-01

---

### L4-02 非齐次解 = 特解 + 齐次解

*做题技巧 · 先求一个特解 $\mathbf{p}$，再求 $A\mathbf{x}=\mathbf{0}$ 的基础解，两者相加就是全部解。*

Solve $\begin{bmatrix}1&1&1\\0&1&2\end{bmatrix}\mathbf{x}=\begin{bmatrix}3\\1\end{bmatrix}$.

**SELECT ONE**

- A. $\mathbf{x}=(2,1,0)+t(1,-2,1)$
- B. $\mathbf{x}=(2,1,0)+t(1,2,1)$
- C. $\mathbf{x}=(3,1,0)+t(1,-2,1)$
- D. $\mathbf{x}=(2,1,0)+t(-2,1,1)$
- E. the system is inconsistent

Answer / 作答：(　　　)　·　解析见 L4-02

---

### L4-03 解集的几何描述

*做题技巧 · 自由变量个数决定「点/线/面」；$\mathbf{b}\neq\mathbf{0}$ 时解集不过原点。*

A consistent system $A\mathbf{x}=\mathbf{b}$ with three unknowns has two pivot columns and $\mathbf{b}\neq\mathbf{0}$. Its solution set is

**SELECT ONE**

- A. a single point
- B. a line not passing through the origin
- C. a plane through the origin
- D. a line passing through the origin
- E. all of $\mathbb{R}^3$

Answer / 作答：(　　　)　·　解析见 L4-03

---

### L4-04 齐次方程组一定有解

*做题技巧 · 取全部未知数为 0 必然满足 $A\mathbf{0}=\mathbf{0}$，所以齐次方程组永远相容。*

Which statement about the homogeneous system $A\mathbf{x}=\mathbf{0}$ is always true?

**SELECT ONE**

- A. It has a unique solution for every $A$.
- B. It is inconsistent for some $A$.
- C. Its solution set is empty.
- D. It is consistent, because $\mathbf{x}=\mathbf{0}$ is a solution.
- E. It has exactly $n$ solutions, where $n$ is the number of columns.

Answer / 作答：(　　　)　·　解析见 L4-04

---

### L4-05 解集的维数

*做题技巧 · 未知数 4 个、主元 2 个 ⇒ 自由变量 2 个 ⇒ 解集是 $\mathbb{R}^4$ 中过原点的平面。*

$A$ is a $2\times4$ matrix whose RREF has 2 pivot columns. The solution set of $A\mathbf{x}=\mathbf{0}$ is

**SELECT ONE**

- A. a single point
- B. a line through the origin in $\mathbb{R}^4$
- C. a plane through the origin in $\mathbb{R}^4$
- D. all of $\mathbb{R}^4$
- E. $\{\mathbf{0}\}$

Answer / 作答：(　　　)　·　解析见 L4-05

---

### L4-06 判断线性无关

*做题技巧 · 三个向量是否相关，等价于以它们为列的矩阵是否有非平凡零空间；能看出倍数关系时直接写出来。*

Is the set $\{(1,2,3),(4,5,6),(7,8,9)\}$ linearly independent?

**SELECT ONE**

- A. Yes, the three vectors are independent.
- B. No, because $(7,8,9)=2(4,5,6)-(1,2,3)$.
- C. No, because $(1,2,3)=(4,5,6)-(7,8,9)$.
- D. Yes, because the determinant is nonzero.
- E. cannot be determined without more information

Answer / 作答：(　　　)　·　解析见 L4-06

---

### L4-07 含零向量的集合

*做题技巧 · 只要集合里有 $\mathbf{0}$，取它的系数不为 0、其余为 0，就得到非平凡线性相关关系。*

If a set of vectors contains the zero vector, then the set is

**SELECT ONE**

- A. linearly independent
- B. a basis for its span
- C. a spanning set for $\mathbb{R}^n$
- D. linearly dependent
- E. necessarily empty

Answer / 作答：(　　　)　·　解析见 L4-07

---

### L4-08 向量个数超过维数

*做题技巧 · $\mathbb{R}^n$ 中任何多于 $n$ 个向量的集合一定线性相关。*

Any set of four vectors in $\mathbb{R}^3$ is

**SELECT ONE**

- A. linearly dependent
- B. linearly independent
- C. a basis of $\mathbb{R}^3$
- D. a spanning set of $\mathbb{R}^3$
- E. inconsistent

Answer / 作答：(　　　)　·　解析见 L4-08

---

### L4-09 参数 $h$ 使集合相关

*做题技巧 · 三个向量相关 ⇔ 它们排成的矩阵行列式为 0；先展开行列式再解 $h$。*

For which value of $h$ is the set $\{(1,4,7),(2,5,8),(3,6,h)\}$ linearly dependent?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L4-09

---

## Lecture 5 · 1.8 Linear Transformations and 1.9 The Standard Matrix

### L5-01 判断线性变换

*做题技巧 · 线性变换必须满足 $T(\mathbf{0})=\mathbf{0}$、$T(c\mathbf{u})=cT(\mathbf{u})$、$T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v})$。*

Which of the following transformations $T:\mathbb{R}^2\to\mathbb{R}^2$ is linear?

**SELECT ONE**

- A. $T(x_1,x_2)=(x_1^2,\ x_2)$
- B. $T(x_1,x_2)=(x_1,\ x_2+1)$
- C. $T(x_1,x_2)=(2x_1-x_2,\ x_1)$
- D. $T(x_1,x_2)=(x_1x_2,\ 0)$
- E. $T(x_1,x_2)=(|x_1|,\ x_2)$

Answer / 作答：(　　　)　·　解析见 L5-01

---

### L5-02 求标准矩阵

*做题技巧 · 标准矩阵的第 $j$ 列就是 $T(\mathbf{e}_j)$：把 $x_j=1$、其余为 0 代入，读出各分量。*

Let $T(x_1,x_2,x_3)=(x_1-2x_2,\ 3x_1+x_3)$. Find the standard matrix of $T$.

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L5-02

---

### L5-03 单射与满射（由主元判断）

*做题技巧 · $A$ 为 $m\times n$：满射 ⇔ 每一行都有主元；单射 ⇔ 每一列都有主元（即无自由变量）。*

$A$ is a $3\times4$ matrix with a pivot in every row. The transformation $T(\mathbf{x})=A\mathbf{x}$ is

**SELECT ONE**

- A. both one-to-one and onto
- B. one-to-one but not onto
- C. neither one-to-one nor onto
- D. onto but not one-to-one
- E. not a linear transformation

Answer / 作答：(　　　)　·　解析见 L5-03

---

### L5-04 旋转矩阵

*做题技巧 · 逆时针旋转 $\theta$ 的标准矩阵是 $\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$，$\theta=\pi/2$ 时 $\cos=0,\ \sin=1$。*

The standard matrix for rotation by $\pi/2$ counterclockwise is

**SELECT ONE**

- A. $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$
- B. $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$
- C. $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$
- D. $\begin{bmatrix}-1&0\\0&-1\end{bmatrix}$
- E. $\begin{bmatrix}1&0\\0&1\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 L5-04

---

### L5-05 由像求标准矩阵

*做题技巧 · 标准矩阵的列就是基向量的像，$A=[\,T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\,]$，注意是「按列放」不是「按行放」。*

Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be linear with $T(\mathbf{e}_1)=(1,2)$ and $T(\mathbf{e}_2)=(3,4)$. Find the standard matrix of $T$.

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L5-05

---

### L5-06 不可逆矩阵对应的变换

*做题技巧 · 列向量成比例 ⇒ 行列式为 0 ⇒ 不是单射、不是满射，值域只是一条线。*

Let $T(\mathbf{x})=A\mathbf{x}$ with $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$. Which statement is true?

**SELECT ONE**

- A. $T$ is one-to-one.
- B. $T$ maps $\mathbb{R}^2$ onto $\mathbb{R}^2$.
- C. The range of $T$ is a line through the origin.
- D. The kernel of $T$ is $\{\mathbf{0}\}$.
- E. $A$ is invertible.

Answer / 作答：(　　　)　·　解析见 L5-06

---

## Lecture 6 · 2.1 Matrix Operations and 2.2 The Inverse of a Matrix

### L6-01 矩阵乘积的某一行元素

*做题技巧 · $AB$ 的 $(i,j)$ 元素 = $A$ 的第 $i$ 行与 $B$ 的第 $j$ 列的点积。*

Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. The $(2,1)$-entry of $AB$ is

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L6-01

---

### L6-02 矩阵线性组合

*做题技巧 · 数乘与减法逐元素进行，先算 $4A$ 与 $2B$ 再相减。*

Let $A=\begin{bmatrix}1&-2\\3&0\end{bmatrix}$, $B=\begin{bmatrix}2&1\\-1&4\end{bmatrix}$. The $(1,2)$-entry of $4A-2B$ is

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L6-02

---

### L6-03 矩阵运算律

*做题技巧 · 矩阵乘法不交换、不满足「零乘积必有零因子」，但分配律与 $(A+B)^2=A^2+AB+BA+B^2$ 成立。*

Which statement is true for square matrices of the same size?

**SELECT ONE**

- A. $AB=BA$ for all $A,B$.
- B. $AB=0$ implies $A=0$ or $B=0$.
- C. $(A+B)^2=A^2+AB+BA+B^2$.
- D. $(AB)^2=A^2B^2$.
- E. $A(B+C)=AB+C$.

Answer / 作答：(　　　)　·　解析见 L6-03

---

### L6-04 转置与乘积

*做题技巧 · $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$，转置把顺序倒过来。*

Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. The $(1,2)$-entry of $(AB)^{\mathsf T}$ is

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L6-04

---

### L6-05 $2\times2$ 逆矩阵公式

*做题技巧 · $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$ 可逆 ⇔ $ad-bc\neq0$，此时 $A^{-1}=\dfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$。*

Find the inverse of $A=\begin{bmatrix}3&1\\4&2\end{bmatrix}$.

**SELECT ONE**

- A. $\begin{bmatrix}2&-1\\-4&3\end{bmatrix}$
- B. $\begin{bmatrix}1/2&-1/4\\-1&3/2\end{bmatrix}$
- C. $\begin{bmatrix}1&-1/2\\-2&3/2\end{bmatrix}$
- D. $\begin{bmatrix}3&1\\4&2\end{bmatrix}$
- E. $A$ is not invertible

Answer / 作答：(　　　)　·　解析见 L6-05

---

### L6-06 用逆矩阵解方程

*做题技巧 · $A\mathbf{x}=\mathbf{b}$ 且 $A$ 可逆时 $\mathbf{x}=A^{-1}\mathbf{b}$；先验证 $\det A\neq0$。*

Solve $\begin{bmatrix}2&1\\1&1\end{bmatrix}\mathbf{x}=\begin{bmatrix}5\\3\end{bmatrix}$.

**SELECT ONE**

- A. $(2,1)$
- B. $(1,2)$
- C. $(5,3)$
- D. $(2,-1)$
- E. $(3,2)$

Answer / 作答：(　　　)　·　解析见 L6-06

---

### L6-07 乘积的逆

*做题技巧 · $(AB)^{-1}=B^{-1}A^{-1}$，顺序必须反过来。*

Let $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $B=\begin{bmatrix}1&0\\3&1\end{bmatrix}$. Find $(AB)^{-1}$.

**SELECT ONE**

- A. $\begin{bmatrix}1&2\\-3&7\end{bmatrix}$
- B. $\begin{bmatrix}7&-2\\-3&1\end{bmatrix}$
- C. $\begin{bmatrix}1&-2\\-3&7\end{bmatrix}$
- D. $\begin{bmatrix}-3&7\\1&-2\end{bmatrix}$
- E. $\begin{bmatrix}1&-2\\3&7\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 L6-07

---

### L6-08 含参数矩阵不可逆

*做题技巧 · $2\times2$ 不可逆 ⇔ 行列式为 0；含参数时令 $ad-bc=0$ 解参数。*

For which $h$ is $A=\begin{bmatrix}h&2\\3&4\end{bmatrix}$ not invertible?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L6-08

---

## Lecture 7 · 2.2 Elementary Matrices and 2.3 The Invertible Matrix Theorem

### L7-01 初等矩阵的逆

*做题技巧 · 交换两行的初等矩阵是自身的逆；乘倍数与加倍的逆分别是乘倒数、加相反倍数。*

Let $E=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. Then $E^{-1}$ is

**SELECT ONE**

- A. $E$ itself
- B. $\begin{bmatrix}0&-1\\-1&0\end{bmatrix}$
- C. $\begin{bmatrix}1&0\\0&1\end{bmatrix}$
- D. $E$ is not invertible
- E. $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 L7-01

---

### L7-02 初等矩阵乘积的逆

*做题技巧 · $(E_1E_2E_3)^{-1}=E_3^{-1}E_2^{-1}E_1^{-1}$：逆序，且每个逆都容易写。*

Let $E_1$ interchange rows 1 and 2, $E_2$ add $-2$ times row 1 to row 3, and $E_3$ multiply row 2 by $\tfrac14$. For $A=E_1E_2E_3$, find $A^{-1}$.

**SELECT ONE**

- A. $\begin{bmatrix}0&1&0\\4&0&0\\0&2&1\end{bmatrix}$
- B. $\begin{bmatrix}0&4&0\\1&0&2\\0&0&1\end{bmatrix}$
- C. $\begin{bmatrix}0&1&0\\1/4&0&0\\0&1/2&1\end{bmatrix}$
- D. $A$ itself
- E. $A$ is not invertible

Answer / 作答：(　　　)　·　解析见 L7-02

---

### L7-03 可逆矩阵定理（IMT）

*做题技巧 · IMT 把所有等价条件串起来：$n$ 个主元、列张成 $\mathbb{R}^n$、列无关、$A\mathbf{x}=\mathbf{0}$ 只有零解、$\det A\neq0$。*

For an $n\times n$ matrix $A$, which statement is **not** equivalent to "$A$ is invertible"?

**SELECT ONE**

- A. $A$ has $n$ pivot positions.
- B. The columns of $A$ span $\mathbb{R}^n$.
- C. $A\mathbf{x}=\mathbf{0}$ has only the trivial solution.
- D. $\det A=0$.
- E. The columns of $A$ are linearly independent.

Answer / 作答：(　　　)　·　解析见 L7-03

---

### L7-04 可逆矩阵的消去律

*做题技巧 · 两边左乘 $A^{-1}$ 即可消去 $A$；不可逆时不能这样消。*

If $A$ is invertible and $AB=AC$, then

**SELECT ONE**

- A. $B=C$ only when $B,C$ are square.
- B. $B=C$.
- C. nothing can be concluded about $B$ and $C$.
- D. $A=0$.
- E. $B=A$.

Answer / 作答：(　　　)　·　解析见 L7-04

---

### L7-05 IMT 的应用

*做题技巧 · $3\times3$ 有 3 个主元 ⇒ 可逆 ⇒ 列无关且张成 $\mathbb{R}^3$；「列相关」正好相反。*

$A$ is a $3\times3$ matrix with three pivot positions. Which statement is **false**?

**SELECT ONE**

- A. $A\mathbf{x}=\mathbf{b}$ is consistent for every $\mathbf{b}$.
- B. The columns of $A$ span $\mathbb{R}^3$.
- C. The columns of $A$ are linearly dependent.
- D. $A$ is row equivalent to $I_3$.
- E. $A\mathbf{x}=\mathbf{0}$ has only the trivial solution.

Answer / 作答：(　　　)　·　解析见 L7-05

---

## Lecture 8 · 2.8 Subspaces, Null Space and Column Space

### L8-01 判断子空间

*做题技巧 · 子空间必须：含零向量、对加法封闭、对数乘封闭。形如「一个线性方程 $=0$」的集合通常是过原点的平面。*

Which set is a subspace of $\mathbb{R}^2$?

**SELECT ONE**

- A. $\{(x_1,x_2):x_1=1\}$
- B. $\{(x_1,x_2):x_1+2x_2=0\}$
- C. $\{(x_1,x_2):x_1x_2=0\}$
- D. $\{(x_1,x_2):x_1\ge0\}$
- E. $\{(x_1,x_2):|x_1|=|x_2|\}$

Answer / 作答：(　　　)　·　解析见 L8-01

---

### L8-02 求零空间的基

*做题技巧 · 把 $A$ 化成 RREF，主元变量用自由变量表示，每个自由变量给 $1$、其余给 $0$，得到一组基。*

Find a basis for $\operatorname{Nul}A$ where $A=\begin{bmatrix}1&2&0&-1\\0&0&1&3\end{bmatrix}$.

**SELECT ONE**

- A. $\{(1,0,0,0),(0,0,1,0)\}$
- B. $\{(-2,1,0,0)\}$
- C. $\{(2,1,0,0),(1,0,-3,1)\}$
- D. $\{(-2,1,0,0),(1,0,-3,1)\}$
- E. $\{(-2,1,0,0),(1,0,-3,1),(0,0,0,0)\}$

Answer / 作答：(　　　)　·　解析见 L8-02

---

### L8-03 求列空间的基

*做题技巧 · 列空间的基 = $A$ 中主元所在的列（用原矩阵的列，不是化简后的列）。*

Let $A=\begin{bmatrix}1&2&0\\0&1&3\\2&5&3\end{bmatrix}$. How many vectors are in a basis for $\operatorname{Col}A$?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 L8-03

---

### L8-04 判断是否为基

*做题技巧 · 基 = 线性无关 + 张成。$\mathbb{R}^2$ 中两个向量成比例就一定不是基。*

Is $\{(1,2),(2,4)\}$ a basis for $\mathbb{R}^2$?

**SELECT ONE**

- A. Yes, because there are two vectors in $\mathbb{R}^2$.
- B. Yes, because they span a plane.
- C. No, because they are linearly dependent.
- D. No, because one of the vectors is zero.
- E. Yes, but it is not a spanning set.

Answer / 作答：(　　　)　·　解析见 L8-04

---

### L8-05 零空间与列空间所在的向量空间

*做题技巧 · $A$ 为 $m\times n$ 时，$\operatorname{Nul}A\subseteq\mathbb{R}^n$（未知数个数），$\operatorname{Col}A\subseteq\mathbb{R}^m$（方程个数）。*

Let $A$ be a $3\times4$ matrix. Which statement is true?

**SELECT ONE**

- A. $\operatorname{Nul}A$ is a subspace of $\mathbb{R}^4$ and $\operatorname{Col}A$ is a subspace of $\mathbb{R}^3$.
- B. $\operatorname{Nul}A\subseteq\mathbb{R}^3$ and $\operatorname{Col}A\subseteq\mathbb{R}^4$.
- C. Both are subspaces of $\mathbb{R}^3$.
- D. Both are subspaces of $\mathbb{R}^4$.
- E. $\operatorname{Nul}A$ is not a subspace.

Answer / 作答：(　　　)　·　解析见 L8-05
