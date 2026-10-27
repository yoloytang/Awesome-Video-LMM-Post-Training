import json
from collections import defaultdict

# Define the categories and their corresponding tags in the desired output order.
ORDERED_CATEGORIES = [
    ("### Reinforced Video-LMMs", "RL"),
    ("### Video-LMM SFT for Reasoning", "SFT"),
    ("### Test-Time Scaling in Video Reasoning", "TTS"),
    ("### Benchmarks for Video Reasoning", "Benchmark"),
    ("### Related Surveys", "Survey")
]

# README header and introduction
README_HEADER = """# Awesome-Video-LMM-Post-Training[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models

> *[Yolo Y. Tang](https://yoloytang.me/)<sup>1</sup>, [Jing Bi](https://jing.vision/)<sup>1</sup>, [Pinxin Liu](https://andypinxinliu.github.io/)<sup>1</sup>, [Zhenyu Pan](https://pzyseere.github.io/)<sup>2</sup>, [Zhangyun Tan](https://zhangyun04.github.io/)<sup>1</sup>, [Qianxiang Shen](https://github.com/chrisqarrowx)<sup>1</sup>, [Jiani Liu](https://openreview.net/profile?id=%7EJiani_Liu5)<sup>1</sup>, [Hang Hua](https://hanghuacs.notion.site/)<sup>1</sup>, [Junjia Guo](https://www.linkedin.com/in/junjia-guo-b3a9b5336/)<sup>1</sup>, [Yunzhong Xiao](https://scholar.google.com/citations?user=b9uTwEgAAAAJ&hl=en)<sup>3</sup>, [Chao Huang](https://wikichao.github.io/)<sup>1</sup>, [Zhiyuan Wang](https://scholar.google.com/citations?user=4TdiRMYAAAAJ&hl=en)<sup>4</sup>, [Susan Liang](https://liangsusan-git.github.io/)<sup>1</sup>, [Xinyi Liu](https://xinyiliu0227.github.io/)<sup>1</sup>, [Yizhi Song](https://song630.github.io/yizhisong.github.io/)<sup>5</sup>, [Yuhe Nie](https://scholar.google.com/citations?user=6Rlva_8AAAAJ&hl=en)<sup>6</sup>, [Jia-Xing Zhong](https://scholar.google.com/citations?hl=en&user=dIckm98AAAAJ)<sup>7</sup>, [Bozheng Li](https://openreview.net/profile?id=~Bozheng_Li1)<sup>8</sup>, [Daiqing Qi](https://daiqing-qi.github.io/me/index.html)<sup>9</sup>, [Ziyun Zeng](https://scholar.google.com/citations?user=b2DIlscAAAAJ)<sup>1</sup>, [Ali Vosoughi](https://alivosoughi.com/)<sup>1</sup>, [Luchuan Song](https://songluchuan.github.io/)<sup>1</sup>, [Zeliang Zhang](https://zhangaipi.github.io/)<sup>1</sup>, [Daiki Shimada](https://scholar.google.com/citations?user=1uAwouQAAAAJ&hl=en)<sup>10</sup>, [Han Liu](https://magics.cs.northwestern.edu/people.html)<sup>2</sup>, [Jiebo Luo](https://www.cs.rochester.edu/u/jluo/)<sup>1</sup>, [Chenliang Xu](https://www.cs.rochester.edu/u/cxu22/)<sup>1</sup>*

> *<sup>1</sup>University of Rochester, <sup>2</sup>Northwestern University, <sup>3</sup>CMU, <sup>4</sup>UCSB, <sup>5</sup>Purdue University, <sup>6</sup>NYU, <sup>7</sup>University of Oxford, <sup>8</sup>Brown University, <sup>9</sup>University of Virginia, <sup>10</sup>Sony Group Corporation*

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
  author={Yolo Y. Tang, Jing Bi, Pinxin Liu, Zhenyu Pan, Zhangyun Tan, Qianxiang Shen, Jiani Liu, Hang Hua, Junjia Guo, Yunzhong Xiao, Chao Huang, Zhiyuan Wang, Susan Liang, Xinyi Liu, Yizhi Song, Yuhe Nie, Jia-Xing Zhong, Bozheng Li, Daiqing Qi, Ziyun Zeng, Ali Vosoughi, Luchuan Song, Zeliang Zhang, Daiki Shimada, Han Liu, Jiebo Luo, Chenliang Xu},
  journal={arXiv preprint arXiv:2510.05034},
  year={2025}
```

## Latest Research in Video-LMMs Post-Training
"""

