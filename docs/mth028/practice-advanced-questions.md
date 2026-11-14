# MTH028 Linear Algebra · Week 1–8 综合提高卷 (Advanced Integrated Set)

> **20 题 · 英文题干 · 15 题五选一 + 5 题填空（只填数字）· 跨节综合**
> 难度高于《Week 1–8 练习册》：每题 2–4 步，多数把两三个小节串起来。重点补三类——含参数的行化简与相容性、基与维数定理的联动、初等矩阵与逆矩阵的复合运算。
> 使用方法：限时 50 分钟做完，再对照《综合卷解析册》。

**覆盖范围**

| 讲义 | 题号 | 综合的考点 |
|---|---|---|
| Lecture 1 (1.1) | A1-01 | 三元方程组求唯一解 |
| Lecture 2 (1.2) | A2-01 · A2-02 | 参数相容性、主元个数与自由变量 |
| Lecture 3 (1.3–1.4) | A3-01 · A3-02 · A3-03 | 列空间判断、张成参数、含参线性相关 |
| Lecture 4 (1.5–1.7) | A4-01 · A4-02 · A4-03 | 参数向量解、含参无关、解集维数 |
| Lecture 5 (1.8–1.9) | A5-01 · A5-02 · A5-03 | 变换复合、单射满射、零空间 |
| Lecture 6 (2.1–2.2) | A6-01 · A6-02 · A6-03 | 矩阵幂、三阶求逆、矩阵方程 |
| Lecture 7 (2.2–2.3) | A7-01 · A7-02 | 初等矩阵复合求逆、含参奇异 |
| Lecture 8 (2.8) | A8-01 · A8-02 · A8-03 | 零空间基、列空间基、主元列与自由变量 |

**作答格式**：每题在 `Answer / 作答：(　　　)` 中写选项字母；解析册按 A1-01 … A8-03 对应。

---

## Lecture 1 · 1.1

### A1-01 三元方程组求唯一解

*做题技巧 · 先看系数行列式是否为 0；不为 0 时用消元或克莱姆法则，求出解后代回第一个方程自检。*

Solve the system

$$x_1+2x_2+3x_3=14,\qquad 2x_1+5x_2+3x_3=21,\qquad x_1+x_2+8x_3=27 .$$

**SELECT ONE**

- A. $(2,\ 1,\ 3)$
- B. $(3,\ 1,\ 2)$
- C. $(1,\ 2,\ 3)$
- D. $(1,\ 3,\ 2)$
- E. 没有唯一解

Answer / 作答：(　　　)　·　解析见 A1-01

---

## Lecture 2 · 1.2

### A2-01 参数相容性

*做题技巧 · 第二行减去第一行的 3 倍，看剩下的系数什么时候被消掉；无穷多解要求「$0=0$」这一行成立。*

Find $h$ and $k$ so that the system

$$x_1+hx_2=2,\qquad 3x_1+6x_2=k$$

has infinitely many solutions.

**SELECT ONE**

- A. $h=6,\ k=2$
- B. $h=2,\ k=6$
- C. $h=2,\ k=2$
- D. $h=6,\ k=6$
- E. 不存在这样的 $(h,k)$

Answer / 作答：(　　　)　·　解析见 A2-01

---

### A2-02 主元个数与自由变量

*做题技巧 · 先数主元个数（不是非零元素个数），再用「列数 − 主元个数」得自由变量个数；4 列里看看哪一列能被前面的列表示。*

Let $A=\begin{bmatrix}1&2&-1&3\\2&4&0&8\\-1&-2&3&1\end{bmatrix}$. How many free variables does $A\mathbf{x}=\mathbf{0}$ have?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 A2-02

---

## Lecture 3 · 1.3–1.4

### A3-01 判断 $\mathbf{b}$ 是否在列空间

*做题技巧 · $\mathbf{b}\in\operatorname{Col}A$ ⇔ $A\mathbf{x}=\mathbf{b}$ 相容 ⇔ 化简 $[A\ \mathbf{b}]$ 后最后一列不出现新主元。*

Let $A=\begin{bmatrix}1&0&1\\2&1&3\\0&1&1\end{bmatrix}$ and $\mathbf{b}=(2,5,3)$. Which statement is correct?

