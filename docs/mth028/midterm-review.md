# MTH028 Linear Algebra 期中复习笔记 (Midterm Review Notes): Lectures 1–8（1.1–2.8）核心知识详解与典型例题

> **范围**：Lecture 1–8，即 §1.1–1.9 与 §2.1–2.3、§2.8。Lecture 9（§2.9）不在本次期中范围。
> **配套**：《Week 1–8 练习册》50 题 + 解析册；《综合提高卷》20 题 + 解析册；两份交互答题卡。
> **用法**：先看第零部分术语表建立词汇，再按 Lecture 顺序过正文，最后用附录的「十大易错点」做考前自检。

---

## 第零部分：核心术语速查表 (Key Terminology Table)

### 0.1 线性方程组与矩阵 (Systems & Matrices)

| 英文 | 中文 | 一句话解释 | 关键判据 |
|---|---|---|---|
| linear equation | 线性方程 | $a_1x_1+\cdots+a_nx_n=b$，未知数只以一次幂单独出现 | 出现根号/乘积/函数 ⇒ 不是线性 |
| system of linear equations | 线性方程组 | 若干线性方程联立 | — |
| solution / solution set | 解 / 解集 | 同时满足所有方程的一组数 / 全部解的集合 | 三种情形：无解、唯一解、无穷多解 |
| consistent / inconsistent | 相容 / 不相容 | 至少有一个解 / 没有解 | 阶梯形出现 $[0\cdots0\mid b],\ b\neq0$ ⇒ 不相容 |
| equivalent systems | 等价方程组 | 解集相同的两个方程组 | 初等行变换保持解集 |
| augmented matrix | 增广矩阵 | 系数矩阵右侧拼上常数列 | 最后一行对应常数项 |
| coefficient matrix | 系数矩阵 | 只含系数 | — |
| elementary row operation | 初等行变换 | 交换两行、某行乘非零常数、某行加另一行的倍数 | 一次只动**一行**、用**同一时刻**的其他行 |
| row equivalent | 行等价 | 可通过有限次初等行变换互相转化 | 行等价 ⇒ 解集相同 |
| echelon form (REF) | 阶梯形 | 零行在底、主元逐行右移、主元列下方全 0 | 主元上方可以有非零元 |
| reduced echelon form (RREF) | 简化阶梯形 | REF + 主元全为 1 + 主元列其余（含上方）全为 0 | 主元列"干净" |
| pivot position / pivot column | 主元位置 / 主元列 | REF 中主元所在的位置 / 列 | 行化简后数主元个数（= 非零行数） |
| free variable | 自由变量 | 非主元列对应的未知数 | 个数 = 列数 − 主元个数 |
| parametric description | 参数表示 | 用自由变量表示全部解 | 见 §1.5 |

### 0.2 向量与子空间 (Vectors & Subspaces)

| 英文 | 中文 | 一句话解释 | 关键判据 |
|---|---|---|---|
| linear combination | 线性组合 | $c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p$ | 系数可任取实数 |
| Span | 张成（空间） | 所有线性组合的集合 | 含 $\mathbf{0}$；对加法、数乘封闭 |
| linearly independent | 线性无关 | 只有全零系数才能组合出 $\mathbf{0}$ | 矩阵每列都有主元 |
| linearly dependent | 线性相关 | 存在不全为零的系数组合出 $\mathbf{0}$ | 有自由变量 / 某列是其余列的组合 |
| trivial / nontrivial solution | 平凡解 / 非平凡解 | $\mathbf{x}=\mathbf{0}$ / $\mathbf{x}\neq\mathbf{0}$ 的齐次解 | 齐次方程必有平凡解 |
| homogeneous / nonhomogeneous | 齐次 / 非齐次 | 右端为 $\mathbf{0}$ / 不为 $\mathbf{0}$ | 齐次必相容 |
| subspace | 子空间 | 含 $\mathbf{0}$ 且对加法、数乘封闭的集合 | 三条件缺一不可 |
| Nul $A$ (null space) | 零空间 | $\{\mathbf{x}:A\mathbf{x}=\mathbf{0}\}$ | 是 $\mathbb{R}^n$ 的子空间 |
| Col $A$ (column space) | 列空间 | $A$ 各列的全部线性组合 | 是 $\mathbb{R}^m$ 的子空间 |
| basis | 基 | 既无关又张成的向量组 | 基向量个数 = 维数 |
| dimension / nullity | 维数 / 零化度 | 基中向量的个数 / $\dim\operatorname{Nul}A$ | $\dim\operatorname{Nul}A$ = 非主元列的个数 |

