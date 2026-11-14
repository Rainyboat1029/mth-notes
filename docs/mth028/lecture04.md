# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 1.5 & 1.7 线性方程组的解集与线性无关 (Solution Sets of Linear Systems & Linear Independence)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 4 Summary)

### Section 1.5 线性方程组的解集 (Solution Sets of Linear Systems)

#### 1. 齐次线性方程组 (Homogeneous Linear Systems)
* **概念定义 (Definition)**：  
  形如 $A\mathbf{x} = \mathbf{0}$ 的线性方程组称为**齐次线性方程组 (Homogeneous Linear System)**，其中 $A$ 为 $m \times n$ 矩阵，$\mathbf{0} \in \mathbb{R}^m$ 为零向量。
* **平凡解与非平凡解 (Trivial & Nontrivial Solutions)**：
  1. **平凡解 (Trivial Solution)**：$\mathbf{x} = \mathbf{0} \in \mathbb{R}^n$ 永远是齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的一个解。因此，齐次方程组**必然是相容的 (Always Consistent)**。
  2. **非平凡解 (Nontrivial Solution)**：满足 $A\mathbf{x} = \mathbf{0}$ 的**非零向量** $\mathbf{x} \neq \mathbf{0}$ 称为非平凡解。
* **解集的线性组合封闭性 (Property)**：  
  若 $\mathbf{u}$ 和 $\mathbf{v}$ 是齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的解，则对任意实数 $c_1, c_2 \in \mathbb{R}$，它们的任意线性组合 $c_1\mathbf{u} + c_2\mathbf{v}$ 仍然是 $A\mathbf{x} = \mathbf{0}$ 的解。
* **非平凡解的存在性定理 (Existence of Nontrivial Solutions)**：  
  齐次方程组 $A\mathbf{x} = \mathbf{0}$ 存在非平凡解 **当且仅当** 该方程组包含**至少一个自由变量 (At least one free variable)**。
  * **推导逻辑**：存在非平凡解 $\iff$ 存在无穷多个解 $\iff$ 系数矩阵化简后存在非主元列（自由变量）。

---

#### 2. 参数向量形式与几何解释 (Parametric Vector Form & Geometric Interpretation)

* **参数向量形式 (Parametric Vector Form)**：  
  当方程组有无穷多个解时，将通解表示为由自由变量作为参数的向量线性组合形式：
  $$\mathbf{x} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_p\mathbf{v}_p \quad (c_1, \dots, c_p \in \mathbb{R})$$
  这种表达方式称为解集的**参数向量形式**。
* **齐次解集的几何解释 (Geometric Interpretation in $\mathbb{R}^3$)**：
  1. **只有一个自由变量**：通解可写为 $\mathbf{x} = t\mathbf{v}$ ($t \in \mathbb{R}$)，在几何上表示 $\mathbb{R}^3$ 中**穿过原点 $\mathbf{0}$ 的一条直线** ($\text{Span}\{\mathbf{v}\}$)。
  2. **有两个自由变量**：通解可写为 $\mathbf{x} = s\mathbf{u} + t\mathbf{v}$ ($s, t \in \mathbb{R}$)，在几何上表示 $\mathbb{R}^3$ 中**穿过原点 $\mathbf{0}$ 的一个平面** ($\text{Span}\{\mathbf{u}, \mathbf{v}\}$)。

---

#### 3. 非齐次线性方程组 (Nonhomogeneous Linear Systems)

* **概念定义**：  
  当 $\mathbf{b} \neq \mathbf{0}$ 时，方程组 $A\mathbf{x} = \mathbf{b}$ 称为**非齐次线性方程组 (Nonhomogeneous Linear System)**。
