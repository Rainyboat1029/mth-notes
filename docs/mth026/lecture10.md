# Chapter 5 Integrals: 反导数与定积分 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 10 Summary)

### 4.10 Antiderivatives (反导数与不定积分)

#### 1. 反导数的定义 (Definition of an Antiderivative)

* **定义:** 若对区间 $I$ 上的每一个 $x$，都有
  $$F'(x)=f(x)$$
  则称 $F$ 是 $f$ 在区间 $I$ 上的一个**反导数 (antiderivative)**。
* **三个基本问题 (Three Questions):**
  * **存在性 (Existence):** 哪些函数有反导数？——**每一个连续函数都有反导数**（证明见 §5.3）。
  * **唯一性 (Uniqueness):** 反导数唯一吗？——**不唯一**：只要有一个反导数，就有无穷多个。
  * **一般形式 (Forms):** 所有反导数长什么样？——若 $F$ 是 $f$ 的一个反导数，则 $F(x)+C$（$C$ 为任意常数）给出 $f$ 的**全部**反导数。
* **为什么相差常数 (Why "+C"):** 由 §4.6 Theorem B，导数相同的两个函数只相差一个常数。因为 $(F+C)'=F'=f$，所以 $F+C$ 仍是反导数；反过来，若 $G'=f=F'$，则 $(G-F)'=0$，故 $G-F$ 为常数。

#### 2. 不定积分的记号 (Notation for Indefinite Integrals)

* **定义:** $f$ 的**全体反导数**称为 $f$ 的**一般反导数 (general antiderivative)** 或**不定积分 (indefinite integral)**，记作
  $$\int f(x)\,dx$$
  其中 $\int$ 是**积分号 (integral sign)**，$f(x)$ 是**被积函数 (integrand)**，$x$ 是**积分变量 (variable of integration)**。
* **术语:** "求反导数"也叫"**积分 (integrate)**"；$\int\cdots dx$ 表示**关于 $x$** 求反导数。
* **互为逆运算 (Inverse Operations):**
  $$D_x\int f(x)\,dx=f(x),\qquad \int D_xF(x)\,dx=F(x)+C$$
  即"先积分再求导"还原被积函数；"先求导再积分"还原原函数但必须补 $+C$。

#### 3. 幂函数法则与基本积分公式 (Power Rule & Basic Formulas)

* **Theorem A（幂法则 Power Rule）:** 若 $r$ 是任意实数且 $r\neq-1$，则
  $$\int x^{r}\,dx=\frac{x^{r+1}}{r+1}+C$$
  **证明:** 对右端求导，
  $$D_x\left(\frac{x^{r+1}}{r+1}+C\right)=\frac{1}{r+1}(r+1)x^{r}=x^{r}$$
  恰为被积函数。$\blacksquare$
* **为什么必须 $r\neq-1$:** 当 $r=-1$ 时公式分母为 $0$；此时 $\int\frac{1}{x}dx=\ln|x|+C$（见本节第 7 部分）。
* **Theorem B（基本积分公式 Basic Formulas）:**

| 序号 | 公式 | 说明 |
|---|---|---|
| (1) | $\displaystyle\int dx=x+C$ | 常函数 $1$ 的反导数 |
| (2) | $\displaystyle\int x^{n}dx=\frac{x^{n+1}}{n+1}+C$ | $n\neq-1$，幂法则 |
| (3) | $\displaystyle\int\frac{1}{x}dx=\ln|x|+C$ | 幂法则的唯一例外 |
| (4) | $\displaystyle\int\sin x\,dx=-\cos x+C$ | 三角函数 |
| (5) | $\displaystyle\int\cos x\,dx=\sin x+C$ | 三角函数 |
| (6) | $\displaystyle\int e^{x}dx=e^{x}+C$ | 指数函数 |
| (7) | $\displaystyle\int a^{x}dx=\frac{a^{x}}{\ln a}+C$ | $a>0,\ a\neq1$ |
| (8) | $\displaystyle\int\frac{dx}{\sqrt{1-x^{2}}}=\sin^{-1}x+C$ | 反三角 |
| (9) | $\displaystyle\int\frac{dx}{1+x^{2}}=\tan^{-1}x+C$ | 反三角 |

* **记号约定:** $\int 1\,dx$ 常简写为 $\int dx$；$\int\frac{1}{x}dx$ 常简写为 $\int\frac{dx}{x}$。

#### 4. 积分的线性性质 (Linearity of the Indefinite Integral)

* **Theorem C（线性性质）:** 设 $f$、$g$ 都有反导数，$k$ 为常数，则
  $$\int k f(x)\,dx=k\int f(x)\,dx,\qquad \int\big[f(x)\pm g(x)\big]\,dx=\int f(x)\,dx\pm\int g(x)\,dx$$
  **证明:** 对右端求导即可：$D_x\left(k\int f\,dx\right)=kf(x)$，$D_x\left(\int f\,dx\pm\int g\,dx\right)=f(x)\pm g(x)$。$\blacksquare$
* **重要提醒:** 积分**没有**乘积法则和商法则！一般地
  $$\int f(x)g(x)\,dx\neq\left(\int f(x)\,dx\right)\left(\int g(x)\,dx\right)$$
  乘积形式的积分要靠换元（本节第 5、6 部分）或分部积分（后续章节）处理。
* **合并常数:** 逐项积分会冒出多个任意常数 $C_1,C_2,\dots$，习惯上把它们合并成一个 $C$，因为常数之和仍是常数。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】由导数反推函数族（含图像）

**Problem:** Find an antiderivative of $f(x)=4x^{3}$ on $(-\infty,\infty)$, and write down the general antiderivative.

* **Process (解题步骤):**
  1. 猜测哪个函数的导数等于 $4x^{3}$：
     $$D_x\left(x^{4}\right)=4x^{3}$$
  2. 所以一个反导数是
     $$F(x)=x^{4}$$
  3. 一般反导数为
     $$\int 4x^{3}\,dx=x^{4}+C$$

* **中文详解:** 反导数就是"倒着做求导"。因为 $x^{4}$ 求导恰好得到 $4x^{3}$，所以 $F(x)=x^{4}$ 是一个反导数。把图像上下平移得到 $x^{4}+6$、$x^{4}$、$x^{4}-4$ 等无穷多条曲线，它们在同一个 $x$ 处的**切线斜率完全相同**（都是 $4x^{3}$），这正是"反导数不唯一、但彼此只差常数"的几何解释。考试中写完 $F(x)$ 后一定要补 $+C$，否则只是"一个"反导数而不是全体。

