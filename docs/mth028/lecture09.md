# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 2.9 维数与秩 (Dimension and Rank)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 9 Summary)

### Section 2.9 维数与秩 (Dimension and Rank)

#### 1. 从标准基到一般基：唯一表示定理

* **动机 (Motivation)**：在 $\mathbb{R}^n$ 中，每个向量 $\mathbf{x}=(x_1,\dots,x_n)^T$ 都能唯一地写成标准基的组合
  $$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\cdots+x_n\mathbf{e}_n,$$
  系数恰好就是它的分量。我们希望任意子空间的任意一组基都具有同样的“系数即坐标”的性质。

* **定理 2.9.1（唯一表示定理, The Unique Representation Theorem）**：设 $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2,\dots,\mathbf{b}_p\}$ 是子空间 $H\subseteq\mathbb{R}^m$ 的基，则对每个 $\mathbf{x}\in H$，存在**唯一**的一组标量 $c_1,c_2,\dots,c_p$，使
  $$\mathbf{x}=c_1\mathbf{b}_1+c_2\mathbf{b}_2+\cdots+c_p\mathbf{b}_p.$$

* **证明 (Proof)**：
  * **存在性 (Existence)**：$\mathcal{B}$ 张成 $H$，故 $\mathbf{x}\in H=\text{Span}\{\mathbf{b}_1,\dots,\mathbf{b}_p\}$，即存在系数 $c_1,\dots,c_p$。
  * **唯一性 (Uniqueness)**：若 $\mathbf{x}=c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p=d_1\mathbf{b}_1+\cdots+d_p\mathbf{b}_p$，两式相减得
    $$\mathbf{0}=(c_1-d_1)\mathbf{b}_1+\cdots+(c_p-d_p)\mathbf{b}_p.$$
    由 $\mathcal{B}$ 线性无关，所有 $c_i-d_i=0$，即 $c_i=d_i$。

* **要点**：存在性来自“张成”，唯一性来自“线性无关”——基的定义中的两条正好各管一半。

#### 2. 坐标与坐标向量

* **定义 (Definition)**：设 $\mathcal{B}=\{\mathbf{b}_1,\dots,\mathbf{b}_p\}$ 是子空间 $H$ 的基，且 $\mathbf{x}=c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p$。
  * 标量 $c_1,\dots,c_p$ 称为 $\mathbf{x}$ 相对基 $\mathcal{B}$ 的**坐标 (coordinates)**（或 $\mathcal{B}$-坐标）；
  * 向量 $[\mathbf{x}]_{\mathcal{B}}=(c_1,\dots,c_p)^T\in\mathbb{R}^p$ 称为 $\mathbf{x}$ 的**坐标向量 (coordinate vector)**。

* **说明 (Remarks)**：
  1. 坐标向量的维数是 $p=\dim H$，与 $\mathbf{x}$ 所在的空间 $\mathbb{R}^m$ 无关；
  2. 同一个向量在不同基下的坐标一般不同——“坐标”永远相对于某组基而言；
  3. $\mathcal{B}$ 是标准基时，$[\mathbf{x}]_{\mathcal{B}}$ 就是 $\mathbf{x}$ 本身。

* **⚠️ 重要易错点**：$[\mathbf{x}]_{\mathcal{B}}$ 是 $\mathbb{R}^p$ 中的向量，不是 $\mathbb{R}^m$ 中的 $\mathbf{x}$；写答案时不要把它与 $\mathbf{x}$ 混为一谈。

#### 3. 求坐标向量

* **方法一（按定义解方程）**：解
  $$c_1\mathbf{b}_1+c_2\mathbf{b}_2+\cdots+c_p\mathbf{b}_p=\mathbf{x},$$
  即以 $\mathbf{b}_1,\dots,\mathbf{b}_p$ 为列、$\mathbf{x}$ 为右端向量的线性方程组，解就是 $[\mathbf{x}]_{\mathcal{B}}$。