* **非齐次解结构定理 (Theorem 6 - Solution Structure Theorem)**：  
  假设非齐次方程组 $A\mathbf{x} = \mathbf{b}$ 对某个给定的 $\mathbf{b}$ 是**相容的 (Consistent)**，设 $\mathbf{p}$ 为该方程组的一个**特解 (Particular Solution)**。则 $A\mathbf{x} = \mathbf{b}$ 的**全解集**由下式给出：
  $$\mathbf{x} = \mathbf{p} + \mathbf{v}_h$$
  其中 $\mathbf{v}_h$ 是对应的齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的**任意解 (Any Homogeneous Solution)**。
  $$\text{非齐次通解 } \mathbf{x} = \text{一个非齐次特解 } \mathbf{p} + \text{齐次通解 } \mathbf{v}_h$$

* **几何解释：平移 (Translation)**：  
  在几何上，非齐次方程组 $A\mathbf{x} = \mathbf{b}$ 的解集是将齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的解集（过原点的直线或平面）沿向量 $\mathbf{p}$ 进行**平行移动 (Translation)** 得到的**平行直线或平行平面**。

* **求参数向量形式的标准步骤 (Algorithm)**：
  1. 将增广矩阵 $[A \mid \mathbf{b}]$ 行化简至**简化行阶梯形 (RREF)**。
  2. 将每个主变量用自由变量（若存在）表示出来。
  3. 将通用解向量 $\mathbf{x}$ 写成分量形式，并拆分为不含自由变量的常数向量 $\mathbf{p}$ 与含自由变量的齐次部分组合。

---

#### 🌟 课件随堂例题与解析 (Lecture Examples)

###### 【课件例题 1】齐次方程组的求解与几何描述
**Problem**: Describe the solution set of $3x_1 + 5x_2 - 4x_3 = 0, -3x_1 - 2x_2 + 4x_3 = 0, 6x_1 + x_2 - 8x_3 = 0$.

* **Process (解题步骤)**:
  Set up the augmented matrix for $A\mathbf{x} = \mathbf{0}$ and reduce to RREF:
  $$\begin{bmatrix} 3 & 5 & -4 & 0 \\ -3 & -2 & 4 & 0 \\ 6 & 1 & -8 & 0 \end{bmatrix} \xrightarrow{R_2 \leftarrow R_2 + R_1, R_3 \leftarrow R_3 - 2R_1} \begin{bmatrix} 3 & 5 & -4 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & -9 & 0 & 0 \end{bmatrix}$$
  $$\xrightarrow{R_2 \leftarrow \frac{1}{3}R_2, R_3 \leftarrow R_3 + 3R_2} \begin{bmatrix} 3 & 5 & -4 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow{R_1 \leftarrow R_1 - 5R_2} \begin{bmatrix} 3 & 0 & -4 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
  $$\xrightarrow{R_1 \leftarrow \frac{1}{3}R_1} \begin{bmatrix} 1 & 0 & -4/3 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
  Thus, $x_1 = \frac{4}{3}x_3$, $x_2 = 0$, with $x_3$ free.
  In parametric vector form:
  $$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_3 \begin{bmatrix} 4/3 \\ 0 \\ 1 \end{bmatrix} \quad (x_3 \in \mathbb{R})$$
  Geometrically, the solution set is $\text{Span}\left\{\begin{bmatrix} 4/3 \\ 0 \\ 1 \end{bmatrix}\right\}$, which is a **line through the origin** in $\mathbb{R}^3$.
* **中文详解**:  
  通过对齐次方程组增广矩阵化简得到 RREF，确定主变量为 $x_1, x_2$，自由变量为 $x_3$。求得通解的参数向量形式，其几何意义为 $\mathbb{R}^3$ 中一条穿过原点的直线。

---

### Section 1.7 线性无关 (Linear Independence)

#### 1. 概念定义与向量方程 (Definitions & Vector Equation)

* **线性无关 (Linearly Independent)**：  
  $\mathbb{R}^n$ 中的一组有序向量集合 $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\}$ 称为**线性无关的**，如果向量方程：
  $$x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \dots + x_p\mathbf{v}_p = \mathbf{0}$$
  **只有平凡解 (Only the trivial solution)** $x_1 = x_2 = \dots = x_p = 0$。

* **线性相关 (Linearly Dependent)**：  
  如果存在**不全为零的标量 (Weights not all zero)** $c_1, c_2, \dots, c_p$，使得：
  $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_p\mathbf{v}_p = \mathbf{0}$$
  则称该向量集合 $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\}$ 是**线性相关的**。上式称为向量间的**线性相关关系 (Linear Dependence Relation)**。