##### 【课件例题 2】幂法则处理分数指数

**Problem:** Find the general antiderivative of $f(x)=x^{4/3}$.

* **Process (解题步骤):**
  1. 这里 $r=\dfrac{4}{3}\neq-1$，直接用幂法则：
     $$\int x^{4/3}\,dx=\frac{x^{7/3}}{1+\frac{4}{3}}+C$$
  2. 化简分母 $1+\frac{4}{3}=\frac{7}{3}$：
     $$\int x^{4/3}\,dx=\frac{3}{7}x^{7/3}+C$$

* **中文详解:** 幂法则的公式是 $\frac{x^{r+1}}{r+1}$，关键是先把 $r+1$ 算对：$r=\frac43$ 时 $r+1=\frac73$，除以 $\frac73$ 等于乘以 $\frac37$。**常见错误**是把结果写成 $\frac{x^{7/3}}{7/3}$ 后不再化简，或者把指数错写成 $\frac43+1=\frac53$。验算方法很简单：对 $\frac37x^{7/3}$ 求导，$\frac37\cdot\frac73x^{4/3}=x^{4/3}$，还原成功。

##### 【课件例题 3】用线性性质拆开积分

**Problem:** Using the linearity of $\int$, evaluate
(a) $\displaystyle\int(3x^{2}+4x-2)\,dx$, (b) $\displaystyle\int\left(\frac{1}{t^{2}}+\sqrt{t}\right)dt$.

* **Process (解题步骤):**
  1. (a) 逐项积分并合并常数：
     $$\int(3x^{2}+4x-2)\,dx=3\int x^{2}dx+4\int x\,dx-2\int dx$$
     $$=3\left(\frac{x^{3}}{3}+C_1\right)+4\left(\frac{x^{2}}{2}+C_2\right)-2(x+C_3)=x^{3}+2x^{2}-2x+C$$
  2. (b) 先改写为幂函数：
     $$\int\left(\frac{1}{t^{2}}+\sqrt{t}\right)dt=\int\left(t^{-2}+t^{1/2}\right)dt=-\frac{1}{t}+\frac{2}{3}t^{3/2}+C$$

* **中文详解:** 线性性质允许把和差拆成若干简单积分、把常数提到积分号外。(a) 中三个常数 $3C_1$、$4C_2$、$-2C_3$ 合并成一个 $C$——这是标准做法，因为任意常数之和仍是任意常数。(b) 的要点是先把 $\frac{1}{t^{2}}$ 写成 $t^{-2}$、把 $\sqrt{t}$ 写成 $t^{1/2}$，再套幂法则：$\frac{t^{-1}}{-1}=-\frac1t$，$\frac{t^{3/2}}{3/2}=\frac23t^{3/2}$。注意积分变量换成了 $t$，微分符号必须跟着写成 $dt$。

#### 5. 广义幂法则 (Generalized Power Rule)

* **回顾链式法则:** 对幂函数复合，
  $$D_x\big[g(x)\big]^{r}=r\big[g(x)\big]^{r-1}g'(x)$$
* **Theorem D（广义幂法则）:** 设 $g$ 可导、$r\neq-1$，则
  $$\int\big[g(x)\big]^{r}g'(x)\,dx=\frac{\big[g(x)\big]^{r+1}}{r+1}+C$$
* **微分写法:** 若 $u=g(x)$，则 $du=g'(x)dx$，于是形式上有
  $$\int\big[g(x)\big]^{r}g'(x)\,dx=\int u^{r}\,du=\frac{u^{r+1}}{r+1}+C=\frac{\big[g(x)\big]^{r+1}}{r+1}+C$$
* **使用要点:** 被积函数中必须**完整地**出现 $g'(x)dx$（可以差一个常数倍，用乘除常数调整）；核心是识别"内层函数 $g(x)$ 及其导数"。

#### 6. 换元法则 (The Substitution Rule)

* **Theorem 5.4B（不定积分换元法则）:** 设 $g$ 可导，$F$ 是 $f$ 的反导数，则
  $$\int f\big(g(x)\big)g'(x)\,dx=F\big(g(x)\big)+C$$
  **证明:** 由链式法则，
  $$D_x\Big[F\big(g(x)\big)+C\Big]=F'\big(g(x)\big)g'(x)=f\big(g(x)\big)g'(x)$$
  故右端确是左端的全体反导数。$\blacksquare$
* **换元四步 (Four Steps):**
  1. 令 $u=g(x)$（通常取"内层函数"或"分母"或"根号里"）；
  2. 求微分 $du=g'(x)dx$；
  3. 把原积分整体改写成关于 $u$ 的积分（常数因子用乘除调整，**不能**把含 $x$ 的因子留在外面）；
  4. 对 $u$ 积分后**回代** $u=g(x)$，并补 $+C$。
