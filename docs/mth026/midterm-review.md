# MTH026 Calculus 期中复习笔记 (Midterm Review Notes): Lectures 1–6 核心知识详解与典型例题

> 覆盖范围：Lecture 1（§1.5–1.9 函数与预备知识）、Lecture 2（§2.1、2.3 极限）、Lecture 3（§2.4、2.5 无穷极限与三角极限）、Lecture 4（§2.6、2.7 指数对数极限、连续性与介值定理）、Lecture 5（§3.1–3.6 导数与求导法则）、Lecture 6（§3.9、3.10、3.7、3.8 指数对数与反三角导数、隐微分、对数求导、相关变化率）。
>
> 使用建议：先背**第零部分**的术语表（期中选择题与计算题都直接考英文术语）；再按章节过定义、定理与公式；最后看每章末的**典型例题**（全部取自 Assignment 1–6 的同型题）。

---

## 第零部分：核心术语速查表 (Key Terminology Table)

> 表中「公式/考点」一列为考前必须能默写的结论或易错点。

### 0.1 函数与预备知识 (Chapter 1: Functions)

| English Term | 中文 | 含义 / 公式 / 考点 |
| :--- | :--- | :--- |
| function | 函数 | 对定义域内每个 $x$ 指定**唯一**的 $y$ |
| independent / dependent variable | 自变量 / 因变量 | 输入 $x$ / 输出 $y$ |
| domain | 定义域 | 记作 $D(f)$ |
| range | 值域 | $R(f)=\{y:y=f(x),\ x\in D(f)\}$ |
| natural domain | 自然定义域 | 使表达式有意义的**最大**实数集：分母 $\neq 0$、偶次根号内 $\ge 0$、对数真数 $>0$、$\arcsin/\arccos$ 内 $\in[-1,1]$ |
| piecewise-defined function | 分段函数 | 不同区间用不同表达式，常用 $[\ ]$ 取整 |
| absolute value function | 绝对值函数 | $\lvert x\rvert$ |
| signum function | 符号函数 | $\operatorname{sgn} x$，取 $-1,0,1$ |
| greatest integer function / floor | 取整函数（下取整） | $[x]=\lfloor x\rfloor=\max\{n\in\mathbb{Z}:n\le x\}$ |
| composition | 复合函数 | $(g\circ f)(x)=g(f(x))$；定义域要求 $x\in D(f)$ 且 $f(x)\in D(g)$ |
| decomposition | 复合函数分解 | 由外而内层层剥离 |
| one-to-one (1-1) function | 一对一函数 | $x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2)$ |
| horizontal line test | 水平线测试 | 判断是否 1-1（从而有反函数） |
| vertical line test | 垂直线测试 | 判断图像是否为函数 |
| inverse function | 反函数 | $f^{-1}$；$D(f^{-1})=R(f)$，图像关于 $y=x$ 对称 |
| cancellation equations | 抵消方程 | $f^{-1}(f(x))=x$，$f(f^{-1}(y))=y$ |
| odd / even function | 奇 / 偶函数 | $f(-x)=-f(x)$ / $f(-x)=f(x)$ |
| exponential function | 指数函数 | $a^x\ (a>0,a\ne1)$；定义域 $\mathbb{R}$，值域 $(0,\infty)$ |
| base | 底数 | $a$；$e\approx2.71828$ |
| logarithmic function | 对数函数 | $\log_a x$ 是 $a^x$ 的反函数；定义域 $(0,\infty)$ |
| natural logarithm | 自然对数 | $\ln x=\log_e x$ |
| common logarithm | 常用对数 | $\log_{10}x=\lg x$ |
| change of base formula | 换底公式 | $\log_a b=\dfrac{\ln b}{\ln a}$ |
| trigonometric functions | 三角函数 | $\sin,\cos,\tan,\cot,\sec,\csc$ |
| secant / cosecant | 正割 / 余割 | $\sec x=1/\cos x$，$\csc x=1/\sin x$ |
| unit circle | 单位圆 | 定义三角函数与判断符号（ASTC） |
| radian | 弧度 | 三角极限只有在弧度制下才成立 $\lim_{t\to0}\frac{\sin t}{t}=1$ |
| Pythagorean identities | 勾股恒等式 | $\sin^2x+\cos^2x=1$；$1+\tan^2x=\sec^2x$；$1+\cot^2x=\csc^2x$ |
| double-angle identities | 倍角公式 | $\sin2x=2\sin x\cos x$；$\cos2x=2\cos^2x-1=1-2\sin^2x$ |
| inverse trigonometric functions | 反三角函数 | $\arcsin,\arccos,\arctan$（主值分支） |
| principal value | 主值 | $\arcsin$ 取 $[-\pi/2,\pi/2]$，$\arccos$ 取 $[0,\pi]$，$\arctan$ 取 $(-\pi/2,\pi/2)$ |
| restricted domain | 限制定义域 | 为得到反函数而把 $\sin/\cos/\tan$ 限制在主值区间 |

---

### 0.2 极限与连续 (Chapter 2: Limits and Continuity)

| English Term | 中文 | 含义 / 公式 / 考点 |
| :--- | :--- | :--- |
| limit | 极限 | $\lim_{x\to c}f(x)=L$：$x$ 靠近 $c$（但 $x\ne c$）时 $f(x)$ 任意接近 $L$ |
| one-sided limit | 单侧极限 | 左极限 $\lim_{x\to c^-}$，右极限 $\lim_{x\to c^+}$ |
| two-sided limit | 双侧极限 | 存在 $\iff$ 左右极限存在且相等（Theorem A） |
| does not exist (DNE) | 极限不存在 | 三种情形：左右不同、趋于无穷、无限振荡（如 $\sin(1/x)$） |
| indeterminate form | 未定式 | 常见 $0/0$、$\infty/\infty$、$1^\infty$、$0\cdot\infty$、$\infty-\infty$ |
| main limit theorem | 主极限定理 | 和差积商、乘幂、开方的极限等于极限的相应运算（分母极限 $\ne0$） |
| substitution theorem | 直接代入定理 | 多项式、有理函数、根式、三角函数在定义点处 $\lim_{x\to c}f(x)=f(c)$ |
| cancellation theorem | 消去定理 | 去心邻域内 $f=g$ $\Rightarrow$ 极限相同；用于 $0/0$ 约分 |
| rationalization | 有理化 | 含根号的 $0/0$ 或 $\infty-\infty$，乘共轭式 |
| sign-preserving property | 保号性 | 若 $\lim_{x\to c}f(x)=L>0$，则在 $c$ 附近 $f(x)>0$ |
| squeeze theorem | 夹逼定理 | $g\le f\le h$ 且 $\lim g=\lim h=L\Rightarrow\lim f=L$ |
| limit at infinity | 无穷远处极限 | $\lim_{x\to\pm\infty}f(x)$；同除以分母最高次幂 |
| infinite limit | 无穷极限 | $\lim_{x\to c}f(x)=\pm\infty$；注意左右符号 |
| horizontal asymptote | 水平渐近线 | $\lim_{x\to\pm\infty}f(x)=L\Rightarrow y=L$（最多两条） |
| vertical asymptote | 垂直渐近线 | 单侧极限为 $\pm\infty$ 处 $x=c$；先约去公因式再找 |
| sequence | 数列 | $n\to\infty$ 时用同样方法；夹逼、主极限定理均适用 |
| continuity at a point | 点连续 | 三条件：$f(c)$ 有定义；$\lim_{x\to c}f(x)$ 存在；二者相等 |
| removable discontinuity | 可去间断点 | 极限存在但 $\ne f(c)$ 或 $f(c)$ 未定义（补定义即可连续） |
| jump discontinuity | 跳跃间断点 | 左右极限都存在但不相等 |
| infinite discontinuity | 无穷间断点 | 单侧或双侧极限为 $\pm\infty$ |
| oscillating discontinuity | 振荡间断点 | 如 $\sin(1/x)$ 在 $0$ 处 |
| elementary function | 初等函数 | 基本初等函数经有限次四则运算与复合而成；在其定义域上连续 |
| composite limit theorem | 复合极限定理 | $\lim g=L$ 且 $f$ 在 $L$ 连续 $\Rightarrow\lim f(g(x))=f(L)$（Theorem E） |
| continuity on an interval | 区间上连续 | 开区间每点连续；闭区间端点要求单侧连续 |
| Intermediate Value Theorem (IVT) | 介值定理 | $f$ 在 $[a,b]$ 连续，$N$ 介于 $f(a),f(b)$ 之间 $\Rightarrow\exists c\in(a,b),f(c)=N$（Theorem F） |
| zero point theorem | 零点定理 | IVT 取 $N=0$：$f(a)f(b)<0\Rightarrow$ 区间内有根 |
| bisection method | 二分法 | 反复取中点、判号，逼近根 |
| fixed point | 不动点 | $f(c)=c$；令 $g(x)=f(x)-x$ 用零点定理 |
| continuous compounding | 连续复利 | $A(t)=Pe^{rt}$；分期复利 $A=P(1+r/n)^{nt}$ |
| first important limit | 第一重要极限 | $\lim_{t\to0}\dfrac{\sin t}{t}=1$（弧度制） |
| second important limit | 第二重要极限 | $\lim_{x\to\infty}\left(1+\frac1x\right)^x=e$，$\lim_{h\to0}(1+h)^{1/h}=e$ |

