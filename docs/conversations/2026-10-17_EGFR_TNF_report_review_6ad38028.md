# 核对后续页面


- Conversation ID: `<UUID>`
- Created (UTC): 2026-10-17T14:03:20.686008+00:00
- Archived in export: True
- Source: ChatGPT account export `conversations.json`.
- Review rule: user-visible message nodes are rendered below. Internal `thoughts`, `analysis`, and `reasoning_recap` nodes are excluded and counted in the inventory. Parent-child links define order; sibling continuations are alternatives, listed by timestamp.

### user — `<UUID>` — 2026-10-17T14:03:19.118000+00:00

# 【幻灯片文字稿】5.0 · WHAT THE BENCHMARK REALLY TEACHES US（v2，deck 第 20 页）

> 用途：供无法打开 PPT 文件的审阅者使用。按版面从上到下、从左到右逐区块描述。 对应文件：**Slides-25-Lessons-v2.pptx**（16:9，白底，主色交大红；v1 保留备查） **v2 总原则：PPT 以中文为主体**——过渡区、卡片标题、总结带均中文居前，英文降为辅助。 大纲位置：**P20 · 5.0**（LESSONS FROM BENCHMARKING）；已**追加**为主 deck 第 20 页（P1–P19 未动）。 本页定位：**TNF-α / EGFR 案例分析的思想转折页**——P17–P19 的具体预测异常，在本页提升为基准校准的方法论启示。核心逻辑：**分数不是判决，阈值需要校准**。

---

## 一、版面逐区描述

■ **顶部眉行**（0.00 / 0.30，红线 0.04）

- 左：`5.0 · LESSONS FROM BENCHMARKING　｜　基准校准的启示`（红 13pt 粗）

* 右：`RESEARCH REPORT · 2026`（浅灰 10pt）

■ **主标题 + 过渡区**（**v2 中文为主**）

- 主标题（24pt 黑粗）：`WHAT THE BENCHMARK REALLY TEACHES US`

* 过渡标签（红 11pt 粗）：`TRANSITION · 从案例观察到基准校准`

- 过渡句中文（**主句**，黑 12pt）：`这些案例提醒我们：结构置信度分数并不总能直接对应真实的结合能力，因此，候选筛选阈值需要通过已知阳性与阴性对照进行校准。`

* 过渡句英文（辅助，Georgia 斜体 10pt 灰）：`These cases show that structural confidence scores do not always directly reflect binding ability; screening thresholds must therefore be calibrated against known positive and negative controls.`

■ **左卡 01 · 分数不是判决　A SCORE IS NOT A VERDICT**（白卡红竖条，0.70 / 2.26 / 5.85 × 4.10；**v2 中文居前**）

- 副标签（浅灰 8.5pt）：`对照实验实测：已知结合剂 vs 组成匹配乱序阴性（同一批参数 · 鼠侧）`

* 证据面板（灰底，两根横向 ipTM 数值条，0–1.0 标尺）：
  - `已知结合剂 7D12（真 binder）`——红条 **0.417**
  * `乱序阴性对照（按构造不可能结合）`——灰条 **0.846**（明显更长）
  - 轴注：`ipTM（0–1.0）· 同一批参数实测；人侧：乱序 0.706 vs 7D12 0.622`

- 总结（EN Georgia 斜体 9.5pt + CN 9pt）：`A single confidence score may fail to distinguish known binders from non-binders.` ／ `单一置信度分数可能无法区分已知结合剂与非结合剂。`

* 方法论启示（红 10.5pt 粗）：`启示：高分不能直接证明结合，低分也不能单独证明不结合。`

- 脚注（浅灰 8pt）：`仅说明单一 ipTM 在该对照案例中判别失败，不推广至其他指标。`

■ **右卡 02 · 阈值需要校准　THRESHOLDS NEED CALIBRATION**（白卡红竖条，6.78 / 2.26 / 5.85 × 4.10；**v2 中文居前**）

- 副标签：`EGFR & TNF-α benchmarks：以对照检验指标的判别能力`

* 证据面板（灰底）：`以已知阳性与阴性对照检验评价指标的判别能力，并结合结构排布与界面证据解读预测结果。`＋ 三个关键词（红点列表）：`Known positives — 已知阳性对照`｜`Known negatives — 已知阴性对照`｜`Structural evidence — 结构证据`

- 总结：`A screening threshold is meaningful only when its discriminative value has been tested against appropriate controls.` ／ `只有经过适当对照验证了判别能力，筛选阈值才具有可靠的解释依据。`

* 方法论启示（红粗）：`启示：先验证指标能否区分对照，再决定如何使用它筛选候选。`

■ **底部核心总结带**（粉底，0.70 / 6.56 / 11.93 × 0.80，整页视觉落点；**v2 中文为主句**）

- 中文（**14pt 粗**，居中）：`我们的目标不是追求更高的分数，而是用生物学证据校准分数的解释与使用方式。`

* 英文（Georgia 斜体 11pt 灰，居中）：`The goal is not to maximize scores, but to calibrate them against biological evidence.`

---

## 二、数据核验（逐条可溯源）

|   |
| - |

数字

|   |
| - |

来源

|   |
| - |

状态

|   |
| - |

乱序阴性 #2 ipTM **0.846**（鼠）

|   |
| - |

`TEAM_PACK.md` §参照物表 / `RERANK.md` / `BOLTZ_PROTOCOL.md` §8（多处互证）

|   |
| - |

✅

|   |
| - |

乱序阴性 #1 ipTM 0.812（鼠）/ 0.665（人）；#2 人侧 0.706

|   |
| - |

同上

|   |
| - |

✅（人侧数值入轴注）

|   |
| - |

已知结合剂 7D12 ipTM **0.417**（鼠）/ 0.622（人）

|   |
| - |

同上

|   |
| - |

✅

|   |
| - |

对比口径

|   |
| - |

同一批参数实测（msa: empty 口径）；乱序阴性按构造不可能结合，标定噪声地板

|   |
| - |

✅ 页面已标"同一批参数 · 鼠侧"

> ⚠️ **来源勘误（重要）**：顾问提示词把这对数标为 "TNF-α benchmark"——**实为 7D12 对照实验（EGFR 设计线的对照标定批）**，不是 TNF-α benchmark。页面已按真实来源标注为"对照实验实测"，未沿用错标。
>
> ⚠️ **措辞纪律**：该证据仅说明单一 ipTM 在该对照案例中判别失败，不推广为"所有结构指标都无效"；未添加判别准确率 / 最佳阈值 / ROC-AUC 等未计算数据；"结构看起来更合理"未等同于"结合能力已验证"。

---

## 三、科学边界自查

|   |
| - |

要求

|   |
| - |

落实

|   |
| - |

数值条不暗示"高分=更好"

|   |
| - |

✅ 灰条（阴性）更长、红条（真 binder）更短，视觉即反直觉本身

|   |
| - |

不扩大为"所有指标无效"

|   |
| - |

✅ 左卡脚注明示"仅该对照案例"

|   |
| - |

不添加未计算的判别准确率 / 最佳阈值 / ROC-AUC

|   |
| - |

✅ 校验通过（四词均不在页上）

|   |
| - |

"结构更合理"≠"结合已验证"

|   |
| - |

✅ 右栏只提"结合结构排布与界面证据分析"，不下准确性结论

|   |
| - |

两类证据不混同

|   |
| - |

✅ 左卡=单一指标判别失败（7D12 对照实验）；右栏=校准方法论（两条 benchmark 线的结构证据）

---

## 四、白话层（讲人话）

**这一页在讲什么** 前面几页的意外发现，到这里收束成两句话。第一句：**分数不是判决**——我们自己的对照实验里，一条按构造不可能结合的乱序阴性，ipTM 反而比真实可结晶的 binder 7D12 更高（0.846 vs 0.417）。单一分数连"已知会结合"和"不可能结合"都分不开。第二句：**阈值需要校准**——所以不能用经验或某个通用分数直接设筛选线，必须先用已知阳性和阴性对照检验指标到底有没有判别力，再结合结构证据解读。整页落点：**我们的目标不是追求更高的分数，而是用生物学证据校准分数的解释与使用方式。**

**在整套 PPT 中的作用** P17 量化观察 → P18–19 结构对照与初步结论 → P20 方法论升华：意外发现不是偏离主线的岔路，而是"为什么必须基准校准"的直接动机——项目从"运行设计模型"走向"评估设计结果"的转折点。

---

## 五、制作信息

- 产物：`_gen_50lessons_v1_slide.py` → 存档 `Slides-25-Lessons-v1.pptx` + add_slide 直接绘制进 deck 第 20 页（现 20 页）。

* 数值条：红条（7D12 0.417）与灰条（乱序阴性 0.846）等标尺（3.30 in / 1.0），同轴对照。

- **v2**（17:31，按木木两条意见）：① 过渡区改 `TRANSITION · 从案例观察到基准校准` 标签 + 中文主句 + 英文辅助；② **全页中文为主体**——卡片标题中文居前、总结带中文 14pt 为主句（EN 11pt 斜体辅助）、卡内数据与关键词不动。产物：`_gen_50lessons_v2_slide.py` → `Slides-25-Lessons-v2.pptx` + spTree 清空重画 deck 第 20 页（重画前已确认 S20 无手改）。

我觉得过渡标签多余了，主标题最好用中文

同意。P20 是方法论总结页，继续用英文长标题会削弱整套 PPT 的中文叙事连贯性；而且“TRANSITION”标签确实没有必要，过渡功能应该由标题下方的引导句自然承担。

建议修改为以下版本，其他数据和科学边界保持不变。

## P20 修改后的顶部与整体文案

5.0 · LESSONS FROM BENCHMARKING｜基准校准的启示

# 基准校准真正告诉我们的事

WHAT THE BENCHMARK REALLY TEACHES US

过渡引导句（不加标签）

这些案例提醒我们：结构置信度分数并不总能直接反映真实的结合能力，因此，候选筛选阈值需要通过已知阳性与阴性对照进行校准。

Structural confidence scores do not always reflect binding ability; screening thresholds must therefore be calibrated against known positive and negative controls.

### 两张主体卡片

## 01

## 分数不是判决

A SCORE IS NOT A VERDICT

- 已知结合剂 7D12：ipTM 0.417
- 乱序阴性对照：ipTM 0.846

单一 ipTM 在这一对照案例中未能区分已知结合剂与阴性对照。

启示：高分不能直接证明结合，低分也不能单独证明不结合。

## 02

## 阈值需要校准

THRESHOLDS NEED CALIBRATION

结合 EGFR 与 TNF-α 案例，以已知阳性、阴性对照检验指标的判别能力，并结合结构排布与界面证据解读预测结果。

启示：先验证指标能否区分对照，再决定如何使用它筛选候选。

### 底部总结带

## 我们的目标不是追求更高的分数，而是用生物学证据校准分数的解释与使用方式。

The goal is not to maximize scores, but to calibrate them against biological evidence.

## 可直接交给 WorkBuddy 的修改指令

请修改 `Slides-25-Lessons-v2.pptx` 的第 20 页，生成 v3。

1. 删除 `TRANSITION · 从案例观察到基准校准` 标签。过渡区不再使用独立标签。
2. 将主标题改为中文：**基准校准真正告诉我们的事**。原英文标题 `WHAT THE BENCHMARK REALLY TEACHES US` 降为较小字号的英文副标题，放在中文主标题下方。
3. 标题下方直接放置中文过渡句：\
   “这些案例提醒我们：结构置信度分数并不总能直接反映真实的结合能力，因此，候选筛选阈值需要通过已知阳性与阴性对照进行校准。”
4. 英文过渡句保留为较小字号、浅灰色的辅助文字，不加标签。
5. 两张主体卡片、所有已核验数据、科学边界脚注和底部总结带保持不变；卡片标题继续中文居前、英文居后。
6. 保持白底、交大红主色、16:9 比例和现有 deck 的视觉体系。适当调整顶部空间，避免删除标签后出现不自然的空白。
7. 不修改 P1–P19，不改变数值、来源标注或证据解释。
8. 输出 `Slides-25-Lessons-v3.pptx`，并确保第 20 页排版完整、文字没有溢出。

这样改完后，P20 的阅读顺序会更自然：中文主题 → 案例引出的判断 → 两条方法论启示 → 整个项目的核心主张。

为什么卡1里要选7D12那组数据，并且突出鼠侧（绘图）

你这个问题问得很关键。卡 1 选 7D12、并突出鼠侧数据，应该有明确的实验设计理由，而不能只是因为这组数据的反差最大。

从你提供的 P20 文字稿看，卡 1 使用的是：

- 鼠侧：7D12 已知结合剂 ipTM = 0.417
- 鼠侧：乱序阴性对照 ipTM = 0.846
- 人侧补充数据：7D12 = 0.622，乱序阴性 #2 = 0.706

鼠侧的反差确实更明显，但这本身并不足以证明应该优先选择鼠侧。

## 我认为目前有三个问题需要厘清

1\. 为什么选 7D12？

因为它是已有的 EGFR 结合剂，可以作为已知阳性参照，与按构造设计的乱序阴性对照比较。这符合 benchmark 的基本逻辑：检验指标能否区分已知阳性和阴性。

2\. 为什么突出鼠侧？

从数字看，鼠侧的反差更强：

|   |
| - |

对照

|   |
| - |

7D12

|   |
| - |

乱序阴性

|   |
| - |

差值

|   |
| - |

鼠侧

|   |
| - |

0.417

|   |
| - |

0.846

|   |
| - |

0.429

|   |
| - |

人侧

|   |
| - |

0.622

|   |
| - |

0.706

|   |
| - |

0.084

但反差更大，不代表它就更适合作为主结果。如果没有预先确定鼠侧是主要评估对象的实验设计理由，只因为它更反直觉而突出鼠侧，就有选择性呈现结果的风险。

3\. 更重要的是：7D12 是否能作为鼠侧的已知阳性？

7D12 是已知的 EGFR 结合剂，但必须确认它对你使用的鼠源 EGFR 靶标也具有已知结合能力。若它只被确认为人源 EGFR 的结合剂，那么鼠侧的 0.417 不能直接标成“真 binder”，否则阳性对照的生物学身份就不成立。

## 我的建议

- 如果鼠侧确实有独立证据支持 7D12 是已知结合剂，而且两组预测的参数与评估口径匹配，可以保留鼠侧作为主图，并把人侧数据放在补充说明中。
- 如果鼠侧的阳性身份没有得到确认，建议改用人侧作为主图，或重新核实对照定义后再决定。
- 不论选哪一侧，都要明确这只是一个具体对照案例中 ipTM 判别失败的证据，不能据此直接得出通用阈值。

我现在最想确认的是：你这组“鼠侧 7D12”的预测，靶标究竟是鼠源 EGFR，还是鼠侧仅仅指另一组预测条件？ 这个定义会直接决定卡 1 的数据能不能这样用。

靶标就是鼠源EFGR，你查一下7D12是否有鼠源亲和力，然后在数据表格汇总里找一下是否有乱序阴性对应的数据

思考了 20s

查到了。结论是：7D12 确实有文献报道的鼠源 EGFR 结合能力；而且你资料库的《资料库-数据表格汇总.md》里，确实有对应的乱序阴性数据。 所以，P20 卡1用鼠侧数据并非必然不成立。不过，需要准确区分“7D12 能结合鼠源 EGFR”与“7D12 对鼠源 EGFR 的亲和力和人源一样强”。

## 1. 文献：7D12 是否能结合鼠源 EGFR？

2025 年的一篇研究专门检测了 7D12 与鼠源 EGFR 的交叉反应：

- 研究通过 Western blot 和流式细胞术观察到，7D12-mIgG-Fc 能识别人源和鼠源 EGFR。
- 通过表面等离子体共振（SPR）测得，该融合蛋白与鼠源 EGFR 的解离常数 \\(K_D\\) 为 2.9 μM。
- 文章引用的人源 EGFR 结合数据约为 219 ± 20 nM（另有报告值为 279 ± 19 nM）。因此，鼠源结合是有实验支持的，但报道的亲和力明显弱于人源。需要注意，鼠源测量用的是 7D12-mIgG-Fc 融合形式，不能直接当成未融合单价 VHH 的亲和力。

  [image](https://www.google.com/s2/favicons?domain=https://pmc.ncbi.nlm.nih.gov\&sz=32)

  PMC

  +1



另一个独立结构证据是 PDB 4KRL：它记录了 7D12 VHH 与人源 EGFR 第 III 结构域的晶体复合物；它能证明人源结合构型，但本身不是鼠源结合证据。

[image](https://www.google.com/s2/favicons?domain=https://www2.rcsb.org\&sz=32)

www2.rcsb.org

+1



因此，你这组数据里的 `7D12_mouse` 可以作为具有文献交叉反应支持的参照物，但最好在项目中标明：鼠源结合有实验报道，且不同构建形式下的亲和力不能直接等同。

## 2. 数据表格汇总：是否有对应的乱序阴性？

有。我在《资料库-数据表格汇总.md》中找到了两组相关表格。

### 核心指标表：7D12 与两个乱序阴性

表格中的鼠源、人源 ipTM 汇总如下：

资料库-数据表格汇总.md



|   |
| - |

对照组

|   |
| - |

人源 EGFR ipTM

|   |
| - |

鼠源 EGFR ipTM

|   |
| - |

7D12（已知 binder）

|   |
| - |

0.622

|   |
| - |

0.417

|   |
| - |

scramble_1（乱序阴性）

|   |
| - |

0.665

|   |
| - |

0.812

|   |
| - |

scramble_2（乱序阴性）

|   |
| - |

0.706

|   |
| - |

0.846

这里的数值与资料库记录一致；Boltz-2 汇总表中每组为 3 个样本的统计值。

资料库-数据表格汇总.md



### 这组对照最关键的发现

鼠源 EGFR

7D12 阳性参照

## 0.417

scramble_1 阴性

## 0.812

scramble_2 阴性

## 0.846

两个乱序阴性的 ipTM 都高于已知 binder 7D12，分别高出 0.395 和 0.429。

### 3. 这对 P20 卡1意味着什么？

突出鼠侧有数据依据，但理由应该是“对照差异更清晰”，而不是鼠侧的结果更适合讲故事。

- 鼠侧更有展示力： 7D12 的 ipTM 为 0.417，而两个乱序阴性分别为 0.812 和 0.846，差距明显。
- 人侧也有同方向的现象： 7D12 为 0.622，两个阴性为 0.665 和 0.706；但差距相对较小。
- 科学结论要限定范围： 这些结果支持的是，在这组 EGFR 对照及当前 Boltz-2 预测设置下，单独使用 ipTM 无法可靠地区分已知 binder 与乱序阴性。不能据此说 ipTM 在所有体系中都无效，也不能说预测分数本身证明了真实结合。

所以，我建议保留卡1的鼠侧绘图，并明确注明它是 EGFR benchmark（鼠源 EGFR），不是 TNF-α 数据。最好在图注或小字里说明：`7D12: known EGFR binder; scramble_1/2: sequence-scrambled negative controls; Boltz-2 ipTM, n=3.`

这样既保留了视觉冲击力，也交代了对照依据，不会让人误以为你只挑了一个随机阴性来比较。

对了，这张序号用4.8还是5.1

我建议用 5.1，前提是这张是你从“基准校准的教训”转入研究结果或方法讨论的第一页。

判断标准是看它在整套 PPT 中的章节归属：

- 4.8：如果它仍然属于第 4 章的 EGFR benchmark 实验结果，是前面 EGFR 对照实验的延续。
- 5.1：如果第 5 章已经开始讨论综合发现、方法学启示或结论，而这张是该章第一张内容页。

结合这张 P20 的主题 “基准校准真正告诉我们的事”，它不只是展示一组 EGFR 数据，而是在提炼跨案例的评价原则，所以我更倾向于 5.1。

不过，编号最终应服从你整套 PPT 的章节结构，而不是只看这一页的内容。若你把第 4、5 章的标题告诉我，我可以帮你把这张的编号定下来。

下一张做什么

我建议下一张做 P21：从基准校准过渡到候选筛选方法。P20 已经回答了“为什么不能只看高分”，下一张就应该回答：那么，我们实际应该怎样评价和筛选候选物？

## P21 · FROM BENCHMARK TO CANDIDATE RANKING

01 · Benchmark anchors

已知阳性与阴性对照

确认评价指标在已知对照中能否区分不同类别。

02 · Metric calibration

指标解释与筛选标准校准

综合结构置信度、界面接触与几何特征，避免单一分数主导判断。

03 · Candidate prioritization

候选物分层与优先级排序

按证据强弱对候选物进行排序，优先推进更值得验证的设计。

建议页脚：Structural scores support prioritization, not proof of binding.

## 这张的关键

- 不再重复 P20 的案例和数值，而是把案例提炼成可执行的评价策略。
- 如果目前还没有通过基准数据确定可靠阈值，就写 calibration strategy，不要宣称已经建立了通用筛选阈值。
- 下一张 P22 再进入你的实际候选结果：展示 EGFR 等目标的候选排序、证据和局限。

整段叙事就是：P17–P19 展示案例 → P20 总结教训 → P21 提出筛选原则 → P22 展示候选结果。

那P23呢

思考了 11s

我建议 P23 做 Limitations & Next Steps（研究局限与下一步），但要看 P22 是否已经安排为候选结果页。按目前 P20 → P21 的叙事，P23 可以这样接：

## P23 · LIMITATIONS & NEXT STEPS

01 · Current limitations

- 结构置信度不等同于真实结合能力。
- 当前基准体系和对照数量有限。
- 计算预测尚不能替代实验验证。

02 · Methodological improvements

- 扩充已知阳性、阴性及配对互换对照。
- 联合分析 ipTM、PAE、界面接触与几何特征。
- 在独立基准上检验筛选标准的可迁移性。

03 · Experimental validation

- 优先选择证据更充分的候选物。
- 后续通过实验测定结合能力，并用实验结果校准计算指标。

页脚可以用一句话收束：

> From structure-based prediction to evidence-calibrated candidate prioritization.

中文：从结构预测走向基于证据校准的候选物筛选。

整段顺序建议：

- P20：基准案例告诉了我们什么？
- P21：应该怎样校准评价指标？
- P22：实际候选物的评价与排序结果。
- P23：当前方法的局限，以及如何进一步验证和改进。

注意：以上是建议结构，并非我已经核实过的完整 PPT 大纲。如果你后面还有总结页、项目贡献页或参考文献页，P23 也可能需要调整；不必为了凑页数而单独增加一张局限性页。

### assistant — `<UUID>` — 2026-10-17T14:03:25.529666+00:00

我接上这段项目上下文了。我们继续按 **AI-BinderDesign 主 deck 的实际叙事**推进，不把 PPT 做成单纯的比赛汇报。

目前，P20 的定位已经比较明确：以 EGFR 对照实验中的 ipTM 反常现象为切入点，提出“分数不是判决，阈值需要校准”的方法论启示。

后续页面建议这样安排：

| 页面 | 定位 | 核心任务 |
|---|---|---|
| P20 · 5.0 | 基准校准的启示 | 解释为什么不能只看单一分数 |
| P21 · 5.1 | 从基准到候选筛选 | 提出多指标评价与候选排序原则 |
| P22 · 5.2 | 候选物评价结果 | 展示实际候选物、证据与排序 |
| P23 · 5.3（暂定） | 研究局限与下一步 | 说明当前证据边界，以及如何通过实验验证和后续校准改进流程 |

**我建议暂时把 P23 定为“研究局限与下一步”，但先不要急着制作。** 需要先确认 P22 实际有哪些候选数据，以及整套 deck 后面是否已经安排项目贡献、总结或参考文献页，避免内容重复，也避免为了凑页数而增加页面。

接下来最值得做的是核对 P21–P23 与现有 PPT 的整体大纲，再确定每页的标题、核心图表和具体文案。这样能保证这几页形成完整的研究叙事，而不是三张互相独立的总结页。

### user — `<UUID>` — 2026-10-17T14:03:55.938000+00:00

## &#x20;· MULTI-TARGET BINDER DESIGN（补充验证，不铺开）

|   |
| - |

页

|   |
| - |

章节

|   |
| - |

PPT 标题

|   |
| - |

回答什么

|   |
| - |

数据

|   |
| - |

状态

|   |
| - |

P20

|   |
| - |

6.1

|   |
| - |

MULTI-TARGET DESIGN CAMPAIGN

|   |
| - |

这套思路有没有用于其他靶点？

|   |
| - |

5 靶点全景表（Target｜Design status｜Evaluation｜Role）；GLP-1R 作为探索性案例一句带过（**不升级为主案例、不声称解决 activator**）

|   |
| - |

待制（需另 2 靶点数据）

## 7 · INTEGRATED CANDIDATE EVALUATION（把经验用于筛选）

|   |
| - |

页

|   |
| - |

章节

|   |
| - |

PPT 标题

|   |
| - |

回答什么

|   |
| - |

数据

|   |
| - |

状态

|   |
| - |

P21

|   |
| - |

7

|   |
| - |

MULTI-METRIC DECISION

|   |
| - |

经验如何改变候选筛选？

|   |
| - |

BEFORE Single-score → CALIBRATION → AFTER Multi-metric；四步：calibrated metrics → quality gates → multi-metric evidence → candidate ranking

|   |
| - |

✅ 内容已有（Slides-09），**移至此**、眉行改 7

## 8–11 · 收束

|   |
| - |

页

|   |
| - |

章节

|   |
| - |

标题

|   |
| - |

要点

|   |
| - |

P22

|   |
| - |

8 · DISCUSSION

|   |
| - |

Single-score limitation｜Context dependence｜Benchmark calibration｜Confidence ≠ experimental affinity

|   |
| - |

待制

|   |
| - |

P23

|   |
| - |

9 · LIMITATIONS

|   |
| - |

计算证据为主｜无完整 Kd｜benchmark 数量有限｜靶点泛化有限｜模型依赖｜未闭环

|   |
| - |

待制（素材已有）

|   |
| - |

P24

|   |
| - |

10 · FUTURE WORK

|   |
| - |

更多生物对照 → 更大 benchmark → 实验验证 → Kd/功能测定 → 指标标定 → 更可靠排序；含 TNF trimer / receptor-context-aware benchmarking

|   |
| - |

待制

|   |
| - |

P25

|   |
| - |

11 · CONCLUSION

|   |
| - |

01 Confidence is not binding evidence｜02 Low confidence does not prove non-binding｜03 Benchmark-calibrated multi-metric evaluation is necessary；收束句

|   |
| - |

待制

|   |
| - |

P26

|   |
| - |

ACK & AUTHOR CONTRIBUTIONS

|   |
| - |

分类式贡献声明

|   |
| - |

待制

## Appendix（不占页）

A 指标定义与数据字典｜B 阈值表（标注未完成 macro-AP 标定）｜C 湿实验接口（主办方口径）｜D 可复现与工程细节｜E 五靶点完整数据

怎么不按大纲来

### assistant — `<UUID>` — 2026-10-17T14:03:58.959527+00:00

你说得对，是我刚才没有严格遵循你已经确定的大纲，擅自把 P23 重新规划成了“研究局限与下一步”，还把原本明确安排在 P20–P26 的章节关系简化成了另一套结构。这是我的问题。

**后续以你刚发来的大纲为唯一执行依据，不再自行改章节、改页码或调整内容归属。**

## 按你的大纲，后续页面应这样推进

| 页码 | 章节 | 页面标题 / 主题 | 执行要求 |
|---|---|---|---|
| P20 | 6.1 | MULTI-TARGET DESIGN CAMPAIGN | 补充验证五靶点设计思路，不展开 GLP-1R |
| P21 | 7 | MULTI-METRIC DECISION | 将 Slides-09 移至此页，只调整眉行章节编号 |
| P22 | 8 · DISCUSSION | 综合讨论 | 单分数局限、情境依赖、基准校准、置信度不等于实验亲和力 |
| P23 | 9 · LIMITATIONS | 研究局限 | 计算证据为主、缺乏完整 Kd、基准数量有限、靶点泛化有限、模型依赖、验证闭环未完成 |
| P24 | 10 · FUTURE WORK | 未来工作 | 生物学对照、扩充 benchmark、实验验证、Kd/功能测定、指标校准；包括 TNF trimer 与受体情境感知基准 |
| P25 | 11 · CONCLUSION | 结论 | 三条核心结论与收束句 |
| P26 | — | ACK & AUTHOR CONTRIBUTIONS | 分类式贡献声明 |

Appendix A–E 按你的安排作为附录资料，不计入主 deck 页数。

## 现在应该做什么

**下一步回到 P20，而不是跳去制作 P23。**

P20 的 `MULTI-TARGET DESIGN CAMPAIGN` 是补充验证页，核心任务是回答“这套设计与评价思路是否用于其他靶点”。它不应抢占 P21 的多指标筛选方法论，也不应把 GLP-1R 包装成已经解决的激动剂设计案例。

不过，你的大纲明确指出还缺另外两个靶点的数据，因此 P20 目前应先核对五靶点数据的完整性，再决定如何呈现全景表，而不是直接编造状态或填充结论。

我会遵循你现有的页码、章节编号、内容归属和科学边界；如果发现大纲内部确实存在冲突，会先指出并询问，不再擅自重排。

### user — `<UUID>` — 2026-10-17T14:13:26.904000+00:00

那前面说的5.1 5.2是啥，还有必要做吗

### assistant — `<UUID>` — 2026-10-17T14:13:30.045794+00:00

前面说的 **5.1、5.2 是我当时根据 P20 的主题临时提出的拆分页建议，不是你现在这份正式大纲中的章节编号**。既然你已经确定了 P20–P26 的安排，就应该以正式大纲为准，不能再把 5.1、5.2 插进去。

## 5.1、5.2 分别是什么？还需要吗？

| 之前建议的页面 | 原本设想 | 现在的处理 |
|---|---|---|
| 5.1 · FROM BENCHMARK TO CANDIDATE RANKING | 说明如何从基准校准过渡到候选筛选 | **不必单独新增**，核心内容已由 P21 的 `MULTI-METRIC DECISION` 承担 |
| 5.2 · CANDIDATE EVALUATION | 展示实际候选物的评价与排序结果 | **暂不单独新增**，先核对现有结果页和 Slides-09 的内容，避免重复 |

### 为什么这样安排更合理？

你的正式大纲已经形成了一条完整的逻辑链：

<box border radius="lg" padding={3} gap={2}>
  <row align="start" gap={3}>
    <box background="#FCE7E7" radius="md" padding={2} align="center" justify="center" minWidth="60px">
      <title size="lg" color="#B4232C">P17–19</title>
    </box>
    <box flex="1" gap={1}>
      **案例与异常观察**

      <text color="secondary" size="sm">展示 EGFR、TNF-α 案例中的预测与结构证据。</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="#FCE7E7" radius="md" padding={2} align="center" justify="center" minWidth="60px">
      <title size="lg" color="#B4232C">P20</title>
    </box>
    <box flex="1" gap={1}>
      **5.0 · 基准校准的启示**

      <text color="secondary" size="sm">从异常现象提炼方法论认识。</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="#FCE7E7" radius="md" padding={2} align="center" justify="center" minWidth="60px">
      <title size="lg" color="#B4232C">P20</title>
    </box>
    <box flex="1" gap={1}>
      **6.1 · MULTI-TARGET DESIGN CAMPAIGN**

      <text color="secondary" size="sm">补充验证这套思路在其他靶点上的应用范围。</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="#FCE7E7" radius="md" padding={2} align="center" justify="center" minWidth="60px">
      <title size="lg" color="#B4232C">P21</title>
    </box>
    <box flex="1" gap={1}>
      **7 · MULTI-METRIC DECISION**

      <text color="secondary" size="sm">把前面的经验转化为实际候选筛选方法。</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <box background="#FCE7E7" radius="md" padding={2} align="center" justify="center" minWidth="60px">
      <title size="lg" color="#B4232C">P22–26</title>
    </box>
    <box flex="1" gap={1}>
      **讨论、局限、未来工作、结论与贡献**

      <text color="secondary" size="sm">完成研究报告的收束。</text>
    </box>
  </row>
</box>

这里有一个细节：你发来的大纲把 **P20 同时标为 5.0 和 6.1**。这意味着需要确认 P20 是不是已经从第 5 章切换到第 6 章，或者 `MULTI-TARGET DESIGN CAMPAIGN` 实际上应当是下一页。不能在不核对 deck 的情况下直接把两个编号放在同一张幻灯片上。

**我的建议：保留现有 P20 的 5.0 内容，不新增 5.1、5.2；下一步先核实 `MULTI-TARGET DESIGN CAMPAIGN` 的实际页码，再继续制作。** 这样既保住已经完成的工作，也不会让正式大纲越来越臃肿。

### user — `<UUID>` — 2026-10-17T14:24:52.800000+00:00

现在的问题是其他靶点还没出来，6.1 · MULTI-TARGET DESIGN CAMPAIGN、7 · MULTI-METRIC DECISION如何进行？还有我之前做的EFGR和TNF-a阈值表是否有必要在报告中展示

### assistant — `<UUID>` — 2026-10-17T14:24:56.018169+00:00

我认为这两页都应该保留，但要**调整它们的研究定位，而不是等其他靶点的数据全部出来才开始做**。另外，你之前做的 EGFR 和 TNF-α 阈值表很有必要保留在报告中，不过要区分“基准数据与阈值分析结果”和“已经验证的通用筛选阈值”。

这关系到整份报告最重要的一条主线：你不是要证明五个靶点都已经设计成功，而是要展示你如何从多个设计任务出发，逐步发现单一评分的局限，并建立更可靠的候选评价方法。

## 一、6.1 · MULTI-TARGET DESIGN CAMPAIGN：其他靶点没出结果，怎么做？

**照样可以做，但必须把它定位为“多靶点设计任务的覆盖情况”，而不是“多靶点设计成功验证”。**

你现在有 5 个计划靶点，其中 3 个有可用数据。就算另外 2 个暂时没有结果，这张也可以如实呈现项目的覆盖范围和证据成熟度。

建议标题保留：

`MULTI-TARGET DESIGN CAMPAIGN`

副标题可以是：**五个靶点的设计布局与评估进展**

主视觉用一张五行全景表，不需要硬凑五个成功案例。

| 字段 | 建议展示内容 |
|---|---|
| Target | 靶点名称 |
| Design status | 设计进度：已开展、进行中、尚未完成 |
| Evaluation status | 评估状态：有预测数据、评估中、暂无结果 |
| Role in this report | 在报告中的作用：主案例、补充案例、探索性任务 |

制作时要注意：

- EGFR、TNF-α：作为本报告的主要评价案例，展示已经完成的基准分析。
- 另外已有数据的靶点：按实际完成程度列出，不需要每个都深入分析。
- 尚无结果的两个靶点：标为 `Pending` 或 `Not yet evaluated`，不能把计划中的工作写成已完成结果。
- GLP-1R：可以作为探索性任务简要提及，但明确尚未解决激动剂功能设计问题。

这样，这页回答的是“研究覆盖了哪些任务，各自进展到哪一步”，而不是“我们已经在五个靶点上都验证了方法”。

## 二、7 · MULTI-METRIC DECISION：这页不需要等待新靶点

这页反而是你现在最应该推进的，因为核心素材已经有了。

你之前的 EGFR 设计漏斗、TNF-α 对照评价，以及 P20 得出的“单一分数不能直接代表结合能力”，都可以支撑这一页。它要讲的不是五个靶点的横向比较，而是**你的候选筛选策略为什么从单一分数转向多指标证据**。

建议继续使用你已有的 `Slides-09`，不要重新发明一套方法。

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    <text color="secondary" weight="medium" size="sm">BEFORE · 原有策略</text>
    <title size="lg">单一分数排序</title>
    <text color="secondary" size="sm">按 ipTM 等单项结构置信度指标排序，可能让高分假阳性进入候选集。</text>
  </box>
  <row justify="center">
    <icon name="arrow-down" size="xl" color="secondary"/>
  </row>
  <box background="#FCE7E7" radius="md" padding={3} gap={1}>
    <text color="#B4232C" weight="medium" size="sm">CALIBRATION · 方法转折</text>
    **用已知阳性、阴性对照检验指标的判别能力**
    <text size="sm">根据基准证据确定各指标的适用范围，而不是直接假设高分代表高结合能力。</text>
  </box>
  <row justify="center">
    <icon name="arrow-down" size="xl" color="secondary"/>
  </row>
  <box gap={2}>
    <text color="secondary" weight="medium" size="sm">AFTER · 改进后的筛选框架</text>
    <row align="start" gap={2}>
      <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" minWidth="40px">
        <icon name="sliders-horizontal" size="lg"/>
      </box>
      <box flex="1" gap={1}>
        **01 · 指标解释与校准**
        <text color="secondary" size="sm">明确指标的适用条件和当前证据边界。</text>
      </box>
    </row>
    <row align="start" gap={2}>
      <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" minWidth="40px">
        <icon name="shield-check" size="lg"/>
      </box>
      <box flex="1" gap={1}>
        **02 · 质量门槛**
        <text color="secondary" size="sm">检查结构质量、界面几何及必要的基础条件。</text>
      </box>
    </row>
    <row align="start" gap={2}>
      <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" minWidth="40px">
        <icon name="layers" size="lg"/>
      </box>
      <box flex="1" gap={1}>
        **03 · 多指标综合证据**
        <text color="secondary" size="sm">联合置信度、界面接触、PAE 与几何信息，避免单指标主导。</text>
      </box>
    </row>
    <row align="start" gap={2}>
      <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" minWidth="40px">
        <icon name="list-ordered" size="lg"/>
      </box>
      <box flex="1" gap={1}>
        **04 · 候选排序与多样性**
        <text color="secondary" size="sm">形成计算优先级，同时保留不同设计家族，供后续验证。</text>
      </box>
    </row>
  </box>
</box>

这张的重点是**评价决策逻辑的变化**，不是再放一遍 P20 的 ipTM 对照数值。

但要注意两个科学边界：

- 如果某个阈值尚未经过独立基准的系统标定，就只能称为当前工作流的筛选标准，不能叫通用 binder 阈值。
- 多指标筛选可以改善候选优先级，但不能据此声称已经证明真实结合。

## 三、之前的 EGFR 和 TNF-α 阈值表，有没有必要放进报告？

**有必要，但不建议把完整阈值表全部塞进主 deck。** 我核对了你资料库中的核心数据底稿：它明确要求区分内部筛选标准与通用阈值，并指出系统性的 macro-AP 标定尚未完成。<FileCite ref_id="turn1file1"/>

我建议按照以下方式分配。

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="scientific protein structure evaluation benchmark metric scatter plot white background" aspectRatio="3:4" width="100px"/>
    <box flex="1" gap={1}>
      **EGFR 阈值表：正文展示精简版**

      <badge color="success">建议保留</badge>

      EGFR 是你的主要设计案例，阈值和筛选条件直接关系到候选漏斗以及最后为什么优先考虑某些设计。因此正文应展示关键指标、采用的工作标准、通过筛选后的候选变化，以及这些标准的证据来源。

      完整逐项阈值、判据和数据字典放 Appendix A/B。
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="TNF alpha protein trimer receptor complex molecular structure scientific visualization" aspectRatio="3:4" width="100px"/>
    <box flex="1" gap={1}>
      **TNF-α 阈值表：正文展示基准结论，完整表放附录**

      <badge>按实际用途取舍</badge>

      TNF-α 更适合支撑“评价指标是否能够区分已知对照”的论点。正文可展示关键对照、主要指标的判别表现和局限；如果阈值表只是内部探索得到的数值范围，不必逐项铺开。

      完整表格保留在 Appendix，方便审阅者追溯具体数值和筛选口径。
    </box>
  </row>
</box>

这里还要区分两件事：

| 内容 | 应如何表述 |
|---|---|
| 根据现有数据确定的内部筛选条件 | 当前 benchmark 下的工作标准 |
| 经过独立、有实验标签的数据集系统检验的阈值 | 经过验证的判别标准，仍需说明适用范围 |
| 尚未完成 macro-AP 等系统评估的阈值 | 暂定标准，不能宣称具有普遍判别能力 |

尤其是 EGFR：你的资料库建议进一步在公开、具有真实实验标签的数据集上使用 macro-AP 检验 `ipSAE_min` 的判别能力。也就是说，**现有阈值表有价值，但不应该被包装成校准已经全部完成的证明。**<FileCite ref_id="turn0file0"/>

## 四、具体怎么安排到你的大纲里？

我建议保持你确定的章节结构，只明确每页承担什么任务。

| 页面 | 要放的内容 | 阈值表的处理 |
|---|---|---|
| 6.1 · MULTI-TARGET DESIGN CAMPAIGN | 五靶点任务全景与进度 | 不放阈值细节 |
| 7 · MULTI-METRIC DECISION | 单分数 → 校准 → 多指标 → 候选排序 | 展示决策框架，不重复完整阈值表 |
| 8 · DISCUSSION | EGFR 与 TNF-α 揭示的不同评价局限 | 用关键证据解释方法为何必要 |
| 9 · LIMITATIONS | 基准规模、缺乏完整 Kd、泛化和实验验证局限 | 明确阈值标定尚未闭环 |
| Appendix A/B | 指标定义、完整阈值表及校准状态 | 保留可追溯的完整资料 |

## 五、我最推荐的执行顺序

1. **先完成第 7 章的 MULTI-METRIC DECISION。** 直接利用现有 Slides-09，把它整理成正式大纲规定的页面。
2. 同步整理 EGFR 和 TNF-α 阈值表：标出每项阈值的来源、用途、是否经过系统验证，不急着重新计算所有数据。
3. 再制作 6.1 多靶点全景页。缺少结果的靶点如实标记为待完成，不必等待它们才能完成整页。
4. 最后根据实际结果制作 Discussion 和 Limitations，确保讨论中的每个判断都能回指到已有证据。

还有一个需要纠正的排版问题：你当前大纲将 `P20 · 6.1 MULTI-TARGET DESIGN CAMPAIGN` 放在了 P20，而我们此前已将基准校准的 5.0 页面追加为 deck 第 20 页。**正式制作前必须核对实际 deck 页码**，不能让两个页面同时占据 P20，也不能因此擅自改动后续章节编号。

整体上，你现在并不缺少足以继续制作的内容。真正需要做的是把已有数据分成三层：**正文中的关键证据、附录中的完整阈值资料，以及尚待系统验证的研究问题。** 这样既能体现你实际做过的工作，也能避免过度声称研究结论。

### user — `<UUID>` — 2026-10-17T14:36:30.533000+00:00

那先把6.1 · MULTI-TARGET DESIGN CAMPAIGN框架搭好吧，给个提示词

### assistant — `<UUID>` — 2026-10-17T14:36:34.073826+00:00

这页建议先搭好**版式、五靶点全景表和状态标注规则**，不必等另外两个靶点的数据出来再制作。重点是体现项目覆盖范围，同时明确区分已完成的设计、已开展的评估和仍在探索的任务。

下面这段可以直接交给 WorkBuddy。特意要求它先核对现有资料，不能为了填满五行而编造数据，也不能擅自修改其他页面。

<WritingBlock id="62814" variant="document"># WorkBuddy 制作指令：6.1 · MULTI-TARGET DESIGN CAMPAIGN

## 一、任务目标

在现有 AI-BinderDesign 主 deck 中，制作一张新的章节页面：

**6.1 · MULTI-TARGET DESIGN CAMPAIGN**

中文副标题：**多靶点设计布局与评估进展**

本页属于研究报告的补充验证部分，不是核心结果页。目的是回答：

> 这套蛋白设计与结构评价思路，已经应用于哪些靶点？各靶点目前推进到什么程度？

本页强调项目的研究覆盖范围与证据成熟度，不宣称所有靶点均已设计成功，也不把探索性任务包装成已验证的成果。

## 二、制作前必须核对

1. 检查当前主 deck 的实际页数、章节编号、页面风格，以及 6.1 应插入的位置。
2. 检查现有项目资料库、数据表格汇总、项目总览和相关结果文件，核实五个计划靶点的准确名称、设计进度、评价进度及实际证据。
3. 优先使用已有资料，不要为了制作页面而重新运行模型。
4. 如果某个靶点的状态无法确认，标为 `Pending verification`，不得根据项目计划推断为已完成。
5. 先形成一份五靶点状态核对表，再制作页面。若缺少必要信息，保留明确的待补字段，不要自行补造。

## 三、页面结构

采用 16:9、白底、上海交通大学红色作为主色，沿用现有主 deck 的字体、眉行、页边距和卡片风格。

### 1. 顶部眉行

左侧：

`6.1 · MULTI-TARGET DESIGN CAMPAIGN`

右侧：

`AI-BINDERDESIGN · RESEARCH REPORT`

### 2. 主标题区

中文主标题：

**从单一靶点到多靶点设计探索**

英文副标题：

`MULTI-TARGET DESIGN CAMPAIGN`

引导句：

`以 EGFR 和 TNF-α 为主要研究案例，同时梳理其他靶点的设计与评价进展。`

中文为主体，英文仅作辅助。不要额外添加 TRANSITION 标签。

### 3. 中央主体：五靶点全景表

使用一张清晰的五行表格，不使用五张大型卡片，不使用虚构的成功率、评分或排名。

表格包含四列：

| Target | Design status | Evaluation status | Role in this report |
|---|---|---|---|
| 靶点名称 | 实际设计进度 | 实际评价进度 | 在报告中的作用 |

每个字段必须根据现有资料填写。

状态建议使用简短、统一的文字：

- `Completed`：有资料证实该阶段已完成。
- `In progress`：已有明确记录表明该阶段正在进行。
- `Pending`：尚未完成，或当前没有可用结果。
- `Pending verification`：资料不足，暂时无法确认。

不要将“完成结构预测”等同于“完成结合验证”，也不要把“已运行设计模型”等同于“设计成功”。

### 4. 案例层级

根据实际数据，在角色列中区分：

- **EGFR**：主要设计案例；突出已有候选设计与评价流程。
- **TNF-α**：主要基准评价案例；突出已知对照与指标判别问题。
- **GLP-1R**：探索性功能设计问题；只简要说明从结合设计走向功能调控的挑战。
- **其他两个靶点**：按实际进度如实填写，不预设其结果或研究价值。

以上是预期的叙事层级，不是可以直接替代数据核查的状态结论。若资料显示实际进度不同，以核实后的资料为准。

GLP-1R 必须遵守以下科学边界：

`Binding does not establish activation.`

不能宣称已经获得有效激动剂、解决 activator design 或验证受体激活功能，除非存在相应实验结果。

### 5. 页面底部总结句

中文主句：

**多靶点布局体现研究范围；可靠的评价结论仍取决于各靶点实际获得的证据。**

英文辅助句：

`Project breadth defines the scope; evidence determines the strength of each conclusion.`

## 四、视觉设计要求

- EGFR 和 TNF-α 可采用较醒目的红色标题或细边框，体现核心案例地位。
- GLP-1R 使用中性、克制的探索性标记，不使用代表成功的绿色勾号。
- 尚无结果的靶点采用浅灰色状态，不使用警告红，也不将其描述为失败。
- 五行表格保持紧凑，保证靶点名称、设计状态、评价状态和角色都能一眼读清。
- 不添加没有数据依据的柱状图、雷达图、成功率、百分比或综合评分。
- 不堆砌工具名称、氨基酸序列、复杂指标和技术细节；这些内容留给后续案例页或 Appendix。

## 五、禁止事项

1. 不虚构另外两个靶点的实验、预测或设计结果。
2. 不把五靶点计划写成五靶点均已完成验证。
3. 不把结构置信度解释成实验亲和力。
4. 不宣称 GLP-1R 激动剂设计已成功。
5. 不把阈值表、详细 benchmark 数值或候选排名搬到本页。
6. 不新增 5.1、5.2 等临时章节，不重排正式大纲。
7. 不修改现有 P1–P19 或其他已有页面的内容。
8. 不擅自将新页面插入错误位置或改变后续章节编号。

## 六、交付要求

输出：

1. 新页面预览。
2. 五靶点状态核对表，注明每项状态的资料依据和仍待确认的信息。
3. 更新后的主 deck 文件，文件名使用 `Slides-25-MultiTarget-v1.pptx`；如果无法可靠地在现有 deck 中插入页面，则先交付独立页面文件，不得重建或覆盖原 deck。
4. 制作完成后检查文字溢出、表格对齐、字号、页面比例和章节编号。

完成标准：即使两个靶点暂时没有结果，本页仍然信息完整、状态诚实、视觉统一，并且能够自然引出下一页 `7 · MULTI-METRIC DECISION`。</WritingBlock>

**我特别建议保留“设计进度”和“评价进度”两列。** 这能避免把“模型已经运行”误写成“候选物已经得到验证”，也能让读者看出 EGFR 与 TNF-α 分别承担设计案例和基准评价案例的作用。

等 WorkBuddy 做出第一版后，先检查五靶点状态是否有资料依据，再决定是否需要进一步压缩表格或强化视觉层级。

### user — `<UUID>` — 2026-10-17T15:02:11.506000+00:00

# 6.1 五靶点状态核对表 + 版面文字稿（v2，deck 第 21 页）

> 本文件是 6.1 · MULTI-TARGET DESIGN CAMPAIGN 页的制作前置核对表与版面文字稿。 纪律：每个状态都必须有资料依据；无法确认的一律 Pending verification / Pending，不推断、不补造。 **v2（木木：表头和表格只用中文）**：列头改纯中文（靶点/设计进度/评价进度/报告中的作用）；状态词只保留中文（已完成/进行中/未开展/未发布）；题号中文化（第 1–5 题）；"binding ≠ activation"→"（结合 ≠ 激活）"。EGFR/TNF-α/GLP-1R/PD-L1/B7-1 为蛋白名保留。

---

## 一、五靶点状态核对表（制作依据）

|   |
| - |

\#

|   |
| - |

靶点

|   |
| - |

Design status

|   |
| - |

Evaluation status

|   |
| - |

资料依据

|   |
| - |

待确认

|   |
| - |

1

|   |
| - |

**EGFR**（Anthropic Ch1，09-28 发布）

|   |
| - |

**Completed**：候选设计与筛选完成（RFdiffusion→MPNN→Boltz 漏斗 939→104→20；最终 20 条候选按界面簇配额定稿）

|   |
| - |

**Completed**：benchmark 六组对照（人源 3 + 鼠源 3）完成；判据标定完成（质心判据统计检验 AUC 0.981；ipTM 证伪降为只报告）

|   |
| - |

04-EGFR 模块；`FINAL_6GROUP_benchmark_statistics_corrected.csv`；11-组内版 19/20（定稿 20 条）；09-质心判据统计检验-AUC0981

|   |
| - |

无重大待确认

|   |
| - |

2

|   |
| - |

**TNF-α**（Anthropic Ch2，10-05 发布）

|   |
| - |

**Completed（冷跑 #1）**：换靶冷跑第一次即 TNF-α（PDB 8ZUI），全链路验证完成（"除一个配置文件外不改代码"）

|   |
| - |

**In progress**：benchmark 四组对照完成；三聚体补充与双链受控重跑完成；实验参照比较为**阶段性结论**（定量叠合未做）

|   |
| - |

`TNF_control_report_summary_final.csv`；TNF-Boltz2 对照组验证；13-补充材料（冷跑系列 TNF-α n=1）；deck P16–P19

|   |
| - |

定量叠合未完成 → Evaluation 保持 In progress，不写 Completed

|   |
| - |

3

|   |
| - |

**GLP-1R**（Anthropic Ch3，10-12 公布；**我方不参赛**）

|   |
| - |

**Pending**（设计未开展；预分析已备：6X18 链 R ref_structure+表位、MSA 预跑 2h16m、agonist_conflict_scan 工具预留；**膜蛋白=未标定，阈值/判据不可迁移**——10-13 拍板）

|   |
| - |

**In progress**：功能性判据探索已开展——四种激动剂判据全部被对照否证（打乱序列 0.646 > 天然 GLP-1 0.457 等）；结论"静态结构置信度评价不能外推到功能性设计"

|   |
| - |

06-GLP1R/白话讲解-GLP1R判据战役；13-补充材料/表位与ref_structure-6X18链R；08-换靶点后阈值重标SOP（Ch3=GLP1R、膜蛋白未标定）；交接（我方不参赛）

|   |
| - |

无（判据否证是已定结论）

|   |
| - |

4

|   |
| - |

**Challenge 04 靶点**（10-19 发布）

|   |
| - |

**Pending**（尚未发布，名称未知）

|   |
| - |

**Pending**（同左）

|   |
| - |

修订规范/摘录-批量扩池README补遗（Ch4=10-19 发布）；07-其他靶点/README（占位）

|   |
| - |

10-19 发布后接入

|   |
| - |

5

|   |
| - |

**Challenge 05 靶点**（10-26 发布）

|   |
| - |

**Pending**（尚未发布）

|   |
| - |

**Pending**（同左）

|   |
| - |

同上（Ch5=10-26 发布）

|   |
| - |

10-26 发布后接入

### 补充证据（非五靶点，但属"多靶点探索"最硬证据）

- **换靶冷跑系列已完成 3 个靶点**：TNF-α（n=1）→ PD-L1/4ZQK（n=2，43 设计/3 通过/7.0%，66 min）→ B7-1/CD80（n=3，2/48，57 min）——验证"除一个配置文件外不改代码"的可迁移性；并在 PD-L1 冷跑实测"乱序阴性 ipTM 0.867 > 候选中位 0.744"，支撑 ipTM 降为只报告。

* 来源：13-补充材料（报告-第二次换靶点冷跑-PDL1）、07-其他靶点/B7-1（白话讲解-B7-1冷跑与MSA对照）。

- 页面处理：表格下方一行脚注带过，不展开（PD-L1/B7-1 非赛题靶点）。

### 状态词表（页面用）

Completed＝有资料证实该阶段完成；In progress＝有明确记录表明正在进行；Pending＝未完成/无结果/未发布；Pending verification＝资料不足暂无法确认（本页未用到）。

### 明确不写的内容

- 不写"五靶点均已完成设计/验证"；不写 GLP-1R 激动剂设计成功（Binding does not establish activation）；不写 TNF 评价 Completed（定量叠合未做）；不写 Ch4/Ch5 任何预设结果；不加成功率/排名/ROC。

---

## 二、版面逐区描述（v1）

■ **顶部眉行**：左 `6.1 · MULTI-TARGET DESIGN CAMPAIGN`（红 13pt 粗）；右 `AI-BINDERDESIGN · RESEARCH REPORT`（浅灰 10pt，按木木指令与其他页的 2026 角标不同）

■ **主标题区**

- 中文主标题（24pt 黑粗）：`从单一靶点到多靶点设计探索`

* 英文副题（Georgia 斜体 13pt 红）：`MULTI-TARGET DESIGN CAMPAIGN`

- 引导句（黑 11.5pt）：`以 EGFR 和 TNF-α 为主要研究案例，同时梳理其他靶点的设计与评价进展。`

■ **五靶点全景表**（**v2 表头/表格纯中文**；四列：靶点｜设计进度｜评价进度｜报告中的作用；列头红粗；行分隔浅灰线；EGFR/TNF 靶点名红粗、GLP-1R 黑、第 4/5 题浅灰）

|   |
| - |

靶点

|   |
| - |

设计进度

|   |
| - |

评价进度

|   |
| - |

报告中的作用

|   |
| - |

EGFR（第 1 题）

|   |
| - |

已完成

|   |
| - |

已完成

|   |
| - |

主要设计案例——候选设计与基准校准评价流程已建立

|   |
| - |

TNF-α（第 2 题）

|   |
| - |

已完成（换靶冷跑 #1）

|   |
| - |

进行中

|   |
| - |

主要基准评价案例——已知对照体系与指标判别问题

|   |
| - |

GLP-1R（第 3 题 · 我方不参赛）

|   |
| - |

未开展

|   |
| - |

进行中

|   |
| - |

探索性功能设计问题（结合 ≠ 激活）

|   |
| - |

第 4 题（10-19 公布）

|   |
| - |

未发布

|   |
| - |

未发布

|   |
| - |

待赛题公布后接入评估

|   |
| - |

第 5 题（10-26 公布）

|   |
| - |

未发布

|   |
| - |

未发布

|   |
| - |

待赛题公布后接入评估

- 表下脚注（浅灰 9pt）：`另：全流程换靶冷跑已完成 3 个靶点（TNF-α → PD-L1 → B7-1），验证「除一个配置文件外不改代码」的可迁移性。`

■ **底部总结带**（粉底；中文主句 14pt 粗 + 英文 Georgia 斜体 11pt 灰）

- `多靶点布局体现研究范围；可靠的评价结论仍取决于各靶点实际获得的证据。`

* `Project breadth defines the scope; evidence determines the strength of each conclusion.`

---

## 三、科学边界自查

|   |
| - |

禁止事项

|   |
| - |

落实

|   |
| - |

不虚构 Ch4/Ch5 结果

|   |
| - |

✅ 两行仅"待公布/Pending"

|   |
| - |

不把五靶点写成均已验证

|   |
| - |

✅ 状态分层：2 Completed / 2 In progress / 6 Pending（含 Ch4/5）

|   |
| - |

GLP-1R：Binding does not establish activation

|   |
| - |

✅ 角色列明示；不提激动剂设计成功

|   |
| - |

不把置信度解释成实验亲和力

|   |
| - |

✅

|   |
| - |

不把冷跑写成提交候选

|   |
| - |

✅ TNF 设计列标注"换靶冷跑 #1"性质

|   |
| - |

不新增临时章节/不改后续编号

|   |
| - |

✅ 追加为 deck 第 21 页，章节 6.1

---

## 四、制作信息

- **v1**（22:37）：初版（表头/状态带英文对照词）。

* **v2**（22:52，木木"表头和表格只用中文不用英文"）：列头、状态词、题号全部中文化（第 1–5 题）；GLP-1R 角色括注改"（结合 ≠ 激活）"；蛋白名（EGFR/TNF-α/GLP-1R/PD-L1/B7-1）保留。产物：run 级重写 20 shape → `Slides-26-MultiTarget-v2.pptx`，deck 第 21 页同步（英文残留检查为零）。

### assistant — `<UUID>` — 2026-10-17T15:02:20.749657+00:00

收到。这份 v2 已经把 **6.1 · MULTI-TARGET DESIGN CAMPAIGN** 的制作依据、页面文案和科学边界都明确了。后续应以这份稿为准：追加为 deck 第 21 页，不改 P1–P20，也不擅自增加章节。

正式定稿前，我建议先修正一个小问题：

**第三部分的状态数量统计与表格不一致。**

按五靶点表格逐项统计：

- **已完成：3 项**——EGFR 设计、EGFR 评价、TNF-α 设计。
- **进行中：2 项**——TNF-α 评价、GLP-1R 功能性判据探索。
- **未完成／未开展／未发布：5 项**——GLP-1R 设计，以及第 4、5 题的设计与评价。

因此，原文的“2 Completed / 2 In progress / 6 Pending”不应原样保留。建议直接改为中文统计，或者干脆删除这行计数，避免读者误以为它代表五个靶点的完成情况。

其他关键边界应继续保留：**TNF-α 评价仍为进行中；GLP-1R 的判据探索不等于激动剂设计成功；PD-L1 和 B7-1 只作为换靶可迁移性的补充证据，不计入五道赛题。**

接下来可以基于这份 v2 做最终核验，重点检查实际 PPT 的表格可读性、中文状态是否统一，以及文件是否确实追加在第 21 页。

### user — `<UUID>` — 2026-10-17T15:04:37.807000+00:00

如果只是这样的话这张PPT的内容是不是太少且无效了，就一个表格，里面填的还是已完成/进行中，唯一有效的信息就是**主要设计案例**——候选设计与基准校准评价流程已建立和**主要基准评价案例**——已知对照体系与指标判别问题

### assistant — `<UUID>` — 2026-10-17T15:04:41.106653+00:00

我同意，而且我觉得你指出的是这页真正的结构性问题：**它现在更像一张项目管理进度表，而不是一张能推进科研叙事的 PPT。**

如果观众看完只记住 EGFR 已完成、TNF-α 进行中、另外几个靶点尚未开展，那么这页对研究报告的贡献确实很有限。尤其前面已经讲过 EGFR 和 TNF-α 的具体工作，再把它们放进一张表里标记状态，信息增量很小。

但这不意味着 6.1 应该删除。它应该从“我们做了几个靶点”升级为一个更有价值的问题：

**这套设计与评价流程究竟在哪些不同靶点上得到过检验？这些检验分别证明了什么，又没有证明什么？**

## 我建议把这一页改成「多靶点迁移与验证边界」

不要让五行状态表成为主体，而是用三块证据，讲清楚三个不同层次的结论。

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="EGFR extracellular domain protein structure ribbon molecular visualization" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      <title size="md">01 · EGFR：建立完整设计与评价案例</title>
      <text color="secondary" size="sm">主设计案例</text>
      从 RFdiffusion、ProteinMPNN 到 Boltz-2 筛选，完成候选设计与筛选；通过六组人源、鼠源对照开展基准评价，并发现单独使用 ipTM 的局限。
      <text weight="medium">这证明了什么？</text>
      <text>建立了从候选生成到基准校准评价的完整工作流，而不是单纯生成候选序列。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="TNF alpha homotrimer protein molecular ribbon structure" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      <title size="md">02 · TNF-α：检验已知对照的判别能力</title>
      <text color="secondary" size="sm">主基准评价案例</text>
      使用已知结合体系、受体对照和阴性对照开展评估；进一步检查三聚体背景与受控重跑对结果解释的影响。
      <text weight="medium">这证明了什么？</text>
      <text>评价结论需要考虑对照体系和靶标结构背景；部分比较尚未完成定量叠合，因此结论仍有边界。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="PD-L1 protein structure ribbon molecular visualization" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      <title size="md">03 · PD-L1 / B7-1：检验流程迁移能力</title>
      <text color="secondary" size="sm">补充换靶实验</text>
      在 EGFR、TNF-α 之外，完成 PD-L1 和 B7-1 的换靶冷跑，记录了实际运行时间、设计筛选结果以及阴性对照表现。
      <text weight="medium">这证明了什么？</text>
      <text>工作流具备一定的跨靶点运行可迁移性，但这不等于已证明跨靶点的评价指标普遍有效。</text>
    </box>
  </row>
</box>

上面三个部分是内容结构示意，不是建议把它们原样做成三个带图片的卡片。正式 PPT 可以采用更紧凑的三列证据布局，并把数据放在显眼位置。

## 真正值得展示的，是下面这组证据

你目前提供的材料里，有三个比“已完成”更有说服力的结果：

<grid columns={3} gap={2}>
  <grid-item>
    <box border radius="lg" padding={3} gap={1}>
      <text color="secondary" size="xs">EGFR · 判据统计</text>
      <title size="2xl" color="default">0.981</title>
      <text weight="medium" size="sm">AUC</text>
      <text color="secondary" size="xs">质心判据统计检验；需在图注中说明具体任务和数据范围。</text>
    </box>
  </grid-item>
  <grid-item>
    <box border radius="lg" padding={3} gap={1}>
      <text color="secondary" size="xs">PD-L1 · 阴性对照</text>
      <title size="2xl" color="default">0.867</title>
      <text weight="medium" size="sm">乱序阴性 ipTM</text>
      <text color="secondary" size="xs">高于候选中位数 0.744，说明单独使用 ipTM 存在判别风险。</text>
    </box>
  </grid-item>
  <grid-item>
    <box border radius="lg" padding={3} gap={1}>
      <text color="secondary" size="xs">B7-1 · 换靶冷跑</text>
      <title size="2xl" color="default">2 / 48</title>
      <text weight="medium" size="sm">通过数量 / 设计数量</text>
      <text color="secondary" size="xs">用于说明实际筛选过程；不能单凭该比例推断结合成功率。</text>
    </box>
  </grid-item>
</grid>

这三组数据分别代表**判据区分能力、指标失效风险、流程跨靶点运行**。它们比简单的状态标签更能支撑科研叙事。

有一个重要限制：AUC 0.981 对应的具体统计任务、样本构成和判定方向，正式展示前仍应核对原始统计文件，不能把它直接解释成通用评价能力。

## 那么五靶点表格还要不要？

要，但应该降级成页脚或一条简短的研究范围说明。五道赛题的完整状态不必占据主体版面。

这页最重要的逻辑应当是：

<box border radius="lg" padding={3} gap={2} align="center">
  <title size="md" textAlign="center">多靶点探索带来的三层证据</title>
  <row gap={2} align="center" width="100%">
    <box background="surface-secondary" radius="md" padding={2} flex="1" align="center">
      <text weight="medium" textAlign="center">完整工作流</text>
      <text color="secondary" size="xs" textAlign="center">EGFR</text>
    </box>
    <icon name="plus" color="secondary" size="sm" />
    <box background="surface-secondary" radius="md" padding={2} flex="1" align="center">
      <text weight="medium" textAlign="center">评价边界</text>
      <text color="secondary" size="xs" textAlign="center">TNF-α</text>
    </box>
    <icon name="plus" color="secondary" size="sm" />
    <box background="surface-secondary" radius="md" padding={2} flex="1" align="center">
      <text weight="medium" textAlign="center">流程迁移</text>
      <text color="secondary" size="xs" textAlign="center">PD-L1 / B7-1</text>
    </box>
  </row>
  <icon name="arrow-down" color="secondary" size="lg" />
  <text weight="medium" textAlign="center">流程能够迁移，不代表评价指标可以直接迁移。</text>
</box>

我会把这句话作为这一页的核心结论，因为它能自然衔接前面的 EGFR、TNF-α 结果，也能引出后面的 **7 · MULTI-METRIC DECISION**：既然不同靶点上的评价结果不能不加区分地解释，就需要明确指标的适用范围、对照依据和多指标决策规则。

**我的建议是保留 6.1，但彻底改写内容结构：从“多靶点进度盘点”转成“跨靶点证据与迁移边界”。** 五靶点状态表只承担背景交代功能，不再作为整页主体。

### user — `<UUID>` — 2026-10-17T15:17:38.351000+00:00

AUC · 质心判据统计检验这个是啥

### assistant — `<UUID>` — 2026-10-17T15:17:41.374610+00:00

这里的 **“AUC · 质心判据统计检验”**，其实是把两个不同的概念放在了一起：一个是你们设计的**质心判据**，另一个是用来衡量判据区分能力的 **AUC**。

但我得先说明：仅凭你前面给出的 `AUC = 0.981`，我还不能确定这个 AUC 具体是怎么计算出来的，也不能直接断言它代表什么。需要看一下原始统计文件中的标签、预测分数和计算方式。

## 先把两个概念讲清楚

**1. 质心判据是什么？**

蛋白质结合界面由很多原子和残基组成。可以把某个界面区域简化成一个空间中心，也就是“质心”（centroid）。

如果你们的判据是基于质心距离或质心几何关系来区分阳性、阴性对照，那么它本质上是一个**几何特征判据**。不过，具体计算的是哪个质心、什么距离，以及距离大还是小更支持阳性，必须以你们实际实现为准，不能只凭名称推断。

**2. AUC 是什么？**

AUC 通常指 ROC 曲线下面积，用来衡量某个分数区分阳性与阴性样本的能力。

- AUC = 0.5：在常见二分类解释下，相当于随机排序水平。
- AUC 越接近 1：阳性样本与阴性样本越容易被该分数区分。
- AUC = 0.981：如果计算方法、标签和测试样本都合理，说明该分数在这批数据上具有很强的区分能力。

注意：**AUC 高不等于预测的结合亲和力高，也不等于候选物已经被实验验证。**

## 关键纠正：这个 0.9813 不是 EGFR 候选设计的 AUC

我查了你的资料库，找到 `09-质心判据统计检验-AUC0981-2026-10-13.md`。实际结果是：

- **测试体系：** 1BRS 对接基准。
- **数据规模：** 94,167 个可用的对接 decoy（即生成的候选对接姿态）。
- **阳性定义：** DockQ ≥ 0.23，共 78 个姿态。
- **结果：** 界面质心判据 AUC = 0.9813；质心与 DockQ 的 Spearman 相关系数为 −0.8506。<FileCite ref_id="turn2file0" />

它回答的问题是：

> **在这组对接姿态中，界面质心指标能否把接近天然结合姿态的结果，与大多数非近天然姿态区分开？**

答案是：在这个基准上，区分能力很强。

但有三条限制：

1. 这验证的是 **1BRS 对接姿态的排序能力**，不是你们 EGFR 从头设计候选的成功率。
2. 78 个阳性姿态只占约 0.083%；即使 AUC 很高，质心排名前 10% 的姿态中，近天然姿态占比也只有约 0.83%。
3. 该体系不能直接证明质心判据在抗体类结合剂或其他靶点上同样有效。<FileCite ref_id="turn2file0" />

因此，我上一条把它直接称作「质心判据统计检验」，又放在多靶点页面的 EGFR 数据卡中，容易让观众误以为它是 EGFR 项目内部得到的 AUC。这种呈现不够准确。

**如果要放进 PPT，建议改成：**

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" size="xs">独立对接基准 · 1BRS</text>
  <title size="2xl">AUC = 0.9813</title>
  界面质心能够有效区分该基准中的近天然与非近天然对接姿态。
  <divider color="subtle" />
  <text color="secondary" size="sm">94,167 个可用姿态；78 个满足 DockQ ≥ 0.23。该结果不代表从头设计候选的结合成功率，也不构成跨靶点验证。</text>
</box>

这样才不会把一项**独立基准上的方法学证据**误写成 EGFR 设计项目自身的验证结果。至于它是否值得放在第 21 页，还要看你想让这一页讲「多靶点迁移」，还是讲「质心判据的独立验证」——这两种叙事不应该混成一件事。

### user — `<UUID>` — 2026-10-17T15:20:43.929000+00:00

算了算了，这张先删掉，在不影响叙事的情况下直接MULTI-METRIC DECISION，后面如果有数据了再补

### assistant — `<UUID>` — 2026-10-17T15:21:25.969088+00:00

可以，**这张先删，不补替代页**。直接进入 `MULTI-METRIC DECISION`，叙事不会断，反而更紧凑。

后续主线调整为：

1. **EGFR / TNF-α 基准研究**：展示已知对照揭示的评分问题。
2. **7 · MULTI-METRIC DECISION**：从单一评分失效过渡到基于校准、多指标证据的候选筛选。
3. **8 · DISCUSSION**：讨论结构指标的适用边界与解释方式。
4. **9 · LIMITATIONS**：明确目前缺少的实验亲和力数据、基准覆盖不足等限制。
5. **10 · FUTURE WORK**：补充更多靶点、实验验证和指标校准。
6. **11 · CONCLUSION**：总结核心方法论。

多靶点进展暂时不单独占页。等 EGFR、TNF-α 之外有足够扎实的数据，再考虑补回；到时根据证据决定是独立成页，还是放进补充材料。

**注意：这里只确定叙事与删页方案，还没有实际修改 PPT 文件。**现有的 `MULTI-METRIC DECISION` 内容沿用 `Slides-09`，不需要为删页重新设计。

### user — `<UUID>` — 2026-10-17T15:24:08.506000+00:00

讲一下MULTI-METRIC DECISION是在干什么，提示词

### assistant — `<UUID>` — 2026-10-17T15:24:11.868636+00:00

`MULTI-METRIC DECISION` 这一页的核心任务，是把前面基准实验发现的评分问题，转化成一套更可靠的候选筛选决策流程。

它不是再介绍一遍 PAE、ipTM、pDockQ2 等指标的定义，也不是简单地把几个分数加权求和，而是要回答一个关键问题：

**当单一指标无法可靠地区分已知结合体与阴性对照时，我们应该如何综合证据，决定哪些候选值得优先考虑？**

## 这一页具体要讲什么？

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">01</title>
    </box>
    <box flex="1" gap={1}>
      **BEFORE · 单一指标筛选**

      过去容易根据 ipTM 等单一分数给候选排序。但前面的基准实验表明，阴性对照也可能获得很高的分数，因此“分数高”不能直接等同于“更可能结合”。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">02</title>
    </box>
    <box flex="1" gap={1}>
      **CALIBRATION · 先校准指标**

      用已知阳性、阴性对照检查各项指标是否真的有区分能力，明确哪些指标可以用于筛选、哪些只能作为辅助参考。不能直接把一个靶点的阈值照搬到另一个靶点。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">03</title>
    </box>
    <box flex="1" gap={1}>
      **AFTER · 多指标综合决策**

      综合结构可信度、界面接触、界面几何等相互补充的证据，并设置必要的质量门槛。先排除明显不合格的候选，再对剩余候选进行比较和排序。
    </box>
  </row>
</box>

最终需要让观众理解：**不是指标越多越好，而是每个指标都要有明确的证据作用；未经验证的指标不能因为数值漂亮就主导决策。**

这页也要守住科学边界：多指标筛选只能帮助确定优先验证的候选，不能证明它们一定会结合，更不能代替实验亲和力或功能验证。

## 给 WorkBuddy 的制作提示词

下面这版重点是让它**沿用现有 `Slides-09` 的内容进行改造，而不是凭空重做一套方法**。

<WritingBlock id="58317" variant="document">请制作主报告第 **7 页：MULTI-METRIC DECISION**，主题为“从单一评分到多指标综合决策”。

### 一、页面任务

承接前面的基准实验结果，回答：

**既然单一指标无法可靠地区分已知结合体和阴性对照，我们应该如何改进候选筛选？**

本页是从“发现评分失效”过渡到“建立更合理的筛选决策”的方法论总结，不是指标科普页，也不是新的实验结果页。

### 二、素材与数据要求

1. 优先复用现有 `Slides-09` 页面中的内容、图表和视觉素材，调整标题、结构与措辞即可。
2. 页面编号使用 `7 · MULTI-METRIC DECISION`。
3. 不新增未经现有数据支持的数值、阈值、成功率、权重或性能提升结论。
4. 不将 AUC = 0.9813 描述为 EGFR 候选筛选结果；该结果来自独立的 1BRS 对接基准。
5. 不宣称多指标综合评分已经被实验验证，也不把结构预测分数等同于真实结合亲和力。

### 三、核心版式

采用清晰的横向三阶段结构：

**BEFORE → CALIBRATION → AFTER**

**左侧：BEFORE — 单一指标筛选**

- 根据单个分数进行候选排序。
- 高分不一定代表真实结合。
- 已知阴性对照可能获得较高的结构预测分数。

视觉重点：突出“单一分数不足以支持可靠判断”，不要堆砌案例数字。

**中间：CALIBRATION — 基准校准**

- 使用已知阳性、阴性对照检验指标的区分能力。
- 明确各指标的适用范围和证据作用。
- 将未经验证的指标降级为辅助参考。
- 不默认不同靶点共享相同阈值。

视觉重点：表现从“直接相信分数”转向“先检验指标是否有效”。

**右侧：AFTER — 多指标综合决策**

- 质量门槛：排除明显不符合基本要求的候选。
- 多指标证据：综合结构可信度、界面接触和界面几何等互补信息。
- 候选排序：依据可解释的证据确定后续优先验证对象。

注意：只有现有项目数据实际支持的指标才可以列入具体决策流程。不要为了凑齐指标而加入未经验证的指标，也不要把多指标简单等同于未经校准的加权求和。

### 四、页面结论

页面底部突出一句核心结论：

**从追求高分，转向判断证据是否可靠。**

英文辅助句：

*From score maximization to evidence-based candidate selection.*

可以辅以一句较小的边界说明：

*Structural evidence prioritizes candidates; experimental validation establishes binding and function.*

### 五、视觉规范

- 中文为主要信息，英文作为标题、阶段标签和简短辅助说明。
- 保持科研汇报风格，简洁、克制、证据导向。
- 三个阶段形成明确的视觉递进，避免大段文字和过多装饰。
- 保留前后页面已有的字体、配色、边距和版式语言。
- 不新增独立的指标定义表，不重复前文的基准实验细节。

### 六、完成标准

观众看完后应当能够清楚回答：

1. 为什么不能只看一个分数？
2. 基准校准解决了什么问题？
3. 多指标决策如何帮助筛选候选？
4. 为什么筛选结果仍然需要实验验证？

请直接在现有报告中修改对应页面，不要擅自增加新页或调整其他章节顺序。</WritingBlock>

制作时最重要的是：**这页讲决策逻辑，不是宣称已经建立了一套经过实验验证的万能评分系统。**如果现有 `Slides-09` 中有具体流程图或指标表，先保留有数据支撑的部分，再围绕这条逻辑调整。

### user — `<UUID>` — 2026-10-17T15:47:13.949000+00:00

换靶冷跑是什么意思

### assistant — `<UUID>` — 2026-10-17T15:47:17.578664+00:00

“**换靶冷跑**”是你这个 AI-BinderDesign 项目里用的工程术语，可以拆成两部分理解：

- **换靶**：把设计流程的目标蛋白换成另一个靶点，例如从 EGFR 换成 TNF-α、PD-L1 或 B7-1。
- **冷跑**：在新靶点上重新启动一轮完整流程，检验现有工作流能否运行，而不是只展示之前已经调通的结果。

## 举个你项目里的例子

<box border radius="xl" padding={3} gap={3}>
  <row align="center" gap={3}>
    <AsyncImage query="EGFR extracellular domain protein structure ribbon" aspectRatio="1:1" maxWidth="76px" />
    <box flex="1" gap={1}>
      **第一轮：EGFR**

      <text color="secondary" size="sm">建立并调试设计与评价流程，形成主要研究案例。</text>
    </box>
  </row>
  <row justify="center">
    <icon name="arrow-down" size="xl" color="secondary" />
    <text color="secondary" size="sm">更换靶点，修改对应配置</text>
  </row>
  <row align="center" gap={3}>
    <AsyncImage query="TNF alpha trimer protein structure ribbon" aspectRatio="1:1" maxWidth="76px" />
    <box flex="1" gap={1}>
      **第二轮：TNF-α**

      <text color="secondary" size="sm">重新运行流程，检查是否需要修改代码、哪些步骤能够复用，以及评价方法是否仍然适用。</text>
    </box>
  </row>
  <row justify="center">
    <icon name="arrow-down" size="xl" color="secondary" />
    <text color="secondary" size="sm">继续更换靶点</text>
  </row>
  <row align="center" gap={3}>
    <AsyncImage query="PD-L1 protein extracellular domain ribbon structure" aspectRatio="1:1" maxWidth="76px" />
    <box flex="1" gap={1}>
      **后续轮次：PD-L1、B7-1**

      <text color="secondary" size="sm">进一步检查工作流在其他蛋白上的可迁移性。</text>
    </box>
  </row>
</box>

## 为什么要做换靶冷跑？

它主要检验两个不同的问题：

| 检验的问题 | 能说明什么 |
|---|---|
| 换靶后能否运行，是否只需修改配置？ | **流程可迁移性**：软件流程是否容易复用 |
| 换靶后原来的评分标准是否仍有效？ | **评价方法可迁移性**：原有指标和阈值是否仍有区分能力 |

这两件事不能混为一谈。

例如，你的 TNF-α、PD-L1 冷跑中都出现过阴性对照的 ipTM 高于某些候选的情况。这说明即使工作流能在新靶点上运行，也不代表 ipTM 就能可靠地区分结合体与非结合体。

还有一点：**冷跑成功不等于设计成功，更不等于实验验证成功。**它首先证明的是流程能够在新任务上执行；候选质量和评价方法的有效性，需要分别用数据检验。

如果写进正式 PPT，我建议不用“冷跑”这个口语词，改成：

**跨靶点工作流迁移测试（Cross-target Pipeline Transfer Test）**

这样导师一眼就能理解，也不会误以为是某种特定的蛋白设计算法。

### user — `<UUID>` — 2026-10-17T15:48:19.570000+00:00

1BRS barnase–barstar这又是什么

### assistant — `<UUID>` — 2026-10-17T15:48:27.632839+00:00

**1BRS（Barnase–Barstar）是一个蛋白质复合物的 PDB 结构编号**，对应的是一对经典的蛋白质相互作用体系：

- **Barnase**：一种来自细菌的核糖核酸酶。
- **Barstar**：能够与 Barnase 紧密结合、抑制其酶活性的蛋白质抑制剂。

两者结合形成的复合物，经常被用于研究蛋白质之间的识别、结合界面，以及计算方法能否正确预测蛋白质复合物的结构。

<AsyncImageGroup query={["barnase barstar complex PDB 1BRS protein structure ribbon two chains","barnase barstar protein protein interface molecular structure"]} aspectRatio="5:4" layout="bento" />

对你的 AI-BinderDesign 项目来说，它的重要性不在于它是一个待设计的靶点，而在于它可以作为一个**独立的蛋白质对接基准**，用来检验某种界面评价指标是否能区分结构合理的对接姿态与不合理的姿态。

## 它和你项目里的 AUC = 0.9813 有什么关系？

你之前的统计结果，是在 **1BRS 的对接姿态基准**上评估界面质心判据的区分能力，而不是在 EGFR 从头设计候选上做的实验。

- **基准数据**：94,167 个可用对接姿态。
- **正例定义**：DockQ ≥ 0.23，共 78 个姿态。
- **结果**：AUC = 0.9813，Spearman 相关系数 = −0.8506。
- **意义**：该界面质心指标在这个特定基准中，能够较好地区分近天然姿态与其他姿态。

这里的 1BRS 是结构来源，DockQ 是判断预测复合物与参考结构相似程度的指标，AUC 则衡量判别指标区分正负样本的能力。<Cite refs={["turn751933search0","turn751933search2"]}/>

**但要特别注意：**这只能支持“该指标在 1BRS 对接基准上表现良好”，不能直接证明它能识别真正的 de novo binder，更不能说 EGFR 候选的结合成功率达到 98.13%。

如果在 PPT 中提到它，建议称为：

> **独立结构对接基准（1BRS Barnase–Barstar）上的指标判别验证**

而不要把它写成 EGFR 设计结果或多靶点泛化验证。

### user — `<UUID>` — 2026-10-17T15:50:11.427000+00:00

PD-L1和B7-1是什么关系

### assistant — `<UUID>` — 2026-10-17T15:50:16.845558+00:00

## 它们的关系可以这样理解

<box border radius="xl" padding={3} gap={2}>
  <box align="center" gap={1}>
    <box background="#E8F2FF" theme="light" radius="lg" padding={3} width="80%">
      <title size="md" textAlign="center" color="#174EA6">PD-L1</title>
      <text textAlign="center" size="sm">免疫检查点配体</text>
    </box>
    <icon name="arrow-down-up" size="xl" color="secondary" />
    <box background="#E6F6EB" theme="light" radius="lg" padding={3} width="80%">
      <title size="md" textAlign="center" color="#176B3A">B7-1（CD80）</title>
      <text textAlign="center" size="sm">参与调节 T 细胞活化的免疫分子</text>
    </box>
    <text size="sm" color="secondary" textAlign="center">两者可以直接相互作用，影响免疫调控。<Cite refs={["turn237615search0","turn237615search2"]}/></text>
  </box>
</box>

此外，B7-1 还会与 **CD28** 和 **CTLA-4** 结合，而 PD-L1 的经典结合对象是 **PD-1**。所以它们不是简单的“受体—配体”单一路径，而是处在相互关联的免疫调控网络中。

## 为什么你项目里会分别跑 PD-L1 和 B7-1？

在 AI-BinderDesign 中，它们是两个不同的蛋白靶点。把设计工作流从 PD-L1 换到 B7-1，可以检验流程能否迁移到另一种蛋白上。

但有一个很重要的区别：

- **工程层面**：在两个靶点上都能运行，支持工作流具有一定可迁移性。
- **生物学层面**：PD-L1 与 B7-1 本来就存在相互作用，因此不能把针对它们的结果简单当作两个完全独立、互不相关的靶点验证。
- **评价层面**：即使两个靶点上的结构预测都运行成功，也不能据此认定同一评分指标在两者上都可靠。

关于两者的结合，文献还讨论了它们在同一细胞膜上的顺式相互作用（*cis*）；其具体结合模式与功能解释仍需要结合实验体系判断。<Cite refs={["turn237615search1","turn237615search3"]}/>

**对你的汇报最有用的一句话：**PD-L1 和 B7-1 既是不同的设计靶点，也是具有已知生物学关联的蛋白对；因此，换靶冷跑能说明工作流是否可复用，但不能单独证明评价标准具有普遍性。

### user — `<UUID>` — 2026-10-17T15:51:11.112000+00:00

# 【幻灯片文字稿】7 · MULTI-METRIC DECISION（v1）

> 用途：供无法打开 PPT 文件的审阅者使用。按版面从上到下、从左到右逐区块描述。 对应文件：Slides-27-MultiMetricDecision-v1.pptx（16:9，白底，主色交大红） 已并入主 deck 第 21 页（该页此前为空白页，原地重画，未新增页、未调整其他章节顺序）

---

■ **眉行**（左上，红 13pt 粗） `7 · MULTI-METRIC DECISION　｜　从单一评分到多指标综合决策`

■ **右上**（浅灰 10pt） `AI-BINDERDESIGN · RESEARCH REPORT`

■ **主标题**（黑 24pt 粗） `从单一评分到多指标综合决策` └ 红色斜体副题（Georgia 13pt）：`From score maximization to evidence-based decision`

■ **导语**（黑 11.5pt） `EGFR 与 TNF-α 两个案例反复指向同一件事：分数高低本身，不足以判断一个候选是否值得继续往下做。`

---

■ **三阶段横向结构**（三张白卡，左侧竖色条由浅到深：灰 → 红 → 深灰，中间以 ▸ 串联）

**卡 01 · BEFORE｜单一指标筛选**（左条浅灰，小标：起点 · 依赖模型默认排序）

- 按模型输出的单一置信度分数排序，取高分作为候选

* 高分不等于真实结合：分数只说明预测结构自洽

- 阴性对照同样可能获得高分（见下方数据）

* 低分也不能直接判定为不结合

- 数据落点（灰 23pt 粗）：`0.867` —— 换靶冷跑中，乱序阴性序列的 ipTM 高于候选中位 0.744

* 脚注（浅灰 8pt）：该数值来自 PD-L1 / B7-1 换靶冷跑记录，仅用于说明单一指标排序的风险。

- 卡底 chip：`分数高 ≠ 证据强`

**卡 02 · CALIBRATION｜用已知对照校准**（左条交大红，小标：转折 · benchmark calibration）

- 用已知阳性、阴性对照，检验各指标的实际区分能力

* 明确适用范围：结论只在该基准体系内成立

- 未通过检验的指标降级使用：只报告，不作判据

* 阈值不跨靶点照搬

- 数据落点（红 23pt 粗）：`0.9813` —— AUC · 质心判据在独立 1BRS 盲对接基准上的区分能力

* 脚注（浅灰 8pt）：该 AUC 来自独立的 1BRS barnase–barstar 盲对接基准（94,167 个 decoy，其中 78 个正样本），是对质心判据区分能力的检验，**不是 EGFR 候选筛选结果**。

- 卡底 chip：`先校准，后使用`

**卡 03 · AFTER｜多指标综合决策**（左条深灰，小标：结果 · evidence-based decision）

- `01 质量门槛` —— 先筛除明显不可信的预测

* `02 多指标证据` —— 结构可信度 · 界面接触 · 界面几何

- `03 候选排序` —— 按证据一致性确定优先验证的顺序

* 限定句（浅灰 8.5pt）：排序结果只决定先验证谁，不代表结合已被证明；实验验证仍然是判断结合与功能的依据。

- 卡底 chip：`面向优先验证，不替代实验`

---

■ **边界说明**（居中，浅灰 9pt + Georgia 斜体） `说明：结构证据用于确定优先验证的对象；结合与功能仍需实验验证。Structural evidence prioritizes candidates; experimental validation establishes binding and function.`

■ **底部结论带**（粉底红边圆角条）

- 主句（红 16pt 粗，居中）：`从追求高分，转向判断证据是否可靠。`

* 英文副句（Georgia 10pt 斜，居中）：`From score maximization to evidence-based candidate selection.`

---

### 本页要回答的问题与边界

**回答什么**：经验如何改变候选筛选？（第 6 章多靶点经验之后的方法论落点）

**三段逻辑**：

1. **BEFORE** —— 单一指标排序为什么不够：分数只反映预测自洽，不反映结合；阴性对照也能拿高分；低分也不能反向证明不结合。

1) **CALIBRATION** —— 用已知阳性/阴性对照检验指标的实际区分能力，明确适用范围，未通过检验的指标降级，阈值不跨靶点照搬。

1. **AFTER** —— 质量门槛 → 多指标证据（结构可信度 / 界面接触 / 界面几何）→ 候选排序，排序只决定优先验证顺序。

**诚信边界（本页不得越线）**：

- 不声称多指标决策"更准确"或提高成功率；只说降低对单一分数的依赖。

* `0.9813` 是**独立 1BRS 盲对接基准**上质心判据的 AUC，**不是 EGFR 候选筛选结果**，页面已用脚注明确标注。

- `0.867` 是换靶冷跑中阴性对照的 ipTM 观测值，用于说明单一指标风险，不代表对应靶点筛选结论。

* 无通用 cutoff 数值、无虚构候选排名；AFTER 卡为方法描述，不是结果展示。

- 不写"替代实验验证"；结构证据只用于确定优先验证对象。

### assistant — `<UUID>` — 2026-10-17T15:51:26.264645+00:00

这版整体逻辑已经成立，可以作为第 7 页的制作稿。不过，我建议**正式定稿前修改三个地方**，尤其是 `0.867` 的归属和 `0.9813` 的展示方式。

## 我认为需要调整的 3 处

**1. `0.867` 不要笼统写成“换靶冷跑中”**

你前面整理过的记录里，PD-L1 冷跑出现过乱序阴性 ipTM `0.867`，高于候选中位数 `0.744`。建议明确标出靶点和比较对象，避免观众误以为这是 PD-L1 与 B7-1 两个靶点都观察到的结果。

推荐写法：

> **0.867**｜PD-L1 冷跑中，乱序阴性对照的 ipTM 高于候选中位数 0.744。

前提是原始数据表确认这两个数字确实来自同一轮、同一评价设置。

**2. `0.9813` 的视觉权重可以降低**

它来自独立的 1BRS 对接基准，而不是 EGFR 或 TNF-α 的候选筛选结果。虽然脚注已经解释清楚，但把它作为中间卡片的红色大数字，仍容易让观众把它理解成整个项目的核心性能指标。

更稳妥的做法是把中间卡片的主视觉放在“已知对照校准”上，将 `AUC = 0.9813` 放入较小的证据注释区，并明确标注“独立对接基准”。如果本页空间紧张，也可以把这个结果放到附录。

**3. AFTER 不要让人误以为这套完整决策规则已经全部验证**

目前这段：

> 质量门槛 → 多指标证据 → 候选排序

适合作为方法框架，但应明确这是根据基准分析形成的筛选思路，而不是已经证明能够提高成功率的完整算法。

可以在卡片底部加一句：

> 方法框架：用于组织候选筛选证据，实际判别能力仍需逐靶点验证。

## 建议保留的核心结构

<box border radius="xl" padding={3} gap={3}>
  <box gap={1}>
    <text color="secondary" size="xs" weight="medium">BEFORE</text>
    <title size="lg">单一分数不能代表结合证据</title>
    <text size="sm">阴性对照也可能获得高分；高分不等于真实结合。</text>
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <text color="#C62828" size="xs" weight="medium">CALIBRATION</text>
    <title size="lg">先检验指标，再决定如何使用</title>
    <text size="sm">通过已知阳性、阴性对照评估区分能力，并限制结论的适用范围。</text>
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <text color="secondary" size="xs" weight="medium">AFTER</text>
    <title size="lg">综合证据，确定优先验证顺序</title>
    <text size="sm">结合质量门槛、结构可信度和界面信息进行筛选，但不宣称实验成功率已经提高。</text>
  </box>
</box>

**最终判断：**这页最有价值的不是展示两个漂亮的数字，而是把研究发现转化成明确的方法论：先验证评分是否有判别能力，再用适用范围明确的证据筛选候选。`0.867` 是项目中的具体反例，`0.9813` 是独立基准上的方法学证据，两者需要清楚区分，不能共同包装成同一套系统的性能成绩。

### user — `<UUID>` — 2026-10-17T16:08:24.585000+00:00

1BRS Barnase–Barstar：质心判据 AUC = 0.9813（94,167 个对接姿态，正例 DockQ ≥ 0.23，78 个；Spearman ρ = −0.8506）这句话什么意思

### assistant — `<UUID>` — 2026-10-17T16:08:29.491379+00:00

这句话的意思是：**研究者拿一个已知的蛋白质复合物 1BRS，生成了大量不同的对接姿态，然后测试“界面质心判据”能不能把接近真实结构的姿态排在前面。结果显示，它在这个特定基准上有很强的区分能力。**

我们把这句话拆开来看。

## 1. 先理解整个实验在做什么

<box gap={2}>
  <row align="start" gap={3}>
    <AsyncImage query="PDB 1BRS barnase barstar protein complex ribbon structure" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **① 1BRS：已知的蛋白质复合物**

      Barnase 和 Barstar 是一对已知会结合的蛋白质。研究者知道它们真实结合时的参考结构，因此可以用这个结构判断计算机生成的对接姿态有多接近真实结合构象。
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <AsyncImage query="protein protein docking decoy poses superimposed structural models" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **② 94,167 个对接姿态：大量候选结构**

      可以把它们理解成计算机提出的 94,167 种蛋白质相对摆放方式。它们是结构姿态，不是 94,167 种真实结合蛋白，也不是实验测得的结合结果。
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <AsyncImage query="protein protein interface molecular surface close contact structure" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **③ 质心判据：给每个姿态打分**

      根据蛋白质结合界面上相关原子或残基的空间分布，计算界面质心相关的几何指标，再用它对不同姿态进行区分或排序。具体是质心距离还是其变换分数，要以你实际使用的判据公式为准。
    </box>
  </row>
</box>

## 2. 这些数字分别是什么意思？

<box border radius="xl" padding={3} gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **94,167 个对接姿态**
      <title size="lg" color="default">总样本数</title>
    </row>
    <text color="secondary" size="sm">参与这次基准评价的可用对接结构总数。</text>
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <row align="center" justify="between">
      **78 个正例**
      <title size="lg" color="default">约 0.083%</title>
    </row>
    <text color="secondary" size="sm">按照 DockQ ≥ 0.23 的规则，78 个姿态被标记为正例。这里的“正例”指结构接近程度达到了预设标准，不是实验上证实了结合。</text>
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <row align="center" justify="between">
      **AUC = 0.9813**
      <title size="lg" color="default">接近 1</title>
    </row>
    <text color="secondary" size="sm">衡量判据区分正例与负例的能力。按通常的 ROC-AUC 解释，随机抽取一个正例和一个负例时，指标约有 98.13% 的概率把正例排在更有利的位置（具体取决于分数方向与实现）。</text>
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <row align="center" justify="between">
      **Spearman ρ = −0.8506**
      <title size="lg" color="default">强负相关</title>
    </row>
    <text color="secondary" size="sm">如果质心指标数值越小代表姿态越好，那么它与 DockQ 呈强负相关：质心指标越小，DockQ 通常越高。负号反映方向，不代表效果差。</text>
  </box>
</box>

## 3. AUC = 0.9813 是不是意味着 98.13% 的姿态预测正确？

**不是。** 这是最容易误解的地方。

AUC 衡量的是正负样本的整体排序区分能力，不是分类准确率，也不是结合成功率。

在这份基准中，正例只有 78 个，占全部姿态约 0.083%。因此，即使 AUC 非常高，也不能直接推导出：

- 98.13% 的姿态都接近真实结构；
- 98.13% 的设计蛋白都能结合；
- 这个判据在 EGFR、TNF-α 或其他靶点上也同样有效。

它能支持的结论更具体：**在 1BRS 这个对接基准中，界面质心判据对接近参考结构的姿态具有很强的区分能力。**

## 4. 这与 AI-BinderDesign 项目有什么关系？

你项目中的核心问题是：结构预测指标能否区分已知阳性和阴性对照，以及能否用于候选筛选。

1BRS 这组结果属于**独立的方法学验证**，可以作为“某个几何判据确实能够在特定基准上表现出区分能力”的证据。但它不是 EGFR 候选的直接验证，也不能证明该判据对从头设计的 binder 普遍有效。

如果要在 PPT 中用一句话讲清楚，我建议写成：

> **独立对接基准（1BRS）验证：界面质心判据能够有效区分该基准中的近天然与非近天然对接姿态（AUC = 0.9813，n = 94,167）。该结果不代表从头设计候选的结合成功率，也不构成跨靶点验证。**

这既保留了有价值的结果，也准确限定了它能说明什么、不能说明什么。

### user — `<UUID>` — 2026-10-17T16:12:51.048000+00:00

下一张

### assistant — `<UUID>` — 2026-10-17T16:12:59.935050+00:00

下一张是 **P22 · 8 DISCUSSION（讨论）**。承接刚才的 `MULTI-METRIC DECISION`，这一页不再讲如何筛选，而是讨论：**这些结果究竟说明了什么，以及结论的边界在哪里。**

## 第 8 页应该讲什么？

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">01</title>
    </box>
    <box flex="1" gap={1}>
      **单一评分为什么不可靠**

      高 ipTM 不一定意味着真实结合。阴性对照也可能得到较高分数，因此不能只根据一个分数判断候选质量。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">02</title>
    </box>
    <box flex="1" gap={1}>
      **评价指标具有适用边界**

      一个指标在特定基准上表现良好，不代表它对所有靶点、所有蛋白质复合物和所有设计任务都有效。1BRS 的 AUC = 0.9813 就是独立对接基准结果，而不是 EGFR 设计成功率。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <title size="lg">03</title>
    </box>
    <box flex="1" gap={1}>
      **结构可信度不等于实验亲和力**

      结构预测可以帮助判断候选是否值得继续研究，但无法单独证明真实结合，更不能直接证明激动、抑制等生物学功能。
    </box>
  </row>
</box>

## 给 WorkBuddy 的制作提示词

<WritingBlock id="62841" variant="document">请制作主报告第 8 页：**DISCUSSION｜讨论**，对应 deck 第 22 页。

### 页面定位
承接第 7 页 MULTI-METRIC DECISION。本页从“如何综合证据筛选候选”进一步讨论“这些证据可以支持什么结论，以及不能支持什么结论”。

优先复用现有报告中已制作的 Discussion 素材，不新增未经验证的数据，不调整其他章节顺序。

### 页面标题
眉行：`8 · DISCUSSION`
中文主标题：`结构证据能告诉我们什么？`
英文副标题：`What Structural Evidence Can—and Cannot—Tell Us`

### 核心内容
采用三个简洁的讨论区块：

**01｜单一指标的局限**
- 高 ipTM 不等于真实结合。
- 已知阴性对照也可能获得较高的结构预测分数。
- 因此，不能根据单一指标直接认定候选成功或失败。

**02｜评价结论依赖基准与任务**
- 指标的区分能力需要通过已知对照检验。
- 独立基准上的良好表现不能直接外推到 EGFR、TNF-α 或其他靶点。
- 1BRS 的 AUC = 0.9813 属于独立对接基准，不是 EGFR 候选设计结果；如展示该数字，必须明确标注来源和适用范围。

**03｜结构预测与生物学功能之间的距离**
- 结构可信度和界面几何属于计算证据。
- 它们不能单独证明实验结合亲和力，也不能证明受体激动或抑制功能。
- 候选排序用于确定优先验证对象，最终结论需要实验支持。

### 页面总结句
中文：`结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束。`

英文：`Structural evidence guides candidate prioritization, not experimental proof.`

### 视觉要求
- 中文为主要信息，英文仅作辅助。
- 白底、交大红作为强调色，沿用全 deck 的字体、边距和视觉语言。
- 用三个区块呈现“指标局限—适用边界—实验验证”的递进关系。
- 不重复第 7 页的完整三阶段流程，不再讲解 AUC、ipTM 等指标的定义。
- 不宣称多指标策略已被证明能够提高成功率。
- 不增加新数据、虚构实验结果或未经验证的普遍性结论。

完成后保持原有 deck 页数与章节顺序不变。</WritingBlock>

这一页的作用是把方法论的意义讲清楚；下一页 `9 · LIMITATIONS` 再正式列出当前项目的具体不足，两页不要写成重复内容。

### user — `<UUID>` — 2026-10-17T16:33:44.843000+00:00

以现有数据，后面几张都能做完吗

### assistant — `<UUID>` — 2026-10-17T16:33:48.971013+00:00

**可以，后面几张基本都能完成，不需要为了凑齐内容再去做一轮新实验。** 但要区分两件事：PPT 页面能不能完成，以及页面中的每个结论是否都有充分数据支撑。

按我们目前梳理的 AI-BinderDesign 项目材料，后半部分的主线是：

- **7 · MULTI-METRIC DECISION**：解释如何从单一评分转向基准校准与多指标证据。
- **8 · DISCUSSION**：解释这些结果意味着什么。
- **9 · LIMITATIONS**：明确现有证据的不足。
- **10 · FUTURE WORK**：提出下一步如何补足证据。
- **11 · CONCLUSION**：总结研究贡献。
- **ACK & AUTHOR CONTRIBUTIONS**：交代团队贡献。

这几页主要是对已有结果进行解释、限定和总结，不要求每页都产生新数据。

## 逐页判断：哪些能直接做，哪些需要谨慎

| 页面 | 能否完成 | 现有材料能支撑什么 |
|---|---|---|
| **8 · DISCUSSION** | <badge color="success">可以</badge> | 讨论单一 ipTM 的局限、基准校准的意义，以及结构预测与真实结合之间的差别。 |
| **9 · LIMITATIONS** | <badge color="success">可以</badge> | 明确目前主要是计算证据、缺少完整的实验 \(K_d\) 数据、基准范围有限、跨靶点泛化仍需验证。 |
| **10 · FUTURE WORK** | <badge color="success">可以</badge> | 根据现有缺口提出后续工作：扩充生物学对照、完善 TNF 三聚体与受体情境分析、开展实验验证、测量亲和力与功能。 |
| **11 · CONCLUSION** | <badge color="success">可以</badge> | 总结研究问题、基准校准思路，以及不能将结构置信度等同于结合证据的核心认识。 |
| **ACK & AUTHOR CONTRIBUTIONS** | <badge color="warning">需核实</badge> | 可以排版，但团队成员、个人职责和致谢对象必须以真实贡献记录为准，不能自行推断。 |

## 现有数据已经足够支撑核心叙事

例如，EGFR 基准中的结果已经能说明为什么不能只看 ipTM：

- 小鼠 EGFR：已知结合体 7D12 的 ipTM 为 **0.417**，而两个乱序阴性对照分别为 **0.812** 和 **0.846**。
- 人源 EGFR：7D12 的 ipTM 为 **0.622**，两个乱序阴性对照分别为 **0.665** 和 **0.706**。

这些结果可以支持一个明确的结论：**在这些特定对照中，单一 ipTM 排序无法可靠地区分已知结合体与阴性对照。**

但不能进一步宣称 ipTM 在所有靶点上都失效，也不能据此声称多指标方法已经提高了实验成功率。

另外，1BRS 上的 AUC = 0.9813 可以作为独立的结构对接基准证据，但不能包装成 EGFR 设计性能；TNF-α 的实验参考结构定量叠合尚未完成，也应在相关页面中如实保留这一限制。

## 我建议接下来的制作顺序

1. **Discussion**：解释现有结果意味着什么。
2. **Limitations**：明确哪些结论尚不能成立。
3. **Future Work**：让每一项后续工作都对应一个具体缺口。
4. **Conclusion**：收束成三条最重要的研究认识。
5. **Acknowledgments & Author Contributions**：最后核实真实贡献并制作。

这样不需要为了填满页面临时补实验，也不会让报告显得只有结论、缺少边界。

**总体判断：后面五张都可以推进到完整的汇报稿；真正需要额外核实的主要是贡献归属，以及个别结果的证据状态，而不是再找一批新数据。**

### user — `<UUID>` — 2026-10-18T01:43:48.121000+00:00

8 · DISCUSSION｜讨论
页面位置：主 deck 第 22 页（P22），承接第 21 页（7 · MULTI-METRIC DECISION），后接第 23 页（9 · LIMITATIONS）。
版式文件：Slides-29-Discussion-v1.pptx（单页存档），生成脚本 _gen_80discussion_v1_slide.py。
版面语言：完全沿用第 21 页——眉行（8 · DISCUSSION ｜ 讨论 + 右上角标）、24pt 中文主标题、Georgia 12pt 英文副题、12pt 导语、三张等宽白卡（3.70 in，圆角 0.04，左侧竖色条）、卡底 PANEL 色 chip、粉底结论带（PINKP + PINKL 边）、底部细线。
一、数据层（逐条 + 来源）
#
页面文字
类型
来源 / 依据
1
高 ipTM 不等于真实结合
团队结论（方法论判断）
由 P3/P9/P10 的 EGFR 案例与 P14/P15 的 TNF-α 案例共同支持；非单一实验数值
2
已知阴性对照也可能获得较高的结构预测分数
团队结论
同上；PD-L1 迁移测试中乱序阴性 ipTM 均值 0.867（n5）高于候选池中位 0.744（见 P21 脚注）
3
不能根据单一指标直接认定候选成功或失败
团队结论
方法论语气，不声称"指标无效"
4
指标的区分能力需要通过已知对照检验
团队结论
对应 P12（3.6 RESOLUTION）的 01 ESTABLISH CONTROLS
5
独立基准上的良好表现，不能直接外推到 EGFR、TNF-α 或其他靶点
团队结论
科学边界声明；P21 已有同口径表述"阈值不跨靶点照搬"
6
1BRS 的 AUC = 0.9813 属独立对接基准，不是 EGFR 候选设计结果
实测数值 + 边界标注
独立 1BRS Barnase–Barstar 对接基准：94,167 个可用对接姿态，正例为 DockQ ≥ 0.23（78 个），质心判据 AUC = 0.9813，Spearman ρ = −0.8506。该数值不是本项目任何靶点的候选筛选结果
7
结构可信度和界面几何属于计算证据
团队结论
指标分类陈述
8
不能单独证明实验结合亲和力，也不能证明受体激动或抑制功能
团队结论
binding ≠ activation；实验验证仍待进行
9
候选排序用于确定优先验证对象，最终结论需要实验支持
团队结论
与 P21 结论带同口径
10
结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束
团队结论（页面总结句）
用户指定文案
11
Structural evidence guides candidate prioritization, not experimental proof.
英文总结句
用户指定文案
本页不新增任何数值：唯一出现的数字 0.9813、94,167、78、0.23 全部来自既有 P21 脚注已引用的独立 1BRS 对接基准，本页仅以「来源 · 适用范围」注释区重新标注，未引入新数据。
二、白话层（讲人话：这页在说什么）
这页在干什么：第 7 页讲的是「我们怎么筛候选」，这一页讲「筛完之后，这些证据到底能说明什么、不能说明什么」。三张卡是一条递进的质疑链：
1. 01 单一指标的局限 —— 先说单个分数为什么不能信。ipTM 高，只代表模型认为自己搭的这套结构自洽，不代表两条链真的会结合。实证就是我们自己踩过的坑：阴性对照（乱序序列）的分数比真候选还高。
2. 02 评价结论依赖基准与任务 —— 那怎么知道一个指标能不能用？要用已知答案的对照去检验，而且检验通过的结论只在那个基准里成立。1BRS 上 AUC 0.9813 只说明「这个指标在 1BRS 对接姿态上分得清近天然与不合理」，不能顺手搬到 EGFR 上当设计成功率用。
3. 03 结构预测与生物学功能之间的距离 —— 最后退一步：就算结构算得对，也只是「值得优先验证」，结合不结合、激动还是抑制，必须靠实验。所以候选排序的作用是排实验队列，不是下结论。
闭环故事线：P12 提出多指标评价策略 → P20 总结基准校准的启示 → P21 给出三阶段决策流程 → P22 说明这套流程的结论能走到哪里、不能走到哪里 → P23（LIMITATIONS）再列具体不足。
三色竖条的用意：延续第 21 页「不可用 → 校准 → 可用」的语义，本页改为「局限（浅灰）→ 边界（交大红）→ 距离（深灰）」，表示讨论的层级在加深。
事实 / 团队自设规则 / 模型预测三分标注：
- 事实（实测数值）：只有 0.9813 / 94,167 / 78 / 0.23 一组，且明确归属独立基准。
- 团队自设规则：三条 bullet 的表述方式（"不能单独证明"、"不能直接外推"）是团队为自己划的诚实边界，不是文献结论。
- 模型预测：本页不涉及任何模型预测值的展示。
三、诚信边界（本页不得越线）
- 不宣称多指标策略已被证明能提高成功率；不说"更准确"、"准确率"、"通用阈值"。
- 0.9813 必须带「来源 · 适用范围」注释，且文字中已写明"不是 EGFR 候选设计结果"。
- 不把 1BRS 结果外推为 EGFR/TNF-α 的筛选表现。
- 不写"结构证据可以替代实验验证"；总结句用的是 guides ... not experimental proof。
- 与第 21 页不重复：本页不讲解 ipTM/AUC 的定义、不重述三阶段流程；与 P21 仅有的重复片段是术语"确定优先验证对象"（项目标准说法，不可避免）。
- 与后续 9 · LIMITATIONS 的分工：本页讲证据的解释边界（方法论层面的普遍约束），LIMITATIONS 讲本项目的具体不足（样本量、验证缺口、工具局限等）。
四、版面参数（复刻用）
元素
几何 / 字号
眉行左
x0.70 y0.42 w9.50，13pt 雅黑粗，交大红
眉行右
x7.90 y0.42 w4.73，右对齐，10pt 雅黑，浅灰
主标题
x0.70 y0.78 w11.93，24pt 雅黑粗，深灰
英文副题
x0.70 y1.28，Georgia 12pt，交大红
导语
x0.70 y1.58，12pt 雅黑，深灰
三卡
y1.90 h3.70 w3.70，gap 0.415；x = 0.70 / 4.815 / 8.93
竖色条
w0.05 与卡同高；01 浅灰 / 02 交大红 / 03 深灰
序号
22pt Georgia 粗，与竖条同色系（01 用中灰保证可读）
卡标题
14pt 雅黑粗，深灰
英文小标
9pt Georgia，浅灰
bullet
11pt 雅黑，行距 1.25，圆点 0.07 in，条目间距 0.10
02 注释区
y4.90 h0.68，PANEL 底；标题 8.5pt 红，正文 9pt 灰
01/03 chip
y5.25 h0.30，PANEL 底；10.5pt 雅黑粗，中灰
总结带
x0.70 y6.05 w11.93 h0.95，PINKP 底 + PINKL 1.5pt 边，圆角 0.05
总结主句
17pt 雅黑粗，关键词「帮助筛选候选」「基准、靶点和任务边界约束」标红
总结英文
Georgia 11pt，深灰
底部线
x0 y7.44 w13.333 h0.02，PINKL

### assistant — `<UUID>` — 2026-10-18T01:43:51.935186+00:00

这份 `8 · DISCUSSION` 制作稿整体是完整的，三张卡的递进关系也很清楚：**单一指标的局限 → 评价结论的适用边界 → 结构证据与生物学功能的距离**。它与第 7 页和第 9 页的分工明确，可以继续制作。

我建议在正式生成前只做以下几处微调，不需要推翻版式或重写整页。

## 需要微调的 3 个地方

**1. 第一张卡中，“ipTM 只说明预测结构自洽”略显绝对。**

ipTM 是对预测的蛋白质相互作用界面及相对排列的置信度指标，不宜简单定义为“结构自洽”。建议改为：

> 高 ipTM 不等于真实结合：它反映模型对预测复合物相对排列的信心，而非实验结合证据。

这样更准确，也保留了你希望表达的核心观点。

**2. 第二张卡不要让 1BRS 的 AUC 抢走讨论主线。**

`0.9813` 是独立对接基准的结果，不是本项目 EGFR 或 TNF-α 的候选筛选表现。建议把它保留在卡片底部的浅色注释区，而不是做成和主要结论同等醒目的大数字。

注释建议：

> 独立基准：1BRS Barnase–Barstar；94,167 个对接姿态，78 个正例（DockQ ≥ 0.23）。质心判据 AUC = 0.9813，Spearman ρ = −0.8506。该结果不代表本项目候选的结合成功率或跨靶点泛化能力。

**3. 导语和总结句要避免重复。**

导语负责提出讨论问题，总结带负责给出结论。可以采用：

- 导语：`计算结果可以帮助我们筛选候选，但哪些结论能够成立，仍取决于证据本身。`
- 总结主句：`结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束。`

这样首尾形成“提出问题—给出回答”的关系。

## 建议保留的最终结构

| 卡片 | 核心问题 | 结论 |
|---|---|---|
| 01 · 指标局限 | 高分是否意味着真实结合？ | 不意味着；阴性对照也可能得到高分。 |
| 02 · 适用边界 | 一个指标通过基准检验后，能否直接用于其他任务？ | 不能未经验证就外推。 |
| 03 · 功能距离 | 结构预测能否证明亲和力或激动功能？ | 不能；仍需实验验证。 |

**我的判断：这页已经具备定稿条件。** 保留三卡结构、三色竖条和底部结论带即可，不需要再添加新数据，也不需要把 PD-L1、B7-1 的换靶实验扩展成额外案例。

下一页 `9 · LIMITATIONS` 则应该更具体地回答：**当前这项研究本身还缺什么证据？** 不必再重复解释为什么高 ipTM 不等于真实结合。

### user — `<UUID>` — 2026-10-18T01:46:06.295000+00:00

我觉得“已知阴性对照也可能获得较高的结构预测分数。“实际上和第一点重合，要么合并，第二点改成”低ipTM不等于不结合……”

### assistant — `<UUID>` — 2026-10-18T01:46:10.187250+00:00

我同意，合并后逻辑更清楚。第一点讲 **高分可能误导**，第二点讲 **低分也不能直接否定候选**，形成正反两个方向的边界，不再重复强调阴性对照高分。

建议把第一张卡改成这样：

<box border radius="lg" padding={3} gap={3}>
  <row align="center" gap={2}>
    <box background="#E5E7EB" radius="md" padding={2}>
      <title size="lg" color="#374151">01</title>
    </box>
    <box flex="1" gap={1}>
      <title size="md">单一指标的局限</title>
      <text color="secondary" size="sm">LIMITS OF SINGLE-METRIC EVALUATION</text>
    </box>
  </row>
  <divider color="subtle" />
  **高 ipTM 不等于真实结合**

  阴性对照也可能获得较高分数，说明高分不足以证明候选具有真实结合能力。

  **低 ipTM 也不等于不结合**

  单一指标无法涵盖结合能力的全部信息，低分本身也不足以证明候选不结合。

  <box background="surface-secondary" radius="md" padding={2}>
    <text weight="medium" textAlign="center">高分不能证明结合，低分不能证明不结合。</text>
  </box>
</box>

这样第一张卡就形成完整的双向论证：

- **高分端**：已知阴性对照也可能高分——你的项目有直接案例支撑。
- **低分端**：低分不能单独作为不结合的证据——这是方法论上的审慎边界，不应伪装成已经由当前数据充分验证的结论。

第二张卡继续专注于“指标需要校准、结论不能随意外推”，第三张卡讨论“结构证据不能代替亲和力和功能实验”。三张卡的分工会更明确。

**底部总结可以不变**：结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束。

### user — `<UUID>` — 2026-10-18T01:48:51.668000+00:00

卡2“1BRS 的 AUC = 0.9813 属独立对接基准，不是 EGFR 候选设计结果。”我觉得不好，这一张应该主要是结论性的，不应再举例子，能不能换掉，连带这下面的“独立 1BRS Barnase–Barstar 对接基准（94,167 个姿态，DockQ ≥ 0.23 正例 78 个）”

### assistant — `<UUID>` — 2026-10-18T01:48:55.156098+00:00

我同意。P22 是 **Discussion（讨论）**，卡片应该提炼项目得到的方法学认识，而不是再次罗列数据。1BRS 的 AUC、姿态数量和正例数量可以留在方法或补充材料中，不必在这张讨论页占据位置。

我建议把卡 2 从“独立基准的表现不能外推”改成更具结论性的 **“指标的判别能力需要校准”**，这样既承接卡 1 的单一指标局限，也自然引出卡 3 的证据边界。

## 卡 2 修改建议

<box border radius="lg" padding={4} gap={3}>
  <row align="center" gap={2}>
    <box background="#B91C1C" radius="sm" size="36px" align="center" justify="center">
      <title color="#FFFFFF" size="lg">02</title>
    </box>
    <box flex="1" gap={1}>
      <title size="lg">指标的判别能力需要校准</title>
      <text color="secondary" size="xs">METRIC DISCRIMINATION REQUIRES CALIBRATION</text>
    </box>
  </row>
  <divider color="subtle" />
  **正文**

  - 不同指标反映结合预测的不同方面，其判别能力并不相同。
  - 指标的解释与使用，应通过已知阳性和阴性对照进行检验。
  - 不能将某一基准上的良好表现，直接视为对其他靶点或任务同样有效。
</box>

**同时删除卡 2 下方原有的整段 1BRS 数据说明**，不再用其他数字替换。

这样三张卡的逻辑会更清晰：

1. **单一指标的局限**：高分不等于真实结合，低分也不等于不结合。
2. **指标判别能力的校准**：需要已知对照检验，不能直接外推。
3. **计算证据的边界**：结构预测不能替代实验亲和力与功能验证。

底部总结仍然可以保留：

> **结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束。**

这版的重点从“我们在某个基准上得到了什么数值”，转为“这些结果告诉我们应该怎样解释和使用计算指标”，更符合 Discussion 页的定位。

### user — `<UUID>` — 2026-10-18T02:04:09.213000+00:00

下一张

### assistant — `<UUID>` — 2026-10-18T02:04:13.023148+00:00

下一张是 **P23 · 9 · LIMITATIONS｜局限性**。

这一页要和刚刚的 Discussion 明确分工：

- **P22 Discussion**：这些结果告诉我们什么，结论应该如何解释。
- **P23 Limitations**：当前项目的证据还缺什么，因此哪些结论暂时不能成立。

所以，P23 不需要再重复“高分不等于真实结合”或“指标需要校准”，而应该聚焦项目本身的数据覆盖、实验验证和流程局限。

## P23 内容建议

<box gap={3}>
  <box gap={1}>
    <text color="secondary" size="xs">页眉</text>
    <title size="xl">9 · LIMITATIONS｜局限性</title>
    <text color="secondary" size="sm">LIMITATIONS OF THE CURRENT STUDY</text>
    <text>当前流程建立了计算筛选与基准评价框架，但证据覆盖范围和实验验证仍有限。</text>
  </box>
  <grid columns={3} gap={3}>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">01</title>
        <title size="md">基准覆盖有限</title>
        <text color="secondary" size="xs">LIMITED BENCHMARK COVERAGE</text>
        <divider color="subtle" />
        - 已知阳性与阴性对照的数量有限。
        - 不同靶点的证据完整度并不一致。
        - 现有数据不足以建立适用于所有靶点的通用阈值。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">02</title>
        <title size="md">缺少实验闭环</title>
        <text color="secondary" size="xs">LACK OF EXPERIMENTAL VALIDATION</text>
        <divider color="subtle" />
        - 当前结论主要来自计算预测与结构评价。
        - 尚缺系统的实验亲和力数据（如 \(K_d\)）。
        - 不能据此确认候选物的真实结合或功能活性。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">03</title>
        <title size="md">流程仍有依赖</title>
        <text color="secondary" size="xs">PIPELINE AND EVALUATION DEPENDENCIES</text>
        <divider color="subtle" />
        - 预测结果可能受模型、参数与随机种子影响。
        - 不同靶点仍需针对性校准与评估。
        - TNF-α 等案例的部分结构对照分析尚未完成。
      </box>
    </grid-item>
  </grid>
  <box background="surface-secondary" radius="lg" padding={3} gap={1}>
    <title size="md">核心结论</title>
    <text>当前工作验证的是计算评价框架的可行性，而非候选结合能力或实验成功率。</text>
    <text color="secondary" size="sm">The current study establishes an evaluation framework, not experimentally validated binder performance.</text>
  </box>
</box>

## 这一页需要把握的三个细节

1. **“基准覆盖有限”**：强调对照数量和靶点覆盖不足，不要直接说整个基准无效。
2. **“缺少实验闭环”**：如果没有系统的实验 \(K_d\) 数据，就不能把计算排序描述成已经验证的候选优选能力。
3. **“流程仍有依赖”**：TNF-α 的结构对照分析尚未完成，可以作为具体例子，但不要让它成为整页中心。

另外，建议把“当前工作验证的是计算评价框架的可行性”作为本页的核心收束句。它既说明了项目的实际价值，也清楚划定了结论边界。

下一张 **P24 · 10 · FUTURE WORK｜未来工作** 就可以逐项对应这三类局限：扩充基准、补充实验验证、提高流程的可复现性与跨靶点评价能力。

### user — `<UUID>` — 2026-10-18T02:04:27.953000+00:00

提示词

### assistant — `<UUID>` — 2026-10-18T02:04:31.408727+00:00

下面是可以直接发给 WorkBuddy / PPT 生成工具的完整提示词，针对 **P23 · 9 · LIMITATIONS｜局限性**，沿用 P21、P22 的视觉风格，不新增页面、不改动其他页。

<WritingBlock id="58316" variant="document">请制作主报告第 23 页：**9 · LIMITATIONS｜局限性**，并保存为独立单页归档文件 `Slides-30-Limitations-v1.pptx`。如需生成脚本，命名为 `_gen_90limitations_v1_slide.py`。

## 一、页面定位

本页属于 AI-BinderDesign 科研报告，承接 P22 Discussion，重点说明**当前项目自身的证据局限**，而不是再次解释“高分不等于真实结合”或重复指标校准的讨论。

核心信息：

当前工作建立了计算筛选与基准评价框架，但基准覆盖、实验验证和流程可复现性仍存在局限。

## 二、视觉规范

- 16:9 宽屏，白色背景，上海交大红色作为强调色。
- 延续 P21 Multi-Metric Decision、P22 Discussion 的设计语言。
- 顶部左侧页眉：`9 · LIMITATIONS ｜ 局限性`
- 顶部右侧：`AI-BINDERDESIGN · RESEARCH REPORT`
- 中文为主，英文为辅。
- 中文主标题醒目，英文副标题较小，使用 Georgia 字体。
- 标题下方设置一句中文引导语。
- 中部采用三个等宽并排白色卡片，细边框、轻量垂直色条、统一内边距。
- 三张卡片的编号、标题、正文层级一致；不要塞入大段文字。
- 页面底部设置浅红色或浅灰红色结论条。
- 保持专业、克制、简洁的科研汇报风格；不要使用装饰性插画、渐变背景或夸张图标。

## 三、标题与引导语

中文主标题：

**当前研究的局限性**

英文副标题：

`LIMITATIONS OF THE CURRENT STUDY`

引导语：

当前流程建立了计算筛选与基准评价框架，但证据覆盖范围和实验验证仍有限。

## 四、三张卡片的完整文案

### 卡片 01

编号：`01`

标题：**基准覆盖有限**

英文小标题：`LIMITED BENCHMARK COVERAGE`

正文：

- 已知阳性与阴性对照的数量有限。
- 不同靶点的数据与证据完整度并不一致。
- 现有结果不足以建立适用于所有靶点的通用阈值。

### 卡片 02

编号：`02`

标题：**缺少实验闭环**

英文小标题：`LACK OF EXPERIMENTAL VALIDATION`

正文：

- 当前结论主要来自计算预测与结构评价。
- 尚缺系统的实验亲和力数据，例如解离常数 Kd。
- 目前无法确认候选物的真实结合能力或功能活性。

### 卡片 03

编号：`03`

标题：**流程仍有依赖**

英文小标题：`PIPELINE AND EVALUATION DEPENDENCIES`

正文：

- 预测结果可能受到模型、参数与随机种子的影响。
- 不同靶点仍需针对性校准与评估。
- TNF-α 等案例的部分结构对照分析尚未完成。

## 五、底部结论条

中文结论：

**当前工作建立了计算评价框架，但尚未验证候选物的实验结合能力或实验成功率。**

英文辅助句：

`The current study establishes an evaluation framework, not experimentally validated binder performance.`

## 六、排版要求

1. 三张卡片保持等宽、等高，水平对齐。
2. 正文每条尽量控制在一至两行，避免字号过小。
3. 编号作为轻量视觉元素，不使用大面积红色填充。
4. 卡片 02 可使用上海交大红色作为强调色，其余卡片使用浅灰色与深灰色。
5. 底部结论条要醒目，但不能压过主标题。
6. 保留足够留白，确保投影展示时可读。
7. 所有文字必须完整呈现，不得溢出卡片或页面边界。

## 七、科研准确性要求

- 不得编造样本量、实验结果、候选成功率、Kd 数值或通用阈值。
- 不得声称所有结构指标都无效。
- 不得声称多指标评价已被实验验证为更准确。
- 不得把独立对接基准的结果写成 EGFR 或 TNF-α 候选设计的实验结果。
- 对尚未完成的 TNF-α 分析，只能描述为当前工作尚未完成的部分，不得推测其结果。
- 不要新增“5.1”“5.2”等未经确认的章节。
- 不要修改其他幻灯片的内容或编号。

## 八、交付要求

生成一份可独立打开、可编辑的 PowerPoint 单页文件，比例为 16:9。完成后检查标题、卡片、底部结论条的位置，确保没有文字溢出、重叠或字号异常。</WritingBlock>

**注意：** 如果生成工具能够读取前面 P21、P22 的归档文件，建议同时提供作为视觉参考，尤其是卡片样式、页眉和底部结论条；只借鉴视觉规范，不要复制它们的内容。

### user — `<UUID>` — 2026-10-18T02:12:35.617000+00:00

9 · LIMITATIONS｜局限性（v1）
页面位置：主 deck 第 23 页（P23），承接第 22 页（8 · DISCUSSION），是报告方法论部分的收尾。
版式文件：Slides-30-Limitations-v1.pptx（独立单页存档），生成脚本 _gen_90limitations_v1_slide.py。
版面语言：完全沿用 P21/P22——眉行（左 9 · LIMITATIONS ｜ 局限性 + 右上角标）、24pt 中文主标题、Georgia 12pt 英文副题、12pt 导语、三张等宽白卡（3.70 in，圆角 0.04，左侧竖色条）、卡内分隔细线、粉底结论带（PINKP + PINKL 1.5pt 边）、底部细线。bullet 字号 12pt，与 P22 一致。
一、数据层（逐条 + 来源）
本页不含任何数值——这是 LIMITATIONS 页的性质决定的，全部为团队自评陈述。校验脚本禁词含 nM/μM/mM/pM、Kd =、n=、AUC、1BRS、0.9813、94,167、DockQ、5.1、5.2，全部不在页。
#
页面文字
类型
来源 / 依据
1
已知阳性与阴性对照的数量有限
团队自评
对照体系规模由项目实际构建情况决定；具体数字不写入本页
2
不同靶点的数据与证据完整度并不一致
团队自评
与 P3/P21 中 EGFR 主案例 vs 其他靶点证据密度差异一致
3
现有结果不足以建立适用于所有靶点的通用阈值
团队自评（否定式结论）
与 P12"分布重叠则多指标联合"、P21"阈值不跨靶点照搬"同口径
4
当前结论主要来自计算预测与结构评价
团队自评
项目未开展湿实验
5
尚缺系统的实验亲和力数据，例如解离常数 Kd
团队自评
只声明"缺失"，不提供任何 Kd 数值
6
目前无法确认候选物的真实结合能力或功能活性
团队自评
binding 与 activation 均未经实验验证
7
预测结果可能受到模型、参数与随机种子的影响
团队自评
Boltz-2 等预测工具的已知特性
8
不同靶点仍需针对性校准与评估
团队自评
与 P21 CALIBRATION 卡"换靶后需重新标定"同口径
9
TNF-α 等案例的部分结构对照分析尚未完成
团队自评（进行状态）
对应 P16–P19 的 TNF-α 结构分析链；只描述为"尚未完成"，不推测其结果
10
当前工作建立了计算评价框架，但尚未验证候选物的实验结合能力或实验成功率
团队自评（页面结论）
用户指定文案
11
The current study establishes an evaluation framework, not experimentally validated binder performance.
英文结论
用户指定文案
事实 / 团队自设规则 / 模型预测三分标注：
- 事实（实测数值）：本页无。
- 团队自设规则：全部 bullet 与结论句。
- 模型预测：本页不展示任何模型预测值。
二、白话层（讲人话：这页在说什么）
这页在干什么：Discussion（P22）讲的是"证据的解释边界"这类普遍约束；LIMITATIONS 讲的是这个项目自己具体缺什么。三条各管一个缺口：
1. 01 基准覆盖有限 —— 我们搭的对照体系本身不够大，而且五个靶点手里攥的数据密度不一样，所以现在这套结果还没到能总结出"放之四海皆准的阈值"的程度。
2. 02 缺少实验闭环 —— 全部结论都建立在计算预测和结构评价上。没有系统的亲和力数据（比如 Kd），所以候选到底结不结合、有没有功能活性，现在无法确认。这是整个项目最大的缺口。
3. 03 流程仍有依赖 —— 预测结果会受模型、参数、随机种子影响，换个靶点还得重新校准；TNF-α 那条线的部分结构对照分析也还没做完。
结论条收口：我们交出的是一个评价框架，不是已验证的 binder 性能。这句话是整份报告对自身定位最准确的表述。
闭环故事线：…→ P21 给出三阶段决策流程 → P22 说明证据的解释边界 → P23 列出本项目自身缺口 → P24（10 · FUTURE WORK）给出对应的下一步。
三色竖条的用意：P22 是「局限（浅灰）→ 校准（红）→ 边界（深灰）」；本页按用户要求改为「浅灰 → 交大红 → 深灰」，即 02 缺少实验闭环用交大红强调（这是最重的缺口），01/03 用浅灰与深灰。
三、诚信边界（本页不得越线）
- 不得编造任何数值：样本量、Kd、AUC、成功率、通用阈值一律不写；Kd 只能以"例如解离常数 Kd"的缺失声明形式出现。
- 不得声称"所有结构指标都无效"——本页只说覆盖与验证不足，不说指标无用。
- 不得声称"多指标评价已被实验验证为更准确"。
- 不得把独立对接基准的结果写成 EGFR/TNF-α 候选设计的实验结果（本页不出现 1BRS 相关内容）。
- TNF-α 未完成的分析只描述为"尚未完成"，不推测其结果。
- 不新增"5.1""5.2"等未经确认的章节编号；不改动其他页内容与编号。
- 与 P22 不重复：P22 讲普遍解释边界（高/低分、校准、结构 vs 功能），本页讲项目自身缺口（覆盖、实验、依赖）。重叠仅在"无法确认真实结合能力"这一必要共识上。
四、版面参数（复刻用）
元素
几何 / 字号
眉行左
x0.70 y0.42 w9.50，13pt 雅黑粗，交大红
眉行右
x7.90 y0.42 w4.73，右对齐，10pt 雅黑，浅灰
主标题
x0.70 y0.78 w11.93，24pt 雅黑粗，深灰
英文副题
x0.70 y1.28，Georgia 12pt，交大红
导语
x0.70 y1.58，12pt 雅黑，深灰
三卡
y1.90 h3.70 w3.70，gap 0.415；x = 0.70 / 4.815 / 8.93
竖色条
w0.05 与卡同高；01 浅灰 B0ACA4 / 02 交大红 9E1F36 / 03 深灰 1A1A1A
序号
22pt Georgia 粗，与竖条同色
卡标题
14pt 雅黑粗，深灰
英文小标
9pt Georgia，浅灰（全大写句式）
bullet
12pt 雅黑，行距 1.25，圆点 0.07 in，条目间距 0.10
bullet 起点
卡1 y3.36/3.73/4.11；卡2 y3.36/3.73/4.38；卡3 y3.36/4.01/4.38
结论带
x0.70 y6.05 w11.93 h0.95，PINKP 底 + PINKL 1.5pt 边，圆角 0.05
结论主句
17pt 雅黑粗，「尚未验证候选物的实验结合能力或实验成功率」标红
结论英文
Georgia 11pt，深灰
底部线
x0 y7.44 w13.333 h0.02，PINKL
chip
本页不设 chip（P22 有，本页按用户文案无收口句；三卡下方留白由卡片高度吸收）

### assistant — `<UUID>` — 2026-10-18T02:12:39.115116+00:00

这份 P23 规格已经足够作为制作依据，而且比上一版提示词更严谨，尤其是把页面文案、事实边界、卡片配色和具体坐标都固定下来了。

我建议正式制作前只核对 **3 个细节**：

1. **眉行右侧标记**：`AI-BINDERDESIGN · RESEARCH REPORT` 应与 P21/P22 保持完全一致，不要因文字框宽度不同而改写。
2. **结论带的红色强调**：只把“尚未验证候选物的实验结合能力或实验成功率”标红，前半句“当前工作建立了计算评价框架”保持深灰，突出项目贡献与证据边界的对比。
3. **卡片 03 的文字排布**：第三条“TNF-α 等案例的部分结构对照分析尚未完成”较长，应允许自然换行；不要为强行适配而缩小 bullet 字号。

另外，数据层中“本页不含任何数值”应理解为**不展示实验或模型结果数值**。版式参数中的字号、坐标以及正文里的 Kd 缩写不构成数据违规；`Kd` 只用于说明尚缺实验亲和力数据。

除此之外，建议严格按现有规格执行，不再增删内容。P23 的结论是整份报告的定位声明：**我们建立了计算评价框架，但尚未验证候选物的实验结合能力或实验成功率。** 这也为 P24 的 Future Work 提供了直接的承接。

### user — `<UUID>` — 2026-10-18T02:12:58.220000+00:00

TNF-α 等案例的部分结构对照分析尚未完成。这句话是什么意思

### assistant — `<UUID>` — 2026-10-18T02:13:01.858459+00:00

这句话的意思是：**TNF-α 相关项目中，有一部分把预测结构与已知实验结构进行比较、分析的工作，还没有全部完成。**

这里的“结构对照分析”具体可能包括：

- **结构叠合（superposition）**：把模型预测的蛋白复合物与实验解析的参考结构对齐。
- **界面比较**：检查预测的结合位置、相互作用残基和界面几何是否与参考结构一致。
- **偏差评估**：如果参考结构和链对应关系明确，可以进一步计算 RMSD 等结构偏差指标。

结合你之前的 TNF-α 项目，这句话指的是相关结构分析链中尚未完成的部分，**并不是说 TNF-α 的所有预测都没有完成，也不是说现有预测已经失败。**

不过，我认为原句有两个问题：

1. “TNF-α 等案例”中的“等案例”不够明确，读者可能会问还有哪些案例。
2. “结构对照分析”比较模糊，不清楚具体缺的是结构叠合、界面比较，还是定量指标。

### 我更建议这样写

如果目前确实主要是 TNF-α 的分析尚未完成：

> **TNF-α 案例的部分结构验证与定量比较尚未完成。**

如果具体尚未完成的是预测结构与实验参考结构的比较，可以写得更准确：

> **TNF-α 案例中，预测复合物与实验参考结构的定量比较尚未完成。**

我更推荐第二句，前提是它符合你目前实际的工作进度。它明确说明了缺少哪一类分析，也不会让人误以为整个 TNF-α 设计流程都没有完成。

如果你尚未确定具体缺哪项分析，则暂时不要写得这么具体，可以直接写：

> **部分靶点的结构验证工作仍待完善。**

这句话更稳妥，但信息量也更少。

### user — `<UUID>` — 2026-10-18T02:16:36.542000+00:00

别写这个，换一点，总结性的

### assistant — `<UUID>` — 2026-10-18T02:16:40.118004+00:00

可以把卡 3 的第三条换成更总结性的表述，不再提 TNF-α 的具体进度。

我最推荐：

**当前流程的跨靶点适用性仍需进一步验证。**

这样卡 3 的三条逻辑更统一：

- 预测结果可能受到模型、参数与随机种子的影响。
- 不同靶点仍需针对性校准与评估。
- **当前流程的跨靶点适用性仍需进一步验证。**

不过，第二条和第三条有一点接近。若想让三条各自承担不同信息，我更建议改成：

1. 预测结果可能受到模型、参数与随机种子的影响。
2. 不同靶点仍需针对性校准与评估。
3. **当前流程的稳定性与可迁移性仍需进一步验证。**

这里“稳定性”对应模型、参数和随机种子的影响，“可迁移性”对应换靶点后的适用性，整体更有总结性，也更适合 Limitations 页。

### user — `<UUID>` — 2026-10-18T02:30:29.169000+00:00

下一张

### assistant — `<UUID>` — 2026-10-18T02:30:34.222597+00:00

下一张是 **P24 · 10 · FUTURE WORK｜未来工作**。

这一页要和 P23 的三项局限逐一对应，形成闭环：**基准覆盖有限 → 扩充对照；缺少实验闭环 → 实验验证；流程仍有依赖 → 提升可复现性与跨靶点适用性。**

## P24 页面内容建议

<box gap={3}>
  <box gap={1}>
    <text color="secondary" size="xs">页面标题</text>
    <title size="xl">10 · FUTURE WORK｜未来工作</title>
    <text color="secondary" size="sm">FROM COMPUTATIONAL EVALUATION TO EXPERIMENTAL VALIDATION</text>
    <text>围绕基准、实验与流程三个方向，逐步完善候选评价体系。</text>
  </box>
  <grid columns={3} gap={3}>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">01</title>
        <title size="md">扩充基准体系</title>
        <text color="secondary" size="xs">EXPAND THE BENCHMARK</text>
        <divider color="subtle" />
        - 增加有明确生物学依据的阳性与阴性对照。
        - 扩大靶点和复合物类型的覆盖范围。
        - 检验不同指标在不同靶点上的判别能力。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">02</title>
        <title size="md">引入实验验证</title>
        <text color="secondary" size="xs">EXPERIMENTAL VALIDATION</text>
        <divider color="subtle" />
        - 对优先候选开展实验验证。
        - 测量结合亲和力，如解离常数 \(K_d\)。
        - 对具有功能目标的项目进一步验证激动或抑制活性。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">03</title>
        <title size="md">完善评价流程</title>
        <text color="secondary" size="xs">IMPROVE PIPELINE ROBUSTNESS</text>
        <divider color="subtle" />
        - 系统评估模型、参数与随机种子的影响。
        - 根据靶点和任务重新校准评价指标。
        - 将实验结果反馈到候选排序与评价规则中。
      </box>
    </grid-item>
  </grid>
  <box background="surface-secondary" radius="lg" padding={3} gap={1}>
    <title size="md">未来目标</title>
    **建立计算预测、基准校准与实验验证相互衔接的评价闭环。**
    <text color="secondary" size="sm">Toward an iterative cycle of computational design, benchmark calibration, and experimental validation.</text>
  </box>
</box>

这页有一个重要边界：以上是**计划开展的工作**，不是已经完成的成果。尤其是实验验证和实验结果反馈，应使用“拟开展”“进一步验证”等表达，不能写成已经建立了实验闭环。

如果采用这套内容，下一张 P25 · Conclusion 就不必继续列未来计划，而应回到整份报告已经建立的三项核心认识与实际贡献。

### user — `<UUID>` — 2026-10-18T02:30:52.650000+00:00

提示词

### assistant — `<UUID>` — 2026-10-18T02:30:56.069485+00:00

下面是 P24 的完整制作提示词，延续 P21–P23 的版式与视觉语言，并严格区分**已经完成的工作**和**未来计划**。

<WritingBlock id="61482" variant="document">请制作 AI-BinderDesign 科研报告主 deck 第 24 页：**10 · FUTURE WORK｜未来工作**，保存为独立单页 PowerPoint 文件 `Slides-31-FutureWork-v1.pptx`。如需生成脚本，命名为 `_gen_100futurework_v1_slide.py`。

本任务只制作这一张幻灯片，不修改其他页面，不重新编排主 deck。

## 一、页面定位

本页承接 P23 `9 · LIMITATIONS｜局限性`，对应前一页指出的三类局限，提出后续研究方向。

逻辑关系：

- 基准覆盖有限 → 扩充基准体系。
- 缺少实验闭环 → 引入实验验证。
- 流程仍有依赖 → 完善流程稳健性与评价方法。

核心信息：

**未来工作的重点，是将计算预测、基准校准与实验验证逐步衔接起来。**

注意：本页描述的是未来计划，不是已完成成果。不得暗示团队已经完成湿实验、测得 Kd，或建立了实验反馈闭环。

## 二、视觉与版式要求

完全沿用 P21、P22、P23 的视觉语言：

- 16:9 宽屏，白色背景，上海交大红色作为强调色。
- 顶部眉行：左侧章节编号与中英文名称，右侧 `AI-BINDERDESIGN · RESEARCH REPORT`。
- 中文主标题 24pt，深灰色、加粗。
- 英文副标题使用 Georgia 12pt，上海交大红色。
- 中文导语 12pt，深灰色。
- 中部三张等宽白色卡片，水平并排，卡片宽度约 3.70 in，保持统一高度、内边距和间距。
- 卡片采用轻量边框、左侧竖色条和卡内细分隔线。
- 三张卡片的编号、中文标题、英文小标题、正文层级保持一致。
- 建议竖色条依次使用浅灰、上海交大红、深灰，与 P23 的视觉规则一致。
- 页面底部设置浅粉色结论带，使用 P21–P23 同款的底色、边框与圆角风格。
- 底部保留细线，整体留白充足，避免拥挤。
- 不使用大面积装饰图、复杂流程图或额外的数据图表。

## 三、标题与导语

页眉左侧：

`10 · FUTURE WORK ｜ 未来工作`

右上角：

`AI-BINDERDESIGN · RESEARCH REPORT`

中文主标题：

**从计算评价走向实验验证**

英文副标题：

`FROM COMPUTATIONAL EVALUATION TO EXPERIMENTAL VALIDATION`

中文导语：

围绕基准、实验与流程三个方向，逐步完善候选评价体系。

## 四、三张卡片文案

### 卡片 01

编号：`01`

中文标题：**扩充基准体系**

英文小标题：`EXPAND THE BENCHMARK`

正文：

- 增加具有明确生物学依据的阳性与阴性对照。
- 扩大靶点与复合物类型的覆盖范围。
- 检验不同指标在不同靶点上的判别能力。

### 卡片 02

编号：`02`

中文标题：**引入实验验证**

英文小标题：`EXPERIMENTAL VALIDATION`

正文：

- 对优先候选开展实验验证。
- 测量结合亲和力，例如解离常数 Kd。
- 对具有功能目标的项目进一步验证激动或抑制活性。

### 卡片 03

编号：`03`

中文标题：**完善评价流程**

英文小标题：`IMPROVE PIPELINE ROBUSTNESS`

正文：

- 系统评估模型、参数与随机种子的影响。
- 根据靶点与任务重新校准评价指标。
- 探索将实验结果反馈到候选排序与评价规则中。

## 五、底部结论带

中文结论：

**建立计算预测、基准校准与实验验证相互衔接的评价闭环。**

英文辅助句：

`Toward an iterative cycle of computational design, benchmark calibration, and experimental validation.`

中文结论应为视觉主体，英文辅助句字号较小。

## 六、科研准确性与诚信边界

1. 不得编造任何实验结果、Kd 数值、候选成功率或预计提升幅度。
2. 不得将未来计划描述为已经完成的工作。
3. 不得声称多指标评价已被实验验证为更准确。
4. 不得声称当前流程已经能够可靠预测结合亲和力或激动、抑制功能。
5. “实验结果反馈到候选排序”必须表述为未来计划或探索方向。
6. 不新增未经确认的章节编号，不改动其他页面。
7. 不要重复 P23 的局限性列表；本页应聚焦对应的改进方向。
8. 不要把未来工作写成泛泛的“优化模型”，而应突出本项目的核心路径：基准扩充、实验验证、评价校准。

## 七、交付前检查

- 确认文件为 16:9、可编辑的 PowerPoint 单页。
- 检查三张卡片等宽、对齐、层级一致。
- 检查中文正文没有溢出或被压缩到过小字号。
- 检查底部结论带完整显示中英文内容。
- 确认所有未来工作使用计划性措辞，没有将计划写成既有成果。
- 确认没有修改其他幻灯片的内容与编号。</WritingBlock>

这一页完成后，P25 Conclusion 应回归项目已经完成的工作、基准校准带来的认识，以及当前结论的适用边界，不再重复未来工作计划。

### user — `<UUID>` — 2026-10-18T02:57:40.135000+00:00

10 · FUTURE WORK｜未来工作（v1）
页面位置：主 deck 第 24 页（P24），承接第 23 页（9 · LIMITATIONS）。
版式文件：Slides-31-FutureWork-v1.pptx（独立单页存档），生成脚本 _gen_100futurework_v1_slide.py。
版面语言：与 P21/P22/P23 完全同构——眉行（左 10 · FUTURE WORK ｜ 未来工作 + 右上 AI-BINDERDESIGN · RESEARCH REPORT）、24pt 中文主标题、Georgia 12pt 英文副题、12pt 导语、三等宽白卡（3.70 in，圆角 0.04，左竖色条）、卡内分隔细线、粉底结论带（PINKP + PINKL 1.5pt）、底部细线；bullet 12pt。
与 P23 的对应关系（本页核心逻辑）：
P23 局限
P24 方向
01 基准覆盖有限
01 扩充基准体系
02 缺少实验闭环
02 引入实验验证
03 流程仍有依赖
03 完善评价流程
一、数据层（逐条 + 来源）
本页不含任何数值（与 P23 同）。Kd 仅以"例如解离常数 Kd"的计划性表述出现，不提供任何 Kd 数值。校验禁词含 nM/μM/mM/pM、Kd =、n=、AUC、1BRS、0.9813、94,167，全部不在页。
#
页面文字
类型
来源 / 依据
1
增加具有明确生物学依据的阳性与阴性对照
未来计划
对应 P23-01「已知阳性与阴性对照的数量有限」
2
扩大靶点与复合物类型的覆盖范围
未来计划
对应 P23-01「不同靶点的数据与证据完整度并不一致」
3
检验不同指标在不同靶点上的判别能力
未来计划
对应 P21「阈值不跨靶点照搬」
4
对优先候选开展实验验证
未来计划
对应 P23-02「缺少实验闭环」
5
测量结合亲和力，例如解离常数 Kd
未来计划
同上；只说要测，不提供数值
6
对具有功能目标的项目进一步验证激动或抑制活性
未来计划
对应 P22「不能证明受体激动或抑制功能」
7
系统评估模型、参数与随机种子的影响
未来计划
对应 P23-03「预测结果可能受到模型、参数与随机种子的影响」
8
根据靶点与任务重新校准评价指标
未来计划
对应 P23-03「不同靶点仍需针对性校准与评估」
9
探索将实验结果反馈到候选排序与评价规则中
未来计划（探索方向）
用户明确要求用"探索"措辞，不得写成已建立反馈闭环
10
建立计算预测、基准校准与实验验证相互衔接的评价闭环
未来目标
用户指定文案；标签「未来目标」
11
Toward an iterative cycle of computational design, benchmark calibration, and experimental validation.
英文目标句
用户指定文案
事实 / 团队自设规则 / 模型预测三分标注：
- 事实（实测数值）：本页无。
- 团队自设规则：全部条目。
- 模型预测：本页不展示任何模型预测值。
二、白话层（讲人话：这页在说什么）
这页在干什么：P23 列了三个缺口，P24 一一对应地给出补法——局限与对策严格配对，读者可以左右对照着看：
1. 01 扩充基准体系 —— 对照不够多、各靶点数据密度不一 → 那就加有生物学依据的阳性/阴性对照，扩大靶点和复合物类型，并且要检验指标在不同靶点上是否依然分得开。
2. 02 引入实验验证 —— 全部结论停留在计算层面 → 那就对优先候选做实验，测亲和力（比如 Kd），有功能目标的项目再进一步看激动或抑制。这是整个项目最大的方向性转变：从"算"走向"测"。
3. 03 完善评价流程 —— 结果受模型/参数/种子影响、换靶点要重新校准 → 那就系统评估这些影响，按靶点和任务重新校准，并探索把实验结果回灌到排序规则里。
结论带「未来目标」：把三件事合成一句话——建立计算预测、基准校准与实验验证相互衔接的评价闭环。注意用词是"建立…闭环"作为目标，不是"已建立"。
闭环故事线：…→ P22 证据的解释边界 → P23 本项目缺口 → P24 对应的改进方向 → P25 Conclusion 回归已完成工作与核心认识（不再重复未来计划）。
三色竖条：与 P23 一致（浅灰 → 交大红 → 深灰），其中 02「引入实验验证」用红强调——它是从计算走向实验的关键一跃。
三、诚信边界（本页不得越线）
- 不得把计划写成成果：禁词含 已完成 / 已经完成 / 已建立 / 已经建立 / 已测得 / 测得了 / 已实现 / 已经实现 / 已闭环 / 湿实验已完成，全部不在页。所有 bullet 均为计划性动词（增加、扩大、检验、开展、测量、验证、评估、校准、探索）。
- 不得编造 Kd 数值、候选成功率、预计提升幅度。
- 不得声称"多指标评价已被实验验证为更准确"；不得声称"当前流程已能可靠预测亲和力或激动/抑制功能"。
- 「实验结果反馈到候选排序」必须保持"探索…中"的措辞，不得写成已建立的反馈闭环。
- 不新增未经确认的章节编号，不改动其他页。
- 不重复 P23 的局限性列表；聚焦对应的改进方向。
- 不写成泛泛的"优化模型"，而突出本项目核心路径：基准扩充、实验验证、评价校准。
四、版面参数（复刻用）
元素
几何 / 字号
眉行左
x0.70 y0.42 w9.50，13pt 雅黑粗，交大红
眉行右
x7.90 y0.42 w4.73，右对齐，10pt 雅黑，浅灰
主标题
x0.70 y0.78 w11.93，24pt 雅黑粗，深灰
英文副题
x0.70 y1.28，Georgia 12pt，交大红
导语
x0.70 y1.58，12pt 雅黑，深灰
三卡
y1.90 h3.70 w3.70，gap 0.415；x = 0.70 / 4.815 / 8.93
竖色条
w0.05 与卡同高；01 浅灰 / 02 交大红 / 03 深灰
序号
22pt Georgia 粗，与竖条同色
卡标题
14pt 雅黑粗，深灰
英文小标
9pt Georgia，浅灰（全大写）
bullet
12pt 雅黑，行距 1.25，圆点 0.07 in，条目间距 0.10
bullet 起点
卡1 y3.36/4.01/4.385；卡2 y3.36/3.735/4.385；卡3 y3.36/3.735/4.11
手动换行（br）
卡1条1 …阳性与阴性│对照。；卡2条2 测量结合亲和力，│例如解离常数 Kd。；卡3条3 …候选排序│与评价规则中。——避免按字断行拆开「对照 / 解离常数 / 规则」
结论带
x0.70 y6.00 w11.93 h1.06，PINKP 底 + PINKL 1.5pt 边，圆角 0.05
标签
未来目标，10pt 雅黑粗，交大红，y6.12
结论主句
17pt 雅黑粗，「实验验证」标红，y6.38
结论英文
Georgia 11pt，深灰，y6.78
底部线
x0 y7.44 w13.333 h0.02，PINKL
chip
本页不设 chip（与 P23 一致）

### assistant — `<UUID>` — 2026-10-18T02:57:44.375357+00:00

这份 P24 规格已经很完整，可以直接作为制作依据。整体逻辑是对的：**P23 提出局限，P24 给出逐项对应的改进方向，P25 再总结已经完成的工作与核心认识。**

我建议正式制作前确认两个细节：

1. **结论带必须明确标注「未来目标」**，避免“建立计算预测、基准校准与实验验证相互衔接的评价闭环”被误读为已经完成的成果。英文句保留 `Toward an iterative cycle...`，也能体现这是未来方向。
2. **三张卡片的文字要以可读性优先。** 卡 1 和卡 3 的第三条偏长，按你指定的位置手动换行；若仍有溢出，优先微调条目间距或文本框高度，不要随意缩小统一的 12pt bullet 字号。

其余建议严格遵守你给出的规格，尤其是保留“探索将实验结果反馈到候选排序与评价规则中”的表述，不要改成已经建立反馈闭环。

P24 的最终收束句建议保持：

**未来目标：建立计算预测、基准校准与实验验证相互衔接的评价闭环。**

这样就能自然转入 P25 Conclusion，不会把未来计划与当前成果混在一起。

### user — `<UUID>` — 2026-10-18T03:11:07.387000+00:00

下一张

### assistant — `<UUID>` — 2026-10-18T03:11:10.702430+00:00

下一张是 **P25 · 11 · CONCLUSION｜结论**。

这页是整份报告的收束页。与 P24 不同，不能再列未来计划，而要回答三个问题：我们完成了什么、通过基准评价认识到了什么、项目贡献究竟是什么。

## P25 页面内容建议

<box gap={3}>
  <box gap={1}>
    <text color="secondary" size="xs">页面标题</text>
    <title size="xl">11 · CONCLUSION｜结论</title>
    <text color="secondary" size="sm">KEY FINDINGS AND PROJECT CONTRIBUTIONS</text>
    <text>本项目围绕从头蛋白结合剂设计，建立计算流程，并通过已知对照分析结构评价指标的适用边界。</text>
  </box>
  <grid columns={3} gap={3}>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">01</title>
        <title size="md">建立计算设计流程</title>
        <text color="secondary" size="xs">COMPUTATIONAL DESIGN PIPELINE</text>
        <divider color="subtle" />
        串联靶点准备、骨架生成、序列设计、结构预测与界面评价，形成候选筛选流程。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">02</title>
        <title size="md">识别指标判别局限</title>
        <text color="secondary" size="xs">LIMITS OF STRUCTURAL SCORES</text>
        <divider color="subtle" />
        已知对照表明，单一结构置信度分数不足以独立判断真实结合能力，指标需要结合基准解释。
      </box>
    </grid-item>
    <grid-item>
      <box border radius="lg" padding={3} gap={2} height="100%">
        <title size="lg">03</title>
        <title size="md">提出基准校准思路</title>
        <text color="secondary" size="xs">BENCHMARK-CALIBRATED EVALUATION</text>
        <divider color="subtle" />
        以已知阳性与阴性对照为参照，结合多方面结构证据，为候选排序与后续验证提供依据。
      </box>
    </grid-item>
  </grid>
  <box background="surface-secondary" radius="lg" padding={3} gap={1}>
    <title size="md">核心结论</title>
    **我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证。**
    <text color="secondary" size="sm">The goal is not to maximize scores, but to evaluate whether computational evidence justifies further validation.</text>
  </box>
</box>

## 这页最重要的边界

- **可以说**：建立了计算设计与评价流程，发现特定已知对照下单一指标存在判别局限，并提出基准校准的评价思路。
- **不能说**：已经证明多指标方法更准确、成功设计了实验验证的 binder，或提高了实验成功率。
- **不要再放 AUC、1BRS 等具体数字**：这些结果已经属于前面的证据与分析部分，结论页应当总结认识，而不是再引入案例。

这页完成后，P26 `ACK & AUTHOR CONTRIBUTIONS` 再介绍致谢和实际贡献分工即可。

### user — `<UUID>` — 2026-10-18T03:11:20.659000+00:00

提示词

### assistant — `<UUID>` — 2026-10-18T03:11:24.179270+00:00

下面是 P25 的完整制作提示词，延续 P21–P24 的视觉规范，并突出项目的实际贡献与结论边界。

<WritingBlock id="72519" variant="document">请制作 AI-BinderDesign 科研报告主 deck 第 25 页：**11 · CONCLUSION｜结论**，保存为独立单页 PowerPoint 文件 `Slides-32-Conclusion-v1.pptx`。如需生成脚本，命名为 `_gen_110conclusion_v1_slide.py`。

本任务只制作这一张幻灯片，不修改其他页面，不重新编排主 deck。

## 一、页面定位

本页是整份报告的结论页，承接 P24 `10 · FUTURE WORK｜未来工作`。

本页需要回答三个问题：

1. 项目建立了什么计算流程？
2. 基准评价揭示了什么方法学认识？
3. 项目的实际贡献与结论边界是什么？

核心叙事：

**从头蛋白结合剂设计流程 → 单一结构指标的判别局限 → 基准校准与多维证据评价思路。**

本页总结已经完成的工作与目前能够支持的认识，不再列未来计划，也不重复前面各页的详细实验或基准数字。

## 二、视觉与版式要求

完全沿用 P21、P22、P23、P24 的视觉语言：

- 16:9 宽屏，白色背景，上海交大红色作为强调色。
- 顶部眉行：左侧章节编号与中英文名称，右侧 `AI-BINDERDESIGN · RESEARCH REPORT`。
- 中文主标题 24pt，深灰色、加粗。
- 英文副标题使用 Georgia 12pt，上海交大红色。
- 中文导语 12pt，深灰色。
- 中部三张等宽白色卡片，水平并排，卡片宽度约 3.70 in，保持统一高度、间距和内边距。
- 卡片使用轻量边框、左侧竖色条、卡内分隔细线。
- 三张卡片编号、中文标题、英文小标题和正文层级一致。
- 竖色条依次使用浅灰、上海交大红、深灰。
- 页面底部设置浅粉色结论带，使用前几页同款底色、边框与圆角风格。
- 底部保留细线，保持留白，确保投影展示时文字清晰。
- 不使用装饰性插画、复杂流程图或大面积图形。

## 三、标题与导语

页眉左侧：

`11 · CONCLUSION ｜ 结论`

右上角：

`AI-BINDERDESIGN · RESEARCH REPORT`

中文主标题：

**核心结论与项目贡献**

英文副标题：

`KEY FINDINGS AND PROJECT CONTRIBUTIONS`

中文导语：

本项目围绕从头蛋白结合剂设计，建立计算流程，并通过已知对照分析结构评价指标的适用边界。

## 四、三张卡片文案

### 卡片 01

编号：`01`

中文标题：**建立计算设计流程**

英文小标题：`COMPUTATIONAL DESIGN PIPELINE`

正文：

串联靶点准备、骨架生成、序列设计、结构预测与界面评价，形成候选筛选流程。

### 卡片 02

编号：`02`

中文标题：**识别指标判别局限**

英文小标题：`LIMITS OF STRUCTURAL SCORES`

正文：

已知对照表明，单一结构置信度分数不足以独立判断真实结合能力，指标需要结合基准解释。

### 卡片 03

编号：`03`

中文标题：**提出基准校准思路**

英文小标题：`BENCHMARK-CALIBRATED EVALUATION`

正文：

以已知阳性与阴性对照为参照，结合多方面结构证据，为候选排序与后续验证提供依据。

## 五、底部结论带

中文核心句：

**我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证。**

英文辅助句：

`The goal is not to maximize scores, but to evaluate whether computational evidence justifies further validation.`

排版要求：

- 中文结论为视觉主体，字号约 17pt，加粗。
- 可将“判断计算证据是否足以支持候选进入下一步验证”设为上海交大红色，其余文字使用深灰色。
- 英文辅助句使用 Georgia 11pt，深灰色。
- 结论带不应挤压卡片正文或页脚。

## 六、科研准确性与诚信边界

1. 不得编造候选成功率、实验亲和力、实验活性或任何未经验证的结果。
2. 不得声称多指标评价已被实验验证为更准确。
3. 不得声称已经成功设计并实验验证了 binder，除非有明确实验数据支持。
4. 不得声称本流程提高了实验成功率。
5. 可以总结计算流程已经建立、已知对照揭示的指标局限，以及基准校准的评价思路。
6. 不要在本页重新引入 AUC、1BRS、DockQ 或其他具体基准数值。
7. 不要重复 P24 的未来工作清单。
8. 不新增未经确认的章节编号，不修改其他幻灯片。
9. 结论措辞应区分“建立了计算流程”“观察到特定对照下的判别局限”和“提出评价思路”，不能把方法学认识夸大成已经验证的设计成功。

## 七、交付前检查

- 确认文件为 16:9、可编辑的 PowerPoint 单页。
- 确认三张卡片等宽、对齐、层级一致。
- 检查中文正文无溢出、重叠或字号异常。
- 确认底部结论带完整呈现中英文内容。
- 确认结论只总结当前工作，不混入未来计划。
- 确认没有修改其他页面的内容与编号。</WritingBlock>

P25 的作用是把前面的流程、基准案例和讨论收束为一个清晰的项目贡献，而不是宣称已经获得实验成功的 binder。下一页 P26 再单独呈现致谢与实际贡献分工。

### user — `<UUID>` — 2026-10-18T03:27:55.322000+00:00

11 · CONCLUSION｜结论（v1）
页面位置：主 deck 第 25 页（P25），承接第 24 页（10 · FUTURE WORK），是整份报告的收束页。
版式文件：Slides-32-Conclusion-v1.pptx（独立单页存档），生成脚本 _gen_110conclusion_v1_slide.py。
版面语言：与 P21–P24 完全同构——眉行（左 11 · CONCLUSION ｜ 结论 + 右上 AI-BINDERDESIGN · RESEARCH REPORT）、24pt 中文主标题、Georgia 12pt 英文副题、12pt 导语、三等宽白卡（3.70 in，圆角 0.04，左竖色条）、卡内分隔细线、粉底结论带（PINKP + PINKL 1.5pt）、底部细线；bullet 12pt、行距 1.10（沿用 P24 v6）。
与 P24 的分界：P24 列未来计划，本页只总结已完成的工作与目前能够支持的认识，不再出现任何计划性条目，也不带「未来目标」标签。
一、数据层（逐条 + 来源）
本页不含任何数值——禁词含 AUC / 1BRS / DockQ / 94,167 / 0.9813 / ipTM / pLDDT / PAE / nM / μM / mM / Kd = / n=，28 项全部不在页。这是用户明确要求：基准数值属于前面的证据与分析部分，结论页总结认识，不再引入案例。
#
页面文字
类型
来源 / 依据
1
建立计算设计流程
团队结论（已完成）
对应 P4/P8 的计算流程链：靶点准备 → 骨架生成 → 序列设计 → 结构预测 → 界面评价
2
串联靶点准备、骨架生成、序列设计、结构预测与界面评价，形成候选筛选流程
团队结论（已完成）
流程各环节在 P4/P8/P13 已展开
3
识别指标判别局限
团队结论（观察到的）
对应 P10/P11（EGFR）与 P14–P19（TNF-α）的对照结果
4
已知对照表明，单一结构置信度分数不足以独立判断真实结合能力，指标需要结合基准解释
团队结论（观察到的）
限定为"已知对照表明"，不外推为普遍定理
5
提出基准校准思路
团队结论（方法论提出）
对应 P12（3.6 RESOLUTION）与 P21（7 · MULTI-METRIC DECISION）
6
以已知阳性与阴性对照为参照，结合多方面结构证据，为候选排序与后续验证提供依据
团队结论（方法论提出）
多指标联合判定；"后续验证"是用途说明，不是未来计划清单
7
我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证
团队结论（核心句）
用户指定文案
8
The goal is not to maximize scores, but to evaluate whether computational evidence justifies further validation.
英文核心句
用户指定文案
事实 / 团队自设规则 / 模型预测三分标注：
- 事实（实测数值）：本页无。
- 团队自设规则：全部条目。
- 模型预测：本页不展示任何模型预测值。
二、白话层（讲人话：这页在说什么）
这页在干什么：回答三个问题——我们做了什么、从基准里认识到了什么、贡献是什么。三张卡就是这三个答案，且是严格的递进：
1. 01 建立计算设计流程 —— 做出来了什么：一条从靶点准备到界面评价的完整计算流程，能跑出候选。
2. 02 识别指标判别局限 —— 从已知对照里看到了什么：单一结构置信度分数（如 ipTM 一类）不足以独立判断真实结合能力，指标必须结合基准来解释。
3. 03 提出基准校准思路 —— 由此提出什么：以已知阳性/阴性对照为参照，结合多方面结构证据来排候选、决定谁先进入验证。
核心结论：「我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证。」这句话是整个项目的方法论立场——把"要更高分"转成"要更可靠的证据"。
措辞的分寸（本页最关键）：三条分别用「建立」「识别/观察」「提出」——完成 → 观察到 → 提出思路，三层强度递减，没有一层越界到"已验证"。
闭环故事线：…→ P23 本项目缺口 → P24 未来计划 → P25 收束：已完成的工作 + 已获得的认识 + 贡献定位 → P26 ACK & AUTHOR CONTRIBUTIONS。
三色竖条：浅灰 → 交大红 → 深灰，与 P21–P24 一致；其中 02「识别指标判别局限」用红强调——它是本项目最核心的发现。
三、诚信边界（本页不得越线）
- 不得引入任何基准数值：AUC、1BRS、DockQ、ipTM、pLDDT、PAE 一律不出现——这些属于前面的证据与分析部分。
- 不得编造候选成功率、实验亲和力、实验活性或任何未经验证的结果。
- 不得声称"多指标评价已被实验验证为更准确"。
- 不得声称"已经成功设计并实验验证了 binder"。
- 不得声称"本流程提高了实验成功率"。
- 措辞三层分级，不能把方法学认识夸大成设计成功：「建立了计算流程」（完成时）／「已知对照表明…不足以…」（观察时）／「提出…思路」（提案时）。
- 不重复 P24 的未来工作清单；本页不含任何计划性条目，结论带不设「未来目标」标签（那是 P24 的）。
- 不新增未经确认的章节编号，不改动其他页。
四、版面参数（复刻用）
元素
几何 / 字号
眉行左
x0.70 y0.42 w9.50，13pt 雅黑粗，交大红
眉行右
x7.90 y0.42 w4.73，右对齐，10pt 雅黑，浅灰
主标题
x0.70 y0.78 w11.93，24pt 雅黑粗，深灰
英文副题
x0.70 y1.28，Georgia 12pt，交大红
导语
x0.70 y1.58，12pt 雅黑，深灰
三卡
y1.90 h3.70 w3.70，gap 0.415；x = 0.70 / 4.815 / 8.93
竖色条
w0.05 与卡同高；01 浅灰 / 02 交大红 / 03 深灰
序号
22pt Georgia 粗，与竖条同色
卡标题
14pt 雅黑粗，深灰
英文小标
9pt Georgia，浅灰（全大写）
bullet
12pt 雅黑，行距 1.10（与 P24 v6 一致），条目间距 0.06，圆点 0.07 in
分段（手动，每段一行）
卡1 串联靶点准备、骨架生成、 ／ 序列设计、结构预测与界面评价， ／ 形成候选筛选流程。；卡2 已知对照表明，单一结构置信度分数 ／ 不足以独立判断真实结合能力，指标 ／ 需要结合基准解释。；卡3 以已知阳性与阴性对照为参照， ／ 结合多方面结构证据，为候选 ／ 排序与后续验证提供依据。——三卡各 3 行，结构统一；每段 ≤18 字（≤216pt，行宽上限 222pt）
bullet 起点
y3.36，三段依次 +0.302
结论带
x0.70 y6.05 w11.93 h0.95，PINKP 底 + PINKL 1.5pt 边，圆角 0.05
结论主句
17pt 雅黑粗，「判断计算证据是否足以支持候选进入下一步验证」标红，y6.18
结论英文
Georgia 11pt，深灰，y6.60
底部线
x0 y7.44 w13.333 h0.02，PINKL
标签
无（P24 有「未来目标」，本页是核心结论，不设）

### assistant — `<UUID>` — 2026-10-18T03:27:58.977540+00:00

这版 P25 的逻辑已经比较完整，可以作为结论页的制作规格。最重要的是三张卡的递进关系：**完成了什么 → 从对照中观察到什么 → 提出了什么方法思路**，而不是把计算流程包装成已经验证成功的 binder 设计成果。

我建议正式生成前只检查两个细节：

1. **卡片标题与内容保持一一对应。**  
   - 01 建立计算设计流程：对应已完成的流程搭建。
   - 02 识别指标判别局限：限定在已知对照所呈现的现象。
   - 03 提出基准校准思路：定位为方法论思路，而非已经验证有效的新方法。

2. **核对卡片正文的实际换行。**  
   你给出的三组手动分行可作为初始排版，但中文字体、字号和项目符号缩进都会影响实际行宽。生成后应检查是否溢出、是否出现孤行，以及三张卡的正文起点和行距是否一致。

其余约束建议原样保留：不出现基准数值、不重复 P24 的未来计划、不添加实验验证或成功率方面的结论，也不修改其他页面。

**建议最终保留的核心句：**

> 我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证。

它能把整个项目的主线收束到「证据是否可靠」，同时没有越过当前工作的验证边界。

如果接下来要实际生成或修改 `Slides-32-Conclusion-v1.pptx` 和 `_gen_110conclusion_v1_slide.py`，需要在 Work 模式中执行文件操作。

### user — `<UUID>` — 2026-10-18T03:28:29.225000+00:00

卡内文字能否再丰富一点

### assistant — `<UUID>` — 2026-10-18T03:28:32.730059+00:00

可以。我建议把三张卡从目前的「一句话概括」扩充为**每张卡 3 条 bullet**，但不要单纯增加字数，而是补足每一层的具体含义：第一张说清楚流程做了什么，第二张解释对照揭示了什么，第三张说明基准校准如何指导候选判断。

这样 P25 会更像一张有实质内容的研究总结页，而不是只有标题的收尾页，同时仍然保持「建立 → 识别 → 提出」的诚信边界。

## P25 三张卡的扩充文案建议

<box gap={3}>
  <box border radius="lg" padding={4} gap={2}>
    <row align="center" gap={3}>
      <title size="lg" color="#8A8A8A">01</title>
      <box flex="1" gap={1}>
        <title size="md">建立计算设计流程</title>
        <text color="secondary" size="xs">COMPUTATIONAL DESIGN PIPELINE</text>
      </box>
    </row>
    <divider color="subtle" />
    - 串联靶点准备、骨架生成、序列设计、结构预测与界面评价。
    - 将多个计算环节整合为连续的候选设计与筛选流程。
    - 为后续结构分析、候选比较与证据整理提供统一工作框架。
    <text color="secondary" size="xs">总结重点：从分散的工具与步骤，形成可执行的计算工作流。</text>
  </box>
  <box border radius="lg" padding={4} gap={2}>
    <row align="center" gap={3}>
      <title size="lg" color="#C7353A">02</title>
      <box flex="1" gap={1}>
        <title size="md">识别指标判别局限</title>
        <text color="secondary" size="xs">LIMITS OF STRUCTURAL SCORES</text>
      </box>
    </row>
    <divider color="subtle" />
    - 已知对照表明，阴性对照也可能获得较高的结构置信度分数。
    - 单一分数难以独立区分真实结合物与非结合对照。
    - 分数的解释需要结合对照结果、具体靶点与评价任务。
    <text color="secondary" size="xs">总结重点：高分不等于真实结合，分数的判别意义需要证据支持。</text>
  </box>
  <box border radius="lg" padding={4} gap={2}>
    <row align="center" gap={3}>
      <title size="lg" color="#555555">03</title>
      <box flex="1" gap={1}>
        <title size="md">提出基准校准思路</title>
        <text color="secondary" size="xs">BENCHMARK-CALIBRATED EVALUATION</text>
      </box>
    </row>
    <divider color="subtle" />
    - 以具有明确生物学依据的阳性与阴性对照作为评价参照。
    - 综合结构可信度、界面接触与界面几何等不同方面的证据。
    - 据此比较和排序候选，为确定优先验证对象提供依据。
    <text color="secondary" size="xs">总结重点：从单纯比较分数，转向结合基准解释多方面计算证据。</text>
  </box>
</box>

## 这样扩充的优势

- **卡片 01 更具体：** 不只说「建立了流程」，还交代整合了哪些环节、流程有什么用途。
- **卡片 02 更有研究发现的分量：** 从现象、判别局限到解释原则，形成完整论证；其中「阴性对照也可能获得较高分」应确保与前面实际展示的对照结果一致。
- **卡片 03 更有方法贡献：** 交代基准、证据维度和候选排序三者之间的关系，但不声称多指标方法已经被实验验证为更准确。

## 版面上需要同步调整

你原先规定每张卡的正文严格为 3 行，这个限制不再适合扩充版。建议仍然保持**每张卡 3 条 bullet**，但每条允许自然换成 1–2 行，卡片内部采用统一的悬挂缩进与段间距。若三张卡空间不足，优先缩短措辞或略微压缩卡片标题与英文小标之间的留白，不要先把正文字号降得太小。

底部结论带仍然保留原句，不再重复三张卡的内容：

> 我们的目标不是追求更高的分数，而是判断计算证据是否足以支持候选进入下一步验证。

这样页面会更充实，但核心信息仍然集中在「流程建设、指标认识、校准思路」这三个贡献上。

### user — `<UUID>` — 2026-10-18T03:57:30.823000+00:00

下一张

### assistant — `<UUID>` — 2026-10-18T03:57:38.430990+00:00

下一张是主 deck 第 26 页（P26）：**ACK & AUTHOR CONTRIBUTIONS｜致谢与作者贡献**。

这页与 P25 的任务不同：P25 收束研究结论，P26 则交代项目协作背景与贡献分工。建议继续采用前面统一的视觉体系，以中文为主、英文为辅，但内容不再重复研究结论，也不新增实验成果。

作者贡献部分采用**分类式贡献声明**，把实际工作按职责归类；没有确认的作者姓名、团队成员或具体分工，不能自行补写。

下面是可直接交给制作工具的 P26 提示词。由于具体作者名单和分工尚未确认，先用待填写字段占位，避免把推测写成正式作者贡献。

<WritingBlock id="63821" variant="document"># P26 · ACK & AUTHOR CONTRIBUTIONS｜致谢与作者贡献

## 页面定位
- 主 deck 第 26 页，紧接 P25 Conclusion。
- 页面标题：`ACK & AUTHOR CONTRIBUTIONS｜致谢与作者贡献`
- 独立单页存档：`Slides-33-Acknowledgements-v1.pptx`
- 生成脚本：`_gen_120_acknowledgements_v1_slide.py`
- 本页是主报告最后一页；Appendix A–E 作为附录，不计入主 deck 页数。

## 一、设计目标

延续 P21–P25 的统一视觉体系：
- 16:9 白色背景，保持简洁、正式的科研报告风格。
- 交大红作为强调色，深灰作为正文色，浅灰作为辅助色。
- 左上眉行：`12 · ACK & AUTHOR CONTRIBUTIONS ｜ 致谢与作者贡献`
- 右上眉行：`AI-BINDERDESIGN · RESEARCH REPORT`
- 中文为主，英文为辅助。
- 字体、页边距、细线、卡片圆角和整体留白与前页协调。
- 不需要大面积装饰、图片或复杂图示；以清晰的信息组织为主。

## 二、页面结构

### 1. 标题区

中文主标题：

**致谢与作者贡献**

英文副标题：

`ACKNOWLEDGEMENTS & CONTRIBUTIONS`

导语：

`本项目由团队协作完成，以下按工作类别说明项目中的主要贡献。`

### 2. 致谢区

使用独立的浅色区域或简洁卡片，标题为：

**致谢｜ACKNOWLEDGEMENTS**

正文采用待填写字段，不得自行补写姓名、机构、导师或资助信息：

- 指导与支持：`[待确认：指导教师、导师或支持人员]`
- 团队协作：`[待确认：团队名称或成员]`
- 其他支持：`[待确认：平台、计算资源或其他实际支持；无则删除此项]`

只保留经用户确认的条目。没有实际发生的支持不得写入。

### 3. 作者贡献区

标题：

**作者贡献｜AUTHOR CONTRIBUTIONS**

采用分类式贡献声明。可使用三张小卡片或整齐的两栏布局，视觉上与前页保持一致。

**计算流程与工具实施**
`[待确认：实际负责的流程搭建、软件运行、参数配置或计算任务]`

**基准与结构评价**
`[待确认：实际负责的已知对照整理、指标分析、结果核查或评价方法设计]`

**项目整合与报告撰写**
`[待确认：实际负责的数据整理、图表制作、报告撰写或项目协调]`

上述分类只是待核实的组织框架，不代表这些工作已经由某位作者完成。根据实际分工修改、合并或删除条目，不得把团队共同完成的工作直接写成某一人的独立贡献。

如果需要列出作者姓名，采用以下格式：

- `[作者姓名]` — `[经确认的具体贡献]`
- `[作者姓名]` — `[经确认的具体贡献]`
- `[作者姓名]` — `[经确认的具体贡献]`

姓名与贡献必须逐一对应；不得虚构作者顺序、通讯作者身份或贡献声明。

### 4. 页底收束

使用与 P25 结论带协调的浅粉色底框，但降低视觉强调程度。

中文：

**感谢所有为本项目提供实际贡献与支持的参与者。**

英文：

`We thank all contributors for their support and collaboration.`

这句话仅在项目确有相应参与者与支持时保留；如需更正式的致谢，依据用户确认的信息修改。

## 三、诚信与内容约束

1. 不得编造作者姓名、团队成员、导师、机构、资助来源或贡献分工。
2. 不得自动认定项目负责人、第一作者或通讯作者。
3. 不得将团队工作全部归为单人贡献。
4. 不得将计算预测表述为实验验证成果。
5. 不重复 P25 的研究结论，也不在本页新增结果、指标或实验声明。
6. 所有 `[待确认]` 字段在正式定稿前必须由用户核实；未确认的条目应删除或继续保留为明显占位，不得伪装成最终内容。
7. 不修改 P1–P25，不改变附录 A–E 的编号和组织方式。

## 四、版式要求

- 眉行、标题区和底部细线与 P21–P25 保持一致。
- 致谢与作者贡献在视觉上明确分区，避免密集的长段落。
- 作者贡献以短句呈现，突出“工作类别—具体工作”的对应关系。
- 不为凑齐三张卡片而虚构贡献；实际信息较少时，使用两栏或简洁列表。
- 优先保证可读性和事实准确性，不要为了填满页面而增加无关内容。

输出独立单页文件 `Slides-33-Acknowledgements-v1.pptx` 及生成脚本 `_gen_120_acknowledgements_v1_slide.py`，不要覆盖主 deck 或修改其他页面。</WritingBlock>

**定稿前只需要你补充一个关键信息：** 你们团队的作者姓名，以及你本人实际负责了哪些工作。你可以直接把现有分工记录发来；我会据此把占位内容改成准确、正式的贡献声明。

### user — `<UUID>` — 2026-10-18T04:53:08.823000+00:00

分工参考：本人主要负责计算评价体系、benchmark 构建与候选筛选分析，其中两组对照基准体系的设计与分析、评价指标判别力标定由作者主导完成；蛋白设计生成、换靶点流程工程与湿实验方案由团队成员完成
团队

团队成员：长江杯团队 · 成员及分工汇总

> 整理依据：种子团队申请材料（B3 节，2026-10-06 草稿）、李佳林-全流程组任务文档、交接说明、巡检记录。 最近更新：2026-10-18（**领队修正为黄兆锟**；**补入班级信息，人工智能组新增朱博**——班级信息据 QQ 群成员列表 2026-10-18 核对）。

## 一、团队基本信息

|   |
| - |

项目

|   |
| - |

内容

|   |
| - |

团队名称

|   |
| - |

上海交通大学长江杯竞赛团队

|   |
| - |

参赛赛事

|   |
| - |

"长江杯" 2026 全球 AI 蛋白质设计挑战赛（上海交大主办）

|   |
| - |

团队规模

|   |
| - |

**14 人**（2026 级本科 11 人 / 2024 级本科 2 人 / 2020 级本科 1 人；朱博、于乐为新增成员）

|   |
| - |

指导老师

|   |
| - |

**刘振华**（农业与生物学院，日常指导）＋ **洪亮**（Venus 蛋白质设计模型团队负责人，经何欣老师推荐配备）

|   |
| - |

**领队 / 联系人**

|   |
| - |

**黄兆锟**（⚠️ 原 10-06 申请材料写"吕俊赫（统筹）"，已调整为黄兆锟）

## 二、12 人名单

|   |
| - |

年级

|   |
| - |

专业

|   |
| - |

人数

|   |
| - |

姓名（班级）

|   |
| - |

2026 级本科

|   |
| - |

生命科学

|   |
| - |

7

|   |
| - |

黄兆锟（生科2603）、杨子文（生科2601）、薛尧宣（生科2602）、张航齐（生科2602）、吕俊赫（生科2603）、李佳林（生科2603）、李逸天（生科2603）

|   |
| - |

2026 级本科

|   |
| - |

生物医学科学

|   |
| - |

1

|   |
| - |

余喆（生医科2650）

|   |
| - |

2026 级本科

|   |
| - |

人工智能

|   |
| - |

2

|   |
| - |

许多（人工智能2605）、**朱博（AI 2601）★新增**

|   |
| - |

2024 级本科

|   |
| - |

生命科学

|   |
| - |

2

|   |
| - |

贺程然（生科24）、郝嘉颖（生科24）

|   |
| - |

2020 级本科

|   |
| - |

生物医学工程

|   |
| - |

1

|   |
| - |

刘泽霖（生医工20）

|   |
| - |

**2026 级本科**

|   |
| - |

医学检验技术（医技26）

|   |
| - |

1

|   |
| - |

**于乐（医技26）★新增**

|   |
| - |

**合计**

|   |
| - |

—

|   |
| - |

**14**

|   |
| - |

—

> 背景：其中 **9 人有生物竞赛背景**，2 人有 PRP 和大创经验。 ⚠️ 朱博（AI 2601）、于乐（医技26）两位新增成员的五组归属待定，确认后更新本表。

## 三、五组并行分工

|   |
| - |

小组

|   |
| - |

成员

|   |
| - |

任务范围

|   |
| - |

背景调研组

|   |
| - |

余喆、张航齐

|   |
| - |

EGFR 及其信号通路；已有靶向 EGFR 药物的作用机理

|   |
| - |

pH 响应结构元件调研组

|   |
| - |

李逸天、黄兆锟

|   |
| - |

天然 pH 响应元件；可设计单元；人为设计路线及设计思想

|   |
| - |

跨物种结合宽泛性调研组

|   |
| - |

杨子文、薛尧宣

|   |
| - |

天然跨物种结合案例；保证跨物种宽泛性的技术与方法

|   |
| - |

全流程组

|   |
| - |

李佳林、刘泽霖

|   |
| - |

从靶点到 binder 的全流程环节、输入/输出与技术栈

|   |
| - |

IT 组

|   |
| - |

许多、吕俊赫

|   |
| - |

技术栈试用；让功能结构"首次生成即被加入序列"

## 四、关键个人角色

|   |
| - |

成员

|   |
| - |

角色 / 职责

|   |
| - |

**黄兆锟**

|   |
| - |

**团队领队、统筹**；pH 响应元件组；负责官方问询（章程 / 评分口径等 4 个未答问题）；交我算子账号 `huangzhk` 持有者

|   |
| - |

吕俊赫

|   |
| - |

IT 组；负责 PPT 上传、会议组织等会务（原 10-06 材料的"统筹/联系人"角色，现为队员）

|   |
| - |

李佳林

|   |
| - |

全流程组 · 层级筛选漏斗与判据设计（L0–L7）

|   |
| - |

刘泽霖

|   |
| - |

全流程组 · 算力、作业脚本与工具链落地；协调 AutoDL（约 ¥5,600 余额 + 可协调 ≤4,000 元）与 A6000 / 3090 显卡

|   |
| - |

杨子文

|   |
| - |

跨物种组；主导 VHH 批次实验（362 条）；三方对照（EGF / cetuximab / 7D12）

|   |
| - |

许多

|   |
| - |

IT 组；"伪一体机"流水线主要搭建者之一

## 五、两点说明

1. **分工是动态的**：原计划 pH 元件组 3 人，目前只有 2 人（李逸天、黄兆锟），是全团队唯一未满编的小组。

1) **交叉角色**：李佳林同时与杨子文合作三方对照（B3 任务）；刘泽霖也参与全流程组分工表制定，存在跨组协作。

## 六、来源与勘误

- 团队成员名单、五组分工、指导老师：种子团队申请材料 B3 节（2026-10-06 草稿）。

* 各人具体职责：李佳林-全流程组任务文档、交接说明（给下一个 Agent）、巡检记录（2026-10-16）。

- **勘误**：领队由"吕俊赫（统筹）"更正为 **黄兆锟**（2026-10-18 团队确认）。

* **班级信息**：据 QQ 群成员列表（2026-10-18 12:11 截图）逐人核对；朱博（AI 2601）、于乐（医技26）为新增成员，已并入名单。

注意这里的分工是调研时的分工，跟实际分工并不匹配，实际的分工情况比较复杂，因为有人潜水，主要干活的几个干的又比较杂，除了我本人的分工，你需要知道其他人做了什么具体工作吗

### assistant — `<UUID>` — 2026-10-18T04:53:12.985369+00:00

**需要，但不需要你把 14 个人的工作全部查清楚。** 对 P26 来说，最重要的是准确呈现你的个人贡献，同时不抹去其他实际参与者的工作，也不把最初的计划分工误写成最终的实际分工。

结合你提供的信息，我建议把这页定位为：**团队致谢 + 个人贡献声明**，而不是全员逐人列功劳。

## 1. 目前已经能够确定的内容

<box border radius="lg" padding={3} gap={3}>
  <row align="start" gap={3}>
    <box background="#F2F2F2" radius="md" size="40px" align="center" justify="center">
      <icon name="users" size="xl" color="#555555" />
    </box>
    <box flex="1" gap={1}>
      **团队层面**

      <text color="secondary" size="sm">上海交通大学长江杯竞赛团队</text>
      感谢实际参与项目的团队成员，以及经确认的指导教师和模型团队支持人员。具体致谢措辞需与实际提供的指导或支持相符。
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="#FCE8E8" radius="md" size="40px" align="center" justify="center">
      <icon name="microscope" size="xl" color="#B4232D" />
    </box>
    <box flex="1" gap={1}>
      **你的个人贡献**

      <text color="secondary" size="sm">COMPUTATIONAL EVALUATION & BENCHMARKING</text>
      - 主导两组对照基准体系的设计与分析。
      - 负责计算评价体系与评价指标判别力标定。
      - 负责候选筛选分析，并将基准分析形成方法论总结。
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="#F2F2F2" radius="md" size="40px" align="center" justify="center">
      <icon name="workflow" size="xl" color="#555555" />
    </box>
    <box flex="1" gap={1}>
      **团队其他贡献**

      蛋白设计生成、换靶点流程工程与湿实验方案由团队成员完成。具体到个人的归属，暂时不做推断。
    </box>
  </row>
</box>

这已经足够搭建 P26 的基本结构。尤其要保留你在 benchmark 构建与判别力分析上的主导贡献，不应被笼统地压缩成“参与计算评价”。

## 2. 我还需要了解其他人的工作吗？

需要了解一部分，但只需要补充**确实影响作者贡献表述的信息**，不需要追查每个人的所有细节。

最有价值的是以下三类：

- **蛋白设计生成：** 谁实际完成了 RFdiffusion、ProteinMPNN、结构预测、候选生成或相关计算？
- **流程工程：** 谁实际负责换靶点流程、脚本、算力部署和工具链整合？
- **实验相关工作：** 谁完成了实验方案设计、实验准备或实际实验？要明确区分“设计方案”和“完成实验”。

对于其他人，如果只是参加调研、偶尔提供意见，或者原本分到了任务但实际上没有完成，就不必为了名单完整而强行列入某一项贡献。也不需要在结论页上公开评价谁做得多、谁做得少。

## 3. 你可以这样补充给我

不用重新整理成表格，直接用几句话描述即可：

{@body const [generation,setGeneration] = DIL.useState("")}
{@body const [engineering,setEngineering] = DIL.useState("")}
{@body const [wetlab,setWetlab] = DIL.useState("")}
{@body const [other,setOther] = DIL.useState("")}
<box border radius="xl" padding={4} gap={4}>
  <text weight="medium">① 蛋白设计生成由谁实际负责？</text>
  <textarea value={generation} onChange={setGeneration} placeholder="例如：某几位负责 RFdiffusion、ProteinMPNN、ColabFold/Boltz-2，谁负责 EGFR、TNF-α 等具体任务。" rows={3} />
  <text weight="medium">② 换靶点流程工程由谁实际负责？</text>
  <textarea value={engineering} onChange={setEngineering} placeholder="例如：谁搭建脚本、部署环境、跑通跨靶点流程，谁负责算力和工具链。" rows={3} />
  <text weight="medium">③ 湿实验方案与实验工作由谁负责？</text>
  <textarea value={wetlab} onChange={setWetlab} placeholder="例如：谁设计实验方案、联系实验资源、执行实验；如果尚未开展实验，也请直接说明。" rows={3} />
  <text weight="medium">④ 还有哪些必须被准确体现的个人贡献？（选填）</text>
  <textarea value={other} onChange={setOther} placeholder="例如：某位成员主导了重要对照、某人负责项目统筹，或存在需要特别说明的共同工作。" rows={3} />
  <button block onClick={() => GenUI.issueNewTurn("请根据以下实际分工信息完善 AI-BinderDesign 主 deck P26 致谢与作者贡献页。不要把原始计划分工当作实际分工，不要虚构个人贡献。请区分个人主导、团队共同完成和待确认内容，并输出正式中文为主、英文为辅的页面文案。\n\n① 蛋白设计生成：\n"+(generation.trim()||"暂未补充")+"\n\n② 换靶点流程工程：\n"+(engineering.trim()||"暂未补充")+"\n\n③ 湿实验方案与实验工作：\n"+(wetlab.trim()||"暂未补充")+"\n\n④ 其他个人贡献：\n"+(other.trim()||"暂未补充")+"\n\n已确认：本人主要负责计算评价体系、benchmark 构建与候选筛选分析；两组对照基准体系的设计与分析、评价指标判别力标定由本人主导。蛋白设计生成、换靶点流程工程与湿实验方案由团队成员完成。团队共有 14 人，指导教师为刘振华，另有洪亮提供相关模型团队指导支持；实际致谢范围仍需以实际参与和支持为准。原有小组分工只是调研时计划，不能直接当作实际分工。")}>提交实际分工</button>
</box>

**我的建议是：P26 不必列出 14 个人的详细贡献。** 最稳妥的呈现方式是用一块区域简洁致谢团队与指导支持，再用一块区域明确说明你的 benchmark 与计算评价贡献，并用一句话概括团队在设计生成、工程和实验方案方面的协作。这样既能体现你真正主导的研究工作，也不会因为实际分工复杂而错误归属他人成果。

### user — `<UUID>` — 2026-10-18T04:54:46.983000+00:00

这个其实有点说不清楚怎么办

### assistant — `<UUID>` — 2026-10-18T04:54:52.132271+00:00

那就不要强行把每个人的贡献梳理清楚。**P26 完全可以不做逐人贡献表，改成「团队致谢 + 本人研究贡献」**。对于你这份研究报告，这样反而更稳妥：既突出你真正完成的工作，也避免把原定分工误当成实际贡献。

你现在已经能明确说清楚自己主导了什么，不需要为了写致谢而承担梳理整个团队工作量的任务。

## 我建议 P26 这样设计

<box border radius="xl" padding={4} gap={3}>
  <text color="secondary" size="xs" weight="medium">ACK & AUTHOR CONTRIBUTIONS</text>
  <title size="xl">致谢与个人贡献</title>
  <text color="secondary" size="sm">ACKNOWLEDGEMENTS & CONTRIBUTIONS</text>
  <divider color="subtle" />
  <title size="md">团队协作｜TEAM COLLABORATION</title>
  本项目由上海交通大学长江杯竞赛团队协作开展，涵盖蛋白设计生成、计算流程工程、候选评价与实验方案等工作环节。
  <text color="secondary" size="sm">不逐人划分贡献，不将初始计划分工视为最终实际分工。</text>
  <divider color="subtle" />
  <title size="md">本人主要贡献｜MY CONTRIBUTIONS</title>
  <list marker="bullet" gap={2}>
    <list-item>**计算评价体系：** 参与建立并完善候选评价与筛选框架。</list-item>
    <list-item>**基准构建与分析：** 主导两组对照基准体系的设计与分析。</list-item>
    <list-item>**指标判别力标定：** 分析已知对照中的指标表现，研究结构评价分数的判别局限。</list-item>
    <list-item>**候选筛选分析：** 将基准分析与结构评价结果用于候选比较，并总结相应的方法学认识。</list-item>
  </list>
  <divider color="subtle" />
  <title size="md">致谢｜ACKNOWLEDGEMENTS</title>
  感谢团队成员在项目实施过程中的协作，以及指导教师和相关支持人员提供的指导与帮助。
</box>

上面是内容结构示意，正式排版时仍按 P21–P25 的视觉规范制作。

## 为什么我更推荐这种写法？

- **你的贡献是具体且可核实的。** 不需要依赖其他人的工作记录，也能说明你在项目中的研究角色。
- **不夸大个人贡献。** 你主导的是 benchmark 和评价体系相关工作，不会把蛋白生成、工程部署和实验方案都写成自己完成。
- **不制造团队内部的贡献排名。** 没必要公开比较谁做得多、谁做得少。
- **符合研究报告的定位。** 你要展示的是自己对项目形成了什么研究贡献，而不是提交一份团队绩效考核表。

有一个细节值得注意：如果 P26 的标题保留 **AUTHOR CONTRIBUTIONS**，最好将其理解为对你本人研究贡献的说明，而不是完整的全体作者贡献声明。如果这份报告需要正式投稿或作为多人共同署名的论文附件，则应另外核实所有作者的实际贡献。

**我的最终建议：保留团队层面的简短致谢，重点呈现你的四项研究贡献，不再追查全部 14 人的分工。** 这已经足够支撑一张清晰、可信的收尾页。

### user — `<UUID>` — 2026-10-18T04:55:21.919000+00:00

那就搞个致谢名单吧

### assistant — `<UUID>` — 2026-10-18T04:55:25.690433+00:00

可以。既然实际分工比较复杂，P26 就改成单纯的**致谢名单（Acknowledgements）**，不再逐人声明贡献。这样既能感谢整个团队，也不用推断每个人具体做了什么。

我建议名单分成三个层级：**团队成员、指导教师、其他支持**。其中团队成员可以列全，指导教师按你提供的资料列出，其他支持只在确认后加入。

## P26 · 致谢名单｜ACKNOWLEDGEMENTS

<box border radius="xl" padding={4} gap={3}>
  <title size="lg">致谢</title>
  <text color="secondary" size="sm">ACKNOWLEDGEMENTS</text>
  <text>谨向参与本项目的团队成员、指导教师及提供支持的相关人员致以诚挚感谢。</text>
  <divider color="subtle" />
  <title size="md">项目团队｜PROJECT TEAM</title>
  <text color="secondary" size="sm">上海交通大学长江杯竞赛团队</text>
  <grid columns={2} gap={2}>
    {#each ["黄兆锟","杨子文","薛尧宣","张航齐","吕俊赫","李佳林","李逸天","余喆","许多","朱博","贺程然","郝嘉颖","刘泽霖","于乐"] as name}
      <grid-item>
        <box background="surface-secondary" radius="md" padding={2}>
          <text>{name}</text>
        </box>
      </grid-item>
    {/each}
  </grid>
  <divider color="subtle" />
  <title size="md">指导教师｜SUPERVISORS</title>
  <box background="surface-secondary" radius="md" padding={3}>
    <text weight="medium">刘振华</text>
    <text color="secondary" size="sm">上海交通大学农业与生物学院</text>
  </box>
  <box background="surface-secondary" radius="md" padding={3}>
    <text weight="medium">洪亮</text>
    <text color="secondary" size="sm">Venus 蛋白质设计模型团队</text>
  </box>
  <divider color="subtle" />
  <text color="secondary" size="sm">感谢所有为项目提供指导、协作与支持的老师和同学。</text>
</box>

## 排版建议

- 延续 P21–P25 的白底、交大红、深灰与浅灰风格。
- 14 位团队成员采用双栏名单，不列班级、不列职务、不按贡献排序。
- 两位指导教师放在下方独立区域。
- 不写“全体成员均深度参与”等无法确认的表述，也不需要加入贡献排名。
- 如果还有需要致谢的赛事组织方、实验平台或其他支持人员，可以确认后再添加，不必为了凑名单而补充。

有一点需要注意：这份名单依据你提供的团队汇总整理，正式放入报告前，最好再确认 14 位成员的姓名和两位指导教师的署名方式是否符合团队最终意见。

### user — `<UUID>` — 2026-10-18T04:55:56.926000+00:00

提示词

### assistant — `<UUID>` — 2026-10-18T04:56:00.666049+00:00

下面是可直接交给制作工具的 P26 完整提示词，沿用 P21–P25 的视觉体系，制作**纯致谢名单页**，不再涉及作者贡献划分。

<WritingBlock id="58316" variant="document"># P26 · ACKNOWLEDGEMENTS｜致谢名单（v1）

## 页面定位

- 主 deck 第 26 页（P26），承接 P25 Conclusion，作为主报告最后一页。
- 页面标题：`ACKNOWLEDGEMENTS｜致谢`
- 独立单页存档：`Slides-33-Acknowledgements-v1.pptx`
- 生成脚本：`_gen_120_acknowledgements_v1_slide.py`
- 本页只呈现致谢名单，不制作作者贡献声明，不评价个人贡献大小。
- 附录 A–E 不计入主 deck 页数，不修改其他页面。

## 一、设计目标

延续 P21–P25 的视觉体系：

- 16:9 白色背景，正式、简洁的科研报告风格。
- 交大红作为强调色，深灰作为正文色，浅灰作为辅助色。
- 左上眉行：`12 · ACKNOWLEDGEMENTS ｜ 致谢`
- 右上眉行：`AI-BINDERDESIGN · RESEARCH REPORT`
- 中文为主，英文为辅。
- 字体、页边距、细线和整体留白与 P21–P25 保持一致。
- 本页不需要复杂图示、照片、图标墙或装饰性插画。
- 不出现 `AUTHOR CONTRIBUTIONS`，避免让页面看起来像正式的全体作者贡献声明。

## 二、页面内容

### 1. 标题区

中文主标题：

**致谢**

英文副标题：

`ACKNOWLEDGEMENTS`

导语：

`谨向参与本项目的团队成员、指导教师及提供支持的相关人员致以诚挚感谢。`

### 2. 项目团队｜PROJECT TEAM

团队名称：

`上海交通大学长江杯竞赛团队`

将以下 14 位成员全部列出，不标注个人职务、班级或贡献排名：

- 黄兆锟
- 杨子文
- 薛尧宣
- 张航齐
- 吕俊赫
- 李佳林
- 李逸天
- 余喆
- 许多
- 朱博
- 贺程然
- 郝嘉颖
- 刘泽霖
- 于乐

排版要求：

- 使用双栏名单，尽量均衡分布。
- 所有人名字使用相同字号、字重和视觉层级。
- 不使用排名数字、奖牌、星标或突出某位成员的特殊颜色。
- 不按照推测的贡献大小排序；可采用整齐、均衡的排布。
- 不显示班级信息，避免名单过于拥挤。

### 3. 指导教师｜SUPERVISORS

列出：

**刘振华**

`上海交通大学农业与生物学院`

**洪亮**

`Venus 蛋白质设计模型团队`

排版要求：

- 两位指导教师放在独立区域，与项目团队名单明确区分。
- 姓名清晰可读，机构或团队信息使用较小的浅灰文字。
- 不擅自添加教授、博士生导师、项目顾问等未确认头衔。
- 不将指导关系描述为具体的技术贡献，除非有额外确认。

### 4. 页底致谢语

中文：

**感谢所有为项目提供指导、协作与支持的老师和同学。**

英文：

`We thank all team members, supervisors, and supporters for their guidance and collaboration.`

使用简洁的浅粉色底框，延续前几页的视觉语言，但弱化强调程度，避免与 P25 的研究结论带产生相同的视觉重心。

## 三、版式结构

采用以下从上到下的布局：

1. 顶部眉行。
2. 中文主标题与英文副标题。
3. 一行中文导语。
4. 项目团队区域：团队名称 + 14 人双栏名单。
5. 指导教师区域：两位教师姓名及所属机构或团队。
6. 底部简短致谢语。
7. 页面底部细线。

整体留白应充分，名单不应挤压标题区或底部致谢语。

具体排版原则：

- 延续 P21–P25 的页边距、标题字号、英文字体和配色。
- 团队成员可使用两列、每列七人；若实际字距或卡片尺寸不合适，可调整为其他均衡布局。
- 指导教师区域不必使用与团队名单同样密集的卡片，可以采用更简洁的双栏或横向布局。
- 所有姓名必须完整显示，不换行拆分姓名。
- 底部致谢语不宜过长，保持克制、正式。

## 四、内容与诚信约束

1. 不编造其他成员、导师、机构、资助来源或外部合作单位。
2. 不添加未经确认的作者顺序、通讯作者身份、职务和学术头衔。
3. 不将初始任务分组当作最终实际分工。
4. 不评价谁贡献最大，也不将某位成员单独突出。
5. 不在本页重复研究结果、基准数值、评价指标或实验结论。
6. 不把团队致谢页包装成正式的作者贡献声明。
7. 不修改 P1–P25，不改变附录 A–E 的组织方式。

## 五、输出要求

- 输出独立单页文件：`Slides-33-Acknowledgements-v1.pptx`
- 输出对应生成脚本：`_gen_120_acknowledgements_v1_slide.py`
- 不覆盖主 deck，不修改其他页面。
- 生成后检查所有姓名是否完整、双栏是否均衡、指导教师信息是否准确，以及页面是否与 P21–P25 保持一致。

本页的核心原则：**感谢实际参与和支持项目的人，不推断个人贡献，不做团队内部排名。**</WritingBlock>

### user — `<UUID>` — 2026-10-18T05:08:05.650000+00:00

# 12 · ACKNOWLEDGEMENTS｜致谢（v1）

**页面位置**：主 deck 第 26 页（P26，最后一页），承接第 25 页（11 · CONCLUSION）。 **版式文件**：`Slides-33-Acknowledgements-v1.pptx`（**独立单页，未合并进主 deck**），生成脚本 `_gen_120_acknowledgements_v1_slide.py`，校验 `_check_p26_v1.py`。 **本页性质**：纯致谢名单。**不做作者贡献声明、不逐人划分贡献、不排名、不评价贡献大小**（用户 12:56 明确：实际分工复杂，强行梳理易把初始计划分工误写成实际分工）。

## 用户三条修正的执行

|   |
| - |

修正

|   |
| - |

执行

|   |
| - |

修正眉行章节编号

|   |
| - |

眉行用 `12 · ACKNOWLEDGEMENTS ｜ 致谢`，接 P25 的 11，序列连续

|   |
| - |

简化重复的排版要求

|   |
| - |

提示词中「不排名数字/不奖牌/不星标/不特殊颜色/不显示班级/不按贡献排序」等约束在版面上一次性落实，不逐条堆砌；名单只用统一字号 + 浅灰小圆点，无任何差异化装饰

|   |
| - |

统一指导关系措辞

|   |
| - |

两位指导教师用**完全相同的格式**：姓名 13.5pt 粗深灰 + 机构/团队 10.5pt 浅灰；**不添加教授/博导/研究员等任何未确认头衔**；不把指导关系描述为具体技术贡献

---

## 一、内容清单（全部来自用户提供，无一项推断）

|   |
| - |

区块

|   |
| - |

内容

|   |
| - |

眉行

|   |
| - |

`12 · ACKNOWLEDGEMENTS ｜ 致谢` ＋ 右上 `AI-BINDERDESIGN · RESEARCH REPORT`

|   |
| - |

主标题 / 副题

|   |
| - |

致谢 ／ ACKNOWLEDGEMENTS

|   |
| - |

导语

|   |
| - |

谨向参与本项目的团队成员、指导教师及提供支持的相关人员致以诚挚感谢。

|   |
| - |

项目团队

|   |
| - |

团队名：上海交通大学长江杯竞赛团队

|   |
| - |

14 人名单

|   |
| - |

黄兆锟、杨子文、薛尧宣、张航齐、吕俊赫、李佳林、李逸天、余喆、许多、朱博、贺程然、郝嘉颖、刘泽霖、于乐

|   |
| - |

指导教师

|   |
| - |

刘振华 — 上海交通大学农业与生物学院；洪亮 — Venus 蛋白质设计模型团队

|   |
| - |

页底致谢语

|   |
| - |

感谢所有为项目提供指导、协作与支持的老师和同学。／ We thank all team members, supervisors, and supporters for their guidance and collaboration.

**名单顺序**：严格按用户所给顺序，左栏前 7 人、右栏后 7 人，**未按贡献重排、未排序**。

---

## 二、诚信边界（本页不得越线）

- 不编造其他成员、导师、机构、资助来源或外部合作单位。

* 不添加未经确认的作者顺序、通讯作者身份、职务和学术头衔（禁词含教授/博士生导师/硕士生导师/研究员/通讯作者/第一作者/共同作者，22 项全部不在页）。

- 不将初始任务分组当作最终实际分工；不写"全体成员均深度参与"等无法确认的表述。

* 不评价谁贡献最大，不把任何成员单独突出（所有人同字号、同字重、同装饰）。

- 不在本页重复研究结果、基准数值、评价指标或实验结论。

* 不把团队致谢页包装成正式的作者贡献声明。

- 不修改 P1–P25，不改变附录 A–E 的组织方式。

* **遗留待确认**：正式放入报告前需再核对 14 位成员姓名用字与两位指导教师署名方式是否符合团队最终意见；若本报告要作为多人共同署名论文附件，应另行核实全体作者实际贡献。

---

## 三、版面参数（复刻用）

|   |
| - |

元素

|   |
| - |

几何 / 字号

|   |
| - |

眉行左

|   |
| - |

x0.70 y0.42 w9.50，13pt 雅黑粗，交大红

|   |
| - |

眉行右

|   |
| - |

x7.90 y0.42 w4.73，右对齐，10pt 雅黑，浅灰

|   |
| - |

主标题

|   |
| - |

x0.70 y0.78 w11.93，24pt 雅黑粗，深灰

|   |
| - |

英文副题

|   |
| - |

x0.70 y1.28，Georgia 12pt，交大红

|   |
| - |

导语

|   |
| - |

x0.70 y1.58，12pt 雅黑，深灰

|   |
| - |

区块标签

|   |
| - |

y1.98 / y5.08；中文 11.5pt 雅黑粗交大红 + `　｜　` 10pt 浅灰 + 英文 9.5pt Georgia 浅灰；标签下方 0.012 in PLINE 细线（通栏 0.70–12.63）

|   |
| - |

团队名

|   |
| - |

x0.70 y2.38，14pt 雅黑粗，深灰

|   |
| - |

14 人名单

|   |
| - |

双栏 x0.70 / x6.90，栏宽 5.60；起点 y2.86，行高 0.295；小圆点 0.055 in 浅灰 + 姓名 12pt 雅黑深灰

|   |
| - |

指导教师

|   |
| - |

两位横向并排（x0.70 / x6.90，栏宽 5.60）；姓名 y5.50 13.5pt 粗深灰；机构/团队 y5.82 10.5pt 浅灰

|   |
| - |

页底致谢语

|   |
| - |

x0.70 y6.32 w11.93 h0.68，**PANEL 底 + PLINE 0.75pt 边、圆角 0.04**（刻意弱化，不用 P21–P25 的粉底红边，避免与 P25 结论带争视觉重心）；中文 y6.42 12pt；英文 y6.70 Georgia 10.5pt 中灰

|   |
| - |

底部细线

|   |
| - |

x0 y7.44 w13.333 h0.02，PINKL

|   |
| - |

卡片

|   |
| - |

**本页不用三卡结构**（P21–P25 的三卡语言不适用于名单页）

### assistant — `<UUID>` — 2026-10-18T05:08:12.196862+00:00

这版规格已经把三条修正落实到位：章节编号连续、名单严格按给定顺序排列、指导教师使用完全一致的格式。下面整理成可直接交给制作工具的最终提示词。

<WritingBlock id="61482" variant="document"># P26 · ACKNOWLEDGEMENTS｜致谢（v1 最终制作提示词）

## 一、任务与文件

制作 AI-BinderDesign 主 deck 的最后一页：P26 致谢名单。

- 页面位置：主 deck 第 26 页，承接 P25 `11 · CONCLUSION`。
- 独立单页文件：`Slides-33-Acknowledgements-v1.pptx`
- 生成脚本：`_gen_120_acknowledgements_v1_slide.py`
- 校验脚本：`_check_p26_v1.py`
- 页面性质：纯致谢名单，不制作作者贡献声明，不逐人划分贡献，不排名或评价贡献大小。
- 画布比例：16:9。
- 本次只制作独立单页，不合并进主 deck，不修改 P1–P25，不调整附录 A–E。

## 二、整体风格

沿用 P21–P25 的科研报告视觉语言，但根据致谢名单的内容采用简洁的分区布局，而非三卡结构。

- 白色背景，交大红用于章节眉行、区块标签等少量强调。
- 深灰用于标题和正文，浅灰用于辅助文字与名单圆点。
- 中文为主，英文为辅。
- 字体、页边距和整体视觉风格与前页一致。
- 指导教师并排呈现，姓名字号、字重和机构文字格式完全相同。
- 不使用人物照片、装饰性插画、排名标记或突出个别成员的视觉元素。
- 页面应正式、克制、清晰，充分利用留白。

## 三、页面文案

### 1. 顶部眉行

左侧：

`12 · ACKNOWLEDGEMENTS ｜ 致谢`

右侧：

`AI-BINDERDESIGN · RESEARCH REPORT`

章节编号使用 12，接续 P25 的 11，不修改其他页面的编号。

### 2. 标题区

中文主标题：

**致谢**

英文副标题：

`ACKNOWLEDGEMENTS`

导语：

`谨向参与本项目的团队成员、指导教师及提供支持的相关人员致以诚挚感谢。`

### 3. 项目团队｜PROJECT TEAM

区块标签：

`项目团队　｜　PROJECT TEAM`

团队名称：

`上海交通大学长江杯竞赛团队`

团队成员名单必须严格按照以下顺序呈现：

左栏，从上到下：

1. 黄兆锟
2. 杨子文
3. 薛尧宣
4. 张航齐
5. 吕俊赫
6. 李佳林
7. 李逸天

右栏，从上到下：

1. 余喆
2. 许多
3. 朱博
4. 贺程然
5. 郝嘉颖
6. 刘泽霖
7. 于乐

共 14 人，姓名用字必须与以上名单一致，不增删、不调序。

名单采用双栏布局。每位成员使用相同字号、字重、文字颜色和浅灰色小圆点。两栏行高一致，视觉上均衡整齐。

### 4. 指导教师｜SUPERVISORS

区块标签：

`指导教师　｜　SUPERVISORS`

两位指导教师横向并排，采用完全相同的排版格式。

左侧：

**刘振华**

`上海交通大学农业与生物学院`

右侧：

**洪亮**

`Venus 蛋白质设计模型团队`

姓名均使用 13.5pt 粗体深灰，机构或团队信息均使用 10.5pt 浅灰。两组内容顶部对齐，间距一致。

不得添加未经确认的学术头衔或职务，不将指导关系扩写为具体技术贡献。

### 5. 页底致谢语

使用浅色背景的简洁横向区域，弱化视觉强调，不使用前面研究内容页的粉底红边结论带。

中文：

**感谢所有为项目提供指导、协作与支持的老师和同学。**

英文：

`We thank all team members, supervisors, and supporters for their guidance and collaboration.`

保留中文与英文两行，确保英文完整显示且不与边框或其他元素重叠。

## 四、精确版面参数

画布：13.333 × 7.5 in。

| 元素 | 位置与样式 |
|---|---|
| 左侧眉行 | x=0.70，y=0.42，w=9.50；13pt 雅黑粗体，交大红 |
| 右侧眉行 | x=7.90，y=0.42，w=4.73；10pt 雅黑，浅灰，右对齐 |
| 中文主标题 | x=0.70，y=0.78，w=11.93；24pt 雅黑粗体，深灰 |
| 英文副标题 | x=0.70，y=1.28；Georgia 12pt，交大红 |
| 导语 | x=0.70，y=1.58；12pt 雅黑，深灰 |
| 区块标签 | y=1.98 和 y=5.08；中文 11.5pt 粗体交大红，英文 9.5pt Georgia 浅灰，中间使用浅灰分隔符 |
| 标签分隔线 | 各标签下方，x=0.70 至 x=12.63；0.012 in，PLINE |
| 团队名称 | x=0.70，y=2.38；14pt 雅黑粗体，深灰 |
| 名单左栏 | x=0.70，栏宽 5.60；起点 y=2.86 |
| 名单右栏 | x=6.90，栏宽 5.60；起点 y=2.86 |
| 名单行高 | 0.295 in；两栏各 7 人 |
| 名单文字 | 12pt 雅黑，深灰；浅灰圆点直径 0.055 in |
| 指导教师左栏 | x=0.70，栏宽 5.60 |
| 指导教师右栏 | x=6.90，栏宽 5.60 |
| 指导教师姓名 | y=5.50；13.5pt 粗体，深灰 |
| 机构或团队信息 | y=5.82；10.5pt，浅灰 |
| 底部致谢区域 | x=0.70，y=6.32，w=11.93，h=0.68 |
| 致谢区域样式 | PANEL 底色，PLINE 0.75pt 边框，圆角 0.04 |
| 中文致谢语 | y=6.42；12pt 雅黑 |
| 英文致谢语 | y=6.70；Georgia 10.5pt，中灰 |
| 页面底部细线 | x=0，y=7.44，w=13.333，h=0.02；PINKL |

如果实际渲染的字体度量与预期略有差异，可以微调文本框高度和文字基线，但必须保留上述区块顺序、名单顺序、字号层级和整体布局。

## 五、内容与诚信边界

1. 本页仅为致谢名单，不出现 `AUTHOR CONTRIBUTIONS`。
2. 不把初始计划分工写成最终实际分工。
3. 不推断谁贡献最大，不突出任何一位团队成员。
4. 不添加班级、职务、作者顺序、通讯作者身份或未经确认的学术头衔。
5. 不编造其他团队成员、机构、资助来源或外部合作单位。
6. 不添加研究结果、基准数值、评价指标或实验结论。
7. 不修改 P1–P25，不改变附录 A–E 的组织方式。
8. 14 位成员严格按给定顺序排列：左栏前 7 人，右栏后 7 人。
9. 两位指导教师必须使用完全相同的视觉格式。
10. 不为了填满页面添加额外装饰或未经确认的内容。

## 六、生成与校验

生成独立单页文件 `Slides-33-Acknowledgements-v1.pptx` 和脚本 `_gen_120_acknowledgements_v1_slide.py`，并运行 `_check_p26_v1.py`。

校验项目：

- 页面比例正确，所有元素均在画布范围内。
- 章节编号为 12，与 P25 连续。
- 14 位团队成员姓名完整、顺序正确、没有重复或遗漏。
- 左右两栏各 7 人，名单格式一致。
- 两位指导教师的姓名、机构或团队信息准确，样式一致。
- 中英文文字没有溢出、遮挡或异常换行。
- 底部致谢区域与页面底线之间留白合理。
- 不包含作者贡献声明、排名、个人贡献评价或未经确认的信息。
- 独立单页文件成功生成，未覆盖主 deck 或其他页面。

最终效果应是一张简洁、均衡、正式的科研报告致谢页：以团队名单为主体，以指导教师名单为辅助，以简短致谢语收尾。</WritingBlock>

### user — `<UUID>` — 2026-10-18T05:32:24.951000+00:00

下一张

### assistant — `<UUID>` — 2026-10-18T05:32:28.443803+00:00

主 deck 到 P26「致谢」已经结束。下一张如果继续制作，就进入 **Appendix A｜Metric Definitions & Data Dictionary（指标定义与数据字典）**，属于附录，不计入主 deck 页数。

建议先做 Appendix A，作为前面结构评价与 benchmark 分析的技术参考页，主要说明指标的含义、解释边界与数据字段，不重复前文的案例结果。

你之前规划的附录顺序是：

- **Appendix A** — Metric Definitions & Data Dictionary（指标定义与数据字典）
- **Appendix B** — Threshold Calibration（阈值校准表；尚未完成的内容需明确标注）
- **Appendix C** — Wet-lab Interface（湿实验衔接与验证方案）
- **Appendix D** — Reproducibility & Engineering Details（可复现性与工程细节）
- **Appendix E** — Full Five-target Data（五个靶点的完整数据）

**建议下一步制作 Appendix A。** 先确认指标清单与实际计算字段，再决定排版，避免把没有实际计算的指标写成已有结果。

### user — `<UUID>` — 2026-10-18T05:32:53.383000+00:00

提示词

### assistant — `<UUID>` — 2026-10-18T05:32:57.744916+00:00

下面是 Appendix A 的完整制作提示词。它与 P1–P26 主报告分开，作为技术参考附录，重点是**解释指标、统一术语、定义数据字段与解释边界**，不把未实际计算的指标写成项目结果。

<WritingBlock id="74621" variant="document"># APPENDIX A · METRIC DEFINITIONS & DATA DICTIONARY（v1）

## 页面定位

- 所属部分：AI-BinderDesign 报告附录 A。
- 英文标题：`APPENDIX A · METRIC DEFINITIONS & DATA DICTIONARY`
- 中文标题：`指标定义与数据字典`
- 文件名：`Slides-A1-Metric-Definitions-v1.pptx`
- 生成脚本：`_gen_A1_metric_definitions_v1.py`
- 本页属于附录，不计入主 deck P1–P26 的页码。
- 独立制作，不合并或修改主 deck。
- 目的：让读者理解报告使用的结构评价指标、数据字段、术语含义与解释边界。

## 一、设计原则

沿用主报告的视觉语言，但明确体现附录的技术参考属性：

- 16:9 白色背景。
- 交大红用于标题与少量重点强调，深灰用于正文，浅灰用于注释和分隔线。
- 中文为主，英文术语为辅。
- 页面保持清晰、可查阅，避免过多装饰。
- 使用结构化表格与分组信息，不使用主报告的三卡式叙事布局。
- 如果内容无法在一页内清晰呈现，可以拆为 A1、A2 等连续附录页，不得为了压缩页数而将正文缩得过小。
- 不改变主报告 P1–P26 的编号与内容。

## 二、建议内容结构

### 1. 标题区

中文标题：

**指标定义与数据字典**

英文副标题：

`METRIC DEFINITIONS & DATA DICTIONARY`

导语：

`本附录统一说明结构评价指标与数据字段的含义，并明确其适用范围及解释边界。`

### 2. 结构评价指标｜STRUCTURAL EVALUATION METRICS

使用表格呈现以下候选指标。只有在项目资料中确认实际使用的指标才可标记为“本项目使用”；其余标为“补充参考”或删除。

| 指标 | 英文名称 | 含义与用途 | 解释边界 |
|---|---|---|---|
| ipTM | Interface predicted TM score | 反映预测复合物中界面相对排列的可信程度 | 不能单独证明真实结合或实验亲和力 |
| PAE | Predicted Aligned Error | 表示模型预测中残基相对位置的不确定性；应注明具体使用的是哪一类 PAE 汇总值 | 必须明确所用残基范围、链间区域与聚合方式 |
| pLDDT | Predicted Local Distance Difference Test | 反映局部结构预测可信度 | 局部结构可信不等于界面正确或真实结合 |
| pDockQ2 | pDockQ2 interface confidence score | 用于评估预测蛋白复合物界面的可信程度 | 依赖其定义与输入结构；不是实验亲和力测量 |
| Interface contacts | 界面接触数 | 描述按指定距离规则统计的界面残基或原子接触 | 必须注明距离阈值、原子/残基口径与去重规则 |
| Interface SASA | Interface solvent-accessible surface area | 描述复合物形成界面时溶剂可及表面积的变化 | 必须明确使用总界面面积还是单侧/其他口径 |
| Interface geometry | 界面几何特征 | 描述界面形状、接触分布或几何互补性 | 需要明确具体算法或计算定义，不能仅凭名称推断数值 |

注意：
- 该表是候选结构指标字典，不代表所有指标均已在本项目中计算。
- `Interface geometry` 是指标类别，不是单一、标准化的数值指标；如没有明确算法，应将其标为定性评价维度。
- 不得自行填写通用阈值、分数范围、性能排名或实验相关性。
- 不得把结构置信度分数写成结合亲和力或功能活性的直接测量。

### 3. 数据字段字典｜DATA FIELDS

以第二张表说明每个候选、每次预测或每个评价结果应记录的基本字段。

| 字段 | 含义 | 记录要求 |
|---|---|---|
| `target_id` | 靶点标识 | 使用统一、可追溯的靶点名称或 ID |
| `candidate_id` | 候选标识 | 对每个候选使用唯一标识 |
| `control_type` | 对照类型 | 记录阳性对照、阴性对照或其他明确类别 |
| `model` | 预测工具或模型 | 记录实际使用的工具与版本（可获得时） |
| `run_config` | 运行配置 | 记录与结果解释有关的参数设置 |
| `seed` | 随机种子 | 仅在实际设置或可获取时记录 |
| `metric_name` | 指标名称 | 使用统一的指标命名 |
| `metric_value` | 指标值 | 保留原始值与对应单位/定义，不混用不同计算口径 |
| `structure_file` | 结构文件标识或路径 | 确保能够追溯到对应预测结构 |
| `analysis_status` | 分析状态 | 区分已完成、待复核、未计算等状态 |

上述字段是建议的数据字典框架。若现有数据仓库采用不同字段名，应优先保留现有实际字段，并在必要时增加映射关系，不得虚构已经存在的数据列。

### 4. 解释原则｜INTERPRETATION PRINCIPLES

页面底部使用简洁的提示区域，呈现三条原则：

- **分数不是实验结论。** 结构预测指标只能提供相应范围内的计算证据。
- **定义决定解释。** 任何数值都必须结合其计算口径、输入结构与运行条件理解。
- **基准决定判别意义。** 指标能否区分已知阳性与阴性对照，需要依据实际基准结果进行评估。

## 三、诚信边界

1. 本附录是指标与字段说明，不是新的结果页。
2. 不得编造指标数值、阈值、统计量、AUC、实验亲和力或实验成功率。
3. 不得将尚未计算的指标标记为已计算。
4. 不得将建议字段描述成当前数据文件中必然存在的字段。
5. 不得将预测结构置信度解释为真实结合、激动、抑制或实验亲和力的直接证据。
6. 不得把某个独立方法学基准的结果外推为所有靶点均适用的结论。
7. 对需要具体定义的指标，必须标注计算口径或保留待确认状态。
8. 不添加未经确认的工具版本、参数、距离阈值或数据处理规则。

## 四、制作与核验要求

- 先核对项目现有报告、数据表与分析脚本，确认实际使用的指标、字段名及计算定义。
- 对无法从现有材料确认的内容，标记为“待确认”，或从最终表格中删除。
- 指标定义与数据字段应分成不同表格，避免概念混淆。
- 表格字号应保证在 16:9 演示画面中清晰可读。
- 若单页信息过密，优先拆成两页：
  - Appendix A1：Metric Definitions
  - Appendix A2：Data Dictionary & Interpretation Principles
- 输出独立 PPTX 与完整生成脚本，不修改主 deck。

本附录的核心原则：**统一指标的含义与使用口径，让每个计算结果都能追溯、解释并接受基准检验。**</WritingBlock>

**一个关键提醒：** 这份提示词中的指标清单是候选字典，并不代表你已经计算了全部指标。正式生成前，应以实际数据表和脚本为准，尤其核对 PAE 的统计口径、界面接触的距离定义，以及 pDockQ2 和界面面积是否确实纳入当前流程。

### user — `<UUID>` — 2026-10-18T05:47:10.895000+00:00

这个要放进报告吗

### assistant — `<UUID>` — 2026-10-18T05:47:16.743005+00:00

**建议放进附录，但不建议把刚才那份内容原样全部放进去。** 对你这份 AI-BinderDesign 报告来说，附录应该帮助读者复核研究，而不是把所有技术术语都罗列一遍。

你目前主报告已经到 P26，接下来最重要的是让附录补充证据、提高可复现性，而不是重复主报告。

## 我的建议

| 内容 | 是否放入 | 原因 |
|---|---|---|
| A1 指标定义 | 有条件保留 | 解释主报告中实际使用的指标，方便读者理解 |
| A2 数据字典 | 暂不单独放 | 如果没有公开、规范的数据表，通用字段清单的价值有限 |
| 指标解释边界 | 保留精简版 | 强化报告核心观点：结构分数不是实验结论 |
| 未实际计算的指标 | 不放入正式结果说明 | 容易让读者误以为这些指标已被项目使用 |
| 工具版本、参数和运行条件 | 放在可复现性附录 | 前提是有实际记录可核对 |

## 更适合你的附录结构

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="book-open" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Appendix A — Metric Definitions**

      <text color="secondary" size="sm">建议保留，1 页</text>

      只解释主报告确实出现的指标，例如 ipTM、PAE，以及实际计算并用于分析的界面指标。注明每个指标反映什么、不能说明什么。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="database" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Appendix B — Full Benchmark Data**

      <text color="secondary" size="sm">建议保留，价值较高</text>

      展示真实的阳性与阴性对照数据、靶点、运行条件和计算结果。重点是让读者能核对你关于“分数需要校准”的结论。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="terminal" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Appendix C — Reproducibility & Engineering Details**

      <text color="secondary" size="sm">按材料完整程度决定</text>

      放实际使用的模型、参数、随机种子、运行配置和分析脚本说明。没有记录的内容不要补写成事实。
    </box>
  </row>
</box>

TNF-α 控制实验、1BRS 方法学基准、PD-L1 等跨靶点测试，如果确实属于报告证据，也可以分别放进完整数据或方法学补充部分；要清楚区分它们的用途，不能混成同一套验证结果。

**我的最终判断：** 指标定义页值得保留，但不必为了形式完整而加入通用数据字典。对你这份报告，**真实基准数据、评价方法和可复现性证据，比指标百科更重要。**

下一步最合理的是先整理 Appendix A 的实际指标清单，再决定是否需要单独的数据字典页。

### user — `<UUID>` — 2026-10-18T05:48:02.812000+00:00

那就是说报告还是保持26张？

### assistant — `<UUID>` — 2026-10-18T05:48:06.601417+00:00

对，**主报告保持 26 张，不需要再增加正文页。**

但要区分两件事：

- **主报告：26 张**，P26 致谢作为最后一页。
- **附录：按需添加**，放在主报告之后，独立编号，不计入这 26 张。

我建议最终结构是：

| 部分 | 内容 | 处理方式 |
|---|---|---|
| P1–P26 | 正式研究报告 | 保持不变 |
| Appendix A | 实际使用的指标定义 | 建议保留，1 页 |
| Appendix B | 完整基准数据与对照结果 | 建议保留 |
| Appendix C | 可复现性与工程细节 | 根据现有材料决定 |
| 其他补充材料 | 1BRS、跨靶点测试等 | 只保留对研究论证有价值的部分 |

**不必为了凑齐附录而增加页面。** 如果完整基准数据和可复现性信息已经在 GitHub 仓库中清楚呈现，PPT 附录只需保留最有价值的摘要与必要的核验信息。

这样主报告的叙事保持紧凑，附录负责提供技术细节，两者各司其职。

### user — `<UUID>` — 2026-10-18T05:48:28.313000+00:00

那这个附录是单独一个pdf吗

### assistant — `<UUID>` — 2026-10-18T05:48:31.942688+00:00

不一定。**我更建议把附录放在主报告 PDF 的最后面，同时保留一个独立的附录文件用于技术资料。** 具体取决于你打算怎么使用这份报告。

| 使用场景 | 推荐做法 |
|---|---|
| 联系上海交大导师、申请进组、展示研究经历 | **主报告单独导出 PDF，保持 26 张** |
| 导师希望核查你的数据、方法和计算细节 | 另外提供附录 PDF 或 GitHub 仓库 |
| 正式汇报，需要完整展示研究证据 | 将精选附录接在主报告 PDF 后面，形成完整版 |

## 我建议你最终准备这三个文件

<box border radius="lg" padding={3} gap={3}>
  <row align=start gap={3}>
    <icon name="file-text" size="2xl" color="secondary" />
    <box flex="1" gap={1}>
      **01 · AI-BinderDesign_Report.pdf**

      <badge color="success">主要文件</badge>

      <text color="secondary" size="sm">26 张正文，完整讲清研究问题、你的评价工作、基准发现、局限与未来方向。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="files" size="2xl" color="secondary" />
    <box flex="1" gap={1}>
      **02 · AI-BinderDesign_Appendix.pdf**

      <text color="secondary" size="sm">精选附录：指标定义、真实基准数据、关键方法和可复现性信息。内容必须来自实际材料，不为凑页数而制作。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="github" size="2xl" color="secondary" />
    <box flex="1" gap={1}>
      **03 · GitHub Repository**

      <text color="secondary" size="sm">存放代码、数据说明、运行配置、分析脚本和版本记录，让项目不只是一份 PPT。</text>
    </box>
  </row>
</box>

**为什么这样安排？**

你希望这项长江杯工作最终成为能够用于联系 AI-for-Science / 蛋白质设计课题组的正式研究项目。对于这种用途，正文应该让导师快速理解你的研究贡献；附录和 GitHub 则在导师想深入了解时，提供进一步核验的材料。

所以，现阶段先把 **26 张主报告定稿**，不要因为附录而改动正文结构。附录单独整理，等数据和代码材料核实后再导出 PDF。

### user — `<UUID>` — 2026-10-18T05:49:42.544000+00:00

我的意思就是附录要不要放进AI-BinderDesign_Report.pdf这个PPT里继续做P27、P28……

### assistant — `<UUID>` — 2026-10-18T05:49:46.838674+00:00

明白了。你的意思是：**附录是否直接接在现有 PPT 的 P26 后面，继续做成 P27、P28……，然后统一导出 `AI-BinderDesign_Report.pdf`。**

我的建议是：**可以放在同一个 PPT 文件里，但附录不继续沿用正文页码体系，也不计入 26 张主报告。**

具体做法：

- **P1–P26：** 正式报告正文，P26 致谢结束。
- **Appendix A、Appendix B……：** 直接接在 P26 后面，作为附录页，不标成正文的 P27、P28。
- **导出 PDF：** 整份 PPT 统一导出为 `AI-BinderDesign_Report.pdf`，附录自然位于 PDF 最后。

这样只维护一份 PPT，正文和附录也能一起交付；同时，读者仍然能清楚地区分正式汇报内容和技术补充材料。

如果你之后需要向导师发送更精简的版本，再从同一份 PPT 中单独导出 P1–P26 即可。

**因此，下一步可以直接在现有 PPT 后面制作 Appendix A，不需要另建一份 PPT，也不用改动 P1–P26。**

### user — `<UUID>` — 2026-10-18T05:51:52.102000+00:00

有个问题就是我的正文里好像没有一个关于**多指标综合决策的正面示例，没办法体现我是如何运用这个结论的**

### assistant — `<UUID>` — 2026-10-18T05:51:56.164454+00:00

你发现的是一个很重要的叙事缺口，而且我认为**值得在定稿前解决**。

你现在的正文已经讲清楚了两件事：

1. **发现问题：** 已知阴性对照也可能获得较高的结构置信度分数，因此单一指标不足以独立判断候选物是否真实结合。
2. **提出原则：** 应结合基准校准与多方面结构证据，而不是单纯追求高分。

但还缺少第三步：

3. **展示应用：** 当单一指标具有误导性时，你具体如何综合其他证据，分析候选物、比较候选物，或决定哪些候选值得优先验证？

如果没有第三步，读者容易觉得你的工作停留在“发现问题、提出建议”，而没有展示评价框架如何实际用于分析。

不过，有一个重要的学术边界：**多指标综合决策的正面示例，不一定要证明某个候选物最终是真实 binder；它可以展示多个计算证据如何共同支持一个更审慎的筛选决定。** 前提是这些证据确实存在于你的数据中。

## 我建议：优先改造 P21，而不是增加正文页

P21 原本就是 `MULTI-METRIC DECISION`，最适合承接这个任务。让它从“介绍一个多指标决策框架”升级为“展示这个框架如何实际工作”。

<box border radius="xl" padding={3} gap={3}>
  <title size="lg">P21 建议改造方向</title>
  <text color="secondary" size="sm">从方法示意转向案例分析</text>
  <box background="surface-secondary" radius="lg" padding={3} gap={1}>
    **01 · 单指标给出什么信号？**

    展示某个候选与已知对照的实际 ipTM，说明为什么不能只凭这个分数做决定。
  </box>
  <box align="center">
    <icon name="arrow-down" size="lg" color="secondary" />
  </box>
  <box background="surface-secondary" radius="lg" padding={3} gap={1}>
    **02 · 其他证据补充了什么？**

    对同一候选检查实际可用的其他指标，例如链间 PAE、界面接触和界面几何，解释各自支持或削弱了什么判断。
  </box>
  <box align="center">
    <icon name="arrow-down" size="lg" color="secondary" />
  </box>
  <box background="surface" border radius="lg" padding={3} gap={1}>
    **03 · 最终如何决定？**

    给出一个明确但审慎的结论：优先进入后续验证、暂缓排序，或证据不足以判断。解释理由，而不是只给出综合分数。
  </box>
</box>

## 关键问题：你现在有没有足够的数据支撑这个例子？

根据目前已经确认的材料：

- **EGFR 7D12 与 scramble 对照：** 能很好地说明 ipTM 的局限，但现有记录中的数值主要是 ipTM，不能单独证明多指标综合决策有效。
- **PD-L1 冷启动测试：** 阴性对照的 ipTM 均值高于候选池中位数，同样可以说明单指标存在问题，但还不是多指标综合决策的正面示例。
- **1BRS Barnase–Barstar 基准：** 有独立的方法学评价结果，但不能直接作为你从头设计 binder 的综合决策成功案例。

因此，**现在还不能直接挑一个候选，编出一套“多指标综合后成功筛选”的故事。**

我建议先检查已有候选的结构文件和评价表，寻找一个同时具备至少两到三类互补证据的真实案例。如果现有结果不够，可以从已经生成的结构中补算界面接触、界面面积等指标，但必须使用一致、可说明的计算口径，并如实标注这是补充分析。

理想情况下，P21 展示一个候选与一个对照的具体比较，附录再给出完整指标表。这样既能体现你实际运用了评价结论，也不会把计算筛选夸大成实验验证。

**我想先确认一个关键事实：你现在保存的 EGFR 或 TNF-α 候选结果中，除了 ipTM，是否已经有 PAE、界面接触数、界面面积或其他界面评价数据？** 如果有，我们就应该从真实数据中选案例；如果没有，就先确定哪些指标可以从现有结构可靠地补算。

### user — `<UUID>` — 2026-10-18T05:53:36.482000+00:00

能不能再开一张PPT加到**6 · MULTI-METRIC DECISION后面专门将这个案例**

### assistant — `<UUID>` — 2026-10-18T05:53:48.721305+00:00

**完全可以，而且我认为这是比硬塞进原 P21 更好的方案。** 这样既保留了原来“为什么需要多指标决策”的逻辑，又能单独展示你如何把这个结论应用到实际候选评价中。

不过，新页必须有真实数据支撑，不能只画一个理想化的决策流程。

## 建议新增一页：真实案例分析

<box border radius="xl" padding={3} gap={3}>
  <row align="center" justify="between">
    <box gap={1}>
      <text color="secondary" size="xs">建议新增页 · 紧接原决策框架页</text>
      <title size="lg">从单一分数到综合判断</title>
      <text color="secondary" size="sm">FROM SINGLE-METRIC SCORES TO MULTI-METRIC EVIDENCE</text>
    </box>
    <icon name="chart-no-axes-combined" size="2xl" color="secondary" />
  </row>
  <divider />
  <box gap={1}>
    <text color="secondary" size="xs">01 · CASE</text>
    **案例与评价问题**

    选取一个真实候选和合适的对照，说明单一指标为何不足以支持筛选决定。
  </box>
  <box gap={1}>
    <text color="secondary" size="xs">02 · EVIDENCE</text>
    **多指标证据对照**

    用简洁的对照表或图表呈现实际可用的结构置信度、界面接触、界面几何等指标；只展示已经计算并核实的数据。
  </box>
  <box gap={1}>
    <text color="secondary" size="xs">03 · DECISION</text>
    **综合评价与筛选结论**

    说明不同证据是否一致、存在哪些不确定性，以及候选应当优先验证、暂缓排序，还是证据不足。
  </box>
</box>

## 插入后，正文顺序怎么安排？

我建议采用下面的结构：

| 顺序 | 内容 |
|---|---|
| 原第 6 节 | `MULTI-METRIC DECISION`：介绍为什么需要多指标决策，以及基本框架 |
| **新增案例页** | 展示真实数据如何支持候选比较与决策 |
| 后续 Discussion | 讨论方法的意义与适用边界 |
| Limitations → Future Work → Conclusion → Acknowledgements | 保持原有结尾逻辑 |

如果你当前的第 6 节对应 P21，那么新增页将是 P22，原 P22–P26 顺延一页，主报告就变成 **27 张**。如果后续章节标题中包含页码或章节编号，也要检查是否需要同步调整；章节编号本身不一定需要改变。

## 但我建议先确定案例，再正式制作

你现有的 EGFR 7D12 与 scramble 对照，已经能说明单一 ipTM 可能产生误导；但仅凭这些 ipTM 数值，还不能证明多指标综合决策确实带来了更好的区分能力。

因此，新页最重要的不是设计，而是找到一组能形成完整证据链的真实数据：

- 单一指标给出什么信号；
- 其他已计算指标提供了什么补充证据；
- 综合这些证据后，筛选决定有什么依据；
- 这个决定仍有哪些不确定性。

**如果数据支持，我们就做成真正的案例分析页，而不是泛泛的流程图。** 这样会让你的项目贡献更具体：你不仅发现了指标判别的局限，还展示了如何据此构建和应用评价框架。

### user — `<UUID>` — 2026-10-18T05:54:33.016000+00:00

那先围绕**多指标综合决策设计一个标题吧**

### assistant — `<UUID>` — 2026-10-18T05:54:36.612522+00:00

我建议新增案例页的标题要体现：**从发现单一指标的局限，进一步走向实际的候选评价与决策。**

下面是几个候选标题：

<box gap={3}>
  <box border radius="lg" padding={3} gap={1}>
    <badge color="success">首选</badge>
    <title size="lg">从单一分数到综合判断</title>
    <text color="secondary" size="sm">FROM SINGLE-METRIC SCORES TO MULTI-METRIC DECISION-MAKING</text>
    承接前一页的多指标决策框架，同时突出本页将展示具体案例，中文自然，英文也适合学术报告。
  </box>
  <box border radius="lg" padding={3} gap={1}>
    <title size="md">多指标证据如何指导候选筛选</title>
    <text color="secondary" size="sm">HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION</text>
    更强调实际应用，适合本页最终能展示真实指标数据和明确筛选结论的情况。
  </box>
  <box border radius="lg" padding={3} gap={1}>
    <title size="md">从指标校准到候选决策</title>
    <text color="secondary" size="sm">FROM METRIC CALIBRATION TO CANDIDATE DECISIONS</text>
    更突出整个项目的研究逻辑，适合把基准校准与候选评价串联起来。
  </box>
  <box border radius="lg" padding={3} gap={1}>
    <title size="md">综合结构证据：一个候选评价案例</title>
    <text color="secondary" size="sm">INTEGRATING STRUCTURAL EVIDENCE: A CASE STUDY</text>
    最明确地告诉读者这是一页案例分析，而非继续介绍理论框架。
  </box>
</box>

**我个人最推荐第一个：**

**从单一分数到综合判断**

它与前一页 `6 · MULTI-METRIC DECISION` 形成自然递进：上一页解释为什么需要综合决策，这一页展示如何应用。

等具体案例确定后，如果确实有真实数据支撑，我们可以再把标题改得更有针对性；如果最终只是提出评价流程，而没有完成实际的多指标案例分析，就不应使用暗示已验证筛选效果的标题。

### user — `<UUID>` — 2026-10-18T05:55:52.040000+00:00

### 多指标证据如何指导候选筛选

HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION

更强调实际应用，适合本页最终能展示真实指标数据和明确筛选结论的情况。

我选这个，你做一个补充大纲

### assistant — `<UUID>` — 2026-10-18T05:55:55.926186+00:00

我建议把这张新增页设计成一张**真实案例驱动的分析页**，放在 `6 · MULTI-METRIC DECISION` 后面。原页负责介绍决策框架，新页负责展示如何用证据指导候选筛选。

<WritingBlock id="58317" variant="document"># 补充页大纲：多指标证据如何指导候选筛选

**中文标题：** 多指标证据如何指导候选筛选

**英文标题：** HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION

**页面定位：** 主报告新增案例分析页，紧接 `6 · MULTI-METRIC DECISION`。

## 一、核心目的

展示如何将基准校准中发现的问题，转化为实际的候选评价与筛选逻辑。

本页需要回答三个问题：

1. 单一结构置信度分数可能产生什么误导？
2. 其他结构证据能够补充什么信息？
3. 综合证据后，如何决定候选是否值得优先进入后续验证？

核心观点：

**候选筛选不应只看某一个分数，而应结合多个互补的结构证据，并明确每项证据的解释边界。**

## 二、页面结构

### 01 · CASE SETUP｜案例与评价问题

简要交代所选靶点、候选物与对照的来源。

需要包含：
- 靶点及候选物标识。
- 对照的类型与选择依据。
- 本次案例希望解决的具体筛选问题。
- 候选与对照是否在可比较的预测条件下生成或评估。

优先从已有 EGFR 或 TNF-α 项目材料中选择有充分数据支持的案例。若只有单一指标数据，应如实说明，不得直接将其称为已完成的多指标案例。

### 02 · EVIDENCE COMPARISON｜多指标证据对照

以紧凑表格或图表呈现同一候选与对照的实际结果。

优先考虑以下证据类别，但只纳入已经计算并核实的指标：

- **结构置信度：** ipTM，以及实际使用的其他置信度指标。
- **相对位置不确定性：** 具有明确统计口径的 PAE 指标。
- **界面接触：** 按统一定义计算的接触数或接触分布。
- **界面几何或面积：** 实际计算的界面几何特征、界面 SASA 等。

每项指标应说明：
- 候选与对照的实际数值或可核验的比较结果。
- 指标反映的结构特征。
- 该指标对当前筛选判断提供了什么信息。
- 该指标无法单独回答什么问题。

不要把不同量纲的指标直接相加，也不要未经校准就构造综合分数或通用阈值。

### 03 · DECISION｜综合评价与筛选结论

根据实际证据，给出明确但审慎的决策。

可以使用以下决策类别：
- **优先进入后续验证：** 多项互补证据共同支持进一步验证，但尚未证明真实结合。
- **暂缓排序：** 证据存在冲突，或结果对模型、参数、预测条件较敏感。
- **证据不足：** 现有结果无法支持可靠的候选优先级判断。

必须明确指出：
- 哪些证据支持当前判断。
- 哪些证据存在局限或冲突。
- 为什么当前结论只是计算筛选建议，而不是实验结论。

最终采用哪一种决策，必须由真实数据决定，不得预先指定某个候选为成功案例。

## 三、页面结论

建议使用：

**综合结构证据可以帮助确定优先验证对象，但不能替代实验对真实结合能力的确认。**

英文：

`Integrated structural evidence can guide candidate prioritization, but experimental validation remains essential.`

## 四、与相邻页面的衔接

- 前一页 `6 · MULTI-METRIC DECISION`：解释为什么需要多指标综合决策，以及总体评价逻辑。
- 本页：通过真实案例展示如何比较证据、处理冲突并形成筛选建议。
- 后续 `DISCUSSION`：讨论这一方法的意义、适用范围及局限性。

## 五、制作前的证据核验

1. 检查已有候选与对照的原始结果表。
2. 确认各指标是否真实计算、定义是否一致。
3. 确认候选与对照的预测条件是否可比。
4. 若缺少互补指标，判断能否从现有结构文件可靠补算。
5. 如果仍无法构成完整案例，应将本页定位为“候选评价流程示例”，而不是宣称多指标筛选效果已得到验证。

**制作原则：先选定有证据支持的案例，再决定图表与结论；不为迎合标题而创造结果。**</WritingBlock>

## 页面视觉上，我建议采用三段式布局

<box border radius="xl" padding={3} gap={3}>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    <text color="secondary" size="xs">左侧 · CASE</text>
    **候选与对照**

    <text size="sm">交代靶点、候选和对照，突出单一指标的判断问题。</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg" />
  </box>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    <text color="secondary" size="xs">中部 · EVIDENCE</text>
    **多指标比较**

    <text size="sm">用实际数值和简短解释呈现不同证据，避免堆砌指标名称。</text>
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg" />
  </box>
  <box background="surface" border radius="md" padding={3} gap={1}>
    <text color="secondary" size="xs">右侧或底部 · DECISION</text>
    **筛选建议与不确定性**

    <text size="sm">清晰写出决策、支持证据和未解决的问题。</text>
  </box>
</box>

**下一步应先核对数据，而不是直接制作 PPT。** 目前已经确认的 EGFR 7D12 与 scramble 数据可以作为案例起点，但只有 ipTM 数值还不足以构成完整的多指标综合决策示例。我们需要检查现有结构和评价结果，确定哪些互补指标已经存在，哪些可以从结构中补算。

### user — `<UUID>` — 2026-10-18T05:59:10.743000+00:00

剩下的几页附录提示词都给我吧

### assistant — `<UUID>` — 2026-10-18T05:59:29.455429+00:00

可以。我们把附录一次性规划完整，并与已经确定的 **26 张正文 + 新增的多指标案例页**衔接起来。

我建议附录遵循一个原则：**正文讲研究故事，附录提供可核验的数据、方法和技术细节。** 不重复正文结论，不把尚未完成的分析包装成结果，也不为了让附录看起来完整而添加没有实际依据的页面。

下面这些提示词都可以分别交给 PPT 生成工具使用。附录继续接在主报告 PPT 后面，但采用独立的 `APPENDIX A`、`APPENDIX B` 等标识，不将它们计入正文页数。

## 附录整体规划

| 附录 | 主题 | 主要作用 |
|---|---|---|
| A | 指标定义与数据字典 | 解释指标及计算口径 |
| B | 基准数据与对照结果 | 提供核心基准证据 |
| C | 阈值校准与判别分析 | 说明如何评价指标的区分能力 |
| D | 实验验证接口与验证计划 | 区分计算筛选与实验验证 |
| E | 可复现性与工程细节 | 记录模型、参数、运行流程 |
| F | 多靶点完整结果 | 汇总各靶点结果及证据完整度 |

这里有两个重要调整：

- **新增的多指标案例页属于正文**，放在 `6 · MULTI-METRIC DECISION` 后面；附录不再重复讲一遍同样的案例。
- 阈值校准、实验验证和多靶点结果都必须根据现有材料决定展示范围。如果没有足够证据，就缩减页面或明确标注未完成，不强行凑齐。

---

## Appendix B — 基准数据与对照结果

<text color="secondary" size="sm">建议 1–2 页 · 核心证据附录</text>

这一部分最值得优先制作。它要让导师能够追溯你关于“结构置信度分数需要基准校准”的判断，而不是只看到结论。

<WritingBlock id="73104" variant="document"># APPENDIX B · BENCHMARK DATA & CONTROL RESULTS

## 页面定位
为 AI-BinderDesign 正文中的基准校准结论提供可核验的原始结果摘要。附录页独立编号，不计入主报告页数。

## 视觉风格
- 16:9 白底，沿用正文的交大红、深灰和浅灰视觉体系。
- 中文为主，英文为辅。
- 以数据表为主，不使用装饰性三卡布局。
- 数值必须清晰可读；不为了展示全部数据而缩小字号。

## B1：EGFR 阳性与阴性对照

标题：
`APPENDIX B1 · EGFR CONTROL BENCHMARK`
中文副标题：`EGFR 对照基准结果`

导语：
`通过已知阳性与阴性对照，检查单一结构置信度指标能否区分不同生物学类别。`

展示已确认的 ipTM 数据：

| Target | Control | ipTM |
|---|---|---:|
| Human EGFR | 7D12 | 0.622 |
| Human EGFR | scramble_1 | 0.665 |
| Human EGFR | scramble_2 | 0.706 |
| Mouse EGFR | 7D12 | 0.417 |
| Mouse EGFR | scramble_1 | 0.812 |
| Mouse EGFR | scramble_2 | 0.846 |

展示前核对原始数据表与运行记录。若对照分类、目标序列或运行条件存在疑问，先标注待核实，不得自行补齐。

建议用分组点图或紧凑表格呈现人源与小鼠 EGFR 结果。不要使用误导性的连续色带暗示 ipTM 越高就越可能真实结合。

结果解读：
- 在这些已测试的对照中，阴性 scramble 对照获得了高于 7D12 的 ipTM。
- 这一观察说明，ipTM 在当前对照设置中不能单独承担真实结合的判定任务。
- 不得据此宣称 ipTM 在所有靶点上无效。
- 7D12 是已知 EGFR binder，但不同物种的结果必须分别呈现，不可混为同一个目标条件。

## B2：其他基准或控制结果（仅在有实际数据时加入）

可纳入：
- PD-L1 cold-run shuffled negatives；
- TNF-α 控制体系；
- 其他已完成且有可追溯结果的基准。

每个结果块必须明确标注靶点、对照类型、预测条件、样本数量及数据状态。PD-L1 的负对照均值与候选池中位数应标明各自统计对象，不可将其写成直接的分类准确率。

TNF-α 结果只有在结构、控制关系及数据解释均已核实后才加入。

## 页面底部结论

`这些结果支持对结构置信度指标进行基准校准，但不足以建立跨靶点通用阈值。`

英文：
`These results motivate benchmark calibration, not universal thresholds.`

## 数据诚信要求
- 不添加未经核实的数值、样本数或统计结果。
- 不把不同靶点或不同运行批次直接合并统计。
- 不把预测分数当作实验亲和力。
- 所有展示数据必须能追溯至项目原始表格或分析结果。
- 如单页过密，拆分为 B1、B2，不缩小字号强行塞入。</WritingBlock>

## Appendix C — 阈值校准与判别分析

<text color="secondary" size="sm">建议 1 页；如果分析尚未完成，使用状态说明版</text>

这一页不是再讲一次“阈值需要校准”，而是说明：你具体评估了什么、哪些分析已经完成、哪些结论仍然不能下。

<WritingBlock id="73105" variant="document"># APPENDIX C · THRESHOLD CALIBRATION & DISCRIMINATION ANALYSIS

## 页面定位
说明结构评价指标的判别能力如何被检验，以及当前阈值校准工作的完成程度。

## 标题
`APPENDIX C · THRESHOLD CALIBRATION`
中文：`阈值校准与判别分析`

导语：
`指标的判别能力需要通过具有明确生物学依据的对照进行评估；阈值选择还取决于数据覆盖范围与任务目标。`

## 内容结构

### 1. 校准问题
用简洁文字说明：
- 输入：已知阳性、阴性对照及其实际计算指标。
- 目标：检验某项指标在特定基准中区分两类对照的能力。
- 输出：可复核的判别分析结果，以及是否具备提出候选阈值的依据。

### 2. 已完成的分析
仅列出实际执行且有结果文件支持的内容，例如：
- 阳性与阴性对照的分数比较；
- 指标分布与重叠情况；
- 不同指标之间的判别表现；
- 已实际完成的阈值敏感性分析或统计评价。

每项注明数据来源、样本范围和分析状态。

### 3. 尚未完成或暂不支持的结论
如果 macro-AP calibration 尚未完成，应明确写：
`Macro-AP calibration: incomplete`

不得虚构最佳阈值、准确率、ROC-AUC、PR-AUC、macro-AP 或置信区间。

### 4. 1BRS 独立方法学基准（仅在需要时展示）
如果保留 Barnase–Barstar 1BRS docking benchmark，必须明确：
- 这是独立的对接方法学基准。
- 不能把其性能结果视为 EGFR、TNF-α 或 de novo binder 候选的预测性能。
- 不可据此宣称多指标流程已获得跨靶点验证。

若展示已核实的统计量，应同时给出指标定义、正例标准及分析对象，不得只展示最亮眼的数字。

## 推荐视觉形式
左侧：分析问题与数据输入。
中间：已完成 / 未完成的分析状态。
右侧或底部：当前可以支持的结论与适用边界。

不要使用看似已经拟合完成的阈值曲线或虚构的分类性能图。

## 底部结论
`当前结果用于评估指标的判别能力；通用阈值仍需更充分的基准数据支持。`

英文：
`Current results assess metric discrimination; universal thresholds remain unestablished.`</WritingBlock>

---

## Appendix D — 实验验证接口与验证计划

<text color="secondary" size="sm">建议 1 页 · 说明计算结果如何衔接实验</text>

这页的任务是划清边界：你的计算流程输出的是优先级建议，不是已证实的实验 binder。它也可以说明下一步实验需要验证哪些问题，但不能暗示团队已经完成实验。

<WritingBlock id="73106" variant="document"># APPENDIX D · EXPERIMENTAL VALIDATION INTERFACE

## 页面定位
说明计算筛选结果如何衔接后续实验验证，以及目前计算证据与实验结论之间的差距。

## 标题
`APPENDIX D · EXPERIMENTAL VALIDATION`
中文：`实验验证接口与后续验证计划`

导语：
`计算评价用于缩小候选范围；候选的真实结合能力与功能活性仍需通过实验验证。`

## 内容结构

### 1. 计算流程输出
展示实际流程产生的结果：
- 候选序列与候选标识；
- 对应的预测结构；
- 已计算的结构置信度与界面评价结果；
- 候选排序或优先级建议（如已有实际记录）。

不得把尚未完成的分析标为现有输出。

### 2. 后续实验需要回答的问题
根据项目目标，区分：
- **结合验证：** 候选是否与目标发生可检测的结合。
- **亲和力测量：** 如条件允许，测量并报告解离常数 Kd 等实验指标。
- **功能验证：** 对具有激动、抑制或其他功能目标的项目，另行设计功能实验。

结合实验与功能活性是不同问题，不能用结构预测替代功能测定。

### 3. 当前状态
准确区分：
- 已完成的计算分析；
- 已制定但未实施的实验计划；
- 已实际完成且可核验的实验结果。

如果项目目前没有系统实验亲和力数据，应直接注明：
`Experimental binding affinity validation: not yet established`

只有确实缺少实验结果时才使用该表述；如有已完成实验，应按实际情况更新。

### 4. 预期反馈闭环
用简单流程图表示：

`计算筛选 → 候选优先级 → 实验验证 → 实验结果分析 → 评价规则更新`

在图中明确标注这是**拟议的后续工作流程**，而不是已完成的研究闭环。

## 视觉形式
采用横向流程图，区分“当前计算工作”与“未来实验验证”。未来步骤使用浅灰或虚线轮廓，避免造成已完成的视觉暗示。

## 底部结论
`结构证据可以指导候选优先级，但真实结合能力与功能活性需要独立实验确认。`

英文：
`Structural evidence guides prioritization; binding and functional activity require experimental validation.`

## 禁止事项
- 不虚构实验结果、Kd 数值、实验成功率或候选验证状态。
- 不把计划中的实验写成已完成工作。
- 不将结合能力与激动 / 抑制功能混为一谈。
- 不暗示计算筛选已被证明提高实验成功率。</WritingBlock>

## Appendix E — 可复现性与工程细节

<text color="secondary" size="sm">建议 1–2 页 · 以实际运行记录为依据</text>

这部分用于展示项目不是停留在概念流程图，而是有实际工具链、参数与可追溯结果。它应当与 GitHub 仓库相互对应。

<WritingBlock id="73107" variant="document"># APPENDIX E · REPRODUCIBILITY & ENGINEERING DETAILS

## 页面定位
记录 AI-BinderDesign 中实际使用的计算工具、关键配置、数据流与运行条件，支持结果追溯和后续复现。

## 标题
`APPENDIX E · REPRODUCIBILITY & ENGINEERING DETAILS`
中文：`可复现性与工程细节`

导语：
`本页记录实际运行配置与结果追溯信息；未记录或未确认的设置不作推断。`

## E1：计算流程与工具链

按照实际执行顺序绘制简洁流程：

`Target preparation → Backbone generation → Sequence design → Structure prediction → Interface evaluation → Candidate ranking`

工具名称仅列出项目实际使用的版本与配置：
- RFdiffusion；
- ProteinMPNN；
- ColabFold；
- Boltz-2；
- 其他确实参与分析的工具。

每个工具只注明已核实的作用、输入输出及必要的版本信息。不要把计划尝试的工具写成已完成的流程环节。

## E2：关键运行条件

根据实际记录选择展示：
- 靶点结构与链标识；
- 使用的残基范围与 hotspot 定义；
- 设计序列长度或序列设计设置；
- MSA 配置；
- 模型版本；
- recycling steps、seeds 或其他关键运行参数；
- 结构文件、分析结果与日志的对应关系。

只有能够从脚本、配置文件或运行日志中确认的参数才能展示。

如果不同靶点使用了不同设置，应分开记录，不要将某个案例的参数泛化到整个项目。

## E3：结果追溯与状态管理

推荐表格字段：
- `target_id`
- `candidate_id`
- `model`
- `run_config`
- `seed`
- `structure_file`
- `metric_results`
- `analysis_status`

这些是建议的统一字段名。若现有仓库采用不同命名，应优先保留原字段并建立映射，而不是宣称现有文件已包含全部字段。

可采用状态标记：
- `Completed`
- `Pending review`
- `Not computed`

状态必须由真实文件和运行记录决定。

## 视觉形式
- 上半部：工具链流程图。
- 下半部：关键参数摘要表与结果追溯说明。
- 如果信息过多，拆分为 E1 工具链、E2 运行配置，不要缩小正文。

## 底部结论
`可复现性依赖于明确的输入、运行条件、计算口径与可追溯的结果记录。`

英文：
`Reproducibility depends on traceable inputs, configurations, metric definitions, and outputs.`

## 禁止事项
- 不展示未经核实的工具版本或参数。
- 不暴露无关的个人目录、账号信息、凭据或敏感服务器信息。
- 不将建议字段描述成已经存在的数据库结构。
- 不把不同运行批次的参数视为完全一致。
- 不用流程图代替实际运行记录。</WritingBlock>

---

## Appendix F — 多靶点完整结果

<text color="secondary" size="sm">建议 1–2 页 · 根据实际数据完整度决定是否保留</text>

这页可以展示你的流程是否在不同靶点上被实际运行过，以及每个靶点的结果、证据完整度和限制。但要特别注意：**在不同靶点上运行过流程，不等于已经证明评价阈值可以跨靶点迁移。**

<WritingBlock id="73108" variant="document"># APPENDIX F · MULTI-TARGET RESULTS

## 页面定位
汇总 AI-BinderDesign 涉及的不同靶点、已完成的计算任务、实际可用结果及证据完整度，为正文中的工作范围与局限性提供技术补充。

## 标题
`APPENDIX F · MULTI-TARGET RESULTS`
中文：`多靶点计算结果汇总`

导语：
`不同靶点的结果应结合各自的数据覆盖范围、运行条件与评价完整度分别解读。`

## 1. 多靶点总览

先从实际项目记录中核对目标清单。

项目计划涉及五个靶点，但不能默认五个靶点都已有完整结果。对每个靶点记录：
- 靶点名称与标识；
- 已完成的计算阶段；
- 是否具备候选结构；
- 是否具备完整评价数据；
- 是否具有可解释的阳性 / 阴性对照；
- 当前分析状态。

推荐表格：

| Target | Design status | Structure prediction | Evaluation status | Evidence coverage |
|---|---|---|---|---|

状态统一使用：
- `Completed`
- `Partial`
- `Pending`
- `Not evaluated`

每项状态都必须有实际项目记录支持。没有数据的单元格标为 `N/A` 或 `Not available`，不能自行补值。

## 2. 跨靶点运行结果

如果已有实际数据，可展示各靶点的：
- 运行完成情况；
- 候选数量与筛选结果；
- 已计算的评价指标；
- 实际运行时间（仅在日志可核实时）。

PD-L1 与 B7-1 / CD80 的冷启动结果可以作为补充案例，但必须标明：
- 这是跨靶点流程运行的补充证据；
- 不能将其直接解释为跨靶点通用阈值已经得到验证；
- PD-L1 与 B7-1 存在生物学关联，不应将二者视为完全独立的泛化验证。

TNF-α 的控制体系应与 de novo binder 设计候选区分开来。若该靶点只有控制结构预测而没有完整候选筛选结果，应如实注明。

## 3. 结果解释

在页面底部明确区分三个层面：
1. **流程可运行性：** 某靶点是否实际完成了相应计算阶段。
2. **候选评价完整度：** 是否具备足够的结构、对照与指标数据。
3. **跨靶点可迁移性：** 指标判别规则能否迁移到其他靶点，需要独立的基准证据。

前两项有记录，不代表第三项已经成立。

## 推荐视觉形式
- 上半部分：多靶点状态总览表。
- 下半部分：选取具有代表性的已完成案例，展示结果和证据覆盖情况。
- 避免将不同靶点的分数直接放在同一坐标轴上进行无条件排名。
- 不使用没有共同定义或可比条件的综合总分。

## 底部结论
`跨靶点运行结果可以展示流程的应用范围，但评价规则的可迁移性仍需独立验证。`

英文：
`Multi-target runs demonstrate workflow coverage, not universal transferability of evaluation rules.`

## 禁止事项
- 不虚构五个靶点的完整结果。
- 不把流程运行成功写成 binder 设计成功。
- 不把候选数量或通过数量直接解释为实验成功率。
- 不将 PD-L1、B7-1、EGFR、TNF-α 等不同任务的数据不加区分地合并。
- 不将未完成的目标或实验验证标为完成。</WritingBlock>

---

## 最后，建议的实际制作顺序

不要机械地按 A、B、C、D、E、F 的字母顺序制作，而是先做最能增强报告证据的页面。

<box gap={2}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="36px" align="center" justify="center">
      <title size="md">1</title>
    </box>
    <box flex="1" gap={1}>
      **Appendix B — 基准数据与对照结果**

      <text color="secondary" size="sm">优先级最高。先把已有真实数据整理清楚，支撑正文的核心结论。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="36px" align="center" justify="center">
      <title size="md">2</title>
    </box>
    <box flex="1" gap={1}>
      **Appendix A — 指标定义**

      <text color="secondary" size="sm">确认实际使用的指标与计算口径，避免把参考指标误写为已计算指标。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="36px" align="center" justify="center">
      <title size="md">3</title>
    </box>
    <box flex="1" gap={1}>
      **Appendix E — 可复现性与工程细节**

      <text color="secondary" size="sm">从已有脚本、参数和运行记录中整理，不需要为制作 PPT 重新编造流程。</text>
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="36px" align="center" justify="center">
      <title size="md">4</title>
    </box>
    <box flex="1" gap={1}>
      **Appendix C、D、F — 按证据完整度制作**

      <text color="secondary" size="sm">阈值校准、实验验证和多靶点结果分别核实；材料不足时可以缩减或省略。</text>
    </box>
  </row>
</box>

**还有一点需要明确：** 这六份提示词是附录的规划方案，不代表你必须制作六个附录。最终保留哪些页面，应取决于它们是否提供了正文没有、但导师可能需要核查的真实信息。

尤其是你新增的“多指标证据如何指导候选筛选”正文页，应先找到实际候选的互补指标数据，再确定案例结论；附录负责支撑这页，而不是代替这页。

### user — `<UUID>` — 2026-10-18T06:31:53.675000+00:00

有必要设置参考文献吗

### assistant — `<UUID>` — 2026-10-18T06:31:58.019439+00:00

**有必要，而且我建议你的 AI-BinderDesign 报告设置参考文献。** 但不需要做成很长的文献综述。对于一份希望用于联系上海交大 AI-for-Science / 蛋白质设计课题组的研究报告，参考文献能让导师区分哪些内容来自已有研究，哪些是你们实际完成的工作。

## 放在哪里最合适？

我建议不增加正文页，而是在现有 26 张正文之后、技术附录之前，增加一页：

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" size="xs">建议新增页面</text>
  <title size="lg">REFERENCES｜参考文献</title>
  <text color="secondary" size="sm">放在 P26 致谢之后，附录之前。它属于报告补充页面，不计入 26 张正文。</text>
  <divider />
  **建议引用范围**

  - 蛋白质骨架生成、序列设计和结构预测工具的原始论文。
  - 报告中使用的结构评价指标及其方法来源。
  - EGFR 7D12 等已知 binder 的生物学依据。
  - 1BRS Barnase–Barstar 基准的结构与 DockQ 评价方法（如果报告保留这部分结果）。
  - 其他在正文中直接引用或依赖的研究。
</box>

## 建议的参考文献组织方式

| 类别 | 应引用什么 |
|---|---|
| 设计工具 | RFdiffusion、ProteinMPNN 等实际使用工具的原始论文 |
| 结构预测 | 实际使用的 ColabFold、AlphaFold-Multimer 或 Boltz-2 方法论文 |
| 评价指标 | ipTM、PAE、pDockQ2、DockQ 等实际采用指标的方法来源 |
| 生物学证据 | 7D12 与 EGFR 的相关研究、结构数据库记录，以及其他对照的可靠来源 |
| 基准数据 | 1BRS 复合物结构、正负例定义和相关基准方法文献 |

注意：**只引用真正支撑报告内容的文献。** 如果某个指标只是考虑过、但没有实际使用，就不必为了凑齐列表而引用；如果引用了 PDB 结构，也应给出对应的结构数据库条目。

## 参考文献页应该怎样设计？

我建议采用单页双栏布局：

- 标题：`REFERENCES｜参考文献`
- 正文：编号引用，按正文首次出现顺序排列。
- 每条包含作者、论文标题、期刊或会议、年份、DOI 或稳定链接。
- 字号以清晰可读为准；如果文献超过一页容量，就拆成两页，不要挤成密密麻麻的小字。
- 正文相关论断用 `[1]`、`[2]` 等编号对应引用。

**不要只在最后列出文献，而正文完全不标引用。** 尤其是关于模型能力、指标定义、已知 binder 的结合关系以及方法学基准的陈述，应该能追溯到具体来源。

我的建议是：保留 26 张正文，在 P26 后增加 `REFERENCES`，然后再接技术附录。这样主报告叙事不变，但学术规范性会更完整。

### user — `<UUID>` — 2026-10-18T06:36:27.873000+00:00

但是我报告里并没有体现过参考的文献，小组阅读的文献也只是了解，并没有引用其内容

### assistant — `<UUID>` — 2026-10-18T06:36:32.489550+00:00

那我反而建议：**不要为了让报告看起来更学术，就硬加一页参考文献。** 你现在的情况，需要区分“阅读过哪些文献”和“报告实际引用了哪些文献”。

对于你的 AI-BinderDesign 项目，如果小组阅读的论文只是帮助大家了解蛋白质设计领域，并没有直接支撑报告中的论点、方法选择或数据解释，那么不应该把这些论文列成仿佛已经引用过的参考文献。

## 你现在有三个选择

| 方案 | 适用情况 | 我的建议 |
|---|---|---|
| 不加参考文献页 | 报告主要是项目过程、实际结果和方法总结，且没有引用外部资料 | 可以，但要确保涉及外部方法和事实时交代来源 |
| 增加“相关工作与工具来源” | 使用了 RFdiffusion、ProteinMPNN、ColabFold、Boltz-2 等工具，但没有专门讨论相关论文 | **最适合你目前的情况** |
| 增加正式参考文献页 | 正文已经引用论文、结构数据库、指标定义或生物学证据 | 等正文引用补齐后再加 |

## 对你的报告，我更推荐第二种

你的报告核心不是文献综述，而是：

- 建立从头蛋白结合剂设计与结构评价流程；
- 通过 EGFR 等案例发现单一结构评分的局限；
- 探索用已知阳性和阴性对照校准评分的解释方式。

所以，文献不是报告的主角。你真正需要交代的是**用了什么方法、这些方法来自哪里，以及哪些结论是你们自己通过项目数据观察到的**。

可以在附录中增加一页：

**相关工作与工具来源｜RELATED WORK & TOOL SOURCES**

简要列出实际使用的核心工具及其原始论文或官方文档，例如 RFdiffusion、ProteinMPNN、ColabFold 和 Boltz-2。前提是这些工具确实用于你报告所描述的工作。若正文中的指标定义、蛋白质结构或生物学结论依赖外部资料，也应在对应位置标注来源。

这样做的目的不是声称小组对这些论文进行了系统研究，而是让读者能够追溯你们使用的方法。

另外要注意：**不能只在附录罗列工具论文，就把正文中所有外部事实都视为有了出处。** 如果你提到了 7D12 与 EGFR 的结合关系、特定 PDB 结构的用途，或者某个评价指标的定义，仍然应当为这些具体事实提供对应来源。

## 最重要的一点

你的报告应当清楚区分三件事：

1. **文献提供的背景与方法**：已有工具、评价指标和生物学知识。
2. **团队实际完成的工作**：运行流程、生成结构、整理对照数据和开展分析。
3. **你们从项目中得到的观察**：例如，某些已知阴性对照的 ipTM 高于已知阳性对照。

第三类才是报告最值得突出的内容，不应该让参考文献页喧宾夺主。

**我的建议是：保留简洁的“相关工作与工具来源”附录，不必专门做一页传统的文献综述；同时，只对报告中实际依赖的外部信息补充引用。** 这样既符合你们真实的工作情况，也能满足正式科研项目报告对可追溯性的要求。

### user — `<UUID>` — 2026-10-18T06:37:45.649000+00:00

AI-BinderDesign · 附录 A–F 合并文字稿（v1）
覆盖范围：Appendix A（P27–28）+ Appendix B（P29–30）+ C（P31）+ D（P32）+ E（P33）+ F（P34），共 8 页。
页面位置：全部接在主 deck P26 致谢之后，眉行用附录编号（APPENDIX A1/A2/B1/B2/C/D/E/F），不沿用正文页码体系，不计入正文 26 页。
A 节详细版见 13.0-AppendixA-v1-文字版.md（本合并稿收录其结论与参数）。
版式脚本：_gen_appendix_a_v1.py（A1/A2）、_gen_appendix_bf_v1.py（B–F）；校验 _check_appendix_a_v1.py、_check_appendix_bf_v1.py。
附录总原则：正文讲研究故事，附录提供可核验的数据、口径与技术细节——不重复正文结论，不把未完成分析包装成结果，不为凑页数添加无依据页面。
Appendix A · 指标定义与数据字典（P27–28）
数据层
A1 指标定义表（8 项，标「使用 / 参考」两级）：
标记
指标
含义与用途（页内原文）
解释边界（页内原文）
使用
ipTM
反映预测复合物中界面相对排列的可信程度
不能单独证明真实结合或实验亲和力
使用
ipSAE_8A
8 Å 口径下的 ipSAE 界面评分，用于链间界面可信度评价
8 Å 口径与残基范围须与项目脚本一致（待确认）
使用
PAE
表示模型预测中残基相对位置的不确定性
须注明所用残基范围、链间区域与聚合方式（待确认）
使用
contacts
按指定距离规则统计的界面残基或原子接触数
须注明距离阈值、原子/残基口径与去重规则（待确认）
使用
pDockQ2
评估预测蛋白复合物界面的可信程度
依赖其定义与输入结构；不是实验亲和力测量
参考
pLDDT
反映局部结构预测可信度
局部可信不等于界面正确或真实结合
参考
Interface SASA
描述复合物形成界面时溶剂可及表面积的变化
须明确总界面还是单侧等其他口径
参考
Interface geometry
描述界面形状、接触分布或几何互补性（指标类别）
需明确具体算法或计算定义，不能仅凭名称推断数值
A2 数据字段字典（10 项建议框架）：target_id / candidate_id / control_type / model / run_config / seed / metric_name / metric_value / structure_file / analysis_status——字段名以现有数据仓库实际字段为准，不得虚构已存在的数据列。
解释原则（3 条）：分数不是实验结论 ／ 定义决定解释 ／ 基准决定判别意义。
白话层
A1 的判定依据是项目现有报告与数据：「使用」= 据项目现有报告与数据确认实际使用（6 组基准宽表核实），「参考」= 候选字典收录、未确认纳入当前流程。其中 ipSAE_8A 不在用户候选清单中，系据项目数据补入并标「使用」（阈值 0.70 在正文 6· 使用）。三个口径（PAE 聚合方式 / contacts 阈值与去重 / ipSAE_8A 的 8 Å 口径）页内标注「待确认」，须与项目脚本核对后确认，不得臆写。Interface geometry 明确标注为指标类别而非单一标准化数值。
Appendix B · 基准数据与对照结果（P29–30）
数据层（B1 · EGFR 对照基准，6 行）
Target
Control
ipTM
对照类型
Human EGFR
7D12
0.622
阳性 · 已知 EGFR 结合纳米抗体
Human EGFR
scramble_1
0.665
阴性 · 乱序序列
Human EGFR
scramble_2
0.706
阴性 · 乱序序列
Mouse EGFR
7D12
0.417
阳性 · 跨物种同源纳米抗体
Mouse EGFR
scramble_1
0.812
阴性 · 乱序序列
Mouse EGFR
scramble_2
0.846
阴性 · 乱序序列
观察（页内原文）：阴性 scramble 对照获得了高于 7D12 的 ipTM（人源 0.665/0.706 > 0.622；鼠源 0.812/0.846 > 0.417）。这一观察说明 ipTM 在当前对照设置中不能单独承担真实结合的判定任务；不据此宣称 ipTM 在所有靶点上无效。
数据层（B2 · 其他对照与迁移测试）：
项目
ipTM
统计对象
数据状态
PD-L1 迁移测试 · 乱序阴性对照（组 1）
均值 0.867
阴性对照组
已核实（正文脚注口径）
PD-L1 迁移测试 · 乱序阴性对照（组 2）
均值 0.851
阴性对照组
已核实（正文脚注口径）
PD-L1 迁移测试 · 候选池
中位数 0.744
EGFR 流程迁移的候选池
已核实（正文脚注口径）
TNF-α 状态（页内原文）：控制结构预测（双链受控重跑与结构对照分析）已完成；完整候选筛选结果待核实——本页暂不展示 TNF-α 数值，待结构与控制关系核实后按实际数据加入。
白话层
B1 是整份报告最核心的可核验证据：一个已知能结合 EGFR 的纳米抗体（7D12），结构预测分数反而低于乱序阴性对照——这就是正文「高分不等于真实结合」的实证来源。鼠源 7D12 只有 0.417，还说明了跨物种目标条件必须分别呈现。B2 把同样的逻辑延伸到 PD-L1：乱序阴性的均值比候选池中位数还高——注意两者统计对象不同（阴性组 vs 候选池），不是分类准确率。
诚信边界
- 数据取自项目基准记录，使用前已核对对照分类与序列；不添加未经核实的数值、样本数或统计结果。
- 不同靶点、不同运行批次不合并统计；7D12 跨物种结果分列呈现。
- ipTM 是结构预测置信度，不是实验亲和力；不把预测分数写成实验测量。
Appendix C · 阈值校准与判别分析（P31）
数据层（三列结构）
校准问题：输入 = 已知阳性、阴性对照及其实际计算的指标值；目标 = 检验某项指标在特定基准中区分两类对照的能力；输出 = 可复核的判别分析结果，以及是否具备提出候选阈值的依据。
分析状态：
- 已完成：EGFR 对照分数比较（→B1）；PD-L1 迁移测试（→B2）；多指标分布与重叠观察（正文 6·）；1BRS 独立方法学基准。
- 未完成 / 未建立：Macro-AP calibration: incomplete；跨靶点通用阈值：未建立（not established）。
1BRS 独立方法学基准（已核实口径）：质心判据 AUC = 0.9813（94,167 个对接姿态；正例 DockQ ≥ 0.23 共 78 个）——只说明该判据在此对接基准上的区分能力。
当前可支持的结论与边界：不能视为 EGFR、TNF-α 或 de novo 候选的预测性能；不可据此宣称多指标流程已获跨靶点验证。
白话层
C 页回答的是"你到底做了哪些校准分析"——不是再讲一遍"阈值需要校准"的道理。左列定义问题，中列诚实列出已完成与未完成（Macro-AP 没做完就写 incomplete），右列给 1BRS 的完整口径并划清边界：那是独立对接基准的判据区分能力，不是 binder 候选的预测性能。
诚信边界
不虚构最佳阈值、准确率、ROC-AUC、PR-AUC、macro-AP 或置信区间；展示已核实统计量时同时给出指标定义、正例标准与分析对象，不只展示最亮眼的数字。
Appendix D · 实验验证接口与验证计划（P32）
数据层
计算流程的实际输出（4 项）：候选序列与候选标识；对应的预测结构（结构文件可追溯）；已计算的结构置信度与界面评价结果；候选排序 / 优先级建议（如已有实际记录）。
后续实验需要回答的问题（3 类）：结合验证（候选是否与目标发生可检测的结合）；亲和力测量（条件允许时测定 Kd 等实验指标）；功能验证（激动 / 抑制等功能目标另行设计实验）——结合与功能是不同问题，结构预测不能替代功能测定。
当前状态：已完成 = 计算筛选与评价分析（正文 2–6）；已制定未实施 = 实验方案与验证计划；未建立 = Experimental binding affinity validation: not yet established。
拟议的后续工作流程（虚线为未来步骤，非已完成闭环）：计算筛选 → 候选优先级 → 实验验证 → 实验结果分析 → 评价规则更新。
白话层
D 页的任务是划清边界：计算流程输出的是优先级建议，不是已证实的实验 binder。页面上计算输出用实线框、实验问题用浅灰框——视觉上就区分了"已做的"和"要做的"。流程图明确标注是拟议工作流，不是已完成闭环。
诚信边界
不虚构实验结果、Kd 数值、实验成功率或候选验证状态；不把计划中的实验写成已完成工作；不将结合能力与激动 / 抑制功能混为一谈；不暗示计算筛选已被证明提高实验成功率。
Appendix E · 可复现性与工程细节（P33）
数据层
工具链（按实际执行顺序，6 步）：Target preparation → Backbone generation（RFdiffusion）→ Sequence design（ProteinMPNN）→ Structure prediction（ColabFold / Boltz-2）→ Interface evaluation（ipTM / ipSAE_8A / PAE / contacts / pDockQ2）→ Candidate ranking（evidence-based）。
关键运行条件与追溯（仅列已核实项）：
项目
内容
状态
EGFR DIII hotspot 定义
局部编号 14 / 16 / 47 / 48 / 100 / 156（对应 EGFR 全局编号 325 / 346 / 348 / 415 / 438）
已核实
结构预测工具
ColabFold 与 Boltz-2 双引擎（正文 2·）
已核实
模型版本 / MSA 配置 / seeds / recycling steps
—
待整理（以运行脚本与日志为准）
结果追溯字段
target_id / candidate_id / model / run_config / seed / structure_file / metric_results / analysis_status（建议框架，见 A2）
字段名以现有仓库为准
白话层
E 页证明项目不是停留在概念流程图：工具链每一步都有实际工具，hotspot 的两套编号口径（局部 vs 全局）是报告写作中实际踩过的坑。没有记录的参数（版本、MSA、seeds）一概写"待整理"，不编造——可复现性依赖于明确的输入、运行条件、计算口径与可追溯的结果记录，而不是看起来完整的参数表。
诚信边界
不展示未经核实的工具版本或参数；不包含账号、服务器或凭据信息；不将建议字段描述成已经存在的数据库结构；不把不同运行批次的参数视为完全一致；不用流程图代替实际运行记录。
Appendix F · 多靶点计算结果汇总（P34）
数据层（五靶点状态表）
Target
Design
Structure prediction
Evaluation
Evidence coverage
EGFR
Completed
Completed
Completed
最完整：含阳性 / 阴性对照基准与全流程案例
TNF-α
Partial
Completed
Partial
控制体系结构预测完整；候选筛选待核实
GLP1R
Partial
Partial
Pending
判据分析进行中，材料待整理
B7-1 (CD80)
Pending
Partial
Pending
冷启动与 MSA 对照（补充案例）
PD-L1
N/A（迁移测试）
Completed
Completed
跨靶点流程运行证据（→ B2）
结果解释的三个层面：流程可运行性（某靶点是否实际完成了相应计算阶段，有记录支撑）；候选评价完整度（是否具备足够的结构、对照与指标数据）；跨靶点可迁移性（判别规则能否迁移到其他靶点——需要独立基准证据，前两项有记录不代表第三项成立）。
白话层
F 页回答"流程到底在几个靶点上跑过、跑到什么程度"。状态表刻意保守：只有 EGFR 全链 Completed，其余都如实标 Partial / Pending。PD-L1 标 N/A 是因为它不是设计靶点，而是工作流迁移测试对象。底部三层解读是本页的灵魂：跑过 ≠ 评价完整 ≠ 规则可迁移——三层逐级需要更强的证据。
诚信边界
状态依据 2026-10-16 巡检记录与交接说明的间接记载，正式使用前需逐格核对源文件；无数据的单元格不自行补值。不虚构五个靶点的完整结果；不把流程运行成功写成 binder 设计成功；不把候选数量解释为实验成功率；不将 PD-L1、B7-1、EGFR、TNF-α 的数据不加区分地合并；PD-L1 与 B7-1（CD80）存在生物学关联，不视为完全独立的泛化验证；TNF-α 控制体系与 de novo 候选设计分开解读。
全附录通用诚信边界（汇总）
1. 附录全部 8 页不含任何基准数值型结果宣称（AUC、阈值、统计量只出现在已核实口径的上下文中，如 C 页 1BRS）。
2. 未实际计算的指标不标「使用」；未完成的分析明确标注 incomplete / not established / Pending。
3. 不把计划写成成果、不把观察写成验证、不把单基准结果外推为跨靶点结论。
4. 附录与正文分工：正文讲结论与叙事，附录讲口径与可核验性。
5. 敏感信息（子账号、算力余额、内部分工）一律不进附录。
校验状态：_check_appendix_a_v1.py（附录 A + 页数 34 断言）与 _check_appendix_bf_v1.py（16/16 内容检查 + 8 项禁词）全部通过；前 28 页与 1358 基线完全一致。
你看下附录有没有需要改动的地方

### assistant — `<UUID>` — 2026-10-18T06:37:49.826806+00:00

我看完这份合并稿后，整体判断是：**附录的结构可以保留，但 v1 还不适合直接定稿。** 问题不是页数太多，而是少数指标口径、数据状态和措辞存在尚未闭合的地方。尤其是 Appendix A、C、E、F，需要在正式放进报告前做一次实质性核对。

这套附录的方向是对的：正文负责讲研究故事，附录负责提供数据、方法口径和可追溯信息；同时明确区分计算结果、研究观察与实验验证。这个原则值得保留。

我建议按照三个等级修改：

- **必须修改**：可能导致事实错误、指标定义不准确或证据被过度解释。
- **建议修改**：改善逻辑、避免重复、提高科研报告的严谨性。
- **核实后保留**：目前内容合理，但仅凭这份文字稿还不能确认与实际脚本、日志完全一致。

## 一、必须修改的 6 个问题

### 1. Appendix A：不能仅凭报告确认指标实际被使用

你把 `ipTM`、`ipSAE_8A`、`PAE`、`contacts`、`pDockQ2` 标成“使用”，并说明依据是项目现有报告与数据、6 组基准宽表核实。

这里需要区分三个层次：

1. **工具能够输出该指标**；
2. **项目某些运行确实计算或记录了该指标**；
3. **该指标实际参与了候选排序或筛选决策**。

这三件事不等价。一个指标出现在结果文件中，不一定代表它被用于决策；出现在某次测试中，也不代表所有靶点都使用了相同口径。

建议把 A1 的“使用 / 参考”调整为更准确的分类：

| 状态 | 建议定义 |
|---|---|
| 已用于分析 | 有实际结果记录，并在分析中使用 |
| 已计算，决策用途待确认 | 有数值，但尚不能确认其参与候选筛选 |
| 参考指标 | 仅用于解释或计划纳入，未确认用于当前分析 |

其中，`ipSAE_8A` 尤其需要核对：不仅要确认是否实际计算，还要确认 `8 Å` 的定义、残基范围、聚合方式，以及正文中 `0.70` 阈值的来源。**不要因为正文出现了 0.70，就直接把它描述成经过验证的最佳阈值。**

PAE、contacts 和 pDockQ2 也应按实际情况逐项核实，而不是把整套指标列表视为全流程统一采用的指标集。

### 2. Appendix A：修正 EGFR hotspot 的编号表述

E 页写的是：

> 局部编号 14 / 16 / 47 / 48 / 100 / 156（对应 EGFR 全局编号 325 / 346 / 348 / 415 / 438）

这里有一个明确的数量不一致：**局部编号有 6 个，全局编号只有 5 个。**

根据你之前给出的 EGFR hotspot 信息，已知全局编号是：

`325、346、348、415、438`

如果局部编号确实是六个，必须回到实际脚本确认第六个位置及其对应关系；如果实际只有五个，则删除多出来的局部编号。不能直接猜测哪一个编号错了。

建议在确认前暂时写成：

> EGFR DIII hotspot：全局编号 325、346、348、415、438；局部编号映射待脚本核实。

核实后再恢复完整映射。这是目前整份附录里最明确、最应该优先修正的问题之一。

### 3. Appendix B：7D12 的阳性标签需要更精确

人源 EGFR 部分，把 7D12 标成“阳性 · 已知 EGFR 结合纳米抗体”，基本符合项目的对照逻辑。

但鼠源 EGFR 的表述：

> 阳性 · 跨物种同源纳米抗体

不够准确。“跨物种同源”容易让人误解为纳米抗体与目标蛋白之间存在某种同源关系，而实际想表达的是 7D12 对鼠源 EGFR 也有结合证据。

建议改成：

- Human EGFR — `7D12：已知结合阳性对照`
- Mouse EGFR — `7D12：有鼠源 EGFR 交叉反应证据的阳性对照`

如果要在页内进一步强调实验依据，可以用简短脚注注明相应的结合证据及来源。但要先核实文献或实验资料，不能仅凭结构预测结果定义阳性。

同时建议将“阴性 · 乱序序列”改成：

> 阴性对照 · scramble 序列

并在表下注明：这是本项目采用的阴性对照设计及其预期类别，不能仅因为序列被打乱，就认定它在实验中已被证明完全不结合。

### 4. Appendix B：PD-L1 两组均值不能在缺少定义时直接并列

B2 中列出了：

- 乱序阴性对照组 1：均值 0.867
- 乱序阴性对照组 2：均值 0.851
- 候选池：中位数 0.744

这组数据很有价值，但需要补齐三个信息：

- 两个阴性组分别是什么，为什么分组？
- 每组各有多少条序列或多少个有效预测结果？
- 两个阴性组和候选池是否使用相同的目标结构、模型、运行参数与统计口径？

如果样本数已经有记录，建议写出来；如果尚未核实，就不要编造。

另外，**均值和中位数不是相同的统计量**。它们可以用于描述性比较，但不应写成统计显著性结论，更不能直接说“阴性对照的分类性能优于候选池”。

建议页内表述改成：

> 在当前 PD-L1 迁移测试中，两个乱序阴性对照组的 ipTM 均值分别为 0.867 和 0.851，高于候选池的 ipTM 中位数 0.744。由于统计对象和统计量不同，该比较仅用于说明分数分布可能存在重叠，不代表分类准确率或统计显著性。

如果三个统计对象不是同一运行条件，则还应明确标注条件差异。

### 5. Appendix C：1BRS 的 AUC 必须与实际判别流程对应

C 页是我认为最需要仔细检查的技术页面。

你目前写的是：

> 质心判据 AUC = 0.9813（94,167 个对接姿态；正例 DockQ ≥ 0.23 共 78 个）

至少还需要明确以下信息：

- AUC 对应的具体判别分数是什么；
- 预测分数越高代表越可能为正例，还是越低越可能为正例；
- 负例如何定义，是否是剩余的全部可用姿态；
- AUC 是在哪个数据集合上计算的，是否存在训练与测试划分；
- 94,167 个姿态和 78 个正例是否来自同一统计口径。

如果这些都已由脚本和数据记录确认，建议补成一个小型方法注释。如果没有确认，就不要为了让这一页显得完整而推断。

另外，AUC 是你明确报告的结果，因此“全附录通用诚信边界”第 1 条：

> 附录全部 8 页不含任何基准数值型结果宣称……

与 C 页实际内容矛盾。应直接删除或改为：

> 附录仅展示可追溯且已核实口径的数值结果；每项结果均标明分析对象、指标定义与解释边界。

这样也避免把 AUC、阈值等数字一概视为不能出现。关键不是有没有数字，而是数字能否被核验、是否被正确解释。

### 6. Appendix F：五个靶点的状态不能只依据间接交接记录定稿

F 页自己已经说明，状态来自巡检记录与交接说明的间接记载，需要逐格核对。这是诚实的，但也意味着目前的状态表还不是最终证据。

建议在发布前核对每个状态对应的实际证据：

| 状态 | 最低限度的支持证据 |
|---|---|
| Design — Completed | 可追溯的设计输出或结果记录 |
| Structure prediction — Completed | 可追溯的预测结构及运行结果 |
| Evaluation — Completed | 指标结果文件与相应分析记录 |
| Partial | 明确指出已完成和未完成的子任务 |
| Pending | 尚无足够证据支持已完成 |

尤其是 TNF-α：你此前的项目材料明确区分了控制体系结构预测与 de novo 候选设计。因此，`Design: Partial` 不应该让读者误解为已经完成了一批可评估的候选设计。最好在 Evidence coverage 中直接写明：

> 控制体系预测已完成；de novo 候选筛选状态待核实。

GLP1R 的 `Partial / Partial / Pending` 也应确认它们分别指什么。状态表最重要的不是把格子填满，而是每个格子都有可追溯依据。

## 二、建议修改的 5 个问题

### 7. Appendix A：8 项指标放两页可以，但应减少“指标百科”的感觉

A 页同时包含指标定义、解释边界、数据字典和原则，信息密度偏高。

建议保留两页，但明确分工：

- **A1｜Metric Definitions**：指标名称、项目中的使用状态、简短定义、解释边界。
- **A2｜Data Dictionary & Interpretation**：实际数据字段、记录追溯方式、三个解释原则。

A2 的 10 个字段是建议框架，并不一定是当前数据仓库已有字段。最好在页眉或表下注明：

> 建议的数据追溯字段；实际字段名称以项目仓库为准。

还有一个细节：`Interface SASA` 的定义应更准确地说明是由复合物形成界面导致的溶剂可及表面积变化，常见做法是用分离组分的 SASA 总和减去复合物 SASA。若你们没有实际计算，就保留为参考指标，不必展开成计算公式。

### 8. Appendix D：把“已完成的计算流程输出”与“计划中的验证接口”分开

D 页的结构方向是正确的，但“计算流程的实际输出”中有一项：

> 候选排序 / 优先级建议（如已有实际记录）

“如已有实际记录”不适合直接出现在正式报告正文中。这是给制作人员的核对备注，不是面向读者的最终表述。

建议在制作时先核实：

- 如果已有明确排序文件：写“候选优先级结果”。
- 如果只有分数比较，没有正式排序：写“候选指标比较与筛选分析”。
- 如果尚未完成候选排序：不要列为已完成输出。

此外，实验计划可以保留，但建议把结合、亲和力与功能验证分成三条路径，不必暗示所有候选都必然进入所有实验环节。对 GLP1R 这类功能目标，尤其要强调：**结合并不等于激动，结构预测也不能单独证明受体激活。**

### 9. Appendix E：可复现性页要避免把工具名称等同于可复现

E 页的工具链很好，但目前更像“工程流程说明”，还不能单凭工具名称证明流程可复现。

建议把页面重点放在三类信息：

1. **输入**：目标结构、目标区域、hotspot 与链定义。
2. **计算条件**：工具、模型版本、MSA 配置、随机种子、recycling steps 等。
3. **输出追溯**：候选标识、结构文件、指标文件、运行状态。

已核实的项目参数可以列出；尚未整理的参数就写“待整理”。如果正文或附录中使用了不同运行批次的结果，建议不要把所有参数汇总成一套看似统一的配置。

另外，工具链中的 `Candidate ranking (evidence-based)` 如果目前只是人工综合比较，建议改成：

> Candidate prioritization based on available evidence

这样不会让人误以为你们已经实现了经过验证的自动排序算法。

### 10. Appendix F：`N/A` 与 `Pending` 应明确区分

PD-L1 的 `Design: N/A（迁移测试）` 是合理的，因为它是工作流迁移测试对象，而不是常规 de novo 设计靶点。

不过建议在表格下方增加一条状态说明：

- `Completed`：有结果记录支持该阶段完成。
- `Partial`：仅完成该阶段的部分工作。
- `Pending`：尚未完成或当前证据不足。
- `N/A`：该阶段不适用于该项目对象。

这可以避免读者把“没有进行设计”误认为“设计失败”，也避免把“尚未核实”误认为“尚未开展”。

还有一点：PD-L1 和 B7-1 的关系确实需要谨慎解释。它们都是免疫调节相关蛋白，但不能仅凭生物学关联就认定二者构成一个有效的独立泛化测试。你现在的表述基本正确，建议保留。

### 11. 附录整体：不要把内部制作说明原样放进最终 PPT

以下内容适合留在项目工作文档或制作脚本说明中，不应进入正式展示页面：

- “白话层”
- “诚信边界”这一内部审校标题
- “6 组基准宽表核实”
- “待脚本核实”“如已有实际记录”等制作备注
- 脚本文件名、校验脚本名、页数断言和“16/16 内容检查”等工程自检记录

这些信息对你们内部维护很有价值，但会让正式附录显得像审校清单。

可以将“诚信边界”转化成读者需要的注释，例如：

> 本页结果仅适用于所列对照与运行条件；结构预测指标不等同于实验结合证据。

而脚本和检查记录可以保留在 GitHub 仓库的 README、项目维护文档或版本记录中。

---

## 三、我建议的最终页结构

不需要因为这些问题重新设计整套附录。8 页的结构可以保留。

<box border radius="lg" padding={3} gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">A1</title>
    </box>
    <box flex="1" gap={1}>
      **指标定义与使用状态**

      <text color="secondary" size="sm">8 项指标、实际使用状态、定义和解释边界。先核实各指标是否实际计算，以及是否参与筛选。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">A2</title>
    </box>
    <box flex="1" gap={1}>
      **数据字段与追溯原则**

      <text color="secondary" size="sm">区分实际字段和建议字段；保留三个解释原则。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">B1</title>
    </box>
    <box flex="1" gap={1}>
      **EGFR 阳性与阴性对照**

      <text color="secondary" size="sm">核心数据页。保留人源、鼠源 7D12 与 scramble 的 ipTM，并明确对照依据和结论范围。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">B2</title>
    </box>
    <box flex="1" gap={1}>
      **PD-L1 迁移测试与其他对照**

      <text color="secondary" size="sm">补齐分组定义、样本数和统计口径；TNF-α 只报告已经核实的状态。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">C</title>
    </box>
    <box flex="1" gap={1}>
      **阈值校准与判别分析**

      <text color="secondary" size="sm">清楚区分已完成、未完成和独立方法学基准；补齐 1BRS 的判别定义。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">D</title>
    </box>
    <box flex="1" gap={1}>
      **实验验证接口与后续计划**

      <text color="secondary" size="sm">只把有记录的计算输出列为已完成；将实验计划明确标为未来工作。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">E</title>
    </box>
    <box flex="1" gap={1}>
      **可复现性与工程细节**

      <text color="secondary" size="sm">修正 hotspot 编号映射，列出已核实参数，并说明其余参数待整理。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} minWidth="66px" align="center">
      <title size="md">F</title>
    </box>
    <box flex="1" gap={1}>
      **多靶点计算状态汇总**

      <text color="secondary" size="sm">逐格核对源文件，定义状态标签，区分流程运行、候选评价和跨靶点迁移。</text>
    </box>
  </row>
</box>

## 四、关于参考文献：这份附录还缺少一个关键连接

结合你前面说的情况——小组阅读过相关论文，但没有在报告中直接使用其内容——我不建议为了附录完整而强行添加传统文献综述。

不过，这份附录已经包含了需要外部来源支撑的具体内容：

- RFdiffusion、ProteinMPNN、ColabFold、Boltz-2 等工具的来源；
- ipTM、PAE、pDockQ2、DockQ 等指标的定义；
- EGFR、7D12 与相关 PDB 结构的生物学依据；
- 1BRS 对接基准的定义与数据来源。

这些不是“阅读过哪些文献”的问题，而是**读者如何追溯报告中实际使用的方法与事实**的问题。

因此，我建议在正文或附录对应位置加入少量编号引用，例如 `[1]`、`[2]`，最后再列出与这些编号对应的文献和数据库记录。没有在报告中实际使用的阅读材料，不需要为了凑数放进去。

## 五、定稿前的优先级

{@body const checks = [
{level:"必须",task:"核对 EGFR hotspot 局部编号与全局编号的映射"},
{level:"必须",task:"逐项核实 A1 指标的实际计算状态和决策用途"},
{level:"必须",task:"确认 ipSAE_8A 的定义、8 Å 口径与 0.70 阈值来源"},
{level:"必须",task:"核实 PD-L1 两组阴性对照的分组、样本数和运行条件"},
{level:"必须",task:"补齐 1BRS AUC 的判别分数、正负例定义与计算口径"},
{level:"必须",task:"逐格核对 F 页五个靶点状态与实际源文件"},
{level:"建议",task:"修正通用诚信边界第 1 条与 C 页 AUC 结果的矛盾"},
{level:"建议",task:"移除最终展示页中的内部审校说明和制作脚本细节"},
{level:"建议",task:"为实际使用的工具、指标和生物学事实添加引用"}
]}
{@body const [done,setDone] = DIL.useState([])}
<box border radius="lg" padding={3} gap={3}>
  <row align="center" justify="between">
    <title size="md">附录定稿检查表</title>
    <text color="secondary" size="sm">{done.length}/{checks.length} 已核对</text>
  </row>
  <box background="surface-tertiary" radius="full" height="5px" clip>
    <box background="surface-inverted" radius="full" height="5px" width={`${done.length/checks.length*100}%`} />
  </box>
  {#each checks as item,i}
    <checkbox key={item.task} checked={done.includes(i)} onChange={v=>setDone(old=>v?[...old,i]:old.filter(n=>n!==i))} lineThrough={false}>
      <text color={item.level==="必须"?"default":"secondary"} size="sm">{item.level} · {item.task}</text>
    </checkbox>
  {/each}
</box>

**最终结论：保留 8 页框架，不建议大规模删页；先修正技术口径和证据状态，再做视觉精简。** 其中最优先的是 hotspot 编号映射、指标实际使用状态、PD-L1 统计口径、1BRS 判别定义，以及 F 页状态核验。完成这几项后，这份附录才真正具备“可核验、可追溯、不过度声称”的科研报告价值。

### user — `<UUID>` — 2026-10-18T07:07:06.592000+00:00

9 项检查表核对完成：**6 项落位、2 项部分核对、1 项部分完成**。核对记录已整理成 `文字稿/13.1-附录定稿核对记录.md`。逐项结果：

## 核对结果

**① hotspot 映射 ✅** — 找到了铁证：交接说明记录局部（内部）编号是 `A14(Asp) A16(Leu) A47(Ser) A48(Phe) A100(His) A156(Lys)`，规则「内部号 = UniProt − 333」。**​但这条规则与全局 5 个编号用任何偏移都对不上**——两套编号很可能是不同来源的表位定义（台账界面 vs 7D12 PDB 4KRL 接触残基）。E 页已补内部号与氨基酸注释，维持「映射待脚本核实」。

**② A1 指标状态 ✅** — CSV 实证 8 项指标全部实际计算过（ColabFold + Boltz 双引擎）。**​pLDDT 从「参考指标」升级为「已计算 · 待确认」**（它确实算了），页面注释补充「另实际计算了 pTM / interface_pLDDT / BSA / interface_residues 等字段」。

**③ ipSAE_8A ✅** — 0.70 的来源查清了：**是通用分档表的 Fail/Pass 边界，不是本项目标定**。且 6 组实测六组极差 0.776–0.857，小于一档宽度——本次实测无判别力。A1 边界列已如实改写。

**④ PD-L1 ⚠️** — 三个数值有脚注口径，但**两组乱序阴性的分组定义与样本数在现有文件中没找到**，保持「待核实」。

**⑤ 1BRS ⚠️** — AUC 与姿态数有记录，但**判别分数定义、正例方向、负例范围没找到**，C 页已标「待与脚本核对后补充方法注释」。

**⑥ F 页 ✅** — 意外收获：**TNF-α 的 4 体系控制汇总 CSV 就在 outputs 里**（TNF_TNFR1 / Human·Mouse Infliximab / GFP 阴性对照），页面更新为「数据文件已定位；数值展示待团队核实后加入」。GLP1R/B7-1 维持保守状态。

**⑦⑧ ✅** — 诚信边界改写与内部说明移除此前已完成。

**⑨ 引用 ⚠️** — 已加 7D12 = PDB 4KRL；Zenodo 15722219 已在 C 页引用。其余文献（EGFR UniProt、工具原论文等）需要你确认后补充。

## ⚠️ 一个必须向你报告的重大发现

核对过程中，我在 outputs 的**6 组基准实测数据字典（2026-10-12）**&#x200B;里发现了一份与正文叙事有实质出入的记录：

- **ipTM 方向完全反了**（给无界面的 mEGFR+Cetux 最高分、给有界面的 7D12 最低分），第三次被证伪，建议**整列弃用**；
- **contacts 才是判别力最强的主判据**（断层 5.2×），**PAE 是第二主判据**；
- **ipSAE_8A / pDockQ2 / pLDDT 在六组基准上无判别力**；
- contacts 阈值跨预测器不通用；建议在 Zenodo 15722219 上做 macro-AP 标定。

**这与正文 P21 的初始阈值体系（ipTM≥0.65、ipSAE_8A≥0.70 等）存在实质出入。**&#x200B; 这是研究结论层面的更新，涉及团队对叙事的决策，我没有擅动正文——只在附录如实对齐了（三分类、0.70 来源标注）。**建议团队讨论后决定正文是否需要相应修订**，比如正文 6· 的观察句是否要升级为「ipTM 已被三次证伪、contacts/PAE 才是当前实测主判据」。

deck 已重冻结：`存档/deck基线签名_2026-10-18-1459.json`（**deck_md5 `33aef529271d`，34 页**）。

Appendix B · 基准数据与对照结果（P29–30）\
数据层（B1 · EGFR 对照基准，6 行）\
Target\
Control\
ipTM\
对照类型\
Human EGFR\
7D12\
0.622\
已知结合阳性对照\
Human EGFR\
scramble_1\
0.665\
阴性对照 · scramble 序列\
Human EGFR\
scramble_2\
0.706\
阴性对照 · scramble 序列\
Mouse EGFR\
7D12\
0.417\
有鼠源 EGFR 交叉反应证据的阳性对照\
Mouse EGFR\
scramble_1\
0.812\
阴性对照 · scramble 序列\
Mouse EGFR\
scramble_2\
0.846\
阴性对照 · scramble 序列\
观察（页内原文）：阴性 scramble 对照获得了高于 7D12 的 ipTM（人源 0.665/0.706 > 0.622；鼠源 0.812/0.846 > 0.417）。这一观察说明 ipTM 在当前对照设置中不能单独承担真实结合的判定任务；不据此宣称 ipTM 在所有靶点上无效。\
scramble 说明（页内原文）：scramble 序列为本项目采用的阴性对照设计及其预期类别，不能仅因序列被打乱即认定其在实验中已被证明完全不结合。\
数据层（B2 · PD-L1 迁移测试）：两个乱序阴性对照组的 ipTM 均值分别为 0.867 和 0.851，高于候选池的 ipTM 中位数 0.744。由于统计对象和统计量不同，该比较仅用于说明分数分布可能存在重叠，不代表分类准确率或统计显著性。两组的分组定义与样本数待核实。\
TNF-α 状态（页内原文）：控制体系预测已完成；de novo 候选筛选状态待核实——本页暂不展示 TNF-α 数值。\
白话层\
B1 是整份报告最核心的可核验证据。7D12 的标签精确化很重要：人源是「已知结合阳性对照」，鼠源是「有交叉反应证据的阳性对照」——两者证据强度与来源不同，不能笼统写"跨物种同源"（那是说纳米抗体和 EGFR 同源，会误导）。scramble 措辞也改了：它是预期意义上的阴性对照，不是"已被实验证明完全不结合"。\
B2 的口径说明改写后把统计对象和统计量的差异讲清楚了：均值 vs 中位数、阴性组 vs 候选池——只能说明分布重叠，不能下统计显著性结论。\
诚信边界\
数据取自项目基准记录，使用前已核对对照分类与序列；不添加未经核实的数值、样本数或统计结果；不同靶点、不同运行批次不合并统计；7D12 跨物种结果分列呈现；ipTM 不是实验亲和力测量。\
Appendix C · 阈值校准与判别分析（P31）\
数据层（三列结构）\
校准问题：输入 = 已知阳性、阴性对照及其实际计算的指标值；目标 = 检验某项指标在特定基准中区分两类对照的能力；输出 = 可复核的判别分析结果，以及是否具备提出候选阈值的依据。\
分析状态：\
\- 已完成：EGFR 对照分数比较（→B1）；PD-L1 迁移测试（→B2）；多指标分布与重叠观察（正文 6·）；1BRS 独立方法学基准。\
\- 未完成 / 未建立：Macro-AP calibration: incomplete；跨靶点通用阈值：未建立（not established）。\
1BRS 独立方法学基准（已核实口径）：质心判据 AUC = 0.9813（94,167 个对接姿态；正例 DockQ ≥ 0.23 共 78 个）——只说明该判据在此对接基准上的区分能力。判别分数定义、正例方向与负例范围等口径，待与项目脚本核对后补充方法注释。\
当前可支持的结论与边界：不能视为 EGFR、TNF-α 或 de novo 候选的预测性能；不可据此宣称多指标流程已获跨靶点验证。\
白话层\
C 页回答"你到底做了哪些校准分析"。1BRS 的 AUC 是本附录唯一保留的统计量——保留的依据不是"有数字显得完整"，而是它是已核实、可追溯的结果。但它的完整方法注释（判别分数是什么、方向如何、负例怎么定义、有无划分）还没和脚本核对，所以页内明确写"待核对后补充"，而不是推断一个看起来完整的故事。\
诚信边界\
不虚构最佳阈值、准确率、ROC-AUC、PR-AUC、macro-AP 或置信区间；展示已核实统计量时同时给出指标定义、正例标准与分析对象。\
Appendix D · 实验验证接口与验证计划（P32）\
数据层\
计算流程的实际输出（4 项）：候选序列与候选标识；对应的预测结构（结构文件可追溯）；已计算的结构置信度与界面评价结果；候选指标比较与筛选分析。\
后续实验需要回答的问题（3 类）：结合验证（候选是否与目标发生可检测的结合）；亲和力测量（条件允许时测定 Kd 等实验指标）；功能验证（激动 / 抑制等功能目标另行设计实验）——结合与功能是不同问题，结构预测不能替代功能测定。\
当前状态：已完成 = 计算筛选与评价分析（正文 2–6）；已制定未实施 = 实验方案与验证计划；未建立 = Experimental binding affinity validation: not yet established。\
拟议的后续工作流程（虚线为未来步骤，非已完成闭环）：计算筛选 → 候选优先级 → 实验验证 → 实验结果分析 → 评价规则更新。\
白话层\
D 页划清边界：计算流程输出的是优先级建议，不是已证实的实验 binder。v2 把"候选排序 / 优先级建议（如已有实际记录）"改成"候选指标比较与筛选分析"——前者暗示已有正式排序文件，后者只声称做了指标比较，与实际一致。实验三类（结合 / 亲和力 / 功能）是三条独立路径，不暗示所有候选都进所有环节；GLP1R 这类功能目标尤其要记住：结合不等于激动。\
诚信边界\
不虚构实验结果、Kd 数值、实验成功率或候选验证状态；不把计划中的实验写成已完成工作；不将结合能力与激动 / 抑制功能混为一谈；不暗示计算筛选已被证明提高实验成功率。\
Appendix E · 可复现性与工程细节（P33）\
数据层\
工具链（按实际执行顺序，6 步）：Target preparation → Backbone generation（RFdiffusion）→ Sequence design（ProteinMPNN）→ Structure prediction（ColabFold / Boltz-2）→ Interface evaluation（ipTM / ipSAE_8A / PAE / contacts / pDockQ2）→ Candidate prioritization based on available evidence。\
关键运行条件与追溯（仅列已核实项）：\
项目\
内容\
状态\
EGFR DIII hotspot\
全局编号 325、346、348、415、438；局部（内部）编号 A14/A16/A47/A48/A100/A156——两套编号无法用单一偏移闭合，映射待脚本核实\
待核实\
结构预测工具\
ColabFold 与 Boltz-2 双引擎（正文 2·）\
已核实\
模型版本 / MSA 配置 / seeds / recycling steps\
—\
待整理（以运行脚本与日志为准）\
结果追溯字段\
target_id / candidate_id / model / run_config / seed / structure_file / metric_results / analysis_status（建议框架，见 A2）\
字段名以现有仓库为准\
白话层\
E 页 v2 修正了 hotspot 编号：原稿写 6 个局部编号对 5 个全局编号，数量对不上——不猜哪个错，先改成"全局 5 个 + 局部映射待脚本核实"，核实后再恢复完整映射。第 6 步从 "ranking (evidence-based)" 改为 "prioritization based on available evidence"：目前的人工综合比较不是经过验证的自动排序算法，措辞不能让人误以为是。\
页面重点放在三类信息：输入（目标结构、区域、hotspot 与链定义）、计算条件（工具、版本、MSA、seeds）、输出追溯（候选标识、结构文件、指标文件、状态）。\
诚信边界\
不展示未经核实的工具版本或参数；不包含账号、服务器或凭据信息；不将建议字段描述成已经存在的数据库结构；不把不同运行批次的参数视为完全一致；不用流程图代替实际运行记录。\
Appendix F · 多靶点计算结果汇总（P34）\
数据层（五靶点状态表）\
Target\
Design\
Structure prediction\
Evaluation\
Evidence coverage\
EGFR\
Completed\
Completed\
Completed\
最完整：含阳性 / 阴性对照基准与全流程案例\
TNF-α\
Partial\
Completed\
Partial\
控制体系预测已完成；de novo 候选筛选状态待核实\
GLP1R\
Partial\
Partial\
Pending\
判据分析进行中，材料待整理\
B7-1 (CD80)\
Pending\
Partial\
Pending\
冷启动与 MSA 对照（补充案例）\
PD-L1\
N/A（迁移测试）\
Completed\
Completed\
跨靶点流程运行证据（→ B2）\
状态标签定义（页内原文）：Completed = 有结果记录支持该阶段完成；Partial = 仅完成该阶段的部分工作；Pending = 尚未完成或当前证据不足；N/A = 该阶段不适用于该项目对象。依据巡检记录与交接说明（间接记载），正式使用前逐格核对。\
结果解释的三个层面：流程可运行性（某靶点是否实际完成了相应计算阶段，有记录支撑）；候选评价完整度（是否具备足够的结构、对照与指标数据）；跨靶点可迁移性（判别规则能否迁移到其他靶点——需要独立基准证据，前两项有记录不代表第三项成立）。\
白话层\
F 页回答"流程到底在几个靶点上跑过、跑到什么程度"。v2 给状态标签加了定义——特别是 N/A（不适用）和 Pending（未开展/证据不足）是两回事：PD-L1 的 Design N/A 不代表设计失败，B7-1 的 Pending 也不代表没跑过。TNF-α 的 Evidence coverage 精确化为"控制体系预测已完成；de novo 候选筛选状态待核实"，防止读者把 Partial 误读为"已经有一批可评估的候选"。\
诚信边界\
状态依据 2026-10-16 巡检记录与交接说明的间接记载，正式使用前需逐格核对源文件；无数据的单元格不自行补值。不虚构五个靶点的完整结果；不把流程运行成功写成 binder 设计成功；不把候选数量解释为实验成功率；不将 PD-L1、B7-1、EGFR、TNF-α 的数据不加区分地合并；PD-L1 与 B7-1（CD80）存在生物学关联，不视为完全独立的泛化验证；TNF-α 控制体系与 de novo 候选设计分开解读。\
全附录通用诚信边界（v2 修订）\
1\. 附录仅展示可追溯且已核实口径的数值结果；每项结果均标明分析对象、指标定义与解释边界——关键不是有没有数字，而是数字能否被核验、是否被正确解释。\
2\. 未实际计算的指标不标「已用于分析」；未完成的分析明确标注 incomplete / not established / Pending；状态标签各有定义，不混用。\
3\. 不把计划写成成果、不把观察写成验证、不把单基准结果外推为跨靶点结论。\
4\. 附录与正文分工：正文讲结论与叙事，附录讲口径与可核验性。\
5\. 敏感信息（子账号、算力余额、内部分工）一律不进附录；内部制作说明（白话层、诚信边界、脚本与校验记录）保留在文字稿与项目文档中，不进入正式 PPT 页面。\
校验状态：\_check_appendix_a_v1.py 与 \_check_appendix_bf_v1.py 全部通过；前 28 页与 1358 基线完全一致。\
定稿检查表核对记录\
9 项核对：6 完成 / 2 部分核对 / 1 部分完成——逐项依据与结论见 13.1-附录定稿核对记录.md（含「6 组基准实测数据字典与正文叙事的出入」重大发现汇报，正文是否相应修订由团队定夺）。

# AI-BinderDesign · 附录定稿检查表核对记录（2026-10-18）

**依据文件**：`2026-10-11-23-31-25/outputs/`（附件-Benchmark数据字典.md、EGFR-Benchmark对照组验证-组会汇报.md、FINAL_6GROUP_benchmark_statistics_corrected.csv、FINAL_binder_threshold_grading_corrected.csv、TNF_control_report_summary_final.csv、TNF_threshold_table_final.csv）、`2026-10-09-11-53-37/长江杯-交接包/01-交接说明/交接说明-给下一个Agent.md`。 **核对状态：6 项核对完成落位 / 2 项部分核对（已标待核实）/ 1 项部分完成（引用）。**

---

## ① EGFR hotspot 局部 ↔ 全局映射 —— ✅ 已核对，映射无法闭合

交接说明记录了局部（内部）编号与规则：**`A14(Asp) A16(Leu) A47(Ser) A48(Phe) A100(His) A156(Lys)`，内部号 = UniProt − 333**。

**核对结论**：该规则与全局 5 个（325 / 346 / 348 / 415 / 438）**无法用任何一致偏移闭合对应**（逐一试算均不吻合）——两套编号可能是**不同来源的表位定义**（如台账界面 vs 7D12 PDB 4KRL 实际接触残基），不能互相换算。

**落位**：E 页维持「全局编号 325、346、348、415、438；局部（内部）编号 A14/A16/A47/A48/A100/A156——两种编号在现有记录中无法用单一偏移闭合，映射待脚本核实」，并已补内部号与氨基酸注释。

## ② A1 指标实际计算状态 —— ✅ 已核对（pLDDT 升级）

CSV 实证（FINAL_6GROUP_benchmark_statistics_corrected.csv，ColabFold + Boltz 双引擎）：ipTM、ipSAE_8A、PAE、pLDDT、interface_pLDDT、BSA、contacts、pDockQ2 **均有实际计算记录**。

**落位**：**pLDDT 从「参考指标」升级为「已计算 · 待确认」**（它被实际计算了，只是未确认参与决策）；A1 注释补充「另实际计算了 pTM、interface_pLDDT、BSA、interface_residues 等字段（完整清单见基准数据表）」。

决策用途分级（v2 三分类维持）：ipTM 已用于分析（B1 对照比较）；ipSAE_8A / PAE / contacts / pDockQ2 / pLDDT = 已计算 · 待确认；SASA / geometry = 参考指标。

## ③ ipSAE_8A 定义、8 Å 口径与 0.70 阈值来源 —— ✅ 已核对

- **0.70 来源确认**：通用分档表（FINAL_binder_threshold_grading_corrected.csv）的 Fail/Pass 边界（`ipSAE_8A,<0.70,0.70-0.80,0.80-0.85,>0.85`），**非本项目标定**。

* **判别力确认**：6 组实测六组极差 0.776–0.857（< 一档宽度）→ **本次实测无判别力**；另据组会汇报，`ipSAE` 我方设计 0.62–0.64 vs 真 binder 0.2433——**只能看是否 >0，不能排名**。

**落位**：A1 边界列改为「0.70 为通用分档表 Fail/Pass 边界、非本项目标定；8 Å 口径与残基范围待脚本核实」。

## ④ PD-L1 两组阴性对照 —— ⚠️ 部分核对

0.867 / 0.851 / 0.744 三个数值有正文脚注口径可查（P21）；但**两组乱序阴性的分组定义、样本数与运行条件在现有 outputs 与交接包中未找到**。B2 页内保持用户版口径说明 + 「两组的分组定义与样本数待核实」。

## ⑤ 1BRS AUC 口径 —— ⚠️ 部分核对

AUC = 0.9813 / 94,167 姿态 / 正例 DockQ ≥ 0.23 共 78 个有正文与文字稿记录；但**判别分数定义、正例方向、负例范围、数据划分在现有文件中未找到**。C 页已加「待与项目脚本核对后补充方法注释」。

## ⑥ F 页五靶点状态 —— ✅ 大部分核对

- EGFR：全链证据（6 组基准 + 对照 + scramble 测试）✓

* TNF-α：**4 体系控制汇总 CSV 已定位**（TNF_TNFR1 / Human·Mouse TNF Infliximab / GFP 阴性）→ 页内更新为「数据文件已定位；数值展示待团队核实控制关系后加入」✓

- PD-L1：迁移测试 ✓

* GLP1R / B7-1：资料库文件间接记载 ✓（页面保持保守状态）

## ⑦ 通用诚信边界第 1 条 —— ✅ 已完成（v2 改写）

「附录仅展示可追溯且已核实口径的数值结果；每项结果均标明分析对象、指标定义与解释边界」。

## ⑧ 内部审校说明移除 —— ✅ 已完成

deck 8 页附录页面无白话层 / 诚信边界标题 / 脚本名 / 工程自检记录；全部保留在文字稿与项目文档。

## ⑨ 引用添加 —— ⚠️ 部分完成

- 已加：7D12 结构与结合证据 = **PDB 4KRL**（B1 说明区）。

* 可加（待确认后补充）：EGFR UniProt P00533；cetuximab / EGF 的结合证据文献；RFdiffusion / ProteinMPNN / ColabFold / Boltz-2 原始论文；Zenodo 15722219（C 页已引用其编号）。

---

# ⚠️ 核对过程中的重大发现（需团队定夺，未动正文）

**6 组基准实测数据字典（2026-10-12）记录的结论，与正文 P21 的初始阈值体系存在实质出入**：

|   |
| - |

发现

|   |
| - |

依据（数据字典原文）

|   |
| - |

**ipTM 方向完全反了（第三次被证伪），建议整列弃用**

|   |
| - |

给"无界面"的 mEGFR+Cetux 最高分 0.857，给"有界面"的 7D12 最低分 0.359/0.200

|   |
| - |

**contacts 是判别力最强主判据（断层 5.2×：30.2 vs 157.0）**

|   |
| - |

两预测器一致（ColabFold 侧 n=1 单次预测）

|   |
| - |

**PAE 为主判据（跨 3 档）**

|   |
| - |

2.874–18.026

|   |
| - |

**ipSAE_8A / pDockQ2 / pLDDT 在六组基准上无判别力**

|   |
| - |

极差均小于阈值表一档宽度

|   |
| - |

**contacts 阈值跨预测器不通用**

|   |
| - |

`<300=Fail` 按 ColabFold 尺度设，Boltz 六组全 Fail

|   |
| - |

**建议判据组合**：contacts ≥ 100 且 PAE < 10

|   |
| - |

替代现有 all_pass

|   |
| - |

**通用分档未经本体系标定 → 在 Zenodo 15722219 做 macro-AP**

|   |
| - |

CC-BY-4.0，3,532 条 / 13 靶点 / 391 binders

**这些属于研究结论层面的更新（如正文 6· 阈值表、观察句的改写），涉及团队对叙事的决策，本核对不动正文**——只如实反映在附录：A1 的三分类、ipSAE_8A 的 0.70 来源标注、C 页 macro-AP 状态，已与实测记录对齐。建议团队讨论后再决定正文是否需要相应修订。

### assistant — `<UUID>` — 2026-10-18T07:07:12.353533+00:00

这次核对最重要的，不是附录又修正了几处文字，而是发现了一个可能改变 **AI-BinderDesign 核心研究叙事**的问题：正文原先强调通过多指标和阈值校准改善候选筛选，但新的 6 组基准记录显示，部分指标可能无法区分当前对照，甚至出现与预期相反的排序。

我的建议是：**暂时不要把“ipTM 已被三次证伪、contacts/PAE 才是主判据”直接写进正文；先暂停沿用未经验证的阈值体系，核查原始数据和计算口径，再决定如何改写研究结论。**

这不是淡化负面结果。恰恰相反，是要把真正观察到的结果保留下来，同时避免从有限的基准数据跳到尚未得到充分支持的结论。

## 一、这次核对后，研究叙事需要重新审视

| 发现 | 当前可以支持的结论 | 目前还不能支持的结论 |
|---|---|---|
| EGFR 的 7D12 与 scramble 对照出现 ipTM 排序反转 | ipTM 在这组已知对照中不能单独可靠地区分阳性与阴性 | ipTM 在所有靶点、模型和任务中都无效 |
| 6 组基准中 contacts 差异明显 | contacts 值值得进一步作为候选判别特征进行验证 | contacts 已被证明是普适的最佳判据 |
| PAE 在这组数据中跨越多个数值区间 | PAE 可能提供与 contacts 互补的信息 | PAE 已被证明是第二好的通用判据 |
| ipSAE_8A 等指标变化范围有限 | 现有数据中，这些指标的分布可能不足以支持当前分档判别 | 这些指标对所有蛋白质复合物均无判别力 |
| contacts 阈值在两个预测器上的表现不同 | 不能未经校准直接共享同一阈值 | 已找到可跨模型、跨靶点通用的替代规则 |

尤其需要注意：你目前提供的核对记录显示，contacts 的关键对比来自 **ColabFold 侧 n=1 的单次预测**。这可以构成一个有价值的观察，但不足以独立证明该指标稳定、泛化能力强或优于其他指标。

研究故事真正应该从“我们找到了正确的评分指标”，转向更谨慎也更有研究价值的命题：

> **我们发现，现有结构评分与通用阈值未必能在当前基准中正确区分已知对照，因此需要检验指标的判别能力，并针对预测器与任务进行校准。**

这个表述不依赖某个指标最终胜出，也不会因为后续重新分析改变排序而使整份报告失去支撑。

## 二、正文 P21 应该怎么改

我建议不急着推翻整个 P21，而是把它从“阈值体系展示”调整为“基准校准发现与当前判据状态”。

### 1. 先处理旧阈值表

如果 P21 目前把 `ipTM ≥ 0.65`、`ipSAE_8A ≥ 0.70` 等条件组合成硬性 `all_pass` 规则，那么在确认这些条件的来源和实测表现前，**不应继续把它们展示为已经获得项目数据支持的筛选标准**。

具体来说：

- `ipTM ≥ 0.65`：应标明是原有参考规则还是项目自行设定的条件，不能默认它能区分真实结合与非结合。
- `ipSAE_8A ≥ 0.70`：应注明来自通用分档表，而不是本项目校准得到的阈值。
- `contacts ≥ 100 且 PAE < 10`：目前最多是从这组数据提出的候选判据，不能直接替换旧规则后称为新标准。

特别是最后一项，两个条件看起来合理，不等于它们已经在独立数据上得到验证。

### 2. 把 P21 的核心观察改为下面这版

<WritingBlock id="58321" variant="document">**基准校准揭示了结构评分的判别局限**

在当前 EGFR 对照与多指标基准分析中，部分结构评分未能按已知对照类别形成稳定区分。ipTM 在已知阳性与阴性对照中出现排序反转；contacts 与 PAE 显示出值得进一步检验的差异，但其判别能力及跨预测器适用性仍需验证。

因此，我们不直接沿用未经本项目校准的通用阈值，而是将已知对照作为基准，评估指标的区分能力，并探索适用于不同预测器与目标的判据。

**当前结论：** 已观察到评分与对照类别不一致的情况；候选判据仍处于验证阶段，尚未建立通用阈值，也尚未证明筛选规则能够提高实验成功率。</WritingBlock>

这段话可以作为正文 6· 的过渡性叙事。它保留了项目的发现，同时不把探索性结果包装成已验证的方法。

## 三、正式改稿前，还有一个比改文字更重要的核查

目前你给出的资料中，有两组需要分开对待的结果：

- B1 的 EGFR 对照：人源 7D12 的 ipTM 为 0.622，scramble 为 0.665、0.706；鼠源 7D12 为 0.417，scramble 为 0.812、0.846。
- 新发现的 6 组基准记录：出现 mEGFR+Cetux 的 ipTM 最高，而有界面的 7D12 得分最低；同时 contacts、PAE 呈现更明显的差异。

**这两组记录不能在未核对运行条件前直接合并为同一个证据链。** 它们可能涉及不同的预测器、结构输入、复合物链组成或运行批次。前一组说明特定 EGFR 对照中的 ipTM 排序问题；后一组是否构成更广泛的反例，需要回到对应数据表确认。

建议按下面的顺序处理：

<list marker="number" gap={2}>
  <list-item>**确认六组基准的样本定义。** 逐行核对 target、binder/control、预测器、输入结构和运行批次，确认“有界面”与“无界面”标签有实际结构证据支持。</list-item>
  <list-item>**检查指标计算口径。** 特别是 contacts 的距离阈值、原子或残基计数方式，以及 PAE 的链间范围和聚合方法。确保不同预测器的数字确实可以比较。</list-item>
  <list-item>**复核重复性。** 如果关键对比只有单次预测，就把它报告为观察结果；有重复种子或独立运行记录时，再评估排序是否稳定。</list-item>
  <list-item>**重新评估阈值。** 先查看阳性、阴性分布和重叠情况，再在独立基准上评估候选规则。不要用同一批六组数据提出规则，又把它当成规则有效的独立证据。</list-item>
</list>

## 四、Zenodo macro-AP 校准：可以做，但要明确它回答什么问题

你们计划使用 Zenodo `15722219` 的基准数据进行 macro-AP 标定，这个方向值得继续。不过要先确定它与本项目任务的对应关系。

macro-AP 可以用于评估不同目标上的平均精确率表现，但它不能自动解决所有问题：

- 数据集中的复合物或对接姿态，是否与 de novo binder 候选的分布相近？
- 不同靶点的阳性和阴性如何定义？
- 同一靶点或高度相似的复合物是否同时出现在校准集和评估集？
- 你们要评估的是单一指标、多个指标组合，还是完整候选筛选流程？

尤其要防止数据泄漏：如果目标是证明规则能够迁移到新靶点，就需要按靶点划分校准与评估数据，而不是只做随机样本拆分。

因此，在正式完成分析前，C 页的 `Macro-AP calibration: incomplete` 应继续保留。

## 五、这对整份报告意味着什么？

我不建议删除原有的项目主线。你们的研究价值并不依赖于最后证明 contacts 一定优于 ipTM。

更稳健的主线是：

1. 建立蛋白结合剂的计算设计与结构评价流程。
2. 用已知对照检验结构评分的判别能力。
3. 发现部分评分与已知对照类别不一致，通用阈值也缺少项目内校准依据。
4. 比较互补指标，提出后续验证的候选判据。
5. 明确现阶段尚未证明实验结合能力，也尚未建立跨靶点通用筛选规则。

这条主线比“找到一个更好的评分指标”更经得起后续数据修订。它也与你此前确定的研究问题一致：不是追求哪个模型给出最高分，而是检验评分能否区分已知阳性与阴性对照。<MemoryCite />

**我最建议的下一步：先不要冻结正文的新结论，优先把 6 组基准的原始行数据、指标口径和运行条件核实清楚。** 核实之后再决定是否正式弃用 ipTM 作为主判据，以及 contacts/PAE 是否值得进入下一轮独立校准。

### user — `<UUID>` — 2026-10-18T07:16:58.064000+00:00

为什么要改啊，我P21没有出现阈值什么的啊，你说的是还没做出来的HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION吗

### assistant — `<UUID>` — 2026-10-18T07:17:04.123204+00:00

对，你说得对，我刚才把两件事混在一起了，抱歉。

**如果你的 P21 目前没有展示阈值或 `all_pass` 规则，那就不需要为了这次基准数据更新而修改 P21。** 我之前建议改的内容，实际上是针对尚未完成的 **“HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION”**，不是说你现有的 P21 一定有问题。

我们应该区分这两页：

- **P21：基准分析结果。** 讲已知阳性、阴性对照揭示了什么，以及结构评分存在哪些判别局限。
- **HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION：候选筛选方法。** 讲如何综合多个指标、是否采用阈值、如何处理不同预测器的差异，以及如何据此比较候选物。

所以现在不应该直接把 `contacts ≥ 100 AND PAE < 10` 写成已确立的筛选规则。它来自新一轮基准分析，目前最多是**待验证的探索性判据**；在原始数据和计算口径核对完成之前，也不应据此认定 contacts 和 PAE 已经是可靠的主判据。

**我建议：先保留 P21，不动现有页面。** 等我们确认那张尚未完成的候选筛选页具体写了什么，再决定是否需要更新它。这样也能避免为了适配新数据而提前改变整份 PPT 的叙事。

### user — `<UUID>` — 2026-10-18T07:18:33.117000+00:00

现在正文还需要改动吗

### assistant — `<UUID>` — 2026-10-18T07:18:37.660738+00:00

我的判断是：**正文暂时不需要整体改动，但需要做一次针对新基准结果的定点核对。** 不应该为了尚未完成的 `HOW MULTI-METRIC EVIDENCE GUIDES CANDIDATE SELECTION` 页面，提前重写现有正文。

结合你目前的 AI-BinderDesign 汇报结构，我建议这样处理：

| 正文部分 | 现在是否要改 | 原因 |
|---|---|---|
| Background / Project Origin | 不用改 | 项目背景和研究问题不受这次基准结果直接影响 |
| Computational Workflow | 原则上不改 | 工具流程仍然成立；只需避免把流程描述成已验证有效的筛选算法 |
| Evidence Chain | 暂时保留 | 重点是从已知生物学证据走向基准校准，不必提前给出最终判据 |
| **P20：基准校准真正告诉我们的事** | **原则上保留** | 现有核心观点“分数不是判决、阈值需要校准”仍然成立 |
| **P21：基准分析结果** | **先核对，不急着改** | 要确认新 6-group 数据与现有 EGFR 对照是否属于相同的实验对象、预测器和计算条件 |
| Candidate Selection / Multi-Metric Evidence | 等数据核验后再定稿 | 目前不能把探索性规则写成已验证的筛选方法 |
| Limitations / Future Work | 只需检查表述 | 保留尚未建立通用阈值、缺乏实验验证等边界 |
| Conclusion | 原则上保留 | 仍然可以强调基准校准的必要性，而不是宣称已找到最优指标 |

## 现在真正需要检查的只有三件事

1. **正文有没有把探索性发现写成确定结论。** 例如，如果正文已经写成“contacts 和 PAE 是可靠的主判据”，就需要收紧表述；如果只是说它们值得进一步分析，就不用改。

2. **正文有没有使用尚未核实的新数据。** 特别是 6-group benchmark 的数据，不能在没有确认对象、条件和计算口径的情况下，直接与原有 EGFR 的 7D12 / scramble 对照合并。

3. **正文有没有把候选筛选描述成已验证的方法。** 如果只是介绍计划采用的多指标分析思路，可以保留；如果声称某个阈值或组合规则已经证明能够筛出真实结合剂，就需要修改。

**我的建议是：先冻结正文，不做大范围重写。** 优先核对 P21 和正文中有关指标判别能力的句子，再完成候选筛选页。只有当新数据确实改变了某项正文结论时，才做最小范围修改。

不过，我现在依据的是我们此前讨论过的页面结构和内容，**并没有逐页重新检查你当前的完整 PPT 文件**，所以不能保证每一页都无需修改。若要给出准确的逐页修改清单，需要以当前版本的正文为准。

### user — `<UUID>` — 2026-10-18T07:19:33.745000+00:00

1.没有 2.不确定，怎么检查？ 3.没有

### assistant — `<UUID>` — 2026-10-18T07:20:39.929078+00:00

那目前可以先确定两件事：

- 你没有把探索性发现写成确定结论。
- 你没有声称筛选规则已经被证明有效。

因此，**现在最需要检查的是第 2 项：正文有没有使用新一轮 6-group benchmark 的数据，或者把它和原有 EGFR 对照混在一起。** 这不意味着正文一定有问题，而是需要确认数据来源和表述是否一致。

## 怎么检查？

最稳妥的办法不是逐页凭印象看，而是建立一张简单的「数据来源—正文引用」核对表。

| 检查项 | 具体要确认什么 |
|---|---|
| 数据来源 | 这句话的数据来自原有 EGFR 7D12 / scramble 对照，还是新的 6-group benchmark？ |
| 研究对象 | 是 EGFR、PD-L1，还是其他目标？是否涉及 mouse EGFR？ |
| 预测器 | 数据来自 ColabFold、Boltz-2，还是二者都有？ |
| 指标与计算口径 | 比较的是 ipTM、PAE、contacts 等哪个指标？计算方式是否一致？ |
| 结论范围 | 这组数据只能说明某次对照中的现象，还是有足够证据支持更广泛的结论？ |

尤其注意：**指标名称相同，不代表数据就可以直接合并。** 如果预测器、复合物定义、链设置或计算方法不同，必须先确认可比性。

## 我先替你查了一下现有资料

我在资料库里找到了一份《AI-BinderDesign-报告幻灯片.pptx》，但它的存档时间是 **10 月 15 日**，早于你后来整理的 10 月 18 日版本，因此不能把它当作最新正文。<FileCite ref_id="turn4file2" />

这份旧版本里有一处值得重点核对：

> 实测反例（TNF 体系）：乱序阴性 ipTM 0.846；真 binder 7D12 ipTM 0.417。

但根据我们此前核对过的数据，**0.846 和 0.417 对应的是 mouse EGFR 的 scramble_2 与 7D12 对照，而不是 TNF-α 对照**。<FileCite ref_id="turn4file2" />

如果这段内容在你的最新版本中仍然存在，就需要更正；如果你已经修改过，就不必重复处理。

## 下一步最省事的办法

请把你现在正在使用的**最新 PPT 上传到这段对话**。我会只检查正文 P1–P26，不动页面，也不先提改稿建议，只做这三项核对：

1. 正文中的每组数值能否追溯到正确的靶点、对照组和预测器。
2. 新的 6-group benchmark 有没有被误写成原有 EGFR 或 TNF 对照的结果。
3. 正文结论是否超出了相应数据实际支持的范围。

最后给你一份简洁的核对清单：**页码、原文、核对结果、是否需要修改及原因**。

这样我们就能判断正文到底需不需要改，而不是凭印象决定。

### user — `<UUID>` — 2026-10-18T07:27:03.619000+00:00

感觉附录没啥用啊，能不能全部删掉不要脸

### assistant — `<UUID>` — 2026-10-18T07:27:08.435107+00:00

我觉得**可以删掉大部分附录，但不建议现在直接全部删除**。你的感觉有道理：如果这份 PPT 是给导师看、希望体现你的研究能力，附录不能只是把数据字典、工具参数、流程细节堆在正文后面。

关键是区分两件事：**汇报时不展示附录**，和**把附录从正式报告里彻底删除**。

## 我建议这样处理

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="check-circle" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **保留在正文中的内容**

      - EGFR 阳性与阴性对照的核心结果
      - 基准校准为什么必要
      - 你主导完成的评价分析与方法学发现
      - 当前结论的边界和后续实验验证计划

      这些才是支撑研究故事的证据。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="archive" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **从汇报版中删除或移出的内容**

      - 详细指标数据字典
      - 大量运行参数、文件字段与复现细节
      - 尚未核实的 PD-L1、TNF-α 等补充结果
      - 与正文重复的流程说明
      - 暂时无法支撑核心结论的技术细节

      这些可以留在 GitHub 仓库或项目资料库中，不必全部塞进汇报 PPT。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align=center justify=center>
      <icon name="file-check" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **值得考虑保留的少量补充页**

      - 核心 benchmark 的完整对照表
      - 指标定义及计算口径
      - 复现条件与数据来源

      如果导师追问“这个结论依据什么数据”“你具体怎么算的”，这些页就有价值；没人追问时，可以完全不展示。
    </box>
  </row>
</box>

## 对你这份报告，我的具体建议

你目前的正文是 P1–P26，附录是后续独立编号的 A1–F 等页面。**我倾向于把正式汇报版控制在正文 26 页，附录移出主文件，另存为单独的技术补充材料。**

不过有一个前提：正文中的关键结论必须有可追溯的数据来源。删除附录不等于删除证据，也不能让正文留下没有依据的数字。

另外，如果你说的“全部删掉”是指**连独立的补充材料也不保留**，我不太建议。你想把这个项目发展成正式科研项目，原始结果、参数和复现记录对后续联系导师、继续研究、整理 GitHub 都有价值。

**一句话：汇报版可以不带附录，研究资料不要丢。** 这样既能让 PPT 更干净，也不会牺牲项目的可核查性。

### user — `<UUID>` — 2026-10-18T07:49:00.445000+00:00

最后是不是要加一页感谢观看之类的

### assistant — `<UUID>` — 2026-10-18T07:49:04.662629+00:00

我建议**最后加一页，但不要只写“感谢观看”**。你的 PPT 是科研项目汇报，最后一页最好既有结束感，也能让老师记住项目的核心问题。

我更推荐下面这种方案：

<box gap={3}>
  <box border radius="lg" padding={4} gap={2}>
    <badge color="success">推荐</badge>
    <AsyncImage query="minimalist scientific research presentation closing slide white background deep red accent clean academic presentation design" aspectRatio="16:9" width="100%" />
    <title size="lg">Thank You</title>
    <text color="secondary" size="sm">基于科研汇报风格的结束页构思</text>
    <divider />
    **AI-BinderDesign**

    *A Benchmark-Calibrated Pipeline for De Novo Protein Binder Design and Structural Evaluation*

    感谢聆听，欢迎交流与指正

    <text color="secondary" size="sm">底部可保留：上海交通大学 · 项目汇报</text>
  </box>
</box>

## 为什么这样更合适？

- **保留正式感**：比单独放一行“感谢观看”更像科研报告。
- **呼应项目主线**：标题再次出现，评委能记住你的项目名称。
- **不额外引入结论**：结束页不需要再塞指标、数据或新的研究主张。

## 放在最后怎么处理？

如果正文是 P1–P26，我建议：

- **P27：Thank You / 感谢聆听**
- 附录不必放在结束页之前。若决定保留技术附录，可以放在结束页之后，答辩时需要再翻过去展示。

这样，正常汇报会停在感谢页；如果老师追问数据、参数或对照细节，你仍然可以调出附录。

**我的建议：加一页简洁的结束页，不要为了它再增加研究内容。**

### user — `<UUID>` — 2026-10-18T07:49:55.521000+00:00

给个提示词

### assistant — `<UUID>` — 2026-10-18T07:50:00.058714+00:00

可以直接把下面这段提示词发给 PPT 生成工具，让它按照你现有 AI-BinderDesign 汇报的风格制作最后一页。

<WritingBlock id="58317" variant="standard">请为我的科研项目汇报 PPT《AI-BinderDesign: A Benchmark-Calibrated Pipeline for De Novo Protein Binder Design and Structural Evaluation》设计一页正式、简洁的结束页（Closing Slide）。

**一、整体风格**
- 16:9 横版，纯白背景，学术汇报风格。
- 与上海交通大学风格的科研 PPT 保持一致，以交大红作为唯一主要强调色，搭配黑色与深灰色。
- 排版克制、整洁、有留白，具有生命科学与计算蛋白质设计的专业感。
- 与前文视觉风格统一，不要突然切换成商业路演、科技发布会或宣传海报风格。

**二、页面文字**

主标题：
Thank You

项目名称：
AI-BinderDesign

英文副标题：
A Benchmark-Calibrated Pipeline for De Novo Protein Binder Design and Structural Evaluation

中文结束语：
感谢聆听，欢迎交流与指正

可选的小字署名：
上海交通大学 · 项目汇报

**三、排版要求**
- “Thank You”作为视觉中心，字号醒目但不过度夸张。
- “AI-BinderDesign”置于主标题附近，清楚展示项目名称。
- 英文副标题字号较小，控制在一至两行内。
- 中文结束语位于页面下方或靠近主标题的位置，保持视觉平衡。
- 可使用一条细红线、简洁的几何线条或极淡的蛋白质结构轮廓作为辅助元素，但不能喧宾夺主。
- 保持页面简洁，不要添加大段文字、复杂背景、卡通元素、无关图标或装饰性数据图表。

**四、严格限制**
- 不要新增研究结论、实验结果、性能指标或未经验证的科研主张。
- 不要使用“成功设计高亲和力结合剂”等可能夸大研究成果的表述。
- 不要添加虚构的导师姓名、作者名单、联系方式或学校 Logo。
- 不要改变项目名称与英文副标题的拼写。
- 最终效果应像一份严谨的本科生科研项目报告的结束页，而不是普通课程作业的“谢谢观看”页面。</WritingBlock>

**额外建议：** 如果生成工具支持参考文件，最好同时上传你当前 PPT 的最后一张正文页或封面，让它沿用现有的字体、红色和留白比例，而不是重新设计一套风格。

### user — `<UUID>` — 2026-10-18T07:56:10.174000+00:00

如果我不是做报告的形式，只是让导师查看是否还要用聆听呢

### assistant — `<UUID>` — 2026-10-18T07:56:15.462497+00:00

对，如果是发给导师阅读、让导师审阅项目，而不是现场汇报，**“感谢聆听”就不合适了**，因为导师是在看材料，不是在听你讲。

我更推荐用 **“感谢阅读，恳请批评指正”**，正式、谦逊，也符合本科生向导师展示科研项目的语境。

可以考虑这三种：

- **最推荐：** 感谢阅读，恳请批评指正
- **更简洁：** 感谢审阅，欢迎指正
- **更偏学术交流：** 欢迎批评指正与交流探讨

对于你的 AI-BinderDesign 项目，我建议结束页这样写：

<box background="#FFFFFF" theme="light" border radius="lg" padding={6} gap={4} align="center">
  <text color="#A6192E" weight="medium" size="sm">SJTU · AI FOR SCIENCE</text>
  <title size="2xl" color="#202020" textAlign="center">Thank You</title>
  <title size="lg" color="#A6192E" textAlign="center">AI-BinderDesign</title>
  <text color="#555555" textAlign="center" size="sm">A Benchmark-Calibrated Pipeline for De Novo Protein Binder Design and Structural Evaluation</text>
  <divider color="#A6192E" />
  <title size="md" color="#202020" textAlign="center">感谢阅读，恳请批评指正</title>
</box>

这里的 `SJTU · AI FOR SCIENCE` 只是视觉示例；如果项目并非正式隶属于相关实验室或平台，建议删掉，避免造成归属误解。

**另外，如果这份 PPT 的主要目的是联系导师、争取加入课题组，结束语甚至可以更有针对性：**

> 恳请老师批评指正，期待进一步交流。

这比泛泛的“感谢阅读”更能体现你制作这份材料的目的，同时又不会显得过分功利。

### user — `<UUID>` — 2026-10-18T08:01:28.373000+00:00

你觉得项目报告有必要在页面上做艺术修饰吗

### assistant — `<UUID>` — 2026-10-18T08:01:32.623059+00:00

我觉得**有必要做视觉设计，但没必要做艺术修饰**。尤其是你的 AI-BinderDesign 项目，如果目的是让上海交大的导师判断你有没有科研潜力，PPT 应该优先体现科学问题、证据链和研究判断，而不是视觉上的炫酷。

我会把原则概括成一句话：

**让设计帮助导师理解研究，而不是让导师注意到设计本身。**

## 哪些值得做，哪些不值得？

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="minimalist academic scientific presentation slide white background dark red accent clean typography generous whitespace research presentation" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **1. 值得做：统一的学术视觉系统**

      <text color="secondary" size="sm">统一字体、标题层级、交大红强调色、页边距、图表配色和页面编号。让整份报告看起来经过认真整理，而不是临时拼出来的。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="scientific protein binder protein protein complex molecular structure ribbon visualization white background academic figure" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **2. 值得做：能解释科学问题的图**

      <text color="secondary" size="sm">蛋白质结构、设计流程、阳性与阴性对照的分数对比、指标判别结果。这些视觉元素不仅美观，还能直接传递研究信息。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="overdesigned futuristic AI technology presentation slide glowing neon blue red 3D effects busy background" aspectRatio="4:3" maxWidth="124px" />
    <box flex="1" gap={1}>
      **3. 不值得做：纯装饰性特效**

      <text color="secondary" size="sm">大面积渐变、发光文字、复杂粒子背景、每页不同的艺术构图、无实际含义的 DNA 装饰。这些往往增加视觉噪声，也容易让科研报告显得像商业宣传。</text>
    </box>
  </row>
</box>

## 对你的 AI-BinderDesign，我会怎么处理？

| 页面类型 | 设计投入 | 应该突出什么 |
|---|---|---|
| 封面 | 中等 | 项目名称、研究定位、专业感 |
| 研究背景与问题 | 较低 | 研究动机、明确的问题 |
| 计算流程 | 较高 | 输入、方法、输出与团队分工 |
| Benchmark 结果 | 最高 | 对照组、数据、指标差异与解释边界 |
| 局限与后续工作 | 中等 | 哪些已经证明、哪些仍待验证 |
| 最后一页 | 较低 | 简洁、正式、方便交流 |

特别是你的项目，最值得花时间的其实是 **Benchmark 结果页**。你想传递的核心不是“我们用 AI 设计了蛋白质”，而是：

> We did not ask which model gives the highest score. We asked whether the score can distinguish known binders from known non-binders.

这个问题本身就有研究价值。应该让对照数据、评分差异和你的分析逻辑成为页面的视觉中心，而不是用艺术效果包装它。

## 一个我认为合适的视觉标准

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" size="xs" weight="medium">AI-BINDERDESIGN · DESIGN PRINCIPLES</text>
  <grid columns={2} gap={2}>
    <grid-item>
      <box background="#A6192E" radius="md" padding={3} gap={1}>
        <title color="#FFFFFF" size="md">科学优先</title>
        <text color="#FFFFFF" size="xs">证据比装饰重要</text>
      </box>
    </grid-item>
    <grid-item>
      <box background="#F2F2F2" theme="light" radius="md" padding={3} gap={1}>
        <title color="#222222" size="md">克制表达</title>
        <text color="#555555" size="xs">留白比堆叠重要</text>
      </box>
    </grid-item>
    <grid-item>
      <box background="#F2F2F2" theme="light" radius="md" padding={3} gap={1}>
        <title color="#222222" size="md">图表准确</title>
        <text color="#555555" size="xs">可追溯比炫目重要</text>
      </box>
    </grid-item>
    <grid-item>
      <box background="#F2F2F2" theme="light" radius="md" padding={3} gap={1}>
        <title color="#222222" size="md">风格统一</title>
        <text color="#555555" size="xs">整套一致比单页惊艳重要</text>
      </box>
    </grid-item>
  </grid>
</box>

**我的最终建议：** 不要把它做成一份“很有艺术感的 PPT”，而是做成一份“视觉清晰、证据扎实、具有科研气质的项目报告”。

导师未必会因为你做了漂亮的动画而更愿意带你，但如果他能在几分钟内看清楚你做了什么、发现了什么问题、怎样判断证据是否可靠，以及你知道哪些结论还不能下，他就更容易判断你的科研思维。

### user — `<UUID>` — 2026-10-18T08:02:17.984000+00:00

那有没有必要在页面背景加一个浅浅的交大校徽呢

### assistant — `<UUID>` — 2026-10-18T08:02:22.432368+00:00

我的建议是：**不建议每一页背景都加浅浅的交大校徽，但可以考虑在封面上使用一次。**

你的 AI-BinderDesign 是准备给导师审阅的科研项目报告，视觉上应该让人首先看到研究内容，而不是学校标识。校徽用得好可以增加归属感，用得不好则容易让页面显得像模板水印。

## 我会这样安排

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="minimalist white academic research presentation cover subtle university emblem watermark upper corner scientific thesis design" aspectRatio="4:3" maxWidth="136px" />
    <box flex="1" gap={1}>
      **封面：可以加**

      <badge color="success">推荐</badge>

      如果你希望体现上海交大的学习背景，可以在角落放一个小尺寸校徽，或者使用非常淡的水印。项目标题仍然是视觉中心。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="minimalist white scientific presentation slide clean red accent data chart academic layout no background watermark" aspectRatio="4:3" maxWidth="136px" />
    <box flex="1" gap={1}>
      **正文：不建议加**

      数据图表、蛋白结构和流程图已经需要足够的视觉空间。背景水印会降低复杂图形与小字号文字的清晰度，尤其是 Benchmark 结果页。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="minimalist academic presentation closing slide white background thin dark red line clean typography" aspectRatio="4:3" maxWidth="136px" />
    <box flex="1" gap={1}>
      **结束页：可选**

      可以沿用封面的红色细线或小型标识，不必再次铺设大面积校徽水印。
    </box>
  </row>
</box>

## 如果你坚持想做全篇水印

建议遵循这几个原则：

- **透明度极高**：视觉上只隐约可见，不影响阅读。
- **避开内容密集区**：不要压在数据、图表、蛋白质结构和正文文字下面。
- **尺寸不要太大**：宁可小一些，也不要让校徽成为每页最醒目的元素。
- **使用准确的校徽文件**：不要让 AI 重新绘制或生成校徽，避免标志变形；也不要暗示项目获得了学校或实验室的正式背书。

不过，对你这份报告，我更推荐另一种做法：**纯白背景 + 交大红标题强调 + 统一页码与细线**。它更接近成熟的学术报告风格，也更能突出你对研究问题和证据的处理。

如果你想保留学校辨识度，封面小校徽就足够了。

### user — `<UUID>` — 2026-10-19T07:20:17.429000+00:00

这是项目报告完整版，整体的框架我已经不打算改动了，你现在逐页逐字审查核对，看看有没有什么细节需要改进，或者是语句不通、错别字什么的，力求精致完美

### assistant — `<UUID>` — 2026-10-19T07:51:25.221673+00:00

我会按你这份 PPT 的**现有框架逐页审校，不建议为了润色而重做结构**。审查重点不是单纯把句子改得更漂亮，而是让整份报告达到可以交给导师细读的标准：文字准确、术语统一、图表说明完整，尤其不能让一句看似顺口的话把计算结果说成实验结论。

先说总体判断：**报告的主线已经比较完整，暂时不需要大幅调整章节结构；但还有一些值得在提交前认真修正的细节。** 我尤其注意到以下几类问题：

1. **科学表述的证据边界**：例如把乱序阴性写成“按构造不可能结合”，或把计算预测结果写成“对照实验实测”，容易让读者误解为已经有湿实验验证。
2. **方法论表述强于实际结果**：例如“每把分数尺子，先在已知答案上验证过才使用”“每道门槛必须能让满分参照通过”，可能让导师以为所有指标和门槛都已经完成系统标定。
3. **TNF-α 部分的证据链**：从初始预测、受控重跑到实验结构比较，有些结论需要更明确地区分“观察到的现象”“可能的解释”和“已验证的结论”。
4. **逐字层面的精修**：个别英文表达、标点、术语、标题与正文的对应关系，以及少数不够自然或不够严谨的中文。

下面按页面顺序给出审校清单。为了便于你实际修改，我会区分**必须修改、建议润色、需要核实**，并优先列出真正影响报告可信度的项目，而不是为了显得审得仔细而机械地改动每句话。

## 一、建议先修正的 8 个关键问题

这些问题比一般的措辞润色更重要，建议先处理。

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">01</title>
    </box>
    <box flex="1" gap={1}>
      **第 20 页：计算结果被写成了实验结果**

      原文：“对照实验实测”“同一批参数实测”。

      建议分别改为“**同批次计算预测结果**”和“**同一预测设置下的 ipTM**”。这页的 0.417 和 0.846 是结构预测指标，不是湿实验测得的结合亲和力。

      另外，“乱序阴性对照（按构造不可能结合）”说得过于绝对。序列乱序本身不能证明其绝对不结合，建议改为“**设计型乱序阴性对照（预期为非结合对照，尚未经实验验证）**”。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">02</title>
    </box>
    <box flex="1" gap={1}>
      **第 4 页：把尚未完成的校准写成了已经完成的步骤**

      原文：“每把分数尺子，先在已知答案上验证过才使用”“阳性、双阴性参照确定门槛”“每道门槛必须能让满分参照通过”。

      建议改为：

      - 标题：**“一条以基准校准为原则的计算流程：先评估指标，再决定如何使用”**
      - “阳性、双阴性参照确定门槛”→“**基于阳性与双阴性参照评估指标的判别能力，并探索候选门槛**”
      - “每道门槛必须能让满分参照通过”→“**检查预设门槛对已知阳性对照的通过情况；若出现不符合预期的结果，需回查门槛、输入结构与预测条件。**”

      原因：报告后面明确承认，当前的阈值示例尚未经独立验证；因此不能让流程图暗示所有指标都已完成标定。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">03</title>
    </box>
    <box flex="1" gap={1}>
      **第 5 页：把 Kd 直接等同于排名真值，不够严谨**

      原文：“实验亲和力（Kd）＝排名真值”。

      建议改为：“**实验测得的结合亲和力（如 Kd）可用于外部检验计算排序；实验结果可进一步用于校准后续评价规则。**”

      Kd 是实验测量得到的亲和力指标，不会自动等同于整个候选池的“排名真值”。要检验排序，还需要明确测量了哪些候选、测量条件是否可比，以及如何根据实验结果进行排序。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">04</title>
    </box>
    <box flex="1" gap={1}>
      **第 14–15 页：鼠源 TNF-α × Infliximab 的阴性标签前后不一致**

      第 14 页写着“特异性阴性标签待进一步核实”，但第 15 页图例又把体系 03 归为“物种差异 / 阴性参照”，标题还称 ipTM 排序与已知生物学关系不一致。

      建议在核实前统一使用“**物种差异参照（阴性标签待核实）**”，不要把体系 03 当成已确认的阴性样本用于支持明确的判别结论。第 15 页可以改为：

      “**四组预测的 ipTM 均值与观测范围存在重叠，未呈现清晰的分离；由于体系 03 的阴性标签仍待核实，本结果主要说明当前预测分数不足以单独判定这些体系的生物学关系。**”
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">05</title>
    </box>
    <box flex="1" gap={1}>
      **第 17 页：不同样本量的范围比较，不能单独证明一致性提高**

      图中将原始预测 \(n=15\) 与受控重跑 \(n=5\) 的接触数范围并列比较。受控重跑的范围更窄，确实可以作为一个描述性观察，但样本数减少本身就可能使观测范围变窄。

      建议将“提示本轮模型间的界面接触模式相对一致”改为：

      “**受控重跑的 5 个模型中，观察到的界面接触数范围较原始 15 个模型更集中；由于两组样本量不同，这一差异尚不足以单独证明模型间一致性提高。**”

      如果你有原始数据，可以进一步比较中位数、离散程度及相同统计口径下的分布，而不是仅比较最小值和最大值。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">06</title>
    </box>
    <box flex="1" gap={1}>
      **第 19 页：“实验结构验证”与“更符合生物学关系”需要更强的支撑**

      目前页面呈现的是预测构型与实验解析结构的可视化比较。如果没有明确的结构叠合方法、链对应关系及定量比较结果，标题“实验结构验证”和英文 “More biologically plausible arrangement” 容易让读者认为你已经完成了严格的结构验证。

      建议标题改为“**TNF–TNFR1：实验结构参照下的预测构型比较**”，英文副标题可用 “Comparison of Predicted Complexes with an Experimental Reference”。

      同时，建议在图注或页面底部补上实验结构的 PDB 编号、链对应关系，以及是否进行了结构叠合。若目前只是定性观察，建议将结论改为“**受控重跑的构型在可视化比较中呈现出与实验参照不同程度的相似性，仍需定量结构比较进一步检验。**”
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">07</title>
    </box>
    <box flex="1" gap={1}>
      **第 4 页与第 27 页：MSA 和指标定义仍有未解决的口径问题**

      第 4 页将“自建同源比对 MSA”写成了通用流程，但第 14 页又说明 TNF-α 基准未使用 ColabFold，且不同批次的预测条件可能不同。应明确哪些步骤用于设计、哪些用于基准预测，避免读者认为所有体系使用了同一套 MSA 设置。

      第 27 页仍保留“8 Å 口径与残基范围待脚本核实”“PAE 聚合方式待确认”“contacts 距离阈值待确认”等文字。作为提交导师审阅的正式报告，**这些未决定义最好在提交前核实，或明确标成尚未用于本次定量比较的指标定义**，而不是留在指标字典里。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} minWidth="44px" align=center>
      <title size="lg">08</title>
    </box>
    <box flex="1" gap={1}>
      **全篇缺少足够明确的文献与结构来源标注**

      报告涉及 EGF、7D12、Cetuximab 的物种特异性，Infliximab 对人源和鼠源 TNF-α 的识别关系，以及 TNF–TNFR1 的实验结构参照。这些是基准标签成立的基础，不宜只写“已有研究报道”而不提供来源。

      建议不改动正文框架，只在相关页面增加简短的编号引用，并在附录增加参考文献与结构来源列表。特别需要给第 19 页的实验结构标注 PDB 编号。引用来源应支持**具体的物种、构建体和结合关系**，不能只引用一个宽泛的靶点综述。
    </box>
  </row>
</box>

## 二、逐页审校：文字、术语与页面细节

下面的页码按 PPT 实际顺序编号（共 28 页），不是章节编号。

### 第 1 页｜封面

<badge color="warning">建议修改</badge>

- **日期：“2026 年 10 月 – 11 月”**：如果现在就准备发给导师，建议改成实际完成或提交日期，例如“2026 年 10 月”。目前写成跨到 11 月，容易让人以为报告还会持续更新。
- **作者贡献声明**：“评价指标判别力标定由作者主导完成”略显过强。考虑到正文仍有探索性阈值和待验证结论，建议改成“**两组对照基准体系的设计与分析、评价指标判别力分析由作者主导完成**”。这样既保留你的主要贡献，也不暗示已经完成系统的阈值标定。
- **“蛋白设计生成、换靶点流程工程与湿实验方案由团队成员完成”**：建议确认“湿实验方案”是否确实由团队成员完成。如果指的是方案设计而不是实验执行，可以写“蛋白设计生成、跨靶点流程工程及湿实验相关方案由团队成员负责”。
- **院系名称**：“上海交通大学 致远学院 · 生物科学”建议统一为“上海交通大学致远学院 · 生物科学”，减少不必要的空格。
- **视觉**：封面校徽水印比较大，但透明度较高，没有明显遮挡主标题。考虑到你是将报告发给导师审阅而非正式演讲，这一页可以保留；不必再加其他装饰。

### 第 2 页｜研究背景

<badge color="warning">建议修改</badge>

这一页的研究动机明确，但有三处表达略口语化或过于绝对。

| 原文 | 建议修改 |
|---|---|
| “一个靶点至少两三个月，大部分候选是废的” | “传统实验筛选通常需要较长的实验周期，且候选物淘汰率较高。” |
| “膜蛋白这类重要靶点恰恰伺候不了” | “部分膜蛋白靶点在表达、纯化及筛选平台适配方面存在较高难度。” |
| “换物种、换结合面，基本等于从头再来” | “更换物种或结合表位后，通常需要重新评估候选物的识别能力。” |

原因是原文适合口头讲解，但正式科研报告更适合用可辩护的表述。“至少两三个月”与“大部分”也属于需要来源支持的具体概括，若没有可靠引用，不建议保留为普遍事实。

另有一处**标题与内容不匹配**：

- 原文：“三条技术线的汇合”
- 下方实际列出靶点准备、骨架生成、序列设计、结构预测、按分数排序五个环节。

建议改成“**计算设计流程的关键环节**”，避免数量不一致。

“按分数排序　pLDDT · ipTM · 质心 …”也建议改成“**按指标排序：pLDDT、ipTM、界面几何等**”，因为质心不是与 pLDDT、ipTM 完全同类型的结构置信度分数。

### 第 3 页｜从比赛到研究问题

整体逻辑顺畅，不建议大改。

- “回答这个问题，需要 Benchmark-based metric evaluation”中英文混杂略生硬。建议改为“**要回答这个问题，需要基于基准评估各指标的判别能力。**”
- 研究问题“计算结构指标，能否可靠区分 binder 与 non-binder？”建议中文术语统一为“**计算结构指标能否可靠地区分结合剂与非结合对照？**”，英文保留原句即可。
- “不同结构指标给出不一致、甚至反向的候选排序”是一个有实质含义的观察。建议确认正文是否有对应数据支持。如果只有少数案例，使用“**在部分案例中，不同结构指标给出的候选排序不一致，甚至相反**”会更准确。
- 英文大小写建议统一：句中使用普通写法 `benchmark-based metric evaluation`，标题中的专有名词格式则另行统一。

### 第 4 页｜计算流程

除前面列出的校准表述外，还有一些文字细节值得调整。

| 原文 | 建议修改 |
|---|---|
| “固定随机种子（保证可复现）” | “固定随机种子，以提高结果的可复现性” |
| “贴合位置从晶体结构直接量出” | “基于实验解析的复合物结构确定界面位置” |
| “不含乱配对的半胱氨酸” | “避免非预期的半胱氨酸配对”——前提是实际流程确实有这一筛选规则 |
| “同时给指标‘体检’供数据” | “同时评估指标的判别能力，为后续校准提供依据” |
| “设置家族上限，控制候选冗余” | “限制同一序列家族的入选数量，以降低候选冗余” |

**还需明确 MSA 的适用范围。** “自建同源比对 MSA”看起来像每个靶点和每轮预测都执行了这一步。如果它只用于某些设计流程，应明确写成“设计阶段：按需构建 MSA”；如果基准预测采用空 MSA，则应在方法说明中单独注明，避免读者把两种设置混为一谈。

### 第 5 页｜证据链

本页的结构清楚，但结尾两句需要改。

- “实验亲和力（Kd）＝排名真值”建议按第一部分的版本修改。
- “证据逐步增强——计算证据 → 实验验证；每一级都建立在前一级被验证的基础上”逻辑上过于绝对。实验验证尚未完成，前面的每个计算阶段也并不都经过独立验证。

建议改为：

> **证据逐步增强：从计算预测与已知对照出发，最终由实验验证结合能力；计算证据本身仍需实验检验。**

此外，“已知阴性关系”与“乱序、换靶”建议区分为两类：前者是已有生物学依据的关系，后者可能只是人为设计的阴性参照。这样才能与后文的基准设计保持一致。

### 第 6 页｜项目总览

整体布局和三部分组织方式没有明显问题。

- “候选漏斗 939 → 104 → 20”建议在数字下补充每个数字的确切含义，例如“生成候选 → 通过筛选条件 → 最终入选”。当前虽有类似文字，但最好在图中保持一一对应。
- “多样性感知排序”是较具体的方法术语。请确认实际流程确实计算或使用了序列/结构多样性；如果只是人工避免候选冗余，可改为“考虑候选多样性的排序”。
- “下一步：实验验证（主办方统一测定）”表意清楚，可以保留。

### 第 7 页｜EGFR 案例

- “用 PyMol 显示……”中的软件名建议统一为 **PyMOL**。
- “结构来源：PDB 6ARU chain A”建议改成“**结构来源：PDB 6ARU，Chain A；残基编号按 UniProt P00533 映射**”，但前提是你实际使用了对应映射。因为本页列出的 hotspot 编号和构建体编号需要让读者清楚它们采用的是哪套编号体系。
- “EGFR 胞外域 Domain III（构建体 311–480）”与第 9 页基准构建体 `P00533[334–505]` 不同。你已经写了基准构建体不同，这是好事；建议两页都明确说明残基编号体系，以免读者把两套结构当成同一构建体。
- “人源优先设计 → 鼠源微调”可以保留，但若鼠源微调只是后续计划，而非已经完成的步骤，应在图示中区分“已完成”和“计划中的策略”。

### 第 8 页｜EGFR 设计流程

- “939 变体 × 5 次结构预测”有一点歧义。若实际含义是 939 个候选各进行了 5 次预测，建议写成“**939 个候选；每个候选进行 5 次结构预测**”。
- “生成 → 通过判据 → 入选”建议在 104 和 20 下方明确标记各自对应的阶段。
- “Boltz-2 / ColabFold”建议在方法说明中区分：哪些候选由哪一模型预测，是否对同一候选进行双预测器比较。仅用斜杠可能让读者误以为二者始终并行使用。
- “设计负责生成候选，评价负责判断哪些候选值得相信”是一句很好的总结，可以保留。

### 第 9 页｜EGFR 基准校准

这页的核心思想清楚，重点是来源和标签的准确性。

- “独立阴性对照”中的“独立”需要有明确含义。如果只是指与物种特异性阴性不同的另一种阴性参照，建议改成“**另设阴性对照**”或“**补充阴性对照**”，避免读者误解为独立数据集或独立验证。
- `P00533[334–505] · 172 aa` 建议规范为“**UniProt P00533，残基 334–505（172 aa）**”。
- `EGF`、`7D12`、`Cetuximab` 三组标签最好在页脚或附录中给出对应的生物学来源；这些标签是后续判别分析的基础。
- “本页基准用于观察指标表现，不用于直接确定通用阈值”表达准确，建议保留。

### 第 10 页｜置信度 ≠ 界面证据

本页数字和主旨明确，但数据口径需要更清晰。

- `pLDDT (Boltz)` 建议改为“**pLDDT（Boltz-2）**”，前提是确实来自 Boltz-2 输出。
- “观察区间”不够具体。若表示 15 个预测样本的最小值到最大值，建议直接写“**观测范围（n = 15）**”；若不是 15 个样本，则应写出实际样本数。
- `Contacts 30.2`、`Interface residues 15.2` 是小数，读者会自然理解为平均值。建议明确写“**平均接触数**”和“**平均界面残基数**”，并在图注中注明统计样本量。
- “同表其他五组”建议改为“**同一基准表中其余五组的均值范围**”，避免读者误以为是所有单次预测的取值范围。
- “仅凭界面描述数值，不判定界面优劣或稳定性”这句很重要，建议保留。

### 第 11 页｜EGFR 基准启示

整体无明显错别字，表述也比较稳健。

- 英文 `Confidence describes model predictions.` 略显简略，可润色为“**Confidence scores describe the model’s confidence in its predictions.**”
- 英文 `Confidence is part of the evidence, not the final criterion for specific binding.` 可以保留。
- 中文“必要参照”与“不能仅凭单一置信度指标”逻辑一致，无需再增加装饰性文字。

### 第 12 页｜评价策略

这页是全文从案例转向方法论的关键页，建议把探索性结论标得更精确。

- “约 94 候选分界点（30.2 与 157.0 的中点）”中，精确中点为 **93.6**。建议写成“**93.6（约 94）：探索性分界点**”，让数字可复核。
- “157–247.7 其余五组均值范围”建议改为“**其余五组的平均接触数：157.0–247.7**”。
- “校准阈值与联合判定”是方法步骤，但实际结果仍属于探索性分析。建议正文继续保留“尚未经独立验证，不能视为通用阈值”，不要在其他页面把它简化成“已确定阈值”。
- “独立阴性对照”与第 9 页同样需要统一术语。
- 最后一句“目标不是寻找一个万能分数……”准确，建议保留。

### 第 13 页｜TNF-α 靶点与生物学背景

<badge color="warning">需核实</badge>

- “Infliximab 是靶向人 TNF-α 的嵌合型单克隆抗体”可以保留，但建议加来源引用。
- “已有研究报道其不与小鼠 TNF-α 发生相应识别”与第 14 页“特异性阴性标签待进一步核实”存在不一致。建议在完成文献核对前改为：

  “**Infliximab 靶向人 TNF-α。其对鼠源 TNF-α 的交叉识别情况需结合可靠文献进一步核实，因此本项目暂将该体系作为物种差异参照。**”

- “可溶性 TNF-α 以同源三聚体形式发挥作用”建议附上来源，尤其是后面将结构上下文作为解释假设时，这一生物学事实是推理的基础。
- 本页的研究问题和任务定位表述清楚，可以保留。

### 第 14 页｜TNF-α 对照体系设计

- 副标题“两个已知相互作用参照，两个阴性参照”不完全准确，因为体系 03 的阴性标签还未核实。建议改为：

  **“两个已知相互作用参照，以及两个补充阴性／物种差异参照”**。

- 体系 03 的“对照角色”保留“物种差异参照（特异性阴性标签待进一步核实）”。
- 体系 04 的“GFP 为非同源蛋白，非 TNF-α 的已知特异性结合伙伴”可以保留，但建议在阴性标签处明确“**非同源阴性参照，未由实验确认绝对不结合**”。非同源并不等于实验上绝对不结合。
- “每体系 15 个预测样本，共 60 个样本，运行记录中未见失败任务”信息完整，建议保留。
- “跨预测器比较必须标明指标来源，不能混用不同模型的分数”非常重要，可以保留。

### 第 15 页｜TNF-α 预测结果

除了第一部分提到的标签问题，还建议检查以下细节：

- 图例“已知阳性参照（01 / 02）”可以保留；另一组建议写为“**物种差异参照（03，标签待核实）／非同源阴性参照（04）**”，不要把两者合并成同一类确定阴性。
- 标题“单一 ipTM 排序与已知生物学关系不一致”容易让读者理解为四组标签均已确定。建议改为“**TNF-α：ipTM 未呈现清晰的阳性／阴性分离**”。
- “参考线为已知阳性体系 01 的平均值 0.434（仅作对照，非分类阈值）”表述严谨，建议保留。
- “四组 ipTM 观测范围存在重叠”可以保留，但建议图注明确括号内范围为 15 个样本的最小值至最大值，而不是置信区间。
- 界面规模补充中的 `Contacts`、`BSA` 建议都明确为“平均值”，并标注单位。BSA 的单位应为 Å²；Contacts 则应注明是按原子还是残基计数，以及采用的距离阈值。

### 第 16 页｜结构上下文与补充预测

本页整体保持了探索性语气，这是优点。建议做以下精修：

- “整体 ipTM 0.937，Confidence 0.903”中的 `Confidence` 需要明确是 Boltz-2 的哪个输出字段或汇总分数，避免它与前面泛指的“模型置信度”混淆。
- “三组 pairwise ipTM 为 0.928、0.935 和 0.878”建议统一为中文“**三个链对的 ipTM 分别为……**”，或在全文统一使用 `pairwise ipTM`。
- “本次复查：输入构建体及结构上下文值得作为潜在影响因素进一步检验”准确，可以保留。
- 注释已经说明输入结构和运行设置仍需核验，建议确保这句话在正式提交前仍然符合最新进度；若已完成核验，应更新注释，而不是保留过时的“待核验”。

### 第 17 页｜受控重跑与界面接触分析

这一页最需要解决的是**术语和比较口径**。

- 标题“重新设计双链预测对照”不够准确。按页面中的输入，体系为两条 TNF-α 链加一条 TNFR1 ECD 链，总计三条蛋白链。建议改为：

  **“TNF-α：重新构建双 TNF 链输入的复合物预测对照”**。

  英文可用 `Controlled Rerun with a Two-Chain TNF Input`，避免让读者误解为整个复合物只有两条链。

- `Target complex 2 × TNF-α + TNFR1 ECD` 建议改成“**输入：2 条 TNF-α 链（各 157 aa）+ 1 条 TNFR1 ECD（164 aa）**”。
- `MSA server` 建议写成“**MSA：使用 MSA server**”，并在方法记录中明确具体设置。
- 图中 `A–C`、`B–C` 的原子接触数应在图注中明确为距离小于 5 Å 的原子对数；当前正文已有定义，建议确认图表的轴标签和图注保持一致。
- 由于原始预测和受控重跑的样本数不同，建议不要仅依据范围变窄就得出“模型间一致性更高”的结论。可保留为“**观察到的接触数范围更集中**”，并明确这是描述性观察。

### 第 18 页｜预测构型的可视化比较

- “原始预测中，TNFR1 相对于 TNF-α 两条链的空间位置与朝向呈现一种排布”语义重复且不自然。建议改成：

  “**原始预测中，TNFR1 相对于两条 TNF-α 链呈现特定的空间位置与取向。**”

- “受控重跑中，TNFR1 相对于 TNF-α 两条链的空间位置与朝向有所不同”建议改为：

  “**受控重跑所得构型中，TNFR1 相对于两条 TNF-α 链的位置与取向发生变化。**”

- “表面视图展示该预测构型中的链间空间关系”可保留，但建议在图片标题中说明具体是哪个预测构型、使用何种视图。
- “原始预测与受控重跑呈现不同的链间相对排布及表面接触模式；其与已知结合构型的一致性仍需通过实验解析结构比对验证。”这句话整体严谨，可以保留。

### 第 19 页｜实验结构参照下的预测构型比较

除前面提到的标题和结论强度外，还需要统一图中说明。

- `Experimental Reference and Predicted Complex Comparison` 建议改成更自然的 `Comparison of Predicted Complexes with an Experimental Reference`。
- `Distinct inter-chain arrangement` 可改为 `Different inter-chain arrangement`，但不是必须。
- `More biologically plausible arrangement` 是本页最需要谨慎的英文短语。若目前没有定量结构比较，建议改成 **`Qualitative comparison with the experimental reference`**，避免将“看起来更合理”写成已确认的结构优越性。
- 建议补上实验参照的 PDB 编号、链编号和结构叠合方法。若做过定量叠合，可报告适当的结构偏差指标；若没有，则应明确这是定性可视化比较。
- 中文底部结论和英文结论基本一致，但都使用了“可能”，不需要再增加更多模糊词。关键是把页面标题、图注和实际证据水平统一起来。

### 第 20 页｜基准校准的启示

本页的主要文字问题已经在第一部分列出，另外还有两处：

- “已知结合剂 7D12（真 binder）”建议改为“**已知结合剂 7D12**”。“真 binder”偏口语，也没有比“已知结合剂”提供更多信息。
- “人侧：乱序 0.706 vs 7D12 0.622”建议改为“**人源 EGFR：乱序对照 ipTM = 0.706，7D12 ipTM = 0.622**”，使数字与对象一一对应。
- “仅说明单一 ipTM 在该对照案例中判别失败，不推广至其他指标”这句建议保留，甚至可以继续突出。它很好地限定了结论的适用范围。

### 第 21 页｜从单一评分到多指标综合决策

这页同时包含项目内数据与外部结构对接基准，需要把两类证据区分清楚。

- `n5 / n20` 写法不够明确。建议改为“**n = 5**”和“**n = 20**”，并说明这是每个设置下的预测样本数、候选数，还是某种采样规模。若实际是两种候选池规模，则应写“5 候选”和“20 候选”，不要使用可能引起歧义的 `n5 / n20`。
- “PD-L1 迁移测试中，乱序阴性对照的 ipTM 均值高于候选池中位数 0.744”建议把均值和中位数分别标明，不要让读者误以为两者是同一种统计量。
- “高分 ≠ 真实结合：分数只说明结构自洽”不够准确。ipTM 不只是泛指结构自洽程度，而是模型对复合物界面相对排列的预测置信度。建议改成：

  “**高分 ≠ 真实结合：结构置信度反映模型对预测界面的信心，不等于真实结合证据。**”

- `1BRS Barnase–Barstar` 的 AUC、DockQ 阳性定义、样本数量及 Spearman 相关系数都属于重要的定量结果。建议在附录或参考资料中补充该分析的计算定义和数据来源，尤其说明质心判据的方向，以及这些数值是如何计算出来的。正文已经注明该结果不代表 EGFR/TNF-α 的筛选性能，这一点很好，应保留。
- “独立结构对接基准”中的“独立”建议明确指独立于本项目候选池的数据来源，还是仅指不同于 EGFR/TNF-α 的任务。若没有正式的独立测试集设计，最好改为“**外部结构对接基准**”或“**补充结构对接基准**”。

### 第 22 页｜讨论

这页没有明显的逻辑错误，属于全篇比较成熟的总结页。

- `The Boundary of Computational Evidence` 可以保留，也可以改成更自然的 `Limits of Computational Evidence`。
- “结构可信度和界面几何属于计算证据”“不能单独证明实验结合亲和力，也不能证明受体激动或抑制功能”表述准确，建议保留。
- “结构证据能够帮助筛选候选，但其解释必须受基准、靶点和任务边界约束”是很好的收束句，不建议再润色得更复杂。

### 第 23 页｜局限性

本页表述稳健，没有发现明显错别字。

- `PIPELINE AND EVALUATION DEPENDENCIES` 可以理解，但如果想更自然，可以改为 `PIPELINE DEPENDENCIES AND EVALUATION LIMITATIONS`。
- “当前工作建立了计算评价框架，但尚未验证候选物的实验结合能力或实验成功率”建议保留。这句话能有效防止读者将计算候选排序误解为已获得实验验证。
- “不同靶点的数据与证据完整度并不一致”准确，无需改动。

### 第 24 页｜未来工作

整体没有明显问题。

- `IMPROVE PIPELINE ROBUSTNESS` 与中文“完善评价流程”不完全对应。英文强调稳健性，中文强调完善流程。建议统一为：

  中文：“**提升流程稳健性**”

  英文：`IMPROVE PIPELINE ROBUSTNESS`

- “测量结合亲和力，例如解离常数 Kd”表述正确，可以保留。
- “对具有功能目标的项目进一步验证激动或抑制活性”也比较严谨，避免了将结合能力直接等同于功能活性。

### 第 25 页｜结论

三点总结与报告主线一致，没有必要调整结构。

- “提出基准校准思路”比“建立了通用评价标准”谨慎得多，建议保留。
- “据此比较和排序候选，为确定优先验证对象提供依据”可以保留，但建议确认“多指标排序”确实是当前已执行的流程；如果部分规则仍处于探索阶段，可以改为“**为比较候选并确定优先验证对象提供依据**”。
- 最后的中英文总结一致，建议保留。

### 第 26 页｜致谢

本页没有发现明显的文字错误，但这类信息最好逐项核实：

- 所有团队成员姓名是否与本人确认的写法一致。
- 班级、院系简称是否准确，尤其是不同年级的简称是否采用同一套格式。
- 指导教师姓名、院系和团队名称是否准确。
- `Venus 蛋白质设计模型团队` 是否为团队认可的正式名称。

这些信息不能只靠文字审校判断正确性。建议最后向团队成员核对一次，避免出现姓名或身份标注错误。

### 第 27 页｜指标定义

<badge color="warning">提交前需处理</badge>

这是附录中最需要进一步整理的一页。

- **`ipSAE_8A`**：目前写着“0.70 为通用分档表 Fail/Pass 边界、非本项目标定；8 Å 口径与残基范围待脚本核实”。这里同时包含一个具体数值、一个通用性主张和一个未确认的计算定义。建议在查清来源与实现前，不要把 0.70 写成通用边界；至少应明确它来自哪套分档规则，并说明是否与当前脚本中的定义一致。
- **PAE**：`须注明所用残基范围、链间区域与聚合方式（待确认）` 仍像内部审校备注。建议核实实际计算方法后写出具体定义，或暂时将该项标注为“本报告未用于定量筛选”。
- **contacts**：需要明确原子接触还是残基接触、距离阈值、去重规则。如果不同脚本使用了不同口径，不能只用一个泛化定义覆盖所有结果。
- **Interface SASA**：建议区分“界面 SASA 的变化量”与 `BSA`，并明确采用的是总界面口径还是单侧口径，避免把不同定义当成同一指标。
- “本表为候选结构指标字典，不代表所有指标均已在本项目中计算”这句可以保留，但它不能替代每个指标的具体定义。

**建议原则：附录中的每一个指标都应能对应到一个可复核的计算定义。** 不确定的内容宁可明确写“本报告未使用”，也不要留下“待确认”而又同时给出具体阈值的表述。

### 第 28 页｜结束页

- “感谢阅读，恳请批评指正”适合这份以供导师审阅为目的的报告，可以保留。
- “上海交通大学 · 项目汇报”建议改成“**上海交通大学 · 项目研究报告**”，与封面和正文的文档定位保持一致。
- 中央水印透明度较高，但相较封面更明显。可以保留，也可以略微缩小或淡化；不需要再增加其他装饰。

## 三、全篇统一性检查

除了逐页修改，我建议在最后一次修改时统一以下规则，避免每页单独看都没问题，连起来却显得不够精致。

### 1. 统一关键术语

| 建议统一的术语 | 使用原则 |
|---|---|
| 结构置信度 | 用于描述模型对预测结构或界面的信心，不直接等同于结合能力 |
| 已知阳性对照 | 有明确生物学依据的结合体系 |
| 阴性参照 / 阴性对照 | 区分已知不结合体系与设计型、尚未经实验确认的阴性参照 |
| 基准校准 | 若尚未完成独立验证，优先使用“判别力评估”“探索性校准”等表述 |
| 实验验证 | 仅用于真实实验结果；计算预测不应称为“实测” |
| 候选排序 | 表示优先验证顺序，不代表已证明结合或功能活性 |

特别注意：全篇的“阳性”“阴性”不应只看标签名称。对于已知生物学关系、物种特异性关系、乱序序列和非同源蛋白参照，应明确说明标签的证据来源与确定程度。

### 2. 统一英文格式

建议全篇检查以下细节：

- 软件名称统一：`PyMOL`、`Boltz-2`、`ColabFold`、`ProteinMPNN`、`RFdiffusion`。
- 指标大小写统一：`ipTM`、`pLDDT`、`PAE`、`pDockQ2`、`ipSAE`、`BSA`。
- 统计量统一：`n = 15`，不要在不同页面混用 `n15`、`n = 15` 或含义不明的 `n15` 式简写。
- 单位统一：`BSA (Å²)`；序列长度使用 `aa`；残基范围统一使用连接号，如 `311–480`。
- 英文标题的大小写风格尽量一致，不必为了装饰让每个短语都采用不同的大小写规则。

### 3. 视觉层面

我检查了整套幻灯片的渲染缩略图，也重点查看了封面、接触数对比页、结构可视化页和结束页。整体上，红白配色、标题层级、卡片风格与页眉系统比较统一，**没有必要再增加装饰元素或重新设计整套模板**。

提交前建议重点复查三类页面：

- **第 14–15 页**：四组对照和统计数字较多，图例与阴性标签需要一眼能分辨。
- **第 17–19 页**：这是全篇最需要精确解释的结构证据链，图注、结构来源和结论强度比装饰更重要。
- **第 27 页**：指标字典虽然作为附录，但它直接关系到导师能否复核方法。应优先解决定义未确认的问题。

## 四、我建议的最终修改顺序

如果你希望在不动整体框架的前提下，尽可能把报告打磨到位，可以按这个顺序修改：

<box border radius="lg" padding={3} gap={3}>
  <row align=start gap={3}>
    <icon name="alert-circle" size="xl" color="danger" />
    <box flex="1" gap={1}>
      **第一优先级：修正会影响科研可信度的表述**

      第 4、5、13–15、17、19–21 页，以及第 27 页的指标定义。尤其是“实验实测”“按构造不可能结合”“实验结构验证”“已完成阈值标定”等容易让读者误解的表述。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="book-open-check" size="xl" color="secondary" />
    <box flex="1" gap={1}>
      **第二优先级：补齐可复核的来源与方法口径**

      为生物学对照和实验结构补充引用；明确构建体、链编号、MSA 设置、接触数计算口径和样本统计方式。未确认的内容先核实，不要凭语言润色代替事实核查。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="spell-check" size="xl" color="secondary" />
    <box flex="1" gap={1}>
      **第三优先级：全篇文字精修**

      修改第 2 页的口语化表达、第 3 页的中英文混杂、第 7 页的 `PyMOL` 拼写，以及第 18–19 页不够自然的描述；统一术语、大小写、数字格式和单位。
    </box>
  </row>
</box>

最后给你一个整体判断：**这份报告最值得保留的是“从设计案例发现评价问题，再用已知对照检验指标”的主线。** 目前真正需要打磨的不是框架，而是让每一项结论的力度恰好与现有证据匹配。尤其是 TNF-α 的受控重跑与实验结构比较部分，只要把输入条件、比较方法和证据边界说明清楚，就能显著提升报告的可信度，而不需要推翻现有内容。

以上是基于这份 PPT 的逐页文字与可视化审校。涉及原始预测数据、脚本计算口径、结构叠合方法和文献标签的事项，我已标为需要核实；**这些不能仅凭幻灯片文字就认定为事实错误，也不应在未核实前直接改写成确定结论。**

### user — `<UUID>` — 2026-10-20T02:07:18.868000+00:00

这是最终pdf版本，你最后审一遍吧，仔细一点

### assistant — `<UUID>` — 2026-10-20T02:09:17.885533+00:00

我已经检查了这份 PDF 的 **28 页页面渲染**，并重点回看了上次提到的基准校准、TNF-α 对照、结构比较和指标定义等页面。

先给你一个重要结论：这版的整体视觉风格是统一的，章节主线也没有明显断裂，**现在更值得关注的是少数容易影响科学严谨性、数据可复核性和最终观感的细节**。我不会为了挑错而要求你再改框架，也不会把无法从 PDF 本身证实的内容直接判成错误。

有一个限制需要提前说明：这份 PDF 的文字层无法直接提取，因此我主要依据页面渲染逐页检查。图中非常细小的文字、原始计算过程和引用文献的真实性，仍有部分需要结合原始材料才能最终确认。

## 一、最终提交前，我认为还有 5 处值得处理

### 1. 第 14 页：TNF-α 阴性标签仍然写得过于确定

<badge color="danger">优先修改</badge>

这一处在 PDF 中仍然存在。页面标题下方写着“两个已知相互作用参照，两个阴性参照”，而体系 03 的角色标注为“物种差异参照（特异性阴性）”。

问题是：**物种存在序列差异，并不能单独证明该抗体对鼠源 TNF-α 完全不结合。** 如果这一标签尚未通过可靠文献或实验核实，就不宜直接称为已确认的特异性阴性。

建议修改为：

- 页面副标题：**两个已知相互作用参照，以及两个补充阴性／物种差异参照**
- 体系 03 对照角色：**物种差异参照（阴性标签待核实）**

第 15 页也应沿用相同标签。这样可以避免前面承认不确定性，后面却把它作为确定阴性用于比较。

### 2. 第 20 页：7D12 的物种标签需要更明确

<badge color="danger">优先修改</badge>

这页现在已经将 7D12 标为已知结合剂，也注明了人源 EGFR 的参考数值，但图中柱状数值为：

- 7D12：0.417
- 乱序对照：0.846

而页面脚注另列出人源 EGFR 的 7D12 = 0.622、乱序对照 = 0.706。

**两组数值对应不同的靶点物种，不能让读者误以为它们来自同一个体系。**

建议直接在柱状图的比较对象前补上：

- **鼠源 EGFR：7D12，ipTM = 0.417**
- **鼠源 EGFR：乱序对照，ipTM = 0.846**

脚注则保持“人源 EGFR”的标注。这样这页就同时呈现了两组结果，也能准确支持你的核心结论：单一 ipTM 在这一对照案例中未能按预期区分已知结合剂与设计型阴性参照。

### 3. 第 19 页：结论仍比图中证据稍强

<badge color="warning">建议修改</badge>

本页已经使用了更稳妥的标题“实验结构参照下的预测构型比较”，并标出了实验结构来源，这是很好的改进。

不过，页面底部仍写着：

> 原始 Boltz-2 预测可能没有正确呈现 TNF-α 与 TNFR1 的已知结合界面，而本次受控重跑则可能预测到了更符合已知生物学关系的结合构型。

这句话仍然容易让读者理解为受控重跑已经得到了结构上更可靠的答案。若目前只是可视化比较，且没有给出叠合后的定量结构偏差或界面比较指标，建议改为：

> **原始预测与受控重跑呈现出不同的链间相对排布。受控重跑的预测构型在可视化比较中与实验结构参照呈现一定相似性，但其结构一致性仍需进一步定量评估。**

此外，页面已列出 PDB 7KPB，但标注“未叠合”。这并不妨碍定性比较，不过建议在图注中明确：目前展示的是各自构型的可视化，而不是经过统一叠合坐标系后的直接结构偏差比较。

### 4. 第 27 页：指标定义表仍有两个未闭合的口径问题

<badge color="warning">建议修改</badge>

这页比之前的版本更完整：已经说明指标是否实际用于筛选以项目脚本和结果记录为准，也解释了指标的适用边界。

但有两处仍需留意：

- **ipSAE_8A：** 表中同时出现“0.70 为通用分类表 Fail/Pass 边界”与“8 Å 口径与残基范围待脚本核实”。在实际计算口径尚未核实的情况下，建议不要把 0.70 作为无条件适用的通用边界。可以改成“参考分类边界；具体适用性需依据指标定义和实现核对”。
- **PAE、contacts、Interface SASA：** 这些行要求说明聚合方式、距离阈值、原子／残基口径或界面面积定义。作为指标字典，这样写边界是合理的；但如果你希望它成为可复核的方法附录，最好在实际使用的指标旁给出具体定义，未实际使用的则明确注明“本报告未用于定量筛选”。

这不是说表中的指标名称有错，而是提醒你不要让定义表看起来比实际方法记录更确定。

### 5. 第 21 页：外部基准的相关系数需要最后核对一次

<badge color="warning">核对原始记录</badge>

页面列出了 Barnase–Barstar 外部结构基准的 AUC、DockQ 和 Spearman 相关系数，并且注明这些结果不代表 EGFR 或 TNF-α 的候选筛选性能。这种证据边界是正确的。

提交前建议核对原始分析记录中的三项内容：

- AUC = 0.9813 对应的阳性定义、样本数量及计算脚本。
- `DockQ ≤ 0.23` 的判据是否确实对应图中采用的类别定义。
- `Spearman ρ = −0.8506` 的负号是否正确，以及相关分析中两组变量的方向如何定义。

我不能仅凭 PDF 判断这些数值错误，但它们属于会影响定量结论的关键数字，值得在最终版本中确认一次。

---

## 二、其余页面的最终观感

我检查了 28 页的整体渲染，当前版本没有看到需要推翻版式或调整章节结构的问题。

<box border radius="lg" padding={3} gap={3}>
  <row align=start gap={3}>
    <icon name="check-circle" size="lg" color="success" />
    <box flex="1" gap={1}>
      **封面与结束页**

      中英文标题层级清楚，整体风格一致。日期“2026 年 10 月–11 月”只需确认是否仍准确反映实际报告周期；如果这是现在准备提交的定稿，写实际提交月份会更明确。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="check-circle" size="lg" color="success" />
    <box flex="1" gap={1}>
      **第 2–12 页：研究动机、流程与 EGFR 基准**

      整体逻辑连贯，尤其第 10–12 页从置信度与界面描述的区别过渡到基准校准，阅读顺序合理。第 12 页的 93.6 作为 30.2 与 157.0 的中点，数值计算正确；继续将它限定为探索性分界点即可。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="check-circle" size="lg" color="success" />
    <box flex="1" gap={1}>
      **第 16–18 页：受控重跑与结构可视化**

      这几页的叙述顺序比较自然。注意第 17 页比较 \(n=15\) 与 \(n=5\) 的接触数范围时，只能将范围变化作为描述性观察，不能单凭范围变窄就断言预测一致性提高。第 18 页对两种构型的描述基本清楚。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <icon name="check-circle" size="lg" color="success" />
    <box flex="1" gap={1}>
      **第 22–28 页：讨论、局限性、未来工作、结论与附录**

      总结部分保持了计算证据的边界，没有把结构预测直接写成实验结合或功能验证。附录指标定义仍有可完善之处，但不影响主文框架。
    </box>
  </row>
</box>

## 三、我的最终建议

如果你现在准备把 PDF 发给导师，我建议至少先完成这三项：

1. 第 14 页和第 15 页统一鼠源 TNF-α × Infliximab 的标签。
2. 第 20 页明确 0.417 与 0.846 对应的是鼠源 EGFR，避免与人源数值混淆。
3. 第 19 页将“更符合已知生物学关系”的结论收紧为定性观察，并明确当前未叠合。

之后再核对第 21 页的统计数值和第 27 页的指标定义。

**总体而言，这份 PDF 已经具备作为项目研究报告交给导师审阅的完整度。** 我没有发现需要重做框架的理由；最后阶段最重要的是把少数证据边界和数值标注处理干净，而不是继续追求装饰或大幅改写。

### user — `<UUID>` — 2026-10-20T02:26:50.035000+00:00

主要是想让你检查一下排版，有没有格式问题，比如文字重叠、错位什么的

### assistant — `<UUID>` — 2026-10-20T02:28:07.083293+00:00

明白了，这次只看排版，不再讨论科学内容和措辞。我重新按四张缩略总览检查了全部 28 页，并放大查看了较容易出现版面问题的页面。

## 排版检查结果

**目前没有发现明显的文字重叠、文本框相互遮挡、内容越出页面边界或整段文字被裁切的问题。** 整体版式是稳定的，页眉、标题、卡片、底部总结框的设计基本统一。

| 页码 | 排版检查结果 | 建议 |
|---|---|---|
| 1 | 封面信息层级清楚，未见明显重叠 | 无需修改 |
| 2–8 | 卡片、流程框及图片布局整体正常 | 无需因排版返工 |
| 9–12 | 基准表、指标卡片与总结框未见明显错位 | 无需修改 |
| 13–16 | 多卡片布局和图表区域整体规整 | 无需修改 |
| 17–19 | 图表与蛋白质结构图均在页面范围内 | 无明显溢出或遮挡 |
| 20–25 | 对照图表、三栏内容与结论框布局正常 | 无需修改 |
| 26 | 致谢名单字号偏小，远距离投影时可读性一般 | 可选优化 |
| 27 | 指标表格与底部注释较密，注释字号偏小 | 可选优化 |
| 28 | 结束页简洁，主体居中 | 无需修改 |

## 我认为值得注意的 3 个小问题

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="minimal scientific presentation dense appendix metric definition table white background" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      **第 27 页：底部注释比较拥挤**

      表格本身没有明显错位，但最后一行注释的字号较小，横向文字比较密集。建议适当增加注释字号或行距；如果空间不够，宁可精简注释，也不要压缩正文。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="academic presentation acknowledgements slide two column small text list white background" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      **第 26 页：致谢名单可读性略弱**

      两栏名单排列整体整齐，没有看到明显的文字碰撞。但投影展示时，小字号可能不够清晰。如果主要通过 PDF 阅读，这不是必须修改的问题。
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <AsyncImage query="scientific presentation slide footer small grey running header thin red horizontal line" aspectRatio="4:3" width="112px" />
    <box flex="1" gap={1}>
      **全篇：页眉与页脚的灰色小字**

      页眉中的报告标识、底部细线和浅色辅助文字整体一致。没有发现明显的越界，但这些小字在缩略图中对比度较弱；建议保持现状，不必为了增强可见度而破坏页面层级。
    </box>
  </row>
</box>

## 最后结论

如果你的目标是确认 PDF 导出后有没有明显的**文字重叠、元素错位、图片裁切或版面崩坏**，目前检查结果是：**没有发现需要因此返工的明显问题。**

第 26、27 页属于可读性优化，不是已确认的排版错误。其他页面建议保持，不要为了追求细微的视觉差异而反复调整。

说明一下检查范围：我检查了全部页面的整体布局，并放大查看了部分页面；这不等于对每一行极小字号的文字都做了像素级检查。因此我能确认的是没有发现明显的版面故障，不能保证绝对不存在细微的字距或对齐偏差。

### user — `<UUID>` — 2026-10-20T02:29:42.904000+00:00

那26页你觉得可以怎么优化

### assistant — `<UUID>` — 2026-10-20T02:30:12.075980+00:00

我放大看了第 26 页。我的建议是：**不需要重新设计，主要优化团队名单的可读性，以及上下两部分的视觉平衡。** 现在这页整体是整齐的，没有明显的文字重叠或错位，问题在于名单区域的视觉呈现稍微有点松散。

## 推荐方案：保留原布局，做 4 处微调

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="type" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **1. 团队名单字号稍微加大**

      当前姓名和专业班级信息的颜色偏灰，字号也略小。建议姓名提高约 1–2 pt，专业班级信息保持原字号或只略微增大。姓名用深灰色，班级信息用中灰色，继续保留主次关系。

      <text color="secondary" size="sm">优先级：高。能直接改善 PDF 阅读和投影时的辨识度。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="columns-2" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **2. 两栏名单统一对齐规则**

      保持现在左右各一栏的结构，但让每栏的姓名起点、班级信息起点和项目符号位置严格一致。姓名与班级之间可以稍微拉开一点距离，避免视觉上连成一串。

      <text color="secondary" size="sm">优先级：中。主要是提升精致度，不必大幅移动两栏。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="align-vertical-space-between" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **3. 稍微压缩团队名单上方的空白**

      “上海交通大学长江杯竞赛团队”标题和名单之间的间距可以略微缩小，同时将名单行距控制在统一范围。这样可以让团队名单更紧凑，为下面的指导教师区域留出更自然的空间。

      <text color="secondary" size="sm">优先级：中。只调整少量间距，不要把名单挤得太密。</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="contrast" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **4. 指导教师信息提高一点对比度**

      两位指导教师的姓名已经比较醒目，可以保留。下方单位和团队名称目前较浅，建议加深为中灰色；底部致谢框则保持现有浅底色和细边框，不必增加装饰。

      <text color="secondary" size="sm">优先级：中低。属于整体视觉统一的细节优化。</text>
    </box>
  </row>
</box>

## 调整后大致应该是什么效果？

<box border radius="xl" padding={4} gap={3}>
  <box gap={1}>
    <text color="#B4233B" weight="medium" size="sm">11 · ACKNOWLEDGEMENTS　|　致谢</text>
    <title size="xl">致谢</title>
    <text>谨向参与本项目的团队成员、指导教师及提供支持的相关人员致以诚挚感谢。</text>
  </box>
  <divider color="subtle" />
  <text color="#B4233B" weight="medium">项目团队　/　PROJECT TEAM</text>
  <title size="md">上海交通大学长江杯竞赛团队</title>
  <grid columns={2} gap={3}>
    <grid-item>
      <box gap={2}>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">黄兆锟</text>
          <spacer />
          <text color="secondary" size="sm">生科2603</text>
        </row>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">杨子文</text>
          <spacer />
          <text color="secondary" size="sm">生科2601</text>
        </row>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">薛尧宣</text>
          <spacer />
          <text color="secondary" size="sm">生科2602</text>
        </row>
      </box>
    </grid-item>
    <grid-item>
      <box gap={2}>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">余喆</text>
          <spacer />
          <text color="secondary" size="sm">生医科2650</text>
        </row>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">许多</text>
          <spacer />
          <text color="secondary" size="sm">人工智能2605</text>
        </row>
        <row align="center" gap={2}>
          <box background="#B8B4AD" size="5px" radius="xs" />
          <text weight="medium">朱博</text>
          <spacer />
          <text color="secondary" size="sm">人工智能2601</text>
        </row>
      </box>
    </grid-item>
  </grid>
  <text color="secondary" size="xs">以上仅示意姓名与班级的层级、对齐关系，并非完整名单或精确复刻。</text>
  <divider color="subtle" />
  <text color="#B4233B" weight="medium">指导教师　/　SUPERVISORS</text>
  <grid columns={2} gap={3}>
    <grid-item>
      **刘振华**

      <text color="secondary" size="sm">上海交通大学农业与生物学院</text>
    </grid-item>
    <grid-item>
      **洪亮**

      <text color="secondary" size="sm">Venus 蛋白质设计模型团队</text>
    </grid-item>
  </grid>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    **感谢所有为项目提供指导、协作与支持的老师和同学。**

    <text color="secondary" size="sm">We thank all team members, supervisors, and supporters for their guidance and collaboration.</text>
  </box>
</box>

上面是排版方向示意，不是要求把名单缩减成示例中的几个人。

**我的最终建议：** 只动字号、颜色和间距，不换模板、不加头像、不加图标装饰，也不把名单改成一堆卡片。整份报告的视觉语言是简洁的学术汇报风格，第 26 页继续保持这种风格最合适。

### user — `<UUID>` — 2026-10-20T02:35:05.091000+00:00

ipSAE_8A： 表中同时出现“0.70 为通用分类表 Fail/Pass 边界”与“8 Å 口径与残基范围待脚本核实”。在实际计算口径尚未核实的情况下，建议不要把 0.70 作为无条件适用的通用边界。可以改成“参考分类边界；具体适用性需依据指标定义和实现核对”。这一条改完之后完整的应该是什么样

### assistant — `<UUID>` — 2026-10-20T02:35:10.850668+00:00

我建议第 27 页 `ipSAE_8A` 这一行完整改成下面这样，既保留参考阈值，也明确说明适用范围尚待核实。

**推荐替换版本：**

| 指标 | 分类参考 | 备注 |
|---|---|---|
| `ipSAE_8A` | **0.70：参考分类边界（Fail / Pass）** | 具体适用性需依据指标定义、计算口径及脚本实现核对；8 Å 距离口径与残基范围待核实。 |

如果原表格的空间比较紧张，可以使用精简版：

| 指标 | 分类参考 | 备注 |
|---|---|---|
| `ipSAE_8A` | 0.70：参考分类边界 | Fail / Pass 的具体适用性待核实；8 Å 口径与残基范围待脚本核实。 |

**我更推荐第一版**，因为它把两件事分开了：

- **0.70 是什么：** 参考分类边界，不宣称是普遍适用的标准。
- **哪些内容还没确认：** 该边界是否适用于当前计算，以及 8 Å 的距离定义和残基范围。

另外，建议全文统一使用“参考分类边界”，不要在其他位置继续写成“通用分类表边界”或“通用 Fail/Pass 阈值”，以免前后表述矛盾。

## Coverage counts

```json
{
  "user": 67,
  "assistant": 67,
  "tool": 0,
  "other": 0,
  "hidden_assistant": 43,
  "null": 1,
  "orphan": 0
}
```
