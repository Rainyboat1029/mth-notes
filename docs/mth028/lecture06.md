# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 2.1 & 2.2 矩阵运算与逆矩阵 (Matrix Operations & The Inverse of a Matrix)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 6 Summary)

### Section 2.1 矩阵运算 (Matrix Operations)

#### 1. 矩阵的基本记号与特殊矩阵 (Notation & Special Matrices)
* **矩阵元素与列表示 (Matrix Entries & Column Representation)**：
  一个 $m \times n$ 矩阵 $A$ 可以记为 $A = [a_{ij}] \in M_{mn}(\mathbb{R})$，其中双下标 $a_{ij}$ 表示位于第 $i$ 行第 $j$ 列的元素（$(i, j)$-entry）。按列向量可表示为：
  $$A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n \end{bmatrix}$$
* **主对角线 (Main Diagonal)**：
  矩阵 $A = [a_{ij}]$ 中，元素 $a_{11}, a_{22}, a_{33}, \dots$ 构成的对角线称为**主对角线 (Main Diagonal)**，这些元素称为**对角元 (Diagonal Entries)**。
* **对角矩阵 (Diagonal Matrix)**：
  主对角线以外的所有元素均为 0 的 $n \times n$ 正方形矩阵（方阵）称为**对角矩阵**。特别地，记：
  $$\text{Diag}\{a_1, a_2, \dots, a_n\} = \begin{bmatrix} a_1 & 0 & \dots & 0 \\ 0 & a_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & a_n \end{bmatrix}$$
* **零矩阵 (Zero Matrix)**：
  所有元素全为零的 $m \times n$ 矩阵称为**零矩阵**，记作 $O$ 或 $0$。
* **单位矩阵 (Identity Matrix)**：
  主对角线上元素全为 1、其余位置元素全为 0 的 $n \times n$ 方阵称为 **$n$ 阶单位矩阵**，记作 $I_n$（或 $I$）。

---

#### 2. 矩阵加法与数乘 (Sums and Scalar Multiples)
* **矩阵相等 (Matrix Equality)**：
  两个矩阵相等，当且仅当它们具有**相同的阶数（尺寸）** $m \times n$，且对应的列向量（或对应位置的元素）完全相等。
* **矩阵加法 (Matrix Sum)**：
  若 $A = [a_{ij}]$ 与 $B = [b_{ij}]$ 是两个同阶的 $m \times n$ 矩阵，则它们的和 $A + B$ 为按对应元素相加得到的 $m \times n$ 矩阵：
  $$A + B = [a_{ij} + b_{ij}]$$
  *⚠️ 警告*：阶数不同的两个矩阵**不能相加**！
* **数乘运算 (Scalar Multiplication)**：
  若 $A = [a_{ij}]$ 是 $m \times n$ 矩阵，$r \in \mathbb{R}$ 为标量（实数），则数乘 $rA$ 是将 $A$ 的每个元素分别乘以 $r$ 得到的矩阵：
  $$rA = [r a_{ij}]$$

##### 加法与数乘的代数性质 (Theorem 1)
设 $A, B, C$ 为同阶 $m \times n$ 矩阵，$r, s$ 为标量，则满足以下代数性质：
1. $A + B = B + A$ （加法交换律）
2. $(A + B) + C = A + (B + C)$ （加法结合律）
3. $A + 0 = A$ （加法单位元）
4. $r(A + B) = rA + rB$ （标量对矩阵加法的分配律）
5. $(r + s)A = rA + sA$ （矩阵对标量加法的分配律）
6. $r(sA) = (rs)A$ （数乘结合律）

---

#### 3. 矩阵乘法 (Matrix Multiplication)
* **按列组合定义 (Definition by Columns)**：
  设 $A$ 为 $m \times n$ 矩阵，$B$ 为 $n \times p$ 矩阵，其列向量为 $\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_p$。则乘积 $AB$ 定义为一个 $m \times p$ 矩阵，其第 $j$ 列为 $A$ 与 $B$ 第 $j$ 列的乘积 $A\mathbf{b}_j$：
  $$AB = A \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \dots & \mathbf{b}_p \end{bmatrix} = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \dots & A\mathbf{b}_p \end{bmatrix}$$
  * **维数匹配约束 (Size Requirement)**：
    为了使乘积 $AB$ 有定义，$A$ 的列数必须**等于** $B$ 的行数。若 $A$ 是 $m \times n$，$B$ 是 $n \times p$，则 $AB$ 的大小为 $m \times p$。