---

### 0.3 导数与相关变化率 (Chapter 3: Derivatives)

| English Term | 中文 | 含义 / 公式 / 考点 |
| :--- | :--- | :--- |
| secant line | 割线 | 过 $(c,f(c))$ 与 $(c+h,f(c+h))$，斜率 $\dfrac{f(c+h)-f(c)}{h}$ |
| tangent line | 切线 | 割线斜率的极限；方程 $y-f(c)=f'(c)(x-c)$ |
| difference quotient | 差商 | $\dfrac{f(x)-f(c)}{x-c}$ 或 $\dfrac{f(c+h)-f(c)}{h}$ |
| average velocity | 平均速度 | $\dfrac{\Delta s}{\Delta t}$ |
| instantaneous velocity | 瞬时速度 | $v(t)=s'(t)=\lim_{\Delta t\to0}\dfrac{\Delta s}{\Delta t}$ |
| derivative | 导数 | $f'(c)=\lim_{h\to0}\dfrac{f(c+h)-f(c)}{h}$ |
| differentiable | 可导 | 该极限存在；可导 $\Rightarrow$ 连续，反之不成立 |
| Leibniz notation | 莱布尼茨记号 | $\dfrac{dy}{dx}$，$\left.\dfrac{dy}{dx}\right\rvert_{x=c}$ |
| differentiation operator | 微分算子 | $D_x$ |
| power rule | 幂法则 | $(x^r)'=rx^{r-1}$（$r$ 为任意实数，必要时 $x>0$） |
| constant / identity rule | 常数 / 恒等法则 | $(c)'=0$，$(x)'=1$ |
| linearity | 线性性质 | $(af\pm bg)'=af'\pm bg'$ |
| product rule | 乘积法则 | $(fg)'=f'g+fg'$（**不是** $f'g'$） |
| quotient rule | 商法则 | $\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$ |
| chain rule | 链式法则 | $\dfrac{dy}{dx}=\dfrac{dy}{du}\cdot\dfrac{du}{dx}$；$(f(g(x)))'=f'(g(x))g'(x)$ |
| higher-order derivative | 高阶导数 | $f'',f''',f^{(n)}$；$s''(t)=a(t)$ |
| acceleration | 加速度 | $a(t)=v'(t)=s''(t)$ |
| inverse function theorem (IFT) | 反函数求导定理 | $(f^{-1})'(y)=\dfrac{1}{f'(x)}$，其中 $y=f(x)$ 且 $f'(x)\ne0$ |
| implicit function | 隐函数 | $F(x,y)=0$ 形式，$y$ 未显式解出 |
| explicit function | 显函数 | $y=f(x)$ |
| implicit differentiation | 隐函数求导 | 两边对 $x$ 求导，$y$ 视为 $y(x)$，每项含 $y$ 处乘 $y'$ |
| logarithmic differentiation | 对数求导法 | 两边取 $\ln$ 化简再求导；适用于 $f(x)^{g(x)}$ 或多项乘除、根式 |
| related rates | 相关变化率 | 各变量对 $t$ 求导，链式法则联系 $\frac{dV}{dt}$、$\frac{dr}{dt}$ 等 |
| rate of change | 变化率 | 导数即瞬时变化率 |
| corner / cusp / vertical tangent | 角点 / 尖点 / 竖直切线 | 不可导的三种几何形态（如 $\lvert x\rvert$、$x^{2/3}$、$\sqrt[3]{x}$ 在 $0$ 处） |

---

## 第一部分：函数与预备知识 (Lecture 1: §1.5–1.9)

### 1.5 Functions and Their Graphs (函数及其图像)

#### 1. 函数、定义域与值域 (Definition, Domain & Range)

* **函数 (Function):** 从集合 $D$ 到 $\mathbb{R}$ 的对应法则，对每个 $x\in D$ 指定**唯一**的 $y$。

* **定义域 (Domain):** $D(f)$，自变量允许取值的集合。

* **值域 (Range):** $R(f)=\{y:y=f(x),\ x\in D(f)\}$。

* **自然定义域 (Natural Domain):** 未特别声明时，使表达式有意义的全体实数。

**求自然定义域的四条检查（必背）：**
1. 分母 $\ne0$；
2. 偶次根号内 $\ge0$（奇次根号无限制）；
3. 对数真数 $>0$，底数 $>0$ 且 $\ne1$；
4. $\arcsin u$、$\arccos u$ 要求 $-1\le u\le1$；$\tan x$ 要求 $\cos x\ne0$。

#### 2. 分段函数 (Piecewise-Defined Functions)

* **绝对值函数:** $\lvert x\rvert=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases}$

* **符号函数:** $\operatorname{sgn}x=\begin{cases}1,&x>0\\0,&x=0\\-1,&x<0\end{cases}$

* **取整函数:** $[x]=\lfloor x\rfloor$ = 不超过 $x$ 的最大整数。例：$[2.7]=2$，$[-1.2]=-2$。

* **小数部分:** $x-[x]\in[0,1)$（Assignment 2 中的 $f(x)=x-[[x]]$ 即此类）。

---

### 1.6 Operations on Functions (函数的运算)

#### 1. 四则运算与复合 (Algebraic Operations & Composition)

* 四则运算在 $D(f)\cap D(g)$ 上进行；除法还需 $g(x)\ne0$。

* **复合:** $(g\circ f)(x)=g(f(x))$，运算顺序**由内而外**。

* **复合函数定义域:** $D(g\circ f)=\{x:x\in D(f)\ \text{且}\ f(x)\in D(g)\}$。
  * 例：$f(x)=\sqrt{x}$，$g(x)=\ln x$，则 $(g\circ f)(x)=\ln\sqrt{x}$ 要求 $x>0$，而不是 $x\ge0$。

* **分解:** 由外而内。例 $F(x)=\sec^3(3\sqrt{x})$：最内 $h(x)=3\sqrt{x}$，中间 $g(x)=\sec x$，最外 $f(x)=x^3$。

#### 2. 一对一函数与反函数 (One-to-One Functions & Inverses)

* **一对一 (1-1):** $x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2)$。

* **水平线测试 (Horizontal Line Test):** 任一水平线与图像至多一个交点 $\iff$ 1-1 $\iff$ 存在反函数。

* **垂直线测试 (Vertical Line Test):** 任一垂直线与图像至多一个交点 $\iff$ 图像表示函数。

* **求反函数三步:** ① 写 $y=f(x)$ 解出 $x$；② 交换 $x,y$；③ 用原函数值域确定反函数定义域。

* **关键性质:** $D(f^{-1})=R(f)$，$R(f^{-1})=D(f)$，图像关于 $y=x$ 对称。

* **抵消方程 (Cancellation Equations):** $f^{-1}(f(x))=x$（$x\in D(f)$），$f(f^{-1}(y))=y$（$y\in R(f)$）。

* **警告:** $f^{-1}(x)\ne\dfrac{1}{f(x)}$。

* **单调函数必为 1-1:** 严格递增/递减函数一定存在反函数（Lecture 6 会用导数判断）。

#### 3. 奇偶性 (Parity)

* **偶函数:** $f(-x)=f(x)$，图像关于 $y$ 轴对称。

* **奇函数:** $f(-x)=-f(x)$，图像关于原点对称。

* **奇偶分解:** 定义在对称区间上的任意函数可写成
  $$f(x)=\underbrace{\frac{f(x)+f(-x)}{2}}_{\text{偶部}}+\underbrace{\frac{f(x)-f(-x)}{2}}_{\text{奇部}}$$
  Assignment 1 中 $2^x=\frac{2^x+2^{-x}}{2}+\frac{2^x-2^{-x}}{2}$ 即此结论。

---

### 1.7 Exponential and Logarithmic Functions (指数与对数函数)

#### 1. 指数函数 (Exponential Functions)

* $f(x)=a^x$，$a>0,a\ne1$；定义域 $\mathbb{R}$，值域 $(0,\infty)$，恒过 $(0,1)$。

* $a>1$ 时递增；$0<a<1$ 时递减。

* 运算律：$a^{x+y}=a^xa^y$，$(a^x)^y=a^{xy}$，$a^{-x}=\dfrac{1}{a^x}$，$a^0=1$。

#### 2. 对数函数 (Logarithmic Functions)

* $f(x)=\log_a x$ 是 $a^x$ 的反函数；定义域 $(0,\infty)$，值域 $\mathbb{R}$，过 $(1,0)$。

* $\log_a(xy)=\log_ax+\log_ay$，$\log_a\dfrac xy=\log_ax-\log_ay$，$\log_a x^r=r\log_ax$。

* $\log_a a=1$，$\log_a1=0$，$a^{\log_a x}=x$。

* **换底公式:** $\log_a b=\dfrac{\ln b}{\ln a}$。

* 自然对数 $\ln x=\log_e x$，满足 $\ln e=1$，$e^{\ln x}=x\ (x>0)$，$\ln(e^x)=x$。

---

### 1.8 The Trigonometric Functions (三角函数)

#### 1. 定义与基本关系 (Definitions)

* 直角三角形：$\sin\theta=\dfrac{\text{opposite}}{\text{hypotenuse}}$，$\cos\theta=\dfrac{\text{adjacent}}{\text{hypotenuse}}$，$\tan\theta=\dfrac{\text{opposite}}{\text{adjacent}}$。

* 单位圆：角 $\theta$ 终边与单位圆交点 $(\cos\theta,\sin\theta)$。

* 倒数关系：$\sec\theta=\dfrac{1}{\cos\theta}$，$\csc\theta=\dfrac{1}{\sin\theta}$，$\cot\theta=\dfrac{\cos\theta}{\sin\theta}$。

* 定义域：$\tan,\sec$ 排除 $\theta=\frac{\pi}{2}+k\pi$；$\cot,\csc$ 排除 $\theta=k\pi$。

#### 2. 核心恒等式 (Identities)

* **勾股恒等式:** $\sin^2\theta+\cos^2\theta=1$；$1+\tan^2\theta=\sec^2\theta$；$1+\cot^2\theta=\csc^2\theta$。

* **倍角公式:** $\sin2\theta=2\sin\theta\cos\theta$；$\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta$。

* 商数关系：$\tan\theta=\dfrac{\sin\theta}{\cos\theta}$。

#### 3. 特殊角函数值（必背）
| $\theta$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\sin\theta$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{\sqrt2}{2}$ | $\dfrac12$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | 不存在 |

---

### 1.9 The Inverse Trigonometric Functions (反三角函数)

#### 1. 三个反三角函数的主值区间（必背）
| 函数 | 定义域 | 值域（主值区间） | 单调性 |
| :--- | :---: | :---: | :---: |
| $y=\arcsin x$ | $[-1,1]$ | $\left[-\dfrac{\pi}{2},\dfrac{\pi}{2}\right]$ | 递增 |
| $y=\arccos x$ | $[-1,1]$ | $[0,\pi]$ | 递减 |
| $y=\arctan x$ | $(-\infty,\infty)$ | $\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$ | 递增 |

* 常用值：$\arcsin\frac12=\frac{\pi}{6}$，$\arccos\frac12=\frac{\pi}{3}$，$\arctan1=\frac{\pi}{4}$，$\arccos(-1)=\pi$，$\arctan0=0$。

* 对称性：$\arcsin(-x)=-\arcsin x$，$\arccos(-x)=\pi-\arccos x$，$\arctan(-x)=-\arctan x$。

#### 2. 抵消公式及其陷阱 (Cancellation Formulas & Pitfalls)

* **外层是三角函数、内层是反三角（恒成立）:**
  $$\sin(\arcsin x)=x\ (x\in[-1,1]),\quad \cos(\arccos x)=x,\quad \tan(\arctan x)=x$$

* **外层是反三角、内层是三角（只在主值区间成立）:**
  $$\arcsin(\sin\theta)=\theta\ \text{仅当}\ \theta\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$$
  $$\arccos(\cos\theta)=\theta\ \text{仅当}\ \theta\in[0,\pi],\qquad \arctan(\tan\theta)=\theta\ \text{仅当}\ \theta\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$$
  超出主值区间时，先用周期性/对称性化到主值区间。例：$\arcsin\left(\sin\frac{9\pi}{7}\right)$ 不能直接等于 $\frac{9\pi}{7}$。

* **用直角三角形求复合值:** 令 $\theta=\arctan x$，则 $\tan\theta=x$，斜边 $\sqrt{1+x^2}$，故
  $$\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}},\quad \cos(\arctan x)=\frac{1}{\sqrt{1+x^2}}$$
  同理 $\sin(\arccos x)=\sqrt{1-x^2}$，$\tan(\arcsin x)=\dfrac{x}{\sqrt{1-x^2}}$。

---

### 🌟 典型例题精解 (Typical Examples from Assignments 1)

##### 【例题 1】差商的计算（Assignment 1, §1.5）

**Problem:** For $F(x)=x^3+3x$, evaluate $\dfrac{F(2+h)-F(2)}{h}$.

**Process (解题步骤):**

$$F(2+h)=(2+h)^3+3(2+h)=h^3+6h^2+15h+14$$
$$F(2)=8+6=14$$
$$\frac{F(2+h)-F(2)}{h}=\frac{h^3+6h^2+15h}{h}=h^2+6h+15$$

**中文详解:** 展开 $(2+h)^3$ 时用二项式定理；减去 $F(2)$ 后分子每项都含 $h$，约分即可。此类差商是第 3 章导数定义的前身。

##### 【例题 2】求自然定义域（Assignment 1, §1.5）

**Problem:** Find the natural domain of $g(x)=\dfrac{\sec x}{x^2}$.

**Process (解题步骤):**

分母 $x^2\ne0\Rightarrow x\ne0$；$\sec x=\dfrac{1}{\cos x}$ 要求 $\cos x\ne0\Rightarrow x\ne\dfrac{\pi}{2}+k\pi$。
$$\text{Domain}=\left\{x\in\mathbb{R}:x\ne0,\ x\ne\frac{\pi}{2}+k\pi,\ k\in\mathbb{Z}\right\}$$

**中文详解:** 两个限制取交集：分母不为零、正割有意义。注意 $\sec$ 的限制来自 $\cos x=0$。

##### 【例题 3】求反函数及其定义域（Assignment 1, §1.6）

**Problem:** Find the inverse of $f(x)=\dfrac{1-\sqrt{x}}{1+\sqrt{x}}$ and the domain of $f^{-1}$.

**Process (解题步骤):**

1. 求值域：$f(x)=-1+\dfrac{2}{1+\sqrt{x}}$，由 $1+\sqrt{x}\ge1$ 得 $0<\dfrac{2}{1+\sqrt{x}}\le2$，故 $-1<f(x)\le1$，即 $D(f^{-1})=(-1,1]$。
2. 解出 $x$：$y(1+\sqrt{x})=1-\sqrt{x}\Rightarrow\sqrt{x}=\dfrac{1-y}{1+y}\Rightarrow x=\left(\dfrac{1-y}{1+y}\right)^2$。
3. 交换 $x,y$：$f^{-1}(x)=\left(\dfrac{1-x}{1+x}\right)^2$，$x\in(-1,1]$。

**中文详解:** 反函数的定义域 = 原函数的值域，必须先求值域；开方时注意 $\frac{1-y}{1+y}\ge0$ 的范围。

##### 【例题 4】反三角复合求值（Assignment 1, §1.9）

**Problem:** Evaluate $\sin(2\arctan2)$ without a calculator.

**Process (解题步骤):**

令 $\theta=\arctan2$，则 $\tan\theta=2$，$\theta\in\left(0,\frac{\pi}{2}\right)$。
由 $1+\tan^2\theta=\sec^2\theta=5$ 得 $\cos\theta=\dfrac{1}{\sqrt5}$，$\sin\theta=\dfrac{2}{\sqrt5}$。
$$\sin2\theta=2\sin\theta\cos\theta=2\cdot\frac{2}{\sqrt5}\cdot\frac{1}{\sqrt5}=\frac45$$

**中文详解:** 设辅助角 $\theta$，把反三角转化为直角三角形边长比；再用倍角公式。

---

## 第二部分：极限与连续 (Lectures 2–4: §2.1、2.3–2.7)

### 2.1 Introduction to Limits (极限引论与直观概念)

#### 1. 极限的直观定义 (Intuitive Definition)
$$\lim_{x\to c}f(x)=L$$
表示：当 $x$ 充分接近 $c$（但 $x\ne c$）时，$f(x)$ 可以任意接近 $L$。

* 极限只关心 $x\to c$ 时 $f$ 的趋势，**与 $f(c)$ 是否有定义、等于多少无关**。

* 三大引例：瞬时速度、圆面积（多边形逼近）、弧长（折线逼近）。

#### 2. 极限不存在的三种情形 (DNE)
1. **左右极限不同:** 如 $f(x)=\operatorname{sgn}x$ 在 $0$ 处（左 $-1$，右 $1$）。
2. **函数值无限增大:** $\lim_{x\to0}\dfrac{1}{x^2}=+\infty$（不是有限数）。
3. **无限振荡:** $\lim_{x\to0}\sin\dfrac1x$ 不存在。

#### 3. 单侧极限与双侧极限 (One-Sided Limits)

* $\lim_{x\to c^-}f(x)$：从左侧逼近；$\lim_{x\to c^+}f(x)$：从右侧逼近。

* **Theorem A（双侧极限存在准则）:**
  $$\lim_{x\to c}f(x)=L\iff\lim_{x\to c^-}f(x)=\lim_{x\to c^+}f(x)=L$$
  这是处理分段函数、绝对值、取整函数在分界点处极限的标准工具。

#### 4. 计算器的陷阱 (Calculator Pitfall)

* 用计算器代小数列表可能因**舍入误差 (rounding error)** 给出错误结论（如 $x\to0$ 时 $x^2-10^{-4}\cos x$ 被误判为 $0$）；必须用代数定理严格计算。

---

### 2.3 Limit Theorems (极限定理与计算法则)

#### 1. 主极限定理 (Main Limit Theorem / Theorem 2.3A)
若 $\lim_{x\to c}f(x)=L$，$\lim_{x\to c}g(x)=M$，则：
$$\lim(f\pm g)=L\pm M,\quad \lim(fg)=LM,\quad \lim\frac fg=\frac LM\ (M\ne0)$$
$$\lim f(x)^r=L^r,\quad \lim\sqrt[n]{f(x)}=\sqrt[n]{L}\quad(\text{在定义范围内})$$

#### 2. 直接代入定理 (Substitution Theorem / Theorem 2.3B)
若 $f$ 是多项式、有理函数、根式函数或三角函数，且 $c\in D(f)$，则
$$\lim_{x\to c}f(x)=f(c)$$

* 有理函数在分母为 $0$ 处不能直接代入；三角函数的代入点必须在其定义域内。

#### 3. $0/0$ 型与消去定理 (Cancellation Theorem / Theorem 2.3C)

* 若在 $c$ 的某去心邻域内 $f(x)=g(x)$ 且 $\lim g$ 存在，则 $\lim f=\lim g$。

* **$0/0$ 的标准处理:** 因式分解并约去公因式；含根号时**有理化**（乘共轭）；复杂分式先通分；含 $[x]$ 时用夹逼并结合取整性质。

#### 4. 保号性 (Sign-Preserving Property)
若 $\lim_{x\to c}f(x)=L>0$，则存在 $c$ 的去心邻域，在其中 $f(x)>0$。反之 $L<0$ 同理；用于证明不等式与判断无穷极限的符号。

#### 5. 夹逼定理 (Squeeze Theorem / Theorem 2.3D)
若在 $c$ 的去心邻域内 $g(x)\le f(x)\le h(x)$，且
$$\lim_{x\to c}g(x)=\lim_{x\to c}h(x)=L,$$
则 $\lim_{x\to c}f(x)=L$。常用于 $x\cos\frac1x$、$\frac{\sin x}{x}$（$x\to\infty$）、含取整函数等。

---

### 2.4 Limits at Infinity; Infinite Limits (无穷远处的极限与无穷极限)

#### 1. 无穷远处求极限的标准方法

* 有理函数：分子分母**同除以分母的最高次幂**。

* 含根号：注意 $\sqrt{x^2}=\lvert x\rvert$；当 $x\to-\infty$ 时 $\sqrt{x^2}=-x$。

* **有理函数末端行为（速判）:**
  | 次数关系 | 极限 | 渐近线 |
  | :--- | :---: | :--- |
  | $\deg P<\deg Q$ | $0$ | $y=0$ |
  | $\deg P=\deg Q$ | 首项系数之比 | $y=\frac{a_n}{b_n}$ |
  | $\deg P=\deg Q+1$ | $\pm\infty$ | 斜渐近线（多项式除法） |
  | $\deg P>\deg Q+1$ | $\pm\infty$ | 无水平/斜渐近线 |

* 数列极限（$n\to\infty$）同法，且主极限定理、夹逼定理对数列同样成立。

#### 2. 无穷极限 (Infinite Limits)

* 记号 $\lim_{x\to c}f(x)=+\infty$ 表示函数值无限增大，**极限本身不存在**（但信息更强）。

* 判断 $\dfrac{1}{0}$ 型：看分母从哪侧趋于 $0$、分子符号。
  * $\lim_{x\to0^+}\dfrac1x=+\infty$，$\lim_{x\to0^-}\dfrac1x=-\infty$。

* 若 $\lim f=L\ne0$，$\lim g=0$ 且 $g$ 在附近保持同号，则 $\lim\dfrac fg=\pm\infty$（符号由 $L$ 与 $g$ 的符号决定）。

#### 3. 渐近线 (Asymptotes)

* **水平渐近线 (HA):** $\lim_{x\to+\infty}f(x)=L$ 或 $\lim_{x\to-\infty}f(x)=L$ $\Rightarrow y=L$。最多两条。

* **垂直渐近线 (VA):** $\lim_{x\to c^\pm}f(x)=\pm\infty$ $\Rightarrow x=c$。
  * 有理函数：先约去分子分母公因式，剩下使分母为 $0$ 的点才是 VA（约掉的点是可去间断点）。

* **陷阱:** $y=\dfrac{\sin x}{x}$ 在 $x=0$ 处极限为 $1\ne\pm\infty$，故 $x=0$ **不是** VA；只有 $y=0$ 一条 HA。

---

### 2.5 Limits Involving Trigonometric Functions (三角函数极限)

#### 1. 三角函数的直接代入
在其定义域内，$\lim_{x\to c}\sin x=\sin c$，$\lim\cos x=\cos c$，$\lim\tan x=\tan c$（$\cos c\ne0$）。

#### 2. 第一重要极限 (Theorem B1)
$$\lim_{t\to0}\frac{\sin t}{t}=1\quad(\text{弧度制})$$
**推广：**
$$\lim_{t\to0}\frac{\sin(at)}{bt}=\frac ab,\qquad \lim_{t\to0}\frac{\tan t}{t}=1,\qquad \lim_{t\to0}\frac{1-\cos t}{t}=0,\qquad \lim_{t\to0}\frac{1-\cos t}{t^2}=\frac12$$

* $1-\cos t$ 的处理：乘共轭 $1+\cos t$，化为 $\dfrac{\sin^2t}{t(1+\cos t)}$。

* 几何证明用面积夹逼：$\cos t\le\dfrac{\sin t}{t}\le\dfrac{1}{\cos t}$（$0<t<\pi/2$），两端 →1。

#### 3. 无穷小 × 有界（夹逼推论）
若 $\lim_{x\to c}f(x)=0$ 且 $g$ 在附近有界，则 $\lim f(x)g(x)=0$。

* 例：$\lim_{x\to0}x\cos\frac1x=0$；$\lim_{x\to\infty}\dfrac{\sin x}{x}=0$；$\lim_{x\to\infty}\dfrac{\cos x}{x}=0$。

#### 4. 易错点

* $\lim_{t\to0}\frac{\sin t}{t}=1$ 只在 $t\to0$ 且**弧度制**下成立；$x\to\infty$ 时 $\frac{\sin x}{x}\to0$，二者不可混用。

* 极限存在 $\ne$ 函数值存在；$\frac{\sin x}{x}$ 在 $0$ 处无定义但极限为 $1$（可去间断点）。

---

### 2.6 Limits of Exponential, Logarithmic & Inverse Functions (指数、对数与反函数极限)

#### 1. 指数函数的极限
$$\lim_{x\to\infty}e^x=+\infty,\qquad \lim_{x\to-\infty}e^x=0$$
对 $a>1$：$\lim_{x\to\infty}a^x=+\infty$，$\lim_{x\to-\infty}a^x=0$；对 $0<a<1$ 方向相反。

#### 2. 反函数极限定理 (Theorem C)
若 $\lim_{x\to a}f(x)=f(a)=c$（即 $f$ 在 $a$ 连续），则 $\lim_{x\to c}f^{-1}(x)=f^{-1}(c)=a$。

* 直观：反函数图像关于 $y=x$ 对称，定义域与值域互换。

#### 3. 对数函数的极限 (Theorem D)

* $a>0$：$\lim_{x\to a}\log_c x=\log_c a$。

* $c>1$ 时：$\lim_{x\to\infty}\log_c x=+\infty$，$\lim_{x\to0^+}\log_c x=-\infty$。

* 复合形式：$\lim\ln u(x)=\ln(\lim u(x))$，前提是 $\lim u(x)>0$（对数在正数处连续）。

#### 4. 连续复利 (Continuous Compounding)
$$A(t)=Pe^{rt}\quad(\text{连续复利}),\qquad A=P\left(1+\frac rn\right)^{nt}\quad(\text{每年 }n\text{ 次复利})$$

* 例：$P=400$，$r=4\%$，$t=2$：
  * 每年复利：$400(1.04)^2=432.64$；
  * 每月复利：$400\left(1+\frac{0.04}{12}\right)^{24}\approx433.26$；
  * 连续复利：$400e^{0.08}\approx433.31$。

---

### 2.7 Continuity of Functions (函数的连续性)

#### 1. 点连续的三条件（必背）
$f$ 在 $x=c$ 连续 $\iff$
1. $f(c)$ 有定义；
2. $\lim_{x\to c}f(x)$ 存在；
3. $\lim_{x\to c}f(x)=f(c)$。

**区间连续:** 开区间内每点连续；闭区间 $[a,b]$ 还要求 $\lim_{x\to a^+}f(x)=f(a)$、$\lim_{x\to b^-}f(x)=f(b)$。

#### 2. 间断点分类 (Classification of Discontinuities)
| 类型 | 特征 | 例 |
| :--- | :--- | :--- |
| 可去间断点 (removable) | 极限存在，但 $f(c)$ 未定义或 $\ne$ 极限 | $\frac{\sin x}{x}$ 在 $0$ 处；$\frac{x^2-4}{x-2}$ 在 $2$ 处 |
| 跳跃间断点 (jump) | 左右极限都存在但不相等 | $\operatorname{sgn}x$ 在 $0$ 处 |
| 无穷间断点 (infinite) | 单侧/双侧极限为 $\pm\infty$ | $\frac1x$ 在 $0$ 处 |
| 振荡间断点 (oscillating) | 极限因振荡不存在 | $\sin\frac1x$ 在 $0$ 处 |

* **补定义使连续:** 若 $\lim_{x\to c}f(x)=L$ 存在，令 $f(c)=L$ 即可（可去间断点）。

* **非可去（nonremovable）:** 跳跃、无穷、振荡三类。

#### 3. 初等函数与复合函数的连续性

* 多项式、有理函数、根式、指数、对数、三角、反三角函数在其**定义域**上连续。

* **复合极限定理 (Theorem E):** 若 $\lim_{x\to c}g(x)=L$ 且 $f$ 在 $L$ 处连续，则
  $$\lim_{x\to c}f(g(x))=f\left(\lim_{x\to c}g(x)\right)=f(L)$$
  例：$\lim_{x\to0}\sin\left(\dfrac{\sin x}{x}\right)=\sin1$；$\lim_{x\to0}\ln\dfrac{\sin x}{x}=\ln1=0$。

* **幂指函数 $f(x)^{g(x)}$:** 若 $f,g$ 连续且 $f(x)>0$，则 $f^g=e^{g\ln f}$ 连续。

#### 4. 第二重要极限与 $1^\infty$ 型
$$\lim_{x\to\infty}\left(1+\frac1x\right)^x=e,\qquad \lim_{h\to0}(1+h)^{1/h}=e$$
**推广:** 若 $\lim u=0$（$u\ne0$），则 $\lim(1+u)^{1/u}=e$。

**$1^\infty$ 型速算公式（必背）:** 若 $f(x)\to1$，$g(x)\to\infty$，则
$$\lim f(x)^{g(x)}=e^{\lim g(x)[f(x)-1]}$$
**常用结论:** $\lim_{x\to0}(1+ax)^{b/x}=e^{ab}$。

#### 5. 闭区间连续函数的性质：介值定理与零点定理

* **介值定理 (IVT / Theorem F):** $f$ 在 $[a,b]$ 连续，$N$ 是介于 $f(a)$ 与 $f(b)$ 之间的任意数，则存在 $c\in(a,b)$ 使 $f(c)=N$。

* **零点定理 (Zero Point Theorem):** 若 $f(a)$ 与 $f(b)$ **异号**，则存在 $c\in(a,b)$ 使 $f(c)=0$。

* **二分法 (Bisection):** 反复取中点并判断符号，把根所在区间减半，可逼近根。

* **不动点 (Fixed Point):** 证明 $f(c)=c$，构造 $g(x)=f(x)-x$，对 $g$ 用零点定理。

---

### 🌟 典型例题精解 (Typical Examples from Assignments 2–4)

##### 【例题 5】$0/0$ 型含根号极限（Assignment 2, §2.3）

**Problem:** Evaluate $\displaystyle\lim_{x\to0}\frac{\sqrt{3+x}-\sqrt{3-x}}{x}$.

**Process (解题步骤):**

有理化分子，乘共轭式 $\sqrt{3+x}+\sqrt{3-x}$：
$$\frac{\sqrt{3+x}-\sqrt{3-x}}{x}\cdot\frac{\sqrt{3+x}+\sqrt{3-x}}{\sqrt{3+x}+\sqrt{3-x}}=\frac{(3+x)-(3-x)}{x\left(\sqrt{3+x}+\sqrt{3-x}\right)}=\frac{2x}{x\left(\sqrt{3+x}+\sqrt{3-x}\right)}$$
约去 $x$ 后令 $x\to0$：
$$\frac{2}{\sqrt3+\sqrt3}=\frac{1}{\sqrt3}$$

**中文详解:** $0/0$ 型含根号差，先乘共轭有理化，约去公因子 $x$ 后再代入；这是 §2.3 与 §2.4 中反复使用的标准手法。

##### 【例题 6】根式差的无穷极限（Assignment 3, §2.4）

**Problem:** Evaluate $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+x}-\sqrt{x^2-x}\right)$.

**Process (解题步骤):**

$$\sqrt{x^2+x}-\sqrt{x^2-x}=\frac{(x^2+x)-(x^2-x)}{\sqrt{x^2+x}+\sqrt{x^2-x}}=\frac{2x}{\sqrt{x^2+x}+\sqrt{x^2-x}}$$
分子分母同除以 $x>0$：
$$=\frac{2}{\sqrt{1+\frac1x}+\sqrt{1-\frac1x}}\to\frac{2}{1+1}=1$$

**中文详解:** $\infty-\infty$ 型先有理化；除以 $x$ 时注意 $x>0$，$\sqrt{x^2}=x$。

##### 【例题 7】有理函数的渐近线（Assignment 3, §2.4）

**Problem:** Find all horizontal and vertical asymptotes of $f(x)=\dfrac{x}{1-x^2}$.

**Process (解题步骤):**

* HA：$\lim_{x\to\pm\infty}\dfrac{x}{1-x^2}=0$，故 $y=0$。

* VA：分母 $1-x^2=(1-x)(1+x)=0\Rightarrow x=\pm1$，分子在 $x=\pm1$ 处不为 $0$，且单侧极限为 $\pm\infty$，故 $x=1$ 与 $x=-1$ 都是 VA。

**中文详解:** 先看末端行为定 HA；再找分母零点（且不能约去）定 VA。

##### 【例题 8】三角极限（Assignment 3, §2.5）

**Problem:** Evaluate $\displaystyle\lim_{x\to0}\frac{\tan4x}{\sin5x}$.

**Process (解题步骤):**

$$\frac{\tan4x}{\sin5x}=\frac{\tan4x}{4x}\cdot\frac{5x}{\sin5x}\cdot\frac{4x}{5x}\to1\cdot1\cdot\frac45=\frac45$$

**中文详解:** 凑第一重要极限的结构 $\frac{\tan u}{u}\to1$、$\frac{\sin v}{v}\to1$，系数按比例留下。

##### 【例题 9】$1^\infty$ 型极限（Assignment 4, §2.6）

**Problem:** Evaluate $\displaystyle\lim_{x\to\infty}\left(\frac{2x+3}{2x+1}\right)^{3x+1}$.

**Process (解题步骤):**

底数 $=\dfrac{2x+3}{2x+1}=1+\dfrac{2}{2x+1}=1+u$，其中 $u=\dfrac{2}{2x+1}\to0$。
用速算公式：
$$\lim g(x)[f(x)-1]=\lim(3x+1)\cdot\frac{2}{2x+1}=3$$
故原式 $=e^3$。

**中文详解:** $1^\infty$ 型先写成 $1+u$，再用 $e^{\lim g u}$；不要直接对底数取极限。

##### 【例题 10】求参数使函数处处连续（Assignment 4, §2.7）

**Problem:** Find $a,b$ such that
$$f(x)=\begin{cases}\dfrac{x^2-1}{x-1},&x<1\\ ax^2-bx+4,&1\le x<3\\ 2x-a+2b,&x\ge3\end{cases}$$
is continuous everywhere.

**Process (解题步骤):**

* $x=1$：$\lim_{x\to1^-}\dfrac{x^2-1}{x-1}=\lim(x+1)=2$；$f(1)=a-b+4$。故 $a-b+4=2\Rightarrow a-b=-2$。

* $x=3$：$\lim_{x\to3^-}=9a-3b+4$；$\lim_{x\to3^+}=6-a+2b$。故 $9a-3b+4=6-a+2b\Rightarrow10a-5b=2\Rightarrow2a-b=\dfrac25$。

* 联立解得 $a=\dfrac{12}{5}$，$b=\dfrac{22}{5}$。

**中文详解:** 分段点连续 $\iff$ 左极限 $=$ 右极限 $=$ 函数值；两个分界点各给一个方程。

##### 【例题 11】介值定理证明根的存在（Assignment 4, §2.7）

**Problem:** Show that $x^4+3x-2=0$ has a real solution between $0$ and $1$.

**Process (解题步骤):**

令 $f(x)=x^4+3x-2$，在 $[0,1]$ 上连续。
$$f(0)=-2<0,\qquad f(1)=1+3-2=2>0$$
由零点定理，存在 $c\in(0,1)$ 使 $f(c)=0$。

**中文详解:** 证明根存在只需：构造连续函数、算两端点、验证异号；不需要解出根。

---

## 第三部分：导数 (Lectures 5–6: §3.1–3.10)

### 3.1 Two Problems with One Theme (切线问题与瞬时速度)

#### 1. 切线斜率 (Tangent Line Problem)

* 割线斜率（过 $c$ 与 $c+h$）：$m_{\text{sec}}=\dfrac{f(c+h)-f(c)}{h}$。

* 切线斜率：$m_{\tan}=\displaystyle\lim_{h\to0}\frac{f(c+h)-f(c)}{h}$（也可写 $\lim_{x\to c}\frac{f(x)-f(c)}{x-c}$）。

* 切线方程：$y-f(c)=m_{\tan}(x-c)$。

#### 2. 瞬时速度 (Instantaneous Velocity)

* 平均速度：$\dfrac{\Delta s}{\Delta t}=\dfrac{s(t+\Delta t)-s(t)}{\Delta t}$。

* 瞬时速度：$v(t)=\displaystyle\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}$。

* 两者本质相同：都是“函数改变量 / 自变量改变量”的极限。

---

### 3.2 The Derivative (导数的定义与性质)

#### 1. 定义 (Definition)
$$f'(c)=\lim_{h\to0}\frac{f(c+h)-f(c)}{h}=\lim_{x\to c}\frac{f(x)-f(c)}{x-c}$$

* 导数存在称 $f$ 在 $c$ **可导 (differentiable)**。

* **记号:** $f'(x)$，$y'$，$\dfrac{dy}{dx}$，$\dfrac{d}{dx}f(x)$，$D_xf(x)$；$f'(c)=\left.\dfrac{dy}{dx}\right|_{x=c}$。

#### 2. 可导与连续 (Differentiability Implies Continuity)

* **定理:** 若 $f$ 在 $c$ 可导，则 $f$ 在 $c$ 连续。

* **证明要点:**
  $$f(x)-f(c)=\frac{f(x)-f(c)}{x-c}(x-c)\to f'(c)\cdot0=0\quad(x\to c)$$

* **逆命题不成立:** $f(x)=\lvert x\rvert$ 在 $0$ 处连续但不可导（左导 $-1$，右导 $1$）。

* **不可导的四种情形:**
  1. **角点 (corner):** 左右导数存在但不相等，如 $\lvert x\rvert$ 在 $0$；
  2. **尖点 (cusp):** 导数趋于 $\pm\infty$ 且两侧符号相反，如 $x^{2/3}$ 在 $0$；
  3. **竖直切线:** 如 $\sqrt[3]{x}$ 在 $0$（导数 $\to+\infty$）；
  4. **间断点:** 不连续必不可导。

---

### 3.3 Rules for Finding Derivatives (求导法则)

#### 1. 基本法则
$$(c)'=0,\qquad (x)'=1,\qquad (x^r)'=rx^{r-1}\quad(r\in\mathbb{R})$$

* 幂法则对负指数、分数指数同样成立（在定义域内）。

#### 2. 线性性质 (Linearity)
$$(af(x)\pm bg(x))'=af'(x)\pm bg'(x)$$

#### 3. 乘积与商法则 (Product & Quotient Rules)
$$(fg)'=f'g+fg'\qquad\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}$$

* 常见错误：$(fg)'\ne f'g'$；商的分子顺序不能颠倒。

---

### 3.4 Derivatives of Trigonometric Functions (三角函数导数)

| 函数 | 导数 | 函数 | 导数 |
| :---: | :---: | :---: | :---: |
| $\sin x$ | $\cos x$ | $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2x$ | $\cot x$ | $-\csc^2x$ |
| $\sec x$ | $\sec x\tan x$ | $\csc x$ | $-\csc x\cot x$ |

* **$\sin x$ 导数的证明:** 用和角公式
  $$\frac{\sin(x+h)-\sin x}{h}=\sin x\cdot\frac{\cos h-1}{h}+\cos x\cdot\frac{\sin h}{h}\to\cos x$$
  其中用到 $\frac{\sin h}{h}\to1$、$\frac{1-\cos h}{h}\to0$。

* 链式法则版本：$(\sin u)'=\cos u\cdot u'$，$(\cos u)'=-\sin u\cdot u'$，等等。

---

### 3.5 The Chain Rule (链式法则)

* **定理:** 若 $g$ 在 $x$ 可导、$f$ 在 $u=g(x)$ 可导，则
  $$\frac{d}{dx}f(g(x))=f'(g(x))\,g'(x)$$

* **多层:** $\dfrac{d}{dx}f(g(h(x)))=f'(g(h(x)))\cdot g'(h(x))\cdot h'(x)$。

* **口诀:** 外层导数（内层保持不变）$\times$ 内层导数，逐层乘到最内层。

* 例：$\left((4+2x^2)^7\right)'=7(4+2x^2)^6\cdot4x$；$(\tan^3x)'=3\tan^2x\cdot\sec^2x$；$\left(\sin\sqrt{x}\right)'=\cos\sqrt{x}\cdot\dfrac{1}{2\sqrt{x}}$。

---

### 3.6 Higher-Order Derivatives (高阶导数)

* 记号：$f''(x)=\dfrac{d^2y}{dx^2}$，$f'''(x)$，$f^{(n)}(x)$。

