# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 2.2 (续) & 2.3 矩阵的逆与可逆矩阵定理 (The Inverse of a Matrix & Characterizations of Invertible Matrices)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 7 Summary)

### Section 2.2 矩阵的逆 (续) (The Inverse of a Matrix - Continued)

#### 1. 可逆矩阵的基本性质 (Properties of Invertible Matrices)
设 $A$ 和 $B$ 为 $n \times n$ 可逆矩阵，则有以下基本运算性质：

* **定理 6 (Theorem 6)**：
  1. 若 $A$ 可逆，则 $A^{-1}$ 也可逆，且：
     $$(A^{-1})^{-1} = A$$
  2. 若 $A$ 和 $B$ 均为 $n \times n$ 可逆矩阵，则 $AB$ 也可逆，且其逆矩阵为因子逆矩阵的**反向乘积**：
     $$(AB)^{-1} = B^{-1}A^{-1}$$
     *推广*：对多个可逆矩阵 $A_1, A_2, \dots, A_p$，有 $(A_1 A_2 \dots A_p)^{-1} = A_p^{-1} \dots A_2^{-1} A_1^{-1}$。
  3. 若 $A$ 可逆，则其转置矩阵 $A^T$ 也可逆，且 $A^T$ 的逆等于 $A^{-1}$ 的转置：
     $$(A^T)^{-1} = (A^{-1})^T$$

* ⚠️ **重要易错点**：
  * **乘积可逆的顺规**：$(AB)^{-1} = B^{-1}A^{-1}$，顺规不可随意颠倒。
  * **和的可逆性**：若 $A$ 与 $B$ 均可逆，$A + B$ **不一定**可逆！例如 $A = I_n, B = -I_n$，两者均可逆，但 $A + B = O$ 奇异不可逆。
  * **负整数幂定义**：对于正整数 $k$，定义 $A^{-k} = (A^{-1})^k = (A^k)^{-1}$。

---

#### 2. 初等矩阵 (Elementary Matrices)
* **概念定义 (Definition)**：
  对单位矩阵 $I_n$ 执行**一次初等行变换**所得到的矩阵称为**初等矩阵 (Elementary Matrix)**，通常记为 $E$。

* **三种初等矩阵示例 (3 Types in $\mathbb{R}^3$)**：
  1. **倍加型 (Replacement)**：$R_3 \leftarrow R_3 + 4R_1 \implies E_1 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix}$
  2. **对换型 (Interchange)**：$R_1 \leftrightarrow R_2 \implies E_2 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
  3. **倍乘型 (Scaling)**：$R_3 \leftarrow 5R_3 \implies E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5 \end{bmatrix}$

* **左乘初等矩阵的作用 (Left-Multiplication Property)**：
  若对 $m \times n$ 矩阵 $A$ 执行某种初等行变换，其结果完全等价于**用同种行变换作用于 $I_m$ 所得的初等矩阵 $E$ 从左侧乘以 $A$**，即：
  $$\text{变换后的矩阵} = EA$$

* **初等矩阵的可逆性 (Invertibility of Elementary Matrices)**：
  由于每种初等行变换都是可逆的，因此**每一个初等矩阵 $E$ 都是可逆矩阵**，且 $E^{-1}$ 就是对 $I$ 执行对应**逆行变换**得到的初等矩阵。
  * 例如，$E_1^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$，$E_2^{-1} = E_2$，$E_3^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/5 \end{bmatrix}$。

---

#### 3. 行等价与求逆算法 (Row Equivalence & Inversion Algorithm)

* **定理 7 (Theorem 7)**：
  $n \times n$ 方阵 $A$ 是可逆矩阵，**当且仅当** $A$ 与单位矩阵 $I_n$ **行等价**（即 $A \sim I_n$）。
  此时，将 $A$ 化为 $I_n$ 的一连串初等行变换，恰好能将 $I_n$ 转化为 $A^{-1}$。

* **初等矩阵乘积表示**：
  若存在初等矩阵使 $E_p \dots E_1 A = I_n$，则：
  $$A^{-1} = E_p \dots E_1, \quad A = (E_p \dots E_1)^{-1} = E_1^{-1} \dots E_p^{-1}$$
  这表明：**任何一个可逆矩阵都可以表示为一系列初等矩阵的乘积**。

* **求逆矩阵的高斯-若尔当算法 (Algorithm for Finding $A^{-1}$)**：
  1. 构造增广矩阵 $[A \mid I_n]$。
  2. 对增广矩阵应用初等行变换求其 RREF：
     * 若 $A \sim I_n$，则有 $[A \mid I_n] \sim [I_n \mid A^{-1}]$，右侧即为 $A^{-1}$。
     * 若 $A$ 不能化为 $I_n$（即主元个数 $< n$），则 $A$ 不可逆（奇异）。

---

