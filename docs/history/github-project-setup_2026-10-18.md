# GitHub项目搭建

> **Publication note / 发布说明:** Selected historical planning conversation exported from the user's local ChatGPT account archive. This file preserves the exported user-visible message order and content except for the listed privacy redactions. The export reported two user and two assistant messages; internal reasoning was excluded. It is not the complete account export, and no attachments were listed for this conversation. This is a planning record; it does not assert that the described setup was already completed.
>
> 本文件是从用户本地 ChatGPT 账户导出中选取的历史规划对话，按导出顺序保留用户可见消息；除下述隐私脱敏外保留正文。导出记录显示用户消息 2 条、助手消息 2 条；内部推理未纳入。它不是完整账户导出；该对话未列出附件。本文件是规划记录，不表示其中描述的搭建当时已经完成。


- Conversation ID: `6ad4ae35…`
- Created (UTC): 2026-10-18T11:32:05.995518+00:00
- Archived in export: False
- Source: ChatGPT account export `conversations.json`.
- Review rule: user-visible message nodes are rendered below. Internal `thoughts`, `analysis`, and `reasoning_recap` nodes are excluded and counted in the inventory. Parent-child links define order; sibling continuations are alternatives, listed by timestamp.

### user — `698c5964…` — 2026-10-18T11:32:02.793000+00:00

二、GitHub项目定位
不要做成：
scripts/
xxx.py
xxx.sh
这种导师看了价值低。
应该像一个科研repo：
protein-binder-design-ai/
│
├── README.md
│
├── LICENSE
│
├── docs/
│   └── project_report.pdf
│
├── workflow/
│
│   ├── pipeline_overview.md
│   └── workflow.png
│
├── EGFR_binder_design/
│
│   ├── README.md
│   │
│   ├── target_preparation/
│   │   ├── 6ARU_original.pdb
│   │   └── EGFR_DIII_RFdiffusion.pdb
│   │
│   ├── RFdiffusion/
│   │   └── generation_notes.md
│   │
│   ├── ProteinMPNN/
│   │   └── sequence_design.md
│   │
│   ├── structure_prediction/
│   │   ├── ColabFold/
│   │   └── Boltz2/
│   │
│   └── results/
│       ├── models/
│       ├── metrics.csv
│       └── figures/
│
│
├── TNF_benchmark/
│
│   ├── README.md
│
│   ├── controls/
│   │
│   ├── ColabFold/
│   │
│   ├── Boltz2/
│   │
│   └── analysis/
│
│
├── scripts/
│
│   ├── prepare_structure/
│   ├── calculate_interface/
│   └── ranking/
│
│
├── analysis/
│
│   ├── interface_metrics/
│   └── visualization/
│
│
└── figures/
├── workflow.png
├── EGFR_design.png
├── TNF_benchmark.png
└── pipeline_summary.png
项目报告完成了，再带我搞一下github

### assistant — `2f978f68…` — 2026-10-18T11:32:22.526253+00:00

好，我们现在把 **AI-BinderDesign 从一份完成的项目报告，整理成一个导师点开 GitHub 就能看懂、能检查、也能继续复现的科研项目仓库。**

我建议不要一上来就创建一堆文件夹、上传所有 PDB 和脚本。我们按照科研项目的思路，一步步把仓库搭好，并且保证每一份文件都有实际内容支撑。

## 一、先确定 GitHub 项目的最终定位

<box border radius="xl" padding={4} gap={3}>
  <row align="center" gap={3}>
    <box background="surface-secondary" radius="lg" size="52px" align="center" justify="center">
      <icon name="microscope" size="2xl"/>
    </box>
    <box flex="1" gap={1}>
      <title size="lg">AI-BinderDesign</title>
      <text color="secondary" size="sm">A Benchmark-Calibrated Pipeline for De Novo Protein Binder Design and Structural Evaluation</text>
    </box>
  </row>
  <divider color="subtle"/>
  <text color="secondary" size="sm">仓库要传达的核心研究问题</text>
  **Can structural confidence scores distinguish known binders from known non-binders?**

  不只是展示如何调用 RFdiffusion、ProteinMPNN 和 Boltz-2，而是展示你如何建立计算设计流程、分析结构评价指标，并通过已知阳性与阴性对照检查评分的判别能力。
</box>

这会比单纯的 `scripts/xxx.py` 仓库更适合你后续联系上海交大的 AI-for-Science / 蛋白质设计课题组。

## 二、我们按这个顺序搭建