**SELECT ONE**

- A. $\mathbf{b}\in\operatorname{Col}A$，因为 $\mathbf{b}=3\mathbf{a}_1-\mathbf{a}_2$
- B. $\mathbf{b}\in\operatorname{Col}A$，因为 $\mathbf{b}=\mathbf{a}_1+2\mathbf{a}_2$
- C. $\mathbf{b}\in\operatorname{Col}A$，因为 $A$ 是 $3\times3$
- D. $\mathbf{b}\notin\operatorname{Col}A$，因为 $A$ 化简后只有 2 个主元，而 $[A\ \mathbf{b}]$ 有 3 个
- E. $\mathbf{b}\in\operatorname{Col}A$，因为 $\mathbf{b}=\mathbf{a}_1+\mathbf{a}_3$

Answer / 作答：(　　　)　·　解析见 A3-01

---

### A3-02 $\mathbf{b}$ 在 span 中的参数

*做题技巧 · 设 $\mathbf{b}=c_1\mathbf{v}_1+c_2\mathbf{v}_2+c_3\mathbf{v}_3$，三个分量给出三个方程，消去 $c_i$ 后剩一个只含 $h$ 的等式。*

For which value of $h$ is $\mathbf{b}=(1,h,3)$ in $\operatorname{Span}\{(1,0,1),(0,1,1),(1,2,3)\}$?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 A3-02

---

### A3-03 含参线性相关

*做题技巧 · 三个向量相关 ⇔ 以它们为列的行列式为 0；先展开成 $k$ 的多项式再求根。*

For which $k$ are the vectors $(1,1,k)$, $(1,k,1)$, $(k,1,1)$ linearly dependent?

**SELECT ONE**

- A. 只有 $k=1$
- B. 只有 $k=-2$
- C. $k=1$ 或 $k=-2$
- D. $k=2$ 或 $k=-1$
- E. 任意实数 $k$

Answer / 作答：(　　　)　·　解析见 A3-03

---

## Lecture 4 · 1.5–1.7

### A4-01 参数向量形式的通解

*做题技巧 · 矩阵已是 RREF：主元列 1、3，自由变量 $x_2,x_4$；先写特解（自由变量取 0），再逐个自由变量取 1 得方向向量。*

The RREF of a system is $\left[\begin{array}{cccc|c}1&-2&0&3&3\\0&0&1&-1&1\end{array}\right]$. Write its general solution.

**SELECT ONE**

- A. $(3,0,1,0)+s(-2,1,0,0)+t(3,0,1,1)$
- B. $(3,0,1,0)+s(2,1,0,0)+t(-3,0,1,1)$
- C. $(0,0,0,0)+s(2,1,0,0)+t(-3,0,1,1)$
- D. $(3,0,1,0)$，唯一解
- E. $(3,0,1,0)+s(2,1,0,0)$，只有一个自由变量

Answer / 作答：(　　　)　·　解析见 A4-01

---

### A4-02 含参线性无关

*做题技巧 · 三个 $\mathbb{R}^3$ 向量相关 ⇔ 行列式为 0；把 $h$ 代进行列式解方程。*

For which $h$ are $(1,2,3)$, $(0,1,h)$, $(2,3,1)$ linearly dependent?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 A4-02

---

### A4-03 解集维数

*做题技巧 · $A\mathbf{x}=\mathbf{0}$ 的解集维数 = 自由变量个数 = 列数 $-$ 主元个数；这里要数**列数**（未知数个数），不是行数。*

$A$ is a $3\times5$ matrix whose RREF has 3 pivot columns. What is the dimension of the solution set of $A\mathbf{x}=\mathbf{0}$?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 A4-03

---

## Lecture 5 · 1.8–1.9

### A5-01 线性变换的复合

*做题技巧 · 先做的作用在右边：$T_2\circ T_1$ 的标准矩阵是 $A_2A_1$；代 $\mathbf{e}_1,\mathbf{e}_2$ 各验一次。*

Let $T_1$ be reflection across the $y$-axis and $T_2$ the counterclockwise rotation by $90^\circ$. Find the standard matrix of $T_2\circ T_1$.