* **常用特例:** 若 $f(u)=\dfrac{1}{u}$，则
  $$\int\frac{g'(x)}{g(x)}\,dx=\int\frac{du}{u}=\ln|u|+C=\ln|g(x)|+C$$
  即"**分子恰是分母的导数 ⇒ 积分等于分母的对数**"，这是识别换元最快的信号。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 4】广义幂法则的两个基本型

**Problem:** Evaluate (a) $\displaystyle\int(x^{4}+3x)^{30}(4x^{3}+3)\,dx$, (b) $\displaystyle\int\sin^{10}x\cos x\,dx$.

* **Process (解题步骤):**
  1. (a) 令 $g(x)=x^{4}+3x$，则 $g'(x)=4x^{3}+3$，恰好是括号外的因子：
     $$\int(x^{4}+3x)^{30}(4x^{3}+3)\,dx=\frac{(x^{4}+3x)^{31}}{31}+C$$
  2. (b) 令 $u=\sin x$，则 $du=\cos x\,dx$：
     $$\int\sin^{10}x\cos x\,dx=\int u^{10}du=\frac{u^{11}}{11}+C=\frac{\sin^{11}x}{11}+C$$

* **中文详解:** 这两小题是广义幂法则的"标准识别题"：被积函数形如 $[\text{内层}]^{r}\cdot[\text{内层的导数}]$。(a) 中外层是 $30$ 次幂，内层 $x^{4}+3x$ 的导数 $4x^{3}+3$ 一字不差地出现在外面，直接套公式。(b) 中 $\sin^{10}x$ 是 $\sin x$ 的 $10$ 次幂，而 $\cos x$ 正是 $\sin x$ 的导数。判断这类题只需问一句：**括号外那个因子，是不是括号里那个东西的导数？**若是，答案就是把指数加一、再除以新指数。

##### 【课件例题 5】换元时的常数调整

**Problem:** Evaluate (a) $\displaystyle\int(x^{3}+6x)^{5}(6x^{2}+12)\,dx$, (b) $\displaystyle\int\frac{x}{10-x^{2}}\,dx$.

* **Process (解题步骤):**
  1. (a) 令 $u=x^{3}+6x$，则 $du=(3x^{2}+6)dx$，而
     $$(6x^{2}+12)dx=2(3x^{2}+6)dx=2\,du$$
     于是
     $$\int(x^{3}+6x)^{5}(6x^{2}+12)\,dx=\int u^{5}\cdot2\,du=2\cdot\frac{u^{6}}{6}+C=\frac{(x^{3}+6x)^{6}}{3}+C$$
  2. (b) 令 $u=10-x^{2}$，则 $du=-2x\,dx$，即 $x\,dx=-\frac12du$：
     $$\int\frac{x}{10-x^{2}}\,dx=-\frac12\int\frac{1}{u}du=-\frac12\ln|u|+C=-\frac12\ln|10-x^{2}|+C$$

* **中文详解:** (a) 的关键是"**差一个常数倍**"——括号外的系数是 $6$，而内层导数是 $3x^{2}+6$，两者差因子 $2$。常数可以自由进出积分号，所以先写成 $2\int u^{5}du$ 再积分。(b) 是"分子是分母导数的常数倍"型：分母 $10-x^{2}$ 的导数是 $-2x$，分子只有 $x$，差因子 $-\frac12$；凑成 $-\frac12\int\frac{du}{u}$ 后得对数。注意绝对值不能丢：$10-x^{2}$ 可正可负（在 $|x|>\sqrt{10}$ 时为负），只有写成 $\ln|10-x^{2}|$ 才对所有 $x$ 成立。

##### 【课件例题 6】假分式先做长除法

**Problem:** Find $\displaystyle\int\frac{x^{2}-x}{x+1}\,dx$.

* **Process (解题步骤):**
  1. 分子次数 $\ge$ 分母次数，先做多项式长除法：
     $$x^{2}-x=(x+1)(x-2)+2$$
     即
     $$\frac{x^{2}-x}{x+1}=x-2+\frac{2}{x+1}$$
  2. 逐项积分：
     $$\int\frac{x^{2}-x}{x+1}\,dx=\int\left(x-2+\frac{2}{x+1}\right)dx=\frac{x^{2}}{2}-2x+2\ln|x+1|+C$$

* **中文详解:** 当被积函数是**假分式**（分子次数不小于分母次数）时，第一步永远是长除法，把它拆成"多项式 + 真分式"。本题 $x^{2}-x$ 除以 $x+1$ 得商 $x-2$、余 $2$，于是被积函数化为 $x-2+\frac{2}{x+1}$，三项都能直接积分。**不能**对 $\frac{x^{2}-x}{x+1}$ 直接套 $\ln$ 公式——$\ln$ 公式只适用于"分子是分母导数"的情形，这里不满足。
* **Exercise（自测）:** $\displaystyle\int\frac{x^{2}-x}{x^{2}+1}\,dx$。提示：先写成 $1-\frac{x+1}{x^{2}+1}$，再拆成 $1-\frac{x}{x^{2}+1}-\frac{1}{x^{2}+1}$，答案为
  $$x-\frac{1}{2}\ln(x^{2}+1)-\tan^{-1}x+C$$

#### 7. 常用反导数补充公式（自学部分）

* **$\dfrac{1}{x}$ 的反导数:** 对 $x>0$ 有 $D_x(\ln x)=\frac1x$；对 $x<0$，由链式法则
  $$D_x\big(\ln(-x)\big)=\frac{1}{-x}\cdot(-1)=\frac{1}{x}$$
  所以对一切 $x\neq0$，
  $$\int\frac{dx}{x}=\ln|x|+C$$
  几何上：$y=\ln|x|$ 是偶函数，$x=c$ 与 $x=-c$ 处的斜率互为相反数，而 $\frac{1}{-c}=-\frac1c$，恰好对应。
* **线性内层 $ax+b$ 的特例:** 若 $F'=f$，则
  $$\int f(ax+b)\,dx=\frac{1}{a}F(ax+b)+C\qquad(a\neq0)$$
  例如
  $$\int\sin 3x\,dx=-\frac{1}{3}\cos 3x+C,\qquad \int e^{-2x}dx=-\frac{1}{2}e^{-2x}+C$$
* **选对换元 (Choosing the Right Substitution):** 同一个函数可能有两种换元思路，选错会绕远路。
  $$\int\frac{dx}{1+3x^{2}}=\frac{1}{\sqrt{3}}\tan^{-1}\big(\sqrt{3}x\big)+C\qquad(\text{令 }u=\sqrt{3}x)$$
  $$\int\frac{x}{1+3x^{2}}\,dx=\frac{1}{6}\ln(1+3x^{2})+C\qquad(\text{令 }u=1+3x^{2})$$
* **$\tan x$ 与 $\cot x$:**
  $$\int\tan x\,dx=\int\frac{\sin x}{\cos x}\,dx=-\ln|\cos x|+C=\ln|\sec x|+C$$
  $$\int\cot x\,dx=\ln|\sin x|+C$$
* **$\sec x$ 与 $\dfrac{1}{1-x^{2}}$（技巧型）:**
  $$\int\sec x\,dx=\int\frac{\sec x(\sec x+\tan x)}{\sec x+\tan x}\,dx=\ln|\sec x+\tan x|+C$$
  $$\int\frac{dx}{1-x^{2}}=\frac{1}{2}\int\left(\frac{1}{1+x}+\frac{1}{1-x}\right)dx=\frac{1}{2}\ln\left|\frac{1+x}{1-x}\right|+C$$
* **简单微分公式表 (Simple Differential Formulas):**

| 微分形式 | 等价写法 |
|---|---|
| $dx=\dfrac{1}{a}d(ax+b)$ | 线性内层换元 |
| $x\,dx=\dfrac{1}{2}d(x^{2})$ | 二次内层换元 |
| $\dfrac{dx}{x^{2}}=-d\left(\dfrac{1}{x}\right)$ | 负幂 |
| $\dfrac{dx}{\sqrt{x}}=2\,d(\sqrt{x})$ | 根式 |
| $\dfrac{dx}{x}=d(\ln x)$ | $x>0$ |
| $e^{x}dx=d(e^{x})$ | 指数 |
| $\sin x\,dx=-d(\cos x)$ | 三角 |
| $\cos x\,dx=d(\sin x)$ | 三角 |
| $\sec^{2}x\,dx=d(\tan x)$ | 三角 |
| $\dfrac{dx}{1+x^{2}}=d(\arctan x)$ | 反三角 |

* **反导数不唯一（同一函数的不同答案）:** 同一个不定积分用不同方法可能得到"看起来不同"的答案，它们只差一个常数。例如
  $$\int\sin x\cos x\,dx=\frac{1}{2}\sin^{2}x+C\quad\text{或}\quad-\frac{1}{4}\cos 2x+C$$
  两者相差 $\frac14$（因为 $\sin^{2}x=\frac{1-\cos 2x}{2}$），都属于正确答案。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 7】$\tan x$ 的反导数

**Problem:** Evaluate $\displaystyle\int\tan x\,dx$.

* **Process (解题步骤):**
  1. 把 $\tan x$ 写成 $\dfrac{\sin x}{\cos x}$：
     $$\int\tan x\,dx=\int\frac{\sin x}{\cos x}\,dx$$
  2. 令 $u=\cos x$，则 $du=-\sin x\,dx$，即 $\sin x\,dx=-du$：
     $$\int\frac{\sin x}{\cos x}\,dx=-\int\frac{du}{u}=-\ln|u|+C$$
  3. 回代：
     $$-\ln|\cos x|+C=\ln|\sec x|+C$$

* **中文详解:** 这里的关键观察是"分子恰是分母导数的相反数"：$(\cos x)'=-\sin x$，所以分子 $\sin x$ 与分母的导数只差一个负号，凑成 $-\int\frac{du}{u}$ 后得对数。结果可以写成 $-\ln|\cos x|$ 或 $\ln|\sec x|$，两者等价。**常见错误**是漏掉负号写成 $\ln|\cos x|$，可以用求导验算：$(\ln|\sec x|)'=\sec x\tan x/\sec x=\tan x$，正确。

##### 【课件例题 8】$\sec x$ 与 $\dfrac{1}{1-x^{2}}$ 的技巧型积分

**Problem:** Evaluate $\displaystyle\int\sec x\,dx$ and $\displaystyle\int\frac{dx}{1-x^{2}}$.

* **Process (解题步骤):**
  1. $\sec x$ 的积分靠"**乘以并除以** $\sec x+\tan x$"：
     $$\int\sec x\,dx=\int\frac{\sec^{2}x+\sec x\tan x}{\sec x+\tan x}\,dx$$
     分子恰是分母的导数（$(\sec x+\tan x)'=\sec x\tan x+\sec^{2}x$），故
     $$\int\sec x\,dx=\ln|\sec x+\tan x|+C$$
  2. $\dfrac{1}{1-x^{2}}$ 先做**部分分式分解**：
     $$\frac{1}{1-x^{2}}=\frac{1}{(1-x)(1+x)}=\frac{1}{2}\left(\frac{1}{1+x}+\frac{1}{1-x}\right)$$
  3. 逐项积分（注意第二项要凑 $-d(1-x)$）：
     $$\int\frac{dx}{1-x^{2}}=\frac{1}{2}\Big[\ln|1+x|-\ln|1-x|\Big]+C=\frac{1}{2}\ln\left|\frac{1+x}{1-x}\right|+C$$

* **中文详解:** 这两题都不能靠"直接套公式"，而是考技巧。(1) $\sec x$ 的积分是微积分里的经典技巧：分子分母同乘 $\sec x+\tan x$ 后，分子恰好变成分母的导数，于是积分化为 $\int\frac{du}{u}$。(2) 有理分式先**因式分解 + 部分分式**，拆成两个一次分式之和，再分别用 $\ln$ 公式；注意 $\frac{1}{1-x}$ 的原函数是 $-\ln|1-x|$（因为 $(1-x)'=-1$，需要补负号）。这类"拆项 + 凑微分"是 Chapter 7 积分技巧的雏形。

##### 【课件例题 9】反导数不唯一：两种解法得到的答案不同

**Problem:** Evaluate $\displaystyle\int\sin x\cos x\,dx$ in two ways, and explain why the two answers look different.

* **Process (解题步骤):**
  1. **解法一:** 令 $u=\sin x$，$du=\cos x\,dx$：
     $$\int\sin x\cos x\,dx=\int u\,du=\frac{1}{2}u^{2}+C=\frac{1}{2}\sin^{2}x+C$$
  2. **解法二:** 用倍角公式 $\sin 2x=2\sin x\cos x$，令 $u=2x$：
     $$\int\sin x\cos x\,dx=\frac{1}{2}\int\sin 2x\,dx=-\frac{1}{4}\cos 2x+C$$
  3. **两者一致:** 因为 $\sin^{2}x=\dfrac{1-\cos 2x}{2}$，所以
     $$\frac{1}{2}\sin^{2}x=\frac{1}{4}-\frac{1}{4}\cos 2x$$
     两个答案只差常数 $\dfrac14$，都可写成"$\cdots+C$"的形式。

* **中文详解:** 这题说明"反导数不唯一"不仅体现在 $+C$，也体现在**不同方法可能得到形式完全不同的表达式**。$\frac12\sin^{2}x$ 与 $-\frac14\cos 2x$ 求导都等于 $\sin x\cos x$，它们相差常数 $\frac14$，被吸收进任意常数 $C$ 里。遇到这种情况不要以为自己算错：**判断标准只有一条——求导回去是否等于被积函数**。考试中任选一种写法即可，但同一题内不要混用两种形式。

### 5.1 Introduction to Area (面积的引入)

#### 1. 用逼近法定义面积 (Area by Approximation)

* **已知面积:** 矩形 $A=lw$，平行四边形 $A=bh$，三角形 $A=\frac12bh$；多边形可以分割成三角形求和：$A=A_1+A_2+\cdots+A_n$。
* **圆面积的处理（Archimedes 的思想）:** 对单位圆作**内接正多边形** $P_1,P_2,P_3,\dots$（边数 $4,8,16,\dots$），圆面积定义为
  $$A(\text{circle})=\lim_{n\to\infty}A(P_n)$$
* **一般问题:** 边界是**曲线**的区域，面积怎么定义？——用一列内接多边形（或矩形）去逼近，把面积定义为这些近似面积的**极限**。

#### 2. 四步法：从内接矩形到精确面积 (Four-Step Procedure)

以 $y=f(x)=x^{2}$ 在 $[0,2]$ 上、由曲线与 $x$ 轴围成的区域 $R$ 为例。

* **Step 1 分割 (Partition):** 把 $[0,2]$ 分成 $n$ 个等长子区间，每个长度
  $$\Delta x=\frac{2}{n},\qquad x_i=i\Delta x=\frac{2i}{n}\quad(i=0,1,\dots,n)$$
  即 $0=x_0<x_1<\cdots<x_n=2$。
* **Step 2 近似 (Approximation):** 在每个 $[x_{i-1},x_i]$ 上以**最小值** $f(x_{i-1})=x_{i-1}^{2}$ 为高作矩形（内接矩形），第 $i$ 个矩形面积为 $f(x_{i-1})\Delta x$。所有矩形之并 $R_n$ 称为**内接多边形 (inscribed polygon)**，其面积
  $$A(R_n)=f(x_0)\Delta x+f(x_1)\Delta x+\cdots+f(x_{n-1})\Delta x$$
* **Step 3 求和 (Summation):** 因为 $f$ 在 $[0,2]$ 上递增，最小值在左端点取到：
  $$f(x_{i-1})\Delta x=x_{i-1}^{2}\Delta x=\left(\frac{2(i-1)}{n}\right)^{2}\cdot\frac{2}{n}=\frac{8}{n^{3}}(i-1)^{2}$$
  于是
  $$A(R_n)=\frac{8}{n^{3}}\Big[0^{2}+1^{2}+2^{2}+\cdots+(n-1)^{2}\Big]=\frac{8}{n^{3}}\cdot\frac{(n-1)n(2n-1)}{6}$$
  $$=\frac{8}{6}\cdot\frac{2n^{3}-3n^{2}+n}{n^{3}}=\frac{8}{3}-\frac{4}{n}+\frac{4}{3n^{2}}$$
* **Step 4 取极限 (Limit):**
  $$A(R)=\lim_{n\to\infty}A(R_n)=\lim_{n\to\infty}\left(\frac{8}{3}-\frac{4}{n}+\frac{4}{3n^{2}}\right)=\frac{8}{3}$$
  数值上：$A(R_7)\approx\frac83-0.5442$，$A(R_{14})\approx\frac83-0.2789$，$A(R_{28})\approx\frac83-0.1412$——随着 $n$ 增大，近似值单调逼近 $\frac83$。
* **外接多边形 (Circumscribed Polygons):** 若把矩形的高改为每个子区间上的**最大值** $f(x_i)=x_i^{2}$，同样四步可得 $A(S_n)=\frac83+\frac{4}{n}+\frac{4}{3n^{2}}$，极限仍是 $\frac83$。**内接与外接给出同一个极限**，这提示面积与"怎么取点"无关——正是定积分定义的思想来源。

#### 3. 求和号与特殊求和公式 (Sigma Notation and Special Sums)

* **定义:**
  $$\sum_{i=1}^{n}a_i=a_1+a_2+\cdots+a_n$$
  $\Sigma$ 是希腊字母 sigma，表示"求和"；下标 $i$ 从 $\Sigma$ 下方的数开始，逐次加 $1$，到上方的数结束。
* **例子:**
  $$\sum_{i=2}^{4}a_ib_i=a_2b_2+a_3b_3+a_4b_4,\qquad \sum_{j=1}^{5}c=5c,\qquad \sum_{k=0}^{n}2^{k}=2^{0}+2^{1}+\cdots+2^{n}$$
* **Theorem 5.1A（$\Sigma$ 的线性性质）:** 设 $c$ 为常数，则
  $$\sum_{i=1}^{n}c=nc,\qquad \sum_{i=1}^{n}ca_i=c\sum_{i=1}^{n}a_i,\qquad \sum_{i=1}^{n}(a_i\pm b_i)=\sum_{i=1}^{n}a_i\pm\sum_{i=1}^{n}b_i$$
* **三个特殊求和公式（务必记住）:**
  $$\sum_{i=1}^{n}i=1+2+\cdots+n=\frac{n(n+1)}{2}$$
  $$\sum_{i=1}^{n}i^{2}=1^{2}+2^{2}+\cdots+n^{2}=\frac{n(n+1)(2n+1)}{6}$$
  $$\sum_{i=1}^{n}i^{3}=1^{3}+2^{3}+\cdots+n^{3}=\left[\frac{n(n+1)}{2}\right]^{2}$$

#### 4. 速度与位置 (Velocity and Position)

* **问题:** 物体沿 $x$ 轴运动，速度 $v=f(t)\ge0$，求 $t=a$ 到 $t=b$ 之间走过的距离。
* **匀速情形:** 速度为常数 $k$、时间间隔 $\Delta t$，距离 $=k\Delta t$。
* **变速情形:** 在 $t_0=a,t_1,\dots,t_n=b$ 处测速，每个子区间上速度**近似为常数** $f(t_i)$，则距离近似为
  $$f(t_1)\Delta t_1+f(t_2)\Delta t_2+\cdots+f(t_n)\Delta t_n=\sum_{i=1}^{n}f(t_i)\Delta t_i$$
  测速越密（$\Delta t_i\to0$）越精确，精确距离定义为
  $$d=\lim_{\text{all }\Delta t_i\to0}\sum_{i=1}^{n}f(t_i)\Delta t_i=\int_{a}^{b}v(t)\,dt$$
  这个和式称为 **Riemann 和 (Riemann sum)**。
* **注意:** 当 $v$ 可取负值时，$\int_a^b v\,dt$ 给出的是**位移 (displacement)** 而不是总路程；总路程要用 $\int_a^b|v|\,dt$。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 10】内接矩形逼近 $y=x^{2}$ 下方面积

**Problem:** Find the area $A(R)$ of the region $R$ bounded by $y=x^{2}$, the $x$-axis, and the line $x=2$, using inscribed rectangles.

* **Process (解题步骤):**
  1. 分割：$\Delta x=\dfrac{2}{n}$，$x_i=\dfrac{2i}{n}$。
  2. 近似：第 $i$ 个矩形高 $f(x_{i-1})=x_{i-1}^{2}$，面积 $\dfrac{8}{n^{3}}(i-1)^{2}$。
  3. 求和：
     $$A(R_n)=\frac{8}{n^{3}}\sum_{k=0}^{n-1}k^{2}=\frac{8}{n^{3}}\cdot\frac{(n-1)n(2n-1)}{6}=\frac{8}{3}-\frac{4}{n}+\frac{4}{3n^{2}}$$
  4. 取极限：
     $$A(R)=\lim_{n\to\infty}A(R_n)=\frac{8}{3}$$

* **中文详解:** 这是本章的"母题"，四步走完全程。要特别注意第 3 步的求和技巧：$\sum_{k=0}^{n-1}k^{2}$ 用的是前 $n-1$ 项平方和公式 $\frac{(n-1)n(2n-1)}{6}$，展开后三项分别除以 $n^{3}$，得 $\frac83-\frac4n+\frac{4}{3n^{2}}$。取极限时后两项都趋于 $0$，只剩 $\frac83$。**常见错误**：把 $\sum_{k=1}^{n}k^{2}$ 的公式套成前 $n$ 项、或把 $f(x_{i-1})$ 误写成 $f(x_i)$（那就变成外接矩形了，极限相同但和式不同）。

##### 【课件例题 11】外接矩形得到同一极限

**Problem:** Approximate the same region $R$ with circumscribed rectangles and show the limit is again $\frac{8}{3}$.

* **Process (解题步骤):**
  1. 外接矩形的高取每个子区间上的最大值 $f(x_i)=x_i^{2}=\dfrac{4i^{2}}{n^{2}}$。
  2. 每个矩形面积
     $$f(x_i)\Delta x=\frac{4i^{2}}{n^{2}}\cdot\frac{2}{n}=\frac{8i^{2}}{n^{3}}$$
  3. 求和：
     $$A(S_n)=\frac{8}{n^{3}}\sum_{i=1}^{n}i^{2}=\frac{8}{n^{3}}\cdot\frac{n(n+1)(2n+1)}{6}=\frac{8}{3}+\frac{4}{n}+\frac{4}{3n^{2}}$$
  4. 取极限：
     $$A(S)=\lim_{n\to\infty}A(S_n)=\frac{8}{3}$$

* **中文详解:** 内接矩形"从下面逼近"，外接矩形"从上面逼近"，两者的和式只差符号：内接是 $\frac83-\frac4n+\cdots$，外接是 $\frac83+\frac4n+\cdots$，夹逼之下极限都等于 $\frac83$。这个对比说明：**只要分割越来越细，无论用左端点、右端点还是区间内任意点作高，极限都相同**——这就是下一节定积分定义中"极限与取点方式无关"的直观依据。

### 5.2 The Definite Integral (定积分)

#### 1. 从面积到定积分：Riemann 和 (From Area to the Definite Integral)

设 $f(x)\ge0$，求曲线 $y=f(x)$ 与 $x$ 轴在 $[a,b]$ 上围成的区域 $R$ 的面积。

* **Step 1 分割:** 任取分割 $a=x_0<x_1<\cdots<x_n=b$，记 $\Delta x_i=x_i-x_{i-1}$（**不必等长**）。
* **Step 2 取点:** 在每个子区间上任取**样本点 (sample point)** $\bar{x}_i\in[x_{i-1},x_i]$，以 $f(\bar{x}_i)$ 为高作矩形。
* **Step 3 求和:** 面积近似为
  $$\sum_{i=1}^{n}f(\bar{x}_i)\Delta x_i=f(\bar{x}_1)\Delta x_1+\cdots+f(\bar{x}_n)\Delta x_n$$
* **Step 4 取极限:**
  $$A(R)=\lim_{\text{all }\Delta x_i\to0}\sum_{i=1}^{n}f(\bar{x}_i)\Delta x_i$$

#### 2. 定积分的定义 (Definition of the Definite Integral)

* **定义:** 设 $f$ 在闭区间 $[a,b]$ 上有定义。若极限
  $$\lim_{\text{all }\Delta x_i\to0}\sum_{i=1}^{n}f(\bar{x}_i)\Delta x_i$$
  **存在**，且**不依赖于**分割的选取与样本点 $\bar{x}_i$ 的选取，则称 $f$ 在 $[a,b]$ 上**可积 (integrable)**，并称此极限为 $f$ 从 $a$ 到 $b$ 的**定积分 (definite integral)**：
  $$\int_{a}^{b}f(x)\,dx:=\lim_{\text{all }\Delta x_i\to0}\sum_{i=1}^{n}f(\bar{x}_i)\Delta x_i$$
* **要点:** 定义中"不依赖"三个字最关键——它保证了定积分是**区域本身**的属性，而不是某种近似方案的结果。

#### 3. 记号、几何意义与约定 (Notation, Geometric Meaning, Conventions)

* **记号解剖:** $\displaystyle\int_{a}^{b}f(x)\,dx$ 中，$a$ 是**下限 (lower limit)**，$b$ 是**上限 (upper limit)**，$[a,b]$ 是**积分区间**，$f(x)$ 是**被积函数**，$x$ 是**积分变量**。
* **提醒 (Caution):** 这里的"上下限"与函数的**极限 (limit)** 毫无关系，只是积分区间的端点。
* **几何意义（有向面积 Signed Area）:** 设 $a<b$ 且 $f$ 可积，
  * $f(x)\ge0$ 时，$\int_a^b f$ 等于曲线下方的**普通面积**；
  * $f(x)\le0$ 时，$\int_a^b f$ 等于该面积的**相反数**；
  * 一般地，$\int_a^b f$ 等于 $x$ 轴上方面积减去下方面积：
    $$\int_{a}^{b}f(x)\,dx=A_{\text{up}}-A_{\text{down}}$$
* **哑变量 (Dummy Variable):** 积分变量可以任意改名，
  $$\int_{a}^{b}f(x)\,dx=\int_{a}^{b}f(t)\,dt=\int_{a}^{b}f(u)\,du$$
* **约定 (Conventions):**
  $$\int_{a}^{a}f(x)\,dx=0,\qquad \int_{b}^{a}f(x)\,dx=-\int_{a}^{b}f(x)\,dx\quad(a>b)$$
  即"区间退化为一点时积分为 $0$"，"交换上下限变号"。

#### 4. 定积分的基本性质 (Properties of the Definite Integral)

* **Theorem 5.3D（线性性质 Linearity）:** 设 $k$ 为常数，且相关积分都存在，则
  $$\int_{a}^{b}k\,dx=k(b-a),\qquad \int_{a}^{b}kf(x)\,dx=k\int_{a}^{b}f(x)\,dx$$
  $$\int_{a}^{b}\big[f(x)\pm g(x)\big]dx=\int_{a}^{b}f(x)\,dx\pm\int_{a}^{b}g(x)\,dx$$
* **Theorem B（区间可加性 Interval Additivity）:** 若 $f$ 在包含 $a,b,c$ 的区间上可积，则
  $$\int_{a}^{c}f(x)\,dx=\int_{a}^{b}f(x)\,dx+\int_{b}^{c}f(x)\,dx$$
  **无论 $a,b,c$ 的大小顺序如何**都成立。例如
  $$\int_{0}^{2}x^{2}dx=\int_{0}^{1}x^{2}dx+\int_{1}^{2}x^{2}dx,\qquad \int_{0}^{2}x^{2}dx=\int_{0}^{3}x^{2}dx+\int_{3}^{2}x^{2}dx$$
  常用变形：$\displaystyle\int_{b}^{c}f=\int_{a}^{c}f-\int_{a}^{b}f$。
* **Theorem 5.3B（比较性质 Comparison）:** 若 $f,g$ 在 $[a,b]$ 上可积且 $f(x)\le g(x)$ 对一切 $x\in[a,b]$ 成立，则
  $$\int_{a}^{b}f(x)\,dx\le\int_{a}^{b}g(x)\,dx$$
  即"定积分保持不等号"。
* **Theorem 5.3C（有界性质 Boundedness）:** 若 $m\le f(x)\le M$ 对一切 $x\in[a,b]$ 成立，则
  $$m(b-a)\le\int_{a}^{b}f(x)\,dx\le M(b-a)$$
  这是"用常数函数夹逼"的比较性质，常用于**估计积分值**或**证明不等式**。
* **Theorem 5.5B（对称性质 Symmetry）:** 设 $f$ 在 $[-a,a]$ 上可积，
  * 若 $f$ 为**偶函数**，则 $\displaystyle\int_{-a}^{a}f(x)\,dx=2\int_{0}^{a}f(x)\,dx$；
  * 若 $f$ 为**奇函数**，则 $\displaystyle\int_{-a}^{a}f(x)\,dx=0$。
  直观上：偶函数左右面积相等（相加），奇函数左右面积符号相反（抵消）。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 12】用几何意义算定积分

**Problem:** Compute by geometric meaning (a) $\displaystyle\int_{0}^{1}\sqrt{1-x^{2}}\,dx$, (b) $\displaystyle\int_{0}^{2\pi}\sin x\,dx$.

* **Process (解题步骤):**
  1. (a) 令 $y=\sqrt{1-x^{2}}$，则 $y\ge0$ 且
     $$y^{2}=1-x^{2}\iff x^{2}+y^{2}=1$$
     这是**单位圆的上半圆**。积分区间 $[0,1]$ 对应**四分之一圆**，面积
     $$\int_{0}^{1}\sqrt{1-x^{2}}\,dx=\frac{1}{4}\pi\cdot1^{2}=\frac{\pi}{4}$$
  2. (b) $y=\sin x$ 在 $[0,\pi]$ 上为正、在 $[\pi,2\pi]$ 上为负，两瓣面积相等，故
     $$\int_{0}^{2\pi}\sin x\,dx=0$$

* **中文详解:** 几何法的思路是"认曲线"。(a) 看到 $\sqrt{1-x^{2}}$ 就要想到单位圆——平方后是 $x^{2}+y^{2}=1$，且根号保证 $y\ge0$，所以是上半圆；区间 $[0,1]$ 只取右半部分，是四分之一圆，面积 $\frac{\pi}{4}$。(b) 正负面积相等的结论要求两瓣**形状全等**：$\sin x$ 在 $[0,\pi]$ 与 $[\pi,2\pi]$ 上的图像关于 $x$ 轴对称，所以积分为 $0$。若区间不对称（如 $[0,\pi]$），答案就是 $2$ 而不是 $0$。

##### 【课件例题 13】区间可加性：$\int_{-1}^{2}|x|\,dx$

**Problem:** Evaluate $\displaystyle\int_{-1}^{2}|x|\,dx$.

* **Process (解题步骤):**
  1. 在 $x=0$ 处拆开（绝对值在此变号）：
     $$\int_{-1}^{2}|x|\,dx=\int_{-1}^{0}|x|\,dx+\int_{0}^{2}|x|\,dx$$
  2. 分段去掉绝对值：$x\le0$ 时 $|x|=-x$，$x\ge0$ 时 $|x|=x$，对应两个三角形：
     $$\int_{-1}^{0}(-x)\,dx=\frac{1}{2}\cdot1\cdot1=\frac{1}{2},\qquad \int_{0}^{2}x\,dx=\frac{1}{2}\cdot2\cdot2=2$$
  3. 相加：
     $$\int_{-1}^{2}|x|\,dx=\frac{1}{2}+2=\frac{5}{2}$$

* **中文详解:** 含绝对值的被积函数必须**在变号点拆区间**，否则不能直接积分。本题在 $x=0$ 拆开：左边是底 $1$、高 $1$ 的三角形（面积 $\frac12$），右边是底 $2$、高 $2$ 的三角形（面积 $2$），合计 $\frac52$。几何上这也说明"定积分是可加的"：两块区域的面积直接相加。**常见错误**：不分段就把 $|x|$ 当成 $x$ 积分，会得到 $\frac{4-1}{2}=\frac32$，漏掉了左半边的面积。

##### 【课件例题 14】比较性质：$\sin x\le x\le\tan x$

**Problem:** Using $\sin x\le x\le\tan x$ for $0\le x\le1$, compare $\displaystyle\int_{0}^{1}\sin x\,dx$, $\displaystyle\int_{0}^{1}x\,dx$, and $\displaystyle\int_{0}^{1}\tan x\,dx$.

* **Process (解题步骤):**
  1. 已知在 $[0,1]$ 上 $\sin x\le x\le\tan x$，由比较性质（Theorem 5.3B）：
     $$\int_{0}^{1}\sin x\,dx\le\int_{0}^{1}x\,dx\le\int_{0}^{1}\tan x\,dx$$
  2. 中间项用几何意义（三角形面积）：
     $$\int_{0}^{1}x\,dx=\frac{1}{2}\cdot1\cdot1=\frac{1}{2}$$
  3. 结论：
     $$\int_{0}^{1}\sin x\,dx\le\frac{1}{2},\qquad \int_{0}^{1}\tan x\,dx\ge\frac{1}{2}$$

* **中文详解:** 比较性质是"不等式可以直接搬到积分上"的合法性依据，前提是**区间相同**且**逐点成立**。这里不需要真的算出 $\int\sin$ 和 $\int\tan$ 的值（它们没有初等原函数），只要把中间那个 $\int_0^1 x\,dx=\frac12$ 算出来，就同时给出了上下界。这类题在考试中常以"证明某积分大于/小于某数"的形式出现，套路就是：**找一个能积出来的函数夹住它**。

##### 【课件例题 15】有界性质估计积分

**Problem:** Show that $\displaystyle 0\le\int_{0}^{\pi/2}\sin x\,dx\le\frac{\pi}{2}$.

* **Process (解题步骤):**
  1. 在 $[0,\frac{\pi}{2}]$ 上，$0\le\sin x\le1$，即 $m=0$，$M=1$。
  2. 由有界性质（Theorem 5.3C），取 $a=0$，$b=\frac{\pi}{2}$，$b-a=\frac{\pi}{2}$：
     $$0\cdot\frac{\pi}{2}\le\int_{0}^{\pi/2}\sin x\,dx\le1\cdot\frac{\pi}{2}$$
  3. 即
     $$0\le\int_{0}^{\pi/2}\sin x\,dx\le\frac{\pi}{2}$$

* **中文详解:** 有界性质把"函数值的上下界"翻译成"积分值的上下界"，缩放因子是区间长度 $b-a$——这一点最容易漏。本题真实值是 $\int_0^{\pi/2}\sin x\,dx=1$，确实夹在 $0$ 与 $\frac{\pi}{2}\approx1.571$ 之间。若把区间改成 $[0,\pi]$，则 $b-a=\pi$，估计式变成 $0\le\int_0^{\pi}\sin x\,dx\le\pi$，而真实值是 $2$，仍然成立——这说明有界性质给出的是**粗估**，不必是最优界。

##### 【课件例题 16】对称性质：奇偶函数在对称区间上的积分

**Problem:** Evaluate without the Newton–Leibniz formula: (a) $\displaystyle\int_{-100}^{100}\tan^{-1}x\,dx$, (b) $\displaystyle\int_{-\pi}^{\pi}\sin^{3}x\cos^{5}x\,dx$.

* **Process (解题步骤):**
  1. (a) $f(x)=\tan^{-1}x$ 是**奇函数**（$\tan^{-1}(-x)=-\tan^{-1}x$），区间 $[-100,100]$ 关于原点对称，故
     $$\int_{-100}^{100}\tan^{-1}x\,dx=0$$
  2. (b) $\sin^{3}x$ 是奇函数，$\cos^{5}x$ 是偶函数，乘积
     $$(-\sin x)^{3}\cos^{5}(-x)=-\sin^{3}x\cos^{5}x$$
     仍为**奇函数**，故
     $$\int_{-\pi}^{\pi}\sin^{3}x\cos^{5}x\,dx=0$$

* **中文详解:** 只要区间关于原点对称，就先检查奇偶性——奇函数积分为 $0$，偶函数积分为"一半区间的两倍"，往往能省掉全部计算。判断复合函数的奇偶性用定义：把 $x$ 换成 $-x$ 看结果是否变号。(b) 中"奇 × 偶 = 奇"是通用规律（奇函数乘偶函数仍为奇函数），因此不必展开 $\sin^{3}x\cos^{5}x$。**注意**：若区间不对称（如 $[0,\pi]$），对称性质完全不适用。

##### 【课件例题 17】由速度图像/分段函数求位置

**Problem:** An object at the origin at $t=0$ has velocity (m/s)
$$v(t)=\begin{cases}t/20, & 0\le t\le40\\ 2, & 40<t\le60\\ 5-t/20, & t>60\end{cases}$$
Sketch the velocity curve, express the position at $t=140$ as a definite integral, and evaluate it geometrically.

* **Process (解题步骤):**
  1. 图像：$[0,40]$ 上是从 $(0,0)$ 到 $(40,2)$ 的直线段；$[40,60]$ 上是高为 $2$ 的水平线段；$t>60$ 上是斜率为 $-\frac{1}{20}$ 的直线，在 $t=100$ 处过 $v=0$，到 $t=140$ 时 $v=5-7=-2$。
  2. 位置等于速度的积分，按分段拆开：
     $$s(140)=\int_{0}^{140}v(t)\,dt=\int_{0}^{40}\frac{t}{20}dt+\int_{40}^{60}2\,dt+\int_{60}^{140}\left(5-\frac{t}{20}\right)dt$$
  3. 逐段用几何面积（梯形/三角形）：
     $$\int_{0}^{40}\frac{t}{20}dt=\frac{1}{2}\cdot40\cdot2=40,\qquad \int_{40}^{60}2\,dt=2\cdot20=40$$
     $$\int_{60}^{100}\left(5-\frac{t}{20}\right)dt=\frac{1}{2}\cdot40\cdot2=40,\qquad \int_{100}^{140}\left(5-\frac{t}{20}\right)dt=-\frac{1}{2}\cdot40\cdot2=-40$$
  4. 合计：
     $$s(140)=40+40+40-40=80\ \text{m}$$

* **中文详解:** 这道题把"定积分 = 有向面积"用到底。前三段（$0\to40$ 的加速段、$40\to60$ 的匀速段、$60\to100$ 的减速到静止）面积都为正，共 $120$；$100\to140$ 物体反向运动，速度为负，面积记为 $-40$。所以 $t=140$ 时**位置**是 $80$ m，而**路程**是 $120+40=160$ m——这正是"位移"与"路程"的区别：$\int v\,dt$ 算位移，$\int|v|\,dt$ 才算路程。分段积分时一定要在速度变号处（$t=100$）断开，否则几何面积的正负会算错。
