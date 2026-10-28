# Awesome-Video-LMM-Post-Training [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models

> *[Yolo Y. Tang](https://yoloytang.me/)<sup>1</sup>, [Jing Bi](https://jing.vision/)<sup>1</sup>, [Pinxin Liu](https://andypinxinliu.github.io/)<sup>1</sup>, [Zhenyu Pan](https://pzyseere.github.io/)<sup>2</sup>, [Zhangyun Tan](https://zhangyun04.github.io/)<sup>1</sup>, [Qianxiang Shen](https://github.com/chrisqarrowx)<sup>1</sup>, [Jiani Liu](https://openreview.net/profile?id=%7EJiani_Liu5)<sup>1</sup>, [Hang Hua](https://hanghuacs.notion.site/)<sup>1</sup>, [Junjia Guo](https://www.linkedin.com/in/junjia-guo-b3a9b5336/)<sup>1</sup>, [Yunzhong Xiao](https://scholar.google.com/citations?user=b9uTwEgAAAAJ&hl=en)<sup>3</sup>, [Chao Huang](https://wikichao.github.io/)<sup>1</sup>, [Zhiyuan Wang](https://scholar.google.com/citations?user=4TdiRMYAAAAJ&hl=en)<sup>4</sup>, [Susan Liang](https://liangsusan-git.github.io/)<sup>1</sup>, [Xinyi Liu](https://xinyiliu0227.github.io/)<sup>1</sup>, [Yizhi Song](https://song630.github.io/yizhisong.github.io/)<sup>5</sup>, [Junhua Huang](https://harry-junhua-huang.github.io/)<sup>6</sup>, [Jia-Xing Zhong](https://scholar.google.com/citations?hl=en&user=dIckm98AAAAJ)<sup>7</sup>, [Bozheng Li](https://openreview.net/profile?id=~Bozheng_Li1)<sup>8</sup>, [Daiqing Qi](https://daiqing-qi.github.io/me/index.html)<sup>9</sup>, [Ziyun Zeng](https://scholar.google.com/citations?user=b2DIlscAAAAJ)<sup>1</sup>, [Ali Vosoughi](https://alivosoughi.com/)<sup>1</sup>, [Luchuan Song](https://songluchuan.github.io/)<sup>1</sup>, [Zeliang Zhang](https://zhangaipi.github.io/)<sup>1</sup>, [Daiki Shimada](https://scholar.google.com/citations?user=1uAwouQAAAAJ&hl=en)<sup>10</sup>, [Han Liu](https://magics.cs.northwestern.edu/people.html)<sup>2</sup>, [Jiebo Luo](https://www.cs.rochester.edu/u/jluo/)<sup>1</sup>, [Chenliang Xu](https://www.cs.rochester.edu/u/cxu22/)<sup>1</sup>*

> *<sup>1</sup>University of Rochester, <sup>2</sup>Northwestern University, <sup>3</sup>CMU, <sup>4</sup>UCSB, <sup>5</sup>Purdue University, <sup>6</sup>UCLA, <sup>7</sup>University of Oxford, <sup>8</sup>Brown University, <sup>9</sup>University of Virginia, <sup>10</sup>Sony Group Corporation*

[![hf_paper](https://img.shields.io/badge/🤗-Paper%20In%20HF-red.svg)](https://huggingface.co/papers/2510.05034) [![arXiv](https://img.shields.io/badge/Arxiv-2510.05034-AD1C18.svg?logo=arXiv)](https://arxiv.org/abs/2510.05034) 

![image](./assets/timeline.png)

## News
- **[2025/10/06]** 🎉 Our survey paper on Video-LMM Post-Training for Video Reasoning is now available on [arXiv](https://arxiv.org/abs/2510.05034) and [Hugging Face Papers](https://huggingface.co/papers/2510.05034)! 
- **[2025/06/18]** 🚀 Initial release of the Awesome-Video-LMM-Post-Training repository! We welcome contributions via Pull Requests.
- **[2025/05/04]** 📢 Our survey paper on Video Understanding with Large Language Model has been accepted to the IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)! 👉 [IEEE Xplore](https://ieeexplore.ieee.org/document/10982110) \| [GitHub](https://github.com/yoloytang/Awesome-LLMs-for-Video-Understanding)

## Overview

This Awesome list systematically curates and tracks the latest research in the post-training of Video-LMMs, with a special emphasis on works that enhance their reasoning capabilities. Following the taxonomy of the field, we focus on three key paradigms:


- 🧠 Reinforced Video-LMMs: Exploring how RL techniques are used to align Video-LMMs with human preferences or specific metrics. This includes methods like RLHF, DPO, GRPO and the design of effective reward models to enhance the logical consistency and factuality of model outputs.

- ⚙️ SFT for Reasoning: Collecting studies that leverage SFT on meticulously curated, reasoning-centric datasets. These works often incorporate CoT or other structured formats to directly teach models how to perform complex, multi-step reasoning.

- 🚀 Test-Time Scaling in Video Reasoning: Focusing on strategies that enhance reasoning capabilities at inference time without requiring further model training. This includes techniques like agentic frameworks, tool use, RAG, long CoT, and other methods that scale reasoning through computation.

- 📊 Benchmarks for Video Reasoning: Including the latest and most challenging benchmarks designed specifically to evaluate the complex reasoning abilities of Video-LMMs.

We hope this repository serves as a comprehensive and up-to-date resource hub for researchers and developers in this cutting-edge field. Contributions from the community are highly welcome via Pull Requests!



## Table of Contents

- [Awesome-Video-LMM-Post-Training](#awesome-video-lmm-post-training)
    - [Overview](#overview)
    - [Table of Contents](#table-of-contents)
    - [Survey](#latest-research-in-video-lmms-post-training)
        - [Reinforced Video-LMMs](#reinforced-video-lmms)
        - [Video-LMM SFT for Reasoning](#video-lmm-sft-for-reasoning)
        - [Test-Time Scaling in Video Reasoning](#test-time-scaling-in-video-reasoning)
        - [Benchmarks for Video Reasoning](#benchmarks-for-video-reasoning)
        - [Related Surveys](#related-surveys)
    - [🌟 Star History](#-star-history)
    - [📝 Citation](#-citation)

    
![image](./assets/teaser.png)

## 📝 Citation

If you find our survey useful for your research, please cite the following paper:

```bibtex
@misc{tang2025videollmposttraining,
  title={Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models},
  author={Yolo Y. Tang, Jing Bi, Pinxin Liu, Zhenyu Pan, Zhangyun Tan, Qianxiang Shen, Jiani Liu, Hang Hua, Junjia Guo, Yunzhong Xiao, Chao Huang, Zhiyuan Wang, Susan Liang, Xinyi Liu, Yizhi Song, Junhua Huang, Jia-Xing Zhong, Bozheng Li, Daiqing Qi, Ziyun Zeng, Ali Vosoughi, Luchuan Song, Zeliang Zhang, Daiki Shimada, Han Liu, Jiebo Luo, Chenliang Xu},
  journal={arXiv preprint arXiv:2510.05034},
  year={2025}
```

## Latest Research in Video-LMMs Post-Training

### Reinforced Video-LMMs

| Title | Paper | Code | Dataset | Venue |
| :--- | :---: | :---: | :---: | :---: |
| Watch Before You Answer: Learning from Visually Grounded Post-Training | [Paper](https://arxiv.org/abs/2604.05117) | [GitHub](https://github.com/reacher-z/vidground) |  | arXiv 2026 |
| Self-alignment of Large Video Language Models with Refined Regularized Preference Optimization | [Paper](https://arxiv.org/abs/2504.12083) | [GitHub](https://github.com/pritamqu/RRPO) | [Dataset](https://huggingface.co/datasets/pritamqu/self-alignment) | NeurIPS 2025 |
| VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception | [Paper](https://arxiv.org/abs/2509.21100) | [GitHub](https://github.com/OpenGVLab/VideoChat-R1) |  | NIPS 2025 |
| MOSS-ChatV: Reinforcement Learning with Process Reasoning Reward for Video Temporal Reasoning | [Paper](https://arxiv.org/abs/2509.21113) |  |  |  |
| TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs | [Paper](https://arxiv.org/abs/2509.18056) |  |  | NeurIPS 2025 |
| ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding | [Paper](https://arxiv.org/abs/2509.15800) |  |  |  |
| AdsQA: Towards Advertisement Video Understanding | [Paper](https://arxiv.org/abs/2509.08621) | [GitHub](https://github.com/TsinghuaC3I/AdsQA) |  | ICCV 2025 |
| Kwai Keye-VL 1.5 Technical Report | [Paper](https://arxiv.org/abs/2509.01563) | [Github](https://github.com/Kwai-Keye/Keye) |  |  |
| Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding | [Paper](https://arxiv.org/abs/2508.20478) |  |  |  |
| Ovis2.5 Technical Report | [Paper](https://arxiv.org/abs/2508.11737) | [Github](https://github.com/AIDC-AI/Ovis) |  |  |
| ReasoningTrack: Chain-of-Thought Reasoning for Long-term Vision-Language Tracking | [Paper](https://arxiv.org/abs/2508.05221) | [Github](https://github.com/Event-AHU/Open_VLTrack) |  |  |
| TAR-TVG: Enhancing VLMs with Timestamp Anchor-Constrained Reasoning for Temporal Video Grounding | [Paper](https://arxiv.org/abs/2508.07683) |  |  |  |
| VQAThinker: Exploring Generalizable and Explainable Video Quality Assessment via Reinforcement Learning | [Paper](https://arxiv.org/abs/2508.06051) | [Github](https://github.com/clh124/VQAThinker) |  |  |
| Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning | [Paper](https://arxiv.org/abs/2508.04416) | [Github](https://github.com/zhang9302002/ThinkingWithVideos) |  | [Dataset](https://huggingface.co/datasets/zhang9302002/MultiTaskVideoReasoning) |
| AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video | [Paper](https://arxiv.org/abs/2508.03100) | [Github](https://github.com/yogkul2000/AVATAR) |  |  |
| ReasonAct: Progressive Training for Fine-Grained Video Reasoning in Small Models | [Paper](https://arxiv.org/abs/2508.01533) |  |  |  |
| ARC-Hunyuan-Video-7B: Structured Video Comprehension of Real-World Shorts | [Paper](https://arxiv.org/abs/2507.20939) | [Github](https://github.com/TencentARC/ARC-Hunyuan-Video-7B) |  |  |
| METER: Multi-modal Evidence-based Thinking and Explainable Reasoning -- Algorithm and Benchmark | [Paper](https://arxiv.org/abs/2507.16206) |  |  |  |
| EmbRACE-3K: Embodied Reasoning and Action in Complex Environments | [Paper](https://arxiv.org/abs/2507.10548) |  |  |  |
| Scaling RL to Long Videos | [Paper](https://arxiv.org/abs/2507.07966) | [GitHub](https://github.com/NVLabs/Long-RL) | [Dataset](https://huggingface.co/datasets/LongVideo-Reason/longvideo-reason) | NeurIPS 2025 |
| Video-RTS: Rethinking Reinforcement Learning and Test-Time Scaling for Efficient and Enhanced Video Reasoning | [Paper](https://arxiv.org/abs/2507.06485) | [GitHub](https://github.com/Ziyang412/Video-RTS) |  | EMNLP 2025 |
| Tempo-R0: A Video-MLLM for Temporal Video Grounding through Efficient Temporal Sensing Reinforcement Learning | [Paper](https://arxiv.org/abs/2507.04702) |  |  |  |
| VRAgent-R1: Boosting Video Recommendation with MLLM-based Agents via Reinforcement Learning | [Paper](https://arxiv.org/abs/2507.02626) |  |  |  |
| Kwai Keye-VL Technical Report | [Paper](https://arxiv.org/abs/2507.01949) | [GitHub](https://github.com/Kwai-Keye/Keye) |  |  |
| VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | [Paper](https://arxiv.org/abs/2506.17221) |  |  |  |
| Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video Reasoning | [Paper](https://arxiv.org/abs/2506.13654) | [GitHub](https://github.com/egolife-ai/Ego-R1) | [Dataset](https://huggingface.co/Ego-R1) |  |
| VersaVid-R1: A Versatile Video Understanding and Reasoning Model from Question Answering to Captioning Tasks | [Paper](https://arxiv.org/abs/2506.09079) | [GitHub](https://github.com/VidBridge-R1/VidBridge-R1) | [Dataset](https://huggingface.co/datasets/VidBridge-R1/VidBridge-R1_training_data) |  |
| VidBridge-R1: Bridging QA and Captioning for RL-based Video Understanding Models with Intermediate Proxy Tasks | [Paper](https://arxiv.org/abs/2506.09079v2) | [Github](https://github.com/VidBridge-R1/VidBridge-R1) |  |  |
| DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO | [Paper](https://arxiv.org/abs/2506.07464) | [GitHub](https://github.com/mlvlab/DeepVideoR1) |  |  |
| AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs | [Paper](https://arxiv.org/abs/2506.05328) | [GitHub](https://github.com/AV-Reasoner/AV-Reasoner) |  |  |
| MiMo-VL Technical Report | [Paper](https://arxiv.org/abs/2506.03569) | [Github](https://github.com/XiaomiMiMo/MiMo-VL) |  |  |
| EgoVLM: Policy Optimization for Egocentric Video Understanding | [Paper](https://arxiv.org/abs/2506.03097) | [GitHub](https://github.com/adityavavre/VidEgoVLM) | [Dataset](https://huggingface.co/datasets/omlab/VLM-R1) |  |
| Reinforcement Learning Tuning for VideoLLMs: Reward Design and Data Efficiency | [Paper](https://arxiv.org/abs/2506.01908) | [GitHub](https://github.com/appletea233/Temporal-R1) |  |  |
| VideoCap-R1: Enhancing MLLMs for Video Captioning via Structured Thinking | [Paper](https://arxiv.org/abs/2506.01725) |  |  |  |
| ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding | [Paper](https://arxiv.org/abs/2506.01300) | [GitHub](https://github.com/aiming-lab/ReAgent-V) |  | NeurIPS 2025 |
| ReFoCUS: Reinforcement-guided Frame Optimization for Contextual Understanding | [Paper](https://arxiv.org/abs/2506.01274) |  |  |  |
| Reinforcing Video Reasoning with Focused Thinking | [Paper](https://arxiv.org/abs/2505.24718) | [GitHub](https://github.com/longmalongma/TW-GRPO) |  |  |
| VAU-R1: Advancing Video Anomaly Understanding via Reinforcement Fine-Tuning | [Paper](https://arxiv.org/abs/2505.23504) | [GitHub](https://github.com/GVCLab/VAU-R1) | [Dataset](https://huggingface.co/datasets/7xiang/VAU-Bench) |  |
| A2Seek: Towards Reasoning-Centric Benchmark for Aerial Anomaly Understanding | [Paper](https://arxiv.org/abs/2505.21962) |  |  |  |
| MUSEG: Reinforcing Video Temporal Understanding via Timestamp-Aware Multi-Segment Grounding | [Paper](https://arxiv.org/abs/2505.20715) | [GitHub](https://github.com/THUNLP-MT/MUSEG) |  |  |
| Omni-R1: Reinforcement Learning for Omnimodal Reasoning via Two-System Collaboration | [Paper](https://arxiv.org/abs/2505.20256) | [GitHub](https://github.com/aim-uofa/Omni-R1) |  |  |
| Vad-R1: Towards Video Anomaly Reasoning via Perception-to-Cognition Chain-of-Thought | [Paper](https://arxiv.org/abs/2505.19877) |  |  |  |
| VerIPO: Cultivating Long Reasoning in Video-LLMs via Verifier-Gudied Iterative Policy Optimization | [Paper](https://arxiv.org/abs/2505.19000) | [GitHub](https://github.com/HITsz-TMG/VerIPO) |  |  |
| Fact-R1: Towards Explainable Video Misinformation Detection with Deep Reasoning | [Paper](https://arxiv.org/abs/2505.16836) |  |  |  |
| From Evaluation to Defense: Advancing Safety in Video Large Language Models | [Paper](https://arxiv.org/abs/2505.16643) |  |  |  |
| Pixel Reasoner: Incentivizing Pixel-Space Reasoning with Curiosity-Driven Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.15966) |  |  |  |
| ViaRL: Adaptive Temporal Grounding via Visual Iterated Amplification Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.15447) | [GitHub](https://github.com/xuzq23/ViaRL) |  |  |
| UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.14231) | [GitHub](https://github.com/AMAP-ML/UniVG-R1) | [Dataset](https://huggingface.co/datasets/GD-ML/UniVG-R1-data) |  |
| BusterX: MLLM-Powered AI-Generated Video Forgery Detection and Explanation | [Paper](https://arxiv.org/abs/2505.12620) |  |  |  |
| VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning | [Paper](https://arxiv.org/abs/2505.12434) | [GitHub](https://github.com/QiWang98/VideoRFT) | [Dataset](https://huggingface.co/datasets/QiWang98/VideoRFT-Data) | NeurIPS 2025 |
| Seed1.5-VL Technical Report | [Paper](https://arxiv.org/abs/2505.07062) |  |  |  |
| Compile Scene Graphs with Reinforcement Learning | [Paper](https://arxiv.org/abs/2504.13617) |  |  |  |
| Self-alignment of Large Video Language Models with Refined Regularized Preference Optimization | [Paper](https://arxiv.org/abs/2504.12083) |  |  |  |
| Mavors: Multi-granularity Video Representation for Multimodal Large Language Model | [Paper](https://arxiv.org/abs/2504.10068) |  |  |  |
| TinyLLaVA-Video-R1: Towards Smaller LMMs for Video Reasoning | [Paper](https://arxiv.org/abs/2504.09641) | [GitHub](https://github.com/ZhangXJ199/TinyLLaVA-Video-R1) |  |  |
| VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning | [Paper](https://arxiv.org/abs/2504.06958) | [GitHub](https://github.com/OpenGVLab/VideoChat-R1) |  |  |
| Spatial-R1: Enhancing MLLMs in Video Spatial Reasoning | [Paper](https://arxiv.org/abs/2504.01805) | [GitHub](https://github.com/OuyangKun10/SpaceR) | [Dataset](https://huggingface.co/datasets/RUBBISHLIKE/SpaceR-151k) |  |
| Improved Visual-Spatial Reasoning via R1-Zero-Like Training | [Paper](https://arxiv.org/abs/2504.00883) |  |  |  |
| Exploring the Effect of Reinforcement Learning on Video Understanding: Insights from SEED-Bench-R1 | [Paper](https://arxiv.org/abs/2503.24376) | [GitHub](https://github.com/TencentARC/SEED-Bench-R1) | [Dataset](https://huggingface.co/datasets/TencentARC/SEED-Bench-R1) |  |
| Video-R1: Reinforcing Video Reasoning in MLLMs | [Paper](https://arxiv.org/abs/2503.21776) | [GitHub](https://github.com/tulerfeng/Video-R1) | [Dataset](https://huggingface.co/datasets/Video-R1/Video-R1-data) |  |
| Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation | [Paper](https://arxiv.org/abs/2503.19622) | [GitHub](https://github.com/Hongcheng-Gao/HAVEN) | [Dataset](https://github.com/Hongcheng-Gao/HAVEN/blob/main/Data/test_data.json) |  |
| TimeZero: Temporal Video Grounding with Reasoning-Guided LVLM | [Paper](https://arxiv.org/abs/2503.13377) | [GitHub](https://github.com/xiaomi-research/time-r1) | [Dataset](https://huggingface.co/datasets/Boshenxx/TimeR1-Dataset) |  |
| ST-Think: How Multimodal Large Language Models Reason About 4D Worlds from Ego-Centric Videos | [Paper](https://arxiv.org/abs/2503.12542) | [GitHub](https://github.com/WPR001/Ego-ST) |  |  |
| Memory-enhanced Retrieval Augmentation for Long Video Understanding | [Paper](https://arxiv.org/abs/2503.09149) |  |  |  |
| video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model | [Paper](https://arxiv.org/abs/2502.11775) | [GitHub](https://github.com/BriansIDP/video-SALMONN-o1) |  |  |
| Unhackable Temporal Rewarding for Scalable Video MLLMs | [Paper](https://arxiv.org/abs/2502.12081) |  |  |  |
| Temporal Preference Optimization for Long-Form Video Understanding | [Paper](https://arxiv.org/abs/2501.13919) |  |  |  |
| InternLM-XComposer2.5-Reward: A Simple Yet Effective Multi-Modal Reward Model | [Paper](https://arxiv.org/abs/2501.12368) | [GitHub](https://github.com/InternLM/InternLM-XComposer/tree/main/InternLM-XComposer-2.5-Reward) |  | ACL 2025 Findings |
| VidChain: Chain-of-Tasks with Metric-based Direct Preference Optimization for Dense Video Captioning | [Paper](https://arxiv.org/abs/2501.06761) |  |  |  |
| VideoSAVi: Self-Aligned Video Language Models without Human Supervision | [Paper](https://arxiv.org/abs/2412.00624) |  |  |  |
| Veason-R1: Reinforcing Video Reasoning Segmentation to Think Before It Segments | [Paper](https://arxiv.org/abs/2407.05513) |  |  |  |
| SAIL-VL2 Technical Report | [Paper]() |  |  |  |
| Factorized Learning for Temporally Grounded Video-Language Models | [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Zeng_Factorized_Learning_for_Temporally_Grounded_Video-Language_Models_ICCV_2025_paper.pdf) | [GitHub](https://github.com/nusnlp/d2vlm) | [Dataset](https://huggingface.co/datasets/wenzhengzeng/D2VLM-Dataset) | ICCV 2025 |

### Video-LMM SFT for Reasoning

| Title | Paper | Code | Dataset | Venue |
| :--- | :---: | :---: | :---: | :---: |
| Kwai Keye-VL 1.5 Technical Report | [Paper](https://arxiv.org/abs/2509.01563) |  |  |  |
| Strefer: Empowering Video LLMs with Space-Time Referring and Reasoning via Synthetic Instruction Data | [Paper](https://arxiv.org/abs/2509.03501) |  |  |  |
| Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding | [Paper](https://arxiv.org/abs/2508.20478) |  |  |  |
| Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding | [Paper](https://arxiv.org/abs/2508.20478) |  |  |  |
| Ovis2.5 Technical Report | [Paper](https://arxiv.org/abs/2508.11737) |  |  |  |
| ReasoningTrack: Chain-of-Thought Reasoning for Long-term Vision-Language Tracking | [Paper](https://arxiv.org/abs/2508.05221) |  |  |  |
| TAR-TVG: Enhancing VLMs with Timestamp Anchor-Constrained Reasoning for Temporal Video Grounding | [Paper](https://arxiv.org/abs/2508.07683) |  |  |  |
| Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning | [Paper](https://arxiv.org/abs/2508.04416) |  |  |  |
| ReasonAct: Progressive Training for Fine-Grained Video Reasoning in Small Models | [Paper](https://arxiv.org/abs/2508.01533) |  |  |  |
| ARC-Hunyuan-Video-7B: Structured Video Comprehension of Real-World Shorts | [Paper](https://arxiv.org/abs/2507.20939) |  |  |  |
| METER: Multi-modal Evidence-based Thinking and Explainable Reasoning -- Algorithm and Benchmark | [Paper](https://arxiv.org/abs/2507.16206) |  |  |  |
| CoTasks: Chain-of-Thought based Video Instruction Tuning Tasks | [Paper](https://arxiv.org/abs/2507.13609) |  |  |  |
| EmbRACE-3K: Embodied Reasoning and Action in Complex Environments | [Paper](https://arxiv.org/abs/2507.10548) |  |  |  |
| Scaling RL to Long Videos | [Paper](https://arxiv.org/abs/2507.07966) | [GitHub](https://github.com/NVLabs/Long-RL) | [Dataset](https://huggingface.co/datasets/LongVideo-Reason/longvideo-reason) | NeurIPS 2025 |
| Video Event Reasoning and Prediction by Fusing World Knowledge from LLMs with Vision Foundation Models | [Paper](https://arxiv.org/abs/2507.05822) |  |  |  |
| Kwai Keye-VL Technical Report | [Paper](https://arxiv.org/abs/2507.01949) | [GitHub](https://github.com/Kwai-Keye/Keye) |  |  |
| VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | [Paper](https://arxiv.org/abs/2506.17221) |  |  |  |
| Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video Reasoning | [Paper](https://arxiv.org/abs/2506.13654) | [GitHub](https://github.com/egolife-ai/Ego-R1) | [Dataset](https://huggingface.co/Ego-R1) |  |
| DAVID-XR1: Detecting AI-Generated Videos with Explainable Reasoning | [Paper](https://arxiv.org/abs/2506.14827) |  |  |  |
| VersaVid-R1: A Versatile Video Understanding and Reasoning Model from Question Answering to Captioning Tasks | [Paper](https://arxiv.org/abs/2506.09079) | [GitHub](https://github.com/VidBridge-R1/VidBridge-R1) | [Dataset](https://huggingface.co/datasets/VidBridge-R1/VidBridge-R1_training_data) |  |
| VidBridge-R1: Bridging QA and Captioning for RL-based Video Understanding Models with Intermediate Proxy Tasks | [Paper](https://arxiv.org/abs/2506.09079v2) |  |  |  |
| AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs | [Paper](https://arxiv.org/abs/2506.05328) | [GitHub](https://github.com/AV-Reasoner/AV-Reasoner) |  |  |
| Video-Skill-CoT: Skill-based Chain-of-Thoughts for Domain-Adaptive Video Reasoning | [Paper](https://arxiv.org/abs/2506.03525) | [GitHub](https://github.com/daeunni/Video-Skill-CoT) |  | EMNLP 2025 Findings |
| MiMo-VL Technical Report | [Paper](https://arxiv.org/abs/2506.03569) |  |  |  |
| Video-Skill-CoT: Skill-based Chain-of-Thoughts for Domain-Adaptive Video Reasoning | [Paper](https://arxiv.org/abs/2506.03525) |  |  |  |
| ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding | [Paper](https://arxiv.org/abs/2506.01300) | [GitHub](https://github.com/aiming-lab/ReAgent-V) |  | NeurIPS 2025 |
| Chain-of-Frames: Advancing Video Understanding in Multimodal LLMs via Frame-Aware Reasoning | [Paper](https://arxiv.org/abs/2506.00318) | [GitHub](https://github.com/SaraGhazanfari/CoF) |  |  |
| Universal Visuo-Tactile Video Understanding for Embodied Interaction | [Paper](https://arxiv.org/abs/2505.22566) |  |  |  |
| Fostering Video Reasoning via Next-Event Prediction | [Paper](https://arxiv.org/abs/2505.22457) | [GitHub](https://github.com/sail-sg/Video-Next-Event-Prediction) | [Dataset](https://huggingface.co/datasets/haonan3/V1-33K) |  |
| A2Seek: Towards Reasoning-Centric Benchmark for Aerial Anomaly Understanding | [Paper](https://arxiv.org/abs/2505.21962) |  |  |  |
| Vad-R1: Towards Video Anomaly Reasoning via Perception-to-Cognition Chain-of-Thought | [Paper](https://arxiv.org/abs/2505.19877) |  |  |  |
| Fact-R1: Towards Explainable Video Misinformation Detection with Deep Reasoning | [Paper](https://arxiv.org/abs/2505.16836) |  |  |  |
| From Evaluation to Defense: Advancing Safety in Video Large Language Models | [Paper](https://arxiv.org/abs/2505.16643) |  |  |  |
| Pixel Reasoner: Incentivizing Pixel-Space Reasoning with Curiosity-Driven Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.15966) |  |  |  |
| UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.14231) | [GitHub](https://github.com/AMAP-ML/UniVG-R1) | [Dataset](https://huggingface.co/datasets/GD-ML/UniVG-R1-data) |  |
| VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning | [Paper](https://arxiv.org/abs/2505.12434) | [GitHub](https://github.com/QiWang98/VideoRFT) | [Dataset](https://huggingface.co/datasets/QiWang98/VideoRFT-Data) | NeurIPS 2025 |
| Seed1.5-VL Technical Report | [Paper](https://arxiv.org/abs/2505.07062) |  |  |  |
| TEMPURA: Temporal Event Masked Prediction and Understanding for Reasoning in Action | [Paper](https://arxiv.org/abs/2505.01583) |  |  |  |
| VEU-Bench: Towards Comprehensive Understanding of Video Editing | [Paper](https://arxiv.org/abs/2504.17828) |  |  |  |
| Eagle 2.5: Boosting Long-Context Post-Training for Frontier Vision-Language Models | [Paper](https://arxiv.org/abs/2504.15271) |  |  |  |
| Compile Scene Graphs with Reinforcement Learning | [Paper](https://arxiv.org/abs/2504.13617) |  |  |  |
| Mavors: Multi-granularity Video Representation for Multimodal Large Language Model | [Paper](https://arxiv.org/abs/2504.10068) |  |  |  |
| LVC: A Lightweight Compression Framework for Enhancing VLMs in Long Video Understanding | [Paper](https://arxiv.org/abs/2504.06835) |  |  |  |
| From 128K to 4M: Efficient Training of Ultra-Long Context Large Language Models | [Paper](https://arxiv.org/abs/2504.06214) |  |  |  |
| Exploring the Effect of Reinforcement Learning on Video Understanding: Insights from SEED-Bench-R1 | [Paper](https://arxiv.org/abs/2503.24376) | [GitHub](https://github.com/TencentARC/SEED-Bench-R1) | [Dataset](https://huggingface.co/datasets/TencentARC/SEED-Bench-R1) |  |
| Video-R1: Reinforcing Video Reasoning in MLLMs | [Paper](https://arxiv.org/abs/2503.21776) | [GitHub](https://github.com/tulerfeng/Video-R1) | [Dataset](https://huggingface.co/datasets/Video-R1/Video-R1-data) |  |
| PAVE: Patching and Adapting Video Large Language Models | [Paper](https://arxiv.org/abs/2503.19794) |  |  |  |
| Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation | [Paper](https://arxiv.org/abs/2503.19622) | [GitHub](https://github.com/Hongcheng-Gao/HAVEN) | [Dataset](https://github.com/Hongcheng-Gao/HAVEN/blob/main/Data/test_data.json) |  |
| VideoMind: A Chain-of-LoRA Agent for Long Video Reasoning | [Paper](https://arxiv.org/abs/2503.13444) | [GitHub](https://github.com/yeliudev/VideoMind) | [Dataset](https://huggingface.co/datasets/yeliudev/VideoMind-Dataset/tree/main) |  |
| ST-Think: How Multimodal Large Language Models Reason About 4D Worlds from Ego-Centric Videos | [Paper](https://arxiv.org/abs/2503.12542) | [GitHub](https://github.com/WPR001/Ego-ST) |  |  |
| TIME: Temporal-sensitive Multi-dimensional Instruction Tuning and Benchmarking for Video-LLMs | [Paper](https://arxiv.org/abs/2503.09994) |  |  |  |
| Memory-enhanced Retrieval Augmentation for Long Video Understanding | [Paper](https://arxiv.org/abs/2503.09149) |  |  |  |
| Token-Efficient Long Video Understanding for Multimodal LLMs | [Paper](https://arxiv.org/abs/2503.04130) |  |  |  |
| M-LLM Based Video Frame Selection for Efficient Video Understanding | [Paper](https://arxiv.org/abs/2502.19680) |  |  |  |
| video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model | [Paper](https://arxiv.org/abs/2502.11775) | [GitHub](https://github.com/BriansIDP/video-SALMONN-o1) |  |  |
| Unhackable Temporal Rewarding for Scalable Video MLLMs | [Paper](https://arxiv.org/abs/2502.12081) |  |  |  |
| Long-VITA: Scaling Large Multi-modal Models to 1 Million Tokens with Leading Short-Context Accuray | [Paper](https://arxiv.org/abs/2502.05177) |  |  |  |
| InternLM-XComposer2.5-Reward: A Simple Yet Effective Multi-Modal Reward Model | [Paper](https://arxiv.org/abs/2501.12368) | [GitHub](https://github.com/InternLM/InternLM-XComposer/tree/main/InternLM-XComposer-2.5-Reward) |  | ACL 2025 Findings |
| Omni-RGPT: Unifying Image and Video Region-level Understanding via Token Marks | [Paper](https://arxiv.org/abs/2501.08326) |  |  |  |
| LongViTU: Instruction Tuning for Long-Form Video Understanding | [Paper](https://arxiv.org/abs/2501.05037) |  |  |  |
| VideoRefer Suite: Advancing Spatial-Temporal Object Understanding with Video LLM | [Paper](https://arxiv.org/abs/2501.00599) |  |  |  |
| Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces | [Paper](https://arxiv.org/abs/2412.14171) |  |  |  |
| Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling | [Paper](https://arxiv.org/abs/2412.05271) | [GitHub](https://github.com/OpenGVLab/InternVL) |  |  |
| STEP: Enhancing Video-LLMs' Compositional Reasoning by Spatio-Temporal Graph-guided Self-Training | [Paper](https://arxiv.org/abs/2412.00161) |  |  |  |
| ReVisionLLM: Recursive Vision-Language Model for Temporal Grounding in Hour-Long Videos | [Paper](https://arxiv.org/abs/2411.14901) | [GitHub](https://github.com/Tanveer81/ReVisionLLM) |  | CVPR 2025 |
| VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection | [Paper](https://arxiv.org/abs/2411.14794) | [GitHub](https://github.com/hshjerry/VideoEspresso) | [Dataset](https://huggingface.co/datasets/hshjerry0315/VideoEspresso_train_video/tree/main) |  |
| Veason-R1: Reinforcing Video Reasoning Segmentation to Think Before It Segments | [Paper](https://arxiv.org/abs/2407.05513) |  |  |  |
| SAIL-VL2 Technical Report | [Paper]() |  |  |  |

### Test-Time Scaling in Video Reasoning

| Title | Paper | Code | Dataset | Venue |
| :--- | :---: | :---: | :---: | :---: |
| VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception | [Paper](https://arxiv.org/abs/2509.21100) |  |  |  |
| Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding | [Paper](https://arxiv.org/abs/2508.20478) |  |  |  |
| Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding | [Paper](https://arxiv.org/abs/2508.20478) |  |  |  |
| Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning | [Paper](https://arxiv.org/abs/2508.04416) |  |  |  |
| VideoForest: Person-Anchored Hierarchical Reasoning for Cross-Video Question Answering | [Paper](https://arxiv.org/abs/2508.03039) |  |  |  |
| Free-MoRef: Instantly Multiplexing Context Perception Capabilities of Video-MLLMs within Single Inference | [Paper](https://arxiv.org/abs/2508.02134) |  |  |  |
| ReasonAct: Progressive Training for Fine-Grained Video Reasoning in Small Models | [Paper](https://arxiv.org/abs/2508.01533) |  |  |  |
| EgoPrune: Efficient Token Pruning for Egomotion Video Reasoning in Embodied Agent | [Paper](https://arxiv.org/abs/2507.15428) |  |  |  |
| Towards Video Thinking Test: A Holistic Benchmark for Advanced Video Reasoning and Understanding | [Paper](https://arxiv.org/abs/2507.15028) |  |  |  |
| ViTCoT: Video-Text Interleaved Chain-of-Thought for Boosting Video Understanding in Large Language Models | [Paper](https://arxiv.org/abs/2507.09876) |  |  |  |
| Video-RTS: Rethinking Reinforcement Learning and Test-Time Scaling for Efficient and Enhanced Video Reasoning | [Paper](https://arxiv.org/abs/2507.06485) | [GitHub](https://github.com/Ziyang412/Video-RTS) |  | EMNLP 2025 |
| StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | [Paper](https://arxiv.org/abs/2507.05240) |  |  |  |
| VRAgent-R1: Boosting Video Recommendation with MLLM-based Agents via Reinforcement Learning | [Paper](https://arxiv.org/abs/2507.02626) |  |  |  |
| Temporal Chain of Thought: Long-Video Understanding by Thinking in Frames | [Paper](https://arxiv.org/abs/2507.02001) |  |  |  |
| Temporal Chain of Thought: Long-Video Understanding by Thinking in Frames | [Paper](https://arxiv.org/abs/2507.02001) |  |  |  |
| DIVE: Deep-search Iterative Video Exploration A Technical Report for the CVRR Challenge at CVPR 2025 | [Paper](https://arxiv.org/abs/2506.21891) | [GitHub](https://github.com/PanasonicConnect/DIVE) |  |  |
| How Far Can Off-the-Shelf Multimodal Large Language Models Go in Online Episodic Memory Question Answering? | [Paper](https://arxiv.org/abs/2506.16450) |  |  |  |
| Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video Reasoning | [Paper](https://arxiv.org/abs/2506.13654) | [GitHub](https://github.com/egolife-ai/Ego-R1) | [Dataset](https://huggingface.co/Ego-R1) |  |
| VideoDeepResearch: Long Video Understanding With Agentic Tool Using | [Paper](https://arxiv.org/abs/2506.10821) |  |  |  |
| CogStream: Context-guided Streaming Video Question Answering | [Paper](https://arxiv.org/abs/2506.10516) | [GitHub](https://github.com/LiamZhao326/CogStream) | [Dataset](https://zenodo.org/records/15870909?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImZiYmFlODkxLWUwZTUtNGUyMi04NzU0LWVhYTUxZWM3MzNhMiIsImRhdGEiOnt9LCJyYW5kb20iOiI3MWI5MzIwZDU3MDA1OWExMTBlZWQ5NTE2OTUzZTA5NSJ9.ITwHqhbk7cUcd4f9qHpIx972Jgfdis5qiMJwNXyo5vT7-Ltd-dvGQLD7yItrKmJPJI8oUCLb8ItODsrm7_t6NA) |  |
| Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency | [Paper](https://arxiv.org/abs/2506.08343) |  |  |  |
| Video-CoT: A Comprehensive Dataset for Spatiotemporal Understanding of Videos Based on Chain-of-Thought | [Paper](https://arxiv.org/abs/2506.08817) |  |  |  |
| CyberV: Cybernetics for Test-time Scaling in Video Understanding | [Paper](https://arxiv.org/abs/2506.07971) |  |  |  |
| Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs | [Paper](https://arxiv.org/abs/2506.07180) |  |  |  |
| VideoChat-A1: Thinking with Long Videos by Chain-of-Shot Reasoning | [Paper](https://arxiv.org/abs/2506.06097) |  |  |  |
| MiMo-VL Technical Report | [Paper](https://arxiv.org/abs/2506.03569) |  |  |  |
| Video-Skill-CoT: Skill-based Chain-of-Thoughts for Domain-Adaptive Video Reasoning | [Paper](https://arxiv.org/abs/2506.03525) |  |  |  |
| ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding | [Paper](https://arxiv.org/abs/2506.01300) | [GitHub](https://github.com/aiming-lab/ReAgent-V) |  | NeurIPS 2025 |
| ReFoCUS: Reinforcement-guided Frame Optimization for Contextual Understanding | [Paper](https://arxiv.org/abs/2506.01274) |  |  |  |
| SiLVR: A Simple Language-based Video Reasoning Framework | [Paper](https://arxiv.org/abs/2505.24869) | [GitHub](https://github.com/CeeZh/SILVR) |  |  |
| Multi-RAG: A Multimodal Retrieval-Augmented Generation System for Adaptive Video Understanding | [Paper](https://arxiv.org/abs/2505.23990) |  |  |  |
| VideoReasonBench: Can MLLMs Perform Vision-Centric Complex Video Reasoning? | [Paper](https://arxiv.org/abs/2505.23359) | [GitHub](https://github.com/llyx97/video_reason_bench) | [Dataset](https://huggingface.co/datasets/lyx97/reasoning_videos) |  |
| Omni-R1: Reinforcement Learning for Omnimodal Reasoning via Two-System Collaboration | [Paper](https://arxiv.org/abs/2505.20256) | [GitHub](https://github.com/aim-uofa/Omni-R1) |  |  |
| Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding | [Paper](https://arxiv.org/abs/2505.18079) |  |  |  |
| Pixel Reasoner: Incentivizing Pixel-Space Reasoning with Curiosity-Driven Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.15966) |  |  |  |
| ViQAgent: Zero-Shot Video Question Answering via Agent with Open-Vocabulary Grounding Validation | [Paper](https://arxiv.org/abs/2505.15928) |  |  |  |
| ViaRL: Adaptive Temporal Grounding via Visual Iterated Amplification Reinforcement Learning | [Paper](https://arxiv.org/abs/2505.15447) | [GitHub](https://github.com/xuzq23/ViaRL) |  |  |
| RVTBench: A Benchmark for Visual Reasoning Tasks | [Paper](https://arxiv.org/abs/2505.11838) | [GitHub](https://github.com/yiqings/rvt) | [Dataset](https://huggingface.co/datasets/yiqingshen/rvtbench/tree/main/rvtbench) |  |
| CoT-Vid: Dynamic Chain-of-Thought Routing with Self Verification for Training-Free Video Reasoning | [Paper](https://arxiv.org/abs/2505.11830) |  |  |  |
| VCRBench: Exploring Long-form Causal Reasoning Capabilities of Large Video Language Models | [Paper](https://arxiv.org/abs/2505.08455) |  |  |  |
| Seed1.5-VL Technical Report | [Paper](https://arxiv.org/abs/2505.07062) |  |  |  |
| Empowering Agentic Video Analytics Systems with Video Language Models | [Paper](https://arxiv.org/abs/2505.00254) |  |  |  |
| Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering | [Paper](https://openreview.net/forum?id=yTpn3QY9Ff) |  |  |  |
| SeriesBench: A Benchmark for Narrative-Driven Drama Series Understanding | [Paper](https://arxiv.org/abs/2504.21435) | [GitHub](https://github.com/zackhxn/SeriesBench-CVPR2025) |  | CVPR 2025 |
| VideoMultiAgents: A Multi-Agent Framework for Video Question Answering | [Paper](https://arxiv.org/abs/2504.20091) |  |  |  |
| MR. Video: "MapReduce" is the Principle for Long Video Understanding | [Paper](https://arxiv.org/abs/2504.16082) |  |  |  |
| Multimodal Long Video Modeling Based on Temporal Dynamic Context | [Paper](https://arxiv.org/abs/2504.10443) | [GitHub](https://github.com/t-montes/viqagent) |  |  |
| VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT | [Paper](https://arxiv.org/abs/2504.04471) |  |  |  |
| WikiVideo: Article Generation from Multiple Videos | [Paper](https://arxiv.org/abs/2504.00939) |  |  |  |
| Aurelia: Test-time Reasoning Distillation in Audio-Visual LLMs | [Paper](https://arxiv.org/abs/2503.23219) |  |  |  |
| From Trial to Triumph: Advancing Long Video Understanding via Visual Context Sample Scaling and Self-reward Alignment | [Paper](https://arxiv.org/abs/2503.20472) |  |  |  |
| Agentic Keyframe Search for Video Question Answering | [Paper](https://arxiv.org/abs/2503.16032) |  |  |  |
| VideoMind: A Chain-of-LoRA Agent for Long Video Reasoning | [Paper](https://arxiv.org/abs/2503.13444) | [GitHub](https://github.com/yeliudev/VideoMind) | [Dataset](https://huggingface.co/datasets/yeliudev/VideoMind-Dataset/tree/main) |  |
| Does Your Vision-Language Model Get Lost in the Long Video Sampling Dilemma? | [Paper](https://arxiv.org/abs/2503.12496) |  |  |  |
| Memory-enhanced Retrieval Augmentation for Long Video Understanding | [Paper](https://arxiv.org/abs/2503.09149) |  |  |  |
| Everything Can Be Described in Words: A Simple Unified Multi-Modal Framework with Semantic and Temporal Alignment | [Paper](https://arxiv.org/abs/2503.09081) |  |  |  |
| QuoTA: Query-oriented Token Assignment via CoT Query Decouple for Long Video Comprehension | [Paper](https://arxiv.org/abs/2503.08689) | [GitHub](https://github.com/MAC-AutoML/QuoTA) |  |  |
| Token-Efficient Long Video Understanding for Multimodal LLMs | [Paper](https://arxiv.org/abs/2503.04130) |  |  |  |
| M-LLM Based Video Frame Selection for Efficient Video Understanding | [Paper](https://arxiv.org/abs/2502.19680) |  |  |  |
| TheoremExplainAgent: Towards Multimodal Explanations for LLM Theorem Understanding | [Paper](https://arxiv.org/abs/2502.19400) | [GitHub](https://github.com/TIGER-AI-Lab/TheoremExplainAgent) | [Dataset](https://huggingface.co/datasets/TIGER-Lab/TheoremExplainBench) | ACL 2025 main |
| CoS: Chain-of-Shot Prompting for Long Video Understanding | [Paper](https://arxiv.org/abs/2502.06428) |  |  |  |
| Long-VITA: Scaling Large Multi-modal Models to 1 Million Tokens with Leading Short-Context Accuray | [Paper](https://arxiv.org/abs/2502.05177) |  |  |  |
| Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge | [Paper](https://arxiv.org/abs/2501.13468) | [GitHub](https://github.com/hmxiong/StreamChat) |  | ICLR2025 |
| InternLM-XComposer2.5-Reward: A Simple Yet Effective Multi-Modal Reward Model | [Paper](https://arxiv.org/abs/2501.12368) | [GitHub](https://github.com/InternLM/InternLM-XComposer/tree/main/InternLM-XComposer-2.5-Reward) |  | ACL 2025 Findings |
| MECD+: Unlocking Event-Level Causal Graph Discovery for Video Reasoning | [Paper](https://arxiv.org/abs/2501.07227) |  |  |  |
| VidChain: Chain-of-Tasks with Metric-based Direct Preference Optimization for Dense Video Captioning | [Paper](https://arxiv.org/abs/2501.06761) |  |  |  |
| Building a Mind Palace: Structuring Environment-Grounded Semantic Graphs for Effective Long Video Analysis with LLMs | [Paper](https://arxiv.org/abs/2501.04336) |  |  |  |
| Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding | [Paper](https://arxiv.org/abs/2501.00358) |  |  |  |
| PruneVid: Visual Token Pruning for Efficient Video Large Language Models | [Paper](https://arxiv.org/abs/2412.16117) |  |  |  |
| Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces | [Paper](https://arxiv.org/abs/2412.14171) |  |  |  |
| VCA: Video Curious Agent for Long Video Understanding | [Paper](https://arxiv.org/abs/2412.10471) |  |  |  |
| Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling | [Paper](https://arxiv.org/abs/2412.05271) | [GitHub](https://github.com/OpenGVLab/InternVL) |  |  |
| VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding | [Paper](https://arxiv.org/abs/2412.03735) |  |  |  |
| VideoICL: Confidence-based Iterative In-context Learning for Out-of-Distribution Video Understanding | [Paper](https://arxiv.org/abs/2412.02186) |  |  |  |
| ReVisionLLM: Recursive Vision-Language Model for Temporal Grounding in Hour-Long Videos | [Paper](https://arxiv.org/abs/2411.14901) | [GitHub](https://github.com/Tanveer81/ReVisionLLM) |  | CVPR 2025 |
| VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection | [Paper](https://arxiv.org/abs/2411.14794) | [GitHub](https://github.com/hshjerry/VideoEspresso) | [Dataset](https://huggingface.co/datasets/hshjerry0315/VideoEspresso_train_video/tree/main) |  |
| Adaptive Video Understanding Agent: Enhancing efficiency with dynamic frame sampling and feedback-driven reasoning | [Paper](https://arxiv.org/abs/2410.20252) |  |  |  |
| VideoINSTA: Zero-shot Long Video Understanding via Informative Spatial-Temporal Reasoning with LLMs | [Paper](https://arxiv.org/abs/2409.20365) |  |  |  |
| MECD: Unlocking Multi-Event Causal Discovery in Video Reasoning | [Paper](https://arxiv.org/abs/2409.17647) | [GitHub](https://github.com/tychen-SJTU/MECD-Benchmark) | [Dataset](https://huggingface.co/datasets/tychen-sjtu/MECD) | NeurIPS 2024 (Spotlight) |
| Video-of-Thought: Step-by-Step Video Reasoning from Perception to Cognition | [Paper](https://arxiv.org/abs/2501.03230) | [GitHub](https://github.com/scofield7419/Video-of-Thought) |  | ICML 2024 Oral |

### Benchmarks for Video Reasoning

| Title | Paper | Code | Dataset | Venue |
| :--- | :---: | :---: | :---: | :---: |
| Scaling RL to Long Videos | [Paper](https://arxiv.org/abs/2507.07966) | [GitHub](https://github.com/NVLabs/Long-RL) | [Dataset](https://huggingface.co/datasets/LongVideo-Reason/longvideo-reason) | NeurIPS 2025 |
| AdsQA: Towards Advertisement Video Understanding | [Paper](https://arxiv.org/abs/2509.08621) |  |  |  |
| CVBench: Evaluating Cross-Video Synergies for Complex Multimodal Understanding and Reasoning | [Paper](https://arxiv.org/abs/2508.19542) |  |  |  |
| ReasoningTrack: Chain-of-Thought Reasoning for Long-term Vision-Language Tracking | [Paper](https://arxiv.org/abs/2508.05221) |  |  |  |
| METER: Multi-modal Evidence-based Thinking and Explainable Reasoning -- Algorithm and Benchmark | [Paper](https://arxiv.org/abs/2507.16206) |  |  |  |
| Towards Video Thinking Test: A Holistic Benchmark for Advanced Video Reasoning and Understanding | [Paper](https://arxiv.org/abs/2507.15028) |  |  |  |
| ImplicitQA: Going beyond frames towards Implicit Video Reasoning | [Paper](https://arxiv.org/abs/2506.21742) |  | [Dataset](https://huggingface.co/datasets/ucf-crcv/ImplicitQA) |  |
| Video-CoT: A Comprehensive Dataset for Spatiotemporal Understanding of Videos Based on Chain-of-Thought | [Paper](https://arxiv.org/abs/2506.08817) |  |  |  |
| Looking Beyond Visible Cues: Implicit Video Question Answering via Dual-Clue Reasoning | [Paper](https://arxiv.org/abs/2506.07811) | [GitHub](https://github.com/tychen-SJTU/Implicit-VideoQA) |  |  |
| MORSE-500: A Programmatically Controllable Video Benchmark to Stress-Test Multimodal Reasoning | [Paper](https://arxiv.org/abs/2506.05523) | [GitHub](https://github.com/morse-benchmark/morse-500) | [Dataset](https://huggingface.co/datasets/video-reasoning/morse-500) |  |
| Time Blindness: Why Video-Language Models Can't See What Humans Can? | [Paper](https://arxiv.org/abs/2505.24867) |  |  |  |
| ScaleLong: A Multi-Timescale Benchmark for Long Video Understanding | [Paper](https://arxiv.org/abs/2505.23922) |  |  |  |
| VidText: Towards Comprehensive Evaluation for Video Text Understanding | [Paper](https://arxiv.org/abs/2505.22810) | [GitHub](https://github.com/shuyansy/VidText) | [Dataset](https://huggingface.co/datasets/sy1998/VidText) |  |
| Video-Holmes: Can MLLM Think Like Holmes for Complex Video Reasoning? | [Paper](https://arxiv.org/abs/2505.21374) | [GitHub](https://github.com/TencentARC/Video-Holmes) |  |  |
| From Evaluation to Defense: Advancing Safety in Video Large Language Models | [Paper](https://arxiv.org/abs/2505.16643) |  |  |  |
| VideoEval-Pro: Robust and Realistic Long Video Understanding Evaluation | [Paper](https://arxiv.org/abs/2505.14640) |  |  |  |
| Breaking Down Video LLM Benchmarks: Knowledge, Spatial Perception, or True Temporal Understanding? | [Paper](https://arxiv.org/abs/2505.14321) |  |  |  |
| RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning through Real-Time Video | [Paper](https://arxiv.org/abs/2505.02064) |[GitHub](https://github.com/LJungang/RTV-Bench)  | [Dataset](https://huggingface.co/datasets/RTVBench/RTV-Bench) | NeurIPS 2025 |
| MINERVA: Evaluating Complex Video Reasoning | [Paper](https://arxiv.org/abs/2505.00681) | [GitHub](https://github.com/google-deepmind/neptune?tab=readme-ov-file#minerva) |  |  |
| VCR-Bench: A Comprehensive Evaluation Framework for Video Chain-of-Thought Reasoning | [Paper](https://arxiv.org/abs/2504.07956) | [GitHub](https://github.com/zhishuifeiqian/VCR-Bench) | [Dataset](https://huggingface.co/datasets/VLM-Reasoning/VCR-Bench) |  |
| Exploring the Effect of Reinforcement Learning on Video Understanding: Insights from SEED-Bench-R1 | [Paper](https://arxiv.org/abs/2503.24376) | [GitHub](https://github.com/TencentARC/SEED-Bench-R1) | [Dataset](https://huggingface.co/datasets/TencentARC/SEED-Bench-R1) |  |
| H2VU-Benchmark: A Comprehensive Benchmark for Hierarchical Holistic Video Understanding | [Paper](https://arxiv.org/abs/2503.24008) |  |  |  |
| OmniMMI: A Comprehensive Multi-modal Interaction Benchmark in Streaming Video Contexts | [Paper](https://arxiv.org/abs/2503.22952) | [Github](https://github.com/OmniMMI/OmniMMI) | [Dataset](https://huggingface.co/datasets/ColorfulAI/OmniMMI) | CVPR 2025  |
| Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation | [Paper](https://arxiv.org/abs/2503.19622) | [GitHub](https://github.com/Hongcheng-Gao/HAVEN) | [Dataset](https://github.com/Hongcheng-Gao/HAVEN/blob/main/Data/test_data.json) |  |
| V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning | [Paper](https://arxiv.org/abs/2503.11495) | [GitHub](https://github.com/V-STaR-Bench/V-STaR) | [Dataset](https://huggingface.co/datasets/V-STaR-Bench/V-STaR) |  |
| Reasoning is All You Need for Video Generalization: A Counterfactual Benchmark with Sub-question Evaluation | [Paper](https://arxiv.org/abs/2503.10691) |  |  |  |
| Towards Fine-Grained Video Question Answering | [Paper](https://arxiv.org/abs/2503.06820) |  |  |  |
| SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding | [Paper](https://arxiv.org/abs/2502.10810) |  |  |  |
| MMVU: Measuring Expert-Level Multi-Discipline Video Understanding | [Paper](https://arxiv.org/abs/2501.12380) | [GitHub](https://github.com/yale-nlp/MMVU) | [Dataset](https://huggingface.co/datasets/yale-nlp/MMVU) |  |
| OVO-Bench: How Far is Your Video-LLMs from Real-World Online Video Understanding? | [Paper](https://arxiv.org/abs/2501.05510) | [GitHub](https://github.com/JoeLeelyf/OVO-Bench) | [Dataset](https://huggingface.co/datasets/JoeLeelyf/OVO-Bench) |  |
| HLV-1K: A Large-scale Hour-Long Video Benchmark for Time-Specific Long Video Understanding | [Paper](https://arxiv.org/abs/2501.01645) |  |  |  |
| Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces | [Paper](https://arxiv.org/abs/2412.14171) |  |  |  |
| 3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark | [Paper](https://arxiv.org/abs/2412.07825) |  |  |  |
| Black Swan: Abductive and Defeasible Video Reasoning in Unpredictable Events | [Paper](https://arxiv.org/abs/2412.05725) | [GitHub](https://github.com/sahithyaravi/BlackSwan) | [Dataset](https://huggingface.co/collections/UBC-ViL/black-swan-abductive-and-defeasible-reasoning-67de1a4ab7ddc22edf0b0542) | CVPR 2025 |
| VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding | [Paper](https://arxiv.org/abs/2412.03735) |  |  |  |
| TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models | [Paper](https://arxiv.org/abs/2410.23266) |  |  |  |
| TemporalBench: Benchmarking Fine-grained Temporal Understanding for Multimodal Video Models | [Paper](https://arxiv.org/abs/2410.10818) |  |  |  |
| On the Consistency of Video Large Language Models in Temporal Comprehension | [Paper](https://arxiv.org/abs/2411.12951) | [Github](https://github.com/minjoong507/Consistency-of-Video-LLM) | [Dataset](https://huggingface.co/datasets/mjjung/Consistency-Evaluation-for-Video-LLMs) | CVPR 2025 |
| EgoExo-Con: Exploring View-Invariant Video Temporal Understanding | [Paper](https://arxiv.org/abs/2510.26113) | | | |

### Related Surveys

| Title | Paper | Code | Dataset | Venue |
| :--- | :---: | :---: | :---: | :---: |
| Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models | [Paper](https://arxiv.org/abs/2505.04921) | [GitHub](https://github.com/HITsz-TMG/Awesome-Large-Multimodal-Reasoning-Models) |  |  |
| VideoLLM Benchmarks and Evaluation: A Survey | [Paper](https://arxiv.org/abs/2505.03829) |  |  |  |
| Reinforced MLLM: A Survey on RL-Based Reasoning in Multimodal Large Language Models | [Paper](https://arxiv.org/abs/2504.21277) |  |  |  |
| Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey | [Paper](https://arxiv.org/abs/2503.12605) |  |  |  |
| From Seconds to Hours: Reviewing MultiModal Large Language Models on Comprehensive Long Video Understanding | [Paper](https://arxiv.org/abs/2409.18938) |  |  |  |
| From Seconds to Hours: Reviewing MultiModal Large Language Models on Comprehensive Long Video Understanding | [Paper](https://arxiv.org/abs/2409.18938) |  |  |  |
| Video Understanding with Large Language Models: A Survey | [Paper](https://arxiv.org/abs/2312.17322) |  |  |  |




## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yoloytang/Awesome-Video-LMM-Post-Training&type=Date)](https://star-history.com/#yoloytang/Awesome-Video-LMM-Post-Training&Date)