### 0.3 线性变换与矩阵运算 (Transformations & Matrix Algebra)

| 英文 | 中文 | 一句话解释 | 关键判据 |
|---|---|---|---|
| linear transformation | 线性变换 | $T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v})$，$T(c\mathbf{u})=cT(\mathbf{u})$ | 等价于 $T(\mathbf{x})=A\mathbf{x}$ |
| standard matrix | 标准矩阵 | 第 $j$ 列是 $T(\mathbf{e}_j)$ | 尺寸 $m\times n$ |
| one-to-one (injective) | 单射 | $T(\mathbf{u})=T(\mathbf{v})\Rightarrow\mathbf{u}=\mathbf{v}$ | 每列有主元；$\operatorname{Nul}A=\{\mathbf{0}\}$ |
| onto (surjective) | 满射 | 值域 $=\mathbb{R}^m$ | 每行有主元；列张成 $\mathbb{R}^m$ |
| elementary matrix | 初等矩阵 | 对 $I$ 做一次初等行变换所得 | $E$ 左乘 $A$ = 对 $A$ 做同样的行变换 |
| invertible / singular | 可逆 / 奇异 | 存在 $A^{-1}$ 使 $AA^{-1}=A^{-1}A=I$ / 不存在 | 可逆 ⇔ $\det A\neq0$ ⇔ $A\sim I$（每列都有主元） |
| transpose | 转置 | 行列互换 | $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$，顺序反转 |
| Invertible Matrix Theorem (IMT) | 可逆矩阵定理 | 一组关于"$A$ 可逆"的等价命题 | 见 §2.3 |

---

## 第一部分：线性方程组与行化简 (Lectures 1–2: §1.1–1.2)

### 1.1 Systems of Linear Equations（线性方程组）

**核心对象.** 一个线性方程是 $a_1x_1+a_2x_2+\cdots+a_nx_n=b$。方程组就是若干个这样的式子联立。解的三种可能：**无解、唯一解、无穷多解**——只有这三种，不存在"恰好两个解"。

**为什么只有三种.** 解集是 $\mathbb{R}^n$ 中的仿射集：要么空，要么单点，要么含一条直线/平面（无穷多点）。几何直观：两个平面相交成一条线，再加一个平面要么切出一点、要么重合、要么平行。

**解法总纲（行化简）.**

1. 写出增广矩阵 $[A\ \mathbf{b}]$。
2. 用初等行变换化到 REF（够用时）或 RREF（求通解时）。
3. 读最后一行：若出现 $[0\ \cdots\ 0\ |\ c],\ c\neq0$ ⇒ **不相容**。
4. 否则主元个数决定解的形态：主元数 = 未知数个数 ⇒ 唯一解；主元数 < 未知数个数 ⇒ 无穷多解（自由变量个数 $=n-\text{主元数}$）。

**⚠ 陷阱.** 只看主元个数不看矛盾行。$2$ 个主元 + 一个 $[0\ 0\ 0\mid5]$ 的行是**无解**，不是"无穷多解"。

### 1.2 Row Reduction and Echelon Forms（行化简与阶梯形）

**初等行变换只有三种.**

1. 交换两行（$R_i\leftrightarrow R_j$）；
2. 某行乘一个非零常数（$R_i\leftarrow cR_i,\ c\neq0$）；
3. 某行加上另一行的倍数（$R_i\leftarrow R_i+cR_j$）。

**判定表（考试必考）.**