* **方法二（矩阵求逆，适用于 $H=\mathbb{R}^n$ 且基含 $n$ 个向量）**：令 $P_{\mathcal{B}}=[\mathbf{b}_1\ \mathbf{b}_2\ \cdots\ \mathbf{b}_n]$，则 $P_{\mathcal{B}}$ 可逆，且
  $$[\mathbf{x}]_{\mathcal{B}}=P_{\mathcal{B}}^{-1}\mathbf{x}.$$

* **几何直观 (Graphical Interpretation)**：基相当于给子空间选定一套“坐标轴”。同一个点 $\mathbf{x}$ 在标准基下坐标是 $(1,6)^T$，在另一组基下可能写成 $(-2,3)^T$——坐标变了，点没变。

#### 4. 坐标映射：子空间与 $\mathbb{R}^p$ 同构

* **坐标映射 (coordinate map)**：$\mathbf{x}\mapsto[\mathbf{x}]_{\mathcal{B}}$ 是从 $H$ 到 $\mathbb{R}^p$ 的映射。
* **一对一 (one-to-one)**：若 $[\mathbf{u}]_{\mathcal{B}}=[\mathbf{v}]_{\mathcal{B}}=(c_1,\dots,c_p)^T$，则 $\mathbf{u}=c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p=\mathbf{v}$。
* **满射 (onto)**：对任意 $\mathbf{c}=(c_1,\dots,c_p)^T\in\mathbb{R}^p$，取 $\mathbf{x}=c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p\in H$，则 $[\mathbf{x}]_{\mathcal{B}}=\mathbf{c}$。
* **线性 (linear)**：对 $\mathbf{u},\mathbf{v}\in H$ 与 $a\in\mathbb{R}$，
  $$[\mathbf{u}+\mathbf{v}]_{\mathcal{B}}=[\mathbf{u}]_{\mathcal{B}}+[\mathbf{v}]_{\mathcal{B}},\qquad [a\mathbf{u}]_{\mathcal{B}}=a[\mathbf{u}]_{\mathcal{B}}.$$
* **同构 (isomorphism)**：既线性又一一对应。故 $H$ 与 $\mathbb{R}^p$ 作为实向量空间**同构**，记作 $H\cong\mathbb{R}^p$。这是“$p$ 维子空间在代数上就是 $\mathbb{R}^p$”的严格含义，也为第四章的线性变换埋下伏笔。

#### 5. 维数的定义与定理 2.9.2

* **问题**：同一个子空间的两组基，所含向量的个数会不会不同？
* **定理 2.9.2**：若子空间 $H$ 有一组含 $p$ 个向量的基，则
  1. $H$ 中任意**多于 $p$ 个**向量必线性相关；
  2. $H$ 中任意**少于 $p$ 个**向量必不能张成 $H$。
  从而 $H$ 的**每一组基都恰含 $p$ 个向量**，这个数只由 $H$ 本身决定。

* **定义（维数, dimension）**：非零子空间 $H$ 的**维数** $\dim H$ 定义为它的任意一组基中向量的个数。

* **约定与例子 (Remarks)**：
  * $\dim\{\mathbf{0}\}=0$（零子空间不含基向量）；
  * $\dim\mathbb{R}^n=n$（标准基有 $n$ 个向量）；
  * 对任意子空间 $H\subseteq\mathbb{R}^n$，都有 $0\le\dim H\le n$。

* **⚠️ 警告 (Warning)**：维数数的是**基向量的个数**，既不是向量的分量个数，也不是任意生成集中向量的个数。例如 $\mathbb{R}^3$ 中一个平面可以由三个、四个甚至无穷多个向量张成，但它的维数永远是 2。

#### 6. 基定理：用维数省去一半工作

