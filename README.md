# 《大宋盛景·云上凡尘》(Northern Metropolis: The Surreal Dreamscape)
> **工业级东方超现实运镜短片 · MuseCanvas 视频提示词工程 · 跨镜头连贯与面部零扭曲全流程解决方案**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/badge/MuseCanvas-Compatible-brightgreen.svg)](https://github.com/songhengchang88-commits/changan-surreal-ai-cinematic)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Edge-TTS](https://img.shields.io/badge/Edge--TTS-Neural-purple.svg)](https://github.com/rany2/edge-tts)

---

## 📖 项目简介 (Overview)

**《大宋盛景·云上凡尘》** 是专为 **无限画布 (MuseCanvas)** 及主流 AI 视频生成大模型（可灵 Kling、Runway Gen-3、Wan 2.1、混元 HunyuanVideo、即梦 Seedance）打造的东方超现实主义 32 秒运镜级短片视听工程。

针对当前 AI 生视频领域普遍存在的三大痼疾：
1. **镜头跳跃生硬（突兀跳切）**
2. **时序跳帧与运动卡顿（Stutter）**
3. **近景人物面部扭曲融化（Facial Morphing / Uncanny Valley）**

本项目深度汲取 GitHub 顶级开源框架精髓：
- **HVision-NKU/StoryDiffusion** (NeurIPS 2024 一致性注意力机制)
- **ai-drama-director** (影视分镜视听工业流水线)
- **VideoLingo** (词级时间轴音画对齐标准)

构建了**“光流惯性继承 + 物理遮挡转场 + 面部骨骼解剖锁死 + 多轨全景市井拟音”**的全链路工业级提示词体系。

---

## 🎯 核心技术攻坚与工程黑科技 (Key Breakthroughs)

| 核心痛点 | 传统成因 | 本项目破局方案 (Engineering Solutions) |
| :--- | :--- | :--- |
| **镜头突兀跳切** | 相邻镜头的摄影机运动矢量不连续，视角突变 | **运动惯性继承 + 物理遮挡转场 (Optical Wipe)**：镜头01以穿云下潜并掠过飞檐入街；镜头02以小贩掀蒸笼爆发的浓厚白汽充盈画面作为天然视线遮挡，平滑滑入微距。 |
| **画面卡顿/跳帧** | 时序隐空间缺乏连续物理动量约束 | **连续光流正负锚点**：正向注入 `seamless continuous optical flow, steady smooth trajectory, fluid physical momentum, 60fps cinematic fluidity, zero motion stutter`，负向严格拦截 `stutter, frame freeze, jitter, sudden camera jerk`。 |
| **面部扭曲融化** | 摄影机运动导致面部像素占比剧变，骨骼点丢失 | **面部结构锁死常数 (Facial Rigidity Lock)**：<br>• 正向解剖锚点：`anatomically correct facial features, hyper-realistic facial symmetry, consistent bone structure, natural eye blink, steady gaze`<br>• 负向强力阻断字典：`facial distortion, melted face, warped eyes, asymmetric pupils, shifting facial features, morphing skin, duplicate mouth`。 |
| **声音单薄假人感** | 仅有单一背景音或生硬旁白，缺乏市井空间感 | **多轨时空声场分层**：近景喉音叫卖（带呼吸喘气感）+ 中景孩童嬉笑与路人闲谈 + 远景万人市井嗡鸣与青铜编钟，毫秒级 adelay 混音对齐。 |

---

## 🎬 4 大黄金分镜全景表 (Cinematic Storyboards)

```
[0~8s 镜01: 天穹穿云] ➔ 破云俯冲入街 ➔ [8~16s 镜02: 白汽化灵] ➔ 白汽遮挡转场 
➔ [16~24s 镜03: 金色声浪] ➔ 微距锁脸与音波涟漪 ➔ [24~32s 镜04: 万家灯火] ➔ 升空盘旋双重天
```

### 1. 镜号 01：【天穹穿云 · 极速俯冲】(0~8s)
- **运镜**：90度超高速垂直俯冲推镜 (Breakneck Dive Crane Tracking) ➔ 掠过飞檐贴地拉平。
- **超自然意象**：万丈云海间倒悬着浮空宋代楼阁，晨曦金光撕裂迷雾，朱雀长街如黄金罗盘在地表延展。
- **Muse 正向提示词 (Positive Prompt)**：
  ```text
  Cinematic master shot, continuous fluid downward dive crane tracking shot descending smoothly from celestial golden clouds down to ancient bustling Chang'an capital during Song Dynasty, seamless continuous optical flow, surreal magical realism: floating ancient pavilions and inverted ethereal pagodas suspended weightlessly in golden sunrise mist, camera glides at high speed parting the clouds, swooping millimeters above glowing terracotta tiled rooftops, gently leveling out into crowded street at eye-level, thousands of citizens walking harmoniously, warm morning volumetric sunbeams, 18mm wide anamorphic lens, IMAX scale, breathtaking visual depth, photorealistic architectural details, stable temporal coherence, fluid physical momentum, 8k resolution --ar 16:9 --motion 7
  ```
- **专用负向词 (Negative Prompt)**：
  ```text
  sudden camera jerk, stutter, frame freeze, jitter, modern cars, modern skyscrapers, blurry, 3d video game, cartoon, plastic textures, dull lighting, abrupt cut
  ```
- **音频对应**：天际破空风声 ➔ 晨雾散去瞬间涌入万民市井嗡鸣与空灵编钟。

---

### 2. 镜号 02：【人间烟火 · 白汽化灵】(8~16s)
- **运镜**：贴地超低机位斯坦尼康滑轨 (Low-Angle Steadicam Tracking) ➔ 仰角聚焦蒸笼。
- **超自然意象**：蒸笼掀开瞬间，滚烫浓郁的白汽凝聚幻化为数十条泛着晶莹金光的**飞天锦鲤与白鹤**，长鸣盘旋冲天。
- **Muse 正向提示词 (Positive Prompt)**：
  ```text
  Smooth steadicam tracking shot pushing forward seamlessly through bustling Song Dynasty market street, pedestrians strolling, ornate wooden carts with brass bells, camera gently tilting up towards a steaming giant bamboo dumpling steamer, street vendor wearing linen robe lifting the lid: dense glowing white steam magically coalesces into living luminous golden koi fish and celestial white cranes soaring into the air above the roofs, children reaching out laughing in wonder, glowing light specks drifting gently, surreal Eastern fantasy, steady fluid camera motion, zero motion stutter, rich vibrant silk colors, volumetric lighting, photorealistic textures, 8k --ar 16:9 --motion 6
  ```
- **专用负向词 (Negative Prompt)**：
  ```text
  abrupt jump cut, camera shake, low framerate, stuttering motion, distorted hands, modern clothes, deformed animals, blurry face, plastic, oversaturated
  ```
- **音频对应**：
  - `07.5s` 小贩洪亮叫卖（`zh-CN-YunyangNeural`）：*“刚出屉的热炊饼、水晶蒸饺嘞！皮薄馅大热腾腾——！客官您尝一个！”*
  - `11.0s` 孩童嬉闹奔跑（`zh-CN-XiaoyiNeural`）：*“慢点跑！等等我！快看那白汽变成大金鲤鱼飞上天啦，哈哈！快追呀！”*

---

### 3. 镜号 03：【百态众生 · 金色声浪】(16~24s)
- **运镜**：浅景深微距稳定推进 (Macro Dolly-in Shot) ➔ 85mm f/1.4 肖像锁焦 ➔ 平滑横移至打铁铺与茶肆。
- **超自然意象**：人物叫卖交谈在空气中激发出**肉眼可见的透明金色同心声波涟漪**，震颤万千铜风铃叮咚作响；铁匠重锤砸下，爆出漫天飘零的金色牡丹花雨。
- **Muse 正向提示词 (Positive Prompt)**：
  ```text
  Intimate cinematic portrait dolly-in shot, perfectly stable focal plane, elegant young Song Dynasty woman in pastel hanfu turning head gracefully with authentic smile, flawless anatomically correct facial features, hyper-realistic facial symmetry, consistent bone structure, natural eye blink, steady gaze, lifelike skin texture, 85mm portrait lens with creamy bokeh; seamless continuous pan to rugged blacksmith striking anvil where flying sparks magically blossom into showers of glowing golden peony petals; surreal phenomenon: visible transparent golden acoustic soundwave ripples expanding horizontally through the air from street vendors shouting, vibrating thousands of copper windchimes gently, warm golden hour sunlight, temporally coherent, zero facial morphing, masterpiece lighting, 8k --ar 16:9 --motion 5
  ```
- **专用负向词 (Negative Prompt)**：
  ```text
  facial distortion, melted face, deformed face, bad eyes, asymmetric pupils, shifting facial features, warped jaw, ugly expression, cross-eyed, plastic face, duplicate nose, mutant fingers, jittery motion, stutter, uncanny valley, flicker
  ```
- **音频对应**：
  - `16.5s` 逛街女子闲谈（`zh-CN-XiaoxiaoNeural`）：*“姐姐你瞧，这摊上的蜀锦料子绣得可真水灵！待会儿再去尝尝那樊楼的蜜饯果子好不好？”*
  - `21.5s` 同伴女子欣喜回应（`zh-CN-XiaoxuanNeural`）：*“好呀！听说前头天桥底下还有吐火杂耍呢，咱们快走瞧瞧去！”*
  - 拟音：万千风铃被音波震颤的叮咚回响、铁砧铿锵节奏。

---

### 4. 镜号 04：【星昼交融 · 万家灯火】(24~32s)
- **运镜**：螺旋升天长镜头 (Epic Ascending Orbit) ➔ 盘旋升空俯瞰古城全貌。
- **超自然意象**：苍穹奇绝地一分为二（左侧夕阳熔金炽烈霞光，右侧深邃夜空银河璀璨），千家万户升腾起万盏孔明灯如逆流星雨。
- **Muse 正向提示词 (Positive Prompt)**：
  ```text
  Grand finale continuous ascending orbit shot rising smoothly from bustling street level into the breathtaking twilight sky, uninterrupted camera momentum, surreal cosmic phenomenon: sky divided in two, western sky ablaze in brilliant crimson and gold sunset, eastern sky deep velvet midnight glittering with the Milky Way galaxy, millions of warm glowing paper lanterns ascending gracefully from every courtyard like an inverted river of golden stars, illuminating miles of ancient Song Dynasty palaces, canals, and glowing night markets, ultimate Eastern prosperity and celestial grandeur, steady cinematic elevation, seamless optical flow, Arri Alexa 65 look, 8k resolution --ar 16:9 --motion 6
  ```
- **专用负向词 (Negative Prompt)**：
  ```text
  abrupt jump, stutter, camera drop, jerky motion, low resolution, dark apocalypse, modern electricity, neon glow, blur, noise, artifacts
  ```
- **音频对应**：
  - `24.0s` 茶楼小二迎客（`zh-CN-YunjianNeural`）：*“好嘞！二位客官里边请，上好的明前龙井、二斤热牛肉！”*
  - `26.0s~32.0s` 万人欢庆海啸与古琴大鼓史诗交响推向最高潮。

---

## 📂 仓库目录结构 (Repository Structure)

```
changan-surreal-ai-cinematic/
├── README.md                           # 本项目核心文档与工程解析
├── LICENSE                             # 开源授权协议 (MIT)
├── storyboards/                        # 详细分镜脚本
│   ├── 01_宋代长安城_一镜到底超现实连贯短片_提示词与音效.md
│   ├── 02_宋代长安城_超现实繁华市井_运镜短片分镜.md
│   └── 附赠_亡羊补牢_第一视角写实反转_分镜提示词.md
├── assets/                             # 预合成音频母带
│   ├── 宋代长安城_32秒电影级全景声_连贯原声带.mp3
│   └── 宋代长安城_市井叫卖配音.mp3
├── prompts/                            # 自动化格式提示词
│   └── changan_prompts.json
└── scripts/                            # 工具与音频混音脚本
    └── generate_changan_audio.py
```

---

## 🛠️ 无限画布 (MuseCanvas) 一键合成生产指南

1. **录入提示词**：将 `prompts/changan_prompts.json` 中的 4 段 Prompt 分别粘入 MuseCanvas 文本/生成节点中（画幅建议 `16:9`，时长选 `8 秒`）。
2. **长片无损合成操作（绝不卡顿跳帧的关键）**：
   - 4 个视频节点生成完毕后，按住键盘 **`Shift` 键**，用鼠标拉框同时框选 4 个视频卡片；
   - 在弹出的工具栏或右键菜单中点击 **「创建合成」**；
   - 在新生成的合成卡片上点击 **「导出」**。
   > 💡 **原理提示**：此方式通过底层的流级拼接（Stream Concatenation）执行，无需对画面做破坏性的二次重编码，彻底消除了镜头间的黑屏跳动与降帧卡顿！
3. **音画合成**：直接挂载 `assets/宋代长安城_32秒电影级全景声_连贯原声带.mp3`，秒级匹配，呈现院线级震撼体验。

---

## 📜 许可证 (License)

本项目遵循 [MIT License](LICENSE) 开源。欢迎点亮 Star ⭐ 与二创派生！