| 条件 | REF | RREF |
|---|---|---|
| 零行全在底部 | ✔ | ✔ |
| 每个非零行首元（主元）比上一行更靠右 | ✔ | ✔ |
| 主元所在列、主元**下方**全为 0 | ✔ | ✔ |
| 每个主元 = 1 | ✘ | ✔ |
| 主元所在列、主元**上方**也为 0 | ✘ | ✔ |

> 只满足前三行的是 REF；五条全满足才是 RREF。**典型失分**：把"主元是 1、零行在底部"当成 RREF，忽略主元列上方的非零元。

**存在唯一性定理（Theorem 2）.** 阶梯形中主元个数为 $r$、未知数个数为 $n$：

- 若某行是 $[0\ \cdots\ 0\ |\ c],\ c\neq0$ ⇒ 无解；
- 若 $r=n$ 且无矛盾行 ⇒ 唯一解；
- 若 $r<n$ 且无矛盾行 ⇒ 无穷多解。

**解题模板（求通解）.**

1. 化 RREF；
2. 主元变量用自由变量表示；
3. 写 $\mathbf{x}=\mathbf{p}+s_1\mathbf{v}_1+\cdots+s_k\mathbf{v}_k$：$\mathbf{p}$ 是自由变量全取 0 的特解，$\mathbf{v}_i$ 是第 $i$ 个自由变量取 1、其余取 0 的方向向量。

---

## 第二部分：向量方程与矩阵方程 (Lectures 3–4: §1.3–1.4)

### 1.3 Vector Equations（向量方程）

**定义.** $\mathbf{b}$ 是 $\mathbf{a}_1,\dots,\mathbf{a}_p$ 的**线性组合**，若存在 $c_1,\dots,c_p$ 使 $\mathbf{b}=c_1\mathbf{a}_1+\cdots+c_p\mathbf{a}_p$。所有这样的组合构成 $\operatorname{Span}\{\mathbf{a}_1,\dots,\mathbf{a}_p\}$。

**核心等价链（贯穿全章）.**

$$\mathbf{b}\in\operatorname{Span}\{\mathbf{a}_1,\dots,\mathbf{a}_p\}\iff[A\ \mathbf{b}]\ \text{相容}\iff c_1\mathbf{a}_1+\cdots+c_p\mathbf{a}_p=\mathbf{b}\ \text{有解}$$

**判断 $\mathbf{b}$ 是否在 span 中（考试标准流程）.**

1. 以 $\mathbf{a}_i$ 为列、$\mathbf{b}$ 为右端写增广矩阵；
2. 行化简；
3. 有矛盾行 ⇒ 不在；无矛盾行 ⇒ 在（并可写出系数）。

**Span 的几何.**

- 一个非零向量 ⇒ 过原点的直线；
- 两个不共线向量 ⇒ 过原点的平面；
- 含 $\mathbf{0}$ ⇒ span 一定含 $\mathbf{0}$（这也是判"能不能张成"的快速筛）。

**齐次方程.** $A\mathbf{x}=\mathbf{0}$ 永远相容（$\mathbf{x}=\mathbf{0}$）。参数形式 $\mathbf{x}=s\mathbf{v}_1+t\mathbf{v}_2$ 表示一个过原点的子空间。

### 1.4 The Matrix Equation $A\mathbf{x}=\mathbf{b}$

**乘法规则.** $A\mathbf{x}=\sum_j x_j\mathbf{a}_j$：**右乘向量 = 各列按 $x_j$ 加权求和**。这条把"矩阵方程"和"向量方程"焊在一起，几乎所有章节都靠它转换。

**Theorem 3（三说法等价）.** 对 $m\times n$ 矩阵 $A$ 与 $\mathbf{b}\in\mathbb{R}^m$：

1. $A\mathbf{x}=\mathbf{b}$ 有解；
2. $\mathbf{b}\in\operatorname{Col}A$；
3. $\mathbf{b}$ 是 $A$ 各列的线性组合。

**Theorem 4（列张成 $\mathbb{R}^m$）.** 下列等价：

1. $A$ 的各列张成 $\mathbb{R}^m$；
2. 对每个 $\mathbf{b}\in\mathbb{R}^m$，$A\mathbf{x}=\mathbf{b}$ 相容；
3. $A$ 的阶梯形每行都有主元（没有全零行）。

