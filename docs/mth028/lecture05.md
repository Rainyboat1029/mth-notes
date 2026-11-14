# MTH028 线性代数 I (Linear Algebra I) 学习笔记

**课程主题**：Section 1.8 & 1.9 线性变换简介与线性变换的矩阵 (Introduction to Linear Transformations and The Matrix of a Linear Transformation)  
**适用目的**：自学、预习与复习  

---

## 第一部分：本节课知识详解 (Lecture 5 Summary)

### Section 1.8 线性变换简介 (Introduction to Linear Transformations)

#### 1. 从矩阵向量乘积到映射视角 (From Matrix Multiplication to Mapping)

在前面的课程中，对于线性方程组对应的矩阵方程 $A\mathbf{x} = \mathbf{b}$，我们有两种理解方式：
1. **矩阵与向量的乘积**：$A\mathbf{x}$ 是矩阵 $A$ 与向量 $\mathbf{x}$ 的乘法运算。
2. **列向量的线性组合**：$A\mathbf{x}$ 是以 $\mathbf{x}$ 的各分量为权重，对 $A$ 的列向量作的线性组合。

现在，我们将矩阵 $A$ 视为固定的，而让向量 $\mathbf{x}$ 变化。此时对应一个对应法则：
$$T : \mathbf{x} \longmapsto A\mathbf{x}$$
该规则将输入的向量 $\mathbf{x}$ 变换（或映射）为输出的向量 $\mathbf{b}$。这提供了对 $A\mathbf{x}$ 的**第三种几何与函数视角——映射视角**。

#### 2. 变换/映射的基本定义与术语 (Definitions & Terminologies)
* **变换 / 映射 / 函数 (Transformation / Mapping / Function)**：  
  从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的变换 $T$ 是一个规则，它为 $\mathbb{R}^n$ 中的每个向量 $\mathbf{x}$ 指定 $\mathbb{R}^m$ 中唯一确定的向量 $T(\mathbf{x})$，记作 $T: \mathbb{R}^n \longrightarrow \mathbb{R}^m$。
* **定义域 (Domain)**：输入向量集 $\mathbb{R}^n$ 称为变换 $T$ 的**定义域**。
* **陪域 (Codomain)**：输出向量所在的整体空间 $\mathbb{R}^m$ 称为变换 $T$ 的**陪域**。
* **像 (Image)**：对于 $\mathbf{x} \in \mathbb{R}^n$，向量 $T(\mathbf{x}) \in \mathbb{R}^m$ 称为 $\mathbf{x}$ 在 $T$ 作用下的**像**。
* **值域 (Range)**：所有像 $T(\mathbf{x})$ 构成的集合称为 $T$ 的**值域**，即 $\text{Range } T = \{T(\mathbf{x}) : \mathbf{x} \in \mathbb{R}^n\}$。  
  *注意*：值域是陪域 $\mathbb{R}^m$ 的子集，不一定等于整个陪域。

---

#### 3. 线性变换的定义与重要性质 (Linear Transformations & Properties)
* **定义 (Definition)**：  
  一个变换（或映射） $T$ 称为**线性的 (Linear)**，如果它满足以下两条基本公理：
  1. 对 $T$ 的定义域中的任意向量 $\mathbf{u}, \mathbf{v}$，均有：
     $$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$$
  2. 对任意标量 $c$ 及 $T$ 的定义域中的任意向量 $\mathbf{u}$，均有：
     $$T(c\mathbf{u}) = cT(\mathbf{u})$$

* **重要推论性质 (Derived Properties)**：  
  若 $T$ 是线性变换，则：
  1. **零向量映射为零向量**：
     $$T(\mathbf{0}) = \mathbf{0}$$
  2. **保持线性组合 (Preserving Linear Combinations)**：  
     对定义域中的任意向量 $\mathbf{v}_1, \dots, \mathbf{v}_p$ 及任意标量 $c_1, \dots, c_p$：
     $$T(c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_p\mathbf{v}_p) = c_1 T(\mathbf{v}_1) + c_2 T(\mathbf{v}_2) + \dots + c_p T(\mathbf{v}_p)$$