**SELECT ONE**

- A. $\begin{bmatrix}0&1\\1&0\end{bmatrix}$
- B. $\begin{bmatrix}-1&0\\0&-1\end{bmatrix}$
- C. $\begin{bmatrix}0&-1\\-1&0\end{bmatrix}$
- D. $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$
- E. $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 A5-01

---

### A5-02 单射与满射

*做题技巧 · $m\times n$ 矩阵：每行有主元 ⇒ 满射；每列有主元 ⇒ 单射。行数与列数不等时两者不可能同时成立。*

$A$ is a $4\times3$ matrix with three pivot positions. Which statement is true about $T(\mathbf{x})=A\mathbf{x}$?

**SELECT ONE**

- A. $T$ 是满射但不是单射
- B. 既是单射又是满射
- C. 既不是单射也不是满射
- D. $T$ 是单射但不是满射
- E. 信息不足，无法判断

Answer / 作答：(　　　)　·　解析见 A5-02

---

### A5-03 零空间

*做题技巧 · 解 $A\mathbf{x}=\mathbf{0}$：RREF 后把主元变量用自由变量表示，自由变量取 1 得基向量。*

Find a basis for $\operatorname{Nul}A$ where $A=\begin{bmatrix}1&-2&1\\0&1&1\end{bmatrix}$.

**SELECT ONE**

- A. $\{(1,2,-1)\}$
- B. $\{(-3,-1,1)\}$
- C. $\{(1,1,0)\}$
- D. $\{(1,0,-1)\}$
- E. $\{(1,-1,1)\}$

Answer / 作答：(　　　)　·　解析见 A5-03

---

## Lecture 6 · 2.1–2.2

### A6-01 矩阵的高次幂

*做题技巧 · 先算 $A^2,A^3$ 找周期；指数按周期取余，$2003=3\cdot667+2$。*

Let $A=\begin{bmatrix}1&1&-3\\2&0&-1\\1&0&-1\end{bmatrix}$. Given that $A^{3}=I$, what is $A^{2003}$?

**SELECT ONE**

- A. $I$
- B. $A$
- C. $0$
- D. $A^{3}$
- E. $A^{2}$

Answer / 作答：(　　　)　·　解析见 A6-01

---

### A6-02 三阶矩阵求逆

*做题技巧 · 上三角矩阵的逆仍是上三角：先算对角线倒数，再逐列用 $AA^{-1}=I$ 回代求非对角元。*

Find $A^{-1}$ for $A=\begin{bmatrix}2&1&0\\0&3&1\\0&0&4\end{bmatrix}$.

**SELECT ONE**

- A. $\begin{bmatrix}1/2&-1/6&1/24\\0&1/3&-1/12\\0&0&1/4\end{bmatrix}$
- B. $\begin{bmatrix}1/2&1/6&1/24\\0&1/3&1/12\\0&0&1/4\end{bmatrix}$
- C. $\begin{bmatrix}2&-1&0\\0&3&-1\\0&0&4\end{bmatrix}$
- D. $\begin{bmatrix}1/2&-1/6&0\\0&1/3&-1/12\\0&0&1/4\end{bmatrix}$
- E. 不存在，因为 $\det A=0$

Answer / 作答：(　　　)　·　解析见 A6-02

---

### A6-03 矩阵方程

*做题技巧 · $AX=B$ 在 $A$ 可逆时 $X=A^{-1}B$；注意 $B$ 是矩阵不是向量，逐列解两次也行。*

Let $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$ and $B=\begin{bmatrix}4&3\\2&1\end{bmatrix}$. Solve $AX=B$.

**SELECT ONE**

- A. $\begin{bmatrix}-1&0\\2&2\end{bmatrix}$
- B. $\begin{bmatrix}2&0\\2&-1\end{bmatrix}$
- C. $\begin{bmatrix}2&2\\0&-1\end{bmatrix}$
- D. $\begin{bmatrix}4&3\\2&1\end{bmatrix}$
- E. 无解

Answer / 作答：(　　　)　·　解析见 A6-03

---

## Lecture 7 · 2.2–2.3

### A7-01 初等矩阵复合求逆