> 注意区分：**每行有主元** ⇒ 满射、列张成 $\mathbb{R}^m$；**每列有主元** ⇒ 单射、列无关。两者同时成立只有 $m=n$ 且每行每列都有主元时（即 $A\sim I$）。

---

## 第三部分：解集与线性无关 (Lectures 4–5: §1.5、§1.7)

### 1.5 Solution Sets of Linear Systems（解集）

**齐次方程的解集.** $A\mathbf{x}=\mathbf{0}$ 的解集 $\operatorname{Nul}A$ 一定含 $\mathbf{0}$，且对加法与数乘封闭 ⇒ 是子空间，写作 $\operatorname{Span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$，称为**零空间**。

**非齐次方程的解集.** 若 $A\mathbf{x}=\mathbf{b}$ 相容且 $\mathbf{p}$ 是一个特解，则

$$\{\mathbf{x}:A\mathbf{x}=\mathbf{b}\}=\mathbf{p}+\operatorname{Nul}A=\{\mathbf{p}+\mathbf{v}:\mathbf{v}\in\operatorname{Nul}A\}$$

即"**特解 + 齐次通解**"。

**几何描述（常考）.**

| 情形 | 解集形状 |
|---|---|
| 主元 $n$ 个（无自由变量）且相容 | 单点 |
| 主元 $n-1$ 个（1 个自由变量）且相容 | 直线（$\mathbf{b}\neq\mathbf{0}$ 时不过原点） |
| 主元 $n-2$ 个（2 个自由变量）且相容 | 平面 |
| 不相容 | 空集 |

**⚠ 陷阱.** $\mathbf{b}\neq\mathbf{0}$ 时解集**不过原点**——它是把 $\operatorname{Nul}A$ 整体平移 $\mathbf{p}$。

### 1.7 Linear Independence（线性无关）

**定义.** $\{\mathbf{v}_1,\dots,\mathbf{v}_p\}$ 线性无关 ⇔ $c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p=\mathbf{0}$ 只有 $c_1=\cdots=c_p=0$。否则称线性相关。

**矩阵判据（最好用）.** 以 $\mathbf{v}_i$ 为列得 $A$：无关 ⇔ $A\mathbf{x}=\mathbf{0}$ 只有零解 ⇔ **每列都有主元**。

**常用结论（直接背）.**

1. 含零向量的集合必相关。
2. 两个向量相关 ⇔ 一个是另一个的倍数。
3. $\mathbb{R}^n$ 中 $p>n$ 个向量必相关。
4. 相关集合的**超集**仍相关；无关集合的**子集**仍无关。
5. 若 $A$ 各列无关，则 $A\mathbf{x}=\mathbf{b}$ 至多一个解（解唯一表示）。

**⚠ 陷阱.** "3 个向量在 $\mathbb{R}^3$ 中就一定无关" —— 错。数量和维数相等既不保证无关，也不保证张成。

---

## 第四部分：线性变换 (Lectures 5–6: §1.8–1.9)

### 1.8 Introduction to Linear Transformations

**定义.** $T:\mathbb{R}^n\to\mathbb{R}^m$ 是线性的 ⇔ 保持加法与数乘：

$$T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}),\qquad T(c\mathbf{u})=cT(\mathbf{u})$$

**必考的推论.** $T(\mathbf{0})=\mathbf{0}$。任何把原点移走的映射（如 $T(\mathbf{x})=\mathbf{x}+\mathbf{b},\ \mathbf{b}\neq\mathbf{0}$）都**不是**线性变换。

**几何变换速查（$\mathbb{R}^2$）.**

| 变换 | 矩阵 |
|---|---|
| 逆时针旋转 $\theta$ | $\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$ |
| 关于 $x$ 轴反射 | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ |
| 关于 $y$ 轴反射 | $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ |
| 关于 $y=x$ 反射 | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ |
| 关于 $y=-x$ 反射 | $\begin{bmatrix}0&-1\\-1&0\end{bmatrix}$ |
| 沿 $x$ 方向伸缩 $k$ | $\begin{bmatrix}k&0\\0&1\end{bmatrix}$ |
| 剪切（shear） | $\begin{bmatrix}1&k\\0&1\end{bmatrix}$ |
| 投影到 $x$ 轴 | $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ |

