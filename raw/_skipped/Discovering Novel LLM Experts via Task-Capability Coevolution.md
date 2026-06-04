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

## Appendix Contents

## Appendix A Setup Details

### A.1 Training Hyperparameters

This section provides the hyperparameters used for all experiments unless otherwise specified.

Table 5: AC/DC hyperparameters.

<table><tbody><tr><td>Component</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="5">General</td><td>Number of generations</td><td>50</td></tr><tr><td>Active models per gen</td><td>16</td></tr><tr><td>New offspring per gen</td><td>8</td></tr><tr><td>Active tasks per gen</td><td>250</td></tr><tr><td>Hist. archive gen interval</td><td>5</td></tr><tr><td></td><td>Scientist Model</td><td>Qwen/Qwen2.5-72B-Instruct</td></tr><tr><td rowspan="2">Mutation</td><td>First k singular values</td><td>256</td></tr><tr><td>mutation rate</td><td>0.25</td></tr><tr><td>Crossover</td><td>standard deviation</td><td>0.5</td></tr><tr><td rowspan="3">Evaluation (synthetic tasks)</td><td>max tokens</td><td>512</td></tr><tr><td>temperature</td><td>0</td></tr><tr><td>top_p</td><td>1.0</td></tr><tr><td rowspan="3">Task Generator</td><td>Task difficulty threshold</td><td>0.5</td></tr><tr><td>Max reflections</td><td>3</td></tr><tr><td>Embedding Model</td><td>intfloat/e5-mistral-7b-instruct</td></tr><tr><td rowspan="7">t-SNE</td><td>n_components</td><td>2</td></tr><tr><td>perplexity</td><td>50</td></tr><tr><td>learning_rate</td><td>200</td></tr><tr><td>n_iter</td><td>3000</td></tr><tr><td>init</td><td>pca</td></tr><tr><td>random_state</td><td>42</td></tr><tr><td>early_exaggeration</td><td>6.0</td></tr><tr><td rowspan="5">HDBSCAN</td><td>min_cluster_size</td><td>16</td></tr><tr><td>min_samples</td><td>4</td></tr><tr><td>cluster_selection_epsilon</td><td>2</td></tr><tr><td>cluster_selection_method</td><td>eom</td></tr><tr><td>metric</td><td>euclidean</td></tr></tbody></table>

### A.2 Models Used

For our experiments with different model families, we use the following models from Hugging Face:  
  
Qwen2 7B [^148]

- Control: Qwen/Qwen2-7B-Instruct
- Experts:
	- Grogros/Qwen2-7B-OurSafecoder
	- Qwen/Qwen2-Math-7B-Instruct
	- Qwen/Qwen2-7B-Instruct
- Big Model: Qwen/Qwen2-72B-Instruct

Qwen2.5 7B [^113]

- Control: Qwen/Qwen2.5-7B-Instruct
- Experts:
	- prithivMLmods/Neumind-Math-7B-Instruct
	- pe-nlp/R1-Qwen2.5-7B-Instruct-code
	- Qwen/Qwen2.5-7B-Instruct
- Big Model: Qwen/Qwen2.5-72B-Instruct

Qwen3 14B [^147]

- Control: Qwen/Qwen3-14B
- Experts:
	- sunblaze-ucb/Qwen3-14B-Intuitor-MATH-1EPOCH
	- ertghiu256/qwen-3-14b-code-and-math-reasoning
	- Qwen/Qwen3-14B
- Big Model: Qwen/Qwen3-235B-A22B-Instruct-2507

DeepSeek V1 7B [^10]

- Control: deepseek-ai/deepseek-llm-7b-chat
- Experts:
	- deepseek-ai/deepseek-math-7b-instruct
	- deepseek-ai/deepseek-coder-7b-base-v1.5
	- deepseek-ai/deepseek-llm-7b-chat
- Big Model: deepseek-ai/deepseek-llm-67b-chat

Llama3 8B [^45]

- Control: meta-llama/Meta-Llama-3-8B-Instruct
- Experts:
	- MathGenie/MathCoder2-Llama-3-8B
	- rombodawg/Llama-3-8B-Instruct-Coder
	- meta-llama/Meta-Llama-3-8B-Instruct
- Big Model: meta-llama/Meta-Llama-3-70B-Instruct

### A.3 Algorithm Details

#### A.3.1 DNS Novelty Score Computation

The Dominated Novelty Score is a key component of our selection mechanism that balances quality and diversity in the model archive. For each model, we compute its novelty relative to models with higher fitness, encouraging retention of models that solve unique subsets of tasks. Algorithm 2 provides the detailed computation.

Algorithm 2 Dominated Novelty Score Computation for One Solution

Input: Solution $s$, Archive $\mathcal{A}$, Parameters $k$, $\alpha_{dom}$, $w$ (difficulty weights)

$\mathcal{F}\leftarrow\{s^{\prime}\in\mathcal{A}:\text{fitness}(s^{\prime})>\text{fitness}(s)\}$ $\triangleright$ Find fitter solutions

if $\mathcal{F}=\emptyset$ then

  return $\alpha_{dom}$ $\triangleright$ Maximum score if no fitter solutions exist

end if

 $\text{scores}\leftarrow[]$

for each $s^{\prime}\in\mathcal{F}$ do

   $v_{s}\leftarrow$ skill vector of $s$ $\triangleright$ Binary vector of task successes

   $v_{s^{\prime}}\leftarrow$ skill vector of $s^{\prime}$

  // Compute weighted unique skills: tasks solved by $s$ but not by $s^{\prime}$

   $\text{unique\_weighted}\leftarrow\sum_{i}w_{i}\cdot(v_{s}[i]\land\neg v_{s^{\prime}}[i])$

   $\text{total\_weighted}\leftarrow\sum_{i}w_{i}$ $\triangleright$ Sum of all difficulty weights

  // Normalize by total skill vector to measure contribution to coverage

   $\text{skill\_score}\leftarrow\frac{\text{unique\_weighted}}{\text{total\_weighted}}\times 100$    $\text{scores.append}(\text{skill\_score})$

end for

$\text{scores.sort}()$ $\triangleright$ Sort ascending

$k^{\prime}\leftarrow\min(k,|\text{scores}|)$ $\triangleright$ Use at most $k$ neighbors

return $\frac{1}{k^{\prime}}\sum_{i=1}^{k^{\prime}}\text{scores}[i]$ $\triangleright$ Mean of $k$ lowest scores

The algorithm identifies models that complement the existing archive by solving tasks that higher-fitness models fail on. A model receives a high novelty score when it uniquely solves many tasks that fitter models cannot solve. The skill score is computed as the ratio of weighted unique skills to the total weighted skill vector, measuring the model’s contribution to overall task coverage relative to fitter solutions. Key configuration parameters include:

- $\alpha_{dom}$ (default: 999): Maximum novelty score assigned when a model has no fitter competitors
- $k$ (default: 3): Number of nearest neighbors for novelty computation
- $w_{i}$: Difficulty weights for task $i$, computed as the fraction of current model population failing that task

When using difficulty weights, harder tasks (those failed by more models) contribute more to the novelty score, encouraging retention of models that solve challenging problems. This mechanism ensures diversity in the archive while maintaining a preference for higher overall fitness. This is also related to what metric [^1] used for diversity maintenance in M2N2. AC/DC directly leverages this as part of explicit distance measurements between model behaviors to support the use of QD algorithms in AC/DC.

### A.4 Experimental Setup Details

This section provides details to the experimental setup such as the benchmarks used and how we augment them (Section A.4.1) and details on our best-of-N single-answer-selection methods (Section A.4.3).

#### A.4.1 Benchmark Details

We evaluate on MMLU [^50], MMLU Pro [^142], GPQA [^114], BBH [^127], GSM8K [^25], Minerva MATH [^80], Humaneval [^21], and MBPP [^6].

We use Language Model Evaluation Harness (lm-evaluation-harness) from EleutherAI [^44] to evaluate on these benchmarks, with task names mmlu\_cot\_llama, mmlu\_pro\_llama, gpqa\_main\_cot\_zeroshot, bbh\_cot\_zeroshot, gsm8k\_llama, minerva\_math, humaneval\_instruct, and mbpp\_instruct respectively. We use the original evaluation config settings for these benchmarks from the repo with the last commit on September 21 (UTC-00).

Since multiple-choice question (MCQ) benchmarks are prone to ”cheating” when evaluating Coverage (randomly sampling each option once will lead to 100% accuracy), we design new, open-ended versions of these benchmarks, which we then refer to as MMLU judge, MMLU Pro judge, GPQA judge, and BBH judge. We design these judge-evaluated benchmarks such that we do not provide multiple-choice options in the questions, relying only on the absolute knowledge/capability of the subject model.

To generate these new datasets, we prompt an LLM to filter out all samples that are not possible to answer without the multiple choice options (e.g., questions in the form of "Which of the following \[...\]"). The remaining questions that are self-consistent are prompted to the subject model.

To evaluate the correctness of a subject’s answer, we prompt an LLM judge to determine whether the candidate solution is correct given the ground truth answer.

We provide the dataset filtering and LLM judge prompts in Section F.7.

For output generation, we set the output token length for the judge-evaluated benchmarks to 256 tokens. A shorter response assesses the capability of LLMs to return concise and direct answers within their first response statements, and forces them to rely on knowledge recall for these knowledge-based tasks instead of guessing through excessive reasoning. This also reduces the compute time for LLM judge calls. For the other four benchmarks, we set the output token length to 2048 tokens.

#### A.4.2 Baseline Details

Fundamentally, our proposal is to rethink model development, moving from developing one large, monolithic LLM, to a population based approach, automatically developing a collective of diverse smaller LLMs.

To evaluate the effectiveness of this approach, we target improving the Coverage over large scale open-source and even proprietary LLMs. Nevertheless, one may ask, whether our discovered collective is better than simply re-prompting the same sized general instruct model. This is our control baseline. Moreover, one might ask, if we start of with the three experts as seed models, we would want to achieve higher Coverage than those.

In Tab. 1, we observe that, compared to the big models, we achieve noticeable Coverage improvements, and even surpass or get close to the GPT-4o performance, demonstrating that our collective of smaller models fundamentally possess the capabilities of much larger models to answer the respective questions.

The Experts N=8 baseline emerged from the question of “What if we resample the three experts N times”. Although we argue that this approach of manually selecting experts is unscalable and it being even worse to tune the sampling distribution, it is an interesting comparison. To establish this baseline and ensure consistency across model families, we arbitrarily select the 3-3-2 (instruct-code-math), which was selected based on observations that the code models achieved higher scores on a wider rage of benchmarks than the math model, arguably, making the baseline stronger.

In addition to these “sanity check” baselines, in Tab. 3, we compare against prior quality-diversity work, demonstrating that AC/DC discovers a task force that achieves higher Coverage while not optimizing for any downstream benchmark (which the other methods actively do).

#### A.4.3 Best-of-N Single-Answer-Selection Methods

In this section, we elaborate on our single-answer-selection methods used in Sec. 4. For the two LLM-judge-based methods, we only provide the final subject model answers without the reasoning trace.

Divide and Conquer. For this method, we prompt a judge LLM to decide on the correct answer for two candidate solution. If the model deems both wrong, we ask it to provide the answer that is ”more correct”. We apply this process in a devide-and-conquer approach, first, grouping all candidate solutions into pairs, then selecting the ”winners”, and repeating this process until only one answers remains.

Monarchical LLM. We provide all $N$ answers to an LLM judge at once and prompt it to select the correct answer.

RM-based. We leverage a scalar reward model [^86] to score each full candidate submission and select the candidate with the highest score.

## Appendix B Detailed Quantitative Results

### B.1 Coverage Results

#### B.1.1 Results for All Models on All Benchmarks

Table 6: AC/DC (ours) Coverage performance comparison across different benchmarks and model configurations for all model families used (see Section A.2). Key findings are discussed in the next subsection in Section B.1.2.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. judge judge judge judge Qwen 2 Big Model 50.44 47.12 4.36 78.32 90.83 66.18 82.93 70.40 61.32 N = 3 Control 54.58 50.97 7.72 73.01 92.34 67.28 87.80 66.00 62.46 Experts 47.05 41.78 6.38 65.29 91.28 75.08 85.98 66.80 59.96 AC/DC 55.42 51.28 9.06 69.44 89.99 65.76 86.59 68.60 62.02 N = 8 Control 67.69 64.27 12.75 84.54 95.68 76.92 92.68 75.00 71.19 AC/DC 67.20 63.03 15.44 82.03 94.77 75.32 89.02 74.40 70.15 Qwen 2.5 Big Model 49.30 47.00 0.00 82.30 91.70 81.96 89.63 80.20 65.26 N = 3 Control 58.17 56.96 8.05 83.18 93.33 83.32 92.68 74.00 68.71 Experts 48.33 50.40 5.03 68.24 97.42 82.44 89.63 76.20 64.71 AC/DC 62.46 59.45 5.37 84.34 93.71 83.10 89.02 75.40 69.11 N = 8 Control 69.35 67.95 12.42 89.29 95.53 88.58 93.90 78.40 74.43 AC/DC 73.31 69.63 11.41 90.29 96.44 88.24 89.63 81.40 75.04 Qwen 3 Big Model 57.30 53.60 0.30 83.70 94.70 84.80 96.34 83.80 69.32 N = 3 Control 63.59 64.95 10.74 87.93 94.77 91.78 92.07 78.60 73.05 Experts 63.77 65.09 9.06 89.67 95.38 90.32 95.12 81.60 73.75 AC/DC 62.74 64.60 12.75 87.71 94.24 90.74 94.51 81.00 73.54 N = 8 Control 73.01 73.55 13.42 92.0 95.83 94.78 93.90 81.60 77.26 AC/DC 73.17 75.09 17.45 92.94 96.29 94.32 95.12 86.00 78.80 DeepSeek V1 Big Model 40.10 31.70 3.00 62.20 80.50 29.80 70.12 64.00 47.68 N = 3 Control 39.85 29.39 2.68 48.21 74.15 22.90 56.10 49.00 40.29 Experts 27.34 18.14 1.34 34.01 54.97 49.48 71.34 63.00 39.95 AC/DC 37.22 32.74 1.68 51.43 84.00 49.52 72.56 68.00 49.64 N = 8 Control 55.94 43.74 8.39 65.57 85.67 34.94 73.17 59.20 53.33 AC/DC 49.35 46.54 6.71 69.34 89.92 64.00 80.49 76.60 60.37 GPT-4o Big Model 54.31 53.64 7.72 83.08 94.69 74.32 90.20 86.80 68.10

#### B.1.2 Analysis and Key Insights

Evolutionary Discovery Outperforms Manual Curation. Despite expert models’ superior performance in specialized domains, AC/DC discovers model combinations with broader skill Coverage. This suggests that the space of useful model combinations extends beyond obvious domain-specific specializations.

Model Diversity Beats Parameter Scaling. Across both task force sizes, our distributed approach outperforms larger monolithic models while using fewer total parameters. This finding supports the hypothesis that specialized model populations can achieve superior Coverage compared to scaling individual models.

Complementary vs. Overlapping Skills. The consistent improvements over control baselines demonstrate that our evolved models develop genuinely complementary capabilities rather than redundant expertise. This validation supports our core hypothesis about automatic discovery of collective intelligence through evolutionary pressure for both quality and diversity.

### B.2 Best-of-N Results

#### B.2.1 Results for All Models on All Benchmarks

Table 7: AC/DC (ours) Best-of-N performance comparison across different benchmarks and model configurations for all model families (see Section A.2). Key findings are discussed in the next subsection in Section B.2.2.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. Qwen 2 Big Model 82.04 63.15 10.27 68.42 90.83 66.18 82.93 70.40 66.78 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 72.16 46.33 22.54 63.97 88.70 67.46 75.61 57.40 61.77 Control 59.81 42.07 16.07 60.01 89.54 60.90 78.05 58.60 58.13 AC/DC 71.31 50.20 19.64 63.11 86.58 59.46 73.78 59.60 60.46 N = 8 Control 71.62 51.45 27.68 67.72 90.22 64.00 80.49 60.80 64.25 AC/DC 76.14 56.84 25.22 69.73 88.86 61.46 78.66 59.80 64.59 Qwen 2.5 Big Model 84.65 70.64 10.71 53.14 91.74 81.96 89.63 80.20 70.33 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 77.97 60.72 19.86 65.40 90.22 77.84 85.98 69.00 68.37 Control 76.29 59.99 17.41 60.91 91.21 76.74 83.54 68.60 66.84 AC/DC 78.22 60.34 18.53 62.20 88.55 77.68 84.15 67.20 67.11 N = 8 Control 78.21 64.40 21.65 67.87 91.13 79.36 86.59 71.20 70.05 AC/DC 79.41 63.50 22.10 70.60 89.91 77.86 83.54 66.80 69.22 Qwen 3 Big Model 88.81 73.11 8.48 38.30 94.69 84.80 96.34 83.80 71.04 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 81.81 67.99 17.86 55.51 92.65 88.14 87.20 74.80 70.75 Control 81.36 68.86 13.62 51.10 93.10 86.70 90.85 74.20 69.97 AC/DC 81.17 69.31 14.06 52.10 92.12 86.86 91.46 75.00 70.26 N = 8 Control 82.03 70.99 18.75 59.12 92.95 89.20 87.80 74.40 71.91 AC/DC 82.33 71.47 20.31 62.05 91.58 88.10 89.02 74.40 72.41 DeepSeek V1 Big Model 70.81 43.12 14.73 57.86 80.52 29.80 70.12 64.00 53.87 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 51.30 29.96 27.90 50.22 54.81 19.34 50.00 43.40 40.87 Control 55.35 33.55 22.54 54.03 73.62 42.72 54.88 48.20 48.11 AC/DC 59.76 37.87 29.24 55.03 81.20 43.80 57.32 56.60 52.60 N = 8 Control 66.46 41.79 25.22 64.11 81.20 25.84 56.10 46.40 50.89 AC/DC 67.70 47.17 33.26 63.86 85.06 50.64 62.20 60.60 58.81 GPT-4o Big Model 54.31 53.64 7.72 83.08 94.69 74.32 90.20 86.80 68.10

#### B.2.2 Analysis and Key Insights

Coverage-to-Selection Translation. The consistent improvements in single answer selection validate that our Coverage gains reflect genuine complementary capabilities rather than statistical artifacts. Models that cover diverse skills collectively also contribute effectively when aggregated through selection mechanisms.

Parameter Efficiency. Our results support the hypothesis that distributed specialized models can (given sophisticated selection/collaboration strategies) achieve superior performance compared to parameter scaling. For example, the N=8 configuration for our DeepSeek 7B models outperform a model with 14% more parameters within the same model family, while the N=3 configuration nearly matches a model with 210% more parameters.

Selection Method Optimization. The benchmark-specific selection strategies highlight the importance of matching aggregation methods to task characteristics. This finding suggests that future work on collective intelligence should consider exploring task-aware selection mechanisms rather than universal approaches.

Generalization Beyond Benchmarks. These findings reinforce our evidence from Section B.1 that diverse collectives of smaller models can outperform larger monolithic models. Importantly, our open-ended evolutionary algorithm achieves these results without optimizing for any specific downstream benchmark, supporting the hypothesis that diversity-driven evolution discovers broadly applicable complementary skills rather than benchmark-specific adaptations.

## Appendix C Extended Discussion on Limitations

Table 8: AC/DC (ours) Coverage performance comparison across different benchmarks for the Llama 3 family of models (see Section A.2 for details on the model used).

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. judge judge judge judge Llama 3 Big Model 47.50 43.40 3.70 78.70 92.20 50.32 81.71 68.20 58.22 N = 3 Control 51.12 45.27 6.04 75.96 89.77 43.48 70.73 63.80 55.77 Experts 45.9 38.58 8.05 66.47 94.47 47.88 68.90 65.00 54.41 AC/DC 47.74 40.25 8.39 71.91 87.26 37.82 67.68 64.20 53.16 N = 8 Control 64.44 59.49 12.08 87.09 95.45 56.40 78.05 71.20 65.53 AC/DC 59.22 52.13 13.09 83.58 90.98 46.14 75.61 70.80 61.44 GPT-4o Big Model 54.31 53.64 7.72 83.08 94.69 74.32 90.20 86.80 68.10

Table 9: AC/DC (ours) Best-of-N performance comparison across different benchmarks for the Llama 3 family of models (see Section A.2 for details on the model used).

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. Big Model 60.67 59.23 17.19 69.21 92.19 50.32 81.71 68.20 62.34 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 71.46 51.44 24.78 61.02 82.03 37.38 67.07 56.60 56.47 Control 68.47 50.22 24.55 65.73 86.05 41.70 62.20 56.60 56.94 AC/DC 69.94 47.58 20.76 62.71 82.79 34.00 62.20 56.00 54.50 N = 8 Control 71.86 55.46 28.35 73.25 89.16 42.92 66.46 58.80 60.78 AC/DC 74.58 51.51 30.80 69.67 84.23 36.58 61.59 55.80 58.10 GPT-4o Big Model 54.31 53.64 7.72 83.08 94.69 74.32 90.20 86.80 68.10

In Sec. 6, we discuss several limitations which we provide further discussion on in this section. As mentioned, the process of model merging is strongly reliant on the compatability of the seed models used, as also observed in previous work [^52]. A supporting example of this observation are our experiments on the Llama3 family of models, where Tab. 8 and Tab. 9 present our Coverage and BoN results, respectively. Merged models typically inherit both the strengths and the limitations of parent models, producing models that are more prone to response degradation even on the same benchmark where other kinds of merged models solve benchmark tasks without fail.

## Appendix D Additional Results

The experiments for additional results were performed using the Qwen 2 family of models.

### D.1 Impact of Algorithm Components

Table 10: Ablation study of AC/DC (ours), showing the impact of different components of the evolutionary algorithm. Coverage performance across benchmarks (excluding Minerva) for N=3 and N=8 configurations with individual components removed.

| Configuration | N=3 | N=8 |
| --- | --- | --- |
| AC/DC | 60.82 | 69.00 |
| Fitness Only | 58.36 | 67.82 |
| No Mutation | 59.66 | 67.81 |
| No Novelty Filter | 60.32 | 68.63 |
| No Gibberish Filter | 58.43 | 68.12 |
| W/o all components | 58.46 | 61.98 |

Tab. 10 presents the results of an ablation where we remove one component of AC/DC’s algorithm at a time. We discuss the observations in Sec. 4. Moreover, we present the average across all benchmarks excluding Minerva Math, which we discuss in Section D.5.1.

### D.2 Impact of Task Force Selection Strategies

Table 11: Impact of Task Force selection strategies. Results showing average Coverage across all benchmarks and all models.

| Method | N=3 | N=8 |
| --- | --- | --- |
| Global Skill Vector (Coverage) | 60.47 | 68.24 |
| Global Skill Vector (Fitness) | 59.94 | 67.44 |
| Random | 57.38 | 65.74 |

After letting AC/DC run for multiple generations, we populate an extensive global archive of models and synthetic tasks. Several approaches to selecting our $N$ models for our Task Force exist. In this section, we discuss the following three:

- Global skill vector (Coverage). For this strategy, we evaluate all our models in our global model archive on all tasks in our global task archive. We then select the $N$ models that maximize the Coverage on our synthetic data archive, ”optimizing” for complementary skills.
- Global skill vector (fitness). Here, we also perform the complete global task archive evaluation as above, but now select the $N$ fittest models.
- Random We here randomly select $N$ models from our global model archive.

Tab. 11 presents the results of these three selection strategies. We evaluate all model families (Qwen 2, Qwen 2.5, Qwen 3, DeepSeek) on all benchmarks (see Section A.4.1, using the llm-as-a-judge variants of the respective benchmarks), except for Minerva Math, due to compute constraints for this ablation. We observe that random selection performs the worst across both $N=3$ and $N=8$ scales, demonstrating that intelligent task force composition based on our synthetic dataset translates to improved downstream performance. Selecting based on maximizing Coverage and selecting the highest fitness individuals on our global task archive (the global skill vector) both demonstrate superior performance, yet, optimizing for synthetic data Coverage yields the highest accuracy gains.

### D.3 Task Archive Novelty Over Time

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/task_adapration_types_and_vendi_over_time.png)

Figure 6: Adaptation types and Vendi score over time. For this experiment, we only enabled adaptations types to be making a task more difficult or completely novel. Moreover, we show the global Vendi Score (Vendi score of the global task archive) over time demosntreating increasing diversity in our task archive.

Fig. 6 presents the adaptation types at each task adaptation cycle and the global Vendi score [^41], i.e., the Vendi score for our global task archive. The Vendi score is a measure for diversity in task embedding space. For this experiment, we only enable tasks to be evolved to be either more difficult, or novel. We can observe that over the course of training, we mostly generate more difficult tasks, highlighting the increasing difficult of our task archive over time, until we discover the capability limits of our population at generation 35, 40, and, especially, generation 45, where we see a stark decrease in adaptations for harder tasks and an increase in adaptations for more novel tasks.

Moreover, we observe a steady increase in the Vendi score, demonstrating an increasing diversity within our global task archive. Nevertheless, we observe that with each adaptation cycle, the increase of the Vendi score gradually decreases, compared to the early generations.

The Vendi score measures diversity within the task embedding space. This has the advantage of capturing the spread across diverse problem formulations and wording, which can be more easily separated using embeddings. Nevertheless, this also means that the Vendi score is subject to a core limitation of embedding-based similarity/spread measures. Although the context can be structurally similar, the semantics can be very different. For this reason, following prior work [^91], we implement a two-layered novelty filter. First, we assess embedding-based similarity, and then we evaluate semantic novelty using an LLM judge. Because of the latter, we can have a more fine-grained assessment of novel tasks, which is reflected in the fact that, although the increase in Vendi score seems to slow down at around generations 40/45, we still observe that we add 71 new tasks (23 harder + 48 novel), which is comparable to earlier generations.

In fact, analyzing the task difficulty dynamics, we observe the generation 45’s decreased ”harder” adaptations reflect the system discovering current capability limits of the model population and pivoting to novel exploration (48 novel tasks). This suggests continued innovation in task space, especially considering that the space of possible tasks may be incomprehensible, rather than task novelty saturation. Fig. 1 shows continued downstream performance improvement through generation 50, confirming that capability advancement continues.

### D.4 Discussion on Experts N=8 Baseline

Table 12: Coverage comparison between Experts and AC/DC (ours) with N = 8 across different model families.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. judge judge judge judge Qwen 2 Experts 72.06 69.14 9.73 86.83 95.91 82.52 91.46 75.20 72.86 AC/DC 67.20 63.03 15.44 82.03 94.77 75.32 89.02 74.40 70.15 Qwen 2.5 Experts 72.97 67.86 10.74 89.55 96.97 88.80 95.12 81.80 75.48 AC/DC 73.31 69.63 11.41 90.29 96.44 88.24 89.63 81.40 75.04 Qwen 3 Experts 72.61 73.51 14.77 92.88 97.27 94.36 95.73 95.40 79.57 AC/DC 73.17 75.09 17.45 92.94 96.29 94.32 95.12 86.00 78.80 DeepSeek V1 Experts 47.24 36.15 5.7 55.68 77.48 60.34 76.22 70.20 53.63 AC/DC 49.35 46.54 6.71 69.34 89.92 64.00 80.49 76.60 60.37

AC/DC demonstrates consistent improvements over our primary baselines across model families. However, one might consider alternative configurations that maximize the utilization of expert models within our inference budget. To address this, we evaluate a configuration that distributes 8 inference calls across our three expert models (3 instruct, 3 code, 2 math calls), shown in Tab. 12.

While this ”Experts 8” baseline achieves competitive performance in some cases, we note several important distinctions from AC/DC: (1) the 3-3-2 distribution represents a manually tuned configuration rather than a principled allocation strategy, (2) it relies on multiple sampling from a limited set of models rather than leveraging diverse evolved capabilities, and (3) the comparison conflates inference-time scaling with AC/DC’s model discovery process.

The arbitrary nature of this baseline becomes apparent when considering alternative distributions: other configurations such as 4-2-2 or 2-4-2 would yield different results, and in the extreme case of 8-0-0 (using only the instruct model), we recover our Control 8 baseline, which we have already demonstrated that AC/DC consistently outperforms across all model families.

Notably, AC/DC maintains competitive or superior performance while discovering genuinely diverse models through evolution, rather than simply increasing inference calls to existing models. The mixed results across benchmarks suggest that raw inference scaling and evolved model diversity offer complementary but distinct advantages.

In particular, on the judge-evaluated benchmarks (MMLU Judge, MMLU Pro Judge, GPQA Judge, BBH Judge), AC/DC consistently outperforms Experts 8 across Qwen 2.5, Qwen 3, and DeepSeek V1 on all four metrics, and achieves notably higher GPQA scores across all model families (+5.71, +0.67, +2.68, +1.01 percentage points respectively), suggesting that our evolved task force is especially beneficial for tasks requiring open-ended reasoning where the answers are not provided in a multiple-choice format.

### D.5 Comparison to Prior QD Methods

To compare AC/DC (with coevolution and QD) with prior quality-diversity approaches without coevolution (DNS [^7] and CycleQD (CQD) [^72]), we conduct experiments using identical training conditions. For all methods discussed, we train on the same model family, Qwen 2. Both baseline methods are trained on the same four benchmarks used in our evaluation, with 50 fixed training samples drawn from each of GSM8K [^25], MBPP [^6], AgentBench OS, and AgentBench DB [^89].

For the task force selection strategies:

- CQD: Following their approach, after evolution, we select the top 2 models from each task-specific archive (2 models × 4 tasks = 8 models total for N=8). For N=3, we collect the top models for GSM8K, MBPP, and AgentBench OS.
- DNS: We select the top-8 models based on local competition scores, which measure performance against local neighborhoods in the behavior space. For N=3, we select the top-3 models.

The key distinction is that while both DNS and CycleQD directly optimize for performance on these specific benchmarks during training, AC/DC evolves models on synthetically generated tasks without any benchmark-specific optimization. Despite this apparent disadvantage, AC/DC achieves superior performance at N=8, demonstrating that evolution on diverse synthetic tasks can discover more capable and complementary models than direct benchmark optimization.

We also analyzed train-set coverage for DNS and CQD. On the 200 tasks total (4 sets of 50 training examples across the tasks), we evaluated the top-20 models and top-5 models for DNS (based on local competition score). For CQD, we select the top-5 from the top-2 in GSM8K, and top models for the three other tasks, and for top-20, we get the five best models for each of the 4 tasks. For top-5 coverage, DNS beats CQD, obtaining 60.5% versus 56.5%. For top-20, DNS again beats CQD, obtaining 70% versus 65%. Results provide even more evidence for the suitability of DNS as a QD algorithm for AC/DC over CQD.

#### D.5.1 Full Results for All Methods on All Benchmarks

Table 13: Comparison of AC/DC (ours) to prior QD methods. Results showing average Coverage across all benchmarks. †Average excluding Minerva benchmark.

Method N MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. Avg.† judge judge judge judge AC/DC 3 55.42 51.28 10.07 69.44 90.00 39.88 84.15 65.40 58.21 60.82 DNS 3 52.26 48.98 9.40 69.08 90.37 45.88 84.15 67.00 58.39 60.18 CQD 3 51.94 48.43 9.06 67.40 91.81 46.08 83.54 66.80 58.13 59.85 AC/DC 8 66.78 62.72 15.77 81.67 95.07 51.86 88.41 72.60 66.86 69.00 DNS 8 62.37 59.69 14.77 79.33 93.03 54.38 86.59 69.60 64.97 66.48 CQD 8 60.19 57.49 13.76 78.82 93.71 51.52 85.37 68.60 63.68 65.42

In Tab. 13, we present the full results per benchmark. Additionally, we show the average performance across all benchmarks and the average across all except Minerva. In Tab. 3 we present the average results without Minerva, because, due to computational constraints, we restricted to running the benchmark with the default lm-eval-harness settings, which have a lower maximum output token length. For other comparisons (and for our main results), we compute results that more accurately reflect the models/populations’ true capabilities.

### D.6 DNS on Static Synthetic Dataset

To estimate the effects of an ablation where we execute our pipeline on a static synthetic dataset, we consider the progress made up until generation 5 of our existing AC/DC run on Qwen 2.5 as representative performance.

In other words, it is reasonable to expect that the performance would stagnate at around that of our task force at generation 5, as up to that point, our synthetic dataset is static and would then be updated.

To support this argument, we analyze the newly added models per generation. With a static dataset, we expect the number of new (fit and diverse) models discovered to significantly reduce early in the evolution process. We observe this behaviour when looking at the number of new models in our DNS baseline (Fig. 7 (a)), where we evolve models on the static dataset of downstream benchmark training sets. In contrast, looking at the number of new models discovered when running our AC/DC algorithm (Fig. 7 (b)), we detect a constant influx of new models.

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/model_counts_per_gen-DNS.png)

(a) DNS

Considering this, we find that the average performance on our LLM-as-a-judge tasks, our generation 5 task force achieves 59.66% accuracy, whereas our final task force, achieved through a dynamically coevolving synthetic dataset achieves 61.19% (1.53% absolute improvement).

Table 14: Static vs. Coevolving Synthetic Dataset. Coverage comparison between task forces evolved on a static synthetic dataset versus our full coevolution approach on Qwen 2.5. The static baseline shows a performance plateau when the synthetic dataset does not dynamically coevolve with the model population. The values for ”AC/DC (Coevolving)” are the average scores across two training runs with two different RNG seeds.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval Avg. judge judge judge judge N=3 Static Dataset 53.15 51.74 3.69 80.97 92.27 51.48 87.80 60.16 AC/DC (Coevolving) 56.67 55.72 5.37 81.65 93.10 40.69 88.72 60.27 Improvement +3.52 +3.98 +1.68 +0.68 +0.83 -10.79 +0.92 +0.11 N=8 Static Dataset 59.38 57.37 4.36 85.18 94.01 59.62 90.24 64.31 AC/DC (Coevolving) 67.80 66.30 7.72 88.40 95.64 56.33 93.29 67.93 Improvement +8.42 +8.93 +3.36 +3.22 +1.63 -3.29 +3.05 +3.62

Additionally, Tab. 14 presents the quantitative comparison between task forces evolved on a static synthetic dataset (i.e. the initialized task pool without further adaptation) versus our full coevolution approach on Qwen 2.5. The static dataset baseline achieves 60.16% average Coverage for N=3 and 64.31% for N=8. In contrast, our coevolving approach achieves 60.27% and 67.93%, respectively, representing absolute improvements of +0.11% and +3.62%.

The improvements are particularly pronounced on knowledge-intensive benchmarks (MMLU: +3.52%/+8.42%, MMLU Pro: +3.98%/+8.93%) and reasoning tasks (GPQA: +1.68%/+3.36%, BBH: +0.68%/+3.22%). While the static baseline shows higher performance on Minerva Math, this is likely due to the early-stage synthetic dataset being biased toward mathematical reasoning tasks, which we expect to be subsequently diversified through coevolution.

These results demonstrate that dynamic coevolution of the synthetic task archive is critical for discovering diverse and complementary model capabilities. The findings strengthen our hypothesis that open-ended evolution requires continuous expansion of the challenge space and going beyond optimizing for the affinity between a population of models and a fixed distribution of diverse tasks [^2].

### D.7 Effect of Seed Tasks

In Section E.3, we present the four seed tasks used to initiate the coevolution process.

Table 15: Impact of Seed Tasks. Coverage comparison between coevolution runs with all seed tasks versus without code generation seed tasks on Qwen 2.5. The values for ”All Seed Tasks” are the average scores across two training runs with two different RNG seeds.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval Avg. judge judge judge judge N=3 W/o Code Seed Task 62.46 59.45 5.37 84.34 93.71 41.02 89.02 62.20 All Seed Tasks 56.67 55.72 5.37 81.65 93.10 40.69 88.72 60.27 N=8 W/o Code Seed Task 73.31 69.63 11.41 90.29 96.44 53.84 90.24 69.31 All Seed Tasks 67.80 66.30 7.72 88.40 95.64 56.33 93.29 67.93

In Tab. 15, we ablate the effect of two different compositions of seed tasks. Once All Seed Tasks, where we use all four seed tasks, and once W/o Code Seed Task, where we use the three seed tasks, excluding Section E.3.2.

We can observe that the selection of seed tasks can have a big effect on the performance of the final task force. Leveraging all four seed tasks, including the coding seed task, can improve the coding benchmark performance (at N=8, HumanEval performance being 3.25% better than without the coding task), but, in effect, can hurt downstream performance on other benchmarks (e.g., at N=8, on MMLU judge and MMLU Pro judge, the performance being -5.51% and -3.33%).

### D.8 Effect of Scientist Model

To explore the generalizability of AC/DC to different scientist models, we conducted an experiment using Qwen3-235B-A22B as the scientist model while maintaining the existing prompts and hyperparameters optimized for Qwen2.5-72B. This experiment highlights both the flexibility of AC/DC and the importance of model-specific prompt engineering.

Using the original generation settings, we observed that the Qwen3-235B-A22B scientist model frequently produced incomplete task implementations within our generation token limit, yielding 555 total synthetic tasks compared to over 1000 tasks generated by the Qwen2.5-72B scientist model. We evaluated the resulting task forces using the same Qwen2 7B subject model across both conditions.

| Scientist Model | Avg. Coverage ($N=3$) | Avg. Coverage ($N=8$) |
| --- | --- | --- |
| Qwen2.5-72B | 58.21 | 66.86 |
| Qwen3-235B-A22B | 57.57 | 65.46 |

Table 16: Task force performance comparison for two runs using two different scientist models. Both configurations use Qwen2 7B as the subject model.

As shown in Table 16, the task forces generated with the Qwen3-235B-A22B scientist model achieve slightly lower Coverage scores than those generated with Qwen2.5-72B. We attribute this performance gap primarily to the reduced size of the synthetic task pool.

Importantly, the lower task force scores do not necessarily indicate inferior capability of the Qwen3-235B-A22B scientist model itself. Rather, this case study illustrates the practical considerations when adapting AC/DC to different scientist models. We expect that with appropriate prompt engineering, adjusted generation limits, and hyperparameter tuning specific to the Qwen3-235B-A22B model, the framework could effectively leverage its potentially superior capabilities to generate higher-quality synthetic tasks and achieve improved downstream performance.

### D.9 Effects of Response Length Criteria for Evolved Model Selection

We may want to discover models that follow desired criteria that are non-trivial to train for via loss functions. Setting the desired criteria for candidate models to follow during coevolution can be a simple approach to get such desired model performance.

We find that the configuration setting of output token length during coevolution can aid in discovering models that are more suited to different response length limits (e.g. 256 output tokens) than off-the-shelf models in some cases. Interestingly still, evolved models are flexible in providing correct responses to benchmark tasks when the default response length setting for a benchmark at test-time (2048) is longer than what was used during coevolution (512). Setting additional minimal criteria for models during coevolution can be a simpler approach of discovering more suitable models for solving tasks in desired ways than defining custom loss functions or architecture adaptations.

We present and discuss the results for Coverage and Best-of-N against baselines under the short response length benchmark setting for code and math benchmarks, and compare the performance of AC/DC against baselines in this setting against the default response length setting.

To show if performance gaps between the AC/DC task force and baselines are wider or narrower in the short response setting in comparison to the default response setting, we calculate the change in performance gap (going from the default setting to the short response setting). This is done for the code and math benchmarks. We then show this for both Coverage and Best-of-N in Tabs. 17 and 19 respectively. The full benchmark results for the short response setting used as part of the calculations are shown in Tabs. 18 and 20.

#### D.9.1 Coverage Comparison Against Default Response Length Setting

Table 17: Change in coverage performance gap: short vs. long response benchmarking. A positive value indicates that AC/DC’s advantage over the baseline is larger in the short-response setting than in the default setting.

<table><tbody><tr><td rowspan="2">Base Model</td><td>vs Experts</td><td colspan="2">vs Control (%)</td><td colspan="2">vs Big Model (%)</td></tr><tr><td>N=3 (%)</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td></tr><tr><td>Qwen2 7B</td><td>+0.43</td><td>+2.34</td><td>+2.84</td><td>+9.76</td><td>+11.53</td></tr><tr><td>Qwen2.5 7B</td><td>-1.47</td><td>+4.43</td><td>+6.19</td><td>+3.90</td><td>+6.32</td></tr><tr><td>Qwen3 14B</td><td>-0.89</td><td>-0.37</td><td>+0.65</td><td>+2.63</td><td>+3.43</td></tr><tr><td>DeepSeek V1 7B</td><td>-1.96</td><td>-6.12</td><td>-5.39</td><td>+0.72</td><td>+1.50</td></tr><tr><td>Average</td><td>-0.97</td><td>+0.07</td><td>+1.07</td><td>+4.25</td><td>+5.70</td></tr></tbody></table>

Coverage gains by AC/DC against the Big Model baseline are wider for the short response setting, when compared to the performance gap observed in the default response setting. The change in performance gap is seen across all four model family runs, as shown in Tab. 17.

These findings suggest that typical larger off-the-shelf models are even weaker by default at giving more concise responses to the prompt than coevolved models that have been selected to give more correct responses given a shorter response length limit. This observation is grounded in the concrete Coverage gains by AC/DC over baselines in the main table. In general, selection of desired criteria for evolved models can be a simple approach to adapt model behavior for better Coverage under different settings, as an alternative to multi-objective optimization.

Table 18: AC/DC (ours) Coverage performance comparison in the short response length evaluation setup across different benchmarks and model configurations for all model families used (see Section A.2). The short response setting has been applied to evaluation on math and code benchmarks.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. judge judge judge judge Qwen 2 Big Model 50.44 47.12 4.36 78.32 90.83 35.56 49.39 64.00 52.50 N = 3 Control 54.58 50.97 7.72 73.01 92.34 36.10 79.88 64.20 57.35 Experts 47.05 41.78 6.38 65.29 91.28 47.50 81.10 66.00 55.80 AC/DC 55.42 51.28 9.06 69.44 89.99 39.88 84.15 65.40 58.08 N = 8 Control 67.69 64.27 12.75 84.54 95.68 46.10 92.07 70.60 66.71 AC/DC 67.20 63.03 15.44 82.03 94.77 53.26 89.02 72.00 67.09 Qwen 2.5 Big Model 49.30 47.00 0.00 82.30 91.70 28.30 89.60 75.40 57.95 N = 3 Control 58.17 56.96 8.05 83.18 93.33 31.94 90.85 66.60 61.14 Experts 48.33 50.40 5.03 68.24 97.42 46.22 90.85 74.2 60.09 AC/DC 62.46 59.45 5.37 84.34 93.71 41.02 89.02 74.60 63.75 N = 8 Control 69.35 67.95 12.42 89.29 95.53 39.84 92.68 70.4 67.18 AC/DC 73.31 69.63 11.41 90.29 96.44 53.84 90.24 82.00 70.90 Qwen 3 Big Model 57.30 53.60 0.30 83.70 94.70 23.10 94.50 74.60 60.23 N = 3 Control 63.59 64.95 10.74 87.93 94.77 32.02 93.29 76.40 65.46 Experts 63.77 65.09 9.06 89.67 95.38 37.48 93.90 77.00 66.42 AC/DC 62.74 64.60 12.75 87.71 94.24 31.32 93.90 78.80 65.76 N = 8 Control 73.01 73.55 13.42 92.0 95.83 37.76 93.29 77.6 69.56 AC/DC 73.17 75.09 17.45 92.94 96.29 39.28 95.73 81.4 71.42 DeepSeek V1 Big Model 40.10 31.70 3.00 62.20 80.50 25.20 26.20 56.40 40.66 N = 3 Control 39.85 29.39 2.68 48.21 74.15 20.94 29.27 49.00 36.69 Experts 27.34 18.14 1.34 34.01 54.97 36.44 60.98 41.00 34.28 AC/DC 37.22 32.74 1.68 51.43 84.0 39.08 58.54 39.20 42.99 N = 8 Control 55.94 43.74 8.39 65.57 85.67 33.02 45.73 60.00 49.76 AC/DC 49.35 46.54 6.71 69.34 89.92 51.02 72.56 47.40 54.11

#### D.9.2 Best-of-N Comparison Against Default Response Length Setting

Table 19: Change in Best-of-N performance gap: short vs. long response benchmarking. A positive value indicates that AC/DC’s advantage over the baseline is larger in the short-response setting than in the default setting.

<table><tbody><tr><td rowspan="2">Base Model</td><td>vs Experts</td><td colspan="2">vs Control (%)</td><td colspan="2">vs Big Model (%)</td></tr><tr><td>N=3 (%)</td><td>N=3</td><td>N=8</td><td>N=3</td><td>N=8</td></tr><tr><td>Qwen2 7B</td><td>+4.40</td><td>+2.50</td><td>+1.67</td><td>+11.92</td><td>+11.89</td></tr><tr><td>Qwen2.5 7B</td><td>-1.48</td><td>+2.21</td><td>+5.45</td><td>+2.80</td><td>+6.08</td></tr><tr><td>Qwen3 14B</td><td>+4.16</td><td>+0.11</td><td>-1.36</td><td>+3.10</td><td>+2.45</td></tr><tr><td>DeepSeek V1 7B</td><td>-8.61</td><td>+4.72</td><td>-6.12</td><td>-6.17</td><td>+0.72</td></tr><tr><td>Average</td><td>-0.38</td><td>+2.38</td><td>-0.09</td><td>+2.91</td><td>+5.28</td></tr></tbody></table>

Best-of-N gains by AC/DC against the Big Model baseline are wider for the short response setting compared to the default response setting, as shown in Tab. 19, mirroring the pattern observed for Coverage. The widening performance gap against the Big Model baseline is consistent across three of the four model families, with an average increase of $+2.91\%$ at N=3 and $+5.28\%$ at N=8. All four model families show a positive increase at N=8.

Our findings suggests that further gains under different Best-of-N evaluation constraint settings can be achieved in coevolved models solely through the design of the right set of selection criteria during coevolution. The right selection criteria could even lead to better Best-of-N performance than standalone answers from big off-the-shelf models, under different (e.g., shorter) response settings. Additionally, further gains in the short response setting can facilitate more efficient Best-of-N selection by reducing the context length for models that need to select the best answer out of multiple candidates.

Table 20: AC/DC (ours) Best-of-N performance comparison in the short response length evaluation setup across different benchmarks and model configurations for all model families (see Section A.2). The short response setting has been applied to evaluation on math and code benchmarks.

Method MMLU MMLU Pro GPQA BBH GSM8K Minerva HumanEval MBPP Avg. Qwen 2 Big Model 82.04 63.15 10.27 68.42 90.83 35.56 49.39 64.00 57.96 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 72.16 46.33 22.54 63.97 88.70 43.70 66.46 49.80 56.71 Control 59.81 42.07 16.07 60.01 89.54 30.84 75.61 58.20 54.02 AC/DC 71.31 50.20 19.64 63.11 86.58 35.28 78.66 56.00 57.60 N = 8 Control 71.62 51.45 27.68 67.72 90.22 37.12 79.88 58.60 60.54 AC/DC 76.14 56.84 25.22 69.73 88.86 41.46 79.27 56.20 61.72 Qwen 2.5 Big Model 84.65 70.64 10.71 53.14 91.74 28.28 89.63 75.40 63.02 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 77.97 60.72 19.86 65.40 90.22 44.12 81.10 66.26 63.21 Control 76.29 59.99 17.41 60.91 91.21 28.30 80.49 64.00 59.83 AC/DC 78.22 60.34 18.53 62.20 88.55 33.64 82.32 65.80 61.20 N = 8 Control 78.21 64.40 21.65 67.87 91.13 31.00 85.98 64.20 63.06 AC/DC 79.41 63.50 22.10 70.60 89.91 45.92 81.71 66.40 64.94 Qwen 3 Big Model 88.81 73.11 8.48 38.30 94.69 23.12 94.51 74.60 61.95 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 81.81 67.99 17.86 55.51 92.65 34.68 82.32 56.20 61.13 Control 81.36 68.86 13.62 51.10 93.10 28.58 89.02 73.40 62.38 AC/DC 81.17 69.31 14.06 52.10 92.12 28.12 89.63 75.26 62.72 N = 8 Control 82.03 70.99 18.75 59.12 92.95 30.92 89.63 73.40 64.72 AC/DC 82.33 71.47 20.31 62.05 91.58 32.96 87.20 68.46 64.55 DeepSeek V1 Big Model 70.81 43.12 14.73 57.86 80.52 25.20 26.22 56.40 46.86 Divide and Conquer Monarchical LLM RM-based N = 3 Experts 51.30 29.96 27.90 50.22 54.81 31.40 48.78 24.60 39.87 Control 55.35 33.55 22.54 54.03 73.62 17.80 20.73 46.00 40.45 AC/DC 59.76 37.87 29.24 55.03 81.20 34.52 50.00 30.80 47.30 N = 8 Control 66.46 41.79 25.22 64.11 81.20 23.94 26.83 48.80 47.29 AC/DC 67.70 47.17 33.26 63.86 85.06 40.30 56.10 23.80 52.16

## Appendix E Additional Qualitative Results

### E.1 Case Study on Synthetic Task Diversity

![Refer to caption](https://arxiv.org/html/2604.14969v1/x6.png)

Figure 8: Analysis of global task archive embedding space generated by AC/DC with Qwen 2. We represent each task by structuring its metadata using the template in Section F.3 and then embedding it using an embedding model (see Tab. 5 ). We then reduce the dimensionality of the embeddings using t-SNE 130. The clusters are automatically generated using HDBSCAN 93.

Fig. 8 presents the global task embedding space evolved through AC/DC with a Qwen2-based population. In the left half of the embedding space, we can find tasks in the writing space, such as

- generating a short story based on a prompt and generating an analogy for an abstract concept, requiring creative writing abilities
- human-ai-interaction, requiring emotional intelligence and alignment
- writing an accurate historical text, testing for historical knowledge
- developing a legal argument given a case, examining legal knowledge and persuasion abilities

The right half of the embedding space presents more technical challenges, for example

- constructing regular expressions
- solving complex math and pattern recognition problems
- proving mathematical theorems
- implementing code such as SQL queries

These example tasks demonstrate the diversity of synthetic tasks generated by AC/DC (many of which might not have been created by human annotators), presenting the breadth of knowledge examined by our system to discover unique capabilities.

### E.2 Case Study on Model Lineages

#### E.2.1 Inspecting Task Force Selection

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/evolution_tree_qwen2.png)

Figure 9: Evolution tree of AC/DC evolving the Qwen2-based seed model. Highlighted models are those selected for the task force by maximizing Coverage on our global task archive.

Fig. 9 presents the evolution tree produced by AC/DC applied to our three Qwen 2 seed models (see Section A.2), highlighting the 8 models selected for our task force. We observe that our task force contains models with a wide fitness range, ranging from $0.53$ to $0.62$. Nevertheless, as described in Sec. 3, this task force is selected for optimizing Coverage across our synthetic data, meaning that we don’t always want the highest fitness individuals, but individuals that have complementary skills (which we discuss in Section D.2).

For instance, we observe that our model discovered in generation 30 (presented as gen\_30\_ind\_1) achieves the highest global fitness, i.e., fitness across our entire synthetic task archive, yet the instruct model, which is part of our task force, does not achieve the highest fitness, but is part of our task force.

#### E.2.2 Inspecting Lineage of Specific Task Force Model

![Refer to caption](https://arxiv.org/html/2604.14969v1/x7.png)

Figure 10: Lineages of AC/DC evolved Qwen2-based models. All presented lineages are of models that are part of the selected task force.

Fig. 10 presents three example lineages of our discovered LLMs, demonstrating complex histories of skill merging of parent models, embedding the knowledge of all three seed models into the weights of the observed models.

The first tree (top) presents the lineage of the model gen\_17\_ind\_6, the sixth model evolved in generation 17. As observed in prior work leveraging evolutionary search techniques [^152], we can see that, to reach the model that was part of the task force, we don’t only leverage high fitness individuals. To discover model gen\_17\_ind\_6, AC/DC first discovered gen\_14\_ind\_6, with a local fitness $f$ of $0.476$, which is weaker lower than that of its parents (gen\_12\_ind\_5, with $f=0.528$ and gen\_10\_ind\_2, $f=0.488$). This highlights that (locally) weaker solutions are relevant for discovering models for a global task force with complementary skills, by potentially providing unique capabilities, not captured by the simple fitness metric.

The second (middle) and third (bottom) tree present the lineages of the models gen\_28\_ind\_6 and gen\_29\_ind\_5, respectively. Both models are accentors of the just discussed model gen\_17\_ind\_6, yet, we can see that gen\_29\_ind\_5 has a more complex lineage than gen\_28\_ind\_6. gen\_28\_ind\_6 only adds one new ancector to its lineage in addition to the lineage of gen\_17\_ind\_6, namely gen\_20\_ind\_3, demonstrating that even only two additional relevant crossover operations can lead to the discovery of capabilities beneficial for the final task force. On the other hand, although the models gen\_29\_ind\_5 and gen\_28\_ind\_6 and gen\_29\_ind\_5 are only one generation apart, we can observe that gen\_29\_ind\_5 introduces more novel and complex lineages.

These observations demonstrate core advantage of evolutionary search, (1) discovering novel solutions by building on top of prior ones that don’t necessarily seem to be the best performing and (2) the emergent complexity of (2.1) intricate lineages or (2.2) sophisticated capabilities through simple but relevant combinations of prior solutions.

### E.3 Seed Tasks Used

#### E.3.1 Seed Task 1: Circular Queue Length

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAicXVlc3Rpb24iOiAiR2l2ZW4gdGhhdCB0aGUgc3RvcmFnZSBzcGFjZSBmb3IgYSBjaXJjdWxhciBxdWV1ZSBpcyB0aGUgYXJyYXkgQVsyMV0sIHdpdGggZnJvbnQgcG9pbnRpbmcgdG8gdGhlIHBvc2l0aW9uIGJlZm9yZSB0aGUgaGVhZCBlbGVtZW50IGFuZCByZWFyIHBvaW50aW5nIHRvIHRoZSB0YWlsIGVsZW1lbnQsIGFzc3VtaW5nIHRoZSBjdXJyZW50IHZhbHVlcyBvZiBmcm9udCBhbmQgcmVhciBhcmUgOCBhbmQgMywgcmVzcGVjdGl2ZWx5LCB0aGUgbGVuZ3RoIG9mIHRoZSBxdWV1ZSBpcyAoKS4iLAogICAgICAgICAgICAgICAgIm9wdGlvbnMiOiB7IkEiOiAiNSIsICJCIjogIjYiLCAiQyI6ICIxNiIsICJEIjogIjE3In0sCiAgICAgICAgICAgICAgICAiYW5zd2VyIjogIkMiLAogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiIiInt0WyJxdWVzdGlvbiJdfVxuQToge3RbIm9wdGlvbnMiXVsiQSJdfVxuQjoge3RbIm9wdGlvbnMiXVsiQiJdfVxuQzoge3RbIm9wdGlvbnMiXVsiQyJdfVxuRDoge3RbIm9wdGlvbnMiXVsiRCJdfVxuXG5SZXR1cm4gdGhlIGxldHRlciBvZiB0aGUgY29ycmVjdCBvcHRpb24uIiIiCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIHJldHVybiAxLjAgaWYgdFsiYW5zd2VyIl0ubG93ZXIoKSA9PSBzdWJtaXNzaW9uLmxvd2VyKCkuc3RyaXAoKSBlbHNlIDAuMA==)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"question": "Given that the storage space for a circular queue is the array A\[21\], with front pointing to the position before the head element and rear pointing to the tail element, assuming the current values of front and rear are 8 and 3, respectively, the length of the queue is ().",

"options": {"A": "5", "B": "6", "C": "16", "D": "17"},

"answer": "C",

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"""{t\["question"\]}\\nA: {t\["options"\]\["A"\]}\\nB: {t\["options"\]\["B"\]}\\nC: {t\["options"\]\["C"\]}\\nD: {t\["options"\]\["D"\]}\\n\\nReturn the letter of the correct option."""

@staticmethod

def score(t: dict, submission: str) -> float | None:

return 1.0 if t\["answer"\].lower() == submission.lower().strip() else 0.0

#### E.3.2 Seed Task 2: First Repeated Character

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAicXVlc3Rpb24iOiAiV3JpdGUgYSBweXRob24gZnVuY3Rpb24gY2FsbGVkIGBmaXJzdF9yZXBlYXRlZF9jaGFyYWN0ZXJgIHRvIGZpbmQgdGhlIGZpcnN0IHJlcGVhdGVkIGNoYXJhY3RlciBpbiBhIGdpdmVuIHN0cmluZy4iLAogICAgICAgICAgICAgICAgInRlc3RfY2FzZXMiOiBbKCJhYmNhYmMiLCAiYSIpLCAoImFiYyIsIE5vbmUpLCAoIjEyMzEyMyIsICIxIildLAogICAgICAgICAgICAgICAgImV4cGVjdGVkX2Z1bmNfbmFtZSI6ICJmaXJzdF9yZXBlYXRlZF9jaGFyYWN0ZXIiLAogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiIiInt0WyJxdWVzdGlvbiJdfSIiIgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGdldF9mdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlCgogICAgICAgICMgVGVzdCBjYXNlcyBmcm9tIGdldF90YXNrcwogICAgICAgIHRlc3RfY2FzZXMgPSB0WyJ0ZXN0X2Nhc2VzIl0KCiAgICAgICAgY29ycmVjdF9jb3VudCA9IDAKICAgICAgICBudW1fdGVzdF9jYXNlcyA9IGxlbih0ZXN0X2Nhc2VzKQoKICAgICAgICAjIEdldCBmdW5jdGlvbiBuYW1lIHRvIGNhbGxhYmxlIG1hcHBpbmcKICAgICAgICBmdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlID0gZ2V0X2Z1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUoc3VibWlzc2lvbikKCiAgICAgICAgaWYgbGVuKGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUpID09IDA6CiAgICAgICAgICAgIHJldHVybiAwLjAKCiAgICAgICAgIyBHZXQgZnVuY3Rpb24gbmFtZXMKICAgICAgICBmdW5jX25hbWVzID0gc2V0KGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUua2V5cygpKQoKICAgICAgICBpZiB0WyJleHBlY3RlZF9mdW5jX25hbWUiXSBub3QgaW4gZnVuY19uYW1lczoKICAgICAgICAgICAgcmV0dXJuIDAuMAoKICAgICAgICAjIFJ1biB0ZXN0IGNhc2VzCiAgICAgICAgZm9yIHRlc3RfaW5wdXQsIGV4cGVjdGVkX291dHB1dCBpbiB0ZXN0X2Nhc2VzOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAjIEV4ZWN1dGUgdGhlIGZ1bmN0aW9uCiAgICAgICAgICAgICAgICBzdWJtaXNzaW9uX3Jlc3VsdCA9IGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGVbCiAgICAgICAgICAgICAgICAgICAgdFsiZXhwZWN0ZWRfZnVuY19uYW1lIl0KICAgICAgICAgICAgICAgIF0odGVzdF9pbnB1dCkKCiAgICAgICAgICAgICAgICAjIENvbXBhcmUgd2l0aCBleHBlY3RlZCBvdXRwdXQKICAgICAgICAgICAgICAgIGlmIHN1Ym1pc3Npb25fcmVzdWx0ID09IGV4cGVjdGVkX291dHB1dDoKICAgICAgICAgICAgICAgICAgICBjb3JyZWN0X2NvdW50ICs9IDEKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICAjIElmIGZ1bmN0aW9uIGZhaWxzIG9uIGEgdGVzdCBjYXNlLCBza2lwIGl0CiAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICBwYXNzX3JhdGUgPSBjb3JyZWN0X2NvdW50IC8gbnVtX3Rlc3RfY2FzZXMKICAgICAgICBtaW5fcGFzc19yYXRlID0gMS4wCgogICAgICAgIHJldHVybiAxLjAgaWYgcGFzc19yYXRlID49IG1pbl9wYXNzX3JhdGUgZWxzZSAwLjAK)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"question": "Write a python function called ‘first\_repeated\_character‘ to find the first repeated character in a given string.",

"test\_cases": \[("abcabc", "a"), ("abc", None), ("123123", "1")\],

"expected\_func\_name": "first\_repeated\_character",

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"""{t\["question"\]}"""

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import get\_function\_name\_to\_callable

\# Test cases from get\_tasks

test\_cases = t\["test\_cases"\]

correct\_count = 0

num\_test\_cases = len(test\_cases)

\# Get function name to callable mapping

function\_name\_to\_callable = get\_function\_name\_to\_callable(submission)

if len(function\_name\_to\_callable) == 0:

return 0.0

\# Get function names

func\_names = set(function\_name\_to\_callable.keys())

if t\["expected\_func\_name"\] not in func\_names:

return 0.0

\# Run test cases

for test\_input, expected\_output in test\_cases:

try:

\# Execute the function

submission\_result = function\_name\_to\_callable\[

t\["expected\_func\_name"\]

\](test\_input)

\# Compare with expected output

if submission\_result == expected\_output:

correct\_count += 1

except Exception:

\# If function fails on a test case, skip it

continue

pass\_rate = correct\_count / num\_test\_cases

min\_pass\_rate = 1.0

return 1.0 if pass\_rate >= min\_pass\_rate else 0.0

#### E.3.3 Seed Task 3: Law Multiple Choice Tree Damage

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAicXVlc3Rpb24iOiAiSG91c2Ugb3ducyBoaXMgaG9tZSBpbiBDaXR5LiBPbiB0aGUgbGF3biBpbiBmcm9udCBvZiBoaXMgaG9tZSBhbmQgd2l0aGluIGZpdmUgZmVldCBvZiB0aGUgcHVibGljIHNpZGV3YWxrIHRoZXJlIHdhcyBhIGxhcmdlIHRyZWUuIFRoZSByb290cyBvZiB0aGUgdHJlZSBjYXVzZWQgdGhlIHNpZGV3YWxrIHRvIGJ1Y2tsZSBzZXZlcmVseSBhbmQgYmVjb21lIGRhbmdlcm91cy4gQW4gb3JkaW5hbmNlIG9mIENpdHkgcmVxdWlyZXMgYWRqYWNlbnQgbGFuZG93bmVycyB0byBrZWVwIHNpZGV3YWxrcyBpbiBzYWZlIGNvbmRpdGlvbi4gSG91c2UgZW5nYWdlZCBDb250cmFjdG9yIHRvIHJlcGFpciB0aGUgc2lkZXdhbGssIGxlYXZpbmcgaXQgdG8gQ29udHJhY3RvciB0byBkZWNpZGUgaG93IHRoZSByZXBhaXIgc2hvdWxkIGJlIG1hZGUuIENvbnRyYWN0b3IgZHVnIHVwIHRoZSBzaWRld2FsaywgY3V0IGJhY2sgdGhlIHJvb3RzIG9mIHRoZSB0cmVlLCBhbmQgbGFpZCBhIG5ldyBzaWRld2Fsay4gVHdvIGRheXMgYWZ0ZXIgSG91c2UgaGFkIHBhaWQgQ29udHJhY3RvciB0aGUgYWdyZWVkIHByaWNlIG9mIHRoZSByZXBhaXIsIHRoZSB0cmVlIGZlbGwgb3ZlciBvbnRvIHRoZSBzdHJlZXQgYW5kIGRhbWFnZWQgYSBwYXJrZWQgY2FyIGJlbG9uZ2luZyB0byBEcml2ZXIuIERyaXZlciBoYXMgYXNzZXJ0ZWQgY2xhaW1zIGFnYWluc3QgSG91c2UgYW5kIENvbnRyYWN0b3IsIGFuZCBib3RoIGRlZmVuZGFudHMgYWRtaXQgdGhhdCBjdXR0aW5nIHRoZSByb290cyBjYXVzZWQgdGhlIHRyZWUgdG8gZmFsbC5JZiBEcml2ZXIgcmVjb3ZlcnMgYSBqdWRnbWVudCBhZ2FpbnN0IEhvdXNlLCBkb2VzIEhvdXNlIGhhdmUgYW55IHJlY291cnNlIGFnYWluc3QgQ29udHJhY3Rvcj8iLAogICAgICAgICAgICAgICAgIm9wdGlvbnMiOiB7CiAgICAgICAgICAgICAgICAgICAgIkEiOiAiTm8sIGlmIHBheW1lbnQgYnkgSG91c2Ugd2FzIGFuIGFjY2VwdGFuY2Ugb2YgdGhlIHdvcmsuIiwKICAgICAgICAgICAgICAgICAgICAiQiI6ICJObywgYmVjYXVzZSBIb3VzZSBzZWxlY3RlZCBDb250cmFjdG9yIHRvIGRvIHRoZSB3b3JrLiIsCiAgICAgICAgICAgICAgICAgICAgIkMiOiAiWWVzLCBpZiB0aGUganVkZ21lbnQgYWdhaW5zdCBIb3VzZSB3YXMgYmFzZWQgb24gdmljYXJpb3VzIGxpYWJpbGl0eS4iLAogICAgICAgICAgICAgICAgICAgICJEIjogIlllcywgYmVjYXVzZSBIb3VzZSdzIGNvbmR1Y3Qgd2FzIG5vdCBhIGZhY3R1YWwgY2F1c2Ugb2YgdGhlIGhhcm0uIiwKICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICAiYW5zd2VyIjogIkMiLAogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiIiInt0WyJxdWVzdGlvbiJdfVxuQToge3RbIm9wdGlvbnMiXVsiQSJdfVxuQjoge3RbIm9wdGlvbnMiXVsiQiJdfVxuQzoge3RbIm9wdGlvbnMiXVsiQyJdfVxuRDoge3RbIm9wdGlvbnMiXVsiRCJdfVxuXG5SZXR1cm4gdGhlIGxldHRlciBvZiB0aGUgY29ycmVjdCBvcHRpb24uIiIiCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIHJldHVybiAxLjAgaWYgdFsiYW5zd2VyIl0ubG93ZXIoKSA9PSBzdWJtaXNzaW9uLmxvd2VyKCkuc3RyaXAoKSBlbHNlIDAuMAo=)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"question": "House owns his home in City. On the lawn in front of his home and within five feet of the public sidewalk there was a large tree. The roots of the tree caused the sidewalk to buckle severely and become dangerous. An ordinance of City requires adjacent landowners to keep sidewalks in safe condition. House engaged Contractor to repair the sidewalk, leaving it to Contractor to decide how the repair should be made. Contractor dug up the sidewalk, cut back the roots of the tree, and laid a new sidewalk. Two days after House had paid Contractor the agreed price of the repair, the tree fell over onto the street and damaged a parked car belonging to Driver. Driver has asserted claims against House and Contractor, and both defendants admit that cutting the roots caused the tree to fall.If Driver recovers a judgment against House, does House have any recourse against Contractor?",

"options": {

"A": "No, if payment by House was an acceptance of the work.",

"B": "No, because House selected Contractor to do the work.",

"C": "Yes, if the judgment against House was based on vicarious liability.",

"D": "Yes, because House’s conduct was not a factual cause of the harm.",

},

"answer": "C",

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"""{t\["question"\]}\\nA: {t\["options"\]\["A"\]}\\nB: {t\["options"\]\["B"\]}\\nC: {t\["options"\]\["C"\]}\\nD: {t\["options"\]\["D"\]}\\n\\nReturn the letter of the correct option."""

@staticmethod

def score(t: dict, submission: str) -> float | None:

return 1.0 if t\["answer"\].lower() == submission.lower().strip() else 0.0

#### E.3.4 Seed Task 4: Math Word Problem Clips

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAicXVlc3Rpb24iOiAiTmF0YWxpYSBzb2xkIGNsaXBzIHRvIDQ4IG9mIGhlciBmcmllbmRzIGluIEFwcmlsLCBhbmQgdGhlbiBzaGUgc29sZCBoYWxmIGFzIG1hbnkgY2xpcHMgaW4gTWF5LiBIb3cgbWFueSBjbGlwcyBkaWQgTmF0YWxpYSBzZWxsIGFsdG9nZXRoZXIgaW4gQXByaWwgYW5kIE1heT8iLAogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiIiInt0WyJxdWVzdGlvbiJdfSIiIgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIHN1Ym1pc3Npb25fdmFsID0gaW50KHN1Ym1pc3Npb24pCiAgICAgICAgICAgICMgQ29tcHV0ZSB0aGUgY29ycmVjdCBhbnN3ZXIgYmFzZWQgb24gdGhlIGdpdmVuIHJlYXNvbmluZwogICAgICAgICAgICBhcHJpbF9zYWxlcyA9IDQ4CgogICAgICAgICAgICAjIENhbGN1bGF0ZSBNYXkgc2FsZXM6IGhhbGYgb2YgQXByaWwncyBzYWxlcwogICAgICAgICAgICBtYXlfc2FsZXMgPSBhcHJpbF9zYWxlcyAvIDIKCiAgICAgICAgICAgICMgQ2FsY3VsYXRlIHRvdGFsIHNhbGVzIGZvciBib3RoIG1vbnRocwogICAgICAgICAgICB0b3RhbF9zYWxlcyA9IGFwcmlsX3NhbGVzICsgbWF5X3NhbGVzCgogICAgICAgICAgICByZXR1cm4gMS4wIGlmIHN1Ym1pc3Npb25fdmFsID09IHRvdGFsX3NhbGVzIGVsc2UgMC4wCiAgICAgICAgZXhjZXB0IFZhbHVlRXJyb3I6CiAgICAgICAgICAgIHJldHVybiAwLjAK)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?",

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"""{t\["question"\]}"""

@staticmethod

def score(t: dict, submission: str) -> float | None:

try:

submission\_val = int(submission)

\# Compute the correct answer based on the given reasoning

april\_sales = 48

\# Calculate May sales: half of April’s sales

may\_sales = april\_sales / 2

\# Calculate total sales for both months

total\_sales = april\_sales + may\_sales

return 1.0 if submission\_val == total\_sales else 0.0

except ValueError:

return 0.0

### E.4 Examples of Generated Tasks

#### E.4.1 Example 1: Logical Reasoning for Legal Fallacies

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAiYXJndW1lbnQiOiAiSWYgeW91J3JlIG5vdCB3aXRoIHVzLCB5b3UncmUgYWdhaW5zdCB1cy4gVGhlcmVmb3JlLCB5b3UgbXVzdCBzdXBwb3J0IG91ciBwb2xpY2llcy4iLAogICAgICAgICAgICAgICAgImZhbGxhY3kiOiAiRmFsc2UgRGlsZW1tYSIKICAgICAgICAgICAgfSwKICAgICAgICAgICAgIjIiOiB7CiAgICAgICAgICAgICAgICAiYXJndW1lbnQiOiAiSm9obiBzYXlzIHRoYXQgY2xpbWF0ZSBjaGFuZ2UgaXMgcmVhbCwgYnV0IGhlJ3MganVzdCBhIHNjaWVudGlzdCwgc28gaGlzIG9waW5pb24gZG9lc24ndCBjb3VudC4iLAogICAgICAgICAgICAgICAgImZhbGxhY3kiOiAiQWQgSG9taW5lbSIKICAgICAgICAgICAgfQogICAgICAgIH0KCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgZ2V0X2luc3RydWN0aW9ucyh0OiBkaWN0KSAtPiBzdHI6CiAgICAgICAgcmV0dXJuIGYiIiJJZGVudGlmeSB0aGUgbG9naWNhbCBmYWxsYWN5IGluIHRoZSBmb2xsb3dpbmcgYXJndW1lbnQsIGV4cGxhaW4gd2h5IGl0IGlzIGEgZmFsbGFjeSwgY29uc3RydWN0IGEgbG9naWNhbGx5IHNvdW5kIGNvdW50ZXItYXJndW1lbnQgdGhhdCBhZGRyZXNzZXMgdGhlIHNhbWUgaXNzdWUsIGFuZCBjcml0aXF1ZSB0aGUgc3RyZW5ndGggb2YgdGhlIGNvdW50ZXItYXJndW1lbnQuCgpBcmd1bWVudDoge3RbJ2FyZ3VtZW50J119CgpGb3JtYXQgeW91ciByZXNwb25zZSBhcyBmb2xsb3dzOgotIEZhbGxhY3k6IFtOYW1lIG9mIHRoZSBmYWxsYWN5XQotIEV4cGxhbmF0aW9uOiBbRXhwbGFuYXRpb24gb2Ygd2h5IGl0IGlzIGEgZmFsbGFjeV0KLSBDb3VudGVyLUFyZ3VtZW50OiBbTG9naWNhbGx5IHNvdW5kIGNvdW50ZXItYXJndW1lbnRdCi0gQ3JpdGlxdWU6IFtDcml0aXF1ZSBvZiB0aGUgY291bnRlci1hcmd1bWVudCwgaW5jbHVkaW5nIHBvdGVudGlhbCB3ZWFrbmVzc2VzXSIiIgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGV2YWxfd2l0aF9sbG1fanVkZ2UKCiAgICAgICAgaW5zdHJ1Y3Rpb25zID0gVGFza0ZhbWlseS5nZXRfaW5zdHJ1Y3Rpb25zKHQpCgogICAgICAgIGV4cGVjdGVkX2ZhbGxhY3kgPSB0WydmYWxsYWN5J10KICAgICAgICBzdWJtaXR0ZWRfZmFsbGFjeSA9IE5vbmUKICAgICAgICBzdWJtaXR0ZWRfZXhwbGFuYXRpb24gPSBOb25lCiAgICAgICAgc3VibWl0dGVkX2NvdW50ZXJfYXJndW1lbnQgPSBOb25lCiAgICAgICAgc3VibWl0dGVkX2NyaXRpcXVlID0gTm9uZQogICAgICAgIHBhcnRzID0gW3BhcnQuc3RyaXAoKSBmb3IgcGFydCBpbiBzdWJtaXNzaW9uLnN0cmlwKCkuc3BsaXQoJ1xuJyldCiAgICAgICAgZm9yIHBhcnQgaW4gcGFydHM6CiAgICAgICAgICAgIGlmIHBhcnQuc3RhcnRzd2l0aCgnRmFsbGFjeTogJyk6CiAgICAgICAgICAgICAgICBzdWJtaXR0ZWRfZmFsbGFjeSA9IHBhcnRbbGVuKCdGYWxsYWN5OiAnKTpdLnN0cmlwKCkKICAgICAgICAgICAgZWxpZiBwYXJ0LnN0YXJ0c3dpdGgoJ0V4cGxhbmF0aW9uOiAnKToKICAgICAgICAgICAgICAgIHN1Ym1pdHRlZF9leHBsYW5hdGlvbiA9IHBhcnRbbGVuKCdFeHBsYW5hdGlvbjogJyk6XS5zdHJpcCgpCiAgICAgICAgICAgIGVsaWYgcGFydC5zdGFydHN3aXRoKCdDb3VudGVyLUFyZ3VtZW50OiAnKToKICAgICAgICAgICAgICAgIHN1Ym1pdHRlZF9jb3VudGVyX2FyZ3VtZW50ID0gcGFydFtsZW4oJ0NvdW50ZXItQXJndW1lbnQ6ICcpOl0uc3RyaXAoKQogICAgICAgICAgICBlbGlmIHBhcnQuc3RhcnRzd2l0aCgnQ3JpdGlxdWU6ICcpOgogICAgICAgICAgICAgICAgc3VibWl0dGVkX2NyaXRpcXVlID0gcGFydFtsZW4oJ0NyaXRpcXVlOiAnKTpdLnN0cmlwKCkKCiAgICAgICAgaWYgbm90IChzdWJtaXR0ZWRfZmFsbGFjeSBhbmQgc3VibWl0dGVkX2V4cGxhbmF0aW9uIGFuZCBzdWJtaXR0ZWRfY291bnRlcl9hcmd1bWVudCBhbmQgc3VibWl0dGVkX2NyaXRpcXVlKToKICAgICAgICAgICAgcmV0dXJuIDAuMAoKICAgICAgICBjcml0ZXJpYSA9IFsKICAgICAgICAgICAgZiJUaGUgaWRlbnRpZmllZCBmYWxsYWN5IHNob3VsZCBiZSAne2V4cGVjdGVkX2ZhbGxhY3l9Jy4iLAogICAgICAgICAgICAiVGhlIGV4cGxhbmF0aW9uIHNob3VsZCBjb3JyZWN0bHkgZGVzY3JpYmUgd2h5IHRoZSBpZGVudGlmaWVkIGZhbGxhY3kgaXMgYSBmYWxsYWN5LiIsCiAgICAgICAgICAgICJUaGUgY291bnRlci1hcmd1bWVudCBzaG91bGQgYmUgbG9naWNhbGx5IHNvdW5kIGFuZCBhZGRyZXNzIHRoZSBzYW1lIGlzc3VlIGFzIHRoZSBvcmlnaW5hbCBhcmd1bWVudC4iLAogICAgICAgICAgICAiVGhlIGNyaXRpcXVlIHNob3VsZCBpZGVudGlmeSBwb3RlbnRpYWwgd2Vha25lc3NlcyBpbiB0aGUgY291bnRlci1hcmd1bWVudCBhbmQgcHJvdmlkZSBhIGJhbGFuY2VkIGV2YWx1YXRpb24uIgogICAgICAgIF0KICAgICAgICByZXR1cm4gMS4wIGlmIGV2YWxfd2l0aF9sbG1fanVkZ2UoaW5zdHJ1Y3Rpb25zLCBzdWJtaXNzaW9uLCBjcml0ZXJpYSkgZWxzZSAwLjA=)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"argument": "If you’re not with us, you’re against us. Therefore, you must support our policies.",

"fallacy": "False Dilemma"

},

"2": {

"argument": "John says that climate change is real, but he’s just a scientist, so his opinion doesn’t count.",

"fallacy": "Ad Hominem"

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"""Identify the logical fallacy in the following argument, explain why it is a fallacy, construct a logically sound counter-argument that addresses the same issue, and critique the strength of the counter-argument.

Argument: {t\[’argument’\]}

Format your response as follows:

\- Fallacy: \[Name of the fallacy\]

\- Explanation: \[Explanation of why it is a fallacy\]

\- Counter-Argument: \[Logically sound counter-argument\]

\- Critique: \[Critique of the counter-argument, including potential weaknesses\]"""

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import eval\_with\_llm\_judge

instructions = TaskFamily.get\_instructions(t)

expected\_fallacy = t\[’fallacy’\]

submitted\_fallacy = None

submitted\_explanation = None

submitted\_counter\_argument = None

submitted\_critique = None

parts = \[part.strip() for part in submission.strip().split(’\\n’)\]

for part in parts:

if part.startswith(’Fallacy: ’):

submitted\_fallacy = part\[len(’Fallacy: ’):\].strip()

elif part.startswith(’Explanation: ’):

submitted\_explanation = part\[len(’Explanation: ’):\].strip()

elif part.startswith(’Counter-Argument: ’):

submitted\_counter\_argument = part\[len(’Counter-Argument: ’):\].strip()

elif part.startswith(’Critique: ’):

submitted\_critique = part\[len(’Critique: ’):\].strip()

if not (submitted\_fallacy and submitted\_explanation and submitted\_counter\_argument and submitted\_critique):

return 0.0

criteria = \[

f"The identified fallacy should be ’{expected\_fallacy}’.",

"The explanation should correctly describe why the identified fallacy is a fallacy.",

"The counter-argument should be logically sound and address the same issue as the original argument.",

"The critique should identify potential weaknesses in the counter-argument and provide a balanced evaluation."

\]

return 1.0 if eval\_with\_llm\_judge(instructions, submission, criteria) else 0.0

#### E.4.2 Example 2: Logical Understanding of Mutual Knowledge

[⬇](data:text/plain;base64,aW1wb3J0IHJlCgpjbGFzcyBUYXNrRmFtaWx5OgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdldF90YXNrcygpIC0+IGRpY3Rbc3RyLCBkaWN0XToKICAgICAgICByZXR1cm4gewogICAgICAgICAgICAnMSc6IHsKICAgICAgICAgICAgICAgICdldmVudHMnOiBbCiAgICAgICAgICAgICAgICAgICAgJ0FnZW50IEEgcHV0cyBhIHJlZCBiYWxsIGluIGEgYm94LicsCiAgICAgICAgICAgICAgICAgICAgJ0FnZW50IEEgdGVsbHMgQWdlbnQgQiB0aGF0IHRoZSBib3ggY29udGFpbnMgYSByZWQgYmFsbC4nLAogICAgICAgICAgICAgICAgICAgICdBZ2VudCBDIG9wZW5zIHRoZSBib3ggYW5kIHNlZXMgdGhlIHJlZCBiYWxsLicKICAgICAgICAgICAgICAgIF0KICAgICAgICAgICAgfSwKICAgICAgICAgICAgJzInOiB7CiAgICAgICAgICAgICAgICAnZXZlbnRzJzogWwogICAgICAgICAgICAgICAgICAgICdBZ2VudCBBIHB1dHMgYSBibHVlIGJhbGwgaW4gYSBib3guJywKICAgICAgICAgICAgICAgICAgICAnQWdlbnQgQSB0ZWxscyBBZ2VudCBCIHRoYXQgdGhlIGJveCBjb250YWlucyBhIGJsdWUgYmFsbC4nLAogICAgICAgICAgICAgICAgICAgICdBZ2VudCBDIG9wZW5zIHRoZSBib3ggYW5kIHNlZXMgdGhlIGJsdWUgYmFsbC4nCiAgICAgICAgICAgICAgICBdCiAgICAgICAgICAgIH0KICAgICAgICB9CgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdldF9pbnN0cnVjdGlvbnModDogZGljdCkgLT4gc3RyOgogICAgICAgIGV2ZW50cyA9ICdcbicuam9pbih0WydldmVudHMnXSkKICAgICAgICByZXR1cm4gZiIiIkdpdmVuIHRoZSBmb2xsb3dpbmcgc2VxdWVuY2Ugb2YgZXZlbnRzLCBkZXRlcm1pbmUgdGhlIGZpbmFsIGtub3dsZWRnZSBvZiBlYWNoIGFnZW50IChBLCBCLCBDKSBhYm91dCB0aGUgY29udGVudHMgb2YgdGhlIGJveC4KClNlcXVlbmNlIG9mIGV2ZW50czoKe2V2ZW50c30KClByb3ZpZGUgeW91ciBhbnN3ZXIgaW4gdGhlIGZvbGxvd2luZyBmb3JtYXQ6Ci0gKipBZ2VudCBBIGtub3dzKio6IFtXaGF0IEFnZW50IEEga25vd3NdCi0gKipBZ2VudCBCIGtub3dzKio6IFtXaGF0IEFnZW50IEIga25vd3NdCi0gKipBZ2VudCBDIGtub3dzKio6IFtXaGF0IEFnZW50IEMga25vd3NdIiIiCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIGZyb20gc2FuZGJveF9ldmFsX2hlbHBlciBpbXBvcnQgZXZhbF93aXRoX2xsbV9qdWRnZQogICAgICAgIGluc3RydWN0aW9ucyA9IFRhc2tGYW1pbHkuZ2V0X2luc3RydWN0aW9ucyh0KQogICAgICAgIGNyaXRlcmlhID0gWwogICAgICAgICAgICAiVGhlIHJlc3BvbnNlIHNob3VsZCBjbGVhcmx5IHN0YXRlIHRoZSBmaW5hbCBrbm93bGVkZ2Ugb2YgZWFjaCBhZ2VudCAoQSwgQiwgQykuIiwKICAgICAgICAgICAgIlRoZSByZXNwb25zZSBzaG91bGQgaW5kaWNhdGUgdGhhdCBBZ2VudCBBIGtub3dzIHRoZSBib3ggY29udGFpbnMgdGhlIGJhbGwgYW5kIHRoYXQgYm90aCBCIGFuZCBDIGtub3cgdGhpcy4iLAogICAgICAgICAgICAiVGhlIHJlc3BvbnNlIHNob3VsZCBpbmRpY2F0ZSB0aGF0IEFnZW50IEIga25vd3MgdGhlIGJveCBjb250YWlucyB0aGUgYmFsbCBhbmQgdGhhdCBDIGtub3dzIHRoaXMuIiwKICAgICAgICAgICAgIlRoZSByZXNwb25zZSBzaG91bGQgaW5kaWNhdGUgdGhhdCBBZ2VudCBDIGtub3dzIHRoZSBib3ggY29udGFpbnMgdGhlIGJhbGwuIgogICAgICAgIF0KICAgICAgICByZXR1cm4gMS4wIGlmIGV2YWxfd2l0aF9sbG1fanVkZ2UoaW5zdHJ1Y3Rpb25zLCBzdWJtaXNzaW9uLCBjcml0ZXJpYSkgZWxzZSAwLjA=)

import re

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

’1’: {

’events’: \[

’Agent A puts a red ball in a box.’,

’Agent A tells Agent B that the box contains a red ball.’,

’Agent C opens the box and sees the red ball.’

\]

},

’2’: {

’events’: \[

’Agent A puts a blue ball in a box.’,

’Agent A tells Agent B that the box contains a blue ball.’,

’Agent C opens the box and sees the blue ball.’

\]

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

events = ’\\n’.join(t\[’events’\])

return f"""Given the following sequence of events, determine the final knowledge of each agent (A, B, C) about the contents of the box.

Sequence of events:

{events}

Provide your answer in the following format:

\- \*\*Agent A knows\*\*: \[What Agent A knows\]

\- \*\*Agent B knows\*\*: \[What Agent B knows\]

\- \*\*Agent C knows\*\*: \[What Agent C knows\]"""

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import eval\_with\_llm\_judge

instructions = TaskFamily.get\_instructions(t)

criteria = \[

"The response should clearly state the final knowledge of each agent (A, B, C).",

"The response should indicate that Agent A knows the box contains the ball and that both B and C know this.",

"The response should indicate that Agent B knows the box contains the ball and that C knows this.",

"The response should indicate that Agent C knows the box contains the ball."

\]

return 1.0 if eval\_with\_llm\_judge(instructions, submission, criteria) else 0.0

#### E.4.3 Example 3: Calculate Are of Segment of a Circle

[⬇](data:text/plain;base64,aW1wb3J0IG1hdGgKCmNsYXNzIFRhc2tGYW1pbHk6CiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgZ2V0X3Rhc2tzKCkgLT4gZGljdFtzdHIsIGRpY3RdOgogICAgICAgIHJldHVybiB7CiAgICAgICAgICAgICcxJzogeydyYWRpdXMnOiA1LCAnYW5nbGUnOiA2MH0sCiAgICAgICAgICAgICcyJzogeydyYWRpdXMnOiAxMCwgJ2FuZ2xlJzogMTIwfQogICAgICAgIH0KCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgZ2V0X2luc3RydWN0aW9ucyh0OiBkaWN0KSAtPiBzdHI6CiAgICAgICAgcmFkaXVzID0gdFsncmFkaXVzJ10KICAgICAgICBhbmdsZSA9IHRbJ2FuZ2xlJ10KICAgICAgICByZXR1cm4gZidDYWxjdWxhdGUgdGhlIGFyZWEgb2YgYSBzZWdtZW50IG9mIGEgY2lyY2xlIHdpdGggcmFkaXVzIHtyYWRpdXN9IGFuZCBjZW50cmFsIGFuZ2xlIHthbmdsZX0gZGVncmVlcy4gUHJvdmlkZSB0aGUgYW5zd2VyIGFzIGEgZmxvYXRpbmctcG9pbnQgbnVtYmVyIHJvdW5kZWQgdG8gdHdvIGRlY2ltYWwgcGxhY2VzLCB3aXRob3V0IGFueSBhZGRpdGlvbmFsIHRleHQgb3IgZXhwbGFuYXRpb25zLicKCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgc2NvcmUodDogZGljdCwgc3VibWlzc2lvbjogc3RyKSAtPiBmbG9hdCB8IE5vbmU6CiAgICAgICAgdHJ5OgogICAgICAgICAgICByYWRpdXMgPSB0WydyYWRpdXMnXQogICAgICAgICAgICBhbmdsZSA9IHRbJ2FuZ2xlJ10KICAgICAgICAgICAgIyBDb252ZXJ0IGFuZ2xlIHRvIHJhZGlhbnMKICAgICAgICAgICAgYW5nbGVfcmFkID0gbWF0aC5yYWRpYW5zKGFuZ2xlKQogICAgICAgICAgICAjIENhbGN1bGF0ZSB0aGUgYXJlYSBvZiB0aGUgc2VjdG9yCiAgICAgICAgICAgIHNlY3Rvcl9hcmVhID0gKGFuZ2xlIC8gMzYwKSAqIG1hdGgucGkgKiAocmFkaXVzICoqIDIpCiAgICAgICAgICAgICMgQ2FsY3VsYXRlIHRoZSBhcmVhIG9mIHRoZSB0cmlhbmdsZQogICAgICAgICAgICB0cmlhbmdsZV9hcmVhID0gMC41ICogKHJhZGl1cyAqKiAyKSAqIG1hdGguc2luKGFuZ2xlX3JhZCkKICAgICAgICAgICAgIyBDYWxjdWxhdGUgdGhlIGFyZWEgb2YgdGhlIHNlZ21lbnQKICAgICAgICAgICAgc2VnbWVudF9hcmVhID0gc2VjdG9yX2FyZWEgLSB0cmlhbmdsZV9hcmVhCiAgICAgICAgICAgICMgUm91bmQgdGhlIGNvcnJlY3QgYW5zd2VyIHRvIHR3byBkZWNpbWFsIHBsYWNlcwogICAgICAgICAgICBjb3JyZWN0X2Fuc3dlciA9IHJvdW5kKHNlZ21lbnRfYXJlYSwgMikKICAgICAgICAgICAgc3VibWl0dGVkX2Fuc3dlciA9IGZsb2F0KHN1Ym1pc3Npb24uc3RyaXAoKSkKICAgICAgICAgICAgaWYgc3VibWl0dGVkX2Fuc3dlciA9PSBjb3JyZWN0X2Fuc3dlcjoKICAgICAgICAgICAgICAgIHJldHVybiAxLjAKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHJldHVybiAwLjAKICAgICAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICAgICAgcmV0dXJuIDAuMAogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgcHJpbnQoZidFcnJvcjoge2V9JykKICAgICAgICAgICAgcmV0dXJuIDAuMA==)

import math

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

’1’: {’radius’: 5, ’angle’: 60},

’2’: {’radius’: 10, ’angle’: 120}

}

@staticmethod

def get\_instructions(t: dict) -> str:

radius = t\[’radius’\]

angle = t\[’angle’\]

return f’Calculate the area of a segment of a circle with radius {radius} and central angle {angle} degrees. Provide the answer as a floating-point number rounded to two decimal places, without any additional text or explanations.’

@staticmethod

def score(t: dict, submission: str) -> float | None:

try:

radius = t\[’radius’\]

angle = t\[’angle’\]

\# Convert angle to radians

angle\_rad = math.radians(angle)

\# Calculate the area of the sector

sector\_area = (angle / 360) \* math.pi \* (radius \*\* 2)

\# Calculate the area of the triangle

triangle\_area = 0.5 \* (radius \*\* 2) \* math.sin(angle\_rad)

\# Calculate the area of the segment

segment\_area = sector\_area - triangle\_area

\# Round the correct answer to two decimal places

correct\_answer = round(segment\_area, 2)

submitted\_answer = float(submission.strip())

if submitted\_answer == correct\_answer:

return 1.0

else:

return 0.0

except ValueError:

return 0.0

except Exception as e:

print(f’Error: {e}’)

return 0.0

#### E.4.4 Example 4: Prove Algorithmic Correctness of the A\* Algorithm

[⬇](data:text/plain;base64,aW1wb3J0IHN5bXB5CgpjbGFzcyBUYXNrRmFtaWx5OgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdldF90YXNrcygpIC0+IGRpY3Rbc3RyLCBkaWN0XToKICAgICAgICByZXR1cm4gewogICAgICAgICAgICAiMSI6IHsKICAgICAgICAgICAgICAgICJhbGdvcml0aG0iOiAiQSogYWxnb3JpdGhtIGZvciBwYXRoZmluZGluZyB3aXRoIGEgY29uc2lzdGVudCBoZXVyaXN0aWMuIiwKICAgICAgICAgICAgICAgICJ0ZXN0X2Nhc2VzIjogWwogICAgICAgICAgICAgICAgICAgICh7J0EnOiB7J0InOiAxLCAnQyc6IDR9LCAnQic6IHsnQyc6IDJ9LCAnQyc6IHt9fSwgJ3Nob3J0ZXN0X3BhdGgoQSwgQykgPSAzJyksCiAgICAgICAgICAgICAgICAgICAgKHsnQSc6IHsnQic6IDEwLCAnQyc6IDN9LCAnQic6IHsnQyc6IDF9LCAnQyc6IHsnRCc6IDJ9fSwgJ3Nob3J0ZXN0X3BhdGgoQSwgRCkgPSA2JyksCiAgICAgICAgICAgICAgICAgICAgKHsnQSc6IHsnQic6IDEsICdDJzogMTAwfSwgJ0InOiB7J0MnOiAtMTUwfSwgJ0MnOiB7fX0sICdzaG9ydGVzdF9wYXRoKEEsIEMpID0gLTQ5JykKICAgICAgICAgICAgICAgIF0sCiAgICAgICAgICAgICAgICAiZXhwZWN0ZWRfZnVuY19uYW1lIjogInByb3ZlX2Ffc3Rhcl9hbGdvcml0aG0iCiAgICAgICAgICAgIH0sCiAgICAgICAgICAgICIyIjogewogICAgICAgICAgICAgICAgImFsZ29yaXRobSI6ICJGbG95ZC1XYXJzaGFsbCBhbGdvcml0aG0gZm9yIGZpbmRpbmcgdGhlIHNob3J0ZXN0IHBhdGhzIGJldHdlZW4gYWxsIHBhaXJzIG9mIHZlcnRpY2VzIGluIGEgZ3JhcGguIiwKICAgICAgICAgICAgICAgICJ0ZXN0X2Nhc2VzIjogWwogICAgICAgICAgICAgICAgICAgICh7J0EnOiB7J0InOiAxLCAnQyc6IDR9LCAnQic6IHsnQyc6IDJ9LCAnQyc6IHt9fSwgJ3Nob3J0ZXN0X3BhdGhzKEEsIEIsIEMpID0gMycpLAogICAgICAgICAgICAgICAgICAgICh7J0EnOiB7J0InOiAxMCwgJ0MnOiAzfSwgJ0InOiB7J0MnOiAxfSwgJ0MnOiB7J0QnOiAyfX0sICdzaG9ydGVzdF9wYXRocyhBLCBCLCBDLCBEKSA9IDYnKQogICAgICAgICAgICAgICAgXSwKICAgICAgICAgICAgICAgICJleHBlY3RlZF9mdW5jX25hbWUiOiAicHJvdmVfZmxveWRfd2Fyc2hhbGxfYWxnb3JpdGhtIgogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZidHZW5lcmF0ZSBhIGZvcm1hbCBwcm9vZiBmb3IgdGhlIGNvcnJlY3RuZXNzIG9mIHRoZSBmb2xsb3dpbmcgYWxnb3JpdGhtOiB7dFsiYWxnb3JpdGhtIl19LiBZb3VyIHByb29mIHNob3VsZCBiZSBjbGVhciwgbG9naWNhbCwgYW5kIHdlbGwtc3RydWN0dXJlZCwgYW5kIHNob3VsZCBjb3ZlciBib3RoIHRoZSBiYXNlIGNhc2UgYW5kIHRoZSBpbmR1Y3RpdmUgc3RlcCBpZiBhcHBsaWNhYmxlLiBGb3IgdGhlIEEqIGFsZ29yaXRobSwgYWRkcmVzcyB0aGUgcHJvcGVydGllcyBvZiBhIGNvbnNpc3RlbnQgaGV1cmlzdGljIGFuZCBob3cgaXQgZW5zdXJlcyB0aGUgb3B0aW1hbGl0eSBvZiB0aGUgc29sdXRpb24uJwoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGV2YWxfd2l0aF9sbG1fanVkZ2UKICAgICAgICBpbnN0cnVjdGlvbnMgPSBUYXNrRmFtaWx5LmdldF9pbnN0cnVjdGlvbnModCkKICAgICAgICBjcml0ZXJpYSA9IFsKICAgICAgICAgICAgIlRoZSBwcm9vZiBzaG91bGQgYmUgbG9naWNhbGx5IHNvdW5kIGFuZCB3ZWxsLXN0cnVjdHVyZWQuIiwKICAgICAgICAgICAgIlRoZSBwcm9vZiBzaG91bGQgY29ycmVjdGx5IHByb3ZlIHRoZSBjb3JyZWN0bmVzcyBvZiB0aGUgZ2l2ZW4gYWxnb3JpdGhtLiIsCiAgICAgICAgICAgICJUaGUgcHJvb2Ygc2hvdWxkIGNvdmVyIGJvdGggdGhlIGJhc2UgY2FzZSBhbmQgdGhlIGluZHVjdGl2ZSBzdGVwIGlmIGFwcGxpY2FibGUuIiwKICAgICAgICAgICAgIkZvciB0aGUgQSogYWxnb3JpdGhtLCB0aGUgcHJvb2Ygc2hvdWxkIGFkZHJlc3MgdGhlIHByb3BlcnRpZXMgb2YgYSBjb25zaXN0ZW50IGhldXJpc3RpYyBhbmQgaG93IGl0IGVuc3VyZXMgdGhlIG9wdGltYWxpdHkgb2YgdGhlIHNvbHV0aW9uLiIKICAgICAgICBdCiAgICAgICAgcmV0dXJuIDEuMCBpZiBldmFsX3dpdGhfbGxtX2p1ZGdlKGluc3RydWN0aW9ucywgc3VibWlzc2lvbiwgY3JpdGVyaWEpIGVsc2UgMC4w)

import sympy

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"algorithm": "A\* algorithm for pathfinding with a consistent heuristic.",

"test\_cases": \[

({’A’: {’B’: 1, ’C’: 4}, ’B’: {’C’: 2}, ’C’: {}}, ’shortest\_path(A, C) = 3’),

({’A’: {’B’: 10, ’C’: 3}, ’B’: {’C’: 1}, ’C’: {’D’: 2}}, ’shortest\_path(A, D) = 6’),

({’A’: {’B’: 1, ’C’: 100}, ’B’: {’C’: -150}, ’C’: {}}, ’shortest\_path(A, C) = -49’)

\],

"expected\_func\_name": "prove\_a\_star\_algorithm"

},

"2": {

"algorithm": "Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a graph.",

"test\_cases": \[

({’A’: {’B’: 1, ’C’: 4}, ’B’: {’C’: 2}, ’C’: {}}, ’shortest\_paths(A, B, C) = 3’),

({’A’: {’B’: 10, ’C’: 3}, ’B’: {’C’: 1}, ’C’: {’D’: 2}}, ’shortest\_paths(A, B, C, D) = 6’)

\],

"expected\_func\_name": "prove\_floyd\_warshall\_algorithm"

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f’Generate a formal proof for the correctness of the following algorithm: {t\["algorithm"\]}. Your proof should be clear, logical, and well-structured, and should cover both the base case and the inductive step if applicable. For the A\* algorithm, address the properties of a consistent heuristic and how it ensures the optimality of the solution.’

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import eval\_with\_llm\_judge

instructions = TaskFamily.get\_instructions(t)

criteria = \[

"The proof should be logically sound and well-structured.",

"The proof should correctly prove the correctness of the given algorithm.",

"The proof should cover both the base case and the inductive step if applicable.",

"For the A\* algorithm, the proof should address the properties of a consistent heuristic and how it ensures the optimality of the solution."

\]

return 1.0 if eval\_with\_llm\_judge(instructions, submission, criteria) else 0.0

#### E.4.5 Example 5: Synthesize Position Paper on Genetic Engineering

[⬇](data:text/plain;base64,aW1wb3J0IHJlCgoKY2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAiZGViYXRlX3RleHQiOiAiVGhlIGRlYmF0ZSBvdmVyIGdlbmV0aWMgZW5naW5lZXJpbmcgaGFzIGJlY29tZSBpbmNyZWFzaW5nbHkgcG9sYXJpemVkLiBQcm9wb25lbnRzIGFyZ3VlIHRoYXQgZ2VuZXRpYyBlbmdpbmVlcmluZyBjYW4gbGVhZCB0byBzaWduaWZpY2FudCBhZHZhbmNlbWVudHMgaW4gbWVkaWNpbmUsIGFncmljdWx0dXJlLCBhbmQgYmlvdGVjaG5vbG9neS4gVGhleSBoaWdobGlnaHQgdGhlIHBvdGVudGlhbCB0byBjdXJlIGdlbmV0aWMgZGlzZWFzZXMsIGluY3JlYXNlIGNyb3AgeWllbGRzLCBhbmQgZGV2ZWxvcCBuZXcgbWF0ZXJpYWxzLiBDcml0aWNzLCBob3dldmVyLCByYWlzZSBzZXJpb3VzIGV0aGljYWwsIHNvY2lhbCwgYW5kIGVudmlyb25tZW50YWwgY29uY2VybnMuIFRoZXkgYXJndWUgdGhhdCBnZW5ldGljIGVuZ2luZWVyaW5nIGNvdWxkIGxlYWQgdG8gdW5pbnRlbmRlZCBjb25zZXF1ZW5jZXMsIHN1Y2ggYXMgdGhlIGNyZWF0aW9uIG9mICdkZXNpZ25lciBiYWJpZXMnIGFuZCB0aGUgZXhhY2VyYmF0aW9uIG9mIHNvY2lhbCBpbmVxdWFsaXRpZXMuIFRoZXJlIGFyZSBhbHNvIGZlYXJzIGFib3V0IHRoZSBlY29sb2dpY2FsIGltcGFjdCwgaW5jbHVkaW5nIHRoZSBwb3RlbnRpYWwgZm9yIGdlbmV0aWNhbGx5IG1vZGlmaWVkIG9yZ2FuaXNtcyAoR01PcykgdG8gZGlzcnVwdCBuYXR1cmFsIGVjb3N5c3RlbXMuIFRoZSBkZWJhdGUgaXMgZnVydGhlciBjb21wbGljYXRlZCBieSB0aGUgbGFjayBvZiBjb21wcmVoZW5zaXZlIHJlZ3VsYXRvcnkgZnJhbWV3b3JrcyBhbmQgdGhlIG5lZWQgZm9yIHB1YmxpYyBlbmdhZ2VtZW50IGFuZCB0cmFuc3BhcmVuY3kuIEJvdGggc2lkZXMgYWNrbm93bGVkZ2UgdGhlIGltcG9ydGFuY2Ugb2YgYmFsYW5jaW5nIGlubm92YXRpb24gd2l0aCByZXNwb25zaWJsZSBnb3Zlcm5hbmNlLCBidXQgdGhleSBkaWZmZXIgb24gdGhlIGFwcHJvcHJpYXRlIGJhbGFuY2UgYW5kIHRoZSByb2xlIG9mIGdvdmVybm1lbnQgaW4gb3ZlcnNlZWluZyBnZW5ldGljIGVuZ2luZWVyaW5nLiIKICAgICAgICAgICAgfSwKICAgICAgICAgICAgIjIiOiB7CiAgICAgICAgICAgICAgICAiZGViYXRlX3RleHQiOiAiVGhlIGV0aGljYWwgaW1wbGljYXRpb25zIG9mIGdlbmV0aWMgZW5naW5lZXJpbmcgYXJlIGEgc3ViamVjdCBvZiBpbnRlbnNlIGRlYmF0ZS4gU3VwcG9ydGVycyBhcmd1ZSB0aGF0IGdlbmV0aWMgZW5naW5lZXJpbmcgY2FuIGFsbGV2aWF0ZSBzdWZmZXJpbmcgYnkgdHJlYXRpbmcgZ2VuZXRpYyBkaXNvcmRlcnMgYW5kIGltcHJvdmluZyBxdWFsaXR5IG9mIGxpZmUuIFRoZXkgYWxzbyBjb250ZW5kIHRoYXQgaXQgY2FuIGNvbnRyaWJ1dGUgdG8gZ2xvYmFsIGZvb2Qgc2VjdXJpdHkgYnkgZGV2ZWxvcGluZyBjcm9wcyB0aGF0IGFyZSByZXNpc3RhbnQgdG8gcGVzdHMgYW5kIGNsaW1hdGUgY2hhbmdlLiBPcHBvbmVudHMsIGhvd2V2ZXIsIHdhcm4gb2YgdGhlIHBvdGVudGlhbCBmb3IgZ2VuZXRpYyBlbmdpbmVlcmluZyB0byBiZSB1c2VkIGZvciBub24tdGhlcmFwZXV0aWMgcHVycG9zZXMsIHN1Y2ggYXMgZW5oYW5jaW5nIHBoeXNpY2FsIG9yIGNvZ25pdGl2ZSB0cmFpdHMuIFRoZXkgcmFpc2UgY29uY2VybnMgYWJvdXQgdGhlIGNvbW1vZGlmaWNhdGlvbiBvZiBodW1hbiBsaWZlIGFuZCB0aGUgcG90ZW50aWFsIGZvciBnZW5ldGljIGRpc2NyaW1pbmF0aW9uLiBFdGhpY2lzdHMgYWxzbyBkZWJhdGUgdGhlIG1vcmFsIHN0YXR1cyBvZiBnZW5ldGljYWxseSBtb2RpZmllZCBvcmdhbmlzbXMgYW5kIHRoZSByaWdodHMgb2YgZnV0dXJlIGdlbmVyYXRpb25zLiBUaGUgZGViYXRlIGlzIGZ1cnRoZXIgY29tcGxpY2F0ZWQgYnkgdGhlIGxhY2sgb2YgaW50ZXJuYXRpb25hbCBjb25zZW5zdXMgYW5kIHRoZSB2YXJ5aW5nIGN1bHR1cmFsIGFuZCByZWxpZ2lvdXMgcGVyc3BlY3RpdmVzIG9uIGdlbmV0aWMgZW5naW5lZXJpbmcuIgogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiJHaXZlbiB0aGUgZm9sbG93aW5nIGRlYmF0ZSBvbiBnZW5ldGljIGVuZ2luZWVyaW5nLCBzdW1tYXJpemUgdGhlIGRlYmF0ZSwgZXZhbHVhdGUgdGhlIGtleSBhcmd1bWVudHMgYW5kIGNvdW50ZXJhcmd1bWVudHMsIGFuZCB0aGVuIHN5bnRoZXNpemUgYSBwb3NpdGlvbiBwYXBlciB0aGF0IHRha2VzIGEgY2xlYXIgc3RhbmNlIG9uIHRoZSBpc3N1ZS4gVGhlIHBvc2l0aW9uIHBhcGVyIHNob3VsZCBiZSBzdXBwb3J0ZWQgYnkgZXZpZGVuY2UgZnJvbSB0aGUgZGViYXRlIGFuZCBhdCBsZWFzdCB0aHJlZSBwZWVyLXJldmlld2VkIHNvdXJjZXMsIGFuZCBzaG91bGQgbWFpbnRhaW4gY29oZXJlbmNlIGFuZCBsb2dpY2FsIGZsb3c6XG5cbnt0WydkZWJhdGVfdGV4dCddfVxuXG5TdW1tYXJ5IGFuZCBFdmFsdWF0aW9uOlxuXG5Qb3NpdGlvbiBQYXBlcjogSW5jb3Jwb3JhdGUgYXQgbGVhc3QgdGhyZWUgcGVlci1yZXZpZXdlZCBzb3VyY2VzIHRvIHN1cHBvcnQgeW91ciBhcmd1bWVudHMuIEZvciBleGFtcGxlLCB5b3UgbWlnaHQgcmVmZXJlbmNlIHN0dWRpZXMgb24gdGhlIGVmZmVjdGl2ZW5lc3Mgb2YgZ2VuZSB0aGVyYXB5IG9yIHRoZSBlbnZpcm9ubWVudGFsIGltcGFjdCBvZiBHTU9zLiIKCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgc2NvcmUodDogZGljdCwgc3VibWlzc2lvbjogc3RyKSAtPiBmbG9hdCB8IE5vbmU6CiAgICAgICAgZnJvbSBzYW5kYm94X2V2YWxfaGVscGVyIGltcG9ydCBldmFsX3dpdGhfbGxtX2p1ZGdlCiAgICAgICAgaW5zdHJ1Y3Rpb25zID0gVGFza0ZhbWlseS5nZXRfaW5zdHJ1Y3Rpb25zKHQpCiAgICAgICAgY3JpdGVyaWEgPSBbCiAgICAgICAgICAgICJUaGUgc3VtbWFyeSBzaG91bGQgY2FwdHVyZSB0aGUgbWFpbiBwb2ludHMgYW5kIGtleSBhcmd1bWVudHMuIiwKICAgICAgICAgICAgIlRoZSBzdW1tYXJ5IHNob3VsZCBpbmNsdWRlIHJlbGV2YW50IGNvdW50ZXJhcmd1bWVudHMuIiwKICAgICAgICAgICAgIlRoZSBzdW1tYXJ5IHNob3VsZCBwcm92aWRlIGEgY3JpdGljYWwgYW5hbHlzaXMgb2YgZXRoaWNhbCwgc29jaWFsLCBhbmQgc2NpZW50aWZpYyBjb25zaWRlcmF0aW9ucy4iLAogICAgICAgICAgICAiVGhlIHN1bW1hcnkgc2hvdWxkIG1haW50YWluIGNvaGVyZW5jZSBhbmQgbG9naWNhbCBmbG93LiIsCiAgICAgICAgICAgICJUaGUgc3VtbWFyeSBzaG91bGQgbm90IGNvbnRhaW4gdW5uZWNlc3NhcnkgZGV0YWlscyBvciB0YW5nZW50cy4iLAogICAgICAgICAgICAiVGhlIHN1bW1hcnkgc2hvdWxkIGFjY3VyYXRlbHkgcmVmbGVjdCB0aGUgY29udGVudCBvZiB0aGUgZGViYXRlLiIsCiAgICAgICAgICAgICJUaGUgcG9zaXRpb24gcGFwZXIgc2hvdWxkIHRha2UgYSBjbGVhciBzdGFuY2Ugb24gdGhlIGlzc3VlLiIsCiAgICAgICAgICAgICJUaGUgcG9zaXRpb24gcGFwZXIgc2hvdWxkIGJlIHN1cHBvcnRlZCBieSBldmlkZW5jZSBmcm9tIHRoZSBkZWJhdGUgYW5kIGF0IGxlYXN0IHRocmVlIHBlZXItcmV2aWV3ZWQgc291cmNlcy4iLAogICAgICAgICAgICAiVGhlIHBvc2l0aW9uIHBhcGVyIHNob3VsZCBtYWludGFpbiBjb2hlcmVuY2UgYW5kIGxvZ2ljYWwgZmxvdy4iLAogICAgICAgICAgICAiVGhlIHBvc2l0aW9uIHBhcGVyIHNob3VsZCBhZGRyZXNzIHBvdGVudGlhbCBjb3VudGVyYXJndW1lbnRzIGFuZCBwcm92aWRlIGEgd2VsbC1yb3VuZGVkIHZpZXcuIgogICAgICAgIF0KICAgICAgICByZXR1cm4gMS4wIGlmIGV2YWxfd2l0aF9sbG1fanVkZ2UoaW5zdHJ1Y3Rpb25zLCBzdWJtaXNzaW9uLCBjcml0ZXJpYSkgZWxzZSAwLjA=)

import re

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"debate\_text": "The debate over genetic engineering has become increasingly polarized. Proponents argue that genetic engineering can lead to significant advancements in medicine, agriculture, and biotechnology. They highlight the potential to cure genetic diseases, increase crop yields, and develop new materials. Critics, however, raise serious ethical, social, and environmental concerns. They argue that genetic engineering could lead to unintended consequences, such as the creation of ’designer babies’ and the exacerbation of social inequalities. There are also fears about the ecological impact, including the potential for genetically modified organisms (GMOs) to disrupt natural ecosystems. The debate is further complicated by the lack of comprehensive regulatory frameworks and the need for public engagement and transparency. Both sides acknowledge the importance of balancing innovation with responsible governance, but they differ on the appropriate balance and the role of government in overseeing genetic engineering."

},

"2": {

"debate\_text": "The ethical implications of genetic engineering are a subject of intense debate. Supporters argue that genetic engineering can alleviate suffering by treating genetic disorders and improving quality of life. They also contend that it can contribute to global food security by developing crops that are resistant to pests and climate change. Opponents, however, warn of the potential for genetic engineering to be used for non-therapeutic purposes, such as enhancing physical or cognitive traits. They raise concerns about the commodification of human life and the potential for genetic discrimination. Ethicists also debate the moral status of genetically modified organisms and the rights of future generations. The debate is further complicated by the lack of international consensus and the varying cultural and religious perspectives on genetic engineering."

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"Given the following debate on genetic engineering, summarize the debate, evaluate the key arguments and counterarguments, and then synthesize a position paper that takes a clear stance on the issue. The position paper should be supported by evidence from the debate and at least three peer-reviewed sources, and should maintain coherence and logical flow:\\n\\n{t\[’debate\_text’\]}\\n\\nSummary and Evaluation:\\n\\nPosition Paper: Incorporate at least three peer-reviewed sources to support your arguments. For example, you might reference studies on the effectiveness of gene therapy or the environmental impact of GMOs."

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import eval\_with\_llm\_judge

instructions = TaskFamily.get\_instructions(t)

criteria = \[

"The summary should capture the main points and key arguments.",

"The summary should include relevant counterarguments.",

"The summary should provide a critical analysis of ethical, social, and scientific considerations.",

"The summary should maintain coherence and logical flow.",

"The summary should not contain unnecessary details or tangents.",

"The summary should accurately reflect the content of the debate.",

"The position paper should take a clear stance on the issue.",

"The position paper should be supported by evidence from the debate and at least three peer-reviewed sources.",

"The position paper should maintain coherence and logical flow.",

"The position paper should address potential counterarguments and provide a well-rounded view."

\]

return 1.0 if eval\_with\_llm\_judge(instructions, submission, criteria) else 0.0

#### E.4.6 Example 6: Simplify Algebraic Expression

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAiZXhwcmVzc2lvbiI6ICIoeCArIDMpICogKHggLSAzKSIKICAgICAgICAgICAgfSwKICAgICAgICAgICAgIjIiOiB7CiAgICAgICAgICAgICAgICAiZXhwcmVzc2lvbiI6ICIyICogKHggKyA0KSAtIDMgKiAoeCAtIDIpIgogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiJTaW1wbGlmeSB0aGUgZm9sbG93aW5nIGFsZ2VicmFpYyBleHByZXNzaW9uOiB7dFsnZXhwcmVzc2lvbiddfS4gUHJvdmlkZSB5b3VyIGFuc3dlciBpbiB0aGUgc2ltcGxlc3QgZm9ybSwgd2l0aG91dCBhbnkgYWRkaXRpb25hbCBleHBsYW5hdGlvbiBvciBzdGVwcy4iCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIGZyb20gc3ltcHkgaW1wb3J0IHN5bWJvbHMsIHNpbXBsaWZ5CiAgICAgICAgeCA9IHN5bWJvbHMoJ3gnKQogICAgICAgIGNvcnJlY3RfYW5zd2VyID0gc2ltcGxpZnkodFsnZXhwcmVzc2lvbiddKQogICAgICAgIHRyeToKICAgICAgICAgICAgIyBSZW1vdmUgTGFUZVggZGVsaW1pdGVycyBpZiBwcmVzZW50CiAgICAgICAgICAgIHN1Ym1pc3Npb24gPSBzdWJtaXNzaW9uLnJlcGxhY2UoJ1xcJywgJycpLnN0cmlwKCkKICAgICAgICAgICAgIyBTaW1wbGlmeSB0aGUgc3VibWl0dGVkIGFuc3dlcgogICAgICAgICAgICBzdWJtaXR0ZWRfYW5zd2VyID0gc2ltcGxpZnkoc3VibWlzc2lvbikKICAgICAgICAgICAgaWYgc3VibWl0dGVkX2Fuc3dlciA9PSBjb3JyZWN0X2Fuc3dlcjoKICAgICAgICAgICAgICAgIHJldHVybiAxLjAKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHJldHVybiAwLjAKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICByZXR1cm4gMC4w)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"expression": "(x + 3) \* (x - 3)"

},

"2": {

"expression": "2 \* (x + 4) - 3 \* (x - 2)"

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"Simplify the following algebraic expression: {t\[’expression’\]}. Provide your answer in the simplest form, without any additional explanation or steps."

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sympy import symbols, simplify

x = symbols(’x’)

correct\_answer = simplify(t\[’expression’\])

try:

\# Remove LaTeX delimiters if present

submission = submission.replace(’\\\\’, ’’).strip()

\# Simplify the submitted answer

submitted\_answer = simplify(submission)

if submitted\_answer == correct\_answer:

return 1.0

else:

return 0.0

except Exception:

return 0.0

#### E.4.7 Example 7: Implement Function to Generate Fibonacci Sequence

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgJzEnOiB7J25fdGVybXMnOiAxMH0sCiAgICAgICAgICAgICcyJzogeyduX3Rlcm1zJzogMTV9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZidXcml0ZSBhIGZ1bmN0aW9uIGNhbGxlZCBgZmlib25hY2NpX3NlcXVlbmNlYCB0aGF0IHRha2VzIGFuIGludGVnZXIgYG5fdGVybXNgIGFzIGlucHV0IGFuZCByZXR1cm5zIGEgbGlzdCBjb250YWluaW5nIHRoZSBGaWJvbmFjY2kgc2VxdWVuY2UgdXAgdG8gdGhlIHNwZWNpZmllZCBudW1iZXIgb2YgdGVybXMuIFRoZSBmdW5jdGlvbiBzaG91bGQgYmUgaW1wbGVtZW50ZWQgdXNpbmcgYSBsb29wIG9yIHJlY3Vyc2lvbi4gRm9yIGV4YW1wbGUsIGlmIGBuX3Rlcm1zYCBpcyA1LCB0aGUgZnVuY3Rpb24gc2hvdWxkIHJldHVybiBbMCwgMSwgMSwgMiwgM10uJwoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGdldF9mdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlCgogICAgICAgICMgRnVuY3Rpb24gdG8gZ2VuZXJhdGUgdGhlIGV4cGVjdGVkIEZpYm9uYWNjaSBzZXF1ZW5jZQogICAgICAgIGRlZiBnZW5lcmF0ZV9maWJvbmFjY2kobl90ZXJtcyk6CiAgICAgICAgICAgIGlmIG5fdGVybXMgPD0gMDoKICAgICAgICAgICAgICAgIHJldHVybiBbXQogICAgICAgICAgICBlbGlmIG5fdGVybXMgPT0gMToKICAgICAgICAgICAgICAgIHJldHVybiBbMF0KICAgICAgICAgICAgZWxpZiBuX3Rlcm1zID09IDI6CiAgICAgICAgICAgICAgICByZXR1cm4gWzAsIDFdCiAgICAgICAgICAgIGZpYl9zZXF1ZW5jZSA9IFswLCAxXQogICAgICAgICAgICBmb3IgXyBpbiByYW5nZSgyLCBuX3Rlcm1zKToKICAgICAgICAgICAgICAgIGZpYl9zZXF1ZW5jZS5hcHBlbmQoZmliX3NlcXVlbmNlWy0xXSArIGZpYl9zZXF1ZW5jZVstMl0pCiAgICAgICAgICAgIHJldHVybiBmaWJfc2VxdWVuY2UKCiAgICAgICAgIyBUZXN0IGNhc2VzIGZyb20gZ2V0X3Rhc2tzCiAgICAgICAgbl90ZXJtcyA9IHRbJ25fdGVybXMnXQogICAgICAgIGV4cGVjdGVkX291dHB1dCA9IGdlbmVyYXRlX2ZpYm9uYWNjaShuX3Rlcm1zKQoKICAgICAgICAjIEdldCBmdW5jdGlvbiBuYW1lIHRvIGNhbGxhYmxlIG1hcHBpbmcKICAgICAgICBmdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlID0gZ2V0X2Z1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUoCiAgICAgICAgICAgIHN1Ym1pc3Npb24KICAgICAgICApCgogICAgICAgICMgUnVuIHRlc3QgY2FzZQogICAgICAgIHRyeToKICAgICAgICAgICAgIyBFeGVjdXRlIHRoZSBmdW5jdGlvbgogICAgICAgICAgICBzdWJtaXNzaW9uX3Jlc3VsdCA9IGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGVbJ2ZpYm9uYWNjaV9zZXF1ZW5jZSddKG5fdGVybXMpCgogICAgICAgICAgICAjIENvbXBhcmUgd2l0aCBleHBlY3RlZCBvdXRwdXQKICAgICAgICAgICAgaWYgc3VibWlzc2lvbl9yZXN1bHQgPT0gZXhwZWN0ZWRfb3V0cHV0OgogICAgICAgICAgICAgICAgcmV0dXJuIDEuMAoKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAjIElmIGZ1bmN0aW9uIGZhaWxzIG9uIGEgdGVzdCBjYXNlLCByZXR1cm4gMC4wCiAgICAgICAgICAgIHJldHVybiAwLjA=)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

’1’: {’n\_terms’: 10},

’2’: {’n\_terms’: 15}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f’Write a function called ‘fibonacci\_sequence‘ that takes an integer ‘n\_terms‘ as input and returns a list containing the Fibonacci sequence up to the specified number of terms. The function should be implemented using a loop or recursion. For example, if ‘n\_terms‘ is 5, the function should return \[0, 1, 1, 2, 3\].’

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import get\_function\_name\_to\_callable

\# Function to generate the expected Fibonacci sequence

def generate\_fibonacci(n\_terms):

if n\_terms <= 0:

return \[\]

elif n\_terms == 1:

return \[0\]

elif n\_terms == 2:

return \[0, 1\]

fib\_sequence = \[0, 1\]

for \_ in range(2, n\_terms):

fib\_sequence.append(fib\_sequence\[-1\] + fib\_sequence\[-2\])

return fib\_sequence

\# Test cases from get\_tasks

n\_terms = t\[’n\_terms’\]

expected\_output = generate\_fibonacci(n\_terms)

\# Get function name to callable mapping

function\_name\_to\_callable = get\_function\_name\_to\_callable(

submission

)

\# Run test case

try:

\# Execute the function

submission\_result = function\_name\_to\_callable\[’fibonacci\_sequence’\](n\_terms)

\# Compare with expected output

if submission\_result == expected\_output:

return 1.0

except Exception:

\# If function fails on a test case, return 0.0

return 0.0

#### E.4.8 Example 8: Implement Function to Compute Longest Common Subsequence

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgJzEnOiB7CiAgICAgICAgICAgICAgICAncHJvbXB0JzogJ0NvbXBsZXRlIHRoZSBmdW5jdGlvbiBgbG9uZ2VzdF9jb21tb25fc3Vic2VxdWVuY2VgIHRoYXQgdGFrZXMgdHdvIGxpc3RzIG9mIGNoYXJhY3RlcnMgYW5kIHJldHVybnMgdGhlIGxvbmdlc3QgY29tbW9uIHN1YnNlcXVlbmNlIChMQ1MpLicsCiAgICAgICAgICAgICAgICAndGVzdF9jYXNlcyc6IFsoWydBJywgJ0InLCAnQycsICdEJywgJ0UnXSwgWydBJywgJ0InLCAnRCcsICdGJywgJ0cnXSwgWydBJywgJ0InLCAnRCddKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIChbJ0EnLCAnQicsICdDJ10sIFsnWCcsICdZJywgJ1onXSwgW10pLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKFsnQScsICdCJywgJ0MnLCAnQicsICdEJywgJ0EnLCAnQiddLCBbJ0InLCAnRCcsICdDJywgJ0EnLCAnQicsICdBJ10sIFsnQicsICdDJywgJ0InLCAnQSddKV0sCiAgICAgICAgICAgICAgICAnZXhwZWN0ZWRfZnVuY19uYW1lJzogJ2xvbmdlc3RfY29tbW9uX3N1YnNlcXVlbmNlJwogICAgICAgICAgICB9LAogICAgICAgICAgICAnMic6IHsKICAgICAgICAgICAgICAgICdwcm9tcHQnOiAnQ29tcGxldGUgdGhlIGZ1bmN0aW9uIGBsb25nZXN0X2NvbW1vbl9zdWJzZXF1ZW5jZWAgdGhhdCB0YWtlcyB0d28gbGlzdHMgb2YgY2hhcmFjdGVycyBhbmQgcmV0dXJucyB0aGUgbG9uZ2VzdCBjb21tb24gc3Vic2VxdWVuY2UgKExDUykuJywKICAgICAgICAgICAgICAgICd0ZXN0X2Nhc2VzJzogWyhbJ0EnLCAnQicsICdDJywgJ0QnLCAnRSddLCBbJ0EnLCAnQicsICdEJywgJ0YnLCAnRyddLCBbJ0EnLCAnQicsICdEJ10pLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKFsnQScsICdCJywgJ0MnLCAnRCcsICdFJ10sIFsnRScsICdEJywgJ0MnLCAnQicsICdBJ10sIFsnQScsICdCJywgJ0MnLCAnRCcsICdFJ10pLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKFsnQScsICdCJywgJ0MnLCAnQicsICdEJywgJ0EnLCAnQiddLCBbJ0InLCAnRCcsICdDJywgJ0EnLCAnQicsICdBJ10sIFsnQicsICdDJywgJ0InLCAnQSddKV0sCiAgICAgICAgICAgICAgICAnZXhwZWN0ZWRfZnVuY19uYW1lJzogJ2xvbmdlc3RfY29tbW9uX3N1YnNlcXVlbmNlJwogICAgICAgICAgICB9CiAgICAgICAgfQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICByZXR1cm4gZiJDb21wbGV0ZSB0aGUgZm9sbG93aW5nIFB5dGhvbiBmdW5jdGlvbjpcblxue3RbJ3Byb21wdCddfVxuIgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzY29yZSh0OiBkaWN0LCBzdWJtaXNzaW9uOiBzdHIpIC0+IGZsb2F0IHwgTm9uZToKICAgICAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGdldF9mdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlCgogICAgICAgICMgVGVzdCBjYXNlcyBmcm9tIGdldF90YXNrcwogICAgICAgIHRlc3RfY2FzZXMgPSB0Wyd0ZXN0X2Nhc2VzJ10KCiAgICAgICAgIyBHZXQgZnVuY3Rpb24gbmFtZSB0byBjYWxsYWJsZSBtYXBwaW5nCiAgICAgICAgZnVuY3Rpb25fbmFtZV90b19jYWxsYWJsZSA9IGdldF9mdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlKAogICAgICAgICAgICBzdWJtaXNzaW9uCiAgICAgICAgKQoKICAgICAgICAjIFJ1biB0ZXN0IGNhc2VzCiAgICAgICAgZm9yIHNlcTEsIHNlcTIsIGV4cGVjdGVkX291dHB1dCBpbiB0ZXN0X2Nhc2VzOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAjIEV4ZWN1dGUgdGhlIGZ1bmN0aW9uCiAgICAgICAgICAgICAgICBzdWJtaXNzaW9uX3Jlc3VsdCA9IGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGVbdFsnZXhwZWN0ZWRfZnVuY19uYW1lJ11dKHNlcTEsIHNlcTIpCgogICAgICAgICAgICAgICAgIyBDb21wYXJlIHdpdGggZXhwZWN0ZWQgb3V0cHV0CiAgICAgICAgICAgICAgICBpZiBzdWJtaXNzaW9uX3Jlc3VsdCAhPSBleHBlY3RlZF9vdXRwdXQ6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIDAuMAoKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgICMgSWYgZnVuY3Rpb24gZmFpbHMgb24gYSB0ZXN0IGNhc2UsIHJldHVybiAwLjAKICAgICAgICAgICAgICAgIHJldHVybiAwLjAKCiAgICAgICAgcmV0dXJuIDEuMA==)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

’1’: {

’prompt’: ’Complete the function ‘longest\_common\_subsequence‘ that takes two lists of characters and returns the longest common subsequence (LCS).’,

’test\_cases’: \[(\[’A’, ’B’, ’C’, ’D’, ’E’\], \[’A’, ’B’, ’D’, ’F’, ’G’\], \[’A’, ’B’, ’D’\]),

(\[’A’, ’B’, ’C’\], \[’X’, ’Y’, ’Z’\], \[\]),

(\[’A’, ’B’, ’C’, ’B’, ’D’, ’A’, ’B’\], \[’B’, ’D’, ’C’, ’A’, ’B’, ’A’\], \[’B’, ’C’, ’B’, ’A’\])\],

’expected\_func\_name’: ’longest\_common\_subsequence’

},

’2’: {

’prompt’: ’Complete the function ‘longest\_common\_subsequence‘ that takes two lists of characters and returns the longest common subsequence (LCS).’,

’test\_cases’: \[(\[’A’, ’B’, ’C’, ’D’, ’E’\], \[’A’, ’B’, ’D’, ’F’, ’G’\], \[’A’, ’B’, ’D’\]),

(\[’A’, ’B’, ’C’, ’D’, ’E’\], \[’E’, ’D’, ’C’, ’B’, ’A’\], \[’A’, ’B’, ’C’, ’D’, ’E’\]),

(\[’A’, ’B’, ’C’, ’B’, ’D’, ’A’, ’B’\], \[’B’, ’D’, ’C’, ’A’, ’B’, ’A’\], \[’B’, ’C’, ’B’, ’A’\])\],

’expected\_func\_name’: ’longest\_common\_subsequence’

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"Complete the following Python function:\\n\\n{t\[’prompt’\]}\\n"

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import get\_function\_name\_to\_callable

\# Test cases from get\_tasks

test\_cases = t\[’test\_cases’\]

\# Get function name to callable mapping

function\_name\_to\_callable = get\_function\_name\_to\_callable(

submission

)

\# Run test cases

for seq1, seq2, expected\_output in test\_cases:

try:

\# Execute the function

submission\_result = function\_name\_to\_callable\[t\[’expected\_func\_name’\]\](seq1, seq2)

\# Compare with expected output

if submission\_result!= expected\_output:

return 0.0

except Exception:

\# If function fails on a test case, return 0.0

return 0.0

return 1.0

#### E.4.9 Example 9: Calculate Free-fall Time

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAiaGVpZ2h0IjogNDUsCiAgICAgICAgICAgICAgICAiZ3Jhdml0eSI6IDkuODEsCiAgICAgICAgICAgICAgICAiZXhwZWN0ZWRfdGltZSI6IDMuMDMKICAgICAgICAgICAgfSwKICAgICAgICAgICAgIjIiOiB7CiAgICAgICAgICAgICAgICAiaGVpZ2h0IjogMTAwLAogICAgICAgICAgICAgICAgImdyYXZpdHkiOiA5LjgxLAogICAgICAgICAgICAgICAgImV4cGVjdGVkX3RpbWUiOiA0LjUyCiAgICAgICAgICAgIH0KICAgICAgICB9CgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdldF9pbnN0cnVjdGlvbnModDogZGljdCkgLT4gc3RyOgogICAgICAgIHJldHVybiBmIkNhbGN1bGF0ZSB0aGUgdGltZSBpdCB0YWtlcyBmb3IgYW4gb2JqZWN0IHRvIGZhbGwgZnJvbSBhIGhlaWdodCBvZiB7dFsnaGVpZ2h0J119IG1ldGVycy4gVXNlIHRoZSBmb3JtdWxhIGZvciBmcmVlLWZhbGwgbW90aW9uIHVuZGVyIGdyYXZpdHk6IFxudCA9IHNxcnQoMiAqIGggLyBnKSwgd2hlcmUgaCBpcyB0aGUgaGVpZ2h0IGFuZCBnIGlzIHRoZSBhY2NlbGVyYXRpb24gZHVlIHRvIGdyYXZpdHkgKDkuODEgbS9zXjIpLiBcblJvdW5kIHlvdXIgYW5zd2VyIHRvIHR3byBkZWNpbWFsIHBsYWNlcy4iCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIGltcG9ydCBtYXRoCiAgICAgICAgIyBDYWxjdWxhdGUgdGhlIGV4cGVjdGVkIHRpbWUgdXNpbmcgdGhlIGZyZWUtZmFsbCBmb3JtdWxhCiAgICAgICAgZXhwZWN0ZWRfdGltZSA9IG1hdGguc3FydCgyICogdFsnaGVpZ2h0J10gLyB0WydncmF2aXR5J10pCiAgICAgICAgZXhwZWN0ZWRfdGltZV9yb3VuZGVkID0gcm91bmQoZXhwZWN0ZWRfdGltZSwgMikKICAgICAgICB0cnk6CiAgICAgICAgICAgICMgQ29udmVydCB0aGUgc3VibWlzc2lvbiB0byBhIGZsb2F0CiAgICAgICAgICAgIHN1Ym1pc3Npb25fdGltZSA9IGZsb2F0KHN1Ym1pc3Npb24uc3RyaXAoKSkKICAgICAgICAgICAgIyBDaGVjayBpZiB0aGUgc3VibWlzc2lvbiBtYXRjaGVzIHRoZSBleHBlY3RlZCB0aW1lIHdpdGggYSBzbWFsbCB0b2xlcmFuY2UKICAgICAgICAgICAgaWYgYWJzKHN1Ym1pc3Npb25fdGltZSAtIGV4cGVjdGVkX3RpbWVfcm91bmRlZCkgPCAwLjA1OgogICAgICAgICAgICAgICAgcmV0dXJuIDEuMAogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcmV0dXJuIDAuMAogICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgICAgICByZXR1cm4gMC4w)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"height": 45,

"gravity": 9.81,

"expected\_time": 3.03

},

"2": {

"height": 100,

"gravity": 9.81,

"expected\_time": 4.52

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return f"Calculate the time it takes for an object to fall from a height of {t\[’height’\]} meters. Use the formula for free-fall motion under gravity: \\nt = sqrt(2 \* h / g), where h is the height and g is the acceleration due to gravity (9.81 m/s^2). \\nRound your answer to two decimal places."

@staticmethod

def score(t: dict, submission: str) -> float | None:

import math

\# Calculate the expected time using the free-fall formula

expected\_time = math.sqrt(2 \* t\[’height’\] / t\[’gravity’\])

expected\_time\_rounded = round(expected\_time, 2)

try:

\# Convert the submission to a float

submission\_time = float(submission.strip())

\# Check if the submission matches the expected time with a small tolerance

if abs(submission\_time - expected\_time\_rounded) < 0.05:

return 1.0

else:

return 0.0

except ValueError:

return 0.0

#### E.4.10 Example 10: Provide Explanation of Chemical Interactions

[⬇](data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgIjEiOiB7CiAgICAgICAgICAgICAgICAicHJvbXB0IjogIlByb3ZpZGUgYSBkZXRhaWxlZCBleHBsYW5hdGlvbiBvZiB0aGUgY2hlbWljYWwgaW50ZXJhY3Rpb25zIGluIHdhdGVyLCBpbmNsdWRpbmc6XG4xLiBCb25kIHR5cGVcbjIuIEVsZWN0cm9uZWdhdGl2aXR5IGRpZmZlcmVuY2VzXG4zLiBNb2xlY3VsYXIgZ2VvbWV0cnlcbjQuIEludGVybW9sZWN1bGFyIGludGVyYWN0aW9uc1xuNS4gUG90ZW50aWFsIHJlYWN0aW9uc1xuIiwKICAgICAgICAgICAgICAgICJ0ZXN0X2Nhc2VzIjogWwogICAgICAgICAgICAgICAgICAgICgiIiwgIiIpCiAgICAgICAgICAgICAgICBdLAogICAgICAgICAgICAgICAgImV4cGVjdGVkX2Z1bmNfbmFtZSI6ICIiCiAgICAgICAgICAgIH0sCiAgICAgICAgICAgICIyIjogewogICAgICAgICAgICAgICAgInByb21wdCI6ICJVc2luZyB0aGUga25vd2xlZGdlIGZyb20gdGhlIHByZXZpb3VzIHRhc2ssIGV4cGxhaW4gdGhlIHJvbGUgb2Ygd2F0ZXIgaW4gdGhlIHByb2Nlc3Mgb2YgcGhvdG9zeW50aGVzaXMuIFNwZWNpZmljYWxseSwgZGVzY3JpYmUgaG93IHdhdGVyIGlzIGludm9sdmVkIGluIHRoZSBsaWdodC1kZXBlbmRlbnQgcmVhY3Rpb25zIGFuZCB0aGUgb3ZlcmFsbCBjaGVtaWNhbCBlcXVhdGlvbiBmb3IgcGhvdG9zeW50aGVzaXMuIE1ha2Ugc3VyZSB0byBtZW50aW9uIHRoZSBwcm9kdWN0cyBhbmQgcmVhY3RhbnRzIG9mIHRoZSBsaWdodC1kZXBlbmRlbnQgcmVhY3Rpb25zIGFuZCBob3cgdGhleSByZWxhdGUgdG8gdGhlIG92ZXJhbGwgcGhvdG9zeW50aGVzaXMgZXF1YXRpb24uXG4iLAogICAgICAgICAgICAgICAgInRlc3RfY2FzZXMiOiBbCiAgICAgICAgICAgICAgICAgICAgKCIiLCAiIikKICAgICAgICAgICAgICAgIF0sCiAgICAgICAgICAgICAgICAiZXhwZWN0ZWRfZnVuY19uYW1lIjogIiIKICAgICAgICAgICAgfQogICAgICAgIH0KCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgZ2V0X2luc3RydWN0aW9ucyh0OiBkaWN0KSAtPiBzdHI6CiAgICAgICAgcmV0dXJuIHRbJ3Byb21wdCddCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgIGZyb20gc2FuZGJveF9ldmFsX2hlbHBlciBpbXBvcnQgZXZhbF93aXRoX2xsbV9qdWRnZQogICAgICAgIGluc3RydWN0aW9ucyA9IFRhc2tGYW1pbHkuZ2V0X2luc3RydWN0aW9ucyh0KQogICAgICAgIGNyaXRlcmlhID0gWwogICAgICAgICAgICAiVGhlIHJlc3BvbnNlIHNob3VsZCBpbmNsdWRlIGEgZGV0YWlsZWQgZXhwbGFuYXRpb24gb2YgdGhlIGNoZW1pY2FsIGludGVyYWN0aW9ucyBpbiB3YXRlciwgY292ZXJpbmcgYm9uZCB0eXBlLCBlbGVjdHJvbmVnYXRpdml0eSBkaWZmZXJlbmNlcywgbW9sZWN1bGFyIGdlb21ldHJ5LCBpbnRlcm1vbGVjdWxhciBpbnRlcmFjdGlvbnMsIGFuZCBwb3RlbnRpYWwgcmVhY3Rpb25zLiIsCiAgICAgICAgICAgICJUaGUgcmVzcG9uc2Ugc2hvdWxkIGV4cGxhaW4gdGhlIHJvbGUgb2Ygd2F0ZXIgaW4gdGhlIHByb2Nlc3Mgb2YgcGhvdG9zeW50aGVzaXMsIHNwZWNpZmljYWxseSBkZXNjcmliaW5nIGhvdyB3YXRlciBpcyBpbnZvbHZlZCBpbiB0aGUgbGlnaHQtZGVwZW5kZW50IHJlYWN0aW9ucyBhbmQgdGhlIG92ZXJhbGwgY2hlbWljYWwgZXF1YXRpb24gZm9yIHBob3Rvc3ludGhlc2lzLiBNZW50aW9uIHRoZSBwcm9kdWN0cyBhbmQgcmVhY3RhbnRzIG9mIHRoZSBsaWdodC1kZXBlbmRlbnQgcmVhY3Rpb25zIGFuZCBob3cgdGhleSByZWxhdGUgdG8gdGhlIG92ZXJhbGwgcGhvdG9zeW50aGVzaXMgZXF1YXRpb24uIgogICAgICAgIF0KICAgICAgICByZXR1cm4gMS4wIGlmIGV2YWxfd2l0aF9sbG1fanVkZ2UoaW5zdHJ1Y3Rpb25zLCBzdWJtaXNzaW9uLCBjcml0ZXJpYSkgZWxzZSAwLjA=)

class TaskFamily:

@staticmethod

def get\_tasks() -> dict\[str, dict\]:

return {

"1": {

"prompt": "Provide a detailed explanation of the chemical interactions in water, including:\\n1. Bond type\\n2. Electronegativity differences\\n3. Molecular geometry\\n4. Intermolecular interactions\\n5. Potential reactions\\n",

"test\_cases": \[

("", "")

\],

"expected\_func\_name": ""

},

"2": {

"prompt": "Using the knowledge from the previous task, explain the role of water in the process of photosynthesis. Specifically, describe how water is involved in the light-dependent reactions and the overall chemical equation for photosynthesis. Make sure to mention the products and reactants of the light-dependent reactions and how they relate to the overall photosynthesis equation.\\n",

"test\_cases": \[

("", "")

\],

"expected\_func\_name": ""

}

}

@staticmethod

def get\_instructions(t: dict) -> str:

return t\[’prompt’\]

@staticmethod

def score(t: dict, submission: str) -> float | None:

from sandbox\_eval\_helper import eval\_with\_llm\_judge

instructions = TaskFamily.get\_instructions(t)

criteria = \[

"The response should include a detailed explanation of the chemical interactions in water, covering bond type, electronegativity differences, molecular geometry, intermolecular interactions, and potential reactions.",

"The response should explain the role of water in the process of photosynthesis, specifically describing how water is involved in the light-dependent reactions and the overall chemical equation for photosynthesis. Mention the products and reactants of the light-dependent reactions and how they relate to the overall photosynthesis equation."

\]

return 1.0 if eval\_with\_llm\_judge(instructions, submission, criteria) else 0.0

## Appendix F AC/DC Prompts

We build upon and extend the system prompts used by [^91].

### F.1 Task Creation Prompts

The system prompt for task creation instructs the scientist model to propose novel, diverse task families to uncover the subject model’s capabilities:

<svg id="A6.SS1.p2.pic1" height="9964.23" overflow="visible" version="1.1" viewBox="0 0 600 9964.23" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,9964.23) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 9964.23 L 600 9964.23 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 9942.68 L 599.31 9942.68 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 9949.99)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p2.pic1.1.1.1.1.1.1">Task Creation System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 -5873.22)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:1142.16em;--ltx-fo-depth:0.19em;" width="559.25" height="15806.77" transform="matrix(1 0 0 -1 0 15804.08)" overflow="visible" color="#000000"><span id="A6.SS1.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p2.pic1.2.2.2.1.1.1">You are an expert in designing task families to assess the capabilities of a particular new large language model (LLM). Your goal is to create novel, diverse task families that can reveal the breadth and depth of the model’s skills.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.2">We especially want you to uncover tasks that could reveal surprising capabilities or failures. Successfully written task families will be added to a task archive.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.3">In each generation, previously generated task families will be provided as context so that you can generate different tasks. Be creative, explore different domains, and design tasks that can distinguish between models with varying levels of expertise. Make sure each task is coherent and does not try to combine too many concepts into one.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.4">Each task family should be designed according to the METR Standard, which requires the following Python format:</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.5"><a href="data:text/plain;base64,Y2xhc3MgVGFza0ZhbWlseToKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGFza3MoKSAtPiBkaWN0W3N0ciwgZGljdF06CiAgICAgICAgIyBSZXR1cm5zIGEgbWFwcGluZyBmcm9tIHRhc2sgbmFtZXMgdG8gYXJiaXRyYXJ5IGRhdGEgdGhhdCBpcyBzcGVjaWZpYyB0byBlYWNoIHRhc2suCiAgICAgICAgIyBFYWNoIHRhc2sgZmFtaWx5IHNob3VsZCBjb250YWluIDIgdGFza3MgaW4gdGhlIGRpY3Rpb25hcnksIGxhYmVsbGVkICIxIiBhbmQgIjIiLgogICAgICAgICMgLi4uIGltcGxlbWVudGF0aW9uIC4uLgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfaW5zdHJ1Y3Rpb25zKHQ6IGRpY3QpIC0+IHN0cjoKICAgICAgICAjIFRoaXMgbWV0aG9kIHNob3VsZCByZXR1cm4gYSBzdHJpbmcgY29udGFpbmluZyBpbml0aWFsIHRhc2sgaW5zdHJ1Y3Rpb25zIGZvciB0aGUgYWdlbnQuCiAgICAgICAgIyAuLi4gaW1wbGVtZW50YXRpb24gLi4uCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgICAgICMgYHNjb3JlYCBpcyBjYWxsZWQgYWZ0ZXIgdGhlIGFnZW50IHN1Ym1pdHMgYSBzb2x1dGlvbi4gUmV0dXJuIDAgb24gZmFpbHVyZSBhbmQgMSBvbiBzdWNjZXNzLiBEbyBub3QgZ2l2ZSBwYXJ0aWFsIHNjb3Jlcy4KICAgICAgICAjIFRocm93aW5nIGFuIGV4Y2VwdGlvbiB3aWxsIHJlc3VsdCBpbiBhIHNjb3JlIG9mIDAuCiAgICAgICAgIyBGb3IgbWF0aCBvciBjb2RlIHJlbGF0ZWQgdGFza3MsIGltcGxlbWVudHMgdGhlIHN0ZXAtYnktc3RlcCBjb2RlIHRvIGNvbXB1dGUgdGhlIGNvcnJlY3QgYW5zd2VyIGdpdmVuIHRoZSB0YXNrIGluc3RydWN0aW9ucy4KICAgICAgICAjIC4uLiBpbXBsZW1lbnRhdGlvbiAuLi4=" download="">⬇</a> <span id="lstnumberx551"><span id="lstnumberx551.1">class</span> <span id="lstnumberx551.3">TaskFamily</span><span id="lstnumberx551.4">:</span></span> <span id="lstnumberx552"><span id="lstnumberx552.2">@staticmethod</span> </span><span id="lstnumberx553"><span id="lstnumberx553.2">def</span> <span id="lstnumberx553.4">get_tasks</span> <span id="lstnumberx553.5">()</span> <span id="lstnumberx553.7">-&gt;</span> <span id="lstnumberx553.9">dict</span> <span id="lstnumberx553.10">[</span><span id="lstnumberx553.11">str</span><span id="lstnumberx553.12">,</span><span id="lstnumberx553.14">dict</span><span id="lstnumberx553.15">]:</span></span> <span id="lstnumberx554"><span id="lstnumberx554.2">#</span> <span id="lstnumberx554.4">Returns</span> <span id="lstnumberx554.6">a</span> <span id="lstnumberx554.8">mapping</span> <span id="lstnumberx554.10">from</span> <span id="lstnumberx554.12">task</span> <span id="lstnumberx554.14">names</span> <span id="lstnumberx554.16">to</span> <span id="lstnumberx554.18">arbitrary</span> <span id="lstnumberx554.20">data</span> <span id="lstnumberx554.22">that</span> <span id="lstnumberx554.24">is</span> <span id="lstnumberx554.26">specific</span> <span id="lstnumberx554.28">to</span> <span id="lstnumberx554.30">each</span> <span id="lstnumberx554.32">task</span><span id="lstnumberx554.33">.</span></span> <span id="lstnumberx555"><span id="lstnumberx555.2">#</span> <span id="lstnumberx555.4">Each</span> <span id="lstnumberx555.6">task</span> <span id="lstnumberx555.8">family</span> <span id="lstnumberx555.10">should</span> <span id="lstnumberx555.12">contain</span> <span id="lstnumberx555.14">2</span> <span id="lstnumberx555.16">tasks</span> <span id="lstnumberx555.18">in</span> <span id="lstnumberx555.20">the</span> <span id="lstnumberx555.22">dictionary</span><span id="lstnumberx555.23">,</span><span id="lstnumberx555.25">labelled</span> <span id="lstnumberx555.27">"1"</span> <span id="lstnumberx555.29">and</span> <span id="lstnumberx555.31">"2".</span></span> <span id="lstnumberx556"><span id="lstnumberx556.2">#</span><span id="lstnumberx556.4">...</span><span id="lstnumberx556.6">implementation</span><span id="lstnumberx556.8">...</span></span> <span id="lstnumberx558"><span id="lstnumberx558.2">@staticmethod</span> </span><span id="lstnumberx559"><span id="lstnumberx559.2">def</span> <span id="lstnumberx559.4">get_instructions</span> <span id="lstnumberx559.5">(</span><span id="lstnumberx559.6">t</span><span id="lstnumberx559.7">:</span><span id="lstnumberx559.9">dict</span><span id="lstnumberx559.10">)</span> <span id="lstnumberx559.12">-&gt;</span> <span id="lstnumberx559.14">str</span><span id="lstnumberx559.15">:</span></span> <span id="lstnumberx560"><span id="lstnumberx560.2">#</span> <span id="lstnumberx560.4">This</span> <span id="lstnumberx560.6">method</span> <span id="lstnumberx560.8">should</span> <span id="lstnumberx560.10">return</span> <span id="lstnumberx560.12">a</span> <span id="lstnumberx560.14">string</span> <span id="lstnumberx560.16">containing</span> <span id="lstnumberx560.18">initial</span> <span id="lstnumberx560.20">task</span> <span id="lstnumberx560.22">instructions</span> <span id="lstnumberx560.24">for</span> <span id="lstnumberx560.26">the</span> <span id="lstnumberx560.28">agent</span><span id="lstnumberx560.29">.</span></span> <span id="lstnumberx561"><span id="lstnumberx561.2">#</span><span id="lstnumberx561.4">...</span><span id="lstnumberx561.6">implementation</span><span id="lstnumberx561.8">...</span></span> <span id="lstnumberx563"><span id="lstnumberx563.2">@staticmethod</span> </span><span id="lstnumberx564"><span id="lstnumberx564.2">def</span> <span id="lstnumberx564.4">score</span> <span id="lstnumberx564.5">(</span><span id="lstnumberx564.6">t</span><span id="lstnumberx564.7">:</span><span id="lstnumberx564.9">dict</span><span id="lstnumberx564.10">,</span><span id="lstnumberx564.12">submission</span><span id="lstnumberx564.13">:</span><span id="lstnumberx564.15">str</span><span id="lstnumberx564.16">)</span> <span id="lstnumberx564.18">-&gt;</span> <span id="lstnumberx564.20">float</span> <span id="lstnumberx564.22">|</span> <span id="lstnumberx564.24">None</span><span id="lstnumberx564.25">:</span></span> <span id="lstnumberx565"><span id="lstnumberx565.2">#</span> <span id="lstnumberx565.4">‘</span> <span id="lstnumberx565.5">score</span> <span id="lstnumberx565.6">‘</span> <span id="lstnumberx565.8">is</span> <span id="lstnumberx565.10">called</span> <span id="lstnumberx565.12">after</span> <span id="lstnumberx565.14">the</span> <span id="lstnumberx565.16">agent</span> <span id="lstnumberx565.18">submits</span> <span id="lstnumberx565.20">a</span> <span id="lstnumberx565.22">solution</span><span id="lstnumberx565.23">.</span><span id="lstnumberx565.25">Return</span> <span id="lstnumberx565.27">0</span> <span id="lstnumberx565.29">on</span> <span id="lstnumberx565.31">failure</span> <span id="lstnumberx565.33">and</span> <span id="lstnumberx565.35">1</span> <span id="lstnumberx565.37">on</span> <span id="lstnumberx565.39">success</span><span id="lstnumberx565.40">.</span><span id="lstnumberx565.42">Do</span> <span id="lstnumberx565.44">not</span> <span id="lstnumberx565.46">give</span> <span id="lstnumberx565.48">partial</span> <span id="lstnumberx565.50">scores</span><span id="lstnumberx565.51">.</span></span> <span id="lstnumberx566"><span id="lstnumberx566.2">#</span> <span id="lstnumberx566.4">Throwing</span> <span id="lstnumberx566.6">an</span> <span id="lstnumberx566.8">exception</span> <span id="lstnumberx566.10">will</span> <span id="lstnumberx566.12">result</span> <span id="lstnumberx566.14">in</span> <span id="lstnumberx566.16">a</span> <span id="lstnumberx566.18">score</span> <span id="lstnumberx566.20">of</span> <span id="lstnumberx566.22">0.</span></span> <span id="lstnumberx567"><span id="lstnumberx567.2">#</span> <span id="lstnumberx567.4">For</span> <span id="lstnumberx567.6">math</span> <span id="lstnumberx567.8">or</span> <span id="lstnumberx567.10">code</span> <span id="lstnumberx567.12">related</span> <span id="lstnumberx567.14">tasks</span><span id="lstnumberx567.15">,</span><span id="lstnumberx567.17">implements</span> <span id="lstnumberx567.19">the</span> <span id="lstnumberx567.21">step</span> <span id="lstnumberx567.22">-</span> <span id="lstnumberx567.23">by</span> <span id="lstnumberx567.24">-</span> <span id="lstnumberx567.25">step</span> <span id="lstnumberx567.27">code</span> <span id="lstnumberx567.29">to</span> <span id="lstnumberx567.31">compute</span> <span id="lstnumberx567.33">the</span> <span id="lstnumberx567.35">correct</span> <span id="lstnumberx567.37">answer</span> <span id="lstnumberx567.39">given</span> <span id="lstnumberx567.41">the</span> <span id="lstnumberx567.43">task</span> <span id="lstnumberx567.45">instructions</span><span id="lstnumberx567.46">.</span></span> <span id="lstnumberx568"><span id="lstnumberx568.2">#</span><span id="lstnumberx568.4">...</span><span id="lstnumberx568.6">implementation</span><span id="lstnumberx568.8">...</span></span></span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.6">When applicable, for example, for any math or code related tasks, the <span id="A6.SS1.p2.pic1.2.2.2.1.1.6.1">score</span> function MUST implement the code to get the correct answer given the task instructions. You can use the standard python operations, but also libraries like <span id="A6.SS1.p2.pic1.2.2.2.1.1.6.2">numpy</span> or <span id="A6.SS1.p2.pic1.2.2.2.1.1.6.3">sympy</span> to do more complex computations. Don’t forget to import them. Also, don’t forget that <span id="A6.SS1.p2.pic1.2.2.2.1.1.6.4">sympy</span> returns fractions by default, so you need to convert the results it returns to floats. Make sure to add comments to your code to explain what you are doing. Make sure to handle different answer types, e.g. latex style answers such as</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.7">sqrta or</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.8">fracab, or text based answers, such as <span id="A6.SS1.p2.pic1.2.2.2.1.1.8.1">p - q</span>, or <span id="A6.SS1.p2.pic1.2.2.2.1.1.8.2">p + q</span>.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.9">The <span id="A6.SS1.p2.pic1.2.2.2.1.1.9.1">score</span> function may optionally call a helper function that calls a GPT-4 based LLM judge.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.10"><a href="data:text/plain;base64,IyBBdXRvbWF0ZWQgTExNIGp1ZGdlIGhlbHBlciBmdW5jdGlvbgpkZWYgZXZhbF93aXRoX2xsbV9qdWRnZSgKICAgICAgICBpbnN0cnVjdGlvbnM6IHN0ciwgICMgVGhlIGluc3RydWN0aW9ucyBmb3IgdGhlIHRhc2sKICAgICAgICBzdWJtaXNzaW9uOiBzdHIsICAgICMgVGhlIHN1Ym1pc3Npb24gdG8gZXZhbHVhdGUKICAgICAgICBjcml0ZXJpYTogT3B0aW9uYWxbTGlzdFtzdHJdXSA9IE5vbmUsICAjIE9wdGlvbmFsIGFkZGl0aW9uYWwgY3JpdGVyaWEKKSAtPiBib29sOgogICAgIyBSZXR1cm5zIGEgYm9vbGVhbiBpbmRpY2F0aW5nIHdoZXRoZXIgdGhlIGFnZW50IGlzIGRlZW1lZCB0byBoYXZlIHN1Y2NlZWRlZAogICAgIyBhdCB0aGUgdGFzaywgYW5kIG1lZXRzIGFueSBhZGRpdGlvbmFsIGNyaXRlcmlhLg==" download="">⬇</a> <span id="lstnumberx569"><span id="lstnumberx569.1">#</span> <span id="lstnumberx569.3">Automated</span> <span id="lstnumberx569.5">LLM</span> <span id="lstnumberx569.7">judge</span> <span id="lstnumberx569.9">helper</span> <span id="lstnumberx569.11">function</span> </span><span id="lstnumberx570"><span id="lstnumberx570.1">def</span> <span id="lstnumberx570.3">eval_with_llm_judge</span> <span id="lstnumberx570.4">(</span></span> <span id="lstnumberx571"><span id="lstnumberx571.2">instructions</span><span id="lstnumberx571.3">:</span><span id="lstnumberx571.5">str</span><span id="lstnumberx571.6">,</span><span id="lstnumberx571.8">#</span> <span id="lstnumberx571.10">The</span> <span id="lstnumberx571.12">instructions</span> <span id="lstnumberx571.14">for</span> <span id="lstnumberx571.16">the</span> <span id="lstnumberx571.18">task</span> </span><span id="lstnumberx572"><span id="lstnumberx572.2">submission</span><span id="lstnumberx572.3">:</span><span id="lstnumberx572.5">str</span><span id="lstnumberx572.6">,</span><span id="lstnumberx572.8">#</span> <span id="lstnumberx572.10">The</span> <span id="lstnumberx572.12">submission</span> <span id="lstnumberx572.14">to</span> <span id="lstnumberx572.16">evaluate</span> </span><span id="lstnumberx573"><span id="lstnumberx573.2">criteria</span><span id="lstnumberx573.3">:</span><span id="lstnumberx573.5">Optional</span> <span id="lstnumberx573.6">[</span><span id="lstnumberx573.7">List</span> <span id="lstnumberx573.8">[</span><span id="lstnumberx573.9">str</span><span id="lstnumberx573.10">]]</span> <span id="lstnumberx573.12">=</span> <span id="lstnumberx573.14">None</span><span id="lstnumberx573.15">,</span><span id="lstnumberx573.17">#</span> <span id="lstnumberx573.19">Optional</span> <span id="lstnumberx573.21">additional</span> <span id="lstnumberx573.23">criteria</span> </span><span id="lstnumberx574"><span id="lstnumberx574.1">)</span> <span id="lstnumberx574.3">-&gt;</span> <span id="lstnumberx574.5">bool</span><span id="lstnumberx574.6">:</span></span> <span id="lstnumberx575"><span id="lstnumberx575.2">#</span> <span id="lstnumberx575.4">Returns</span> <span id="lstnumberx575.6">a</span> <span id="lstnumberx575.8">boolean</span> <span id="lstnumberx575.10">indicating</span> <span id="lstnumberx575.12">whether</span> <span id="lstnumberx575.14">the</span> <span id="lstnumberx575.16">agent</span> <span id="lstnumberx575.18">is</span> <span id="lstnumberx575.20">deemed</span> <span id="lstnumberx575.22">to</span> <span id="lstnumberx575.24">have</span> <span id="lstnumberx575.26">succeeded</span> </span><span id="lstnumberx576"><span id="lstnumberx576.2">#</span> <span id="lstnumberx576.4">at</span> <span id="lstnumberx576.6">the</span> <span id="lstnumberx576.8">task</span><span id="lstnumberx576.9">,</span><span id="lstnumberx576.11">and</span> <span id="lstnumberx576.13">meets</span> <span id="lstnumberx576.15">any</span> <span id="lstnumberx576.17">additional</span> <span id="lstnumberx576.19">criteria</span><span id="lstnumberx576.20">.</span></span></span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.11">You should use this function unless the task is better evaluated through code. DO NOT RE-IMPLEMENT THIS FUNCTION! There is no need to repeat any criteria that are already in the instructions. One possible use of the criteria field is if you already have an answer in mind for the task. An example usage in <span id="A6.SS1.p2.pic1.2.2.2.1.1.11.1">score</span> with an optional criteria is as follows:</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.12"><a href="data:text/plain;base64,QHN0YXRpY21ldGhvZApkZWYgc2NvcmUodDogZGljdCwgc3VibWlzc2lvbjogc3RyKSAtPiBmbG9hdCB8IE5vbmU6CiAgICBmcm9tIHNhbmRib3hfZXZhbF9oZWxwZXIgaW1wb3J0IGV2YWxfd2l0aF9sbG1fanVkZ2UKICAgIGluc3RydWN0aW9ucyA9IFRhc2tGYW1pbHkuZ2V0X2luc3RydWN0aW9ucyh0KQogICAgY3JpdGVyaWEgPSBbIlRoZSByZXNwb25zZSBzaG91bGQgaW5jbHVkZSB0aGUgbmFtZSBBbGljZS4iXQogICAgcmV0dXJuIDEuMCBpZiBldmFsX3dpdGhfbGxtX2p1ZGdlKGluc3RydWN0aW9ucywgc3VibWlzc2lvbiwgY3JpdGVyaWEpIGVsc2UgMC4w" download="">⬇</a> <span id="lstnumberx577"><span id="lstnumberx577.1">@staticmethod</span> </span><span id="lstnumberx578"><span id="lstnumberx578.1">def</span> <span id="lstnumberx578.3">score</span> <span id="lstnumberx578.4">(</span><span id="lstnumberx578.5">t</span><span id="lstnumberx578.6">:</span><span id="lstnumberx578.8">dict</span><span id="lstnumberx578.9">,</span><span id="lstnumberx578.11">submission</span><span id="lstnumberx578.12">:</span><span id="lstnumberx578.14">str</span><span id="lstnumberx578.15">)</span> <span id="lstnumberx578.17">-&gt;</span> <span id="lstnumberx578.19">float</span> <span id="lstnumberx578.21">|</span> <span id="lstnumberx578.23">None</span><span id="lstnumberx578.24">:</span></span> <span id="lstnumberx579"><span id="lstnumberx579.2">from</span> <span id="lstnumberx579.4">sandbox_eval_helper</span> <span id="lstnumberx579.6">import</span> <span id="lstnumberx579.8">eval_with_llm_judge</span> </span><span id="lstnumberx580"><span id="lstnumberx580.2">instructions</span> <span id="lstnumberx580.4">=</span> <span id="lstnumberx580.6">TaskFamily</span><span id="lstnumberx580.7">.</span><span id="lstnumberx580.8">get_instructions</span> <span id="lstnumberx580.9">(</span><span id="lstnumberx580.10">t</span><span id="lstnumberx580.11">)</span> </span><span id="lstnumberx581"><span id="lstnumberx581.2">criteria</span> <span id="lstnumberx581.4">=</span> <span id="lstnumberx581.6">["</span> <span id="lstnumberx581.7">The</span> <span id="lstnumberx581.9">response</span> <span id="lstnumberx581.11">should</span> <span id="lstnumberx581.13">include</span> <span id="lstnumberx581.15">the</span> <span id="lstnumberx581.17">name</span> <span id="lstnumberx581.19">Alice</span><span id="lstnumberx581.20">."]</span> </span><span id="lstnumberx582"><span id="lstnumberx582.2">return</span> <span id="lstnumberx582.4">1.0</span> <span id="lstnumberx582.6">if</span> <span id="lstnumberx582.8">eval_with_llm_judge</span> <span id="lstnumberx582.9">(</span><span id="lstnumberx582.10">instructions</span><span id="lstnumberx582.11">,</span><span id="lstnumberx582.13">submission</span><span id="lstnumberx582.14">,</span><span id="lstnumberx582.16">criteria</span><span id="lstnumberx582.17">)</span> <span id="lstnumberx582.19">else</span> <span id="lstnumberx582.21">0.0</span> </span></span><span id="A6.SS1.p2.pic1.2.2.2.1.1.13">Additionally, the <span id="A6.SS1.p2.pic1.2.2.2.1.1.13.1">score</span> function may call the <span id="A6.SS1.p2.pic1.2.2.2.1.1.13.2">get_function_name_to_callable</span> function to get a mapping from function names to their callables.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.14"><a href="data:text/plain;base64,QHN0YXRpY21ldGhvZApkZWYgZ2V0X2Z1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUoCiAgICBmdW5jX3N0cmluZzogc3RyLCAjIEEgc3RyaW5nIGNvbnRhaW5pbmcgb25lIG9yIG11bHRpcGxlIHB5dGhvbiBmdW5jdGlvbiBkZWZpbml0aW9ucy4KKSAtPiBkaWN0W3N0ciwgQ2FsbGFibGVdOgogICAgIyBSZXR1cm5zIGEgZGljdGlvbmFyeSBtYXBwaW5nIGZ1bmN0aW9uIG5hbWVzIHRvIHRoZWlyIGNhbGxhYmxlcy4=" download="">⬇</a> <span id="lstnumberx583"><span id="lstnumberx583.1">@staticmethod</span> </span><span id="lstnumberx584"><span id="lstnumberx584.1">def</span> <span id="lstnumberx584.3">get_function_name_to_callable</span> <span id="lstnumberx584.4">(</span></span> <span id="lstnumberx585"><span id="lstnumberx585.2">func_string</span><span id="lstnumberx585.3">:</span><span id="lstnumberx585.5">str</span><span id="lstnumberx585.6">,</span><span id="lstnumberx585.8">#</span> <span id="lstnumberx585.10">A</span> <span id="lstnumberx585.12">string</span> <span id="lstnumberx585.14">containing</span> <span id="lstnumberx585.16">one</span> <span id="lstnumberx585.18">or</span> <span id="lstnumberx585.20">multiple</span> <span id="lstnumberx585.22">python</span> <span id="lstnumberx585.24">function</span> <span id="lstnumberx585.26">definitions</span><span id="lstnumberx585.27">.</span></span> <span id="lstnumberx586"><span id="lstnumberx586.1">)</span> <span id="lstnumberx586.3">-&gt;</span> <span id="lstnumberx586.5">dict</span> <span id="lstnumberx586.6">[</span><span id="lstnumberx586.7">str</span><span id="lstnumberx586.8">,</span><span id="lstnumberx586.10">Callable</span><span id="lstnumberx586.11">]:</span></span> <span id="lstnumberx587"><span id="lstnumberx587.2">#</span> <span id="lstnumberx587.4">Returns</span> <span id="lstnumberx587.6">a</span> <span id="lstnumberx587.8">dictionary</span> <span id="lstnumberx587.10">mapping</span> <span id="lstnumberx587.12">function</span> <span id="lstnumberx587.14">names</span> <span id="lstnumberx587.16">to</span> <span id="lstnumberx587.18">their</span> <span id="lstnumberx587.20">callables</span><span id="lstnumberx587.21">.</span></span></span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.15">You should use this function if the task instruction requests the agent to write code. You may use this example function as a reference for how to implement the <span id="A6.SS1.p2.pic1.2.2.2.1.1.15.1">score</span> function. Reimplement it for simple tasks, or extend it for more complex tasks. An example usage in <span id="A6.SS1.p2.pic1.2.2.2.1.1.15.2">score</span> is as follows:</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.16"><a href="data:text/plain;base64,ZGVmIHNjb3JlKHQ6IGRpY3QsIHN1Ym1pc3Npb246IHN0cikgLT4gZmxvYXQgfCBOb25lOgogICAgZnJvbSBzYW5kYm94X2V2YWxfaGVscGVyIGltcG9ydCBnZXRfZnVuY3Rpb25fbmFtZV90b19jYWxsYWJsZQoKICAgICMgVGVzdCBjYXNlcyBmcm9tIGdldF90YXNrcwogICAgdGVzdF9pbnB1dCwgZXhwZWN0ZWRfb3V0cHV0ID0gdFsidGVzdF9jYXNlcyJdWzBdCgogICAgIyBHZXQgZnVuY3Rpb24gbmFtZSB0byBjYWxsYWJsZSBtYXBwaW5nCiAgICBmdW5jdGlvbl9uYW1lX3RvX2NhbGxhYmxlID0gZ2V0X2Z1bmN0aW9uX25hbWVfdG9fY2FsbGFibGUoCiAgICAgICAgc3VibWlzc2lvbgogICAgKQoKICAgICMgUnVuIHRlc3QgY2FzZQogICAgdHJ5OgogICAgICAgICMgRXhlY3V0ZSB0aGUgZnVuY3Rpb24KICAgICAgICBzdWJtaXNzaW9uX3Jlc3VsdCA9IGZ1bmN0aW9uX25hbWVfdG9fY2FsbGFibGVbdFsiZXhwZWN0ZWRfZnVuY19uYW1lIl1dKAogICAgICAgICAgICB0ZXN0X2lucHV0CiAgICAgICAgKQoKICAgICAgICAjIENvbXBhcmUgd2l0aCBleHBlY3RlZCBvdXRwdXQKICAgICAgICBpZiBzdWJtaXNzaW9uX3Jlc3VsdCA9PSBleHBlY3RlZF9vdXRwdXQ6CiAgICAgICAgICAgIHJldHVybiAxLjAKCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICMgSWYgZnVuY3Rpb24gZmFpbHMgb24gYSB0ZXN0IGNhc2UsIHJldHVybiAwLjAKICAgICAgICByZXR1cm4gMC4w" download="">⬇</a> <span id="lstnumberx588"><span id="lstnumberx588.1">def</span> <span id="lstnumberx588.3">score</span> <span id="lstnumberx588.4">(</span><span id="lstnumberx588.5">t</span><span id="lstnumberx588.6">:</span><span id="lstnumberx588.8">dict</span><span id="lstnumberx588.9">,</span><span id="lstnumberx588.11">submission</span><span id="lstnumberx588.12">:</span><span id="lstnumberx588.14">str</span><span id="lstnumberx588.15">)</span> <span id="lstnumberx588.17">-&gt;</span> <span id="lstnumberx588.19">float</span> <span id="lstnumberx588.21">|</span> <span id="lstnumberx588.23">None</span><span id="lstnumberx588.24">:</span></span> <span id="lstnumberx589"><span id="lstnumberx589.2">from</span> <span id="lstnumberx589.4">sandbox_eval_helper</span> <span id="lstnumberx589.6">import</span> <span id="lstnumberx589.8">get_function_name_to_callable</span> </span><span id="lstnumberx591"><span id="lstnumberx591.2">#</span> <span id="lstnumberx591.4">Test</span> <span id="lstnumberx591.6">cases</span> <span id="lstnumberx591.8">from</span> <span id="lstnumberx591.10">get_tasks</span> </span><span id="lstnumberx592"><span id="lstnumberx592.2">test_input</span><span id="lstnumberx592.3">,</span><span id="lstnumberx592.5">expected_output</span> <span id="lstnumberx592.7">=</span> <span id="lstnumberx592.9">t</span> <span id="lstnumberx592.10">["</span> <span id="lstnumberx592.11">test_cases</span> <span id="lstnumberx592.12">"][0]</span> </span><span id="lstnumberx594"><span id="lstnumberx594.2">#</span> <span id="lstnumberx594.4">Get</span> <span id="lstnumberx594.6">function</span> <span id="lstnumberx594.8">name</span> <span id="lstnumberx594.10">to</span> <span id="lstnumberx594.12">callable</span> <span id="lstnumberx594.14">mapping</span> </span><span id="lstnumberx595"><span id="lstnumberx595.2">function_name_to_callable</span> <span id="lstnumberx595.4">=</span> <span id="lstnumberx595.6">get_function_name_to_callable</span> <span id="lstnumberx595.7">(</span></span> <span id="lstnumberx596"><span id="lstnumberx596.2">submission</span> </span><span id="lstnumberx597"><span id="lstnumberx597.2">)</span> </span><span id="lstnumberx599"><span id="lstnumberx599.2">#</span> <span id="lstnumberx599.4">Run</span> <span id="lstnumberx599.6">test</span> <span id="lstnumberx599.8">case</span> </span><span id="lstnumberx600"><span id="lstnumberx600.2">try</span><span id="lstnumberx600.3">:</span></span> <span id="lstnumberx601"><span id="lstnumberx601.2">#</span> <span id="lstnumberx601.4">Execute</span> <span id="lstnumberx601.6">the</span> <span id="lstnumberx601.8">function</span> </span><span id="lstnumberx602"><span id="lstnumberx602.2">submission_result</span> <span id="lstnumberx602.4">=</span> <span id="lstnumberx602.6">function_name_to_callable</span> <span id="lstnumberx602.7">[</span><span id="lstnumberx602.8">t</span> <span id="lstnumberx602.9">["</span> <span id="lstnumberx602.10">expected_func_name</span> <span id="lstnumberx602.11">"]](</span></span> <span id="lstnumberx603"><span id="lstnumberx603.2">test_input</span> </span><span id="lstnumberx604"><span id="lstnumberx604.2">)</span> </span><span id="lstnumberx606"><span id="lstnumberx606.2">#</span> <span id="lstnumberx606.4">Compare</span> <span id="lstnumberx606.6">with</span> <span id="lstnumberx606.8">expected</span> <span id="lstnumberx606.10">output</span> </span><span id="lstnumberx607"><span id="lstnumberx607.2">if</span> <span id="lstnumberx607.4">submission_result</span> <span id="lstnumberx607.6">==</span> <span id="lstnumberx607.8">expected_output</span><span id="lstnumberx607.9">:</span></span> <span id="lstnumberx608"><span id="lstnumberx608.2">return</span> <span id="lstnumberx608.4">1.0</span> </span><span id="lstnumberx610"><span id="lstnumberx610.2">except</span> <span id="lstnumberx610.4">Exception</span><span id="lstnumberx610.5">:</span></span> <span id="lstnumberx611"><span id="lstnumberx611.2">#</span> <span id="lstnumberx611.4">If</span> <span id="lstnumberx611.6">function</span> <span id="lstnumberx611.8">fails</span> <span id="lstnumberx611.10">on</span> <span id="lstnumberx611.12">a</span> <span id="lstnumberx611.14">test</span> <span id="lstnumberx611.16">case</span><span id="lstnumberx611.17">,</span><span id="lstnumberx611.19">return</span> <span id="lstnumberx611.21">0.0</span> </span><span id="lstnumberx612"><span id="lstnumberx612.2">return</span> <span id="lstnumberx612.4">0.0</span> </span></span><span id="A6.SS1.p2.pic1.2.2.2.1.1.17">Respond precisely in the following format including the JSON start and end markers:</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.18"><span id="A6.SS1.p2.pic1.2.2.2.1.1.18.1">THOUGHT</span>: <span id="A6.SS1.p2.pic1.2.2.2.1.1.18.2">&lt;THOUGHT&gt;</span></span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.19"><span id="A6.SS1.p2.pic1.2.2.2.1.1.19.1">RESPONSE JSON</span>: <span id="A6.SS1.p2.pic1.2.2.2.1.1.19.2">&lt;JSON&gt;<br></span></span><span id="A6.SS1.p2.pic1.2.2.2.1.1.20">In <span id="A6.SS1.p2.pic1.2.2.2.1.1.20.1">&lt;THOUGHT&gt;</span>, first briefly think and reason about what kind of task family you want to propose. Thoughts may also include (but are not limited to): your motivation for investigating the capability, whether you think the model will succeed or fail, its novelty relative to what you have already generated, how to ensure the tasks are valid, and whether it is suitable to invoke an LLM judge for scoring.</span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.21">In <span id="A6.SS1.p2.pic1.2.2.2.1.1.21.1">&lt;JSON&gt;</span>, provide a JSON response with the following fields:</span> <span id="A6.I1"><span id="A6.I1.i1" style="list-style-type:none;">• <span id="A6.I1.i1.p1"><span id="A6.I1.i1.p1.1"><span id="A6.I1.i1.p1.1.1">"name_of_task"</span>: A concise, descriptive label (lowercase, no spaces, e.g., <span id="A6.I1.i1.p1.1.2">"name_capital_city"</span>).</span></span></span> <span id="A6.I1.i2" style="list-style-type:none;">• <span id="A6.I1.i2.p1"><span id="A6.I1.i2.p1.1"><span id="A6.I1.i2.p1.1.1">"description_of_task"</span>: A clear explanation of what the task entails (e.g., <span id="A6.I1.i2.p1.1.2">"Return the capital city of a country"</span>).</span></span></span> <span id="A6.I1.i3" style="list-style-type:none;">• <span id="A6.I1.i3.p1"><span id="A6.I1.i3.p1.1"><span id="A6.I1.i3.p1.1.1">"capability_being_measured"</span>: The specific LLM capability being evaluated (e.g., knowledge, reasoning, creativity, …).</span></span></span> <span id="A6.I1.i4" style="list-style-type:none;">• <span id="A6.I1.i4.p1"><span id="A6.I1.i4.p1.1"><span id="A6.I1.i4.p1.1.1">"estimated_human_difficulty"</span>: An estimate of the difficulty of the task on a 1-5 scale. 1 = very easy (simple factual recall), 2 = easy (basic understanding, some inference), 3 = moderate (application of knowledge, multiple steps), 4 = difficult (analysis, synthesis, creative problem-solving), 5 = very difficult (highly specialized knowledge, complex reasoning).</span></span></span> <span id="A6.I1.i5" style="list-style-type:none;">• <span id="A6.I1.i5.p1"><span id="A6.I1.i5.p1.1"><span id="A6.I1.i5.p1.1.1">"done"</span>: By default, this is set to <span id="A6.I1.i5.p1.1.2">"False"</span>. You will have <span id="A6.I1.i5.p1.1.3">{num_rounds}</span> rounds to refine the task family but do not need to use them all. Tasks will only be saved if they are flagged <span id="A6.I1.i5.p1.1.4">"done"</span> by the end. Do not return <span id="A6.I1.i5.p1.1.5">"True"</span> until you are satisfied with and have received feedback on the task family.</span></span></span> <span id="A6.I1.i6" style="list-style-type:none;">• <span id="A6.I1.i6.p1"><span id="A6.I1.i6.p1.1"><span id="A6.I1.i6.p1.1.1">"task_family"</span>: The fully implemented Python code for the <span id="A6.I1.i6.p1.1.2">TaskFamily</span> class. Write good human-readable code.</span></span></span> <span id="A6.I1.i7" style="list-style-type:none;">• <span id="A6.I1.i7.p1"><span id="A6.I1.i7.p1.1"><span id="A6.I1.i7.p1.1.1">"example_instruction"</span>: An example instruction for the task that we would expect from the output of <span id="A6.I1.i7.p1.1.2">get_instructions</span>. This should be a string..</span></span></span></span> <span id="A6.SS1.p2.pic1.2.2.2.1.1.22">All values in the JSON should be strings. You may only use standard Python packages and libraries to implement the tasks. Required library imports should be included either at the top of the file or in the class method where they are used. An import at the start of the class has no effect. DO NOT download additional data from the internet, or access the file system. Your response will be automatically parsed and used for evaluation, so ensure all components MUST be fully implemented and adhere to the METR standard.</span></span></foreignObject></g></g></svg>

In the initial round of task generation (starting from just the seed tasks), we generate a first batch of tasks. We hereby define a probability that the task is supposed to be completely novel, or novel, but still related to the seed task.

For generating a completely novel task, we use this user prompt for the scientist (alongside the system prompt above):

<svg id="A6.SS1.p5.pic1" height="75.54" overflow="visible" version="1.1" viewBox="0 0 600 75.54" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,75.54) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 75.54 L 600 75.54 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 53.99 L 599.31 53.99 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 61.31)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p5.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p5.pic1.1.1.1.1.1.1">Initial Task Prompt Completely Novel</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:1.95em;--ltx-fo-depth:0.19em;" width="559.25" height="29.67" transform="matrix(1 0 0 -1 0 26.98)" overflow="visible" color="#000000"><span id="A6.SS1.p5.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p5.pic1.2.2.2.1.1.1">A previous generated task family is provided below (with code):</span><pre><code>{prev_json}</code></pre><span id="A6.SS1.p5.pic1.2.2.2.1.1.3">Generate the next interestingly new task family.</span></span></foreignObject></g></g></svg>

For generating a novel but similar task, we use the following prompt:

<svg id="A6.SS1.p7.pic1" height="108.75" overflow="visible" version="1.1" viewBox="0 0 600 108.75" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,108.75) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 108.75 L 600 108.75 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 87.2 L 599.31 87.2 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 94.51)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p7.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p7.pic1.1.1.1.1.1.1">Initial Task Prompt Adapt Similar</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:4.35em;--ltx-fo-depth:0.19em;" width="559.25" height="62.88" transform="matrix(1 0 0 -1 0 60.19)" overflow="visible" color="#000000"><span id="A6.SS1.p7.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p7.pic1.2.2.2.1.1.1">A previous generated task family is provided below (with code):</span><pre><code>{prev_json}</code></pre><span id="A6.SS1.p7.pic1.2.2.2.1.1.3">Generate a new task family that is inspired by the previous task family, so that it provides a more interesting challenge that is more complex or explores beyond what the current task family is evaluating in terms of model capabilities.</span></span></foreignObject></g></g></svg>

Similarly, for new tasks after the initial generation phase, we adapt a task given its difficulty level (see Sec. 3).

For creating a novel task, when the parent task difficulty was ”appropriately difficult”, we again use the same probability as above for generating a completely novel task, or a novel one that is still similar to the parent task.

<svg id="A6.SS1.p10.pic1" height="3227.46" overflow="visible" version="1.1" viewBox="0 0 600 3227.46" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,3227.46) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 3227.46 L 600 3227.46 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 3205.9 L 599.31 3205.9 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 3213.22)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p10.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p10.pic1.1.1.1.1.1.1">Task Prompt Completely Novel</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:229.74em;--ltx-fo-depth:0.19em;" width="559.25" height="3181.59" transform="matrix(1 0 0 -1 0 3178.9)" overflow="visible" color="#000000"><span id="A6.SS1.p10.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p10.pic1.2.2.2.1.1.1">Consider the following task family:</span><pre><code>{original_task_json}</code></pre><span id="A6.SS1.p10.pic1.2.2.2.1.1.3">Summaries of other previously generated tasks for context are:</span><pre><code>{other_task_jsons}</code></pre><span id="A6.SS1.p10.pic1.2.2.2.1.1.5">Generate a new task family that is interestingly different, aiming to explore diverse capabilities. You can draw inspiration from the provided task, but prioritize novelty in terms of:</span> <span id="A6.I2"><span id="A6.I2.i1" style="list-style-type:none;">• <span id="A6.I2.i1.p1"><span id="A6.I2.i1.p1.1">The specific capability being measured.</span></span></span> <span id="A6.I2.i2" style="list-style-type:none;">• <span id="A6.I2.i2.p1"><span id="A6.I2.i2.p1.1">The domain or context of the task.</span></span></span> <span id="A6.I2.i3" style="list-style-type:none;">• <span id="A6.I2.i3.p1"><span id="A6.I2.i3.p1.1">The format or style of the interaction.</span></span></span></span> <span id="A6.SS1.p10.pic1.2.2.2.1.1.6">Ensure the new task is coherent, adheres to the METR standard, and is distinct from existing tasks. Respond in the standard JSON format with THOUGHT and RESPONSE JSON sections. Set ”done” to ”False” initially, as this task will be validated.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS1.p11.pic1" height="5336.29" overflow="visible" version="1.1" viewBox="0 0 600 5336.29" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,5336.29) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 5336.29 L 600 5336.29 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 5314.74 L 599.31 5314.74 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 5322.06)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p11.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p11.pic1.1.1.1.1.1.1">Task Prompt Adapt Similar</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:382.14em;--ltx-fo-depth:0.2em;" width="559.25" height="5290.42" transform="matrix(1 0 0 -1 0 5287.66)" overflow="visible" color="#000000"><span id="A6.SS1.p11.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p11.pic1.2.2.2.1.1.1">Consider the following task family:</span><pre><code>{original_task_json}</code></pre><span id="A6.SS1.p11.pic1.2.2.2.1.1.3">Summaries of other previously generated tasks for inspiration are:</span><pre><code>{other_task_jsons}</code></pre><span id="A6.SS1.p11.pic1.2.2.2.1.1.5">Generate a new task family that is inspired by the previous task family, so that it provides a more interesting challenge that is more complex or explores beyond what the current task family is evaluating in terms of model capabilities. Draw inspiration from the provided task and implement novelty in terms of:</span> <span id="A6.I3"><span id="A6.I3.i1" style="list-style-type:none;">• <span id="A6.I3.i1.p1"><span id="A6.I3.i1.p1.1">The specific capability being measured.</span></span></span> <span id="A6.I3.i2" style="list-style-type:none;">• <span id="A6.I3.i2.p1"><span id="A6.I3.i2.p1.1">The contextual setting of the task.</span></span></span> <span id="A6.I3.i3" style="list-style-type:none;">• <span id="A6.I3.i3.p1"><span id="A6.I3.i3.p1.1">The format or style of the interaction.</span></span></span></span> <span id="A6.SS1.p11.pic1.2.2.2.1.1.6">Ensure the new task is coherent, adheres to the METR standard, and is distinct from existing tasks. Respond in the standard JSON format with THOUGHT and RESPONSE JSON sections. Set <span id="A6.SS1.p11.pic1.2.2.2.1.1.6.1">"done"</span> to <span id="A6.SS1.p11.pic1.2.2.2.1.1.6.2">"False"</span> initially, as this task will be validated.</span></span></foreignObject></g></g></svg>

For creating tasks that are inspired by the parent task but are more difficult or easier, we leverage the following prompts:

<svg id="A6.SS1.p13.pic1" height="2047.85" overflow="visible" version="1.1" viewBox="0 0 600 2047.85" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,2047.85) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 2047.85 L 600 2047.85 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 2026.3 L 599.31 2026.3 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 2033.62)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p13.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p13.pic1.1.1.1.1.1.1">Make Task Harder Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:144.48em;--ltx-fo-depth:0.2em;" width="559.25" height="2001.98" transform="matrix(1 0 0 -1 0 1999.22)" overflow="visible" color="#000000"><span id="A6.SS1.p13.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p13.pic1.2.2.2.1.1.1">The following task family was found to be too easy for the current models:</span><pre><code>{original_task_json}</code></pre><span id="A6.SS1.p13.pic1.2.2.2.1.1.3">Summaries of other previously generated tasks for context are:</span><pre><code>{other_task_jsons}</code></pre><span id="A6.SS1.p13.pic1.2.2.2.1.1.5">Generate a new task family that is conceptually related but significantly more challenging. This could involve:</span> <span id="A6.I4"><span id="A6.I4.i1" style="list-style-type:none;">• <span id="A6.I4.i1.p1"><span id="A6.I4.i1.p1.1">Requiring deeper reasoning or multi-step problem solving.</span></span></span> <span id="A6.I4.i2" style="list-style-type:none;">• <span id="A6.I4.i2.p1"><span id="A6.I4.i2.p1.1">Introducing more complex constraints or edge cases.</span></span></span> <span id="A6.I4.i3" style="list-style-type:none;">• <span id="A6.I4.i3.p1"><span id="A6.I4.i3.p1.1">Using more advanced concepts within the same domain.</span></span></span> <span id="A6.I4.i4" style="list-style-type:none;">• <span id="A6.I4.i4.p1"><span id="A6.I4.i4.p1.1">Increasing the required precision or detail in the answer.</span></span></span></span> <span id="A6.SS1.p13.pic1.2.2.2.1.1.6">Ensure the new task remains coherent and adheres to the METR standard. Respond in the standard JSON format with THOUGHT and RESPONSE JSON sections. Set <span id="A6.SS1.p13.pic1.2.2.2.1.1.6.1">"done"</span> to <span id="A6.SS1.p13.pic1.2.2.2.1.1.6.2">"False"</span> initially, as this task will be validated.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS1.p14.pic1" height="1882.58" overflow="visible" version="1.1" viewBox="0 0 600 1882.58" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,1882.58) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 1882.58 L 600 1882.58 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 1861.02 L 599.31 1861.02 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 1868.34)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p14.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p14.pic1.1.1.1.1.1.1">Make Task Easier Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:132.54em;--ltx-fo-depth:0.2em;" width="559.25" height="1836.71" transform="matrix(1 0 0 -1 0 1833.94)" overflow="visible" color="#000000"><span id="A6.SS1.p14.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p14.pic1.2.2.2.1.1.1">The following task family was found to be too difficult (or impossible) for the current models:</span><pre><code>{original_task_json}</code></pre><span id="A6.SS1.p14.pic1.2.2.2.1.1.3">Summaries of other previously generated tasks for context are:</span><pre><code>{other_task_jsons}</code></pre><span id="A6.SS1.p14.pic1.2.2.2.1.1.5">Generate a new task family that is conceptually related but significantly easier. This could involve:</span> <span id="A6.I5"><span id="A6.I5.i1" style="list-style-type:none;">• <span id="A6.I5.i1.p1"><span id="A6.I5.i1.p1.1">Breaking the problem down into simpler steps.</span></span></span> <span id="A6.I5.i2" style="list-style-type:none;">• <span id="A6.I5.i2.p1"><span id="A6.I5.i2.p1.1">Reducing the complexity of the required reasoning or knowledge.</span></span></span> <span id="A6.I5.i3" style="list-style-type:none;">• <span id="A6.I5.i3.p1"><span id="A6.I5.i3.p1.1">Providing more scaffolding or clearer instructions.</span></span></span> <span id="A6.I5.i4" style="list-style-type:none;">• <span id="A6.I5.i4.p1"><span id="A6.I5.i4.p1.1">Focusing on a more fundamental aspect of the capability.</span></span></span></span> <span id="A6.SS1.p14.pic1.2.2.2.1.1.6">Ensure the new task remains coherent and adheres to the METR standard. Respond in the standard JSON format with THOUGHT and RESPONSE JSON sections. Set <span id="A6.SS1.p14.pic1.2.2.2.1.1.6.1">"done"</span> to <span id="A6.SS1.p14.pic1.2.2.2.1.1.6.2">"False"</span> initially, as this task will be validated.</span></span></foreignObject></g></g></svg>

If the generated task has implementation or logic errors and needs refinement, the scientist sees:

<svg id="A6.SS1.p16.pic1" height="2676.9" overflow="visible" version="1.1" viewBox="0 0 600 2676.9" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,2676.9) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 2676.9 L 600 2676.9 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 2655.34 L 599.31 2655.34 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 2662.66)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS1.p16.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS1.p16.pic1.1.1.1.1.1.1">Task Creation Reflexion Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:189.94em;--ltx-fo-depth:0.2em;" width="559.25" height="2631.03" transform="matrix(1 0 0 -1 0 2628.26)" overflow="visible" color="#000000"><span id="A6.SS1.p16.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS1.p16.pic1.2.2.2.1.1.1">Current round = { <span id="A6.SS1.p16.pic1.2.2.2.1.1.1.1">current_round</span> }/{ <span id="A6.SS1.p16.pic1.2.2.2.1.1.1.2">num_rounds</span> }.</span> <span id="A6.SS1.p16.pic1.2.2.2.1.1.2">In your thoughts, first carefully consider the correctness of the task family you just created. Factors may include but are not limited to:</span> <span id="A6.I6"><span id="A6.I6.i1" style="list-style-type:none;">• <span id="A6.I6.i1.p1"><span id="A6.I6.i1.p1.1">Whether sufficient synthetic data has been given in the instructions to challenge the models.</span></span></span> <span id="A6.I6.i2" style="list-style-type:none;">• <span id="A6.I6.i2.p1"><span id="A6.I6.i2.p1.1">Incomplete class definitions, syntax errors, misplaced import statements.</span></span></span> <span id="A6.I6.i3" style="list-style-type:none;">• <span id="A6.I6.i3.p1"><span id="A6.I6.i3.p1.1">Feasibility of the evaluation criteria.</span></span></span> <span id="A6.I6.i4" style="list-style-type:none;">• <span id="A6.I6.i4.p1"><span id="A6.I6.i4.p1.1">Any ambiguity or issues in the clarity of the tasks.</span></span></span> <span id="A6.I6.i5" style="list-style-type:none;">• <span id="A6.I6.i5.p1"><span id="A6.I6.i5.p1.1">The consistency and accuracy of all the fields in the JSON.</span></span></span> <span id="A6.I6.i6" style="list-style-type:none;">• <span id="A6.I6.i6.p1"><span id="A6.I6.i6.p1.1">Whether precisely two entries in <span id="A6.I6.i6.p1.1.1">get_tasks</span> have been defined.</span></span></span> <span id="A6.I6.i7" style="list-style-type:none;">• <span id="A6.I6.i7.p1"><span id="A6.I6.i7.p1.1">Whether agents can get a successful score in an unintended manner.</span></span></span> <span id="A6.I6.i8" style="list-style-type:none;">• <span id="A6.I6.i8.p1"><span id="A6.I6.i8.p1.1">Whether the desired response format for the agent has been given in the instructions.</span></span></span> <span id="A6.I6.i9" style="list-style-type:none;">• <span id="A6.I6.i9.p1"><span id="A6.I6.i9.p1.1">Under no circumstances should the instructions contain the answer or any direct hints leading to the answer. Ensure that the task remains challenging without giving away the solution.</span></span></span> <span id="A6.I6.i10" style="list-style-type:none;">• <span id="A6.I6.i10.p1"><span id="A6.I6.i10.p1.1">If the agent fails at the task, it is OK as long as the task is valid and the agent’s failure is due to the difficulty of the task. You are also trying to find surprising failures!</span></span></span></span> <span id="A6.SS1.p16.pic1.2.2.2.1.1.3">Here is the result of attempting to evaluate the tasks on the given model:</span><pre><code>{eval_response}</code></pre><span id="A6.SS1.p16.pic1.2.2.2.1.1.5">In the next attempt, try and improve on the implementation. Respond in the same JSON format as before. If there is nothing to improve, simply repeat the previous response EXACTLY after the thought and set the <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.1">"done"</span> flag to <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.2">"True"</span>. Do not set the <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.3">"done"</span> flag to <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.4">"True"</span> if you are still improving the task on the current turn. Do not set the <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.5">"done"</span> flag to <span id="A6.SS1.p16.pic1.2.2.2.1.1.5.6">"True"</span> on the final step if there are major issues with the task family.</span></span></foreignObject></g></g></svg>

### F.2 Evaluation Prompts

We can configure the subject model to provide an answer using chain-of-thought prompting [^143]:

<svg id="A6.SS2.p2.pic1" height="853.41" overflow="visible" version="1.1" viewBox="0 0 600 853.41" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,853.41) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 853.41 L 600 853.41 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 831.86 L 599.31 831.86 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 839.18)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS2.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS2.p2.pic1.1.1.1.1.1.1">Chain-of-Thought Evaluation System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:58.17em;--ltx-fo-depth:0.19em;" width="559.25" height="807.54" transform="matrix(1 0 0 -1 0 804.85)" overflow="visible" color="#000000"><span id="A6.SS2.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS2.p2.pic1.2.2.2.1.1.1">You are a helpful assistant. You are given a task to complete.</span> <span id="A6.SS2.p2.pic1.2.2.2.1.1.2">First, reason about the problem and your plan for solving the task, and then provide your final answer starting with <span id="A6.SS2.p2.pic1.2.2.2.1.1.2.1">’Answer: ’</span>. If you are asked to write code, write the code after the <span id="A6.SS2.p2.pic1.2.2.2.1.1.2.2">’Answer: ’</span> in the following format: [[START OF FINAL ANSWER TEMPLATE]] Answer:</span> <span id="A6.SS2.p2.pic1.2.2.2.1.1.3"><a href="data:text/plain;base64,ZGVmIGZ1bmN0aW9uX25hbWUoeW91cl9hcmd1bWVudHMpOiAjIEFkZCB0aGUgcmVsZXZhbnQgYXJndW1lbnRzIGhlcmUuCiAgICAjIC4uLiBpbXBsZW1lbnRhdGlvbiAuLi4KICAgIHJldHVybiB5b3VyX3JldHVybl9yZXN1bHQ=" download="">⬇</a> <span id="lstnumberx613"><span id="lstnumberx613.1">def</span> <span id="lstnumberx613.3">function_name</span> <span id="lstnumberx613.4">(</span><span id="lstnumberx613.5">your_arguments</span><span id="lstnumberx613.6">):</span><span id="lstnumberx613.8">#</span> <span id="lstnumberx613.10">Add</span> <span id="lstnumberx613.12">the</span> <span id="lstnumberx613.14">relevant</span> <span id="lstnumberx613.16">arguments</span> <span id="lstnumberx613.18">here</span><span id="lstnumberx613.19">.</span></span> <span id="lstnumberx614"><span id="lstnumberx614.2">#</span><span id="lstnumberx614.4">...</span><span id="lstnumberx614.6">implementation</span><span id="lstnumberx614.8">...</span></span> <span id="lstnumberx615"><span id="lstnumberx615.2">return</span> <span id="lstnumberx615.4">your_return_result</span> </span></span><span id="A6.SS2.p2.pic1.2.2.2.1.1.4">[[END OF FINAL ANSWER TEMPLATE]]</span> <span id="A6.SS2.p2.pic1.2.2.2.1.1.5">Make sure to define the function with its arguments and return the result of the function in the format specified in the task prompt. Don’t forget to import the necessary libraries.</span> <span id="A6.SS2.p2.pic1.2.2.2.1.1.6">Only the text after <span id="A6.SS2.p2.pic1.2.2.2.1.1.6.1">’Answer: ’</span> will be evaluated. This will be automatically parsed so ensure you follow the format exactly. Respect any other output constraints given in the task prompt after <span id="A6.SS2.p2.pic1.2.2.2.1.1.6.2">’Answer: ’</span>.</span></span></foreignObject></g></g></svg>

### F.3 Task Embedding Prompt

We generate embeddings using intfloat/e5-mistral-7b-instruct [^135] to be then stored in our vector databases for cosine similarity-based retrieval. Before embedding, we encode each task in the following format:

<svg id="A6.SS3.p2.pic1" height="126.13" overflow="visible" version="1.1" viewBox="0 0 600 126.13" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,126.13) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 126.13 L 600 126.13 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 104.57 L 599.31 104.57 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 111.89)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS3.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS3.p2.pic1.1.1.1.1.1.1">Task Embedding Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:5.55em;--ltx-fo-depth:0.25em;" width="559.25" height="80.25" transform="matrix(1 0 0 -1 0 76.8)" overflow="visible" color="#000000"><span id="A6.SS3.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS3.p2.pic1.2.2.2.1.1.1">Name of task: { <span id="A6.SS3.p2.pic1.2.2.2.1.1.1.1">name_of_task</span> }</span> <span id="A6.SS3.p2.pic1.2.2.2.1.1.2">Description of task: { <span id="A6.SS3.p2.pic1.2.2.2.1.1.2.1">description_of_task</span> }</span> <span id="A6.SS3.p2.pic1.2.2.2.1.1.3">Capability being measured: { <span id="A6.SS3.p2.pic1.2.2.2.1.1.3.1">capability_being_measured</span> }</span> <span id="A6.SS3.p2.pic1.2.2.2.1.1.4">Estimated human difficulty: { <span id="A6.SS3.p2.pic1.2.2.2.1.1.4.1">estimated_human_difficulty</span> }</span> <span id="A6.SS3.p2.pic1.2.2.2.1.1.5">Example instruction: { <span id="A6.SS3.p2.pic1.2.2.2.1.1.5.1">example_instruction</span> }</span></span></foreignObject></g></g></svg>

### F.4 Novelty Assessment Prompts

To determine whether a newly generated task is interestingly new compared to the three most similar existing tasks in the archive, we use the following system prompt:

<svg id="A6.SS4.p2.pic1" height="6298.5" overflow="visible" version="1.1" viewBox="0 0 600 6298.5" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,6298.5) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 6298.5 L 600 6298.5 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 6276.95 L 599.31 6276.95 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 6284.27)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS4.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS4.p2.pic1.1.1.1.1.1.1">Interestingly New System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:451.68em;--ltx-fo-depth:0.19em;" width="559.25" height="6252.63" transform="matrix(1 0 0 -1 0 6249.94)" overflow="visible" color="#000000"><span id="A6.SS4.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS4.p2.pic1.2.2.2.1.1.1">You are an expert in designing task families to assess the capabilities of a particular new large language model (LLM). Your goal is to create novel, diverse task families that can reveal the breadth and depth of the model’s skills.</span> <span id="A6.SS4.p2.pic1.2.2.2.1.1.2">You will be given a task family that you just generated along with its closest saved neighbours (i.e., the task families that are most similar to the newly generated one). Determine whether the generated task family is interestingly new compared to the closest task families. If so, it should be added to the task archive. Factors may include but are not limited to:</span> <span id="A6.I7"><span id="A6.I7.i1" style="list-style-type:none;">• <span id="A6.I7.i1.p1"><span id="A6.I7.i1.p1.1">The novelty of the subject area</span> </span></span><span id="A6.I7.i2" style="list-style-type:none;">• <span id="A6.I7.i2.p1"><span id="A6.I7.i2.p1.1">The difficulty of the tasks</span> </span></span><span id="A6.I7.i3" style="list-style-type:none;">• <span id="A6.I7.i3.p1"><span id="A6.I7.i3.p1.1">The capabilities being measured</span> </span></span><span id="A6.I7.i4" style="list-style-type:none;">• <span id="A6.I7.i4.p1"><span id="A6.I7.i4.p1.1">Whether the agent succeeded at the task</span> </span></span></span><span id="A6.SS4.p2.pic1.2.2.2.1.1.3">First, briefly think and reason about the task family in relation to the existing closest task families.</span> <span id="A6.SS4.p2.pic1.2.2.2.1.1.4">Then, provide your decision as <span id="A6.SS4.p2.pic1.2.2.2.1.1.4.1">’Decision: Yes’</span> or <span id="A6.SS4.p2.pic1.2.2.2.1.1.4.2">’Decision: No’</span> to indicate whether the task family should be added to the task archive.</span> <span id="A6.SS4.p2.pic1.2.2.2.1.1.5">Your response will be automatically parsed, so ensure you follow the above format exactly.</span></span></foreignObject></g></g></svg>

We then prompt with:

<svg id="A6.SS4.p4.pic1" height="138.5" overflow="visible" version="1.1" viewBox="0 0 600 138.5" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,138.5) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 138.5 L 600 138.5 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 116.94 L 599.31 116.94 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 124.26)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS4.p4.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS4.p4.pic1.1.1.1.1.1.1">Interestingly New Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 12.5)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:6.69em;--ltx-fo-depth:0em;" width="559.25" height="92.63" transform="matrix(1 0 0 -1 0 92.63)" overflow="visible" color="#000000"><span id="A6.SS4.p4.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS4.p4.pic1.2.2.2.1.1.1">You have just generated the task family:</span><pre><code>{new_task}</code></pre><span id="A6.SS4.p4.pic1.2.2.2.1.1.3">The closest task families that have already been created are:</span><pre><code>{closest_tasks}</code></pre><span id="A6.SS4.p4.pic1.2.2.2.1.1.5">Is the generated task family interestingly new compared to the closest task families? If yes, it should be added to the task archive.</span></span></foreignObject></g></g></svg>

See Tab. 5 for details on which specific scientist model we use.

### F.5 Gibberish Filter Prompts

We propose a novel minimal criterion filter for determining whether a newly discovered model is a valid solution, or not. Hereby, we define a valid solution to be an LLM that produces coherent and sensible text and not gibberish.

To detect these degenerate solutions, we prompt an LLM judge with the following system and user prompts:

<svg id="A6.SS5.p3.pic1" height="58.17" overflow="visible" version="1.1" viewBox="0 0 600 58.17" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,58.17) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 58.17 L 600 58.17 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 36.61 L 599.31 36.61 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 43.93)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS5.p3.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS5.p3.pic1.1.1.1.1.1.1">Gibberish Filter System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#000000"><span id="A6.SS5.p3.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS5.p3.pic1.2.2.2.1.1.1">You are a helpful assistant.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS5.p4.pic1" height="2903.83" overflow="visible" version="1.1" viewBox="0 0 600 2903.83" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,2903.83) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 2903.83 L 600 2903.83 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 2882.27 L 599.31 2882.27 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 2889.59)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS5.p4.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS5.p4.pic1.1.1.1.1.1.1">Gibberish Filter User Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:206.35em;--ltx-fo-depth:0.19em;" width="559.25" height="2857.96" transform="matrix(1 0 0 -1 0 2855.26)" overflow="visible" color="#000000"><span id="A6.SS5.p4.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS5.p4.pic1.2.2.2.1.1.1">Consider the following tasks shown in the numbered list:</span> <span id="A6.SS5.p4.pic1.2.2.2.1.1.2"><span id="A6.SS5.p4.pic1.2.2.2.1.1.2.1">[TASK 1]</span></span><pre><code>{instruction1}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.4"><span id="A6.SS5.p4.pic1.2.2.2.1.1.4.1">[TASK 2]</span></span><pre><code>{instruction2}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.6"><span id="A6.SS5.p4.pic1.2.2.2.1.1.6.1">[TASK 3]</span></span><pre><code>{instruction3}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.8">and the following three responses to the task from an LLM (in a numbered list):</span> <span id="A6.SS5.p4.pic1.2.2.2.1.1.9"><span id="A6.SS5.p4.pic1.2.2.2.1.1.9.1">[RESPONSE 1]</span></span><pre><code>{outputs1}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.11"><span id="A6.SS5.p4.pic1.2.2.2.1.1.11.1">[RESPONSE 2]</span></span><pre><code>{outputs2}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.13"><span id="A6.SS5.p4.pic1.2.2.2.1.1.13.1">[RESPONSE 3]</span></span><pre><code>{outputs3}</code></pre><span id="A6.SS5.p4.pic1.2.2.2.1.1.15">Your task is to determine if the LLM responded with gibberish, incoherent sentences, or not. Factors may include but are not limited to:</span> <span id="A6.I8"><span id="A6.I8.i1" style="list-style-type:none;">• <span id="A6.I8.i1.p1"><span id="A6.I8.i1.p1.1">Does the LLM form coherent sentences or are they responding with jumbled words and strings?</span></span></span> <span id="A6.I8.i2" style="list-style-type:none;">• <span id="A6.I8.i2.p1"><span id="A6.I8.i2.p1.1">Does the LLM use punctuation in a sensible way, or spam random symbol characters?</span></span></span> <span id="A6.I8.i3" style="list-style-type:none;">• <span id="A6.I8.i3.p1"><span id="A6.I8.i3.p1.1">Does the LLM end up repeating sentences non-stop?</span></span></span> <span id="A6.I8.i4" style="list-style-type:none;">• <span id="A6.I8.i4.p1"><span id="A6.I8.i4.p1.1">Does the LLM fail to return any output response?</span></span></span> <span id="A6.I8.i5" style="list-style-type:none;">• <span id="A6.I8.i5.p1"><span id="A6.I8.i5.p1.1">Does the LLM respond in a way that completely ignores the task or goes completely off-topic, in a reasonable way of attempting to solve the task?</span></span></span> <span id="A6.I8.i6" style="list-style-type:none;">• <span id="A6.I8.i6.p1"><span id="A6.I8.i6.p1.1">Does the LLM format its response in a way that is highly unexpected in the context of the tasks?</span></span></span></span> <span id="A6.SS5.p4.pic1.2.2.2.1.1.16">The responses don’t have to be correct! But they should be at least somewhat coherent, considering the factors on gibberish responses mentioned above as well as any other reasonable expectations on how LLMs may respond in a gibberish manner.</span> <span id="A6.SS5.p4.pic1.2.2.2.1.1.17">Firstly, very briefly think step-by-step and reason about the responses. Then, provide your answer as <span id="A6.SS5.p4.pic1.2.2.2.1.1.17.1">’Answer: Yes’</span> if the responses are gibberish, or <span id="A6.SS5.p4.pic1.2.2.2.1.1.17.2">’Answer: No’</span> if they are not.</span> <span id="A6.SS5.p4.pic1.2.2.2.1.1.18">Your response will be automatically parsed, so ensure you follow the above format exactly.</span></span></foreignObject></g></g></svg>

### F.6 LLM-as-a-Judge Tool Prompts

For tasks where score calls an LLM-based judge (which we set to be the same as the general-purpose scientist model), we use the following system and user prompts.

<svg id="A6.SS6.p2.pic1" height="476.43" overflow="visible" version="1.1" viewBox="0 0 600 476.43" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,476.43) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 476.43 L 600 476.43 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 454.88 L 599.31 454.88 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 462.19)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS6.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS6.p2.pic1.1.1.1.1.1.1">LLM Judge System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:30.92em;--ltx-fo-depth:0.2em;" width="559.25" height="430.56" transform="matrix(1 0 0 -1 0 427.79)" overflow="visible" color="#000000"><span id="A6.SS6.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS6.p2.pic1.2.2.2.1.1.1">You are an impartial judge evaluating the quality of responses provided by an AI assistant. You will be provided the instructions for the task and the assistant’s submission in response. You will decide whether or not the agent succeeded at the task. Please consider factors such as helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response. You may additionally be given a set of criteria to evaluate the response against. Do not allow the length of the response to influence your decision.</span> <span id="A6.SS6.p2.pic1.2.2.2.1.1.2">Respond precisely in the following format:</span> <span id="A6.SS6.p2.pic1.2.2.2.1.1.3"><span id="A6.SS6.p2.pic1.2.2.2.1.1.3.1">THOUGHT</span>: <span id="A6.SS6.p2.pic1.2.2.2.1.1.3.2">&lt;THOUGHT&gt;</span></span> <span id="A6.SS6.p2.pic1.2.2.2.1.1.4"><span id="A6.SS6.p2.pic1.2.2.2.1.1.4.1">DECISION</span>: <span id="A6.SS6.p2.pic1.2.2.2.1.1.4.2">&lt;DECISION&gt;<br></span></span><span id="A6.SS6.p2.pic1.2.2.2.1.1.5">In <span id="A6.SS6.p2.pic1.2.2.2.1.1.5.1">&lt;THOUGHT&gt;</span>, first briefly reason about the agent’s response and whether it meets the additional criteria.</span> <span id="A6.SS6.p2.pic1.2.2.2.1.1.6">In <span id="A6.SS6.p2.pic1.2.2.2.1.1.6.1">&lt;DECISION&gt;</span>, provide your answer as either <span id="A6.SS6.p2.pic1.2.2.2.1.1.6.2">"Yes"</span> or <span id="A6.SS6.p2.pic1.2.2.2.1.1.6.3">"No"</span>.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS6.p3.pic1" height="109.52" overflow="visible" version="1.1" viewBox="0 0 600 109.52" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,109.52) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 109.52 L 600 109.52 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 87.96 L 599.31 87.96 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 95.28)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS6.p3.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS6.p3.pic1.1.1.1.1.1.1">LLM Judge Prompt</span></span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:4.35em;--ltx-fo-depth:0.25em;" width="559.25" height="63.65" transform="matrix(1 0 0 -1 0 60.19)" overflow="visible" color="#000000"><span id="A6.SS6.p3.pic1.2.2.2.1.1" style="width:38.49em;"><pre><code>{criteria}</code></pre></span></foreignObject></g></g></svg>

### F.7 Open-ended Multiple-Choice Benchmark LLM Judge Prompts

We leverage new, open-ended versions of the common multiple-choice benchmarks MMLU, MMLU Pro, GPQA, and BBH. We discuss the details on these benchmarks in Section A.4.1 and provide the prompts used here.

For filtering the dataset, we use the following system and user prompts:

<svg id="A6.SS7.p3.pic1" height="539.93" overflow="visible" version="1.1" viewBox="0 0 600 539.93" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,539.93) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 539.93 L 600 539.93 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 518.37 L 599.31 518.37 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 525.69)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS7.p3.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS7.p3.pic1.1.1.1.1.1.1">MCQ Benchmark Filtering System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:35.51em;--ltx-fo-depth:0.2em;" width="559.25" height="494.06" transform="matrix(1 0 0 -1 0 491.29)" overflow="visible" color="#000000"><span id="A6.SS7.p3.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS7.p3.pic1.2.2.2.1.1.1">You are a professional educator. Your job is to evaluate whether a question is unambiguous and can be answered without the multiple choice options. You need to determine whether it is clear what the question is asking.</span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.2">You will be given the parsed question that you need to evaluate.</span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.3">A valid question here means:</span> <span id="A6.I9"><span id="A6.I9.i1" style="list-style-type:none;">• <span id="A6.I9.i1.p1"><span id="A6.I9.i1.p1.1">The standalone question can be answered without the multiple choice options.</span></span></span> <span id="A6.I9.i2" style="list-style-type:none;">• <span id="A6.I9.i2.p1"><span id="A6.I9.i2.p1.1">It is clear what the question is asking.</span></span></span> <span id="A6.I9.i3" style="list-style-type:none;">• <span id="A6.I9.i3.p1"><span id="A6.I9.i3.p1.1">Even if a question is posed as a text continuation task, if the continuation can be generated without the context of multiple choice options, then it is valid.</span></span></span> <span id="A6.I9.i4" style="list-style-type:none;">• <span id="A6.I9.i4.p1"><span id="A6.I9.i4.p1.1">If the question contains anything along the lines of ”Which of the following…”, then the question is not valid.</span></span></span></span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.4">Respond precisely in the following format:</span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.5"><span id="A6.SS7.p3.pic1.2.2.2.1.1.5.1">THOUGHT</span>: <span id="A6.SS7.p3.pic1.2.2.2.1.1.5.2">&lt;THOUGHT&gt;</span></span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.6"><span id="A6.SS7.p3.pic1.2.2.2.1.1.6.1">DECISION</span>: <span id="A6.SS7.p3.pic1.2.2.2.1.1.6.2">&lt;DECISION&gt;<br></span></span><span id="A6.SS7.p3.pic1.2.2.2.1.1.7">In <span id="A6.SS7.p3.pic1.2.2.2.1.1.7.1">&lt;THOUGHT&gt;</span>, briefly reason about the question and whether it can be answered without the multiple choice answers.</span> <span id="A6.SS7.p3.pic1.2.2.2.1.1.8">In <span id="A6.SS7.p3.pic1.2.2.2.1.1.8.1">&lt;DECISION&gt;</span>, provide your answer as either <span id="A6.SS7.p3.pic1.2.2.2.1.1.8.2">"Yes"</span> or <span id="A6.SS7.p3.pic1.2.2.2.1.1.8.3">"No"</span>.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS7.p4.pic1" height="59.71" overflow="visible" version="1.1" viewBox="0 0 600 59.71" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,59.71) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 59.71 L 600 59.71 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 38.15 L 599.31 38.15 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 45.47)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS7.p4.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS7.p4.pic1.1.1.1.1.1.1">MCQ Benchmark Filtering User Prompt</span></span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:0.75em;--ltx-fo-depth:0.25em;" width="559.25" height="13.84" transform="matrix(1 0 0 -1 0 10.38)" overflow="visible" color="#000000"><span id="A6.SS7.p4.pic1.2.2.2.1.1" style="width:38.49em;"><pre><code>{question}</code></pre></span></foreignObject></g></g></svg>

To evaluate a subject model’s candidate solution, we leverage the following system and user prompts:

<svg id="A6.SS7.p6.pic1" height="659.08" overflow="visible" version="1.1" viewBox="0 0 600 659.08" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,659.08) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 659.08 L 600 659.08 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 637.52 L 599.31 637.52 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 644.84)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS7.p6.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS7.p6.pic1.1.1.1.1.1.1">Benchmark Eval LLM Judge System Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.27)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:44.12em;--ltx-fo-depth:0.2em;" width="559.25" height="613.21" transform="matrix(1 0 0 -1 0 610.44)" overflow="visible" color="#000000"><span id="A6.SS7.p6.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS7.p6.pic1.2.2.2.1.1.1">You are an impartial judge evaluating the quality of responses provided by an AI assistant. You will be provided the question for the task, its multiple choice answer options, the correct ground truth solution, and the assistant’s response. You will decide whether or not the AI assistant succeeded at the task. Please consider factors such as helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response. Do not allow the length of the response to influence your decision. However, the AI assistant should respond in a clear manner and try to answer the question directly. Even if the AI assistant uses slightly different wording to the ground truth answer, as long as it provides the equivalent right answer, the response should be evaluated as correct.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.2">The question for the task is inserted between <span id="A6.SS7.p6.pic1.2.2.2.1.1.2.1">[[START OF QUESTION]]</span> and <span id="A6.SS7.p6.pic1.2.2.2.1.1.2.2">[[END OF QUESTION]]</span>.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.3">The multiple choice answer options are inserted between <span id="A6.SS7.p6.pic1.2.2.2.1.1.3.1">[[START OF MULTIPLE CHOICE OPTIONS]]</span> and <span id="A6.SS7.p6.pic1.2.2.2.1.1.3.2">[[END OF MULTIPLE CHOICE OPTIONS]]</span>.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.4">The correct ground truth solution is inserted between <span id="A6.SS7.p6.pic1.2.2.2.1.1.4.1">[[START OF GROUND TRUTH ANSWER]]</span> and <span id="A6.SS7.p6.pic1.2.2.2.1.1.4.2">[[END OF GROUND TRUTH ANSWER]]</span>.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.5">The assistant’s response is inserted between <span id="A6.SS7.p6.pic1.2.2.2.1.1.5.1">[[START OF AI ASSISTANT RESPONSE]]</span> and <span id="A6.SS7.p6.pic1.2.2.2.1.1.5.2">[[END OF AI ASSISTANT RESPONSE]]</span>.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.6">Respond precisely in the following format:</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.7"><span id="A6.SS7.p6.pic1.2.2.2.1.1.7.1">THOUGHT</span>: <span id="A6.SS7.p6.pic1.2.2.2.1.1.7.2">&lt;THOUGHT&gt;</span></span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.8"><span id="A6.SS7.p6.pic1.2.2.2.1.1.8.1">DECISION</span>: <span id="A6.SS7.p6.pic1.2.2.2.1.1.8.2">&lt;DECISION&gt;<br></span></span><span id="A6.SS7.p6.pic1.2.2.2.1.1.9">In <span id="A6.SS7.p6.pic1.2.2.2.1.1.9.1">&lt;THOUGHT&gt;</span>, briefly reason about the AI assistant’s response and whether it meets the criteria of the ground truth solution.</span> <span id="A6.SS7.p6.pic1.2.2.2.1.1.10">In <span id="A6.SS7.p6.pic1.2.2.2.1.1.10.1">&lt;DECISION&gt;</span>, provide your answer as either <span id="A6.SS7.p6.pic1.2.2.2.1.1.10.2">"Yes"</span> or <span id="A6.SS7.p6.pic1.2.2.2.1.1.10.3">"No"</span>.</span></span></foreignObject></g></g></svg>

<svg id="A6.SS7.p7.pic1" height="2136.33" overflow="visible" version="1.1" viewBox="0 0 600 2136.33" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,2136.33) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 2136.33 L 600 2136.33 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 2114.78 L 599.31 2114.78 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 2122.1)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A6.SS7.p7.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A6.SS7.p7.pic1.1.1.1.1.1.1">Benchmark Eval LLM Judge User Prompt</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:150.83em;--ltx-fo-depth:0.25em;" width="559.25" height="2090.46" transform="matrix(1 0 0 -1 0 2087)" overflow="visible" color="#000000"><span id="A6.SS7.p7.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A6.SS7.p7.pic1.2.2.2.1.1.1"><span id="A6.SS7.p7.pic1.2.2.2.1.1.1.1">[[START OF QUESTION]]</span></span><pre><code>{question}</code></pre><span id="A6.SS7.p7.pic1.2.2.2.1.1.3"><span id="A6.SS7.p7.pic1.2.2.2.1.1.3.1">[[END OF QUESTION]]</span></span> <span id="A6.SS7.p7.pic1.2.2.2.1.1.4"><span id="A6.SS7.p7.pic1.2.2.2.1.1.4.1">[[START OF MULTIPLE CHOICE OPTIONS]]</span></span><pre><code>{choices}</code></pre><span id="A6.SS7.p7.pic1.2.2.2.1.1.6"><span id="A6.SS7.p7.pic1.2.2.2.1.1.6.1">[[END OF MULTIPLE CHOICE OPTIONS]]</span></span> <span id="A6.SS7.p7.pic1.2.2.2.1.1.7"><span id="A6.SS7.p7.pic1.2.2.2.1.1.7.1">[[START OF GROUND TRUTH ANSWER]]</span></span><pre><code>{target}</code></pre><span id="A6.SS7.p7.pic1.2.2.2.1.1.9"><span id="A6.SS7.p7.pic1.2.2.2.1.1.9.1">[[END OF GROUND TRUTH ANSWER]]</span></span> <span id="A6.SS7.p7.pic1.2.2.2.1.1.10"><span id="A6.SS7.p7.pic1.2.2.2.1.1.10.1">[[START OF AI ASSISTANT RESPONSE]]</span></span><pre><code>{submission}</code></pre><span id="A6.SS7.p7.pic1.2.2.2.1.1.12"><span id="A6.SS7.p7.pic1.2.2.2.1.1.12.1">[[END OF AI ASSISTANT RESPONSE]]</span></span></span></foreignObject></g></g></svg>

## Appendix G Extended Related Work

Coevolution and Open-Endedness through LLMs. Building AI capable of unbounded innovation is a grand challenge of open-endedness [^123], which seeks to generate endless sequences of artifacts and interactions that are both novel [^119] and learnable/interesting [^55]. By studying how life coevolves with an ever-changing environment, we see a complexity explosion emerge through local competition [^79] and the coevolution of agents and environments [^136] [^137]. One important question is on how to ensure the necessary minimal criteria (MC) and filters that enable exploration to flourish, while avoiding completely undesired outcomes from dominating [^77] [^122] [^63]. [^14] [^15] (MCC) show that defining filters or MCs for both agents and environments to satisfy enables more open-ended outcomes in coevolution. Recent advances demonstrate the potential for open-endedness through LLMs [^153] [^129] [^111] [^3] [^35] [^31], where language models can generate diverse environments and challenges. AC/DC takes a first step towards discovering LLMs themselves via more open-ended search, which could subsequently power open-ended agentic search [^53] [^152]. Building on established principles of minimal criteria and coevolutionary dynamics, AC/DC applies these concepts to the joint evolution of model populations and synthetic task distributions. Additionally, while [^31] combines QD with self-play, AC/DC combines QD with population-based coevolution, which is related to MCC [^14].

Evolutionary Model Merging. Model merging can produce LLMs by combining multiple existing LLMs. Merging and testing resulting models is computationally cheaper than training models. Approaches include linear interpolation of weights [^144] [^58] or TIES [^146] and DARE [^149]. [^4] introduced evolutionary model merge (EvoMerge), automating merging by presenting a model benchmark optimization approach with CMA-ES [^48]. Subsequent works extend EvoMerge to discover LLM populations that optimize for benchmark performance [^154] while maintaining diversity via CycleQD [^72] or competition/fitness sharing (M2N2) [^1]. Unlike these approaches, AC/DC discovers LLMs that generalize to tasks without any explicit objective optimization on benchmarks. Furthermore, AC/DC can compute both quality and BCs for any LLM evaluated on synthetic task pools of any size and composition/topics (via DNS [^7]), allowing QD for the coevolution of LLMs and tasks without the limitations or rigidity of fixed niche or measurement bin interval sizes, given that skill vectors are consistent in order and size within the same generation/iteration of coevolution. Additionally, we solve the limitation of behavior characteristics (BCs) used in CQD [^72] through the fine-grained behavior signature represented in skill vectors, which uniquely distinguish models with different expertises (based on synthetic tasks solved), unlike CQD that uses binned intervals over aggregated benchmark accuracies (i.e., distinguishing model niches as unique when percentage accuracies on a benchmark for science tasks are different when aggregated, but discarding models with similar accuracies on science tasks even when such models are unique in being specialized in subfields such as physics or biology).

Novelty Search. Both Novelty Search and QD methods explicitly incorporate diversity of *behavior* into evolutionary search, i.e., encourage solutions that *do* things that are different and new. These approaches move beyond traditional optimization by encouraging continuous exploration and generation of diverse and novel artifacts. Novelty Search [^76] [^78] [^32] explicitly ranks and selects artifacts based solely on their novelty relative to previously discovered solutions, promoting continual discovery without direct reliance on predefined objectives. This approach successfully mitigates deception in search spaces and highlights the strength of novelty as a guiding principle for exploration, inspiring broader discussions about open-ended innovation [^124]. Adaptive approaches for evaluating novelty were introduced to allow for more open-ended exploration of different spaces of novelty [^95] [^109] [^34]. Unlike existing frameworks, our approach enables AC/DC to adapt to different definitions of behavior during search by leveraging the skill vector as a means of flexibly measuring behavioral diversity during task adaptation and coevolution.

Quality-Diversity (QD). QD [^112] [^29] [^20] explicitly optimizes both diversity and high-quality performance, while maintaining a structured collection (archive) of diverse high-quality solutions with unique behavior characteristics (BCs). Influential algorithms such as MAP-Elites [^98] [^28] emphasize local competition within niches [^79] to systematically explore and optimize throughout a diverse behavior space. Extensions include methods for efficiently handling higher-dimensional descriptor spaces and novel mutation operators [^131] [^132] [^37] [^27] [^26] [^36]. Existing methods handle the complexity and adaptation of diverse high-quality search spaces through either a meta-adaptation approach [^12] or learned parametrized behavior functions [^42] [^68] [^67] [^9] [^85] [^155] [^108] [^46]. Different to existing paradigms of search space adaptation and known QD applications, skill vectors in our framework, AC/DC, naturally represent both quality and behavior (for diversity), while being simple to adapt to the composition and size of synthetic task pools during coevolution.

Synthetic Data for LLMs. In the direction of synthetic data for evaluating LLM capabilities, early work has explored prompting LLMs to rewrite existing LLM benchmark tasks into variants of those tasks, as well as having LLMs generate example yes/no questions [^110]. They demonstrated that model-written evaluations can discover LLM capabilities and weaknesses that manually curated benchmarks fail to reveal. Instead of being constrained to training on internet data, many works show that LLMs can generate effective text training data [^140] [^92] [^88] of increasing quality, diversity, and complexity, starting from seed text data [^13] [^111] [^116] [^49] (where QD approaches help). Synthetic training signals can also be obtained through LLM-generated preference data [^8] or task solution reward [^156]. [^91], a method we build upon, show that principles of open-ended search can generate surprisingly new tasks that reveal unexpected capabilities or weaknesses in LLMs. To the best of our understanding, AC/DC leverages synthetic data to demonstrate the first instance of diverse LLM-generated tasks coevolving with a population of LLMs, rather than fine-tuning just one LLM.

Multi-Agent Systems and Best-of-N Strategies. The gap between coverage metrics (pass@k, oracle accuracy, our proposed Coverage) and practical single-answer selection represents a fundamental challenge in LLM evaluation. The pass@k metric [^22] measures whether at least one correct answer exists among k samples, with coverage scaling log-linearly over orders of magnitude [^16], yet recent work demonstrates pass@k serves as a diagnostic tool rather than an effective optimization objective [^150], highlighting that generating correct answers and selecting them are fundamentally different problems. Recent advances in test-time compute scaling have shown that optimal strategies are problem-dependent, with adaptive allocation of inference compute outperforming fixed sampling budgets [^121], and tree search methods enabling principled exploration-exploitation trade-offs [^59]; while these approaches focus on improving individual model reasoning through extended inference, AC/DC generates diverse model populations with complementary capabilities scaling on the number of model axis. Self-consistency via majority voting [^139] has become the standard baseline for aggregating multiple samples from a single model. However, majority voting assumes samples from a single model with homogeneous capabilities and has been shown to overlook informative minority responses [^54] and can even degrade performance in certain settings [^138]. In contrast, our work explicitly seeks to evolve distinct specialist models whose complementary capabilities should not be aggregated via simple majority rule, which would suppress the unique perspectives we aim to discover. Beyond voting methods, reward model-based selection suffers from reward hacking when models have imperfect alignment with true objectives [^84] [^64], while LLM judge-based approaches exhibit systematic biases including position bias and verbosity bias [^157] [^118]. We explore three simple selection strategies-tournament-style judge selection, single-prompt judge selection, and reward model scoring-finding that all exhibit substantial gaps between Coverage and single-answer performance. Multi-agent debate and collaborative systems [^83] [^61] [^33] represent alternative approaches, though recent work questions their reliability compared to simpler methods [^120], while ensemble diversity from heterogeneous models shows promise [^128]; these collaborative techniques are orthogonal to our evolutionary discovery process and represent promising future directions for answer aggregation from evolved populations.

Alternative Model Output Diversity Methods. Model output diversity (of meaningful quality) remains a challenge that, if unsolved, would impede the ability of LLMs to return diverse responses that may solve different problems [^13] [^70] [^105] [^82]. To facilitate more divergent outputs from LLMs, prior work introduced methods to facilitate diverse outputs through approaches such as encouraging semantic diversity during output sampling [^134] [^38] [^39] [^49], diversity-inducing optimization of a single model [^74] [^23] [^62], or even facilitating diverse persona generation [^106] [^19] as a possible approach of introducing input diversity in prompting for more diverse outputs. While these methods can facilitate model (output) diversity for the sake of primarily diversity, our method, AC/DC, approaches the problem with a fundamentally different solution, by automatically generating multiple models with diverse task-solving capabilities. Our approach takes a direct step towards tackling the challenge of facilitating model diversity for the sake of facilitating both diverse and useful outputs, that can lead to correct solutions for knowledge-based tasks.

## Appendix H Human Study

### H.1 Human Study Methodology

We conducted a human evaluation study with 94 independent assessments (45 synthetic, 49 benchmark tasks) across three expert reviewers to validate task quality and novelty. Our protocol incorporated multiple bias mitigation strategies:

Blind Evaluation Protocol: Task sources (synthetic vs. benchmark) were completely hidden from reviewers during evaluation, preventing confirmation bias and ensuring objective assessment.

Balanced Sampling Design: Tasks were sampled using a controlled 50/50 distribution (50% synthetic, 50% distributed across 8 our benchmarks), ensuring fair comparison without overrepresentation.

Similarity-Based Calibration: For each task, reviewers were shown the 3 most similar benchmark tasks (via embedding-based retrieval) to establish a concrete reference point when assessing out-of-distribution characteristics—this grounds the OOD metric in actual distributional differences rather than subjective perception.

Standardized Evaluation Criteria: All reviewers received detailed written guidelines (see Section H.3) defining correctness, creativity, and OOD characteristics, ensuring consistent interpretation across annotators.

Statistical Validation: We verified inter-rater reliability using chi-square tests, confirming strong agreement on objective metrics (correctness: $p=0.46$, OOD: $p=0.57$), which validates that our findings are not driven by individual annotator biases.

This multi-layered approach ensures our human evaluation provides reliable, unbiased evidence for synthetic task quality and distributional novelty.

### H.2 Human Study Results

Our evaluation demonstrates that synthetically generated tasks achieve high quality while exhibiting noticeable distributional novelty as shown in the results of Tab. 4.

Synthetic Task Validation: The 97.8% correctness rate demonstrates that our generation approach is capable of producing high-quality, well-formed, solvable, and meaningful tasks. Nearly 70% of synthetic tasks were rated as out-of-distribution compared to established benchmarks, providing strong evidence that our approach successfully generates novel task types beyond existing evaluation datasets. Notably, we expect a certain percentage of “in-distribution” tasks, as core math and code tasks are likely to be similar. Over one-third (37.8%) were rated as creative, indicating they explore problem-solving approaches not commonly tested by standard benchmarks.

Benchmark Baseline Validation: As expected, benchmark tasks showed substantially lower OOD (10.2%) and creativity (6.1%) ratings, confirming that reviewers correctly identified established benchmark tasks as in-distribution. Notably, the benchmark tasks rated as OOD or creative were concentrated exclusively in the most challenging benchmarks—MMLU-Pro (33.3% OOD, 16.7% creative) and GPQA (16.7% OOD, 16.7% creative)—while all other benchmarks (BBH, GSM8K, MATH, HumanEval, MBPP, MMLU) received 0% OOD and 0% creative ratings. This pattern validates our evaluation protocol: reviewers appropriately recognized that graduate-level and expert-domain questions may appear novel due to their complexity, while correctly identifying that standard benchmarks are in-distribution. This serves as a sanity check confirming the reliability of our human evaluation.

Inter-Rater Reliability: Statistical analysis confirms strong inter-rater agreement on objective metrics (correctness: $p=0.46$, OOD: $p=0.57$), demonstrating that our findings are robust and not driven by individual annotator biases. While the creativity metric showed expected variability ($p=0.02$) due to its inherently subjective nature, the pattern remained consistent: synthetic tasks received substantially higher creativity ratings across all three reviewers (ranging from 21.4% to 69.2%), compared to benchmark tasks (0% to 17.6%).

### H.3 Labeling Guidelines

#### H.3.1 Correctness

<svg id="A8.SS3.SSS1.p1.pic1" height="271.18" overflow="visible" version="1.1" viewBox="0 0 600 271.18" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,271.18) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 271.18 L 600 271.18 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 252.47 L 599.31 252.47 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 257.1)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A8.SS3.SSS1.p1.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A8.SS3.SSS1.p1.pic1.1.1.1.1.1.1">CORRECTNESS EVALUATION GUIDELINES</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:16.29em;--ltx-fo-depth:0.19em;" width="559.25" height="228.16" transform="matrix(1 0 0 -1 0 225.47)" overflow="visible" color="#000000"><span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.1">A task is considered CORRECT if:</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.2">The instruction is clear and unambiguous</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.3">The instruction can be understood and executed by a human or AI</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.4">If it’s a question, it has a well-defined answer</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.5">The task does not contain logical contradictions</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.6">The task specification is internally consistent</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.7">The requirements are feasible to implement/answer</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.8">A task is considered INCORRECT if:</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.9">The instruction is unclear, ambiguous, or confusing</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.10">The task contains logical errors or contradictions</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.11">The task is impossible to solve or implement</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.12">Critical information is missing</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.13">The task specification is self-contradictory</span> <span id="A8.SS3.SSS1.p1.pic1.2.2.2.1.1.14">Note: Focus on the task definition itself, not on potential implementation details.</span></span></foreignObject></g></g></svg>

#### H.3.2 Out-of-Distribution

<svg id="A8.SS3.SSS2.p1.pic1" height="342.75" overflow="visible" version="1.1" viewBox="0 0 600 342.75" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,342.75) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 342.75 L 600 342.75 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 319.66 L 599.31 319.66 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 327.74)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.75em;--ltx-fo-depth:0.25em;" width="559.25" height="13.84" transform="matrix(1 0 0 -1 0 10.38)" overflow="visible" color="#FFFFFF"><span id="A8.SS3.SSS2.p1.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A8.SS3.SSS2.p1.pic1.1.1.1.1.1.1">OUT-OF-DISTRIBUTION (OOD) EVALUATION GUIDELINES</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:21.15em;--ltx-fo-depth:0.19em;" width="559.25" height="295.34" transform="matrix(1 0 0 -1 0 292.65)" overflow="visible" color="#000000"><span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.1">A task is considered OUT-OF-DISTRIBUTION (OOD) if:</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.2">It’s unlikely to appear in standard AI benchmarks or datasets</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.3">It requires knowledge or skills not commonly tested</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.4">It involves unusual domain combinations</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.5">It requires novel reasoning patterns</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.6">It would be difficult to find similar examples in typical training data</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.7">It tests capabilities in unexpected or underexplored ways</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.8">A task is considered IN-DISTRIBUTION (not OOD) if:</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.9">It resembles common benchmark tasks (MMLU, GSM8K, HumanEval, etc.)</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.10">It’s a standard problem type from textbooks or courses</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.11">It follows well-known problem patterns</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.12">Similar examples are abundant in typical training datasets</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.13">It tests standard, frequently-evaluated capabilities</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.14">Key question to ask:</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.15">”Would this task likely appear in existing AI benchmarks or training data?”</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.16">If NO → likely OOD</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.17">If YES → likely in-distribution</span> <span id="A8.SS3.SSS2.p1.pic1.2.2.2.1.1.18">Note: A task can be creative but still in-distribution, or vice versa.</span></span></foreignObject></g></g></svg>

#### H.3.3 Creativity

<svg id="A8.SS3.SSS3.p1.pic1" height="387.41" overflow="visible" version="1.1" viewBox="0 0 600 387.41" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,387.41) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 387.41 L 600 387.41 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 368.7 L 599.31 368.7 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 373.33)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A8.SS3.SSS3.p1.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A8.SS3.SSS3.p1.pic1.1.1.1.1.1.1">CREATIVITY EVALUATION GUIDELINES</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:24.69em;--ltx-fo-depth:0.19em;" width="559.25" height="344.39" transform="matrix(1 0 0 -1 0 341.7)" overflow="visible" color="#000000"><span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.1">A task is considered CREATIVE if:</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.2">It presents a novel or unusual problem formulation</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.3">It combines concepts in interesting or unexpected ways</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.4">It requires non-trivial reasoning or problem-solving</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.5">It goes beyond simple variations of common tasks</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.6">It demonstrates originality in approach or domain</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.7">It would be interesting or engaging to solve</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.8">A task is considered NOT CREATIVE if:</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.9">It’s a straightforward, routine task</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.10">It’s a simple variation of a very common problem</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.11">It requires only basic, mechanical operations</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.12">It’s a standard textbook-style problem</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.13">It lacks novelty or originality</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.14">Examples of creative tasks:</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.15">- Novel combinations of domains (e.g., applying game theory to music composition)</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.16">- Tasks requiring multi-step creative reasoning</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.17">- Problems with interesting constraints or twists</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.18">Examples of non-creative tasks:</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.19">- Simple arithmetic calculations</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.20">- Basic data structure operations</span> <span id="A8.SS3.SSS3.p1.pic1.2.2.2.1.1.21">- Standard classification problems</span></span></foreignObject></g></g></svg>

## Appendix I Comparison of Seed Models and Merged Models on Synthetic Data

### I.1 Quantitative Analysis

#### I.1.1 Performance Across Model Families

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/fitness_comparison.png)

Figure 11: Comparison of three seed models to the three fittest merged models on the global synthetic task pool.

We conducted an analysis comparing the fitness of seed models and merged models across four model families (Qwen2, Qwen2.5, Qwen3, and DeepSeek) on their respective complete synthetic datasets. Table 21 summarizes the fitness scores and improvements for each family.

Table 21: Model merging performance across different model families. Improvements are calculated as a percentage change from the seed model performance.

<table><tbody><tr><td>Family</td><td>Tasks</td><td colspan="2">Seed Models</td><td colspan="2">Top-3 Merged</td><td>Avg Imp.</td></tr><tr><td></td><td></td><td>Avg</td><td>Max</td><td>Avg</td><td>Max</td><td></td></tr><tr><td>Qwen2.5</td><td>1,094</td><td>0.5253</td><td>0.5622</td><td>0.6252</td><td>0.6353</td><td>+19.0%</td></tr><tr><td>Qwen3</td><td>1,044</td><td>0.5361</td><td>0.5661</td><td>0.6255</td><td>0.6255</td><td>+16.7%</td></tr><tr><td>Qwen2</td><td>1,117</td><td>0.3405</td><td>0.5058</td><td>0.6085</td><td>0.6132</td><td>+78.7%</td></tr><tr><td>DeepSeek</td><td>1,005</td><td>0.3032</td><td>0.4418</td><td>0.4163</td><td>0.4179</td><td>+37.3%</td></tr></tbody></table>

Fig. 11 further illustrates the fitness distributions for seed models versus merged models across all four families. The fitness improvements vary significantly across families, with Qwen2 showing the highest average improvement (+78.7%) starting from the generally weakest seed model (0.34), while Qwen2.5 and Qwen3, despite having higher seed baselines (0.53 and 0.54, respectively), show more moderate improvements (+19.0% and +16.7%).

In Fig. 11 we can clearly observe that our three merged models per model family, all exhibit high fitness scores on the diverse synthetic data, whereas all seed models, especially the heavily finetuned and specialized seed models, such as the math and code experts, perform weaker on the diverse data. Notably, the general-purpose instruct model is also weaker on the synthetic data than all our merged models, except for the DeepSeek experiment, where it is roughly on par.

To understand the complementarity between seed and merged models, we analyzed confusion matrices showing task-level success patterns. Fig. 12 presents these matrices using the following criteria: (1) All seeds fail, merged succeed: all seed models fail (score=0.0) and at least one merged model succeeds (score=1.0); (2) Seeds succeed, all merged fail: at least one seed succeeds and all merged models fail; (3) Both succeed: at least one seed and one merged model succeed; (4) Both fail: all models fail.

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/confusion_matrix.png)

Figure 12: Confusion matrix of synthetic tasks where all models merged and seed models failed and at least one model succeeded. We show the confusion matrices for the experiments with all model families.

The confusion matrices reveal complementarity patterns. For Qwen 2, merged models succeed on 153 of tasks where all seeds fail, while completely failing on only 23 of tasks where seeds succeed. Improvement patterns emerge across Qwen 2.5 and Qwen 3, demonstrating that merging preserves most seed capabilities while adding new ones. Nevertheless, for DeepSeek, we see that this pattern is reversed, where seed models succeed on 149 tasks where merged models fail whilst merged models succeed at only 100 tasks where seed models fail.

These findings demonstrate that our individual merged models improve over the individual seed models.

#### I.1.2 Enhanced Performance on Out-of-Distribution Tasks

To investigate whether model merging provides differential benefits for challenging tasks, we evaluated Qwen2.5 on the set of 31 out-of-distribution (OOD) synthetic tasks identified through our human study (see Appendix App. H). Tab. 22 compares performance on the full task set versus the OOD subset.

Table 22: Fitness improvement of Qwen2.5 merged models vs seed expert models on all synthetic tasks and those labeled as OOD. The improvement differential demonstrates stronger benefits on challenging tasks that are not commonly evaluated in standard benchmarks, which the seed models are optimized for.

| Metric | All Tasks | OOD+Synthetic | Difference |
| --- | --- | --- | --- |
|  | (1,094 tasks) | (31 tasks) |  |
| Avg fitness improvement | +19.0% | +44.0% | +25.0pp |
| Max fitness improvement | +13.0% | +31.6% | +18.6pp |

The results reveal that merged models show 2.3× stronger average improvement on OOD+synthetic tasks compared to the full task set.

Fig. 13 visualizes the fitness distributions for the OOD task subset. The fitness comparison shows merged models achieving substantially higher scores (avg 0.7742, max 0.8065) compared to seeds (avg 0.5376, max 0.6129).

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/qwen2.5_fitness_comparison.png)

Figure 13: Qwen2.5 performance on 31 human-labeled OOD and synthetic tasks (see App. H ), showing improved performance compared to seed models.

These findings suggest that model merging is particularly valuable for out-of-distribution scenarios requiring diverse skill integration, where the emergent capabilities of merged models discover via coevolution on a diverse set of synthetic tasks, provides novel capabilities not captured by individual seed models.

### I.2 Qualitative Analysis

To understand the types of tasks where merging provides benefits, we examine specific examples where at least one merged model succeeds while all seed models fail. We present representative cases from both in-distribution and OOD task categories.

#### I.2.1 In-Distribution Tasks

(qwen2.5) task\_630\_advanced\_probability\_and\_combinatorics

<svg id="A9.SS2.SSS1.p2.pic1" height="105.14" overflow="visible" version="1.1" viewBox="0 0 600 105.14" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,105.14) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 105.14 L 600 105.14 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 86.43 L 599.31 86.43 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 91.06)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p2.pic1.1.1.1.1.1.1">Instruction</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:4.29em;--ltx-fo-depth:0.19em;" width="559.25" height="62.11" transform="matrix(1 0 0 -1 0 59.42)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p2.pic1.2.2.2.1.1.1">A box contains 5 red, 3 blue, and 2 green balls. Two balls are drawn without replacement. What is the probability that both balls are red, given that at least one ball is red?</span> <span id="A9.SS2.SSS1.p2.pic1.2.2.2.1.1.2">Provide your answer as a simplified fraction. Provide your answer in the specified format. Do not include any additional text or explanations.</span></span></foreignObject></g></g></svg>

<svg id="A9.SS2.SSS1.p3.pic1" height="291.4" overflow="visible" version="1.1" viewBox="0 0 600 291.4" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,291.4) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#1B701B;" fill="#1B701B" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 291.4 L 600 291.4 L 600 0 Z"></path></g><g style="--ltx-fill-color:#D3E8D3;" fill="#D3E8D3" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 269.84 L 599.31 269.84 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 277.16)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p3.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p3.pic1.1.1.1.1.1.1">Merged Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:17.49em;--ltx-fo-depth:0.25em;" width="559.25" height="245.53" transform="matrix(1 0 0 -1 0 242.07)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.1">Number of red balls = 5</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.2">number of blue balls = 3</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.3">number of green balls = 2</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.4">total number of balls = 5 + 3 + 2 = 10</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.5">Probability of drawing at least one red ball:</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.6">- Case 1: Drawing two red balls</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.7">Probability = (5/10) * (4/9) = 20/90 = 2/9</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.8">- Case 2: Drawing one red and one non-red ball</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.9">Probability = (5/10) * (5/9) + (5/10) * (5/9) = 50/90 = 5/9</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.10">Total probability of at least one red ball = 2/9 + 5/9 = 7/9</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.11">Probability of drawing two red balls given that at least one is red:</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.12">- Total probability of at least one red ball = 7/9</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.13">- Probability of drawing two red balls = 2/9</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.14">Conditional probability = (2/9) / (7/9) = 2/7</span> <span id="A9.SS2.SSS1.p3.pic1.2.2.2.1.1.15">Answer: 2/7</span></span></foreignObject></g></g></svg>

<svg id="A9.SS2.SSS1.p4.pic1" height="58.45" overflow="visible" version="1.1" viewBox="0 0 600 58.45" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,58.45) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#CC2222;" fill="#CC2222" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 58.45 L 600 58.45 L 600 0 Z"></path></g><g style="--ltx-fill-color:#FFD5D5;" fill="#FFD5D5" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 36.89 L 599.31 36.89 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 44.21)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p4.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p4.pic1.2.2.2.1.1.1">Math Expert</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.62)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0.23em;" width="559.25" height="12.58" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p4.pic1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p4.pic1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1">Answer: <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="\frac{5}{14}"><semantics><mfrac><mn>5</mn> <mn>14</mn></mfrac> <annotation encoding="application/x-tex">\frac{5}{14}</annotation></semantics></math></span></span></foreignObject></g></g></svg>

The merged model correctly applies Bayes’ theorem. In contrast, the math expert does not provide any reasoning trace and provides an incorrect answer

(qwen2.5) task\_549\_advanced\_mathematical\_proofs

<svg id="A9.SS2.SSS1.p7.pic1" height="72.7" overflow="visible" version="1.1" viewBox="0 0 600 72.7" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,72.7) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 72.7 L 600 72.7 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 53.99 L 599.31 53.99 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 58.62)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p7.pic1.4.4.4.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p7.pic1.4.4.4.1.1.1">Instruction</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.96)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:1.89em;--ltx-fo-depth:0.25em;" width="559.25" height="29.67" transform="matrix(1 0 0 -1 0 26.21)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p7.pic1.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3" style="width:40.42em;"><span id="A9.SS2.SSS1.p7.pic1.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3">Generate a step-by-step mathematical proof for the following statement: Prove that for any integer <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&gt;1"><semantics><mrow><mi>n</mi> <mo>&gt;</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">n&gt;1</annotation></semantics></math>, there exists a prime number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&lt;p&lt;2n"><semantics><mrow><mi>n</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">n&lt;p&lt;2n</annotation></semantics></math> (Bertrand’s Postulate).</span></span></foreignObject></g></g></svg>

<svg id="A9.SS2.SSS1.p8.pic1" height="8329.85" overflow="visible" version="1.1" viewBox="0 0 600 8329.85" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,8329.85) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#1B701B;" fill="#1B701B" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 8329.85 L 600 8329.85 L 600 0 Z"></path></g><g style="--ltx-fill-color:#D3E8D3;" fill="#D3E8D3" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 8308.3 L 599.31 8308.3 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 8315.61)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p8.pic1.11.11.11.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p8.pic1.11.11.11.1.1.1">Merged Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:598.49em;--ltx-fo-depth:0.19em;" width="559.25" height="8283.98" transform="matrix(1 0 0 -1 0 8281.29)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p8.pic1.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10" style="width:40.42em;"><span id="A9.SS2.SSS1.p8.pic1.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4">To prove Bertrand’s Postulate, we will use the Prime Number Theorem and some properties of the factorial function. The Prime Number Theorem states that the number of primes less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="x"><semantics><mi>x</mi> <annotation encoding="application/x-tex">x</annotation></semantics></math>, denoted by <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="\pi(x)"><semantics><mrow><mi>π</mi> <mo lspace="0em" rspace="0em"></mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></mrow> <annotation encoding="application/x-tex">\pi(x)</annotation></semantics></math>, is approximately <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="\frac{x}{\log x}"><semantics><mfrac><mi>x</mi> <mrow><mi>log</mi> <mo lspace="0.167em">⁡</mo> <mi>x</mi></mrow></mfrac> <annotation encoding="application/x-tex">\frac{x}{\log x}</annotation></semantics></math> as <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="x"><semantics><mi>x</mi> <annotation encoding="application/x-tex">x</annotation></semantics></math> approaches infinity. However, for our purposes, we will use a more elementary approach.</span> <span id="A9.I1"><span id="A9.I1.i1" style="list-style-type:none;">1. <span id="A9.I1.i1.p1"><span id="A9.I1.i1.p1.1"><span id="A9.I1.i1.p1.1.1">Step 1: Consider the factorial function and its properties.</span></span></span> <span id="A9.I1.i1.p2"><span id="A9.I1.i1.p2.3">The factorial function <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n!"><semantics><mrow><mi>n</mi><mo>!</mo></mrow><annotation encoding="application/x-tex">n!</annotation></semantics></math> (n factorial) is the product of all positive integers up to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>. For example, <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="5!=5\times 4\times 3\times 2\times 1=120"><semantics><mrow><mrow><mn>5</mn><mo>!</mo></mrow><mo>=</mo> <mrow><mn>5</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>4</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>3</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>1</mn></mrow> <mo>=</mo> <mn>120</mn></mrow> <annotation encoding="application/x-tex">5!=5\times 4\times 3\times 2\times 1=120</annotation></semantics></math>.</span></span></span> <span id="A9.I1.i2" style="list-style-type:none;">2. <span id="A9.I1.i2.p1"><span id="A9.I1.i2.p1.1"><span id="A9.I1.i2.p1.1.1">Step 2: Use the factorial function to find a lower bound for the number of primes.</span></span></span> <span id="A9.I1.i2.p2"><span id="A9.I1.i2.p2.2">We will use the fact that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="(n!)^{2}"><semantics><msup><mrow><mo stretchy="false">(</mo><mrow><mi>n</mi><mo>!</mo></mrow><mo stretchy="false">)</mo></mrow> <mn>2</mn></msup> <annotation encoding="application/x-tex">(n!)^{2}</annotation></semantics></math> (the square of <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n!"><semantics><mrow><mi>n</mi><mo>!</mo></mrow><annotation encoding="application/x-tex">n!</annotation></semantics></math>) can be expressed in terms of factorials of smaller numbers. Specifically, we have:</span> <span id="A9.Ex1"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block" data-latex="(n!)^{2}=n!\times n!=n\times(n-1)\times(n-2)\times\cdots\times 2\times 1\times n\times(n-1)\times(n-2)\times\cdots\times 2\times 1"><semantics><mrow><msup><mrow><mo stretchy="false">(</mo><mrow><mi>n</mi><mo>!</mo></mrow><mo stretchy="false">)</mo></mrow> <mn>2</mn></msup> <mo>=</mo> <mrow><mrow><mi>n</mi><mo rspace="0.055em">!</mo></mrow><mo rspace="0.222em">×</mo> <mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>=</mo> <mrow><mi>n</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>1</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>2</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mi mathvariant="normal">⋯</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>1</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mi>n</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>1</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>2</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mi mathvariant="normal">⋯</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>1</mn></mrow></mrow> <annotation encoding="application/x-tex">(n!)^{2}=n!\times n!=n\times(n-1)\times(n-2)\times\cdots\times 2\times 1\times n\times(n-1)\times(n-2)\times\cdots\times 2\times 1</annotation></semantics></math> </span><span id="A9.I1.i2.p2.6">This can be rewritten as:</span> <span id="A9.Ex2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block" data-latex="(n!)^{2}=n\times(n!)\times(n-1)\times(n-2)\times\cdots\times 2\times 1\times n\times(n-1)\times(n-2)\times\cdots\times 2\times 1"><semantics><mrow><msup><mrow><mo stretchy="false">(</mo><mrow><mi>n</mi><mo>!</mo></mrow><mo stretchy="false">)</mo></mrow> <mn>2</mn></msup> <mo>=</mo> <mrow><mi>n</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi><mo>!</mo></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>1</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>2</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mi mathvariant="normal">⋯</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>1</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mi>n</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>1</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>−</mo> <mn>2</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mi mathvariant="normal">⋯</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>1</mn></mrow></mrow> <annotation encoding="application/x-tex">(n!)^{2}=n\times(n!)\times(n-1)\times(n-2)\times\cdots\times 2\times 1\times n\times(n-1)\times(n-2)\times\cdots\times 2\times 1</annotation></semantics></math> </span><span id="A9.I1.i2.p2.5">Notice that each term in the product is a multiple of a prime number less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="(n!)^{2}"><semantics><msup><mrow><mo stretchy="false">(</mo><mrow><mi>n</mi><mo>!</mo></mrow><mo stretchy="false">)</mo></mrow> <mn>2</mn></msup> <annotation encoding="application/x-tex">(n!)^{2}</annotation></semantics></math> is divisible by all primes less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>.</span></span></span> <span id="A9.I1.i3" style="list-style-type:none;">3. <span id="A9.I1.i3.p1"><span id="A9.I1.i3.p1.2"><span id="A9.I1.i3.p1.2.2">Step 3: Use the properties of the factorial function to find a prime between <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math> and <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow> <annotation encoding="application/x-tex">2n</annotation></semantics></math>.</span></span></span> <span id="A9.I1.i3.p2"><span id="A9.I1.i3.p2.1">Consider the number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><annotation encoding="application/x-tex">2n!</annotation></semantics></math>. We can write:</span> <span id="A9.Ex3"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block" data-latex="2n!=2\times n!\times(n+1)\times(n+2)\times\cdots\times 2n"><semantics><mrow><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>=</mo> <mrow><mrow><mn>2</mn> <mo lspace="0.222em" rspace="0.222em">×</mo> <mrow><mi>n</mi><mo rspace="0.055em">!</mo></mrow><mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>+</mo> <mn>1</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mrow><mo stretchy="false">(</mo><mrow><mi>n</mi> <mo>+</mo> <mn>2</mn></mrow><mo rspace="0.055em" stretchy="false">)</mo></mrow> <mo rspace="0.222em">×</mo> <mi mathvariant="normal">⋯</mi> <mo lspace="0.222em" rspace="0.222em">×</mo> <mn>2</mn></mrow> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">2n!=2\times n!\times(n+1)\times(n+2)\times\cdots\times 2n</annotation></semantics></math> </span><span id="A9.I1.i3.p2.8">Notice that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><annotation encoding="application/x-tex">2n!</annotation></semantics></math> is divisible by all primes less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math> (as shown in Step 2). Now, consider the number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!-1"><semantics><mrow><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>−</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">2n!-1</annotation></semantics></math>. This number is not divisible by any prime less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math> because <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><annotation encoding="application/x-tex">2n!</annotation></semantics></math> is divisible by all such primes, and subtracting 1 from a multiple of a prime <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> results in a number that is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math>.</span></span></span> <span id="A9.I1.i4" style="list-style-type:none;">4. <span id="A9.I1.i4.p1"><span id="A9.I1.i4.p1.1"><span id="A9.I1.i4.p1.1.1">Step 4: Conclude the proof using the properties of <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!-1"><semantics><mrow><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>−</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">2n!-1</annotation></semantics></math>.</span></span></span> <span id="A9.I1.i4.p2"><span id="A9.I1.i4.p2.7">Since <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!-1"><semantics><mrow><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>−</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">2n!-1</annotation></semantics></math> is not divisible by any prime less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>, it must be divisible by a prime <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&lt;p\leq 2n"><semantics><mrow><mi>n</mi> <mo>&lt;</mo> <mi>p</mi> <mo>≤</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">n&lt;p\leq 2n</annotation></semantics></math>. This is because the only primes that could divide <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n!-1"><semantics><mrow><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mrow><mi>n</mi><mo>!</mo></mrow></mrow><mo>−</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">2n!-1</annotation></semantics></math> are those greater than <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math> and less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2n"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow> <annotation encoding="application/x-tex">2n</annotation></semantics></math>.</span></span></span></span> <span id="A9.SS2.SSS1.p8.pic1.7.7.7.7.7.7.7.7.7.7.7.7.7.7.7.7.7.7">Therefore, we have shown that for any integer <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&gt;1"><semantics><mrow><mi>n</mi> <mo>&gt;</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">n&gt;1</annotation></semantics></math>, there exists a prime number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&lt;p&lt;2n"><semantics><mrow><mi>n</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">n&lt;p&lt;2n</annotation></semantics></math>. This completes the proof of Bertrand’s Postulate.</span> <span id="A9.SS2.SSS1.p8.pic1.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10"><span id="A9.SS2.SSS1.p8.pic1.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.10.1">Answer:</span> Bertrand’s Postulate is proven by showing that for any integer <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&gt;1"><semantics><mrow><mi>n</mi> <mo>&gt;</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">n&gt;1</annotation></semantics></math>, there exists a prime number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&lt;p&lt;2n"><semantics><mrow><mi>n</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">n&lt;p&lt;2n</annotation></semantics></math>.</span></span></foreignObject></g></g></svg>

<svg id="A9.SS2.SSS1.p9.pic1" height="1348.82" overflow="visible" version="1.1" viewBox="0 0 600 1348.82" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,1348.82) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#CC2222;" fill="#CC2222" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 1348.82 L 600 1348.82 L 600 0 Z"></path></g><g style="--ltx-fill-color:#FFD5D5;" fill="#FFD5D5" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 1327.26 L 599.31 1327.26 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 1334.58)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SS2.SSS1.p9.pic1.5.5.5.1.1" style="width:40.42em;"><span id="A9.SS2.SSS1.p9.pic1.5.5.5.1.1.1">Code Expert</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:93.97em;--ltx-fo-depth:0.19em;" width="559.25" height="1302.95" transform="matrix(1 0 0 -1 0 1300.26)" overflow="visible" color="#000000"><span id="A9.SS2.SSS1.p9.pic1.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.1"><span id="A9.SS2.SSS1.p9.pic1.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.1.p1"><span id="A9.SS2.SSS1.p9.pic1.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3.3">To prove Bertrand’s Postulate, which states that for any integer <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&gt;1"><semantics><mrow><mi>n</mi> <mo>&gt;</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">n&gt;1</annotation></semantics></math>, there exists a prime number <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n&lt;p&lt;2n"><semantics><mrow><mi>n</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow></mrow> <annotation encoding="application/x-tex">n&lt;p&lt;2n</annotation></semantics></math>, we can use a combination of mathematical induction and properties of prime numbers. The proof is quite involved and requires careful analysis. Let’s proceed step by step.</span></span><section id="A9.SSx1"><h3>Approach</h3><span id="A9.SSx1.p1"><span id="A9.I2"><span id="A9.I2.i1" style="list-style-type:none;">1. <span id="A9.I2.i1.p1"><span id="A9.I2.i1.p1.1"><span id="A9.I2.i1.p1.1.1">Base Case</span>: Verify the statement for small values of <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>.</span></span></span> <span id="A9.I2.i2" style="list-style-type:none;">2. <span id="A9.I2.i2.p1"><span id="A9.I2.i2.p1.1"><span id="A9.I2.i2.p1.1.1">Inductive Hypothesis</span>: Assume the statement holds for all integers up to some <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="k"><semantics><mi>k</mi> <annotation encoding="application/x-tex">k</annotation></semantics></math>.</span></span></span> <span id="A9.I2.i3" style="list-style-type:none;">3. <span id="A9.I2.i3.p1"><span id="A9.I2.i3.p1.1"><span id="A9.I2.i3.p1.1.1">Inductive Step</span>: Prove the statement for <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="k+1"><semantics><mrow><mi>k</mi> <mo>+</mo> <mn>1</mn></mrow> <annotation encoding="application/x-tex">k+1</annotation></semantics></math> using the inductive hypothesis and other properties of primes.</span></span></span></span></span></section><section id="A9.SSx2"><h3>Solution Code</h3><span id="A9.SSx2.p1"><pre><code>def bertrands_postulate(n):
    if n &lt;= 1:
        return False
    # Check for primes in the range (n, 2n)
    for p in range(n + 1, 2 * n + 1):
        if is_prime(p):
            return True
    return False

def is_prime(num):
    if num &lt;= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num %
            return False
    return True

# Test the function with some values
print(bertrands_postulate(2))  # True
print(bertrands_postulate(3))  # True
print(bertrands_postulate(5))  # True
print(bertrands_postulate(10)) # True</code></pre></span></section><section id="A9.SSx3"><h3>Explanation</h3><span id="A9.SSx3.p1"><span id="A9.I3"><span id="A9.I3.i1" style="list-style-type:none;">1. <span id="A9.I3.i1.p1"><span id="A9.I3.i1.p1.4"><span id="A9.I3.i1.p1.4.1">Base Case</span>: For <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n=2"><semantics><mrow><mi>n</mi> <mo>=</mo> <mn>2</mn></mrow> <annotation encoding="application/x-tex">n=2</annotation></semantics></math>, the primes between 2 and 4 are 3, which satisfies the condition. For <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n=3"><semantics><mrow><mi>n</mi> <mo>=</mo> <mn>3</mn></mrow> <annotation encoding="application/x-tex">n=3</annotation></semantics></math>, primes between 3 and 6 are 3 and 5, but 5 is in the range. For <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n=5"><semantics><mrow><mi>n</mi> <mo>=</mo> <mn>5</mn></mrow> <annotation encoding="application/x-tex">n=5</annotation></semantics></math>, primes between 5 and 10 are 7, which is valid. For <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n=10"><semantics><mrow><mi>n</mi> <mo>=</mo> <mn>10</mn></mrow> <annotation encoding="application/x-tex">n=10</annotation></semantics></math>, primes between 10 and 20 include 11, 13, 17, 19, etc.</span></span></span> <span id="A9.I3.i2" style="list-style-type:none;">2. <span id="A9.I3.i2.p1"><span id="A9.I3.i2.p1.4"><span id="A9.I3.i2.p1.4.1">Inductive Hypothesis</span>: Assume that for all integers <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="k"><semantics><mi>k</mi> <annotation encoding="application/x-tex">k</annotation></semantics></math> where <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2\leq k&lt;m"><semantics><mrow><mn>2</mn> <mo>≤</mo> <mi>k</mi> <mo>&lt;</mo> <mi>m</mi></mrow> <annotation encoding="application/x-tex">2\leq k&lt;m</annotation></semantics></math>, there exists a prime <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="k&lt;p&lt;2k"><semantics><mrow><mi>k</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>k</mi></mrow></mrow> <annotation encoding="application/x-tex">k&lt;p&lt;2k</annotation></semantics></math>.</span></span></span> <span id="A9.I3.i3" style="list-style-type:none;">3. <span id="A9.I3.i3.p1"><span id="A9.I3.i3.p1.4"><span id="A9.I3.i3.p1.4.1">Inductive Step</span>: We need to show that for <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m"><semantics><mi>m</mi> <annotation encoding="application/x-tex">m</annotation></semantics></math>, there exists a prime <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="p"><semantics><mi>p</mi> <annotation encoding="application/x-tex">p</annotation></semantics></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m&lt;p&lt;2m"><semantics><mrow><mi>m</mi> <mo>&lt;</mo> <mi>p</mi> <mo>&lt;</mo> <mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>m</mi></mrow></mrow> <annotation encoding="application/x-tex">m&lt;p&lt;2m</annotation></semantics></math>. To do this, we consider the product of all primes up to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m"><semantics><mi>m</mi> <annotation encoding="application/x-tex">m</annotation></semantics></math> and use properties of factorials and primes to derive a contradiction if no such prime exists.</span></span></span></span></span> <span id="A9.SSx3.p2"><span id="A9.SSx3.p2.5">The detailed proof involves showing that the product of primes up to <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m"><semantics><mi>m</mi> <annotation encoding="application/x-tex">m</annotation></semantics></math> multiplied by <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m"><semantics><mi>m</mi> <annotation encoding="application/x-tex">m</annotation></semantics></math> is less than <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="(2m)^{m/2}"><semantics><msup><mrow><mo stretchy="false">(</mo><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>m</mi></mrow><mo stretchy="false">)</mo></mrow> <mrow><mi>m</mi> <mo>/</mo> <mn>2</mn></mrow></msup> <annotation encoding="application/x-tex">(2m)^{m/2}</annotation></semantics></math>, leading to a contradiction if there are no primes between <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="m"><semantics><mi>m</mi> <annotation encoding="application/x-tex">m</annotation></semantics></math> and <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="2m"><semantics><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>m</mi></mrow> <annotation encoding="application/x-tex">2m</annotation></semantics></math>. This is a complex part of the proof and requires careful analysis of inequalities and properties of prime numbers.</span></span> <span id="A9.SSx3.p3"><span id="A9.SSx3.p3.2">The code provided uses a brute-force approach to check for primes in the range <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="(n,2n)"><semantics><mrow><mo stretchy="false">(</mo><mi>n</mi><mo>,</mo><mrow><mn>2</mn> <mo lspace="0em" rspace="0em"></mo><mi>n</mi></mrow><mo stretchy="false">)</mo></mrow> <annotation encoding="application/x-tex">(n,2n)</annotation></semantics></math> for a given <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" data-latex="n"><semantics><mi>n</mi> <annotation encoding="application/x-tex">n</annotation></semantics></math>. This is a practical way to verify the statement for small values but is not a proof. The actual proof of Bertrand’s Postulate is more theoretical and involves deeper mathematical concepts.</span></span> <span id="A9.SSx3.p4"><span id="A9.SSx3.p4.1">Thus, the code serves as a verification tool, but the proof itself is beyond the scope of this example. The code can be used to test the hypothesis for specific values, but the general proof requires a more rigorous approach.</span></span></section></span></foreignObject></g></g></svg>

The merged model correctly solves the task, following the instruction to prove Bertrand’s Postulate. Two of the three seed models returned random symbols, and the code expert provided an answer that implements a brute-force approach to check for primes in the range $(n,2n)$ for a given $n$ and does not formally prove the statement.

#### I.2.2 Out-of-Distribution Tasks

(qwen2.5) task\_272\_complex\_logical\_reasoning

<svg id="A9.SSx3.SSS2.p2.pic1" height="171.56" overflow="visible" version="1.1" viewBox="0 0 600 171.56" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,171.56) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 171.56 L 600 171.56 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 152.84 L 599.31 152.84 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 157.47)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p2.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p2.pic1.1.1.1.1.1.1">Instruction</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:9.09em;--ltx-fo-depth:0.19em;" width="559.25" height="128.53" transform="matrix(1 0 0 -1 0 125.84)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.1">Given the following logical statements:</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.2">For all x, if x is a bird, then x can fly.</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.3">For all x, if x can fly, then x has wings.</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.4">Penguin is a bird.</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.5">Penguin cannot fly.</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.6">Deduce the most consistent conclusion and provide a detailed explanation of the reasoning process, even if the premises contain contradictions.</span> <span id="A9.SSx3.SSS2.p2.pic1.2.2.2.1.1.7">Do not include any additional text other than the conclusion and the explanation.</span></span></foreignObject></g></g></svg>

<svg id="A9.SSx3.SSS2.p3.pic1" height="207.61" overflow="visible" version="1.1" viewBox="0 0 600 207.61" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,207.61) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#1B701B;" fill="#1B701B" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 207.61 L 600 207.61 L 600 0 Z"></path></g><g style="--ltx-fill-color:#D3E8D3;" fill="#D3E8D3" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 186.05 L 599.31 186.05 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 193.37)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p3.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p3.pic1.1.1.1.1.1.1">Merged Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:11.49em;--ltx-fo-depth:0.19em;" width="559.25" height="161.74" transform="matrix(1 0 0 -1 0 159.05)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p3.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p3.pic1.2.2.2.1.1.1">The conclusion is that penguins have wings.</span> <span id="A9.SSx3.SSS2.p3.pic1.2.2.2.1.1.2">Explanation: The logical statements establish that all birds can fly (if they are birds), and all flying creatures have wings. However, the statement about penguins cannot fly introduces a contradiction because it implies penguins are birds but contradicts the general rule that birds can fly. Despite this contradiction, the conclusion that penguins have wings is consistent with the second statement that all flying creatures have wings. Since penguins cannot fly, they do not fall under the category of flying creatures and thus do not have wings. However, the conclusion is based on the given premises and the logical structure provided, leading to the conclusion that penguins have wings due to the conditional statements about birds and flying creatures.</span></span></foreignObject></g></g></svg>

<svg id="A9.SSx3.SSS2.p4.pic1" height="238.13" overflow="visible" version="1.1" viewBox="0 0 600 238.13" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,238.13) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#CC2222;" fill="#CC2222" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 238.13 L 600 238.13 L 600 0 Z"></path></g><g style="--ltx-fill-color:#FFD5D5;" fill="#FFD5D5" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 219.26 L 599.31 219.26 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 223.89)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0em;" width="559.25" height="9.61" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p4.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p4.pic1.1.1.1.1.1.1">Instruct Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:13.89em;--ltx-fo-depth:0.19em;" width="559.25" height="194.95" transform="matrix(1 0 0 -1 0 192.26)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p4.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p4.pic1.2.2.2.1.1.1">The premises contain a contradiction because according to the first and second statements, all birds can fly and all that can fly have wings. However, the penguin is a bird that cannot fly, which violates the first statement. Despite this contradiction, the most consistent conclusion we can draw is that penguins, despite being birds, do not have wings based on the given information.</span> <span id="A9.SSx3.SSS2.p4.pic1.2.2.2.1.1.2">Explanation: The first two statements establish a logical chain where all birds can fly and all that can fly have wings. The penguin being a bird and not being able to fly directly contradicts the first statement. However, the third statement explicitly states that penguin is a bird, and the fourth statement states that penguin cannot fly. Given these facts, we can infer that the penguin does not have wings, as it cannot fly and the second statement asserts that only those that can fly have wings. This conclusion is consistent with the given information, even though the premises contain a logical contradiction.</span></span></foreignObject></g></g></svg>

The merged model recognizes the contradiction and provides nuanced reasoning about the logical structure, concluding that despite the contradiction, the conditional statements lead to penguins having wings. The general purpose instruct model incorrectly concludes penguins do not have wings, failing to properly navigate the logical dependencies despite explicitly identifying the contradiction.

(qwen2.5) task\_626\_complex\_sentence\_transformation

<svg id="A9.SSx3.SSS2.p7.pic1" height="138.35" overflow="visible" version="1.1" viewBox="0 0 600 138.35" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,138.35) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#86AECC;" fill="#86AECC" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 138.35 L 600 138.35 L 600 0 Z"></path></g><g style="--ltx-fill-color:#EDF7FF;" fill="#EDF7FF" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 119.64 L 599.31 119.64 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 124.26)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.68em;--ltx-fo-depth:0em;" width="559.25" height="9.46" transform="matrix(1 0 0 -1 0 9.46)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p7.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p7.pic1.1.1.1.1.1.1">Instruction</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:6.69em;--ltx-fo-depth:0.19em;" width="559.25" height="95.32" transform="matrix(1 0 0 -1 0 92.63)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p7.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p7.pic1.2.2.2.1.1.1">Transform the following sentence according to the rule:</span> <span id="A9.SSx3.SSS2.p7.pic1.2.2.2.1.1.2">Original Sentence: If she writes a letter every day, then her friends will be happy.</span> <span id="A9.SSx3.SSS2.p7.pic1.2.2.2.1.1.3">Transformation Rule: Change the sentence to past tense and passive voice.</span> <span id="A9.SSx3.SSS2.p7.pic1.2.2.2.1.1.4">Provide only the transformed sentence without any additional text. Ensure that the transformed sentence maintains the original meaning and follows the specified grammatical rules precisely, especially the conditional structure and the past perfect tense.</span></span></foreignObject></g></g></svg>

<svg id="A9.SSx3.SSS2.p8.pic1" height="58.17" overflow="visible" version="1.1" viewBox="0 0 600 58.17" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,58.17) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#1B701B;" fill="#1B701B" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 58.17 L 600 58.17 L 600 0 Z"></path></g><g style="--ltx-fill-color:#D3E8D3;" fill="#D3E8D3" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 36.61 L 599.31 36.61 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 43.93)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p8.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p8.pic1.1.1.1.1.1.1">Merged Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p8.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p8.pic1.2.2.2.1.1.1">If a letter was written by her every day, then her friends would have been happy.</span></span></foreignObject></g></g></svg>

<svg id="A9.SSx3.SSS2.p9.pic1" height="55.48" overflow="visible" version="1.1" viewBox="0 0 600 55.48" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,55.48) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#CC2222;" fill="#CC2222" fill-opacity="1.0"><path style="stroke:none" d="M 0 0 L 0 55.48 L 600 55.48 L 600 0 Z"></path></g><g style="--ltx-fill-color:#FFD5D5;" fill="#FFD5D5" fill-opacity="1.0"><path style="stroke:none" d="M 0.69 0.69 L 0.69 36.61 L 599.31 36.61 L 599.31 0.69 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 41.24)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0em;" width="559.25" height="9.61" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#FFFFFF"><span id="A9.SSx3.SSS2.p9.pic1.1.1.1.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p9.pic1.1.1.1.1.1.1">Instruct Model</span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.38 15.19)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.42em;--ltx-fo-height:0.69em;--ltx-fo-depth:0.19em;" width="559.25" height="12.3" transform="matrix(1 0 0 -1 0 9.61)" overflow="visible" color="#000000"><span id="A9.SSx3.SSS2.p9.pic1.2.2.2.1.1" style="width:40.42em;"><span id="A9.SSx3.SSS2.p9.pic1.2.2.2.1.1.1">If a letter is written by her every day, then her friends will have been happy.</span></span></foreignObject></g></g></svg>

The merged model properly applies both passive voice transformation and past perfect tense in the consequent. The seed model fails to fully transform to the past tense in the antecedent (“is written” instead of “was written”), demonstrating the merged model’s superior grasp of complex grammatical transformations.

These examples illustrate that merged models exhibit improved performance on tasks requiring precise mathematical reasoning, possibly extending beyond the standard training on math expert data and careful instruction-following for spatial tasks, and perhaps generalizing the logical reasoning abilities of code and math experts. The diversity of successful tasks suggests that merging could enable the integration of complementary skills beyond what individual seed models provide.

## Appendix J Merging Compatibility Analysis

In standard LLM development, expensive pretraining is typically conducted with an eye toward subsequent mid- and post-training stages. In the space of (evolutionary) model merging, developing core models specifically suited for merging has received comparatively less attention. Only very recently have efforts been made to deliberately conduct research on this challenge [^52].

We evaluate AC/DC across 5 model families, seed model configurations, and different model sizes and observe that 4 out of 5 demonstrate improvements over baselines, with absolute improvements varying across these configurations.

In Sec. 6 of the main paper, we briefly address this limitation. Nevertheless, the question remains whether there are diagnostic predictors of successful seed model merging and how practitioners can know beforehand.

To address this question, we analyzed differences in weight space among different seed model configurations, identifying relevant correlations to assess their compatibility (which points to interesting future research). Moreover, we propose an additional technique to evaluate early in training whether the coevolution process will successfully produce merged models.

### J.1 Analysis Approach and Findings

We conducted an analysis of weight-space geometry across five seed model compositions across different model families to identify potential predictors of compatibility. Our investigation proceeded in two stages:

Stage 1: Expert-to-Base Analysis — We first measured L2 norm distances between each expert model and its base model across all layers (embedding, transformer blocks, output head). While this analysis revealed differences in specialization magnitude (e.g., some experts diverged substantially from the base while others remained close), it failed to predict merging success. Most critically, the Llama3 family exhibited excellent uniformity metrics (low coefficient of variation across experts and tight L2 norm ranges), yet this seed model choice did not lead to models that demonstrably outperform baselines in our experiments. This suggests that measuring expert deviation from a shared reference point (the base model) is insufficient for predicting merge compatibility.

Stage 2: Pairwise Expert Geometry — We then computed direct pairwise distances between experts (comparing experts to each other rather than to the base). For three experts, A, B, and C, we measured the mean L2 norm between all pairs:

$$
d(X,Y)=\frac{1}{N}\sum_{i=1}^{N}||X_{i}-Y_{i}||_{2}
$$

where $N$ is the number of parameters and $X_{i},Y_{i}$ are corresponding parameter values. We then computed a similarity ratio to characterize the geometric structure:

$$
\text{similarity ratio}=\frac{\min(d(A,B),d(A,C),d(B,C))}{\max(d(A,B),d(A,C),d(B,C))}
$$

This metric quantifies whether a “clear pair” of similar experts exists (low ratio) versus all experts being roughly equidistant (high ratio approaching 1.0).

Key Observations:

The pairwise analysis correctly predicted merging outcomes for 4 out of 5 families (80% accuracy). The similarity ratio appears to correlate with merge success in many cases: families with low ratios ($<0.1$), indicating a clear pair structure where two experts are substantially closer to each other than to the third, generally merged well. Conversely, families with high ratios ($>0.7$), indicating equidistant configurations where all experts are roughly equally separated, generally merged poorly. Importantly, even within the same base model family (Qwen2.5), different expert selections yielded dramatically different outcomes—the seed models used in our paper (here referred to as Qwen2.5 ALT to distinguish them) achieved excellent merging performance (similarity ratio 0.097), while the native Qwen2.5 instruct/code/math experts (Qwen2.5 Official) produced very poor merging results (similarity ratio 0.834). This suggests that seed model selection, even from the same pretrained base, affects merge compatibility.

Breaking down the specific geometric structures observed:

- Clear pair structure (Qwen2.5 ALT: ratio 0.097, Qwen 2.0: ratio 0.047): Two experts very close to each other with the third more distant $\rightarrow$ these families merged well
- Equidistant structure (Llama3: ratio 0.786, Qwen2.5 Official: ratio 0.834): All three experts are roughly equally distant from each other $\rightarrow$ these families merged poorly
- Specialist cluster (DeepSeek: ratio 0.642): The two specialist experts (code, math) closest to each other, despite both being far from base $\rightarrow$ merged best of all families

However, we emphasize caution in generalization: The DeepSeek family, which achieved the best merging performance, does not conform to the “clear pair” pattern and instead exhibits a moderate similarity ratio (0.642) with considerable absolute distances (maximum pairwise distance 182.76). Notably, in DeepSeek, the two specialist experts (code and math) are closest to each other—in contrast to Qwen2.5 Official (which merged poorly), where the specialist experts are furthest apart (distance 75.85). This suggests that which experts form the closest pair may matter as much as the overall geometric structure, but this hypothesis rests on limited data points and requires validation.

Finally, as demonstrated in Fig. 14, one predictor we used during development was tracking the number of gibberish models during coevolution. We found that if we observed many gibberish models being detected within the first few generations, we could confidently assume that the final performance would be poor.

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/final_gibberish_count-llama.png)

(a) Llama3 8B

## Appendix K Statistical Significance Analysis

To rigorously assess the significance of Coverage and Best-of-N (BoN) improvements achieved by AC/DC, we conducted comprehensive statistical testing across all experimental conditions. This section describes our bootstrap-based methodology and presents detailed results demonstrating the statistical reliability of our findings.

### K.1 Methodology

#### K.1.1 Score Normalization

To ensure fair comparisons across benchmarks with different difficulty levels and score distributions, we applied min-max normalization to all scores. For each benchmark $b$, we linearly mapped scores to the range $[0,1]$:

$$
s^{\prime}_{b,m,f}=\frac{s_{b,m,f}-\min_{\forall m^{\prime},f^{\prime}}s_{b,m^{\prime},f^{\prime}}}{\max_{\forall m^{\prime},f^{\prime}}s_{b,m^{\prime},f^{\prime}}-\min_{\forall m^{\prime},f^{\prime}}s_{b,m^{\prime},f^{\prime}}}
$$

where $s_{b,m,f}$ is the raw score for benchmark $b$, method $m$, and model family $f$, and $s^{\prime}_{b,m,f}$ is the normalized score. The minimum and maximum values are computed across all methods and model families for each benchmark independently.

We performed normalization separately for two groups: (1) main baselines and model merging baselines, and (2) ablation experiments. This grouping ensures an adequate range of data points from which we can get clear performance differentials within controlled experiment groups, that would then lead to more informative relative benchmark score gains comparisons.

#### K.1.2 Bootstrap Hypothesis Testing

We employed bootstrap resampling to test the significance of performance differences between AC/DC and baseline methods. For each comparison, we:

1. Computed pairwise performance differences $\Delta_{i}=s^{\prime}_{\text{AC/DC},i}-s^{\prime}_{\text{baseline},i}$ across all $n=8$ benchmarks for a given model family (or aggregated across multiple model families).
2. Generated a bootstrap distribution by resampling the differences $\{\Delta_{i}\}_{i=1}^{n}$ with replacement 50,000 times, computing the mean difference for each resample.
3. Calculated the bootstrapped mean $\bar{\Delta}_{\text{boot}}$ and 95% confidence intervals using the percentile method.
4. Computed one-tailed p-values to test whether AC/DC shows consistent improvement (i.e., $H_{0}:\bar{\Delta}\leq 0$ vs. $H_{1}:\bar{\Delta}>0$). Lower p-values indicate higher confidence that AC/DC achieves meaningful performance gains.

This approach accounts for variance across benchmarks while providing robust statistical evidence for performance improvements.

### K.2 Coverage Results

#### K.2.1 Main Baselines: Task Force Size N=3N=3

Aggregated testing across 8 benchmarks and 4 model families demonstrates that AC/DC significantly outperforms these baselines at $N=3$:

- vs. Control baseline: $p=0.0127$ (CI: $0.006:0.053:0.107$)
- vs. Experts baseline: $p<0.0001$ (CI: $0.048:0.104:0.167$)
- vs. Big Model baseline: $p=0.0017$ (CI: $0.026:0.095:0.177$)

For the DeepSeek model family specifically, AC/DC shows particularly strong performance:

- vs. Experts baseline: $p<0.0001$ (CI: $0.088:0.221:0.380$)
- vs. Control baseline: $p=0.0045$ (CI: $0.044:0.189:0.336$)

Additionally, the Qwen 3 model family significantly outperforms GPT-4o at $N=3$:

- Qwen 3 vs. GPT-4o: $p=0.0080$ (CI: $0.026:0.140:0.246$)

#### K.2.2 Main Baselines: Task Force Size N=8N=8

At the larger task force size, aggregated across 4 model families and 8 benchmarks, AC/DC significantly outperforms the following baselines:

- vs. Big Model baseline: $p<0.0001$ (CI: $0.234:0.312:0.396$)
- vs. Control baseline: $p=0.0175$ (CI: $0.003:0.052:0.106$)
- vs. Experts baseline: $p=0.1265$ (CI: $-0.022:0.035:0.098$) \[more often outperforms\]

Notably, AC/DC with Qwen 2.5 and Qwen 3 model families significantly outperforms GPT-4o in Coverage, while Qwen 2 more often outperforms GPT-4o:

- Qwen 2.5 vs. GPT-4o: $p=0.0041$ (CI: $0.044:0.185:0.333$)
- Qwen 3 vs. GPT-4o: $p<0.0001$ (CI: $0.160:0.305:0.445$)
- Qwen 2 vs. GPT-4o: $p=0.1698$ (CI: $-0.087:0.081:0.248$) \[more often outperforms\]

For DeepSeek at $N=8$, AC/DC significantly outperforms all baselines except GPT-4o:

- vs. Big Model baseline: $p<0.0001$ (CI: $0.272:0.346:0.423$)
- vs. Experts baseline: $p<0.0001$ (CI: $0.109:0.219:0.359$)
- vs. Control baseline: $p=0.0214$ (CI: $0.005:0.162:0.317$)

#### K.2.3 Knowledge Recall Benchmarks

When isolating tests to MMLU judge, MMLU Pro judge, and GPQA judge benchmarks—which test general and scientific knowledge recall without multiple-choice options—the $N=8$ AC/DC Qwen 3 task force outperforms the following baselines:

- vs. Big Model: $p<0.0001$; paired t-test $p=0.0294$ (CI: $0.478:0.652:0.983$)
- vs. GPT-4o: $p<0.0001$; paired t-test $p=0.0009$ (CI: $0.494:0.540:0.568$)
- vs. Control: $p<0.0001$; paired t-test $p=0.1649$ (CI: $0.005:0.090:0.231$)
- vs. Experts: $p<0.0001$; paired t-test $p=0.1238$ (CI: $0.017:0.069:0.154$)

For Qwen 2 on these knowledge-focused benchmarks:

- vs. Big Model ($N=3$): $p<0.0001$; paired t-test $p=0.0746$ (CI: $0.089:0.198:0.369$)
- vs. Big Model ($N=8$): $p<0.0001$; paired t-test $p=0.0115$ (CI: $0.367:0.502:0.635$)
- vs. Experts ($N=3$): $p<0.0001$; paired t-test $p=0.0007$ (CI: $0.202:0.214:0.230$)
- vs. Experts ($N=8$): $p=0.30$; paired t-test $p=0.47$ (CI: $-0.146:0.013:0.327$)
- vs. Control ($N=3$): $p<0.0001$; paired t-test $p=0.1391$ (CI: $0.007:0.045:0.105$)
- vs. Control ($N=8$): $p=0.30$; paired t-test $p=0.2968$ (CI: $-0.029:0.037:0.154$)

Aggregating across these 3 knowledge benchmarks and 4 model families at $N=8$:

- vs. Big Model: $p<0.0001$ (CI: $0.407:0.516:0.636$)
- vs. Experts: $p=0.0586$ (CI: $-0.013:0.058:0.134$) \[borderline significant\]
- vs. Control: $p=0.2573$ (CI: $-0.042:0.021:0.084$) \[more often improves\]

#### K.2.4 Summary: Coverage

The statistical analysis confirms that AC/DC reliably produces more diverse, specialized model task forces with broader Coverage than baseline methods. Key findings include:

- AC/DC significantly outperforms all three main baselines (Control, Experts, Big Model) at $N=3$ when aggregated across model families, and outperforms Control and Big Model baselines at $N=8$; the Experts baseline at $N=8$ remains the only case where improvements do not reach significance (more often outperforms).
- Strong per-family results are observed for DeepSeek and Qwen 3 at both task force sizes, with Qwen 2.5 and Qwen 3 also significantly outperforming GPT-4o at $N=8$, and Qwen 3 significantly outperforming GPT-4o even at $N=3$.
- The method achieves particularly strong results on knowledge recall tasks, with Qwen 3 significantly outperforming both the Big Model baseline and GPT-4o, and Qwen 2 showing significant gains over Big Model and Experts baselines at smaller task force sizes.

### K.3 Best-of-N Selection Results

#### K.3.1 Task Force Size N=3N=3

For Best-of-N selection with $N=3$ models, AC/DC aggregated across 4 model families outperforms the following baselines:

- vs. Control baseline: $p=0.0002$ (CI: $0.022:0.053:0.088$) \[highly significant\]
- vs. Experts baseline: $p=0.0552$ (CI: $-0.008:0.043:0.103$) \[borderline significant\]

For DeepSeek V1 specifically at $N=3$:

- vs. Experts: $p<0.0001$ (CI: $0.151:0.257:0.392$)
- vs. Control: $p<0.0001$ (CI: $0.064:0.125:0.194$)

Model family-specific results for $N=3$:

- Qwen 2 vs. Control: $p=0.0578$ (CI: $-0.015:0.071:0.164$) \[borderline significant\]
- Qwen 2.5 vs. Control: $p=0.2560$ (CI: $-0.019:0.009:0.033$) \[more often outperforms\]
- Qwen 3 vs. Control: $p=0.0951$ (CI: $-0.004:0.007:0.016$) \[marginally better\]

#### K.3.2 Task Force Size N=8N=8

At $N=8$, AC/DC significantly outperforms the control baseline in aggregate:

- vs. Control baseline: $p=0.0104$ (CI: $0.007:0.050:0.097$) \[significant\]

DeepSeek V1 demonstrates particularly strong performance at $N=8$, significantly outperforming both the control and big model baselines:

DeepSeek V1 results:

- vs. Control: $p<0.0001$ (CI: $0.114:0.210:0.303$) \[highly significant\]
- vs. Big Model: $p=0.0457$ (CI: $-0.022:0.158:0.360$) \[significant\]

Qwen 3 more likely outperforms GPT-4o at $N=8$:

Qwen 3 results:

- vs. GPT-4o: $p=0.1940$ (CI: $-0.160:0.197:0.433$)

#### K.3.3 Summary: Best-of-N Selection

The BoN analysis demonstrates that AC/DC’s Coverage improvements can translate into practical single-answer selection scenarios:

- At $N=3$, AC/DC significantly outperforms the control baseline; DeepSeek V1 shows particularly strong individual gains over control and expert baselines.
- At $N=8$, AC/DC significantly outperforms the control baseline in aggregate; DeepSeek V1 shows particularly strong gains over both the control and big model baselines, and Qwen 3, the best model family task force against GPT-4o, more likely outperforms GPT-4o than the inverse, in spite of the absolute average performance difference being lower.

### K.4 Comparison to Alternative QD Methods

We compared AC/DC against two alternative quality-diversity approaches: CycleQD (CQD) and standard Dominated Novelty Search (DNS). Additionally, we test DNS against CQD to justify its integration as part of AC/DC.

At $N=3$, AC/DC shows marginally significant improvements over both alternatives, while DNS and CQD remain statistically indistinguishable:

- AC/DC vs. CQD: $p=0.0356$ (bootstrap; CI: $-0.002:0.033:0.066$; wins: 5/7) \[marginally significant\]
- AC/DC vs. DNS: $p=0.0431$ (bootstrap; CI: $-0.003:0.023:0.052$; wins: 4/6) \[marginally significant\]
- DNS vs. CQD: $p=0.1065$ (bootstrap; CI: $-0.007:0.010:0.023$; wins: 6/7) \[more often outperforms\]

At $N=8$, AC/DC demonstrates substantially stronger and highly significant advantages:

- AC/DC vs. CQD: $p<0.0001$ (bootstrap; CI: $0.076:0.104:0.140$; wins: 7/7) \[highly significant\]
- AC/DC vs. DNS: $p<0.0001$ (bootstrap; CI: $0.055:0.075:0.098$; wins: 7/7) \[highly significant\]
- DNS vs. CQD: $p=0.0130$ (bootstrap; CI: $0.004:0.029:0.051$; wins: 6/7) \[significant\]

These results demonstrate that AC/DC outperforms alternative QD methods even at small population sizes, with these advantages growing substantially as scale increases. Furthermore, DNS as the QD algorithm of choice is shown to be more effective at selecting more diverse, specialized models than CQD, making it a clear choice for model selection in AC/DC.

### K.5 Ablation Study Results

To understand the contribution of each algorithmic component, we conducted ablation experiments where individual components were systematically removed.

#### K.5.1 Task Force Size N=3N=3

At $N=3$, removing most components leads to statistically significant performance degradation:

- Fitness-only selection: $p<0.0001$ (bootstrap; CI: $0.393:0.632:0.856$; wins 7/7) \[significantly worse\]
- No gibberish filter: $p<0.0001$ (bootstrap; CI: $0.385:0.628:0.854$; wins 7/7) \[significantly worse\]
- No (task) novelty filter: $p=0.1246$ (bootstrap; CI: $-0.064:0.112:0.304$; wins 4/7) \[more often worse\]
- None of the above (fitness-only selection, no novelty filter, no gibberish filter, no mutation): $p<0.0001$ (bootstrap; CI: $0.293:0.549:0.788$; wins 7/7) \[significantly worse\]

#### K.5.2 Task Force Size N=8N=8

At $N=8$, the importance of the complete method becomes substantially more evident:

- None of the above: $p<0.0001$ (bootstrap; CI: $0.677:0.852:1.014$; wins 7/7) \[highly significant degradation\]
- No gibberish filter: $p<0.0001$ (bootstrap; CI: $0.067:0.123:0.181$; wins 6/6) \[significantly worse\]
- Fitness-only selection: $p=0.0036$ (bootstrap; CI: $0.050:0.169:0.272$; wins 6/7) \[significantly worse\]
- No novelty filter: $p=0.0207$ (bootstrap; CI: $0.002:0.064:0.126$; wins 5/7) \[significantly worse\]
- No mutation: $p=0.0358$ (bootstrap; CI: $-0.012:0.214:0.503$; wins 5/7) \[significantly worse\]

#### K.5.3 Summary: Ablations

The ablation studies confirm that each component of AC/DC contributes meaningfully to overall performance:

- At $N=3$, using fitness-based selection only, removing the gibberish filter, or removing all components simultaneously results in significant performance degradation. The novelty filter shows a positive but non-significant effect at this scale ($p=0.125$).
- At $N=8$, the importance of the full method becomes dramatically more evident, with the complete ablation (removing all components) showing highly significant performance drops ($p<0.0001$, mean difference $0.85$). Notably, the novelty filter reaches statistical significance at this scale ($p=0.021$), as does mutation removal ($p=0.036$).
- These results demonstrate that AC/DC’s algorithmic innovations work synergistically, with benefits becoming more pronounced at larger population sizes.

### K.6 Reproducibility Analysis: Variance Across Re-runs

To assess the reproducibility and stability of AC/DC, we analyzed the variance in performance across multiple independent runs. We report standard deviations and ranges for the Qwen 2.5 model family benchmark scores at both $N=3$ and $N=8$ task force sizes, comparing AC/DC against the control baseline.

#### K.6.1 Task Force Size N=3N=3

For the control baseline (3 runs), we observed low variance across benchmarks with a mean standard deviation of 0.94 points and median of 0.13 points in raw scores. The highest variance occurred on GPQA judge (std dev: 0.78 points, range: 1.35 points) and Minerva (std dev: 1.43 points, range: 2.82 points), while most other benchmarks showed standard deviations below 0.36 points.

For AC/DC (2 runs), variance was comparable, with mean standard deviation of 0.64 points and median of 0.43 points. The benchmarks with highest variance were GPQA judge (std dev: 0.95 points, range: 1.34 points) and Minerva (std dev: 1.32 points, range: 1.86 points). Overall, AC/DC demonstrated similar reproducibility to the control baseline at $N=3$.

#### K.6.2 Task Force Size N=8N=8

At $N=8$, the control baseline (3 runs) maintained low variance with mean standard deviation of 0.59 points and median of 0.16 points. Again, GPQA judge (std dev: 0.70 points) and Minerva (std dev: 1.52 points) showed the highest variance.

For AC/DC (2 runs) at $N=8$, we observed moderately higher variance with mean standard deviation of 1.80 points and median of 0.95 points. Notable variance appeared on MMLU judge (std dev: 1.48 points), MMLU Pro judge (std dev: 1.32 points), and particularly Minerva (std dev: 4.99 points, range: 7.06 points). Overall, ranges appear to be reasonable given the stochastic nature of evolutionary search.

#### K.6.3 Summary: Reproducibility

The reproducibility analysis reveals that:

- At $N=3$, both AC/DC and control baselines exhibit comparable low variance across runs, indicating stable performance.
- At $N=8$, AC/DC shows moderately higher variance than the control, which is expected given the increased complexity of evolutionary search over larger populations.
- Despite this increased variance, the statistically significant performance improvements reported in previous sections remain robust, as our bootstrap hypothesis testing accounts for cross-benchmark variance.
- Certain benchmarks (GPQA judge, Minerva) consistently show higher variance across both methods, likely reflecting the inherent difficulty and sensitivity of these tasks.
- The observed variance levels are acceptable for evolutionary methods and do not undermine the reliability of our main findings. That is, multiple findings suggest that AC/DC, being the first method of its kind towards open-ended model population discovery, significantly outperforms existing non-coevolutionary model merging approaches, and is more reliable in producing broader Coverage task forces than other baseline approaches.

### K.7 Interpretation and Implications

The comprehensive statistical analysis provides strong evidence for AC/DC’s effectiveness:

1. Reliability across model families: AC/DC demonstrates consistent improvements when considering aggregated stats across diverse base architectures, indicating the method’s broad applicability.
2. Scalability: In several cases, performance advantages become more pronounced at larger population sizes ($N=8$), suggesting that the advantages of model diversity often compound with scale.
3. Domain specificity: Positive results on knowledge recall benchmarks indicate that evolutionary model merging can more broadly discover domain-specific capabilities.
4. Practical deployment: BoN improvements (in some cases, significant) suggest that Coverage gains can translate to realistic single-answer scenarios.
5. Component synergy: Ablation results reveal that AC/DC’s components work together synergistically, with the full method substantially outperforming partial implementations.
6. Reproducibility: The method demonstrates acceptable variance across multiple runs, with statistically significant improvements remaining robust despite the stochastic nature of evolutionary search.

Overall, these statistical analyses establish AC/DC as a reliable method for discovering diverse, capable model populations that achieve broader skill Coverage than existing approaches, with the framework showing particular promise for scaling to larger model collectives.

## Appendix L Computational Cost Analysis

The total computational cost of our coevolution process is approximately 324 GPU hours, which, after 50 generations and an active model count per generation of 16, yields a population of approximately 80 diverse models selected to maintain high model quality and increase diversity. During the coevolution process, our scientist successfully develops around 1000 tasks (where another roughly 1000 do not pass our quality and novelty filters). During coevolution, each generation, 250 tasks are actively considered for evaluation of each model in the active model pool. The computational cost includes the GPUs for the model merging and evaluation pipeline, the GPUs for hosting a large, open-source scientist LLM, and for an embedding model. Notably, AC/DC works without any API calls to proprietary models and relies solely on self-hosted models.

Critically, these requirements represent a cost of roughly 4 GPU hours per merged model—significantly more efficient than standard post-training approaches such as reinforcement learning, which can require 10 <sup>2</sup> to 10 <sup>5</sup> GPU hours per 7B model depending on the method and scale [^69], plus AC/DC eliminates manual dataset curation.

While baseline approaches like selecting expert models from Hugging Face require no training cost, they face fundamental scalability and complementarity limitations: (1) the availability of diverse, specialized models is limited (dozens, not 80+), (2) there is no guarantee that independently-trained experts will have complementary specializations, and (3) manual search costs grow with collective size. Creating 80 complementary specialists through traditional post-training could require 10 <sup>3</sup> to 10 <sup>6</sup> GPU hours, plus the design of 80 distinct specializations and datasets.

Furthermore, our 324-hour investment provides flexibility: the evolved population can be composed into collectives of any size (N=1 to 80) for different downstream applications without additional training. As shown in the Fig. 15, downstream performance scales with N, and our approach (1) scales better than re-prompting a single instruct model (control experiment) and (2) uniquely enables exploring this trade-off without the prohibitive cost of manually training individual models or the availability constraints of pre-existing expert models.

![Refer to caption](https://arxiv.org/html/2604.14969v1/images/Scaling_trend-qwen2.5.png)

Figure 15: Scaling trend with the number of models on our Qwen2.5 based experiment.

## Appendix M LLM Parameter Update Details

### M.1 Model Merging Based Crossover

Our crossover operator employs parameter space merging, creating new models by merging task vectors at the model level [^57] [^72]. For a pre-trained base LLM with parameters $\theta_{\mathrm{base}}\in\mathbb{R}^{d}$ and a fine-tuned LLM with parameters $\theta\in\mathbb{R}^{d}$, we define the task vector as:

$$
\tau=\theta-\theta_{\mathrm{base}}
$$

The crossover operator generates offspring parameters by combining task vectors from two parents:

$$
\theta_{\mathrm{child}}=\theta_{\mathrm{base}}+\frac{\omega_{1}}{\omega_{1}+\omega_{2}}\tau_{p_{1}}+\frac{\omega_{2}}{\omega_{1}+\omega_{2}}\tau_{p_{2}}
$$

where $\tau_{p_{1}}$ and $\tau_{p_{2}}$ are the parents’ task vectors. The weights $\omega_{1}$ and $\omega_{2}$ are sampled i.i.d. from $\mathcal{N}(\mu,\sigma^{2})$, with $(\mu,\sigma)$ as predetermined hyperparameters fixed throughout evolution. We normalize the mixing coefficients to prevent merged weights from becoming outliers that could cause issues in downstream layers.

### M.2 Generalized SVD-Based Mutation

The model merging crossover has an inherent limitation: constructing $\theta_{\mathrm{child}}$ as a linear combination of parent task vectors confines offspring to the convex region in performance space formed by the parents. To enable extrapolation beyond this region, we introduce a mutation operator $\theta_{\mathrm{child}}=h(\theta_{\mathrm{child}})$ applied after crossover.

Rather than adding random Gaussian perturbations to parameters-which introduces excessive degrees of freedom and can be hard to optimize-we propose sampling perturbations along the principal components of the model’s weight matrices. This is achieved through singular value decomposition (SVD).

For each weight matrix $W_{l}$ in the offspring model, we compute its SVD:

$$
W_{l}=U_{l}\Sigma_{l}V_{l}^{T}
$$

where $U_{l}\in\mathbb{R}^{m\times r}$, $\Sigma_{l}\in\mathbb{R}^{r\times r}$ (diagonal), and $V_{l}\in\mathbb{R}^{n\times r}$ are the left singular vectors, singular values, and right singular vectors, respectively.

We then apply perturbations to the first $k$ singular values:

$$
\Sigma_{l}^{\prime}=\Sigma_{l}+\text{diag}(w_{1},\ldots,w_{k},0,\ldots,0)
$$

where $w_{i}\sim\mathcal{N}(0,\sigma)$ are sampled independently, and $\sigma$ is a hyperparameter controlling mutation strength. The mutated weight matrix is then reconstructed:

$$
W_{l}^{\prime}=U_{l}\Sigma_{l}^{\prime}V_{l}^{T}
$$

This approach is loosely inspired by the transformer-squared SVD-based finetuning method [^126] and offers several advantages. By perturbing along the principal components-which capture the most significant variance in the weight space-we maintain the fundamental geometric structure of the weights while allowing controlled exploration. This generalizes the task vector SVD mutation operator by [^72] but still allows for training fewer, higher signal parameters.

Our mutation operator becomes a pass-through for rank-1 matrices (e.g., layer normalization or bias parameters).

## Appendix N Justification of Open-endedness Design Choices

This section provides detailed justification for each open-endedness component in AC/DC, grounded in established principles from the literature on evolutionary computation, quality-diversity, and coevolution.

### N.1 Summary

- Minimal Criteria (Gibberish & Impossible Task Filters): Prevents degenerate solutions from dominating while enabling exploration, following MCC principles [^14] [^15].
- Quality-Diversity via DNS: Balances performance and diversity without predefined niches, handling variable-dimensional skill vectors that grow with task evolution [^7].
- Skill Vectors as Behavioral Descriptors: Provides fine-grained capability signatures that naturally adapt to task evolution, requiring no manual niche design or learning (unlike MAP-Elites [^98] [^28]).
- Coevolution of Models and Tasks: Creates complexity explosion through bidirectional feedback, with tasks adapting to model capabilities and vice versa [^136] [^137].
- Task Adaptation via Difficulty Profiles: Maintains tasks in the learnable regime-challenging but not impossible-implementing automatic curriculum generation [^153] [^35].
- Novelty Filtering for Tasks: Prevents trivial task variants by explicitly rewarding semantic novelty, core to Novelty Search principles [^76] [^91].
- Task Reflection and Validation: Ensures task quality through scientist LLM self-solving, preventing broken or ambiguous tasks from accumulating [^91].
- Historical Archive & Coverage-Based Selection: Preserves specialized models from all generations and selects task force based on synthetic task Coverage, not benchmark performance [^112].

Together, these choices implement key properties of open-ended systems: continual novelty generation, increasing complexity, cumulative innovation, and minimal criteria rather than explicit objectives [^123] [^125].

### N.2 Minimal Criteria for Models and Tasks

Design Choice: AC/DC implements two primary minimal criteria (MC) filters: (1) the gibberish filter for models, which eliminates degenerate LLMs producing incoherent text, and (2) the impossible task filter, which removes tasks that no model in the population can solve.

Justification: This design directly follows the Minimal Criterion Coevolution (MCC) framework established by [^14], which demonstrates that defining MCs for both agents and environments enables more open-ended outcomes in coevolution. The fundamental insight is that MCs prevent the search from being dominated by completely undesired outcomes while still enabling exploration to flourish.

The gibberish filter addresses a critical failure mode in model merging: degenerate models that produce syntactically invalid or semantically meaningless text. Without this filter, such models could dominate the population simply by producing output that accidentally matches ground truth through random character generation. This aligns with the principle in [^77] that evolution requires protection against deceptive local optima that appear successful by trivial metrics.

The impossible task filter prevents the task archive from accumulating challenges that lie outside the reach of the current model population’s capabilities. As noted by [^122], without such filtering, the coevolutionary process can become trapped in arms races where increasingly difficult tasks provide no useful gradient for improvement. By replacing impossible tasks with their parent tasks, we maintain difficulty adaptation while ensuring tasks remain within the “learnable” regime described by [^55] as essential for open-endedness.

### N.3 Quality-Diversity via Dominated Novelty Search

Design Choice: AC/DC employs Dominated Novelty Search (DNS) [^7] for model selection, computing local competition fitness by measuring each solution’s distance from better-performing solutions in skill vector space.

Justification: The integration of quality-diversity principles addresses a fundamental challenge in open-ended discovery: maintaining both high performance and behavioral diversity without predefined niches. Traditional Novelty Search [^76] [^78] promotes exploration by rewarding behavioral novelty regardless of performance, while MAP-Elites [^98] requires predefined behavioral dimensions and discretization.

DNS offers several advantages for our domain:

1. Adaptive Behavior Spaces: Unlike MAP-Elites’ fixed grid structure, DNS naturally handles variable-dimensional behavioral descriptors. Our skill vectors grow as new tasks are added to the archive, making predefined niche boundaries impractical. This aligns with the adaptive approaches for evaluating novelty introduced by [^95] and [^109], which enable more open-ended exploration of different spaces of novelty.
2. Local Competition without Binning: DNS implements the local competition principle established by [^79] for encouraging diversity, but avoids the limitations of binned behavior characteristics. As we note in the related work, CycleQD’s use of aggregated benchmark accuracies can fail to distinguish models with unique subfield expertise (e.g., physics vs. biology specialists both appearing in a “science” bin). DNS preserves fine-grained distinctions through continuous distance metrics in skill vector space.
3. Quality Pressure with Diversity: By measuring distances only to better-performing neighbors, DNS maintains explicit optimization pressure toward high-quality solutions while rewarding distance from those solutions-effectively balancing the exploration-exploitation trade-off central to QD methods [^112] [^29].

### N.4 Skill Vectors as Behavioral Descriptors

Design Choice: AC/DC represents model capabilities through binary skill vectors, where each element indicates task completion status, serving as behavioral signatures for diversity measurement.

Justification: This representation addresses multiple challenges in applying QD to LLM discovery:

1. No Predefined Niches Required: Traditional MAP-Elites requires manually specifying behavioral dimensions and their ranges before evolution begins. As [^43] and [^68] note, learned parametrized behavior functions can adapt to problem structure, but require additional training. Skill vectors emerge naturally from evaluation, requiring no a priori design or learning.
2. Fine-Grained Behavior Characterization: Each skill vector provides a detailed signature of what a model can solve, analogous to the “illumination” concept in QD [^98] but at task-level granularity. This enables AC/DC to distinguish models with complementary expertise (e.g., one model excels at physics while another excels at biology) even when their aggregate performance might be similar.
3. Adaptation to Task Evolution: As the task archive evolves, skill vectors naturally adapt or expand to incorporate new tasks. This aligns with the meta-adaptation approaches in QD [^12] that handle complexity and adaptation of diverse high-quality search spaces, but through a simpler mechanism that does not require explicit meta-learning.
4. Direct Connection to Coverage: Skill vectors directly support our Coverage metric (Eq. 1), which measures collective problem-solving capacity. This provides a natural bridge between behavioral diversity (used during evolution) and practical utility/response quality (measured at test time).

### N.5 Coevolution of Models and Tasks

Design Choice: AC/DC simultaneously evolves both model populations and task distributions, with models evaluated on tasks and tasks filtered based on model performance.

Justification: This bidirectional coevolution implements several established principles:

1. Environmental Complexity from Coevolution: Drawing on [^136] [^137] and PAIRED [^30], we leverage the insight that coevolving agents and environments produces a complexity explosion through local competition. Unlike PAIRED’s adversarial setup, AC/DC uses task difficulty profiles (average pass rates) to guide adaptive task generation, ensuring tasks remain challenging but not impossible.
2. MCC for Both Populations: Following [^14] [^15], we apply minimal criteria to both models (gibberish filter) and tasks (impossible task filter, novelty filter). This dual-sided filtering is essential for open-ended outcomes, as it prevents either population from dominating with trivial or degenerate solutions.
3. Open-Ended Task Generation via LLMs: Recent work demonstrates the potential for open-endedness through LLMs generating diverse environments and challenges [^153] [^3] [^35]. Our approach builds on [^91], who show that open-ended search principles can generate surprisingly novel tasks revealing unexpected LLM capabilities. AC/DC extends this by making task evolution responsive to current model population performance, creating a feedback loop that drives increasing sophistication.
4. Avoiding Benchmark Optimization: By coevolving tasks alongside models and never optimizing explicitly for downstream benchmarks, AC/DC embodies the “abandoning objectives” philosophy of [^78]. The synthetic task distribution provides a training signal that encourages general capability development rather than overfitting to specific evaluation metrics.

### N.6 Task Adaptation Based on Difficulty Profiles

Design Choice: AC/DC classifies parent tasks by their pass rates (difficulty profile) and uses this to determine adaptation type: increase difficulty, decrease difficulty, or generate novel variants.

Justification: This adaptive difficulty mechanism addresses the “interestingness” criterion for open-endedness identified by [^55]. Tasks that are too easy (high pass rate) provide no learning signal, while tasks that are too hard (low pass rate) are frustrating and unlearnable.

This approach implements a form of automatic curriculum generation similar to PAIRED [^30], but tailored to LLM capabilities. Unlike adversarial environment generation that might produce arbitrarily difficult challenges, our difficulty-based adaptation ensures the task distribution remains anchored to the current population’s zone of proximal development-challenging enough to drive improvement but feasible enough to provide useful gradients [^153].

The three-way classification (increase/decrease/novel) also promotes diversity in task evolution. Novel variants at intermediate difficulty levels encourage exploration of different task types and domains, preventing the task archive from collapsing into minor variations on a single theme.

### N.7 Novelty Filtering for Tasks

Design Choice: Generated tasks are compared to the three most similar tasks in the global archive via embedding similarity, with a judge LLM determining if sufficient novelty exists.

Justification: This filtering implements the core principle of Novelty Search: explicitly rewarding behavioral novelty relative to previously discovered solutions [^76] [^32]. Without novelty filtering, task evolution could generate trivial variants (e.g., changing numbers in a math problem) that provide no new behavioral challenges for models.

The use of semantic embeddings for similarity measurement allows AC/DC to recognize deep structural similarity between tasks that might differ superficially. For example, two physics problems with different contexts but identical underlying principles would be flagged as non-novel. This aligns with the notion from [^119] that true novelty requires doing things that are meaningfully different, not merely cosmetically varied.

The judge LLM adds a second layer of semantic understanding, catching cases where embedding similarity alone might miss conceptual relationships. This two-stage process balances computational efficiency (embedding search) with nuanced judgment (LLM evaluation) [^91].

### N.8 Reflection and Validation for Task Quality

Design Choice: The scientist LLM attempts to solve its own generated tasks, with automatic correction for compilation errors and refinement prompts for logic errors.

Justification: This self-evaluation cycle addresses a critical challenge in synthetic data generation: ensuring that automatically generated tasks are well-formed and solvable. Recent work on synthetic data quality [^49] emphasizes that data quality matters as much as quantity.

The iterative refinement process implements a form of minimal criterion for task quality, preventing the task archive from accumulating broken or ambiguous tasks. By having the scientist LLM solve its own tasks before accepting them, we create selection pressure toward tasks with clear problem statements and unambiguous scoring functions.

This also relates to the principle of “autotelic learning” in open-ended systems [^34], where the system must develop its own evaluation criteria. The scientist LLM effectively learns to generate tasks that meet implicit quality standards through its own solution attempts.

### N.9 Historical Model Archive and Task Force Selection

Design Choice: AC/DC maintains a historical archive of all models every $G_{task}$ generations and selects the final task force by maximizing Coverage over the global task archive.

Justification: The historical archive implements a key principle from QD: maintaining a collection of diverse high-quality solutions rather than just the current population [^112]. This is crucial because behavioral diversity at intermediate generations might not be preserved if we only keep the final population. Some specialized models might be replaced during evolution, but could still contribute unique capabilities to the final ensemble.

The Coverage-based selection for the task force directly optimizes for our practical goal: collective problem-solving capacity across diverse tasks. This selection is independent of downstream benchmarks, implementing the “novelty search without objectives” approach while still providing a clear utility-based criterion for ensemble construction.

Importantly, this selection happens after coevolution completes, avoiding optimization pressure during evolution. This prevents the kind of overfitting to specific benchmarks that could be expected in recent evolutionary model merging work [^4]. Our models are selected based on synthetic task Coverage, then evaluated on held-out benchmarks, ensuring genuine out-of-distribution generalization.

### N.10 Synthesis: AC/DC as an Open-Ended System

Taken together, these design choices implement the key properties of open-ended systems identified by [^123] and [^124]:

1. Continual Generation of Novelty: The coevolution of models and tasks produces an ongoing stream of new capabilities and challenges, with no predetermined endpoint.
2. Increasing Complexity: Task difficulty adaptation and model selection pressure drive both populations toward increasing sophistication over time (demonstrated in Fig. 1’s improvement trajectory).
3. Cumulative Innovation: New models build on previous models through crossover, and new tasks build on previous tasks through adaptation, creating a stepping-stone effect where discoveries enable further discoveries.
4. No Explicit Fitness Function: While we use quality (task pass rates) and diversity (skill vector distances) for selection, we never optimize explicitly for downstream benchmarks, allowing unexpected capabilities to emerge.
5. Minimal Criteria Rather Than Objectives: Our gibberish and impossible task filters prevent completely undesired outcomes without constraining the search to predefined goals.

This combination of principles, grounded in established open-endedness literature, enables AC/DC to discover model collectives with broader and more diverse capabilities than methods that optimize directly for benchmark performance, while maintaining lower computational costs than training large monolithic models.

[^1]: Competition and attraction improve model fusion. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 1217–1225. Cited by: §A.3.1, Appendix G, §6.

[^2]: Unsupervised task clustering for multi-task reinforcement learning. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases, pp. 222–237. Cited by: §D.6.

[^3]: LLM-poet: evolving complex environments using large language models. External Links: 2406.04663 Cited by: item 3, Appendix G, §1.

[^4]: Evolutionary optimization of model merging recipes. Nature Machine Intelligence 7 (2), pp. 195–204. Cited by: §N.9, Appendix G, §1, §2.

[^5]: A survey on data selection for language models. arXiv preprint arXiv:2402.16827. Cited by: §1.

[^6]: Program synthesis with large language models. arXiv preprint arXiv:2108.07732. Cited by: §A.4.1, §D.5.

[^7]: Dominated novelty search: rethinking local competition in quality-diversity. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 104–112. Cited by: 2nd item, §N.3, §D.5, Appendix G, §2.

[^8]: Constitutional ai: harmlessness from ai feedback. arXiv preprint arXiv:2212.08073. Cited by: Appendix G.

[^9]: Deep surrogate assisted generation of environments. Advances in Neural Information Processing Systems 35, pp. 37762–37777. Cited by: Appendix G.

[^10]: Deepseek llm: scaling open-source language models with longtermism. arXiv preprint arXiv:2401.02954. Cited by: §A.2.

[^11]: On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258. Cited by: §1.

[^12]: Quality-diversity meta-evolution: customizing behavior spaces to a meta-objective. IEEE Transactions on Evolutionary Computation 26 (5), pp. 1171–1181. Cited by: item 3, Appendix G.

[^13]: Quality-diversity through ai feedback. Cited by: Appendix G, Appendix G.

[^14]: Minimal criterion coevolution: a new approach to open-ended search. In Proceedings of the Genetic and Evolutionary Computation Conference, GECCO ’17, New York, NY, USA, pp. 67–74. External Links: ISBN 9781450349208, [Link](https://doi.org/10.1145/3071178.3071186), [Document](https://dx.doi.org/10.1145/3071178.3071186) Cited by: 1st item, item 2, §N.2, Appendix G, §1, §2, §3.

[^15]: Diversity preservation in minimal criterion coevolution through resource limitation. In Proceedings of the 2020 Genetic and Evolutionary Computation Conference, GECCO ’20, New York, NY, USA, pp. 58–66. External Links: ISBN 9781450371285, [Link](https://doi.org/10.1145/3377930.3389809), [Document](https://dx.doi.org/10.1145/3377930.3389809) Cited by: 1st item, item 2, Appendix G, §2.

[^16]: Large language monkeys: scaling inference compute with repeated sampling. arXiv preprint arXiv:2407.21787. Cited by: Appendix G.

[^17]: Language models are few-shot learners. Advances in neural information processing systems 33, pp. 1877–1901. Cited by: §1.

[^18]: Why creativity cannot be interpolated. MLST Archive. External Links: [Link](https://archive.mlst.ai/paper/why-creativity-cannot-be-interpolated) Cited by: §6.

[^19]: Persona: a reproducible testbed for pluralistic alignment. In Proceedings of the 31st International Conference on Computational Linguistics, pp. 11348–11368. Cited by: Appendix G.

[^20]: Quality-diversity optimization: a novel branch of stochastic optimization. In Black Box Optimization, Machine Learning, and No-Free Lunch Theorems, pp. 109–135. Cited by: Appendix G.

[^21]: Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374. Cited by: §A.4.1.

[^22]: Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374. Cited by: Appendix G.

[^23]: Modifying large language model post-training for diverse creative writing. arXiv preprint arXiv:2503.17126. Cited by: Appendix G.

[^24]: AI-gas: ai-generating algorithms, an alternate paradigm for producing general artificial intelligence. External Links: 1905.10985, [Link](https://arxiv.org/abs/1905.10985) Cited by: §1.

[^25]: Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168. Cited by: §A.4.1, §D.5.

[^26]: Scaling map-elites to deep neuroevolution. In Proceedings of the 2020 Genetic and Evolutionary Computation Conference, pp. 67–75. Cited by: Appendix G.

[^27]: Improving exploration in evolution strategies for deep reinforcement learning via a population of novelty-seeking agents. Advances in neural information processing systems 31. Cited by: Appendix G.

[^28]: Robots that can adapt like animals. Nature 521 (7553), pp. 503–507. Cited by: 3rd item, Appendix G.

[^29]: Quality and diversity optimization: a unifying modular framework. IEEE Transactions on Evolutionary Computation 22 (2), pp. 245–259. Cited by: item 3, Appendix G.

[^30]: Emergent complexity and zero-shot transfer via unsupervised environment design. Advances in neural information processing systems 33, pp. 13049–13061. Cited by: item 1, §N.6, §1.

[^31]: Foundation model self-play: open-ended strategy innovation via foundation models. arXiv preprint arXiv:2507.06466. Cited by: Appendix G.

[^32]: Novelty search: a theoretical perspective. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 99–106. Cited by: §N.7, Appendix G.

[^33]: Improving factuality and reasoning in language models through multiagent debate. In International Conference on Machine Learning (ICML), Note: arXiv:2305.14325 Cited by: Appendix G.

[^34]: Meta-diversity search in complex systems, a recipe for artificial open-endedness?. Cited by: §N.8, Appendix G.

[^35]: OMNI-epic: open-endedness via models of human notions of interestingness with environments programmed in code. External Links: 2405.15568 Cited by: 5th item, item 3, Appendix G, §1.

[^36]: Enhancing map-elites with multiple parallel evolution strategies. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 1082–1090. Cited by: Appendix G.

[^37]: Covariance matrix adaptation for the rapid illumination of behavior space. In Proceedings of the 2020 genetic and evolutionary computation conference, pp. 94–102. Cited by: Appendix G.

[^38]: Creative beam search: llm-as-a-judge for improving response generation. arXiv preprint arXiv:2405.00099. Cited by: Appendix G.

[^39]: DiffSampling: enhancing diversity and accuracy in neural text generation. arXiv preprint arXiv:2502.14037. Cited by: Appendix G.

[^40]: On the creativity of large language models. AI & society 40 (5), pp. 3785–3795. Cited by: §6.

[^41]: The vendi score: a diversity evaluation metric for machine learning. arXiv preprint arXiv:2210.02410. Cited by: §D.3.

[^42]: Data-efficient design exploration through surrogate-assisted illumination. Evolutionary computation 26 (3), pp. 381–410. Cited by: Appendix G.

[^43]: Are quality diversity algorithms better at generating stepping stones than objective-based search?. In Proceedings of the Genetic and Evolutionary Computation Conference Companion, pp. 115–116. Cited by: item 1.

[^44]: The language model evaluation harness. Zenodo. External Links: [Document](https://dx.doi.org/10.5281/zenodo.12608602), [Link](https://zenodo.org/records/12608602) Cited by: §A.4.1.

[^45]: The llama 3 herd of models. arXiv preprint arXiv:2407.21783. Cited by: §A.2.

[^46]: Quality-diversity actor-critic: learning high-performing and diverse behaviors via value and successor features critics. In International Conference on Machine Learning, Cited by: Appendix G.

[^47]: Collective intelligence for deep learning: a survey of recent developments. Collective Intelligence 1 (1), pp. 26339137221114874. Cited by: §1.

[^48]: Completely derandomized self-adaptation in evolution strategies. Evolutionary Computation 9, pp. 159–195. External Links: [Document](https://dx.doi.org/10.1162/106365601750190398) Cited by: Appendix G, §2.

[^49]: Surveying the effects of quality, diversity, and complexity in synthetic data from large language models. arXiv preprint arXiv:2412.02980. Cited by: §N.8, Appendix G, Appendix G, §1.

[^50]: Measuring massive multitask language understanding. In International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=d7KBjmI3GmQ) Cited by: §A.4.1, Figure 1.

[^51]: Measuring massive multitask language understanding. Proceedings of the International Conference on Learning Representations (ICLR). Cited by: §1.

[^52]: Less is more: undertraining experts improves model upcycling. arXiv preprint arXiv:2506.14126. Cited by: Appendix J, Appendix C, §6.

[^53]: Automated design of agentic systems. In The Thirteenth International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=t9U3LW7JVX) Cited by: Appendix G.

[^54]: Mirror-consistency: harnessing inconsistency in majority voting. arXiv preprint arXiv:2410.10857. Cited by: Appendix G.

[^55]: Open-endedness is essential for artificial superhuman intelligence. External Links: 2406.04268 Cited by: §N.2, §N.6, Appendix G.

[^56]: Gpt-4o system card. arXiv preprint arXiv:2410.21276. Cited by: §1.

[^57]: Editing models with task arithmetic. arXiv preprint arXiv:2212.04089. Cited by: §M.1.

[^58]: Editing models with task arithmetic. In The Eleventh International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=6t0Kwf8-jrj) Cited by: Appendix G, §2.

[^59]: Wider or deeper? scaling llm inference-time compute with adaptive branching tree search. arXiv preprint arXiv:2503.04412. Cited by: Appendix G, §1, §6.

[^60]: PRIME-environments. External Links: [Link](https://github.com/PrimeIntellect-ai/prime-environments) Cited by: §1.

[^61]: AI safety via debate. arXiv preprint arXiv:1805.00899. Cited by: Appendix G.

[^62]: Creative preference optimization. arXiv preprint arXiv:2505.14442. Cited by: Appendix G.

[^63]: General intelligence requires rethinking exploration. Royal Society Open Science 10 (6), pp. 230539. Cited by: Appendix G.

[^64]: Regularized best-of-n sampling to mitigate reward hacking for language model alignment. In Proceedings of the Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), Note: arXiv:2404.01054 Cited by: Appendix G.

[^65]: Challenges and applications of large language models. arXiv preprint arXiv:2307.10169. Cited by: §1.

[^66]: The common pile v0. 1: an 8tb dataset of public domain and openly licensed text. arXiv preprint arXiv:2506.05209. Cited by: §1.

[^67]: Model-based quality-diversity search for efficient robot learning. In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9675–9680. Cited by: Appendix G.

[^68]: Bayesian optimisation for quality diversity search with coupled descriptor functions. IEEE Transactions on Evolutionary Computation. Cited by: item 1, Appendix G.

[^69]: The art of scaling reinforcement learning compute for llms. arXiv preprint arXiv:2510.13786. Cited by: Appendix L.

[^70]: Understanding the effects of rlhf on llm generalisation and diversity. arXiv preprint arXiv:2310.06452. Cited by: Appendix G.

[^71]: Questioning representational optimism in deep learning: the fractured entangled representation hypothesis. arXiv preprint arXiv:2505.11581. Cited by: §1.

[^72]: Agent skill acquisition for large language models via cycleQD. In The Thirteenth International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=Kvdh12wGC0) Cited by: §M.1, §M.2, §D.5, Appendix G, §2.

[^73]: Tulu 3: pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124. Cited by: §1.

[^74]: Diverse preference optimization. arXiv preprint arXiv:2501.18101. Cited by: Appendix G.

[^75]: Evolution through large models. In Handbook of Evolutionary Machine Learning, pp. 331–366. Cited by: §1.

[^76]: Exploiting open-endedness to solve problems through the search for novelty.. In ALIFE, pp. 329–336. Cited by: 6th item, §N.3, §N.7, Appendix G.

[^77]: Revising the evolutionary computation abstraction: minimal criteria novelty search. In Proceedings of the 12th annual conference on Genetic and evolutionary computation, pp. 103–110. Cited by: §N.2, Appendix G.

[^78]: Abandoning objectives: evolution through the search for novelty alone. Evolutionary computation 19 (2), pp. 189–223. Cited by: item 4, §N.3, Appendix G, §1.

[^79]: Evolving a diversity of virtual creatures through novelty search and local competition. In Proceedings of the 13th annual conference on Genetic and evolutionary computation, pp. 211–218. Cited by: item 2, Appendix G, Appendix G, §2.

[^80]: Solving quantitative reasoning problems with language models. Advances in neural information processing systems 35, pp. 3843–3857. Cited by: §A.4.1.

[^81]: Making ai less’ thirsty’. Communications of the ACM 68 (7), pp. 54–61. Cited by: §1.

[^82]: Encouraging divergent thinking in large language models through multi-agent debate. arXiv preprint arXiv:2305.19118. Cited by: Appendix G, §1.

[^83]: Encouraging divergent thinking in large language models through multi-agent debate. In Proceedings of the 2024 conference on empirical methods in natural language processing, pp. 17889–17904. Cited by: Appendix G.

[^84]: Let’s verify step by step. arXiv preprint arXiv:2305.20050. Note: OpenAI Cited by: Appendix G.

[^85]: Efficient exploration using model-based quality-diversity with gradients. In Artificial Life Conference Proceedings 35, Vol. 2023, pp. 4. Cited by: Appendix G.

[^86]: Skywork-reward-v2: scaling preference data curation via human-ai synergy. arXiv preprint arXiv:2507.01352. Cited by: §A.4.3.

[^87]: Muon is scalable for llm training. arXiv preprint arXiv:2502.16982. Cited by: §1.

[^88]: Best practices and lessons learned on synthetic data. arXiv preprint arXiv:2404.07503. Cited by: Appendix G.

[^89]: AgentBench: evaluating llms as agents. arXiv preprint arXiv: 2308.03688. Cited by: §D.5.

[^90]: The ai scientist: towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292. Cited by: §1, §6.

[^91]: Automated capability discovery via foundation model self-exploration. arXiv preprint arXiv:2502.07577. Cited by: 6th item, 7th item, item 3, §N.7, §D.3, Appendix F, Appendix G, §1, §3.

[^92]: Rephrasing the web: a recipe for compute and data-efficient language modeling. arXiv preprint arXiv:2401.16380. Cited by: Appendix G, §1.

[^93]: Hdbscan: hierarchical density based clustering. Journal of Open Source Software 2 (11), pp. 205. External Links: [Document](https://dx.doi.org/10.21105/joss.00205), [Link](https://doi.org/10.21105/joss.00205) Cited by: Figure 8.

[^94]: Metr task standard. External Links: [Link](https://github.com/METR/task-standard/blob/main/STANDARD.md) Cited by: §3.

[^95]: Learning behavior characterizations for novelty search. In Proceedings of the Genetic and Evolutionary Computation Conference 2016, pp. 149–156. Cited by: item 1, Appendix G.

[^96]: Discovering evolutionary stepping stones through behavior domination. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 139–146. Cited by: §2.

[^97]: Complexity: a guided tour. Oxford university press. Cited by: §1.

[^98]: Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. Cited by: 3rd item, item 2, §N.3, Appendix G.

[^99]: Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. Cited by: §2.

[^100]: Generative representational instruction tuning. In The Thirteenth International Conference on Learning Representations, Cited by: §1.

[^101]: Scaling data-constrained language models. Advances in Neural Information Processing Systems 36, pp. 50358–50376. Cited by: §1.

[^102]: Understanding innovation engines: automated creativity and improved stochastic optimization via deep learning. Evolutionary computation 24 (3), pp. 545–572. Cited by: §1.

[^103]: From text to life: on the reciprocal relationship between artificial life and large language models. In Artificial Life Conference Proceedings 36, Vol. 2024, pp. 39. Cited by: §1.

[^104]: AlphaEvolve: a coding agent for scientific and algorithmic discovery. Google DeepMind. Cited by: §1.

[^105]: Attributing mode collapse in the fine-tuning of large language models. In ICLR 2024 Workshop on Mathematical and Empirical Understanding of Foundation Models, Vol. 2, pp. 2. Cited by: Appendix G.

[^106]: Persona generators: generating diverse synthetic personas at scale. arXiv preprint arXiv:2602.03545. Cited by: Appendix G.

[^107]: A cost-benefit analysis of on-premise large language model deployment: breaking even with commercial llm services. External Links: 2509.18101, [Link](https://arxiv.org/abs/2509.18101) Cited by: §1.

[^108]: Discovering and exploiting sparse rewards in a learned behavior space. Evolutionary Computation 32 (3), pp. 275–305. Cited by: Appendix G.

[^109]: Unsupervised learning and exploration of reachable outcome space. In 2020 IEEE International Conference on Robotics and Automation (ICRA), pp. 2379–2385. Cited by: item 1, Appendix G.

[^110]: Discovering language model behaviors with model-written evaluations. In Findings of the association for computational linguistics: ACL 2023, pp. 13387–13434. Cited by: Appendix G.

[^111]: Aces: generating a diversity of challenging programming puzzles with autotelic generative models. Advances in Neural Information Processing Systems 37, pp. 67627–67662. Cited by: Appendix G, Appendix G.

[^112]: Quality diversity: a new frontier for evolutionary computation. Frontiers in Robotics and AI 3, pp. 40. Cited by: 8th item, item 3, §N.9, Appendix G, §2.

[^113]: Qwen2.5 technical report. arXiv preprint arxiv:2412.15115. External Links: [Link](https://arxiv.org/abs/2412.15115) Cited by: §A.2.

[^114]: Gpqa: a graduate-level google-proof q&a benchmark. In First Conference on Language Modeling, Cited by: §A.4.1.

[^115]: Mathematical discoveries from program search with large language models. Nature. External Links: [Document](https://dx.doi.org/10.1038/s41586-023-06924-6) Cited by: §1.

[^116]: Rainbow teaming: open-ended generation of diverse adversarial prompts. Advances in Neural Information Processing Systems 37, pp. 69747–69786. Cited by: Appendix G.

[^117]: Deepseekmath: pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300. Cited by: §1.

[^118]: Judging the judges: a systematic study of position bias in llm-as-a-judge. arXiv preprint arXiv:2406.07791. Cited by: Appendix G.

[^119]: A definition of open-ended learning problems for goal-conditioned agents. arXiv preprint arXiv:2311.00344. Cited by: §N.7, Appendix G.

[^120]: Should we be going mad? a look at multi-agent debate strategies for llms. arXiv preprint arXiv:2311.17371. Cited by: Appendix G.

[^121]: Scaling LLM test-time compute optimally can be more effective than scaling model parameters. arXiv preprint arXiv:2408.03314. Note: August 2024 Cited by: Appendix G.

[^122]: Identifying necessary conditions for open-ended evolution through the artificial life world of chromaria. In Proc. Int. Conf. on the Sythesis and Simulation of Living Systems (ALIFE), Cambridge, MA, pp. 793–800. Cited by: §N.2, Appendix G.

[^123]: Open-endedness: the last grand challenge you’ve never heard of. While open-endedness could be a force for discovering intelligence, it could also be a component of AI itself. Cited by: §N.1, §N.10, Appendix G, §1, §6.

[^124]: Why greatness cannot be planned: the myth of the objective. Springer. Cited by: §N.10, Appendix G, §1, §6.

[^125]: Why open-endedness matters. Artificial life 25 (3), pp. 232–235. Cited by: §N.1.

[^126]: Transformer-squared: self-adaptive LLMs. In The Thirteenth International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=dh4t9qmcvK) Cited by: §M.2, §2.

[^127]: Challenging big-bench tasks and whether chain-of-thought can solve them. arXiv preprint arXiv:2210.09261. Cited by: §A.4.1.

[^128]: Wisdom of the machines: exploring collective intelligence in LLM crowds. In First Workshop on Social Simulation with LLMs, External Links: [Link](https://openreview.net/forum?id=fxqroxvUhk) Cited by: Appendix G.

[^129]: L. Teodorescu, C. Colas, M. Bowers, T. Carta, and P. Oudeyer Codeplay: autotelic learning through collaborative self-play in programming environments. In Intrinsically-Motivated and Open-Ended Learning Workshop@ NeurIPS2023, Cited by: Appendix G.

[^130]: Visualizing data using t-sne. Journal of Machine Learning Research 9 (86), pp. 2579–2605. External Links: [Link](http://jmlr.org/papers/v9/vandermaaten08a.html) Cited by: Figure 8.

[^131]: Using centroidal Voronoi tessellations to scale up the multidimensional archive of phenotypic elites algorithm. IEEE Transactions on Evolutionary Computation 22 (4), pp. 623–630. Cited by: Appendix G.

[^132]: Discovering the elite hypervolume by leveraging interspecies correlation. In Proceedings of the Genetic and Evolutionary Computation Conference, GECCO ’18, New York, NY, USA, pp. 149–156. External Links: ISBN 9781450356183, [Link](https://doi.org/10.1145/3205455.3205602), [Document](https://dx.doi.org/10.1145/3205455.3205602) Cited by: Appendix G.

[^133]: Attention is all you need. Advances in neural information processing systems 30. Cited by: §1.

[^134]: Diverse beam search: decoding diverse solutions from neural sequence models. arXiv preprint arXiv:1610.02424. Cited by: Appendix G.

[^135]: Improving text embeddings with large language models. arXiv preprint arXiv:2401.00368. Cited by: §F.3.

[^136]: Paired open-ended trailblazer (POET): endlessly generating increasingly complex and diverse learning environments and their solutions. CoRR abs/1901.01753. External Links: [Link](http://arxiv.org/abs/1901.01753) Cited by: 4th item, item 1, Appendix G, §1.

[^137]: Enhanced poet: open-ended reinforcement learning through unbounded invention of learning challenges and their solutions. In International conference on machine learning, pp. 9940–9951. Cited by: 4th item, item 1, Appendix G.

[^138]: Ranked voting based self-consistency of large language models. arXiv preprint arXiv:2505.10772. Cited by: Appendix G.

[^139]: Self-consistency improves chain of thought reasoning in language models. In International Conference on Learning Representations (ICLR), Note: arXiv:2203.11171 Cited by: Appendix G.

[^140]: Self-instruct: aligning language models with self-generated instructions. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.), Toronto, Canada, pp. 13484–13508. External Links: [Link](https://aclanthology.org/2023.acl-long.754/), [Document](https://dx.doi.org/10.18653/v1/2023.acl-long.754) Cited by: Appendix G.

[^141]: Self-instruct: aligning language models with self-generated instructions. External Links: 2212.10560 Cited by: §1.

[^142]: MMLU-pro: a more robust and challenging multi-task language understanding benchmark. In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track, External Links: [Link](https://openreview.net/forum?id=y10DM6R2r3) Cited by: §A.4.1, Figure 1.

[^143]: Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems 35, pp. 24824–24837. Cited by: §F.2.

[^144]: Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In International conference on machine learning, pp. 23965–23998. Cited by: Appendix G, §2.

[^145]: WizardLM: empowering large language models to follow complex instructions. External Links: 2304.12244 Cited by: §1.

[^146]: Ties-merging: resolving interference when merging models. Advances in Neural Information Processing Systems 36, pp. 7093–7115. Cited by: Appendix G.

[^147]: Qwen3 technical report. arXiv preprint arXiv:2505.09388. Cited by: §A.2, §1.

[^148]: Qwen2 technical report. arXiv preprint arxiv:2407.10671. Cited by: §A.2.

[^149]: Language models are super mario: absorbing abilities from homologous models as a free lunch. In Forty-first International Conference on Machine Learning, Cited by: Appendix G.

[^150]: Pass@ k metric for rlvr: a diagnostic tool of exploration, but not an objective. arXiv preprint arXiv:2511.16231. Cited by: Appendix G.

[^151]: LLMs can’t jump. Cited by: §6.

[^152]: Darwin godel machine: open-ended evolution of self-improving agents. arXiv preprint arXiv:2505.22954. Cited by: §E.2.2, Appendix G.

[^153]: OMNI: open-endedness via models of human notions of interestingness. arXiv preprint arXiv:2306.01711. Cited by: 5th item, item 3, §N.6, Appendix G, §1.

[^154]: Nature-inspired population-based evolution of large language models. arXiv preprint arXiv:2503.01155. Cited by: Appendix G.

[^155]: Deep surrogate assisted map-elites for automated hearthstone deckbuilding. In Proceedings of the Genetic and Evolutionary Computation Conference, pp. 158–167. Cited by: Appendix G.

[^156]: Absolute zero: reinforced self-play reasoning with zero data. arXiv preprint arXiv:2505.03335. Cited by: Appendix G, §1.

[^157]: Judging LLM-as-a-judge with MT-Bench and chatbot arena. In Advances in Neural Information Processing Systems (NeurIPS), Note: arXiv:2306.05685 Cited by: Appendix G.