* **行内积法则 / 按元素计算法则 (Row-Column Rule)**：
  若乘积 $AB$ 有定义，则 $AB$ 中位于第 $i$ 行第 $j$ 列的元素 $(AB)_{ij}$ 等于 $A$ 的第 $i$ 行与 $B$ 的第 $j$ 列对应元素的乘积之和：
  $$(AB)_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj} = \sum_{k=1}^n a_{ik}b_{kj}$$
* **行观察与列观察 (Observations on Rows and Columns)**：
  - $\text{col}_j(AB) = A \cdot \text{col}_j(B)$ （$AB$ 的第 $j$ 列是矩阵 $A$ 乘以 $B$ 的第 $j$ 列）
  - $\text{row}_i(AB) = \text{row}_i(A) \cdot B$ （$AB$ 的第 $i$ 行是 $A$ 的第 $i$ 行乘以矩阵 $B$）

##### 复合映射的几何解释 (Composition of Linear Transformations)
矩阵乘法的实质是**线性映射的复合 (Composition)**：
设 $T_2(\mathbf{y}) = B\mathbf{y}$ 是从 $\mathbb{R}^p \to \mathbb{R}^n$ 的线性变换，$T_1(\mathbf{x}) = A\mathbf{x}$ 是从 $\mathbb{R}^n \to \mathbb{R}^m$ 的线性变换，则复合变换 $(T_1 \circ T_2)(\mathbf{y}) = T_1(T_2(\mathbf{y})) = A(B\mathbf{y}) = (AB)\mathbf{y}$ 是从 $\mathbb{R}^p \to \mathbb{R}^m$ 的线性变换，其标准矩阵恰好为乘积矩阵 $AB$。

---

#### 4. 矩阵乘法的运算律与代数避坑 (Properties & Warnings)

##### 矩阵乘法的运算律 (Theorem 2)
设 $A$ 为 $m \times n$ 矩阵，$B, C$ 的阶数使下列算式有定义，则：
1. $A(BC) = (AB)C$ （结合律）
2. $A(B + C) = AB + AC$ （左分配律）
3. $(B + C)A = BA + CA$ （右分配律）
4. $r(AB) = (rA)B = A(rB)$ （对标量乘法）
5. $I_m A = A = A I_n$ （单位矩阵性质）

##### ⚠️ 矩阵代数三大避坑警告 (Important Warnings)
1. **通常不满足交换律 (Non-commutative)**：  
   一般情况下 $AB \neq BA$。即使 $AB$ 与 $BA$ 均有定义且同阶，两者也未必相等！
2. **消去律不成立 (No Cancellation Law)**：  
   如果 $AB = AC$ 且 $A \neq O$，**不能**推导出 $B = C$。
3. **零因子存在 (Presence of Zero Divisors)**：  
   如果乘积 $AB = O$，**不能**推导出 $A = O$ 或 $B = O$（两个非零矩阵相乘完全可能得到零矩阵）。

---

#### 5. 矩阵的幂与转置 (Powers and Transpose)
* **矩阵的幂 (Powers of a Matrix)**：
  设 $A$ 为 $n \times n$ 阶方阵，$k$ 为正整数，则 $A^k$ 表示 $k$ 个 $A$ 连乘：
  $$A^k = \underbrace{A \cdot A \dots A}_{k \text{ 个}}$$
  规定 $A^0 = I_n$。对正整数 $k, l$，有指数律 $A^k A^l = A^{k+l}$。
* **矩阵转置 (Transpose of a Matrix)**：
  给定 $m \times n$ 矩阵 $A$，将 $A$ 的行与列互换得到的 $n \times m$ 矩阵称为 $A$ 的**转置 (Transpose)**，记作 $A^T$。其元素满足 $(A^T)_{ij} = a_{ji}$。
* **转置的代数性质 (Theorem 3)**：
  1. $(A^T)^T = A$
  2. $(A + B)^T = A^T + B^T$
  3. $(rA)^T = r A^T$
  4. $(AB)^T = B^T A^T$ （**穿脱原则：乘积转置等于次序颠倒后各自转置相乘**）
* **对称矩阵 (Symmetric Matrix)**：
  若方阵 $A$ 满足 $A^T = A$，则称 $A$ 为**对称矩阵**。对角矩阵均为对称矩阵。

---

#### 🌟 课件随堂例题与解析 (Lecture Examples)

###### 【课件例题 1】按定义计算矩阵乘法
**Problem**: Compute $AB$ for $A = \begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 3 & 6 \\ 1 & -2 & 3 \end{bmatrix}$.