### 1.9 The Matrix of a Linear Transformation

**标准矩阵.** 对线性变换 $T:\mathbb{R}^n\to\mathbb{R}^m$，

$$A=[\,T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\ \ \cdots\ \ T(\mathbf{e}_n)\,]$$

尺寸 $m\times n$：**行数 = 输出维数，列数 = 输入维数**。

**单射与满射（Theorem 11 / 12）.**

| 性质 | 主元条件 | 另一说法 |
|---|---|---|
| 单射 (one-to-one) | 每**列**有主元 | $\operatorname{Nul}A=\{\mathbf{0}\}$ |
| 满射 (onto) | 每**行**有主元 | $\operatorname{Col}A=\mathbb{R}^m$ |

**尺寸速判.** $m>n$（输出维数更高）⇒ 不可能满射；$m<n$ ⇒ 不可能单射；$m=n$ 时单射 ⇔ 满射 ⇔ 可逆。

**⚠ 陷阱.** 看题先看尺寸再看主元——很多题的答案靠尺寸就能排除一半选项。

---

## 第五部分：矩阵运算与逆矩阵 (Lectures 6–7: §2.1–2.3)

### 2.1 Matrix Operations（矩阵运算）

**乘法.** $(AB)_{ij}=$ $A$ 的第 $i$ 行与 $B$ 的第 $j$ 列的点积。要求 $A$ 的列数 = $B$ 的行数；结果尺寸 $=$ (行数 of $A$) × (列数 of $B$)。

**列视角（很常用）.** $AB$ 的第 $j$ 列 $=A\cdot(B$ 的第 $j$ 列$)$。

**性质.**