* **物理意义:** $s(t)$ 位置，$v(t)=s'(t)$ 速度，$a(t)=v'(t)=s''(t)$ 加速度。

* **常用结论:** $n$ 次多项式的 $n+1$ 阶导数为 $0$；$(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}{2}\right)$，$(\cos x)^{(n)}=\cos\left(x+\frac{n\pi}{2}\right)$，$(e^x)^{(n)}=e^x$。

---

### 3.7 Implicit Differentiation & Logarithmic Differentiation (隐函数求导与对数求导)

#### 1. 隐函数求导五步
1. 方程两边对 $x$ 求导；
2. 把 $y$ 看作 $y(x)$，每遇到含 $y$ 的项就用链式法则乘 $y'$（如 $(y^2)'=2yy'$，$(\sqrt y)'=\frac{y'}{2\sqrt y}$）；
3. 把含 $y'$ 的项移到一边；
4. 提取 $y'$ 并解出；
5. 若求某点切线，先代点求 $y'$，再用点斜式。

#### 2. 对数求导法 (Logarithmic Differentiation)
**适用:** 幂指函数 $f(x)^{g(x)}$；多个因子乘除、开方的复杂表达式。

**步骤:**
1. 两边取自然对数，用对数性质把乘除化为加减、指数化为系数；
2. 两边对 $x$ 隐式求导；
3. 解出 $y'$，最后把 $y$ 乘回（$y'=y\cdot(\ln y)'$）。

* 例：$y=x^x\ (x>0)$：$\ln y=x\ln x\Rightarrow\dfrac{y'}{y}=\ln x+1\Rightarrow y'=x^x(\ln x+1)$。

* 例：$y=(x^2+1)^{\sin x}$：$\ln y=\sin x\ln(x^2+1)$，$\dfrac{y'}{y}=\cos x\ln(x^2+1)+\dfrac{2x\sin x}{x^2+1}$。

---

### 3.8 Related Rates (相关变化率)

#### 1. 五步法
1. **画图**并标出变量（长度、体积、角度等）；
2. **定义变量**，写清已知变化率与所求变化率（对时间 $t$ 的导数）；
3. **建立关系方程**（勾股定理、相似三角形、体积/面积公式、三角函数）；
4. **两边对 $t$ 求导**（链式法则）；
5. **代入瞬时数值**求解；注意单位与符号（增加/减少）。

#### 2. 三个经典模型

* **勾股模型:** 气球高度 $h$、水平距离固定 $150$，斜边 $s$：$s^2=h^2+150^2\Rightarrow s\dfrac{ds}{dt}=h\dfrac{dh}{dt}$。

* **相似三角形（圆锥注水）:** $\dfrac{r}{h}=\dfrac{R}{H}$，$V=\dfrac13\pi r^2h=\dfrac{\pi R^2}{3H^2}h^3$，故 $\dfrac{dV}{dt}=\dfrac{\pi R^2}{H^2}h^2\dfrac{dh}{dt}$。

* **三角模型:** 仰角 $\theta$，$\tan\theta=\dfrac{h}{x}$，两边对 $t$ 求导得 $\sec^2\theta\dfrac{d\theta}{dt}=\dfrac{x\frac{dh}{dt}-h\frac{dx}{dt}}{x^2}$。

---

### 3.9 Derivatives of Exponential and Logarithmic Functions (指数与对数函数导数)

#### 1. 单调性与反函数存在性

* 若 $f$ 在区间 $I$ 上连续、内部可导且 $f'(x)>0$（或 $<0$），则 $f$ 在 $I$ 上严格单调，从而存在反函数 $f^{-1}$。

#### 2. 反函数求导定理 (Inverse Function Theorem)
若 $f$ 在 $x$ 处可导且 $f'(x)\ne0$，$y=f(x)$，则
$$(f^{-1})'(y)=\frac{1}{f'(x)}=\frac{1}{f'(f^{-1}(y))}$$

* 几何直观：$f^{-1}$ 的图像是 $f$ 关于 $y=x$ 的镜像，斜率互为倒数。

#### 3. 求导公式（必背）
$$(\ln x)'=\frac1x,\qquad (e^x)'=e^x,\qquad (\log_a x)'=\frac{1}{x\ln a},\qquad (a^x)'=a^x\ln a$$
**链式版本:**
$$(\ln u)'=\frac{u'}{u},\qquad (e^u)'=e^u u',\qquad (a^u)'=a^u\ln a\cdot u'$$

---

### 3.10 Derivatives of Inverse Trigonometric Functions (反三角函数导数)

$$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}\ (-1<x<1),\qquad (\arccos x)'=-\frac{1}{\sqrt{1-x^2}}$$
$$(\arctan x)'=\frac{1}{1+x^2}\ (x\in\mathbb{R})$$
**链式版本:** $(\arcsin u)'=\dfrac{u'}{\sqrt{1-u^2}}$，$(\arccos u)'=-\dfrac{u'}{\sqrt{1-u^2}}$，$(\arctan u)'=\dfrac{u'}{1+u^2}$。