* ⚠️ **避坑特别提示 (Warning)**：  
  在实数域上，函数 $f(x) = ax$ ($a \in \mathbb{R}$) 是线性变换，但函数 $f(x) = ax + b$ （当 $b \neq 0$ 时）**不是**线性变换（它是仿射变换，因为 $f(0) = b \neq 0$）。

---

#### 4. 矩阵变换 (Matrix Transformations)
由定理 5（矩阵向量乘积的线性性质），对任意 $m \times n$ 矩阵 $A$，定义变换 $T_A(\mathbf{x}) = A\mathbf{x}$：
* 变换 $T_A : \mathbb{R}^n \longrightarrow \mathbb{R}^m$ 必然是一个**线性变换**，称为**矩阵变换 (Matrix Transformation)**。
* 其定义域为 $\mathbb{R}^n$，陪域为 $\mathbb{R}^m$。
* 其值域为矩阵 $A$ 的列向量的**张成空间 (Span)**，即 $\text{Range } T_A = \text{Span}\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}$。

---

#### 🌟 课件随堂例题与解析 (Lecture Examples)

##### 【课件例题 1】判断变换是否为线性变换
**Problem**: Which of the following transformations $T: \mathbb{R}^3 \to \mathbb{R}^3$ are linear?
$$T_1\left(\begin{bmatrix} s \\ t \\ h \end{bmatrix}\right) = \begin{bmatrix} 0 \\ t \\ h \end{bmatrix}, \quad T_2\left(\begin{bmatrix} s \\ t \\ h \end{bmatrix}\right) = \begin{bmatrix} s+h \\ 0 \\ -5t \end{bmatrix}, \quad T_3\left(\begin{bmatrix} s \\ t \\ h \end{bmatrix}\right) = \begin{bmatrix} s+3 \\ t-1 \\ h+2 \end{bmatrix}$$

* **Process (解题步骤)**:
  1. For $T_1$: $T_1(\mathbf{x}) = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s \\ t \\ h \end{bmatrix}$. Since it can be written as $A\mathbf{x}$, $T_1$ is linear.
  2. For $T_2$: $T_2(\mathbf{x}) = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & -5 & 0 \end{bmatrix} \begin{bmatrix} s \\ t \\ h \end{bmatrix}$. Since it is a matrix transformation, $T_2$ is linear.
  3. For $T_3$: Evaluate $T_3(\mathbf{0}) = T_3\left(\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}\right) = \begin{bmatrix} 3 \\ -1 \\ 2 \end{bmatrix} \neq \mathbf{0}$. Since a linear transformation must send $\mathbf{0}$ to $\mathbf{0}$, $T_3$ is **not** linear.
* **中文详解**:
  $T_1$ 和 $T_2$ 均可改写为矩阵与向量相乘的形式（矩阵变换），因此符合加法与数乘公理，是线性变换；而 $T_3$ 在零向量作用下的像 $T_3(\mathbf{0}) = [3, -1, 2]^T \neq \mathbf{0}$，违反了线性变换必须将零向量映射为零向量的性质，故不是线性变换。

---

##### 【课件例题 2】矩阵变换应用
**Problem**: Let $A = \begin{bmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \end{bmatrix}$, $\mathbf{u} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 3 \\ 2 \\ -5 \end{bmatrix}$, $\mathbf{c} = \begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix}$, and define $T(\mathbf{x}) = A\mathbf{x}$.
a. Find $T(\mathbf{u})$, the image of $\mathbf{u}$ under $T$.  
b. Find an $\mathbf{x} \in \mathbb{R}^2$ whose image under $T$ is $\mathbf{b}$.  
c. Is there more than one $\mathbf{x}$ whose image under $T$ is $\mathbf{b}$?  
d. Determine if $\mathbf{c}$ is in the range of the transformation $T$.