- $A(B+C)=AB+AC$，$(B+C)A=BA+CA$ ✔
- $A(BC)=(AB)C$ ✔
- $AB\neq BA$ 一般成立 ✘（**不交换**）
- $AB=0$ 不推出 $A=0$ 或 $B=0$ ✘（**无零因子律**）
- $(A+B)^2=A^2+AB+BA+B^2\neq A^2+2AB+B^2$（除非 $AB=BA$）
- $(A^{\mathsf T})^{\mathsf T}=A$，$(A+B)^{\mathsf T}=A^{\mathsf T}+B^{\mathsf T}$，$(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$ ← **顺序反转**

### 2.2 The Inverse of a Matrix（逆矩阵）

**定义.** $A$ 可逆 ⇔ 存在 $n\times n$ 的 $B$ 使 $AB=BA=I$；此时 $B=A^{-1}$ 唯一。

**$2\times2$ 公式（必须背熟）.**

$$A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\quad A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

口诀：**主对角互换、副对角变号、除以行列式**。

**逆的性质.**

$$(A^{-1})^{-1}=A,\qquad (AB)^{-1}=B^{-1}A^{-1},\qquad (A^{\mathsf T})^{-1}=(A^{\mathsf T})^{-1}= (A^{-1})^{\mathsf T}$$

（顺序反转是最高频失分点。）

**求逆算法.** $[A\ |\ I]\xrightarrow{\text{行变换}}[I\ |\ A^{-1}]$；若左边化不出 $I$，则 $A$ 奇异。

**初等矩阵.** 对 $I$ 做一次行变换得 $E$，则 $EA$ = 对 $A$ 做同样的行变换。每个初等矩阵都可逆，其逆是"反向操作"：

| 操作 | 逆操作 |
|---|---|
| 交换 $R_i,R_j$ | 再交换一次 |
| $R_i\leftarrow cR_i$ | $R_i\leftarrow\frac1cR_i$ |
| $R_i\leftarrow R_i+cR_j$ | $R_i\leftarrow R_i-cR_j$ |

**乘积求逆顺序.** $(E_1E_2E_3)^{-1}=E_3^{-1}E_2^{-1}E_1^{-1}$——**从右往左**逐个取逆。

### 2.3 Characterizations of Invertible Matrices（IMT）

对 $n\times n$ 矩阵 $A$，下列命题**全部等价**（任一条成立则全部成立）：

1. $A$ 可逆；
2. $A$ 行等价于 $I_n$；
3. $A$ 有 $n$ 个主元；
4. $A\mathbf{x}=\mathbf{0}$ 只有零解；
5. $A$ 的各列线性无关；
6. 对每个 $\mathbf{b}\in\mathbb{R}^n$，$A\mathbf{x}=\mathbf{b}$ 有唯一解；
7. $A$ 的各列张成 $\mathbb{R}^n$；
8. $T(\mathbf{x})=A\mathbf{x}$ 是单射；
9. $T(\mathbf{x})=A\mathbf{x}$ 是满射；
10. $\det A\neq0$。

**⚠ 高频错.** 问"哪个**不是**等价条件"时，正确答案往往是 $\det A=0$、列相关、$\mathbf{b}$ 不可达这一类**否定式**。

---

## 第六部分：子空间与基 (Lecture 8: §2.8)

### 2.8 Subspaces of $\mathbb{R}^n$

**子空间三条件.** $H\subseteq\mathbb{R}^n$ 是子空间 ⇔

1. $\mathbf{0}\in H$；
2. $\mathbf{u},\mathbf{v}\in H\Rightarrow\mathbf{u}+\mathbf{v}\in H$（加法封闭）；
3. $\mathbf{u}\in H,\ c\in\mathbb{R}\Rightarrow c\mathbf{u}\in H$（数乘封闭）。

**两类标准子空间.**

- $\operatorname{Nul}A=\{\mathbf{x}\in\mathbb{R}^n:A\mathbf{x}=\mathbf{0}\}$，住在 $\mathbb{R}^n$（$n$ = 列数）；
- $\operatorname{Col}A=\operatorname{Span}\{\mathbf{a}_1,\dots,\mathbf{a}_n\}$，住在 $\mathbb{R}^m$（$m$ = 行数）。

**求基的标准流程.**

| 求什么 | 怎么做 |
|---|---|
| $\operatorname{Nul}A$ 的基 | 解 $A\mathbf{x}=\mathbf{0}$，化 RREF，自由变量逐个取 1 |
| $\operatorname{Col}A$ 的基 | 化简 $A$ 找**主元列位置**，回到**原矩阵**取这些列 |

**⚠ 陷阱.** 列空间的基**不能**取化简后矩阵的列（那属于行空间，不是列空间）。必须回到原矩阵。

**基与维数.**

- 基 = 线性无关 + 张成；
- $\dim V$ = 基中向量个数（唯一）；
- 主元个数 + 自由变量个数 = 列数 $n$——两者正好把 $n$ 列分完。

---

## 🌟 典型例题精解（综合各 Lecture）

### 例 1（1.2 参数系统）$h,k$ 取何值使系统有无穷多解

$$\begin{cases}x_1+3x_2=1\\ 2x_1+hx_2=k\end{cases}$$

**做法.** $R_2-2R_1$：$(h-6)x_2=k-2$。

- $h\neq6$：$x_2=\dfrac{k-2}{h-6}$，唯一解；
- $h=6,\ k=2$：该行 $0=0$，只剩一个方程、两个未知数 ⇒ **无穷多解**；
- $h=6,\ k\neq2$：$0\neq0$ ⇒ 无解。

**要点.** 先算"消元后剩下的系数"，再分别检验"$0=0$"与"$0=\text{非零}$"。

### 例 2（1.3 是否在 span）$\mathbf{b}=(1,h,3)$ 何时属于 $\operatorname{Span}\{(1,0,1),(0,1,1),(1,2,3)\}$

**做法.** 设 $\mathbf{b}=c_1\mathbf{v}_1+c_2\mathbf{v}_2+c_3\mathbf{v}_3$，比较分量：

$$c_1+c_3=1,\qquad c_2+2c_3=h,\qquad c_1+c_2+3c_3=3$$

前两式代入第三式得 $1+h=3$，故 $h=2$。

**要点.** 三个未知系数的 span 题，通常消去两个系数后剩一个含参数的等式。

### 例 3（1.5 通解）RREF 为 $\left[\begin{array}{cccc|c}1&-2&0&3&3\\0&0&1&-1&1\end{array}\right]$

**做法.** 主元列 1、3，自由变量 $x_2,x_4$：

$$x_1=3+2x_2-3x_4,\qquad x_3=1+x_4$$

特解 $(3,0,1,0)$；取 $x_2=1,x_4=0$ 得 $(2,1,0,0)$；取 $x_2=0,x_4=1$ 得 $(-3,0,1,1)$：

$$\mathbf{x}=(3,0,1,0)+s(2,1,0,0)+t(-3,0,1,1)$$

**要点.** 特解 = 自由变量全 0；每个自由变量单独取 1 得一个方向向量。

### 例 4（1.7 含参相关）$\det\begin{bmatrix}1&4&7\\2&5&8\\3&6&h\end{bmatrix}=0$ 的 $h$

**做法.**

$$\det=1(5h-48)-4(2h-24)+7(12-15)=5h-48-8h+96-21=-3h+27$$

$-3h+27=0\Rightarrow h=9$。

**要点.** 三个向量相关 ⇔ 行列式为 0。展开时注意第二项的负号。

### 例 5（1.9 标准矩阵）已知 $T(\mathbf{e}_1)=(1,2)$、$T(\mathbf{e}_2)=(3,4)$

**做法.** 标准矩阵的列就是像：$A=\begin{bmatrix}1&3\\2&4\end{bmatrix}$。

**要点.** 像按**列**排，不是按行排。写反就得到转置。

### 例 6（2.2 乘积求逆）$A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\ B=\begin{bmatrix}1&0\\3&1\end{bmatrix}$

**做法.** $A^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$，$B^{-1}=\begin{bmatrix}1&0\\-3&1\end{bmatrix}$，故

$$(AB)^{-1}=B^{-1}A^{-1}=\begin{bmatrix}1&0\\-3&1\end{bmatrix}\begin{bmatrix}1&-2\\0&1\end{bmatrix}=\begin{bmatrix}1&-2\\-3&7\end{bmatrix}$$

验算：$AB=\begin{bmatrix}7&2\\3&1\end{bmatrix}$，其逆确实是 $\begin{bmatrix}1&-2\\-3&7\end{bmatrix}$。

**要点.** 顺序必须反转；算完用 $AB$ 直接求逆验一次最稳。

### 例 7（2.2 初等矩阵复合）$E_1$ 交换 $R_1,R_2$；$E_2$ 把 $-2R_1$ 加到 $R_3$；$E_3$ 把 $R_2$ 乘 $\frac14$

**做法.** $(E_1E_2E_3)^{-1}=E_3^{-1}E_2^{-1}E_1^{-1}$：

$$E_3^{-1}:\ R_2\to4R_2,\quad E_2^{-1}:\ R_3\to R_3+2R_1,\quad E_1^{-1}=E_1$$

按 $E_3^{-1}E_2^{-1}E_1^{-1}$ 从右往左作用到 $I$ 上：

1. $I\cdot E_1^{-1}=E_1=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix}$（交换 $R_1,R_2$）；
2. 左乘 $E_2^{-1}$：$R_3\to(0,0,1)+2(0,1,0)=(0,2,1)$；
3. 左乘 $E_3^{-1}$：$R_2\to4R_2$。

