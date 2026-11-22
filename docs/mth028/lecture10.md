# MTH028 线性代数 I｜第十课笔记 v2

**§3.1 行列式入门（Introduction to Determinants）**

本节要会做两件事：用**代数余子式展开（cofactor expansion）**把行列式降阶，或者认出**三角矩阵（triangular matrix）**并直接乘主对角元。两种算法背后是同一件事：遇到零元素，对应的展开项就消失。

来源：Lecture 10 – Section 3.1。配套练习见 Weekly Assignment 9 解析 v2。

## 1. 从二阶到高阶

行列式（determinant）把一个方阵（square matrix）对应到一个数，写成 $\det A$ 或 $|A|$。例如

$$
A=\begin{bmatrix}1&2\\3&4\end{bmatrix},
\qquad
\det A=\begin{vmatrix}1&2\\3&4\end{vmatrix}
=1\cdot4-2\cdot3=-2.
$$

一般地，二阶行列式是 $ad-bc$。它还出现在二阶矩阵的逆矩阵公式中：

$$
\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}
=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
\quad(ad-bc\ne0).
$$

课件从这个二阶可逆判据出发，介绍高阶情形如何定义行列式。一般方阵的可逆判据与行变换对行列式的影响在 §3.2 系统讨论。

## 2. 删行删列，再看位置符号

| 符号 | 中文 / English | 怎么得到 |
|---|---|---|
| $a_{ij}$ | 元素 / entry | 第 $i$ 行、第 $j$ 列的那个数 |
| $A_{ij}$ | 子矩阵 / submatrix | 删去第 $i$ 行、整条第 $j$ 列，保留剩余行列的原顺序 |
| $\det A_{ij}$ | 余子式 / minor | 求剩下的子矩阵的行列式 |
| $C_{ij}$ | 代数余子式 / cofactor | 给余子式乘上位置符号 $(-1)^{i+j}$ |

例如课件中的矩阵

$$
A=\begin{bmatrix}1&5&0\\2&4&-1\\0&-2&0\end{bmatrix}.
$$

看 $a_{32}=-2$。删去第 3 行、第 2 列，会留下原来的第 1、2 行和第 1、3 列：

$$
A_{32}=\begin{bmatrix}1&0\\2&-1\end{bmatrix},
\qquad
\det A_{32}=-1,
\qquad
C_{32}=(-1)^{3+2}(-1)=1.
$$

所以位置 $(3,2)$ 的**完整展开项**是 $a_{32}C_{32}=(-2)(1)=-2$。这里有三个独立的量：**原元素 $-2$、位置符号 $-1$、余子式的值 $-1$**。把三者分开写，就能追踪每个负号来自哪里。

位置符号可以画成棋盘格（checkerboard pattern），左上角从 $+$ 开始：

$$
\begin{bmatrix}
+&-&+&-\\
-&+&-&+\\
+&-&+&-\\
-&+&-&+
\end{bmatrix}.
$$

每次降阶都用当前子矩阵自己的行列编号。例如删掉原第 2 行后，原第 3 行在新矩阵里变成第 2 行。

## 3. 行列式的定义与任意行列展开

**递归定义（recursive definition）**沿第一行写。对 $n\ge2$，

$$
\det A=\sum_{j=1}^n a_{1j}(-1)^{1+j}\det A_{1j},
\qquad \det[a]=a.
$$

每个子矩阵都小一阶，所以展开最终会停在一阶。实际做题可以在二阶直接用 $ad-bc$。

**课件定理 1（Cofactor Expansion）**允许在任意一行或一列使用同样的规则：

$$
\begin{aligned}
\text{沿第 }i\text{ 行（固定 }i\text{）} &\quad \det A=\sum_{j=1}^n a_{ij}C_{ij},\\
\text{沿第 }j\text{ 列（固定 }j\text{）} &\quad \det A=\sum_{i=1}^n a_{ij}C_{ij}.
\end{aligned}
$$

**为什么找零多的行或列？**每个非零元素通常都要引出一个低阶行列式，而 $0\cdot C_{ij}$ 直接等于零。选定一条线后，给其中每个非零元素做“取元素 → 配符号 → 删行列 → 求值”，再把各项相加。遇到新的子矩阵，可以重新选一条最省事的线。

### 课件例题｜同一个三阶行列式，两种展开

**Method 1. Expand across the first row.** 第一行有 $1,5,0$，只留下前两项：

$$
\det A=
1\begin{vmatrix}4&-1\\-2&0\end{vmatrix}
-5\begin{vmatrix}2&-1\\0&0\end{vmatrix}
=1(-2)-5(0)=-2.
$$