* **定理 2.9.3（基定理, The Basis Theorem）**：设 $H$ 是 $\mathbb{R}^n$ 的 $p$ 维子空间（$p\ge 1$）。
  * $H$ 中任意恰含 $p$ 个向量的**线性无关**集自动是 $H$ 的基；
  * $H$ 中任意恰含 $p$ 个向量且**张成** $H$ 的集合自动是 $H$ 的基。

* **用法**：当 $\dim H$ 已知时，要判定 $p$ 个向量构成基，只需验证“线性无关”或“张成”其中之一，不必两者都证。

* **⚠️ 前提**：向量个数必须**恰好等于** $\dim H$；多了必相关，少了必张不满，基定理不适用。

#### 7. 零空间与列空间的维数

* **核心结论**：设 $A$ 是 $m\times n$ 矩阵，则
  $$\dim\text{Col}\,A=\text{主元列的个数},\qquad \dim\text{Nul}\,A=\text{非主元列的个数},$$
  于是
  $$n=\text{列数}=\text{主元列数}+\text{非主元列数}=\dim\text{Col}\,A+\dim\text{Nul}\,A.$$

* **解释**：
  * 主元列对应**基本变量**；原矩阵的主元列构成 $\text{Col}\,A$ 的基（定理 2.8.5），故 $\dim\text{Col}\,A$ 就是主元列数；
  * 每个**非主元列**对应一个自由变量，也就对应 $\text{Nul}\,A$ 的一个基向量，故 $\dim\text{Nul}\,A$ 就是非主元列数。

* **例（见例题 7）**：$4\times 5$ 矩阵行化简后主元在第 $1,2,4$ 列，则 $\dim\text{Col}\,A=3$；非主元列是第 $3,5$ 列，则 $\dim\text{Nul}\,A=2$；$3+2=5$，恰为列数。

#### 8. 秩与秩定理

* **定义（秩, rank）**：$\text{rank}\,A=\dim\text{Col}\,A$。

* **定理 2.9.4（秩定理, The Rank Theorem）**：对 $m\times n$ 矩阵 $A$，
  $$\text{rank}\,A+\dim\text{Nul}\,A=n,$$
  并且 $\text{rank}\,A$ 等于 $A$ 中主元位置（pivot positions）的个数。

* **推论 (Remark)**：$\text{rank}\,A\le\min\{m,n\}$——因为每行、每列最多贡献一个主元。

* **用法**：已知 $m,n$ 与 $\text{rank}\,A$、$\dim\text{Nul}\,A$ 中的一个，可反求另一个；也可用 $\text{rank}\,A\le\min\{m,n\}$ 判断“某个维数的零空间是否可能存在”。

#### 9. 秩、线性变换与可逆性

* **与线性变换**：设 $T:\mathbb{R}^n\to\mathbb{R}^m$ 的标准矩阵为 $A$，则 $T(\mathbf{x})=A\mathbf{x}$，且 $\text{Range}\,T$ 由 $A$ 的列的所有线性组合构成，即 $\text{Range}\,T=\text{Col}\,A$。因此
  $$\text{rank}\,A=\dim\text{Col}\,A=\dim\text{Range}\,T.$$

* **可逆矩阵定理（Theorem 8 续）**：设 $A$ 为 $n\times n$ 矩阵，则以下各条都与“$A$ 可逆”等价：
  * (m) $A$ 的列构成 $\mathbb{R}^n$ 的基；
  * (n) $\text{Col}\,A=\mathbb{R}^n$；
  * (o) $\dim\text{Col}\,A=n$；
  * (p) $\text{rank}\,A=n$；
  * (q) $\text{Nul}\,A=\{\mathbf{0}\}$；
  * (r) $\dim\text{Nul}\,A=0$。