* **$\arcsin$ 导数证明:** 令 $y=\arcsin x$，则 $x=\sin y$，$y\in(-\pi/2,\pi/2)$。由 IFT，
  $$\frac{dy}{dx}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-\sin^2y}}=\frac{1}{\sqrt{1-x^2}}$$
  其中 $\cos y>0$ 保证了取正根。

---

### 🌟 典型例题精解 (Typical Examples from Assignments 5–6)

##### 【例题 12】用定义求导数（Assignment 5, §3.2）

**Problem:** Use the definition to find $f'(x)$ for $f(x)=x^3+3x$.

**Process (解题步骤):**

$$\frac{f(x+h)-f(x)}{h}=\frac{(x+h)^3+3(x+h)-x^3-3x}{h}=\frac{3x^2h+3xh^2+h^3+3h}{h}=3x^2+3xh+h^2+3$$
令 $h\to0$：$f'(x)=3x^2+3$。

**中文详解:** 展开后约去 $h$，再令 $h\to0$；这是“导数定义题”的标准流程。

##### 【例题 13】高阶导数（Assignment 5, §3.6）

**Problem:** Find $D^{11}(80x^{10}-6x^9+3)$.

**Process (解题步骤):**

多项式次数为 $10$，故 $11$ 阶导数为 $0$：
$$D^{11}(80x^{10}-6x^9+3)=0$$

