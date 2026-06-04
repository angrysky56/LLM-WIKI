---
title: "Discovering Novel LLM Experts via Task-Capability Coevolution"
source: "https://arxiv.org/html/2604.14969v1"
author:
published:
created: 2026-06-04
description:
tags:
  - "clippings"
---
Andrew Dai Boris Meinardus <sup>1</sup>  Ciaran Regan Yingtao Tian Yujin Tang  
Sakana AI Equal contribution. Correspondence: adai\[at\]tcd.ie, boris.meinardus00\[at\]gmail.com

###### Abstract

Frontier model developers aim to train models continually to possess emergent, diverse capabilities. To extend capabilities, the current pre-training and post-training paradigm requires manually starting training runs with static datasets or reward functions every time. Addressing this limitation, our work pursues the insight that open-endedness (via the coevolution of models and tasks) can discover models with increasingly novel skills in a single run. We introduce a new model development framework that extends coevolution to large language model (LLM) discovery, open-ended Assessment Coevolving with Diverse Capabilities (AC/DC). AC/DC evolves both LLMs via model merging and natural language tasks via synthetic data generation. AC/DC discovers growing archives of LLMs that surpass the capabilities of larger LLMs while taking up less GPU memory. In particular, our LLM populations achieve a broader Coverage of expertise than other curated models or baselines on downstream benchmarks, without any explicit benchmark optimization. Furthermore, AC/DC improves Coverage over time, continually innovates on tasks and models, and improves performance in multi-agent best-of-N selection. Our findings highlight the potential of coevolution as a means of discovering broader sets of capabilities from base LLMs. Overall, AC/DC brings us one step closer to a profoundly new paradigm of LLM development, where continual improvements to the diversity of model capabilities can be accelerated by leveraging existing models as stepping stones to increasingly powerful models. Project page and code: [acdc-llm.github.io](https://acdc-llm.github.io/).

## 1 Introduction

LLMs and foundation models [^17] [^11] [^65] underpin key advances in AI for open-ended discovery and innovation [^102] [^75] [^153] [^90]. Such innovation capacity in future AI systems, innate to human civilization, would not only have profound implications for automated scientific discovery, but would also accelerate AI research itself. How do we get closer to LLMs as engines of knowledge accumulation and serendipitous discovery, with the ability to stumble upon greatness [^124] and drive paradigm shifts (e.g., the Transformer [^133])? Additionally, how do we imbue LLMs with innovation capacity and broader capabilities, given the prohibitively expensive costs and inaccessibility of running bigger and bigger models [^107] or obtaining more data [^101], especially for typical ML researchers?

While excitement grows around LLMs for scientific discovery [^115] [^104], the current paradigm of LLM development struggles to keep up with the accumulation of knowledge on learnable or discovered data. Developers must continually adapt to incremental improvements in static datasets [^5] [^66], environments [^60] [^73] [^104], learning algorithms [^117] [^87], and architectures [^147] [^100], to push the boundaries of frontier models. Continually training on synthetic data [^141] [^145] [^92] [^49] and broad-domain reward signals [^156] brings us closer to self-improving LLMs. Still, only one model is produced at a time. Trusting a single big static model to solve all real-world problems would therefore be challenging, due to concerns about fractured entangled representations [^71] and costs [^81].

![Refer to caption](https://arxiv.org/html/2604.14969v1/x1.png)

Figure 1: Method Overview. AC/DC coevolves an increasing set of diverse LLMs alongside an increasingly diverse and complex set of tasks, measuring the discovered models’ capabilities. Our discovered collective of models (across different model families tested) covers more skills than baselines across a wide range of benchmarks. Moreover, AC/DC discovers improved single model performance (as seen by MMLU 50 performance) and demonstrates improvement over time (shown as an average of MMLU and MMLU Pro 142 accuracy).

In contrast to individual models, collective intelligence (CI) (exemplified by human civilization) is capable of endlessly achieving feats far greater than any single human could [^97]. CI has even inspired new paradigms in AI [^47] and multi-agent LLM systems [^82] [^59], making them more robust during test-time scaling. By discovering whole collectives of small and accessible LLMs with diverse capabilities, we can overcome the limitations and weaknesses of any single trained model or the need to train different models separately.

To overcome the challenge of CI discovery, open-endedness (OE) is an emerging paradigm aiming for never-ending discovery via open-ended algorithms [^123]. Pursuing such AI-generating algorithms [^24], open-ended coevolution takes inspiration from the creativity explosion of natural evolution and human innovation, and pursues ever-changing learning environments for populations of increasingly intelligent agents to gain diverse capabilities [^136] [^30]. Leveraging recent advances in OE through LLMs [^35] [^3] [^103], we introduce a new framework to discover a whole population of expert LLMs through open-ended Assessment Coevolving with (/w) Diverse Capabilities (AC/DC). AC/DC combines evolutionary model merging [^4] and synthetic data generation [^91] to enable LLM populations to continually adapt to novel challenges that are generated, while satisfying minimal criteria for model and task quality [^14], all without explicit benchmark optimization [^78].

Following coevolution via AC/DC, we discovered a broad array of LLMs with diverse expertise and response styles that solve synthetic tasks spanning engineering, the sciences, and creative writing. When we selected a fixed-size subset of LLMs that make up the broadest skill Coverage on synthetic tasks, and then evaluated them on various LLM benchmarks that are out-of-distribution (OOD) to synthetic tasks at test time, we found that our population of smaller evolved LLMs (with a combined lower LLM parameter count than compared baseline models) was able to solve and cover more benchmark tasks than bigger LLMs of the same model family, as well as the initial seed LLM population. Our results also suggest that our LLM collectives surpass or reach GPT-4o [^56] levels of knowledge covered with a significantly lower proportion of collective model parameters. Furthermore, a single evolved model achieved better MMLU [^51] performance than the best starting seed model (cf. Fig. 1), more iterations of coevolution led to continually improved model population performance at test time, and cooperative final answer (Best-of-N) selection was more often successful with our LLM collectives than with baselines.

In short, our main contributions are (1) the AC/DC method applying coevolution to a novel joint LLM-and-synthetic-data discovery framework, (2) a demonstration of autonomous discovery of diverse LLM experts solving OOD tasks more broadly than baseline methods (some directly optimizing for benchmarks) and off-the-shelf models, and (3) evidence of a path to open-ended improvement of LLMs without explicit benchmark optimization, through an analysis of AC/DC.

## 2 Background and Preliminaries

This section introduces key concepts central to AC/DC: model merging operations that enable evolutionary discovery of LLM populations, Coverage metrics that quantify collective capabilities, and quality-diversity (QD) principles that guide our coevolutionary process.

Evolutionary Model Merging. Model merging combines multiple existing LLMs to produce new models with lower resource requirements than training from scratch [^144] [^58]. [^4] introduced evolutionary model merge (EvoMerge), which automates the merging process through evolutionary optimization using CMA-ES [^48]. Building on this foundation, we employ two key evolutionary operations:

Crossover: We sample two parent LLMs randomly and merge them using weighted linear interpolation of their task vectors, as done in CycleQD (CQD) [^72]. The task vector $\tau_{pi}=\theta_{parent_{i}}-\theta_{base}$ represents the difference between parent LLM $i$ and a base LLM (see Appendix App. M for more details).

Mutation: We generalize existing mutation operations by applying noise to the singular values of weight matrices in merged LLMs. For each weight matrix $W$, we compute its singular value decomposition $W=U\Sigma V^{T}$ and apply perturbations to the first $k$ singular values in $\Sigma$ before reconstruction, loosely inspired by [^126]. This approach modifies the representational structure while preserving the overall weight matrix geometry (see Appendix App. M for more details).

Coverage Metric. Coverage measures the collective problem-solving capacity of LLM populations. Given $Q$ total number of questions and $N$ number of LLMs, Coverage is:

$$
\text{Coverage}=\frac{1}{Q}\sum_{q=1}^{Q}\Bigg(\bigvee_{i=1}^{N}(x_{q,i}=y_{q})\Bigg)
$$

where $x_{q,i}$ is the output of LLM $i$ for question $q$, $y_{q}$ is the ground truth answer for question $q$, and $\bigvee_{i=1}^{N}$ denotes the logical OR operation over all $N$ LLMs. Coverage quantifies whether at least one LLM in the population solves each problem, capturing the collective intelligence potential of diverse LLM ensembles. Unlike individual LLM accuracy, Coverage emphasizes complementary capabilities that emerge from LLM diversity.

Skill Vectors. We represent LLM capabilities through binary skill vectors, where each indexed element indicates task completion status. They serve as behavioral signatures that enable direct comparison of LLMs without predefining niches (as in MAP-Elites [^99]). The distance between skill vectors informs the diversity of complementary LLM capabilities.

Quality-Diversity (QD). QD generates collections of diverse, high-quality solutions [^112] [^79], unlike traditional optimization, which seeks a single optimal solution. For model selection, we apply Dominated Novelty Search (DNS) [^7], a recent QD algorithm particularly suited to skill vector representations (similar to [^96]). DNS computes local competition fitness $\tilde{f}_{i}$ by measuring each solution’s distance from better-performing solutions in the descriptor space. For solution $i$, $\tilde{f}_{i}$ is computed as:

$$
\tilde{f}_{i}=\begin{cases}\frac{1}{k}\sum_{j\in\mathcal{K}_{i}}d_{i,j}&\text{if }|\mathcal{D}_{i}|>0\\
+\infty&\text{otherwise}\end{cases}
$$

where $\mathcal{D}_{i}$ contains solutions fitter than solution $i$, $\mathcal{K}_{i}$ contains indices of $k$ solutions in $\mathcal{D}_{i}$ with smallest distances $d_{i,j}$ between solutions $i$ and $j$. Local competition encourages diversity by rewarding solutions that are distant from higher-performing neighbors in the behavioral space.

Open-Ended Coevolution. [^14] [^15] demonstrate that defining minimal criteria (MC) for both agents and environments enables more open-ended outcomes in coevolution, filtering out undesired outcomes while enabling exploration to flourish. AC/DC coevolves populations of LLMs and synthetic tasks, where models must satisfy quality thresholds while maximizing quality and behavioral diversity through their skill vector representations. This creates a dynamic environment where increasingly sophisticated capabilities can emerge through the interplay between model evolution and task complexity. Related work discussion in App. G highlights AC/DC as a novel system combining concepts from various fields.

## 3 AC/DC: Assessment Coevolving with Diverse Capabilities

![Refer to caption](https://arxiv.org/html/2604.14969v1/x2.png)

Figure 2: Algorithm Overview. AC/DC continuously coevolves a model (LLM) archive and a synthetic task archive. LLMs are evolved using model merging crossover, and weight noising as a mutation operation. Tasks are evolved using a large scientist LLM that transforms existing task descriptions to generate increasingly novel and complex tasks. Models are evaluated on this data. We then compute a skill vector (i.e., signature of quality and diversity) for each model and a pass rate for each task. Based on those, we first apply minimal criterion (MC) filters (gibberish LLM filter, impossible task filter) and then select the models and tasks to update the archives, respectively.

We describe an open-ended algorithm for automatically discovering diverse LLMs that can collectively cover a wide range of skills. AC/DC coevolves two archives: an LLM archive $\mathcal{A}_{M}$ selected via DNS on skill vectors, and a synthetic active task archive $\mathcal{A}_{Q}$ containing an increasingly complex and novel set of challenges that the LLM archive must solve. We illustrate the algorithm in Fig. 2 and provide the pseudocode below (Algorithm 1). Inspired by [^14], we highlight minimal criteria (MC) for both LLMs and tasks. For further details, see Appendix App. N.

Algorithm 1 AC/DC: Assessment Coevolving with Diverse Capabilities

Initialize: Model archive $\mathcal{A}_{M}\leftarrow$ seed and init models, Task archive $\mathcal{A}_{Q}\leftarrow$ seed and init tasks

for $g=1$ to $G$ do $\triangleright$ Model Evolution Phase

   $P\leftarrow$ SelectParents($\mathcal{A}_{M}$) $\triangleright$ Select $P$ parents

   $O\leftarrow$ CrossoverMutate($P$, $N$) $\triangleright$ Generate $N$ offspring

   $E\leftarrow$ Evaluate($O$, $\mathcal{A}_{Q}$) $\triangleright$ Evaluate skill vectors, get responses to tasks; Section F.2

   $T\leftarrow$ GibberishFilter($E$) $\triangleright$ Trim away/discard degenerate models; Section F.5

   $\mathcal{A}_{M}\leftarrow$ DNSUpdate($\mathcal{A}_{M}$, $T$) $\triangleright$ Select top $M$ models; Section A.3.1

  if $g\bmod G_{task}=0$ then $\triangleright$ Task Evolution Phase

    $Q\leftarrow$ GenerateTasks(scientist LLM) $\triangleright$ Generate $N_{gen}$ tasks; Section F.1

    $Q_{nov}\leftarrow$ NoveltyFilter($Q$) $\triangleright$ Remove similar tasks; Section F.4

    $Q_{valid}\leftarrow$ ValidateTasks($Q_{nov}$) $\triangleright$ Reflection & validation; Section F.1

    $\mathcal{A}_{Q},\mathcal{A}_{Q_{g}}\leftarrow$ UpdateTaskArchive($\mathcal{A}_{Q}$, $\mathcal{A}_{Q_{g}}$, $Q_{valid}$) $\triangleright$ $\mathcal{A}_{Q_{g}}$ is global task archive

   ReevaluateArchive($\mathcal{A}_{M}$, $Q_{valid}$) $\triangleright$ Update skill vectors with new task pool

  end if

  SaveArchives($\mathcal{A}_{M}$, $\mathcal{A}_{Q}$, $g$)

end for

return SelectTaskForce($\mathcal{A}_{M}$, $\mathcal{A}_{Q_{g}}$) $\triangleright$ Select $N_{tf}$ diverse models

Model Archive Evolution. Evolution begins with at least three seed LLMs, representing fine-tuned versions of the same base architecture. We maintain $M$ active LLMs, i.e., LLMs considered as parents for the next generation (as in DNS). We also save a historical archive of LLMs every $G_{task}$ generations (before task adaptation), as candidates for a future task force. Given the existing parent population in $M$, we apply crossover and mutation operators as described in Sec. 2, producing $N$ offspring and yielding $M+N$ candidates for evaluation (Lines 3-4). Each candidate LLM is evaluated on our synthetic task archive and assigned skill vectors (Line 5). We apply a novel MC filter called the ”gibberish filter” to eliminate degenerate models by sampling outputs from the LLM for three random tasks each and employing a judge LLM to assess text coherence (Line 6). For the remaining models, we employ DNS to compute adjusted local competition scores $\tilde{f}$ (cf. Section A.3.1). We retain the highest-fitness model and select the remaining $P-1$ models with top $\tilde{f}$ scores such that we have at most $M$ active models (Line 7).

Task Archive Evolution. Alongside LLM agents, we coevolve an increasingly challenging and diverse set of tasks. We employ a large scientist LLM to synthesize tasks in line with [^94] (but simplified), where each task comprises a question-answer pair with an accompanying scoring function defined in Python (Line 9; Section F.1). We extend [^91] with a code extraction tool that enables robust evaluation of tasks requiring code generation, allowing the scientist LLM to programmatically parse and execute subject model responses. We maintain at most $Q_{max}$ active tasks per generation that are used to evaluate the current generation of models, alongside a global task archive updated every $G_{task}$ generations. We employ two vector databases for efficient similarity search: one for active tasks (newest) and another for the global archive.

Task evolution begins with $N_{seed}$ manually curated seed tasks (cf. Section E.3) and generates $N_{init}$ initial tasks through our evolution pipeline (Lines 9-13): (1) Task Proposal Phase samples a parent task and three random tasks from the active task database. Based on the parent task’s difficulty profile—determined by average pass rates across the current model population—we classify adaptation requirements as: increase difficulty, decrease difficulty, or generate a novel variant. The scientist LLM receives the parent task, three random reference tasks, and an adaptation type to generate a candidate task. (2) Novelty Filtering retrieves the three most similar tasks from the global archive using cosine similarity in embedding space. A judge LLM then determines whether the proposed task introduces sufficient novelty relative to existing tasks. (3) Reflection and Validation applies iterative refinement through self-evaluation cycles where the scientist LLM first attempts to solve its own generated task, and we execute the scoring function to identify implementation issues. Compilation errors trigger automatic correction with error feedback, while logic-based errors prompt task refinement. (4) Quality Assurance and MC implements additional filtering to remove impossible tasks that no LLM was able to solve, replacing them with their parent tasks. Accepted tasks are added to both the global archive and the active tasks. See Section E.4 for generated example tasks.

Model Selection for Downstream Evaluation. After coevolution over multiple generations, we select $N_{tf}$ models (from the historical archive) for our task force that maximize the number of correctly solved tasks across our synthetic task distribution $\mathcal{A}_{Q_{g}}$ (Line 17) (see Section D.2 for experiments with different selection strategies). This selection process operates independently of downstream benchmarks, avoiding optimization pressure and maintaining model generalization for OOD domains.

## 4 Quantitative Results

We compare our task force Coverage (Eq. 1) against several baseline approaches. We evaluate on a diverse set of benchmarks covering general knowledge, math, STEM, and code (see Section A.4.1 for details). See Section A.2 for model specifications and Section A.1 for hyperparameters.

Baselines Setup. We compare against four baselines: (1) Experts (N=3): Hand-selected instruct models (code, math, general) prompted once each with temperature 0 (for a discussion on N=8 experts, see Section D.4). (2) Control (N=3/N=8): The general instruct model prompted 3 or 8 times with temperature 0.7. (3) Big Model: A single large instruct model prompted once with temperature 0. (4) GPT-4o: Prompted once as the Big Model.

Best-of-N Selection Setup. Next to Coverage, we also evaluate Best-of-N (BoN) single-answer selection from multiple candidates using standard benchmark versions, testing whether Coverage improvements translate to practical deployment scenarios. We implement three techniques for the three benchmark types (MCQ, math, code). For further details, see Section A.4.

Table 1: AC/DC (ours) Coverage improvement across different models. Results show average performance improvement across all benchmarks for N=3 and N=8 configurations over the respective baseline. Gains are significant in most individual and aggregated (cf. App. K).

<table><tbody><tr><td rowspan="2">Base Model</td><td>vs Experts</td><td colspan="2">vs Control (%)</td><td colspan="2">vs Big Model (%)</td><td colspan="2">vs GPT-4o (%)</td></tr><tr><td>N=3 (%)</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td></tr><tr><td>Qwen2 7B</td><td>+2.06</td><td>-0.45</td><td>-1.04</td><td>+0.69</td><td>+8.83</td><td>-6.08</td><td>+2.05</td></tr><tr><td>Qwen2.5 7B</td><td>+4.40</td><td>+0.40</td><td>+0.61</td><td>+3.85</td><td>+9.78</td><td>+1.02</td><td>+6.95</td></tr><tr><td>Qwen3 14B</td><td>-0.21</td><td>+0.49</td><td>+1.54</td><td>+4.22</td><td>+9.48</td><td>+5.45</td><td>+10.71</td></tr><tr><td>DeepSeek V1 7B</td><td>+9.69</td><td>+9.35</td><td>+7.04</td><td>+1.96</td><td>+12.69</td><td>-18.46</td><td>-7.72</td></tr><tr><td>Average</td><td>+3.99</td><td>+2.45</td><td>+2.04</td><td>+2.68</td><td>+10.19</td><td>-4.52</td><td>+2.99</td></tr></tbody></table>

Coverage. Tab. 1 presents Coverage results across four base model families (see Section B.1 for details), revealing important patterns in AC/DC’s performance across different architectures and scales. AC/DC works on mulitple model families, achieving positive improvements on average across all model families and configurations (+2.04% to +10.19% across comparisons). Qwen 2.5 and DeepSeek numbers show consistent improvements across expert and control baselines, indicating effective discovery of complementary capabilities. Qwen3 14B exhibits scaling-dependent behavior where N=3 configurations underperform expert baselines but demonstrate improvement over the control baselines. Qwen2 demonstrates strong improvement over the three experts, but slightly lower coverage against control. Still, in Fig. 1, Qwen2 coverage increase over time for N=8.

AC/DC also achieves substantial parameter efficiency—for example, Qwen2.5 7B achieves 3.85% improvement over a 72B model using only 29% of the parameters at N=3, growing to 9.78% improvement at N=8, suggesting that distributed specialization benefits compound with scale. Our results show that AC/DC successfully discovers complementary capabilities that extend beyond what can be achieved through either manual expert selection or parameter scaling.

Finally, comparing our task force to GPT-4o, we demonstrate that our N=8 collective of models achieves broader Coverage. This is especially interesting considering that our task forces require very little compute to merge and then serve them in consideration of the potential costs of GPT-4o. Moreover, at N=3, our Qwen 2.5 task force of 3 7B models outperforms GPT-4o. This finding suggests that a collective of smaller, diverse, and capable models possesses the knowledge of a single frontier model, which can be leveraged given advances in BoN section methods.

Table 2: AC/DC (ours) Best-of-N improvement across different models. Results show average performance improvement across all benchmarks for N=3 and N=8 configurations over the respective baseline. Gains are significant in several individual and aggregated cases (cf. App. K).

<table><tbody><tr><td rowspan="2">Base Model</td><td>vs Experts</td><td colspan="2">vs Control (%)</td><td colspan="2">vs Big Model (%)</td><td colspan="2">vs GPT-4o (%)</td></tr><tr><td>N=3 (%)</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td></tr><tr><td>Qwen2 7B</td><td>-1.31</td><td>+2.33</td><td>+0.34</td><td>-6.32</td><td>-2.19</td><td>-12.97</td><td>-8.84</td></tr><tr><td>Qwen2.5 7B</td><td>-1.26</td><td>+0.27</td><td>-0.83</td><td>-3.22</td><td>-1.11</td><td>-6.32</td><td>-4.21</td></tr><tr><td>Qwen3 14B</td><td>-0.49</td><td>+0.29</td><td>+0.50</td><td>-0.78</td><td>+1.37</td><td>-3.17</td><td>-1.02</td></tr><tr><td>DeepSeek V1 7B</td><td>+11.73</td><td>+4.49</td><td>+7.92</td><td>-1.27</td><td>+4.94</td><td>-20.83</td><td>-14.62</td></tr><tr><td>Average</td><td>+1.34</td><td>+0.99</td><td>+1.05</td><td>-3.89</td><td>-0.25</td><td>-10.82</td><td>-7.17</td></tr></tbody></table>

Best-of-N (BoN). Tab. 2 presents BoN selection results across four base model families (see Section B.2 for details), revealing how Coverage improvements can translate into practical single-answer scenarios. AC/DC maintains strong performance when restricted to best-of-N, achieving positive improvements on average across representative comparisons (+0.99% to +1.34% vs control and experts). Most base model groups show positive improvements over control baselines, with particularly strong performance from Qwen2 7B, and DeepSeek V1 7B. Compared against the 3 expert baselines, the DeepSeek task force demonstrates exceptional improvements, whereas on the Qwen-based model families, we observe room for improvement.

Most notably, AC/DC sometimes achieves improved parameter efficiency against big models. For example, DeepSeek 7B reaches within 1.27% of the 67B model’s performance using only 17% of the parameters at N=3, and surpasses it by 4.94% at N=8 while using 16% fewer parameters.

Comparing against GPT-4o, we observe that our 8 Qwen2.5 7B and Qwen3 14B models come close to GPT-4o’s performance, indicating that with improved BoN methods, the collective of smaller models is within reach of outperforming the significantly larger proprietary model.

These results suggest that AC/DC can narrow the gap between single big models and multiple small models, even in rudimentary Best-of-N response setups. AC/DC can also scale up to larger collectives. Closing the gap remains a general challenge for future research focused on Best-of-N as a whole (as acknowledged in Sec. 6), but can leverage complementary gains via AC/DC.

Ablations. We examine the contribution of individual algorithmic components by systematically removing each from AC/DC’s evolutionary process (detailed results in Section D.1). The ablation reveals that QD selection (via DNS) and the gibberish filter are the most critical components, with their removal causing the largest absolute performance drops (2.39% and 2.46% at N=3, 0.88% and 1.18% at N=8, respectively). Removing individual components like mutation or novelty filtering causes modest decreases ranging from 0.50%-1.16% at N=3 and 0.37%-1.19% at N=8.

Most importantly, removing all evolutionary components simultaneously causes substantial performance degradation (2.36% drop at N=3, 7.02% drop at N=8). Overall, AC/DC is more often significantly better if none of these components are removed (cf. App. K). Performance drop is severe when all the components are removed, especially for larger task forces. In Section D.6, we demonstrate that including coevolution improves performance over model evolution on a static synthetic dataset (by 3.62% for N=8). In Section D.7, we demonstrate the effect of seed task selection, and in Section D.8, the effect of changing the scientist model.

Table 3: AC/DC (ours) outperforms prior QD methods. Avg. Coverage across benchmarks.

| Configuration | N=3 | N=8 |
| --- | --- | --- |
| AC/DC (ours) | 60.82 | 69.00 |
| DNS | 60.18 | 66.48 |
| CQD | 59.85 | 65.42 |

Finally, Tab. 3 compares AC/DC to prior QD methods (DNS, CQD) that optimize for benchmark-specific datasets (see Section D.5 for implementation details and extended tables). In contrast, AC/DC does not optimize for any benchmark and achieves the highest benchmark Coverage at N=8 models, demonstrating that AC/DC discovers more diverse and capable LLMs. Concurrently, DNS improves on Coverage over CQD, justifying its usage in AC/DC.

## 5 Qualitative Case Study

### 5.1 Emergent Specialization of Merged Models

Fig. 3 illustrates how our eight discovered models develop distinct performance profiles, with each model excelling in specific categories while performing differently across others, enabling them to function as complementary components of a collective intelligence. This specialization creates valuable Coverage patterns where models contribute unique capabilities to the ensemble. For instance, Model 4 may not achieve the highest overall accuracy, but it provides correct answers to chemistry questions that no other model in the population can solve.

![Refer to caption](https://arxiv.org/html/2604.14969v1/x3.png)

Refer to caption

### 5.2 Response Examples and Diversity from Merged Models

![Refer to caption](https://arxiv.org/html/2604.14969v1/x4.png)

Figure 4: Merged models unlock new capabilities. Higher Coverage means that our models solve tasks that baselines didn’t. These examples show a sample from MMLU, GSM8K, and GPQA, respectively, where none of the baseline models (math expert, code expert, reprompting the instruct model 8x, and the 72B model) solved the task, whereas at least one of our models did.

Merged Models vs. Baselines on Benchmark Tasks. AC/DC demonstrates superior Coverage by solving tasks that baseline methods cannot address. Fig. 4 presents examples where none of the baseline models—including math experts, code experts, repeated instruct model sampling, and the 72B model—successfully solve the task, while at least one of our discovered models provides the correct solution.

The MMLU example (left) illustrates multiple advantages of AC/DC beyond correctness. While baseline models fail to identify the correct answer, the 72B model additionally demonstrates poor response formatting, incorrectly placing square brackets around the main reasoning rather than the step headers. Our model not only provides the correct answer but also delivers concise, well-formatted reasoning that adheres to the expected structure.

The GSM8K arithmetic example (middle) showcases improved mathematical reasoning capabilities that likely emerge from our model merging process. By combining the potentially overfitted math expert with the general instruct model, AC/DC appears to broaden narrow mathematical skills to handle a wider range of instruction formats, resulting in more robust problem-solving abilities.

The GPQA physics example (right) reveals an important advantage related to output length constraints. During evaluation, responses exceeding the 1024-token limit often result in incorrect assessments, and most baseline responses violate this constraint. AC/DC implements a 512-token maximum during training, creating selection pressure for models that produce concise answers. Qualitative analysis suggests our discovered models find solutions using fewer tokens, leading to higher accuracy within the evaluation framework’s constraints. This demonstrates how evolutionary pressure can optimize for practical deployment considerations beyond raw capability.

![Refer to caption](https://arxiv.org/html/2604.14969v1/x5.png)

Figure 5: Models in our Task Force give diverse answers. Two examples of synthetic tasks generated by AC/DC and the answers of 3 models in our Task Force. In the left example, we can see how all three models give different analogies. Moreover, Model 1 structures the analogy in a Python function. For the right example, we can see that our models provide 3 different implementations of the same optimal algorithm.

Merged Model Response Diversity on Synthetic Tasks. Building on the quantitative capability distribution demonstrated in Section 5.1, we examine qualitatively whether our models generate diverse responses by analyzing their outputs on two synthetic tasks (Fig. 5).

The creative writing task (left) requires both analogical reasoning and computer science knowledge, revealing distinct approaches across our three models. Each model proposes a completely different analogy—library navigation, urban directions, and maze solving—demonstrating genuine diversity in conceptual frameworks rather than superficial variations. Notably, one model presents its analogy as a Python function, likely reflecting its ancestry from a code expert model and illustrating how evolutionary merging preserves specialized formatting preferences even in non-coding contexts (for more details on model evolution analysis, see Section E.2).

The algorithm implementation task (right) shows diversity in coding style and approach while maintaining algorithmic correctness. These variations demonstrate that AC/DC produces models with different coding philosophies and defensive programming practices, suggesting genuine stylistic diversity beyond mere surface-level differences.

This qualitative analysis confirms that our discovered models exhibit meaningful diversity in both creative reasoning and technical implementation, supporting the quantitative evidence of broad capability distributions and validating that AC/DC generates truly complementary rather than redundant model behaviors. More qualitative analyses on coevolution are in App. E.

Additionally, in Appendix App. I, we demonstrate quantitative and qualitative analysis comparing the three expert seed models to discovered merged models, investigating how challenging our synthetic tasks are to the expert models compared to our merged models. We find that our merged models, on average and as individual models, perform better on our synthetic data, demonstrating further evidence for the complexity of our synthetic data and the capabilities emerging through AC/DC, potentially beyond those present in off-the-shelf models.

### 5.3 Quality and Diversity of Synthetic Tasks - A Human Study

To validate the quality and novelty of our synthetically generated tasks, we conducted a human study where three expert reviewers evaluated 47 synthetic tasks and 49 benchmark tasks across three dimensions: correctness, out-of-distribution (OOD) nature relative to standard benchmarks, and creativity. Full methodology and results details are provided in Appendix App. H.

Table 4: Human evaluation results for synthetic tasks. Values show mean $\pm$ standard error across all labels.

| Correctness | Out-of-Distribution | Creativity |
| --- | --- | --- |
| 97.8% $\pm$ 2.2% | 68.9% $\pm$ 6.9% | 37.8% $\pm$ 7.2% |

Results demonstrate that AC/DC generates high-quality tasks with strong novelty characteristics. The 97.8% correctness rate confirms that synthetic tasks are well-formed and solvable. Critically, nearly 70% were rated as out-of-distribution compared to established benchmarks, providing evidence that AC/DC successfully generates novel task types beyond existing evaluation datasets, supporting our claims for OOD training. Over one-third were rated as creative, indicating exploration of problem-solving approaches not commonly tested by standard benchmarks.

As a validation baseline, we also evaluated tasks from eight standard benchmarks. These showed substantially lower OOD (10.2%) and creativity (6.1%) ratings, with the few exceptions concentrated exclusively in complex graduate-level benchmarks (MMLU-Pro, GPQA). This pattern confirms that reviewers appropriately distinguished between novel synthetic tasks and established benchmark content. Statistical analysis reveals strong inter-rater agreement on objective metrics (correctness: $p=0.46$, OOD: $p=0.57$), demonstrating robust and reliable findings.

## 6 Conclusion, Limitations, and Future Work

This work introduces AC/DC, a framework for automatically discovering diverse LLM collectives through open-ended coevolution of models and synthetic tasks. AC/DC demonstrates that extending EvoMerge to a novel innovation-driven pipeline can create task forces that outperform both larger monolithic models (while using fewer parameters) and manually curated expert ensembles. AC/DC does not optimize for any downstream benchmark and achieves consistent improvements across multiple model families, with evolved populations showing a wider coverage of capabilities and emergent specializations that validate the discovery of complementary skills.

We highlight limitations with AC/DC that motivate further work. Firstly, successful merge outcomes can depend on empirically testing seed model combinations; for example, strongly fine-tuned models with divergent parameter spaces merges poorly, potentially limiting performance gains [^52] (e.g., see results with Llama3, App. C). The framework relies on a fixed scientist LLM for task generation, constraining exploration potential. AC/DC primarily discovers emergent skills through crossover rather than candidate models themselves acquiring new knowledge, bounded by the initial seed models’ capabilities, which could be addressed through mutation (e.g., our mutation operator). Finally, an inherited limitation from EvoMerge is that it requires seed models that are fine-tuned versions of the same base model.

Key future work directions include developing recursive self-improving scientist models using evolved model populations for task generation. Furthermore, as with all prior attempts towards unbounded open-endedness, extending runs well beyond an arbitrary limit on coevolution steps would enable investigation of longer-term open-ended dynamics and whether innovation rates remain stable over extended time horizons (as we observe promising signs of continual task and model innovations in Appendix Section D.3 and Section D.6). Moreover, similar to how a lot of research focuses on developing base LLMs suitable for subsequent post-training, research on the understanding of model merging compatibility of seed models is a relevant future research direction. We investigate potential ad-hoc predictors for the compatibility of seed models for evolutionary model merging in Appendix App. J, which can be an interesting starting point for future research. A complementary challenge to determining seed conditions for coevolution is determining the right minimal criteria to facilitate the discovery of ideal model behaviors that are non-trivial to obtain via loss or objective functions. We investigate another way in which the criteria settings we have set for AC/DC can lead to better performance in different evaluation settings, for example, under constrained response length limits (cf. Appendix Section D.9). Additionally, expanding scientist LLM tools (e.g., adding web search capabilities) for task generation would enhance the correctness and scope of novel tasks [^90]. Integrating model fine-tuning could enable more efficient knowledge acquisition beyond crossover-based discovery. Moreover, advanced merging techniques such as M2N2 [^1] could provide higher-degree-of-freedom model combinations. Finally, implementing model collaboration during training and test-time inference could enhance population-level performance. Nevertheless, independently developing more sophisticated multi-agent best-of-N extraction methods could be a valuable complementary research direction [^59] (cf. App. G, on multi-agent systems). Finally, the creativity of standalone LLMs remains a fundamental bottleneck that necessitates further innovations to AI model architectures or open-ended discovery pipelines that leverage AI models for search/exploration [^18] [^151] [^40].

In conclusion, AC/DC represents a paradigm shift from scaling individual models toward deliberately developing complementary agent collectives. We hint at possible new directions to further address the limitations of the norm, monolithic model development, by introducing a more open-ended model population discovery approach. This distributed specialization approach offers a path to parameter-efficient AI systems that achieve sophisticated capabilities without the computational costs of ever-larger monolithic (frontier) models (cf. App. L). By automatically discovering novel LLM experts and continually advancing a population of diversely capable LLMs, LLMs may one day embody the engine that drives both knowledge acquisition and transformative creativity, enabling discoveries that improve both its own inner workings, and the outer loop environment that it may transform and adapt to in tandem with humans and other AI systems. After all, natural evolution on Earth actively produces a rich phylogeny that has enabled lifeforms (e.g., trees, coral) that also serve as challenges and opportunities for others (e.g., giraffes, fish), a successful instance of open-ended coevolution since over a billion years ago. Or, through cultural (co)evolution, even leaps of serendipitous invention from the vacuum tube to the computer [^124] [^123]. With AC/DC, we demonstrate a first step towards this vision, bringing us closer to discovering collective AI that is as open-ended, complex, and creative as human civilization.

## Ethics statement

AC/DC focuses on automatically coevolving LLMs and synthetic tasks. As this work only encompasses the evaluation of models on synthetic and benchmark tasks without involving sensitive data, human subjects, or potential misuse applications, we identify no ethical concerns.

## Reproducibility statement

To ensure reproducibility of our results, we provide source code and configs, showing the details of the algorithm, run setup, seed tasks, and LLM prompts. All base models and evaluation benchmarks used in this work are publicly available.

#### Author Contributions

In the following, we list the contributions of the authors to the paper.

- Andrew Dai: Proposed the initial idea. Equal main contribution to the development of the AC/DC framework and conducted the experiments. Equal main contribution to the writing of the paper.
- Boris Meinardus: Equal main contribution to the development of the AC/DC framework and conducted the experiments. Equal main contribution to the writing of the paper.
- Ciaran Regan: Assisted with the experiments and contributed to the writing of the paper.
- Yingtao Tian: Advised on the project and the writing of the paper.
- Yujin Tang: Advised on the writing of the paper.

#### Acknowledgments

We thank the Sakana AI research team, in particular (in alphabetical order), Johannes Ackermann, Takuya Akiba, Sam Earle, Simon Guo, David Ha, Shengran Hu, Yuichi Inoue, Llion Jones, Akarsh Kumar, Robert Lange, Sebastian Risi, and Alex L. Zhang, for helpful discussions and feedback. We also thank Koshi Eguchi and Kou Misaki for providing technical support and maintenance during our experimental runs on our compute cluster.

## References