* **Process (解题步骤)**:
  a. $T(\mathbf{u}) = A\mathbf{u} = \begin{bmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 2(1) - 1(-3) \\ 2(3) - 1(5) \\ 2(-1) - 1(7) \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \\ -9 \end{bmatrix}$.
  
  b. Solve $A\mathbf{x} = \mathbf{b}$. Row reduce the augmented matrix $[A \mid \mathbf{b}]$:
     $$\begin{bmatrix} 1 & -3 & 3 \\ 3 & 5 & 2 \\ -1 & 7 & -5 \end{bmatrix} \xrightarrow{\substack{R_2 \leftarrow R_2 - 3R_1 \\ R_3 \leftarrow R_3 + R_1}} \begin{bmatrix} 1 & -3 & 3 \\ 0 & 14 & -7 \\ 0 & 4 & -2 \end{bmatrix} \xrightarrow{R_2 \leftarrow \frac{1}{14}R_2} \begin{bmatrix} 1 & -3 & 3 \\ 0 & 1 & -1/2 \\ 0 & 4 & -2 \end{bmatrix} \xrightarrow{R_3 \leftarrow R_3 - 4R_2} \begin{bmatrix} 1 & -3 & 3 \\ 0 & 1 & -1/2 \\ 0 & 0 & 0 \end{bmatrix}$$
     From Row 2: $x_2 = -1/2$. From Row 1: $x_1 - 3(-1/2) = 3 \implies x_1 = 3/2$.  
     Thus, $\mathbf{x} = \begin{bmatrix} 3/2 \\ -1/2 \end{bmatrix}$.
  
  c. Since the system $A\mathbf{x} = \mathbf{b}$ has no free variables (both columns of $A$ are pivot columns), the solution $\mathbf{x}$ is **unique**. There is no other $\mathbf{x}$.
  
  d. Row reduce $[A \mid \mathbf{c}]$:
     $$\begin{bmatrix} 1 & -3 & 3 \\ 3 & 5 & 2 \\ -1 & 7 & 5 \end{bmatrix} \xrightarrow{\substack{R_2 \leftarrow R_2 - 3R_1 \\ R_3 \leftarrow R_3 + R_1}} \begin{bmatrix} 1 & -3 & 3 \\ 0 & 14 & -7 \\ 0 & 4 & 8 \end{bmatrix} \xrightarrow{R_3 \leftarrow R_3 - \frac{2}{7}R_2} \begin{bmatrix} 1 & -3 & 3 \\ 0 & 14 & -7 \\ 0 & 0 & 10 \end{bmatrix}$$
     Row 3 corresponds to $0 = 10$, which is inconsistent. Thus, $\mathbf{c}$ is **not** in the range of $T$.

---

### Section 1.9 线性变换的矩阵 (The Matrix of a Linear Transformation)

#### 1. 标准矩阵 (The Standard Matrix - Theorem 10)
* **核心定理 (Theorem 10)**：  
  设 $T : \mathbb{R}^n \longrightarrow \mathbb{R}^m$ 为线性变换。则存在**唯一**的 $m \times n$ 矩阵 $A$，使得对 $\mathbb{R}^n$ 中的每个向量 $\mathbf{x}$，均有：
  $$T(\mathbf{x}) = A\mathbf{x}$$
  事实上，矩阵 $A$ 的第 $j$ 列是向量 $\mathbf{e}_j$ 在 $T$ 作用下的像：
  $$A = \begin{bmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) & \dots & T(\mathbf{e}_n) \end{bmatrix}$$
  其中 $\mathbf{e}_j$ 是 $n \times n$ 单位矩阵 $I_n$ 的第 $j$ 列。矩阵 $A$ 称为 $T$ 的**标准矩阵 (Standard Matrix)**。

---

#### 2. $\mathbb{R}^2$ 中常见的几何变换 (Geometric Transformations in $\mathbb{R}^2$)

##### (1) 投影 (Projections)
* **投影到 $x_1 x_2$-平面 (在 $\mathbb{R}^3$ 中)**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}\right) = \begin{bmatrix} x_1 \\ x_2 \\ 0 \end{bmatrix}, \quad A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