<box gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="42px" align="center" justify="center">
      <icon name="folder-git-2" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **第一步：确认现有材料**

      <text color="secondary" size="sm">找到已完成的项目报告、实际运行结果、分析表格和现有脚本，避免重复制作，也避免上传不完整或错误归属的数据。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="42px" align="center" justify="center">
      <icon name="file-text" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **第二步：建立 README 和项目说明**

      <text color="secondary" size="sm">让导师打开仓库首页，就能理解研究问题、整体流程、你的具体贡献、已有结果和项目局限。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="42px" align="center" justify="center">
      <icon name="network" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **第三步：整理科研目录**

      <text color="secondary" size="sm">按 EGFR 设计、TNF 基准测试、工作流、分析与报告组织材料。只建立有内容或有明确用途的目录。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="42px" align="center" justify="center">
      <icon name="git-commit" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **第四步：上传 GitHub 并检查**

      <text color="secondary" size="sm">补齐许可证、数据来源、运行说明和必要的忽略规则，再进行首次提交，最后从导师视角检查仓库。</text>
    </box>
  </row>
</box>

## 三、先确认你的材料现在在哪里

我记得你的项目里，EGFR 设计与评分校准、TNF-α 对照测试是两条需要区分的工作线。尤其不能把 EGFR 的 7D12 / scramble 对照结果误放进 TNF benchmark 目录。

先确认一下当前材料的位置，这决定我们下一步怎么操作。

