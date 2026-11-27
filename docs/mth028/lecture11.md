# MTH028 线性代数 I｜第 11 课笔记

**§3.2 行列式的性质（Properties of Determinants）**

依据 第 11 课课件。配套练习见 Weekly Assignment 10 解析。前一课的[余子式展开](../lecture10/)在本课仍然有用，尤其是消元产生一排零之后。

| 题目给的信息 | 可以先做什么 |
|---|---|
| 给具体方阵，零很少 | 行消元造零，再乘三角矩阵的对角元或做余子式展开 |
| 给变换前后的两组行 | 识别行加法、换行和行倍乘，逐个记下因子 |
| 只给 $\det A,\det B$ | 直接用乘积、幂、逆和整体倍乘公式 |
| 问向量组是否线性无关 | 若有 $n$ 个 $\mathbb R^n$ 中的向量，将它们排成列，检查行列式是否非零 |

## 1. 三种行变换如何改变行列式？

课件定理 3。设由 $A$ 做一次行变换得到 $B$。

| 行变换（row operation） | 对行列式的影响 |
|---|---|
| 行加法（row replacement）$R_i\leftarrow R_i+kR_j$，$i\ne j$ | $\det B=\det A$ |
| 行交换（row interchange）$R_i\leftrightarrow R_j$ | $\det B=-\det A$ |
| 行倍乘（row scaling）$R_i\leftarrow kR_i$，$k\ne0$ | $\det B=k\det A$ |

上表写的是**从原矩阵到新矩阵**的关系。比如一行乘 $5$ 使 $\det B=5\det A$，已知 $\det B$ 时就要除以 $5$，才能找回 $\det A$。因此消元时通常只用行加法和换行，主元可以原样保留。

**课件例题（English steps）.** Reduce $A$ to an upper triangular matrix. First apply $R_2\leftarrow R_2+2R_1$ and $R_3\leftarrow R_3+R_1$. Then interchange rows 2 and 3.

$$
\begin{bmatrix}1&-4&2\\-2&8&-9\\-1&7&0\end{bmatrix}
\longrightarrow
\begin{bmatrix}1&-4&2\\0&0&-5\\0&3&2\end{bmatrix}
\longrightarrow
U=\begin{bmatrix}1&-4&2\\0&3&2\\0&0&-5\end{bmatrix}.
$$

The two replacements leave the determinant unchanged. The one interchange reverses its sign, so $\det A=-\det U=-(1)(3)(-5)=15$.

**中文解析。** 两次行加法先消掉第一列的两个数。中间矩阵的 $(3,2)$ 仍有一个 $3$，交换后两行才得到上三角。中间矩阵和原矩阵行列式相同，最后的 $U$ 则和原矩阵差一个负号。这个例子也说明为什么不能看到对角线上有零，就直接判断行列式是零。

一般地，若用行加法与 $r$ 次换行得到阶梯形（echelon form）$U$，则对方阵有

$$\boxed{\det A=(-1)^r\det U=(-1)^r u_{11}\cdots u_{nn}.}$$

若过程中也分别用 $k_1,\ldots,k_s$ 倍乘单行，则 $\det U=(-1)^r(k_1\cdots k_s)\det A$，求原行列式时要把倍乘因子除回去。

## 2. 行列式与可逆性、转置和线性相关

课件定理 4 与定理 5：

$$
\boxed{A\text{ 可逆（invertible）}\iff \det A\ne0},
\qquad
\boxed{\det(A^T)=\det A}.
$$

**为什么非零就可逆？** 方阵消元后，可逆等价于每一行都有主元（pivot）。此时 $n$ 个主元就在上三角矩阵的主对角线上，乘积非零。若主元不足，就会出现零行，乘积为零。行加法和换行保留“是否为零”，所以这个判断也适用于原矩阵。

**为什么转置不改变行列式？** 沿 $A^T$ 第一行展开，对应沿 $A$ 第一列展开。对应位置的符号 $(-1)^{1+j}=(-1)^{j+1}$，删行列后的子矩阵互为转置。用低一阶的结论逐层往下推，到一阶时转置前后完全相同。