---

#### 2. 矩阵列向量的线性无关性 (Independence of Matrix Columns)

* **重要等价定理 (Theorem for Matrix Columns)**：  
  矩阵 $A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n \end{bmatrix}$ 的列向量组是线性无关的，**当且仅当**矩阵方程 $A\mathbf{x} = \mathbf{0}$ 满足以下逻辑等价条件：
  1. $A\mathbf{x} = \mathbf{0}$ **只有平凡解 (Only the trivial solution)**；
  2. $A\mathbf{x} = \mathbf{0}$ **没有自由变量 (No free variables)**；
  3. 矩阵 $A$ 的**每一列都是主元列 (Every column of $A$ is a pivot column)**。

---

#### 3. 特殊情形与判定定理 (Special Cases & Characterization Theorems)

* **单向量集合 ($p = 1$)**：  
  * 包含单个向量的集合 $\{\mathbf{v}\}$ 线性无关 $\iff \mathbf{v} \neq \mathbf{0}$。
  * 集合 $\{\mathbf{0}\}$ 是线性相关的。

* **双向量集合 ($p = 2$)**：  
  * 包含两个向量的集合 $\{\mathbf{v}_1, \mathbf{v}_2\}$ 线性无关 $\iff$ **没有任何一个向量是另一个向量的数量倍 (Neither vector is a scalar multiple of the other)**。

* **线性相关集合的特征定理 (Theorem 7 - Characterization of Linearly Dependent Sets)**：  
  包含两个或更多向量的集合 $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\}$ ($p \ge 2$) 是线性相关的，**当且仅当** $S$ 中**至少存在一个向量是其余向量的线性组合**。
  * *更精准表述*：若 $S$ 线性相关且 $\mathbf{v}_1 \neq \mathbf{0}$，则至少存在一个向量 $\mathbf{v}_j$ ($j \ge 2$) 可以表示为前面向量 $\mathbf{v}_1, \dots, \mathbf{v}_{j-1}$ 的线性组合。

* **定理 8 ($p > n$ 必相关)**：  
  如果一个向量集合包含的**向量个数 $p$ 大于每个向量的分量维度 $n$**（即 $p > n$），则该集合 $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\} \subset \mathbb{R}^n$ **必然是线性相关的**。
  * *证明要点*：构造矩阵 $A \in \mathbb{R}^{n \times p}$，主元个数最多为 $n$。因为 $p > n$，必定有至少 $p - n > 0$ 个自由变量，故 $A\mathbf{x} = \mathbf{0}$ 必有非平凡解。

* **定理 9 (含零向量必相关)**：  
  如果向量集合 $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\} \subset \mathbb{R}^n$ **包含零向量 $\mathbf{0}$**，则该集合**必然是线性相关的**。
  * *证明要点*：若 $\mathbf{v}_j = \mathbf{0}$，可取权重 $c_j = 1 \neq 0$，其余权重全为 0，得到 $0\mathbf{v}_1 + \dots + 1\mathbf{0} + \dots + 0\mathbf{v}_p = \mathbf{0}$。

---

## 总结与解的唯一性联系 (Summary & Connection to Uniqueness)

对于线性方程组 $A\mathbf{x} = \mathbf{b}$（其中 $A = [\mathbf{a}_1 \; \mathbf{a}_2 \; \dots \; \mathbf{a}_p]$）：
1. **解的存在性 (Existence)**：$A\mathbf{x} = \mathbf{b}$ 相容 $\iff \mathbf{b} \in \text{Span}\{\mathbf{a}_1, \dots, \mathbf{a}_p\}$。
2. **解的唯一性 (Uniqueness)**：在相容前提下，解是唯一的 $\iff A\mathbf{x} = \mathbf{0}$ 只有平凡解 $\iff A$ 的列向量组 $\mathbf{a}_1, \dots, \mathbf{a}_p$ **线性无关**（即无自由变量）。