##### (2) 反射 (Reflections in $\mathbb{R}^2$)
* **关于 $x_2$ 轴（纵轴）反射**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = \begin{bmatrix} -x_1 \\ x_2 \end{bmatrix}, \quad A = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$
* **关于 $x_1$ 轴（横轴）反射**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = \begin{bmatrix} x_1 \\ -x_2 \end{bmatrix}, \quad A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
* **关于直线 $x_2 = x_1$ 反射**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = \begin{bmatrix} x_2 \\ x_1 \end{bmatrix}, \quad A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$
* **关于直线 $x_2 = -x_1$ 反射**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = \begin{bmatrix} -x_2 \\ -x_1 \end{bmatrix}, \quad A = \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$$
* **关于原点反射**：
  $$T\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = \begin{bmatrix} -x_1 \\ -x_2 \end{bmatrix}, \quad A = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$

##### (3) 旋转 (Rotations in $\mathbb{R}^2$)
* **绕原点逆时针旋转 $\theta$ 角**：  
  单位向量的像是：$T(\mathbf{e}_1) = \begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$， $T(\mathbf{e}_2) = \begin{bmatrix} -\sin\theta \\ \cos\theta \end{bmatrix}$。  
  标准矩阵为：
  $$A = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
  * 特例：当 $\theta = 90^\circ$ ($\frac{\pi}{2}$) 时，$A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$。

---

#### 3. 单射与满射的概念 (One-to-One and Onto Mappings)

对于映射 $T : \mathbb{R}^n \longrightarrow \mathbb{R}^m$：
* **满射 (Onto / Surjective)**：  
  如果陪域 $\mathbb{R}^m$ 中的**每个**向量 $\mathbf{b}$ **至少是** $\mathbb{R}^n$ 中某一个向量 $\mathbf{x}$ 的像，则称 $T$ 为**满射**。  
  等价条件：$T$ 的值域等于整个陪域，即 $\text{Range } T = \mathbb{R}^m$。
* **单射 / 一对一 (One-to-One / Injective)**：  
  如果陪域 $\mathbb{R}^m$ 中的**每个**向量 $\mathbf{b}$ **至多是** $\mathbb{R}^n$ 中某一个向量 $\mathbf{x}$ 的像，则称 $T$ 为**单射**。  
  等价条件：$T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}$。

##### 单射的判定定理 (Theorem 11)
* 线性变换 $T : \mathbb{R}^n \longrightarrow \mathbb{R}^m$ 是**单射**，**当且仅当**齐次方程：
  $$T(\mathbf{x}) = \mathbf{0}$$
  **只有平凡解** $\mathbf{x} = \mathbf{0}$。

##### 矩阵判定准则 (Theorem 12)
设 $T : \mathbb{R}^n \longrightarrow \mathbb{R}^m$ 是线性变换，$A$ 为 $T$ 的标准矩阵。则：
a. $T$ 把 $\mathbb{R}^n$ 映射**到 $\mathbb{R}^m$ 上（满射）** $\iff A$ 的列向量张成 $\mathbb{R}^m$ $\iff A$ 的**每一行都有主元**。
b. $T$ 是**一对一映射（单射）** $\iff A$ 的列向量**线性无关** $\iff A$ 的**每一列都有主元**。

##### 维数对映射性质的限制 (Dimensions Restrict Possibilities)
设 $A$ 是线性变换 $T : \mathbb{R}^n \longrightarrow \mathbb{R}^m$ 的 $m \times n$ 标准矩阵：
1. **若 $n > m$**（定义域维数大于陪域）：$A$ 的列数大于行数，必有自由变量，故 $T$ **绝不是单射**。
2. **若 $n < m$**（定义域维数小于陪域）：$A$ 的行数大于列数，不可能每行都有主元，故 $T$ **绝不是满射**。
3. **若 $T$ 既是单射又是满射**：则必有 $n = m$（但 $n = m$ 本身不能保证单射或满射）。

---

💡 **学习建议与复习提示**：  
* 熟练掌握由变换表达式构建标准矩阵 $A = [T(\mathbf{e}_1) \ \ \dots \ \ T(\mathbf{e}_n)]$ 的方法。  
* 深刻理解几何变换（反射、旋转、投影）的矩阵表示。  
* 牢记定理 12：**满射看行主元（张成），单射看列主元（线性无关）**。