* **Process (解题步骤)**:
  Let $B = \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \mathbf{b}_3 \end{bmatrix}$. Compute each column of $AB = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & A\mathbf{b}_3 \end{bmatrix}$:
  - $A\mathbf{b}_1 = 4\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 3 \\ -5 \end{bmatrix} = \begin{bmatrix} 8 + 3 \\ 4 - 5 \end{bmatrix} = \begin{bmatrix} 11 \\ -1 \end{bmatrix}$
  - $A\mathbf{b}_2 = 3\begin{bmatrix} 2 \\ 1 \end{bmatrix} - 2\begin{bmatrix} 3 \\ -5 \end{bmatrix} = \begin{bmatrix} 6 - 6 \\ 3 + 10 \end{bmatrix} = \begin{bmatrix} 0 \\ 13 \end{bmatrix}$
  - $A\mathbf{b}_3 = 6\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 3\begin{bmatrix} 3 \\ -5 \end{bmatrix} = \begin{bmatrix} 12 + 9 \\ 6 - 15 \end{bmatrix} = \begin{bmatrix} 21 \\ -9 \end{bmatrix}$
  
  Therefore, $AB = \begin{bmatrix} 11 & 0 & 21 \\ -1 & 13 & -9 \end{bmatrix}$.
* **中文详解**:
  按照矩阵乘法的列定义法，将 $B$ 的三列分别作为权重与 $A$ 的列作线性组合，得到 $AB$ 的三个列向量。

---

###### 【课件例题 2】矩阵乘法的非交换性验证
**Problem**: Let $A = \begin{bmatrix} 5 & 1 \\ 3 & -2 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 0 \\ 4 & 3 \end{bmatrix}$. Compute $AB$ and $BA$.

* **Process (解题步骤)**:
  $$AB = \begin{bmatrix} 5 & 1 \\ 3 & -2 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 4 & 3 \end{bmatrix} = \begin{bmatrix} 5(2)+1(4) & 5(0)+1(3) \\ 3(2)+(-2)(4) & 3(0)+(-2)(3) \end{bmatrix} = \begin{bmatrix} 14 & 3 \\ -2 & -6 \end{bmatrix}$$
  $$BA = \begin{bmatrix} 2 & 0 \\ 4 & 3 \end{bmatrix} \begin{bmatrix} 5 & 1 \\ 3 & -2 \end{bmatrix} = \begin{bmatrix} 2(5)+0(3) & 2(1)+0(-2) \\ 4(5)+3(3) & 4(1)+3(-2) \end{bmatrix} = \begin{bmatrix} 10 & 2 \\ 29 & -2 \end{bmatrix}$$
  Notice $AB \neq BA$.
* **中文详解**:
  计算表明 $AB \neq BA$，这具体说明了矩阵乘法一般情况下不满足交换律。

---

### Section 2.2 矩阵的逆 (The Inverse of a Matrix)

#### 1. 动机与定义 (Motivation and Definition)
* **动机 (Motivation)**：
  在实数乘法中，非零实数 $a$ 存在倒数 $a^{-1} = \frac{1}{a}$ 满足 $a \cdot a^{-1} = 1$，从而可以定义除法 $b \div a = b \cdot a^{-1}$。
  对于矩阵，单位矩阵 $I$ 充当数字 1 的角色。为了使双侧逆矩阵 $CA = I_m$ 且 $AC = I_n$ 有意义，矩阵必须是**方阵 (Square Matrix)**（即 $m = n$）。
* **可逆与逆矩阵的定义 (Invertible & Inverse)**：
  一个 $n \times n$ 方阵 $A$ 被称为是**可逆的 (Invertible)**（或**非奇异的 / Nonsingular**），如果存在一个 $n \times n$ 方阵 $C$ 满足：
  $$CA = I_n \quad \text{且} \quad AC = I_n$$
  此时称 $C$ 为 $A$ 的一个**逆矩阵 (Inverse)**。
  不可逆的方阵称为**奇异矩阵 (Singular Matrix)**。
* **逆矩阵的唯一性 (Uniqueness of Inverse)**：
  若 $A$ 是可逆矩阵，则其逆矩阵是**唯一的**。唯一性允许我们将 $A$ 的逆矩阵无歧义地记为 $A^{-1}$。
  * **证明 (Proof of Uniqueness)**：
    假设 $B$ 和 $C$ 都是 $A$ 的逆矩阵，利用矩阵乘法结合律与单位矩阵性质：
    $$B = B I_n = B(AC) = (BA)C = I_n C = C$$
    故 $B = C$。

---

#### 2. $2 \times 2$ 矩阵的求逆公式 (Inverse of a $2 \times 2$ Matrix - Theorem 4)
* **定理 (Theorem 4)**：
  设 $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$。定义 $A$ 的**行列式 (Determinant)** 为：
  $$\text{det} A = ad - bc$$
  - 若 $\text{det} A = ad - bc \neq 0$，则 $A$ 是**可逆的**，且其逆矩阵公式为：
    $$A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
  - 若 $\text{det} A = ad - bc = 0$，则 $A$ 是**不可逆的 (Singular)**。

