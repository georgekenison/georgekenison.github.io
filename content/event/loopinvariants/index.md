---
title: "Loop Invariants and Algebraic Reasoning"
summary: "Workshop On Loop Invariants and Algebraic Reasoning"
date: 2025-07-07
showDate: true
layout: article
enableEmoji: true


# Blowfish utilizes a direct string for addresses
layoutBackgroundHeader: false

links:
  - icon: "github" # Replace with valid Blowfish icons like link, github, book, etc.
    name: "Conference Website"
    url: "https://conferences.au.dk/icalp2025"
  - icon: "link"
    name: "Workshop Registration"
    url: "https://conferences.au.dk/icalp2025/registration"

tags:
  - "Loops"
  - "Loop Invariants"
  - "Invariant Generation"
  - "Invariant Verification"
  - "Algebraic Methods"
  - "Workshop"

---

{{< zenmode-enabled >}}



## Aim

Reasoning about loops is a fundamental task in program analysis and verification. To this end, loop invariants are an indispensable tool. They help both to establish safety properties (e.g., proofs of non-reachability) and liveness properties (e.g., as supporting invariants in termination proofs). Beyer et al. [[VMCAI 2007]](https://link.springer.com/chapter/10.1007/978-3-540-69738-1_27) go so far as to call the problem of automatic invariant generation "the most important task in program verification."

There has been a resurgence of interest in computing the polynomial invariants for loops. In one direction, theoretical work has produced complete algorithms that will generate the invariant ideal for abstract classes of loops. In another direction, recent works have produced templates and heuristics aimed at generating some (but not necessarily all) the invariants of more general classes of loops with conditional branching, polynomial assignments, and probabilistic updates.

This workshop aims to span the divide between the aforementioned directions and bring together researchers from both communities.

------------------------------------------------------------------------

## Participation

To participate in-person, please register for the workshop through ICALP's [registration portal](https://conferences.au.dk/icalp2025/registration). To participate remotely over Zoom, please contact the organisers for further details.

------------------------------------------------------------------------

## Speakers, Talks, and Slides

*(Click on a talk title header to reveal the abstract and slides.)*

{{< accordion mode=open separated=true >}}
  {{< accordionItem title="Algebraic invariants of rational linear loops — Rida Ait El Manssour (Oxford)" >}} 
  Automatically generating loop invariants is essential for ensuring software correctness, yet it remains a challenging problem in general. In this talk, I will focus on a specific class of programs: branching-free loops with a single linear update. I will introduce a PSPACE algorithm that computes all algebraic relationships that consistently hold among program variables throughout the loop’s execution. Additionally, I will highlight how these results can be applied to verify proposed invariants, and discuss promising directions for extending this approach to loops with multiple linear updates.
  
  This is based on a project with George Kenison, Mahsa Shirmohammadi, and Anton Varonka.
  {{< /accordionItem >}}
  

  {{< accordionItem title="S-unit equations in modules — Ruiwen Dong (Magdalen College, Oxford)" >}}  
  Let $M$ be a finitely presented module over a Laurent polynomial ring $R$. We consider S-unit equations over $M$: these are equations of the form $x_1 m_1 + \cdots + x_K m_K = m_0$, where the coefficients $m_i$ are in $M$ and the variables $x_i$ range over the set of monomials of $R$. When the Laurent polynomial ring $R$ has the base ring $\mathbb{Z}$, (that is, $R = \mathbb{Z}[X_1^{\pm}, \ldots, X_N^{\pm}]$), we show that it is undecidable whether a given S-unit equation over a given module $M$ admits a solution. When $R$ has the base ring $\mathbb{Z}/T\mathbb{Z}$ for some integer $T > 1$, (that is, $R = (\mathbb{Z}/T\mathbb{Z})[X_1^{\pm}, \ldots, X_N^{\pm}]$), we show that the problem of deciding whether a given S-unit equation over a given module $M$ admits a solution is Turing equivalent to solving a system of linear-exponential Diophantine equations over $\mathbb{Z}$.

  This talk is based on a paper in SODA'25 as well as ongoing work with Doron Shafrir.
  {{< /accordionItem >}}
  
  {{< accordionItem title="Finite Rational Matrix Semigroups have at most Exponential Size — Roland Guttenberg (TUM)" >}}  Weighted Automata or equivalently semigroups of matrices are a model for while loops with linear updates. While it has been shown that the optimal polynomial invariants for matrix semigroups can be computed, the algorithms have prohibitively high complexity. In ongoing work together with Rida Ait El Manssour, Nathan Lhote, Mahsa Shirmohammadi and James Worrell we are attempting to tackle the complexity by giving algorithms for identifying and solving simple subcases.

  The first such simple but interesting subcase are finite semigroups. While it is known that if a group of n-by-n matrices is finite, then it has size at most 2^n n!, for semigroups the best known bound is double exponential. We reduce this bound to a single exponential and obtain a PSPACE algorithm for deciding finiteness of a given matrix semigroup. Our main tool, which is applicable for any matrix semigroup, is the PTIME computation of an irreducible component decomposition. This can be viewed as a kind of extension of the decomposition of a graph into strongly-connected components.

  [Slides: :page_facing_up:](/uploads/liar25/guttenberg-liar25.pdf)
  {{< /accordionItem >}} 
  
  {{< accordionItem title="Applications of O-Minimality to Linear Loops — Toghrul Karimov (MPI-SWS)" >}}
  The Termination Problem for linear while loops subsumes, among others, the famous Skolem Problem for linear recurrence sequences, and is consequently known to be decidable only in low dimensions (i.e. the number of program variables). We will discuss how o-minimality of real numbers equipped with arithmetic and exponentiation can be used to prove sweeping decidability results—that do not depend on the dimension—for certain robust variants of the classical decision problems of linear loops. This talk is largely based on the paper "Verification of Linear Dynamical Systems via O-Minimality of the Real Numbers."
  {{< /accordionItem >}}

  {{< accordionItem title="Minimizing Cost Register Automata over a Field — Nathan Lhote (Aix-Marseille University)" >}} 
  Weighted automata (WA) are an extension of finite automata that define functions from words to values in a given semiring. An alternative deterministic model, called Cost Register Automata (CRA), was introduced by Alur et al. It enriches deterministic finite automata with a finite number of registers, which store values, updated at each transition using the operations of the semiring. It is known that CRA with register updates defined by linear maps have the same expressiveness as WA. Previous works have studied the register minimization problem: given a function computable by a WA and an integer k, is it possible to realize it using a CRA with at most k registers? In this paper, we solve this problem for CRA over a field with linear register updates, using the notion of linear hull, an algebraic invariant of WA introduced recently by Bell and Smertnig. We then generalise the approach to solve a more challenging problem, that consists in minimizing simultaneously the number of states and that of registers. Last, while the linear hull was recently shown to be computable by Bell and Smertnig, no complexity bounds were given. To fill this gap, we provide two new algorithms to compute invariants of WA. This allows us to show that the register (resp. state-register) minimization problem can be solved in 2-ExpTime (resp. in NExpTime).


This is joint work with Yahia Idriss Benalioua and Pierre-Alain Reynier
  {{< /accordionItem >}}

  {{< accordionItem title="Algebraic tools for computing polynomial loop invariants — Fatemeh Mohammadi (KU Leuven)" >}}
  Loop invariants are properties of a loop program that hold before and after each iteration of the loop. They are often employed to verify programs and ensure that algorithms consistently produce correct results during execution. Consequently, the generation of invariants becomes a crucial task for loops. I specifically focus on polynomial loops, where both the loop conditions and assignments within the loop are expressed as polynomials. Although computing polynomial invariants for general loops is undecidable, efficient algorithms have been developed for certain classes of loops. For instance, when all assignments within a while loop involve linear polynomials, the loop becomes solvable. In this talk, I will discuss the more general case where the polynomials exhibit arbitrary degrees. Applying tools from algebraic geometry, I present two algorithms designed to generate all polynomial invariants for a while loop, up to a specified degree. These algorithms differ based on whether the initial values of the loop variables are given or treated as parameters. <br> <br> This talk is based on joint work with Erdenebayar Bayarmagnai and Rémi Prébet.

  [Slides: :page_facing_up:](/uploads/liar25/mohammadi-liar25.pdf)
  {{< /accordionItem >}}
  

  {{< accordionItem title="Algebraic Closure of Matrix Sets Recognized by 1-VASS — Mahsa Naraghi (Université Paris Cité)" >}}
  We prove that for a 1-VASS $\mathcal V$, with labels $\Sigma$ and morphism $f:\Sigma^* \to M_d(\mathbb Q)$, the Zariski closure of $f(L(\mathcal V))$ is computable. To this end, we adapt Imre Simon’s factorisation trees—originally defined for finite monoids—to the infinite monoid $M_d(\mathbb Q)$ by replacing idempotent elements with stable matrices. We show, through multilinear algebraic arguments, that every sequence of matrices in $M_d(\mathbb Q)$ can be realised as the yield of a factorisation tree of height bounded by an explicit function of $d$.

This work is in collaboration with Rida Ait El Manssour, Mahsa Shirmohammadi, and James Worrell.


  {{< /accordionItem >}}


  {{< accordionItem title="Modern algorithms for one block quantifier elimination over the reals — Mohab Safey El Din (Sorbonne Université, CNRS, LIP6)" >}}
  One block quantifier elimination algorithms take as input a formula which consists of a (universal or existential) quantifier on real variables arising in some input polynomial constraints. These algorithms compute a logically equivalent quantifier-free formula of polynomial constraints. This problem is known to be solvable since Tarski's original work on elementary algebra and geometry.

  Quantifier elimination arises frequently in problems related to algebraic reasoning From a geometric perspective, one-block quantifier elimination computes a description of the projection of the real solution set to polynomial constraints on some affine subspace.

  In this talk, I will describe a new one block quantifier algorithm which leverages this geometric perspective. This yields  new complexity results and practical performances which outperform the current state-of-the-art algorithms on a large family of examples.

  [Slides: :page_facing_up:](/uploads/liar25/safeyeldin-liar25.pdf)
  {{< /accordionItem >}}
  

  {{< accordionItem title="Polynomial Ideals and Order Ideals — Sylvain Schmitz (Université Paris Cité)" >}}
  There is a well-known connection between polynomial ideals and order ideals, which relates e.g. Hilbert's Basis Theorem and the ascending chain condition on polynomial ideals with Dickson's Lemma and the descending chain condition on order ideals.

  As an illustration of how this connection can be exploited to use complexity results on order ideals, I'll revisit the results of Benedikt, Duff, Sharad, and Worrell [LICS 2017] on the complexity of the zeroness problem for general and invertible polynomial automata, using recent results obtained with Schütze [ICALP 2024].  As a second illustration, I will point to some open questions regarding the complexity of computing Gröbner bases.
  
  
  [Slides: :page_facing_up:](/uploads/liar25/schmitz-liar25.pdf)
  {{< /accordionItem >}}


  {{< accordionItem title="Rational Loop Synthesis — Anton Varonka (TU Wien)" >}}
  Polynomial (equality) invariants have proven to be helpful in the inductive arguments about loop programs. The class of such invariants enjoys good closure properties and most importantly, allows for a finite representation of the set of all polynomial invariants for a given loop program. Therefore, a question of special theoretical interest concerns the decidability/complexity of finding this representation.
  
  Notably, small changes in the program model can render the problem of generating all polynomial invariants undecidable. We discuss the landscape and focus on the question “What polynomials can be invariants of simple enough loops?”. In this talk, we consider the model of simple linear loops, where the update of the rational variable vector is given by a single rational matrix. Loops like these are exactly the linear dynamical systems, as known in the linear recurrence sequences community. We further restrict ourselves to the loops that attain infinitely many different vectors.

  In order to understand the polynomial invariants of simple linear loops, we turn to the problem of loop synthesis from desired polynomial equalities. That is, we ask whether there exists a simple linear loop that has a given polynomial invariant. In this setting, synthesising a loop also means finding a vector of initial values---no surprise that loop synthesis is as hard as Hilbert's Tenth Problem over the rationals.

  Our results concern the decidability of existence and, in addition, the algorithmic generation of loops from invariants. We will discuss special classes of input polynomials: quadratic equations and conjunctions of pure binomial equalities. Finally, we will introduce a bit-bounded version of loop synthesis--where the objective is to find a simple linear loop with input entries of a bounded size.

  
  [Slides: :page_facing_up:](/uploads/liar25/varonka-liar25.pdf)
  {{< /accordionItem >}}
  
  
  {{< /accordion >}}

------------------------------------------------------------------------

## Schedule

(All times are CEST/UTC+02:00)

*08:30--09:00 Registration*

-   09:00--10:00 **Mohab Safey El Din** · Modern algorithms for one block quantifier elimination over the reals
-   10:00--10:30 **Fatemeh Mohammadi** · Algebraic tools for computing polynomial loop invariants

*10:30--11:00 Coffee Break*

-   11:00--11:30 **Rida Ait El Manssour** · Algebraic invariants of rational linear loops
-   11:30--12:00 **Mahsa Naraghi** · Algebraic Closure of Matrix Sets Recognized by 1-VASS
-   12:00--12:30 **Roland Guttenberg** · Finite Rational Matrix Semigroups have at most Exponential Size

*12:30--14:00 Lunch*

-   14:00--15:00 **Nathan Lhote** · Minimizing Cost Register Automata over a Field
-   15:00--15:30 **Sylvain Schmitz** · Polynomial Ideals and Order Ideals

*15:30--16:00 Coffee Break*

-   16:00--16:30 **Anton Varonka** · Rational Loop Synthesis
-   16:30--17:00 **Ruiwen Dong** · S-unit equations in modules
-   17:00--17:30 **Toghrul Karimov** · Applications of O-Minimality to Linear Loops

*Workshop Ends*

------------------------------------------------------------------------

## Organisers

-   [George Kenison](https://georgekenison.github.io/) (LJMU)
-   [Mahsa Shirmohammadi](https://www.irif.fr/~mahsa/) (CNRS, Paris)