*做题技巧 · $(E_1E_2E_3)^{-1}=E_3^{-1}E_2^{-1}E_1^{-1}$，逆序是唯一的易错点；每种初等操作求逆就是「反向操作」。*

Let $E_1$ interchange rows 1 and 2, $E_2$ add $-2$ times row 1 to row 3, and $E_3$ multiply row 2 by $\frac14$. Find $(E_1E_2E_3)^{-1}$.

**SELECT ONE**

- A. $\begin{bmatrix}0&1/4&0\\1&0&0\\-2&0&1\end{bmatrix}$
- B. $\begin{bmatrix}0&1&0\\4&0&0\\0&2&1\end{bmatrix}$
- C. $\begin{bmatrix}0&1&0\\0&0&4\\0&2&1\end{bmatrix}$
- D. $\begin{bmatrix}1&0&0\\0&4&0\\0&0&1\end{bmatrix}$
- E. $\begin{bmatrix}0&4&0\\1&0&0\\0&2&1\end{bmatrix}$

Answer / 作答：(　　　)　·　解析见 A7-01

---

### A7-02 含参奇异

*做题技巧 · 奇异 ⇔ 行列式为 0；沿第一列展开最快。*

For which $h$ is $A=\begin{bmatrix}1&2&3\\0&1&h\\1&0&1\end{bmatrix}$ singular?

**FILL IN · 只填数字（整数；分数写成 3/2 这样的形式）**

Answer / 作答：(　　　)　·　解析见 A7-02

---

## Lecture 8 · 2.8

### A8-01 零空间的基

*做题技巧 · 主元列 1、3，自由变量 $x_2,x_4$；分别取 $1$ 得两个基向量，写回原变量顺序。*

Find a basis for $\operatorname{Nul}A$ where $A=\begin{bmatrix}1&-2&1&0\\0&0&1&3\end{bmatrix}$.

**SELECT ONE**

- A. $\{(2,1,0,0),\ (3,0,3,1)\}$
- B. $\{(-2,1,0,0),\ (-3,0,-3,1)\}$
- C. $\{(1,2,0,0),\ (3,0,-3,1)\}$
- D. $\{(2,1,0,0)\}$
- E. $\{(2,1,0,0),\ (3,0,-3,1)\}$

Answer / 作答：(　　　)　·　解析见 A8-01

---

### A8-02 列空间的基

*做题技巧 · 用行化简找主元列的位置，再回到**原矩阵**取对应列；不能直接取化简后的列。*

For $A=\begin{bmatrix}1&0&1\\2&1&3\\0&1&1\end{bmatrix}$, the standard procedure (pivot columns of $A$) gives which basis for $\operatorname{Col}A$?

**SELECT ONE**

- A. $\{(1,2,0),\ (0,1,1)\}$
- B. $\{(1,2,0),\ (1,3,1)\}$
- C. $\{(1,2,0),\ (1,0,1)\}$
- D. $\{(1,0,1),\ (0,1,1),\ (2,1,3)\}$
- E. $\{(1,0,1),\ (0,1,1)\}$

Answer / 作答：(　　　)　·　解析见 A8-02

---

### A8-03 主元列与自由变量

*做题技巧 · 数出 RREF 里主元列的个数 $p$：$\operatorname{Col}A$ 的基取原矩阵的 $p$ 个主元列，$\operatorname{Nul}A$ 的基有 $n-p$ 个向量（自由变量的个数）。行数只决定 $\operatorname{Col}A$ 住在哪个 $\mathbb{R}^m$。*

$A$ is a $5\times7$ matrix whose RREF has 4 pivot columns. Which statement is true?

**SELECT ONE**

- A. $\operatorname{Col}A$ 的基有 3 个向量，$\operatorname{Nul}A$ 的基有 4 个向量
- B. 两个基都含 4 个向量
- C. $\operatorname{Col}A$ 的基有 4 个向量，$\operatorname{Nul}A$ 的基有 3 个向量
- D. $\operatorname{Nul}A$ 的基有 7 个向量
- E. 信息不足，无法确定两个基的向量个数

Answer / 作答：(　　　)　·　解析见 A8-03