* **证明链条**：$(a)\Rightarrow(m)\Rightarrow(n)\Rightarrow(o)\Rightarrow(p)\Rightarrow(r)\Rightarrow(q)\Rightarrow(a)$
  * $(a)\Rightarrow(m)$：由 (e)(h)，$A$ 的列线性无关且张成 $\mathbb{R}^n$，故构成基；
  * $(m)\Rightarrow(n)\Rightarrow(o)$：基张成 $\mathbb{R}^n$，故 $\dim\text{Col}\,A=\dim\mathbb{R}^n=n$；
  * $(o)\Rightarrow(p)$：秩的定义；
  * $(p)\Rightarrow(r)$：由秩定理，$\dim\text{Nul}\,A=n-\text{rank}\,A=n-n=0$；
  * $(r)\Rightarrow(q)$：零维子空间只能是 $\{\mathbf{0}\}$；
  * $(q)\Rightarrow(a)$：$A\mathbf{x}=\mathbf{0}$ 只有零解，这正是原定理中的条件 (d)，由 $(d)\Rightarrow(a)$ 知 $A$ 可逆。链条闭合，$(a)$–$(r)$ 全部等价。

#### 10. 秩与矩阵运算

* 对任意矩阵 $A$ 与 $c\ne 0$：$\text{rank}(cA)=\text{rank}\,A$；
* 对可逆方阵 $A$：$\text{rank}\,A^{-1}=\text{rank}\,A$；
* 对任意矩阵 $A$：$\text{rank}(A^T)=\text{rank}\,A$；
* 对乘积有定义的 $A,B$：$\text{rank}(AB)\le\min\{\text{rank}\,A,\text{rank}\,B\}$；
* **秩不可加**：$\text{rank}(A+B)$ 不能由 $\text{rank}\,A$、$\text{rank}\,B$ 决定。反例：
  $$A=\begin{bmatrix}1&0\\0&0\end{bmatrix},\qquad B=\begin{bmatrix}0&0\\0&1\end{bmatrix},\qquad \text{rank}\,A=\text{rank}\,B=1,$$
  而 $A+B=I_2$ 的秩为 2，$A+(-A)=O$ 的秩为 0。
* **补充（常用不等式）**：$\text{rank}(A+B)\le\text{rank}\,A+\text{rank}\,B$，因为 $\text{Col}(A+B)\subseteq\text{Col}\,A+\text{Col}\,B$。

#### 🌟 课件随堂例题与解析 (Lecture Examples)

###### 【课件例题 1】标准基下的坐标
**Problem**: 设 $\mathcal{E}=\{\mathbf{e}_1,\mathbf{e}_2\}$ 是 $\mathbb{R}^2$ 的标准基，求 $\mathbf{x}=\begin{bmatrix}1\\6\end{bmatrix}$ 相对 $\mathcal{E}$ 的坐标向量。

* **Process (解题步骤)**:
  $$\mathbf{x}=1\mathbf{e}_1+6\mathbf{e}_2\ \Longrightarrow\ [\mathbf{x}]_{\mathcal{E}}=\begin{bmatrix}1\\6\end{bmatrix}.$$
* **中文详解**:
  标准基下“坐标”就是分量本身，这是坐标概念最平凡的情形，用来作为后面非标准基的对照。注意 $[\mathbf{x}]_{\mathcal{E}}$ 与 $\mathbf{x}$ 数值相同，但这只是因为 $\mathcal{E}$ 恰好是标准基。

---

###### 【课件例题 2】由坐标向量还原向量
**Problem**: 设 $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2\}$ 是 $\mathbb{R}^2$ 的基，$\mathbf{b}_1=\begin{bmatrix}1\\0\end{bmatrix}$，$\mathbf{b}_2=\begin{bmatrix}1\\2\end{bmatrix}$，且 $[\mathbf{x}]_{\mathcal{B}}=\begin{bmatrix}-2\\3\end{bmatrix}$，求 $\mathbf{x}$。

* **Process (解题步骤)**:
  $$\mathbf{x}=-2\mathbf{b}_1+3\mathbf{b}_2=-2\begin{bmatrix}1\\0\end{bmatrix}+3\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}1\\6\end{bmatrix}.$$