$$\begin{bmatrix}0&1&0\\4&0&0\\0&2&1\end{bmatrix}$$

**要点.** 逆序 + 每种操作取"反向操作"，两个错都能靠 $A\cdot A^{-1}=I$ 验出来。

### 例 8（2.8 零空间的基）$A=\begin{bmatrix}1&-2&1&0\\0&0&1&3\end{bmatrix}$

**做法.** $R_1-R_2$ 得 $\begin{bmatrix}1&-2&0&-3\\0&0&1&3\end{bmatrix}$：

$$x_1=2x_2+3x_4,\qquad x_3=-3x_4$$

取 $(x_2,x_4)=(1,0)$ 得 $(2,1,0,0)$；取 $(0,1)$ 得 $(3,0,-3,1)$。基为 $\{(2,1,0,0),(3,0,-3,1)\}$。

**要点.** 自由变量的符号跟着方程走，$x_3=-3x_4$ 的负号最容易丢。

---

## 附录 A：考前 10 分钟速览

### A1. 判据一页纸

| 问 | 答 |
|---|---|
| 方程组有解？ | 阶梯形无 $[0\cdots0\mid c],c\neq0$ |
| 唯一解？ | 无矛盾行且主元数 = 未知数个数 |
| 向量组无关？ | 以它们为列的矩阵每列有主元 |
| $\mathbf{b}\in\operatorname{Col}A$？ | $[A\ \mathbf{b}]$ 化简后最后一列没有新主元（主元个数与 $A$ 相同） |
| $T$ 单射？ | 每列有主元 / $\operatorname{Nul}A=\{\mathbf{0}\}$ |
| $T$ 满射？ | 每行有主元 / $\operatorname{Col}A=\mathbb{R}^m$ |
| $A$ 可逆？ | $\det A\neq0$ ⇔ 每列有主元 ⇔ $A\sim I$ |
| $\dim\operatorname{Nul}A$？ | 数非主元列：个数 = 列数 − 主元个数 |

