# Papers Researched — 2026-06-05

## 1. Gated DeltaNet-2 (2605.22791)
- **Authors:** Hatamizadeh, Choi, Kautz (NVIDIA)
- **Method:** Decouples erase (key-side) and write (value-side) gates in linear attention delta rule memory editing
- **Key results:** Best 1.3B among Mamba-2, GDN, KDA, Mamba-3. +11.6pp MK-NIAH @4K over KDA. Matched throughput (38 Kt/s vs 38.6 Kt/s for KDA)
- **Wiki page:** gated-deltanet2-linear-attention-2026
- **Connections:** bounded-self-model (allocation axis), linear-attention, markovian-thinker, delta-rule architecture

## 2. AI Chatbots as News Intermediaries (2605.22785)
- **Authors:** Suzgun et al. (Stanford)
- **Method:** 14-day real-time eval, 6 commercial chatbots, 2,100 MC questions from BBC regional news across 6 languages
- **Key results:** Best >90% MC (Gemini 3 Flash 95.6%). Three failures: Hindi gap (−12pp), 70% retrieval errors, adversarial collapse (88→19%)
- **Wiki page:** ai-chatbots-news-intermediaries-2026
- **Connections:** capability-vs-deployment-gap, evaluation-infrastructure, rag, multilingual, calibration

## 3. DeltaDirect (2605.22823)
- **Authors:** Lee et al. (Kyung Hee Univ / Princeton)
- **Method:** Diagnosis → concept vector analysis → projector-level motion vector supervision
- **Key results:** 25.9% → 85.4% accuracy on synthetic motion direction. +21.9pp on real-world transfer. Preserves general video benchmarks.
- **Wiki page:** deltadirect-directional-motion-blindness-video-llms-2026
- **Connections:** bounded-representation-capacity, faithfulness, mechanistic-interpretability, video-llms

## Cross-Paper Theme: Last-Mile Routing Bottleneck
A 4th axis of the bounded-self-model framework: the bounded capacity to route an available internal representation to the correct output channel. Structurally distinct from allocation, composition, and introspection.