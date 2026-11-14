# Chapter 1 Preliminaries: Functions 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 1 Summary)

---

### 1.5 Functions and Their Graphs (函数及其图像)

* **函数的严谨定义 (Definition of Functions):** 设 $\mathbb{R}$ 为实数集，自变量 $x$ 所在的非空集合记为 $D$。函数 (**function**) 是从集合 $D$ 到 $\mathbb{R}$ 的一种对应法则 $f$，它为 $D$ 中的每一个元素 $x$ 指定了一个**唯一**的实数 $y$ 作为输出。
    * 其中，输入值 $x$ 称为自变量 (**independent variable**)，输出值 $y$ 称为因变量 (**dependent variable**)。
* **定义域与值域 (Domain & Range):**
    * **定义域 (Domain):** 集合 $D$ 称为该函数的定义域，通常记作 $D(f)$ 或 $D_f$。
    * **值域 (Range):** 因变量 $y$ 能够取到的所有可能值的集合称为值域，记作 $R(f)$ 或 $R_f$，即 $R(f) = \{y : y = f(x), x \in D(f)\}$。
    * **自然定义域 (Natural Domain):** 在未明确给出定义域的情况下，我们默认函数的定义域是使该函数表达式有数学意义的所有实数构成的最大集合。例如：对于分式，分母不能为 0；对于偶次根号，被开方数必须非负。
* **分段函数 (Piecewise-defined function):** 这类函数在定义域的不同区间内，由不同的数学表达式来定义。常见的分段函数包括：
    * 绝对值函数 (**Absolute value function**): $y = |x|$。
    * 符号函数 (**Signum function**): $y = \text{sgn}(x)$。
    * 最大整数函数/取整函数 (**Greatest integer function**): $y = [x] = \max\{n \in \mathbb{Z} \mid n \le x\}$。

---

### 1.6 Operations on Functions (函数的运算)

* **函数的代数运算 (Algebraic Operations):** 给定两个函数 $f$ 和 $g$，它们的定义域交集为 $D = D(f) \cap D(g)$。在这个交集上，我们可以定义以下运算：
    * **加法 (Sum):** $(f + g)(x) = f(x) + g(x)$。
    * **减法 (Difference):** $(f - g)(x) = f(x) - g(x)$。
    * **乘法 (Product):** $(f \cdot g)(x) = f(x) \cdot g(x)$。
    * **除法 (Quotient):** $(f/g)(x) = f(x) / g(x)$，前提是 $g(x) \neq 0$。
    * **乘方 (Power):** $f^n(x) = [f(x)]^n$。
* **复合函数 (Composition of Functions):** 
    * 定义为 $(g \circ f)(x) = g(f(x))$，表示 $g$ 与 $f$ 的复合。
    * 计算顺序为“由内而外”：先将输入 $x$ 代入内层函数 $f$，得到输出 $f(x)$，再将 $f(x)$ 作为输入代入外层函数 $g$。
    * 复合函数的定义域 $D(g \circ f) = \{x \mid x \in D(f) \text{ 且 } f(x) \in D(g)\}$。
    * **分解复合函数 (Decomposition):** 在分析复杂函数时，需要“由外而内”层层剥离。例如 $y = \ln(\sin(1/\sqrt{x^2+1}))$，最内层是 $t = x^2+1$，然后是 $v = t^{-1/2}$，接着是 $u = \sin v$，最外层是 $y = \ln u$。
* **反函数 (The Inverse of a Function):**
    * **一对一函数 (One-to-one Function, 1-1):** 如果对于定义域内任意两个不相等的输入值 $x_1 \neq x_2$，总有 $f(x_1) \neq f(x_2)$，则该函数是一对一的。
    * **水平线测试 (Horizontal Line Test):** 如果任何一条水平线与函数图像的交点最多只有一个，那么这个函数就是一对一函数，从而存在反函数。
    * （补充对比）**垂直线测试 (Vertical Line Test):** 如果任何一条垂直线与图像的交点最多只有一个，那么该图像代表一个函数。
    * **求反函数的三个步骤:** 1. 写出 $y = f(x)$ 并解出 $x$ 关于 $y$ 的表达式； 2. 将表达式中的 $x$ 和 $y$ 互换，得到 $f^{-1}(x)$； 3. 确定反函数的定义域。
    * **反函数的性质 (Properties):** 原函数 $f$ 的值域即为反函数 $f^{-1}$ 的定义域，即 $D(f^{-1}) = R(f)$。它们满足抵消方程 (**Cancellation Equations**): $f^{-1}(f(x)) = x$ 以及 $f(f^{-1}(y)) = y$。
    * **警告:** $f^{-1}(x)$ 表示反函数，绝不等于 $1/f(x)$（倒数）。