* **中文详解**:
  由坐标向量还原 $\mathbf{x}$ 就是按定义作线性组合。与例题 1 对照可见：同一个向量 $(1,6)^T$ 在标准基下坐标是 $(1,6)^T$，在 $\mathcal{B}$ 下坐标是 $(-2,3)^T$——坐标随基而变，向量本身不变。这也是考试中最常见的“双向”考点。

---

###### 【课件例题 3】求坐标向量
**Problem**: 设 $\mathbf{b}_1=\begin{bmatrix}2\\1\end{bmatrix}$，$\mathbf{b}_2=\begin{bmatrix}-1\\1\end{bmatrix}$，$\mathbf{x}=\begin{bmatrix}4\\5\end{bmatrix}$，$\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2\}$，求 $[\mathbf{x}]_{\mathcal{B}}$。

* **Process (解题步骤)**:
  需要 $c_1,c_2$ 使 $c_1\mathbf{b}_1+c_2\mathbf{b}_2=\mathbf{x}$，即
  $$\begin{cases}2c_1-c_2=4\\ c_1+c_2=5\end{cases}\ \Longrightarrow\ \begin{bmatrix}2&-1\\1&1\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix}=\begin{bmatrix}4\\5\end{bmatrix}\ \Longrightarrow\ \begin{bmatrix}c_1\\c_2\end{bmatrix}=\begin{bmatrix}3\\2\end{bmatrix}.$$
  故 $[\mathbf{x}]_{\mathcal{B}}=\begin{bmatrix}3\\2\end{bmatrix}$。
* **中文详解**:
  按定义解方程即可；因为 $\det\begin{bmatrix}2&-1\\1&1\end{bmatrix}=3\ne 0$，系数矩阵可逆，解唯一，与唯一表示定理一致。也可用 $[\mathbf{x}]_{\mathcal{B}}=P_{\mathcal{B}}^{-1}\mathbf{x}$ 计算。最后回代 $3(2,1)^T+2(-1,1)^T=(4,5)^T$ 验证。

---

###### 【课件例题 4】求参数形式子空间的维数
**Problem**: 求
$$H=\left\{\begin{bmatrix}a-3b+6c\\ 5a+4d\\ b-2c-d\\ 5d\end{bmatrix}:a,b,c,d\in\mathbb{R}\right\}$$
的维数。

* **Process (解题步骤)**:
  分离参数得 $H=\text{Span}\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3,\mathbf{v}_4\}$，其中
  $$\mathbf{v}_1=\begin{bmatrix}1\\5\\0\\0\end{bmatrix},\quad \mathbf{v}_2=\begin{bmatrix}-3\\0\\1\\0\end{bmatrix},\quad \mathbf{v}_3=\begin{bmatrix}6\\0\\-2\\0\end{bmatrix},\quad \mathbf{v}_4=\begin{bmatrix}0\\4\\-1\\5\end{bmatrix}.$$
  因为 $\mathbf{v}_3=-2\mathbf{v}_2$，可删去 $\mathbf{v}_3$，得 $H=\text{Span}\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_4\}$。以它们为列作矩阵并行化简：
  $$A=[\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_4]=\begin{bmatrix}1&-3&0\\5&0&4\\0&1&-1\\0&0&5\end{bmatrix}\sim\begin{bmatrix}1&-3&0\\0&1&-1\\0&0&19\\0&0&0\end{bmatrix}.$$
  三列全是主元列，故 $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_4\}$ 线性无关，是 $H$ 的基，$\dim H=3$。
* **中文详解**:
  标准流程是“分离参数 → 得生成集 → 删去冗余向量 → 对剩下的向量作无关性检验”。删去 $\mathbf{v}_3$ 的依据是 $\mathbf{v}_3=-2\mathbf{v}_2$，从分量上直接可见，不必再算。$H\subseteq\mathbb{R}^4$ 但 $\dim H=3$，说明 $H$ 是 $\mathbb{R}^4$ 中过原点的三维超平面。