# README footer
README_FOOTER = """


## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yoloytang/Awesome-Video-LMM-Post-Training&type=Date)](https://star-history.com/#yoloytang/Awesome-Video-LMM-Post-Training&Date)


"""

def generate_markdown_table(papers):
    """Generates a Markdown table for a list of papers."""
    lines = []
    # Add table header
    lines.append("| Title | Paper | Code | Dataset | Venue |")
    lines.append("| :--- | :---: | :---: | :---: | :---: |")
    
    # Add a row for each paper
    for paper in papers:
        # Sanitize title to prevent breaking table format if it contains '|'
        title = paper.get('title', 'N/A').replace('|', '\\|')
        paper_link = paper.get('link', '#')
        
        # Get code link (if exists)
        code_link = paper.get('code', '')
        code_cell = f"[GitHub]({code_link})" if code_link else ""
        
        # Get dataset link (if exists)
        dataset_link = paper.get('dataset', '')
        dataset_cell = f"[Dataset]({dataset_link})" if dataset_link else ""
        
        # Get venue info
        venue = paper.get('venue', '')
        
        # Format the row
        row = f"| {title} | [Paper]({paper_link}) | {code_cell} | {dataset_cell} | {venue} |"
        lines.append(row)
        
    return "\n".join(lines)

def main(json_file_path, output_md_path):
    """
    Reads paper data from a JSON file, categorizes and sorts the papers,
    and then generates a Markdown file with the results.
    """
    # 1. Read and parse the JSON file from the given path.
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            all_papers = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found. Please make sure it exists.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from the file '{json_file_path}'.")
        return

    # 2. Categorize papers based on their tags.
    categorized_papers = defaultdict(list)
    for paper in all_papers:
        for tag in paper.get('tags', []):
            categorized_papers[tag].append(paper)

    # 3. Sort papers within each category by release date (newest first).
    for tag in categorized_papers:
        # Use a default date string for papers that might be missing the 'released' key.
        categorized_papers[tag].sort(key=lambda p: p.get('released', '1970-01-01T00:00:00'), reverse=True)

    # 4. Generate the final Markdown content.
    markdown_output_parts = [README_HEADER]
    
    for header, tag_key in ORDERED_CATEGORIES:
        markdown_output_parts.append(header)
        markdown_output_parts.append("") # Add a blank line after the header
        
        papers_in_category = categorized_papers.get(tag_key, [])
        if papers_in_category:
            table_md = generate_markdown_table(papers_in_category)
            markdown_output_parts.append(table_md)
        else:
            # Add a placeholder if no papers are found for a category.
            markdown_output_parts.append("*No papers in this category yet.*")
        
        # Add extra spacing between sections for better readability.
        markdown_output_parts.append("")

    # Add the footer
    markdown_output_parts.append(README_FOOTER)

    # 5. Write the generated content to the output Markdown file.
    try:
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(markdown_output_parts))
        print(f"Successfully generated Markdown file at '{output_md_path}'")
    except IOError as e:
        print(f"Error writing to file '{output_md_path}': {e}")

if __name__ == '__main__':
    # This script depends on an existing 'papers.json' file in the same directory.
    input_json_filename = 'awesome_papers.json'
    output_md_filename = 'README.md'
    
    # Run the main function.
    main(input_json_filename, output_md_filename)