* **函数分类 (Catalog of Functions):**
    * **基本初等函数 (Basic Elementary Functions):** 常数函数 (**Constant**)、幂函数 (**Power**)、指数函数 (**Exponential**)、对数函数 (**Logarithmic**)、三角函数 (**Trigonometric**) 和反三角函数 (**Inverse Trigonometric**)。
    * 由上述基本初等函数经过有限次代数运算和复合操作构成的函数称为初等函数 (**Elementary Functions**)。

---

### 1.7 Exponential and Logarithmic Functions (指数与对数函数)

* **指数函数 (Exponential Functions):** 形式为 $f(x) = a^x$ (底数 $a>0, a \neq 1$)。其定义域为全体实数 $(-\infty, \infty)$，值域为正实数 $(0, \infty)$。
    * 指数运算性质：$a^x a^y = a^{x+y}$，$(a^x)^y = a^{xy}$，$a^{-x} = 1/a^x$ 等。
* **对数函数 (Logarithmic Functions):** $f(x) = \log_a x$ 是 $a^x$ 的反函数。其定义域为 $(0, \infty)$，值域为 $(-\infty, \infty)$。
    * **换底公式 (Change of Base Formula):** $\log_c b = \frac{\log_a b}{\log_a c}$。
    * 以自然常数 $e$ 为底的对数称为自然对数 (**natural logarithm**)，记作 $\ln x$；以 $10$ 为底的称为常用对数 (**common logarithm**)，记作 $\log_{10} x$ 或 $\lg x$。

---

### 1.8 The Trigonometric Functions (三角函数)

* **基础定义 (Definitions):** 可以通过直角三角形（对边 **opposite**、邻边 **adjacent**、斜边 **hypotenuse**）或单位圆 (**unit circle**) 来定义 $\sin \theta, \cos \theta, \tan \theta$。
* **正割与余割 (Secant & Cosecant):** 
    * 正割 $\sec x = 1/\cos x$，定义域排除 $x = k\pi + \pi/2$，值域为 $(-\infty, -1] \cup [1, \infty)$。
    * 余割 $\csc x = 1/\sin x$，定义域排除 $x = k\pi$，值域同为 $(-\infty, -1] \cup [1, \infty)$。
* **核心三角恒等式 (Trigonometric Identities):**
    * **勾股恒等式 (Pythagorean Identities):** $\sin^2 x + \cos^2 x = 1$；$1 + \tan^2 x = \sec^2 x$；$1 + \cot^2 x = \csc^2 x$。
    * **倍角公式 (Double-Angle Identities):** $\sin 2x = 2\sin x \cos x$；$\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$。

---

### 1.9 The Inverse Trigonometric Functions (反三角函数)

* **反余弦函数 (Inverse Cosine):** 记作 $y = \cos^{-1} x$ 或 $\arccos x$。为了使其成为一对一函数，我们将 $\cos x$ 的定义域限制在 $[0, \pi]$。因此，$\arccos x$ 的定义域是 $[-1, 1]$，值域是主值区间 $[0, \pi]$。
* **复合函数恒等式 (Composite Function Identities):** 可以利用直角三角形辅助推导。例如，令 $\theta = \cos^{-1} x$，则 $\cos \theta = x$，根据勾股定理可得出 $\sin(\cos^{-1} x) = \sqrt{1 - x^2}$，同理 $\sec(\tan^{-1} x) = \sqrt{1 + x^2}$。
* **抵消公式的陷阱 (Cancellation Formulas Warning):** 公式 $\sin^{-1}(\sin x) = x$ **并不是**对所有实数 $x$ 都成立。它仅仅在受限主值区间 $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ 时才成立。如果 $x$ 超出此范围（例如 $x = 9\pi/7$），必须先利用三角函数的周期性和对称性将其转换回主值区间，再求解。