---

###### 【课件例题 5】用基定理判断一组向量是否为基
**Problem**: 设 $H=\left\{\begin{bmatrix}x\\y\\0\end{bmatrix}:x,y\in\mathbb{R}\right\}$，$\mathbf{u}=\begin{bmatrix}1\\1\\0\end{bmatrix}$，$\mathbf{v}=\begin{bmatrix}1\\-1\\0\end{bmatrix}$。证明 $\{\mathbf{u},\mathbf{v}\}$ 是 $H$ 的基。

* **Process (解题步骤)**:
  显然 $H=\text{Span}\left\{\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\1\\0\end{bmatrix}\right\}$，故 $\dim H=2$。又 $\mathbf{u},\mathbf{v}\in H$，且二者不成比例，故线性无关。它们恰有 $2=\dim H$ 个，由基定理，$\{\mathbf{u},\mathbf{v}\}$ 自动是 $H$ 的基。
* **中文详解**:
  若按定义做，还要验证 $\text{Span}\{\mathbf{u},\mathbf{v}\}=H$（即 $H$ 中任意向量都能写成 $a\mathbf{u}+b\mathbf{v}$），计算量更大。基定理把“无关 + 张成”两条合并成一条：个数对了，只需证其中一条。注意个数必须**恰好是 2**。

---

###### 【课件例题 6】由参数解求零空间的维数
**Problem**: 设 $A\mathbf{x}=\mathbf{0}$ 的解恰为
$$\mathbf{x}=s\begin{bmatrix}-6\\1\\0\end{bmatrix}+t\begin{bmatrix}0\\4\\1\end{bmatrix},\qquad s,t\in\mathbb{R}.$$
求 $\dim\text{Nul}\,A$，并说明 $\text{Nul}\,A$ 的几何形状。

* **Process (解题步骤)**:
  令 $\mathbf{u}=(-6,1,0)^T$，$\mathbf{v}=(0,4,1)^T$，则 $\text{Nul}\,A=\text{Span}\{\mathbf{u},\mathbf{v}\}$。$\mathbf{u},\mathbf{v}$ 不成比例，故线性无关，$\{\mathbf{u},\mathbf{v}\}$ 是 $\text{Nul}\,A$ 的基，$\dim\text{Nul}\,A=2$。
* **中文详解**:
  参数个数 = 自由变量个数 = 基向量个数 = 零空间维数。$\text{Nul}\,A$ 是 $\mathbb{R}^3$ 中过原点的平面（2 维），这与“两个自由参数”一致。考试中只要把解写成参数向量形式，基和维数就同时读出来了。

---

###### 【课件例题 7】由行化简同时读出 $\dim\text{Col}\,A$ 与 $\dim\text{Nul}\,A$
**Problem**: 设
$$A=\begin{bmatrix}2&5&-3&-4&8\\ 4&7&-4&-3&9\\ 6&9&-5&2&4\\ 0&-9&6&5&-6\end{bmatrix}\sim\begin{bmatrix}2&5&-3&-4&8\\ 0&-3&2&5&-7\\ 0&0&0&4&-6\\ 0&0&0&0&0\end{bmatrix}.$$
求 $\dim\text{Col}\,A$ 与 $\dim\text{Nul}\,A$。

* **Process (解题步骤)**:
  主元列为第 $1,2,4$ 列，对应基本变量 $x_1,x_2,x_4$；原矩阵的第 $1,2,4$ 列构成 $\text{Col}\,A$ 的基，故
  $$\dim\text{Col}\,A=3.$$
  非主元列为第 $3,5$ 列，对应自由变量 $x_3,x_5$，每个自由变量给出 $\text{Nul}\,A$ 的一个基向量，故
  $$\dim\text{Nul}\,A=2.$$
  校验：$n=5=3+2$。
