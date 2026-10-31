# AI-BinderDesign

Benchmark-calibrated de novo protein binder design and structural evaluation.

[中文说明](#中文说明)

## Research scope

This project includes EGFR binder-design materials, EGFR human/mouse structural controls, TNF control benchmarking, shared analysis scripts, and the original 28-slide report. EGFR and TNF datasets are kept separate. The folder name `EFGR` is preserved as supplied in source paths; it denotes the EGFR project.

## Results and evidence limits

The archived work evaluates structural prediction and confidence metrics against selected positive and negative controls. Computational confidence and interface metrics do not establish experimental binding affinity. Each summary table must be interpreted with its included species, model, target construct, and control labels. This repository preserves the source results and does not claim a new scientific rerun.

## Contents

- `EGFR_binder_design/`: source inputs, prediction controls, structures, and analyses.
- `TNF_benchmark/`: TNF control prediction and analyses.
- `scripts/`: analysis and summary-building scripts.
- `results/benchmark_summaries/`: source summary tables.
- `docs/AI-BinderDesign.pptx`: original project report.
- Large original prediction outputs will be attached as versioned GitHub Releases with per-file SHA-256 manifests.

## Reproduction status

Historical commands, software versions, and missing details are recorded alongside the relevant source material. No complete clean-room rerun is claimed. See file provenance and release manifests before interpreting or restoring data.

## 中文说明

本项目包含 EGFR 结合剂设计、EGFR 人/鼠结构对照、TNF 对照基准测试、分析脚本和原始 28 页报告。EGFR 与 TNF 数据分开保存。原始目录名 `EFGR` 按来源保留，指 EGFR 项目。

项目使用选定阳性与阴性对照评估结构预测和置信度指标。计算置信度及界面指标不能证明实验亲和力。应结合每张表中的物种、模型、靶标构建体和对照标签解读。本仓库保存既有结果，不表示重新运行了科学计算。

大型原始预测产物将作为带版本的 GitHub Release 附件，并提供逐文件 SHA-256 清单。历史命令、软件版本和缺失信息以实际留存材料为准，不宣称已完成独立全流程复现。