### Section 2.3 可逆矩阵定理 (Characterizations of Invertible Matrices)

#### 1. 可逆矩阵定理 (The Invertible Matrix Theorem, IMT - Theorem 8)
设 $A$ 为 $n \times n$ 方阵，则下列 12 个命题在逻辑上是**完全等价的 (Logically Equivalent)**：

a. $A$ 是可逆矩阵 (Invertible Matrix)。  
b. $A$ 行等价于 $n \times n$ 单位矩阵 $I_n$ ($A \sim I_n$)。  
c. $A$ 拥有 $n$ 个主元位置 (Pivot Positions)。  
d. 齐次方程 $A\mathbf{x} = \mathbf{0}$ 只有平凡解 ($\mathbf{x} = \mathbf{0}$)。  
e. $A$ 的列向量集形成线性无关集 (Linearly Independent Set)。  
f. 线性变换 $\mathbf{x} \mapsto A\mathbf{x}$ 是单射 / 一对一的 (One-to-One)。  
g. 对 $\mathbb{R}^n$ 中的每个向量 $\mathbf{b}$，方程 $A\mathbf{x} = \mathbf{b}$ 至少有一个解（即必相容）。  
h. $A$ 的列向量集张成整个 $\mathbb{R}^n$ ($\text{Span}\{\mathbf{a}_1, \dots, \mathbf{a}_n\} = \mathbb{R}^n$)。  
i. 线性变换 $\mathbf{x} \mapsto A\mathbf{x}$ 是满射 / 映上的 (Onto $\mathbb{R}^n$)。  
j. 存在 $n \times n$ 矩阵 $C$ 使得 $CA = I_n$（存在左逆）。  
k. 存在 $n \times n$ 矩阵 $D$ 使得 $AD = I_n$（存在右逆）。  
l. $A^T$ 是可逆矩阵。

---

#### 2. IMT 的核心推论 (Corollaries of IMT)

1. **单边逆即双边逆 (One-sided inverse implies two-sided inverse)**：  
   对于 $n \times n$ **方阵** $A$ 和 $B$，只要满足 $AB = I_n$ 或 $BA = I_n$ 之一，即可直接推出 $B = A^{-1}$（无需同时验证两个等式）。
2. **乘积可逆充要条件**：  
   设 $A, B$ 为 $n \times n$ 方阵，$AB$ 可逆 **当且仅当** $A$ 与 $B$ **均可逆**。

---

#### 3. 奇异矩阵的等价条件 (Singular Matrices - Negations)
若 $n \times n$ 方阵 $A$ 是**奇异矩阵 (Singular Matrix)**（即不可逆），则否定 IMT 的所有条款：
* $A$ 主元个数 $< n$（存在非主元列 / 自由变量）。
* $A\mathbf{x} = \mathbf{0}$ 有非平凡解。
* $A$ 的列向量线性相关，且无法张成 $\mathbb{R}^n$。
* 矩阵变换 $\mathbf{x} \mapsto A\mathbf{x}$ 既不是单射，也不是满射。

---

#### 4. 可逆线性变换 (Invertible Linear Transformations)
* **定义 (Definition)**：  
  线性变换 $T: \mathbb{R}^n \to \mathbb{R}^n$ 称为可逆的，若存在映射 $S: \mathbb{R}^n \to \mathbb{R}^n$ 使得对任意 $\mathbf{x} \in \mathbb{R}^n$ 均有：
  $$S(T(\mathbf{x})) = \mathbf{x} \quad \text{且} \quad T(S(\mathbf{x})) = \mathbf{x}$$
  此时 $S$ 是唯一的线性变换，记作 $T^{-1}$。

* **定理 9 (Theorem 9)**：  
  设 $T: \mathbb{R}^n \to \mathbb{R}^n$ 是线性变换，$A$ 为其标准矩阵。则：  
  $$T \text{ 可逆} \Longleftrightarrow A \text{ 可逆}$$  
  当 $T$ 可逆时，$T^{-1}$ 的标准矩阵恰为 $A^{-1}$，即 $T^{-1}(\mathbf{x}) = A^{-1}\mathbf{x}$。

---

💡 **学习建议与复习提示**：  
* 牢记初等矩阵与初等行变换的左乘对应关系，$EA$ 代表对 $A$ 执行 $E$ 所对应的行变换。  
* 高斯-若尔当求逆算法 $[A \mid I] \sim [I \mid A^{-1}]$ 是期中与期末考试必考的计算技能。  
* **IMT (Invertible Matrix Theorem)** 是前两章概念的“大一统定理”，务必建立“可逆 $\leftrightarrow$ 满主元 $\leftrightarrow$ 齐次解唯一 $\leftrightarrow$ 列线性无关 $\leftrightarrow$ 列张成 $\mathbb{R}^n \leftrightarrow$ 单射且满射”的联动思维。