* **记忆口诀**：主对角线元素对调（$a, d$ 互换），副对角线元素变号（$b, c$ 变为 $-b, -c$），再除以行列式 $\text{det} A$。

---

#### 3. 线性方程组与逆矩阵 (Linear Systems & Invertible Matrix - Theorem 5)
* **定理 (Theorem 5)**：
  若 $A$ 是可逆的 $n \times n$ 方阵，则对于 $\mathbb{R}^n$ 中的任意向量 $\mathbf{b}$，矩阵方程 $A\mathbf{x} = \mathbf{b}$ 拥有**唯一解**，其表达式为：
  $$\mathbf{x} = A^{-1}\mathbf{b}$$
* **证明 (Proof)**：
  - **解的存在性**：将 $\mathbf{x} = A^{-1}\mathbf{b}$ 代入方程：
    $$A(A^{-1}\mathbf{b}) = (A A^{-1})\mathbf{b} = I_n \mathbf{b} = \mathbf{b}$$
    故 $A^{-1}\mathbf{b}$ 确实是方程的一个解。
  - **解的唯一性**：假设 $\mathbf{y}$ 也是方程的解，即 $A\mathbf{y} = \mathbf{b}$。方程两侧左乘 $A^{-1}$：
    $$A^{-1}(A\mathbf{y}) = A^{-1}\mathbf{b} \implies (A^{-1}A)\mathbf{y} = A^{-1}\mathbf{b} \implies I_n \mathbf{y} = A^{-1}\mathbf{b} \implies \mathbf{y} = A^{-1}\mathbf{b}$$
    故解是唯一的。

* **应用提示**：Theorem 5 主要用于理论证明推导。在具体计算数值方程 $A\mathbf{x} = \mathbf{b}$ 时，对增广矩阵 $[A \mid \mathbf{b}]$ 进行高斯消元求 RREF 比直接求 $A^{-1}$ 更高效。

---

#### 🌟 课件随堂例题与解析 (Lecture Examples)

###### 【课件例题 3】求 $2 \times 2$ 矩阵的逆并求解线性方程组
**Problem**:
(a) Find the inverse of $A = \begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix}$ (if it exists).  
(b) Use $A^{-1}$ to solve the linear system: $\begin{cases} 3x_1 + 4x_2 = 3 \\ 5x_1 + 6x_2 = 7 \end{cases}$.

* **Process (解题步骤)**:  
  (a) Compute the determinant of $A$:
  $$\text{det} A = (3)(6) - (4)(5) = 18 - 20 = -2 \neq 0$$
  Since $\text{det} A \neq 0$, $A$ is invertible. By Theorem 4:
  $$A^{-1} = \frac{1}{-2} \begin{bmatrix} 6 & -4 \\ -5 & 3 \end{bmatrix} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix}$$

  (b) Write the linear system as $A\mathbf{x} = \mathbf{b}$, where $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} 3 \\ 7 \end{bmatrix}$. By Theorem 5, the unique solution is:
  $$\mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix} \begin{bmatrix} 3 \\ 7 \end{bmatrix} = \begin{bmatrix} -3(3) + 2(7) \\ \frac{5}{2}(3) - \frac{3}{2}(7) \end{bmatrix} = \begin{bmatrix} -9 + 14 \\ \frac{15 - 21}{2} \end{bmatrix} = \begin{bmatrix} 5 \\ -3 \end{bmatrix}$$
  So $x_1 = 5, x_2 = -3$.

* **中文详解**:
  (a) 首先计算行列式 $\text{det} A = -2 \neq 0$，确认矩阵可逆。套用 $2 \times 2$ 矩阵求逆公式，主对角线对调，副对角线变号并乘以 $-1/2$，得到 $A^{-1}$。  
  (b) 将方程组写成 $A\mathbf{x} = \mathbf{b}$ 形式，利用 Theorem 5 计算 $\mathbf{x} = A^{-1}\mathbf{b}$，直接求得唯一解 $x_1 = 5, x_2 = -3$。

---

💡 **学习建议与复习提示**：
* 熟练掌握矩阵乘法的**列组合视角**与**行内积法则**，并牢记乘法三大避坑规则（不满足交换律、无消去律、存在零因子）。
* 掌握转置乘积的穿脱原则 $(AB)^T = B^T A^T$。
* 牢记 $2 \times 2$ 矩阵求逆公式 $A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ 及唯一解公式 $\mathbf{x} = A^{-1}\mathbf{b}$。