其中第二项的元素 $5$ 非零，但余子式为零，所以算完仍会消失。

**Method 2. Expand across the third row.** 第三行是 $(0,-2,0)$，一开始就知道只需算一项：

$$
\det A=(-2)\underbrace{(-1)^{3+2}}_{-1}
\begin{vmatrix}1&0\\2&-1\end{vmatrix}
=(-2)(-1)(-1)=-2.
$$

换成沿第 3 列展开也只需一项。判断计算量时，行和列都可以扫一遍。

### 课件例题｜五阶怎样降到已经会算的三阶？

$$
B=\begin{bmatrix}
3&-7&8&9&-6\\
0&2&-5&7&3\\
0&0&1&5&0\\
0&0&2&4&-1\\
0&0&0&-2&0
\end{bmatrix}.
$$

第一列只剩 $3$，而降阶后的第一列只剩 $2$。两者各自在当前矩阵的 $(1,1)$ 位置，所以都配正号：

$$
\det B=
3\begin{vmatrix}2&-5&7&3\\0&1&5&0\\0&2&4&-1\\0&0&-2&0\end{vmatrix}
=3\cdot2\begin{vmatrix}1&5&0\\2&4&-1\\0&-2&0\end{vmatrix}
=3\cdot2\cdot(-2)=-12.
$$

每展开一次，只删本次选中元素所在的那一行和那一列。被删掉的行里的其他数不会进入下一阶。

## 4. 三角矩阵为什么能直接乘主对角元？

| 类型 | 零在哪里 | 第一轮怎样展开 |
|---|---|---|
| 上三角（upper triangular） | 主对角线下方全为零 | 沿第一列 |
| 下三角（lower triangular） | 主对角线上方全为零 | 沿第一行 |

两种情形都只有左上角 $a_{11}$ 可能贡献一项，且位置符号是 $+$。因此 $\det A=a_{11}\det A_{11}$。右下角剩余的子矩阵仍是同类型的三角矩阵，于是可以反复取出左上角，得到课件**定理 2**：

$$
\boxed{\det A=a_{11}a_{22}\cdots a_{nn}\quad(A\text{ 为三角矩阵}).}
$$

课件末尾的例子：

$$
\begin{vmatrix}3&-7&8&9\\0&2&-5&7\\0&0&1&5\\0&0&0&-2\end{vmatrix}
=3\cdot2\cdot1\cdot(-2)=-12.
$$

和上一节的五阶例题对照：五阶矩阵主对角线下方有 $a_{43}=2$，上方也有非零元，所以应使用展开。**先检查整侧是不是零，再决定能否直接乘主对角元。**对角矩阵（diagonal matrix）两侧都是零，也适用定理 2，因此 $\det I_n=1$。

## 5. 回看课件开头：三阶公式从哪来？

课件用消元解释为什么会想到把三阶式子按第一行分组。设

$$
A=\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix},\qquad a\ne0.
$$

将第 2、3 行分别乘 $a$，再分别减去第 1 行的 $d$ 倍和 $g$ 倍。结果是

$$
\begin{bmatrix}a&b&c\\0&p&q\\0&r&s\end{bmatrix},
\quad p=ae-bd,\quad q=af-cd,\quad r=ah-bg,\quad s=ai-cg.
$$

**额外假设 $p\ne0$** 时，可以用 $R_3\leftarrow pR_3-rR_2$ 消去 $r$。右下角变成 $ps-rq$，把它展开、按 $a,b,c$ 分组：

$$
ps-rq=a\big[a(ei-fh)-b(di-fg)+c(dh-eg)\big].
$$

括号里的三项恰好是 $a\det A_{11}-b\det A_{12}+c\det A_{13}$，因此课件用这个表达式引出递归定义。

**这里的 $p\ne0$ 是消元路线的假设。**例如
$\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix}$
可通过交换后两行变成单位矩阵，却有 $a=1$、$p=0$。此时换一行当主元（pivot）即可继续消元，行列式也仍可按定义展开。

## 6. 做题前的三项检查

1. **先看结构。** 已是上三角或下三角，直接乘主对角元。
2. **一般方阵先找零。** 沿零多的行或列展开，每降一阶重新选。二阶直接算 $ad-bc$。
3. **逐项检查来源。** 元素是否带负号？位置符号是否用当前矩阵的编号？子矩阵是否准确删掉了对应的一行一列？

**自测。** 计算 $\begin{vmatrix}1&0&0\\0&0&2\\0&3&0\end{vmatrix}$。沿第一行只剩 $1\cdot\begin{vmatrix}0&2\\3&0\end{vmatrix}=-6$。这也是为什么主对角线上出现零时，需要先判断矩阵结构，再判断行列式。