**中文详解:** $n$ 次多项式的 $n+1$ 阶导数恒为 $0$，无需逐阶计算。

##### 【例题 14】反函数求导定理（Assignment 6, §3.9）

**Problem:** Let $f(x)=3x^5+x-2$ with $f(1)=2$. Find $(f^{-1})'(2)$.

**Process (解题步骤):**

$f(1)=2\Rightarrow f^{-1}(2)=1$；$f'(x)=15x^4+1$，故 $f'(1)=16$。
$$(f^{-1})'(2)=\frac{1}{f'(f^{-1}(2))}=\frac{1}{f'(1)}=\frac{1}{16}$$

**中文详解:** 先由 $f(1)=2$ 找到对应点，再对原函数求导取倒数；不要试图解出 $f^{-1}$。

##### 【例题 15】隐函数求切线（Assignment 6, §3.7）

**Problem:** Find the tangent line to $\sqrt y+xy^2=5$ at $(4,1)$.

**Process (解题步骤):**

两边对 $x$ 求导：
$$\frac{y'}{2\sqrt y}+y^2+2xyy'=0$$
代入 $(x,y)=(4,1)$：
$$\frac{y'}{2}+1+8y'=0\Rightarrow\frac{17}{2}y'=-1\Rightarrow y'=-\frac{2}{17}$$
切线：$y-1=-\dfrac{2}{17}(x-4)$，即 $2x+17y=25$。

**中文详解:** 隐函数求导后先代点求斜率，再写点斜式；含 $y^2$ 的项要用乘积法则。

##### 【例题 16】对数求导法（Assignment 6, §3.7）

**Problem:** Find $y'$ for $y=(x^4+1)^{\sin x}$.

**Process (解题步骤):**

两边取对数：
$$\ln y=\sin x\ln(x^4+1)$$
两边对 $x$ 求导：
$$\frac{y'}{y}=\cos x\ln(x^4+1)+\sin x\cdot\frac{4x^3}{x^4+1}$$
故
$$y'=(x^4+1)^{\sin x}\left[\cos x\ln(x^4+1)+\frac{4x^3\sin x}{x^4+1}\right]$$

**中文详解:** 底数与指数都含 $x$，必须用对数求导；最后别忘了乘回 $y$。

##### 【例题 17】相关变化率（Assignment 6, §3.8）

**Problem:** Each edge of a cube increases at $3$ in/s. How fast is the volume increasing when the edge is $12$ in?

**Process (解题步骤):**

$V=s^3$，两边对 $t$ 求导：
$$\frac{dV}{dt}=3s^2\frac{ds}{dt}$$
代入 $s=12$，$\dfrac{ds}{dt}=3$：
$$\frac{dV}{dt}=3(12)^2(3)=1296\ \text{in}^3/\text{s}$$

**中文详解:** 先建立几何关系，再对时间求导；单位保持一致。

---

## 附录：考前 10 分钟速览 (Formula Sheet & Traps)

### A. 高频极限
| 极限 | 值 |
| :--- | :---: |
| $\lim_{x\to0}\dfrac{\sin x}{x}$ | $1$ |
| $\lim_{x\to0}\dfrac{\tan x}{x}$ | $1$ |
| $\lim_{x\to0}\dfrac{1-\cos x}{x}$ | $0$ |
| $\lim_{x\to0}\dfrac{1-\cos x}{x^2}$ | $\dfrac12$ |
| $\lim_{x\to0}\dfrac{\sin ax}{bx}$ | $\dfrac ab$ |
| $\lim_{x\to\infty}\dfrac{\sin x}{x}$ | $0$ |
| $\lim_{x\to0}(1+x)^{1/x}$ | $e$ |
| $\lim_{x\to\infty}\left(1+\dfrac1x\right)^x$ | $e$ |
| $\lim_{x\to0}\dfrac{e^x-1}{x}$ | $1$ |
| $\lim_{x\to0}\dfrac{\ln(1+x)}{x}$ | $1$ |
| $\lim_{x\to0}x\cos\dfrac1x$ | $0$ |

### B. 求导公式总表
| 函数 | 导数 | 函数 | 导数 |
| :---: | :---: | :---: | :---: |
| $x^r$ | $rx^{r-1}$ | $e^x$ | $e^x$ |
| $a^x$ | $a^x\ln a$ | $\ln x$ | $\dfrac1x$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ | $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ | $\tan x$ | $\sec^2x$ |
| $\cot x$ | $-\csc^2x$ | $\sec x$ | $\sec x\tan x$ |
| $\csc x$ | $-\csc x\cot x$ | $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | $\arctan x$ | $\dfrac{1}{1+x^2}$ |

### C. 十大易错点
1. $f^{-1}(x)\ne\dfrac{1}{f(x)}$。
2. $\arcsin(\sin x)=x$ 只在 $x\in[-\pi/2,\pi/2]$；$\arccos(\cos x)=x$ 只在 $[0,\pi]$。
3. $\lim_{x\to c}f(x)$ 与 $f(c)$ 无关；求极限先看能否直接代入。
4. $0/0$ 型必须约分或有理化，不能“分母为零所以极限不存在”。
5. $\sqrt{x^2}=\lvert x\rvert$；$x\to-\infty$ 时开方要变号。
6. 分母为零不一定是垂直渐近线（先约分；如 $\frac{\sin x}{x}$ 在 $0$ 处）。
7. 可导 $\Rightarrow$ 连续，连续 $\nRightarrow$ 可导（$\lvert x\rvert$ 在 $0$ 处）。
8. $1^\infty$ 型不能把底数直接当 $1$；用 $e^{\lim g(f-1)}$。
9. 隐函数求导中 $y$ 是 $x$ 的函数，$(y^2)'=2yy'$，漏乘 $y'$ 是常见失分点。
10. 相关变化率中“增加/减少”的符号、单位（in/s、cm³/min）要与题目一致。