### A2. 必背公式

$$A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\qquad (AB)^{-1}=B^{-1}A^{-1}\qquad (AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$$

$$R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$$

### A3. 十大易错点（含你自己踩过的）

1. **抄错符号**：把 $-9$ 抄成 $9$、把 $-13$ 抄成 $13$。→ 每步重抄一遍原矩阵，别凭记忆改。
2. **乘积元素位置**：$AB$ 的 $(i,j)$ 是 $A$ 第 $i$ 行 · $B$ 第 $j$ 列，不是第 $i$ 列。
3. **RREF 没消干净**：主元列上方仍有非零元就还不是 RREF。
4. **顺序反转**：$(AB)^{-1}=B^{-1}A^{-1}$、$(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$。
5. **列空间的基**：取原矩阵的主元列，不是化简后的列。
6. **解集过不过原点**：$\mathbf{b}\neq\mathbf{0}$ 时不过原点。
7. **自由变量数用错维度**：自由变量个数 = 列数 − 主元个数（拿**列数**算，不是行数）。
8. **单射/满射看错行**：每行有主元 ⇒ 满射；每列有主元 ⇒ 单射。
9. **行列式展开符号**：第二项、第四项带负号。
10. **"$AB=0$ 所以 $A=0$ 或 $B=0$"**：矩阵没有零因子律。

### A4. 你 Practice Quiz 1 的四道错题回顾

| 题 | 错因 | 纠正动作 |
|---|---|---|
| Q8 | 矩阵符号抄错（$-9$ 抄成 $9$） | 每步从上一行重新抄，不要凭记忆 |
| Q9 | 参数 $k$ 应为 $-10$ | 含参题代回原方程验一次 |
| Q13 | 乘积第二行算成 $-13$（应为 $-3$） | 逐元素点积，写全中间过程 |
| Q15 | RREF 里 $3$ 没消成 $0$ | 化完 RREF 后回头检查每个主元列 |

---

## 附录 B：复习时间分配建议（考前 3 天）

| 时段 | 内容 |
|---|---|
| Day 1 上午 | 第零、一、二部分（1.1–1.4）+ 练习册 L1–L3 |
| Day 1 下午 | 第三部分（1.5、1.7）+ 练习册 L4 |
| Day 2 上午 | 第四、五部分（1.8–2.2）+ 练习册 L5–L6 |
| Day 2 下午 | 第六部分（2.3、2.8）+ 练习册 L7–L8 |
| Day 3 上午 | 综合提高卷 20 题（限时 50 分钟） |
| Day 3 下午 | 错题二刷 + 附录 A 速览 |