由转置性质，同样的三条规则也适用于**列变换（column operations）**。对方阵：

- 行或列线性相关（linearly dependent）时，行列式为零。
- 两行成比例、两列相同或出现零行、零列，都是能直接判零的情形。
- 已知 $\det A<0$ 时，$\det A$ 仍然非零，所以矩阵满秩（full rank），$\operatorname{rank}A=n$。

## 3. 行列式只在单独一行或一列上线性

把其他行固定，仅第 $i$ 行可变，记所得的行列式为 $D_i(\mathbf r)$。则**单行线性（linearity in one row）**意味着

$$D_i(c\mathbf u+d\mathbf v)=cD_i(\mathbf u)+dD_i(\mathbf v).$$

沿这一行展开时，各项的代数余子式都已删掉该行，因此系数保持固定。这就是能对该行做加法拆分和提常数的原因。用转置同样能得到单列线性。

**单行倍乘与整矩阵倍乘。** $kA$ 将 $n$ 行都乘了 $k$，每行各带出一个 $k$：

$$\boxed{\det(kA)=k^n\det A.}$$

比如 $\det(2I_2)=4$。若把两矩阵相加，所有行都变了，逐行拆分会出现混合项。可以用 $A=B=I_2$ 检查：

$$\det(A+B)=4,\qquad \det A+\det B=2.$$

单行线性也解释了行加法为什么保值：把新行 $R_i+kR_j$ 拆开，第一项是原行列式，第二项有两行都是 $R_j$，因此那一项为零。

## 4. 乘积、幂与逆矩阵

课件定理 6 是**乘积性质（multiplicative property）**。对同阶方阵，

$$\boxed{\det(AB)=\det A\det B.}$$

上节作业算过三类**初等矩阵（elementary matrices）**的行列式：行加法给 $1$、换行给 $-1$、一行乘 $k$ 给 $k$。左乘初等矩阵 $E$ 恰好做对应的行变换，因此 $\det(EA)=\det E\det A$ 就把三条行变换规则统一起来。

| 要算的量 | 公式与原因 |
|---|---|
| $\det(A^k)$，$k$ 为正整数 | $(\det A)^k$，因为有 $k$ 个矩阵因子 |
| $\det(A^{-1})$，$A$ 可逆 | $1/\det A$，由 $\det(AA^{-1})=\det I=1$ |
| $\det(BA)$ | $\det(AB)$，因为 $\det A$、$\det B$ 是可交换的数 |
| $\det(B^{-1}AB)$，$B$ 可逆 | $\det A$，因为 $\det(B^{-1})\det B=1$ |

**课件例题。** $A=\begin{bmatrix}6&1\\3&2\end{bmatrix}$、$B=\begin{bmatrix}4&3\\1&2\end{bmatrix}$，$\det A=9$、$\det B=5$。因此 $\det(AB)=45$。若想核对，$AB=\begin{bmatrix}25&20\\14&13\end{bmatrix}$，其行列式 $25\cdot13-20\cdot14$ 确实是 $45$。

作业里同时出现 $A^3$ 和 $2A$。前者的指数来自**相乘了几次**，所以 $\det(A^3)=(\det A)^3$。后者的指数来自**有多少行被倍乘**，所以若 $A$ 是四阶，$\det(2A)=2^4\det A$。

## 5. 配套应用：二阶行列式与平行四边形

把两个向量 $\mathbf u,\mathbf v$ 排成列，$|\det[\mathbf u\ \mathbf v]|$ 给出它们围成的平行四边形的面积（area of a parallelogram）。在作业给出的特例中，$\mathbf u=(3,0)^T$、$\mathbf v=(x,2)^T$，底边水平且长 $3$，垂直高度一直是 $2$。所以面积是 $6$，而代数计算也有 $\det[\mathbf u\ \mathbf v]=3\cdot2-0\cdot x=6$。横向挪动顶边会改变斜度，底和高保持不变。