* **中文详解**:
  这是本节最核心的一张“对照表”：主元列 ↔ 基本变量 ↔ $\text{Col}\,A$ 的基；非主元列 ↔ 自由变量 ↔ $\text{Nul}\,A$ 的基。两组个数相加恰好是列数 $n$，这正是秩定理的直观来源。注意列空间的基要回到**原矩阵**取对应列（行变换改变列空间）。

---

###### 【课件例题 8】用秩定理判断可行性
**Problem**: (1) 若 $7\times 9$ 矩阵 $A$ 的零空间是 2 维，求 $\text{rank}\,A$。(2) $6\times 9$ 矩阵 $A$ 能否有 2 维零空间？

* **Process (解题步骤)**:
  (1) 由秩定理 $\text{rank}\,A+\dim\text{Nul}\,A=9$，故 $\text{rank}\,A=9-2=7$。
  (2) 若 $\dim\text{Nul}\,A=2$，则同样有 $\text{rank}\,A=7$；但 $6\times 9$ 矩阵满足 $\text{rank}\,A\le\min\{6,9\}=6$，矛盾，故不可能。
* **中文详解**:
  秩定理给出“秩 + 零空间维数 = 列数”这一条约束；$\text{rank}\,A\le\min\{m,n\}$ 是第二条约束。判断“是否存在这样的矩阵”时，必须两条都检查：先用秩定理算出所需秩，再检查它是否超过 $\min\{m,n\}$。本题 (2) 中 $7>6$，所以无论怎么选矩阵都造不出来。

---

###### 【课件例题 9】秩不可加
**Problem**: 设 $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$，$B=\begin{bmatrix}0&0\\0&1\end{bmatrix}$。比较 $\text{rank}(A+B)$、$\text{rank}(A+I_2)$、$\text{rank}(2A)$、$\text{rank}(A+(-A))$。

* **Process (解题步骤)**:
  $\text{rank}\,A=\text{rank}\,B=1$。而
  $$A+B=\begin{bmatrix}1&0\\0&1\end{bmatrix}\Rightarrow\text{rank}(A+B)=2,\qquad A+I_2=\begin{bmatrix}2&0\\0&1\end{bmatrix}\Rightarrow\text{rank}(A+I_2)=2,$$
  $$2A=\begin{bmatrix}2&0\\0&0\end{bmatrix}\Rightarrow\text{rank}(2A)=1,\qquad A+(-A)=O\Rightarrow\text{rank}(A+(-A))=0.$$
* **中文详解**:
  这些例子说明“秩不可加”：两个秩为 1 的矩阵之和，秩可以是 2、1 甚至 0。正确的关系只有不等式 $\text{rank}(A+B)\le\text{rank}\,A+\text{rank}\,B$，本题中 $2\le 1+1$ 取等。另外注意数乘保持秩（$c\ne0$），加法不保持。

---

💡 **学习建议与复习提示**：  
* 坐标向量三步：确认基 → 解 $c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p=\mathbf{x}$ → 写成 $[\mathbf{x}]_{\mathcal{B}}$。  
* 维数 = 基向量个数；$\dim\{\mathbf{0}\}=0$、$\dim\mathbb{R}^n=n$，别把分量个数当维数。  
* 基定理省力：已知 $\dim H=p$ 时，$p$ 个向量只需证“线性无关”或“张成”之一。  
* $\dim\text{Col}\,A$ 数主元列，$\dim\text{Nul}\,A$ 数非主元列，两者之和 = 列数 $n$。  
* 秩定理中的 $n$ 永远是**列数**，不是行数；另外别忘 $\text{rank}\,A\le\min\{m,n\}$。  
* 遇到“是否存在这样的矩阵”：先用秩定理求所需秩，再用秩的上界检查是否矛盾。  
* 秩与运算：数乘、转置、可逆矩阵求逆都保持秩；乘积秩不超过两者较小者；加法**没有**等式关系。