{@body const [report,setReport] = DIL.useState("ppt")}
{@body const [project,setProject] = DIL.useState("wsl")}
{@body const [github,setGithub] = DIL.useState("new")}
{@body const [materials,setMaterials] = DIL.useState(["results","scripts"])}
<box border radius="xl" padding={4} gap={4}>
  <text weight="medium">1. 项目报告目前是什么格式？</text>
  <radio-group value={report} onChange={setReport} direction="col">
    <radio value="pdf">已经导出为 PDF</radio>
    <radio value="ppt">目前是 PPTX，还没有导出 PDF</radio>
    <radio value="both">PPTX 和 PDF 都有</radio>
  </radio-group>
  <divider color="subtle"/>
  <text weight="medium">2. 项目文件目前主要在哪里？</text>
  <radio-group value={project} onChange={setProject} direction="col">
    <radio value="wsl">WSL / Ubuntu，主要在 `<LOCAL_PRP>`</radio>
    <radio value="windows">Windows 文件夹</radio>
    <radio value="github">已经有一个 GitHub 仓库</radio>
    <radio value="mixed">分散在多个位置</radio>
  </radio-group>
  <divider color="subtle"/>
  <text weight="medium">3. GitHub 仓库状态</text>
  <radio-group value={github} onChange={setGithub} direction="col">
    <radio value="new">还没创建仓库</radio>
    <radio value="empty">已经创建，但基本是空的</radio>
    <radio value="existing">已有内容，需要重组</radio>
  </radio-group>
  <divider color="subtle"/>
  <text weight="medium">4. 你目前手里有哪些现成材料？（可多选）</text>
  {#each [{value:"results",label:"预测结果、PDB、指标 CSV"},{value:"scripts",label:"实际运行过的脚本"},{value:"figures",label:"项目流程图、结果图"},{value:"data",label:"数据汇总表、实验或文献依据"}] as item}
    <checkbox key={item.value} checked={materials.includes(item.value)} onChange={v=>setMaterials(old=>v?[...old,item.value]:old.filter(x=>x!==item.value))} lineThrough={false}>{item.label}</checkbox>
  {/each}
  <button block onClick={() => GenUI.issueNewTurn("开始搭建 AI-BinderDesign GitHub 科研仓库。项目报告："+({"pdf":"已有 PDF","ppt":"只有 PPTX，尚未导出 PDF","both":"PPTX 和 PDF 都有"}[report])+"；项目文件位置："+({"wsl":"WSL/Ubuntu，主要在 <LOCAL_PRP>","windows":"Windows 文件夹","github":"已有 GitHub 仓库","mixed":"文件分散在多个位置"}[project])+"；GitHub 状态："+({"new":"尚未创建","empty":"已创建空仓库","existing":"已有内容需要重组"}[github])+"；现有材料："+(materials.length?materials.join("、"):"暂未确认")+"。请根据这些信息指导下一步，并坚持只整理实际存在且来源明确的科研材料。")} >确认，开始搭建 <icon name="arrow-right" size="sm" inline/></button>
</box>

**我的建议：先把首页和核心目录做好，再上传结果。** 一个内容扎实、逻辑清楚、如实标注完成度的仓库，比目录庞大但很多文件为空的仓库更有科研价值。

### user — `e5c461d3…` — 2026-10-18T11:34:09.487000+00:00

开始搭建 AI-BinderDesign GitHub 科研仓库。项目报告：只有 PPTX，尚未导出 PDF；项目文件位置：WSL/Ubuntu，主要在 <LOCAL_PRP>；GitHub 状态：已创建空仓库；现有材料：results、scripts。请根据这些信息指导下一步，并坚持只整理实际存在且来源明确的科研材料。

### assistant — `753214fd…` — 2026-10-18T11:34:25.915772+00:00

我们就从第一步开始：**先盘点 `<LOCAL_PRP>` 中已经存在的真实材料，再决定怎么组织仓库。** 暂时不批量上传，也不创建没有实际内容支撑的目录。

由于你选择留在当前聊天，我不能直接替你检查 WSL 磁盘或操作 GitHub 网页；不过我可以带你逐步执行命令，并根据真实输出决定下一步。

## 第一步：检查项目文件

打开 WSL Ubuntu 终端，依次执行下面的命令。

### 1. 查看现有项目目录

```bash
cd <LOCAL_PRP>

echo "===== Current directory ====="
pwd

echo "===== Top-level files ====="
ls -lah

echo "===== Candidate project directories ====="
find . -maxdepth 2 -type d \
  \( -iname '*egfr*' -o -iname '*tnf*' \
     -o -iname '*binder*' -o -iname '*result*' \
     -o -iname '*script*' -o -iname '*slide*' \) \
  -print
```

这一步是确认项目材料的实际位置，不会修改任何文件。

### 2. 查找报告、数据和分析脚本

```bash
echo "===== Project reports ====="
find <LOCAL_PRP> -maxdepth 5 -type f \
  \( -iname '*.pptx' -o -iname '*.pdf' \) \
  -print 2>/dev/null

echo "===== Result and analysis files ====="
find <LOCAL_PRP> -maxdepth 5 -type f \
  \( -iname '*.csv' -o -iname '*.tsv' \
     -o -iname '*.json' -o -iname '*.md' \
     -o -iname '*.py' -o -iname '*.sh' \) \
  -print 2>/dev/null | head -200
```

这里先只列出文件名，不读取或上传所有结果。后续我们会重点确认：

- 哪个 PPTX 是最终项目报告；
- 哪些 CSV 真正对应 EGFR 设计或评分校准；
- 哪些结果来自独立的 TNF-α 对照测试；
- 哪些脚本是你实际运行过的，哪些只是第三方工具自带的代码。

如果 `<LOCAL_PRP>` 下还有其他无关项目，我们不会把它们全部放进仓库。

## 第二步：确定 GitHub 仓库位置

你已经创建了空仓库。接下来需要确认远程地址，避免把项目推送到错误的仓库。

执行：

```bash
git -C <LOCAL_PRP> remote -v
```

如果提示该目录不是 Git 仓库，也不用担心，这只是说明当前项目目录还没有初始化 Git。

你也可以在 GitHub 空仓库页面复制 HTTPS 地址。**不要发送密码、Personal Access Token 或其他凭证。**

## 第三步：我们最终会建立什么结构？

在检查完文件后，预计会整理成下面这种结构。它是目标方案，不代表这些目录和文件现在都已经存在。

```text
AI-BinderDesign/
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   └── project_report.pdf
│
├── workflow/
│   └── pipeline_overview.md
│
├── EGFR_binder_design/
│   ├── README.md
│   ├── target_preparation/
│   ├── structure_prediction/
│   └── results/
│       ├── metrics.csv
│       └── figures/
│
├── TNF_benchmark/
│   ├── README.md
│   ├── controls/
│   └── analysis/
│
├── scripts/
│   ├── prepare_structure/
│   ├── calculate_interface/
│   └── ranking/
│
├── analysis/
│   ├── interface_metrics/
│   └── visualization/
│
└── figures/
```

我们会根据盘点结果删减、调整目录，不会为了让仓库看起来完整而创建大量空文件夹。

另外有三条原则：

1. **报告：** 保留最终 PPTX，并在确认导出效果后添加 PDF。
2. **结果：** 优先提交可以说明研究结论的指标表、代表性结构和分析图；大型中间文件不默认全部上传。
3. **科研诚信：** EGFR 的 7D12 / scramble 校准结果与 TNF-α benchmark 分开记录；未计算的指标不写进结论，未验证的流程不标注为可复现。

---

**现在先把第一步和第二步的终端输出发给我。** 我会根据实际文件清单帮你确定哪些文件该进仓库、哪些应该排除，然后给你下一组具体命令。我们先把仓库的真实基础搭稳，再写 README 和首次提交。

## Coverage counts

```json
{
  "user": 2,
  "assistant": 2,
  "tool": 0,
  "other": 0,
  "hidden_assistant": 0,
  "null": 1,
  "orphan": 0
}
```
