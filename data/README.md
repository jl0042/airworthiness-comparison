# 数据档案 (data/)

本目录存放 `index.html` 中所有图表使用的原始数据 + 方法论文档。每个 CSV 对应若干图表, 字段都有 `source_url` 列, 方便逐项核对。

---

## 文件清单

### Section 1 — 地理与经济

| 文件 | 内容 | 行数 |
|---|---|---|
| `s1_cn_provinces.csv` | 中国 31 省 (含港澳台): 人口密度 / 人均 GDP / 民用机场 / 面积 / 2024 人口, 各省统计局 2024 公报 | 33 |
| `s1_us_states.csv` | 美国 50 州 + DC: 人均 GDP / 人口 / FAA NPIAS 机场细分 (Primary/Nonprimary/Reliever/GA) | 51 |
| `s1_cn_cities.csv` | 中国 Top 35 城市 GDP + 经纬度 (累计覆盖全国 GDP ~60%), 各市统计局 2024 公报 | 35 |
| `s1_us_metros.csv` | 美国 Top 35 MSA GDP + 经纬度 (累计覆盖 ~65%), BEA Real GDP by Metropolitan Area 2023 | 35 |
| `s1_cargo_hubs.csv` | 中国 10 大 + 美国 10 大货运机场: 坐标 + cargo 量 + 排名, ACI 2024 + 公司年报 | 22 |
| `s1_airport_counts.csv` | 机场口径方法论: CAAC vs FAA NPIAS vs FAA 全部 (含私用) 三个口径数字 + 解释 | — |

### Section 2 — 基础设施差距

| 文件 | 内容 | 行数 |
|---|---|---|
| `s2_freight_modes.csv` | 中美 2024 货运分模式 (公路/铁路/水运/民航/管道) 中国 MOT 公报直接给出, 美国 ATA+AAR+USACE 综合 | 14 |
| `s2_air_cargo.csv` | 民航货运三种口径 (国内运输量 / 总运输量 / 机场吞吐量) 中美对比 + Top 10 机场 + 估算来源 | 15 |
| `s2_express_parcels.csv` | 中美 2024 快递包裹: 中国国家邮政局 1750.8 亿件 (含同城/异地/国际拆分); 美国 ShipMatrix 238 亿件 (按 USPS/Amazon/UPS/FedEx 拆分) | 9 |
| `s2_logistics_cost.csv` | 中美 2024 物流成本: CFLP 19.0 万亿 / 14.1% vs CSCMP $2.58T / 8.8% + 子项拆分 (运输/库存/管理) | 14 |
| `s2_aircraft_fleet.csv` | 中美飞机 + 机场数: CAAC 4394 运输机 / 3232 通航 + FAA NPIAS 3287 + GA Survey 204K | 14 |
| `s2_highway_distribution.csv` | 中国高速公路 19.07 万 km 东/中/西部分布 + 4 大省细节 | 8 |
| `s2_comparison_analysis.md` | S2 完整对比分析 + 6 项交叉验证 + 修正前后对比 + 数据局限 | (markdown) |

### Section 3 — 第一性原理需求分析

| 文件 | 内容 | 行数 |
|---|---|---|
| `s3_west_china_geo.csv` | 中国西部 12 省 (含 4 红 + 4 边缘红色) 面积 / 人口 / 公路里程 / 公路密度 / 通航机场 / 铁路 + 西部合计 + 全国对比, 各省 2024 公报 | 16 |
| `s3_alaska_bypass.csv` | 阿拉斯加 Bypass Mail 完整事实清单: 起源 1972 / Rural Service Improvement Act 2002 / 1000 lb 最低 / FY2010-FY2024 补贴 / 苏打水托盘 $485 / Bethel 薯片例 / 主要承运人 / 货物类型 + 阿拉斯加 FAA 注册 761 起降设施 / 82% 社区无路 | 22 |
| `s3_comparison_analysis.md` | S3 完整 review: 17 项数据修正前后对比 + 西部 12 省 verified 表 + 阿拉斯加面粉故事完整版 + radar 删除理由 + 红色省份名单论证 + 400-600 架估算下调论证 | (markdown) |

### Section 4 — 高铁货运竞争分析

| 文件 | 内容 | 行数 |
|---|---|---|
| `s4_hsr_freight.csv` | 高铁货运 + 阿拉斯加机场 + Caravan 速度 verified 数据: 全国 4.8 万 km 高铁 / 高铁快运覆盖 252 站 + 高铁急送 196 城 / 350 km/h 复兴号货运动车组 (CR200JS-G 张冠李戴 修正) / 中铁急送实际分档定价 150-340 元/件 / 各省 250+ km/h 高铁覆盖 (西藏唯一无) / Cessna 208 Caravan 巡航 175 KTAS = 324 km/h | 26 |
| `s4_comparison_analysis.md` | S4 完整 review: 20 项修正前后对比 + 高铁货运动车组车型澄清 + 中铁快运实际定价 verified + 各省高铁覆盖修正 (6 省错→1 省) + chart-tonkm 速度修正 + S2/S6/S7 连带引用清单 | (markdown) |

### Section 5 — 机队与枢纽

| 文件 | 内容 | 行数 |
|---|---|---|
| `s5_hubs_cn.csv` | CAAC 2024 全国十大货运机场 + 错位的昆明/厦门 (实际第 12/14): 上海浦东 377.83 / 鄂州花湖 86.52 (航空货邮口径, 同比 +253%) / 重庆江北 46.95 (原网页缺) / 上海虹桥 42.77 (原网页缺) | 12 |
| `s5_hubs_us.csv` | ACI-NA 2024 北美十大货运机场 metric tonnes: MEM 375.4 / ANC 369.9 / SDF 315.3 / JFK 155.9 (原 168 short ton 换算错) / IND 90.8 (原 110 错) / ONT 74.3 (替代原 DFW, 不在 ACI-NA top10) | 10 |
| `s5_fleet_cn.csv` | CAAC 2024 通航 3,232 架 (含教学训练 1,252, 公报直接公开) + 8 类明细 (AOPA 推算, CAAC 公报未公开) + Cessna 208 ~30 架 | 13 |
| `s5_fleet_us.csv` | FAA GA Survey CY2023 (最新可得): 总 214,222 架 / 单发活塞 128,000 (60%) / 涡桨 11,000 / 公务机 16,000 / 实验机 33,000 / Part 135 支线货运涡桨 ~1,000 架 | 10 |
| `s5_cargo_airlines_cn.csv` | 中国 7 家货运航司机队 2024 年底 + 2025 最新: 顺丰 88→90 / 中邮 35→37 / 圆通 13→14 / 三家合计 136 / 全产业约 200 架 | 9 |
| `s5_feeder_us.csv` | 美国支线接驳生态: Ameriflight 125 / Empire 54 / Mountain Air Cargo 35 / Baron / CSA / Everts; FedEx 合同租赁 317 架 (231 Cessna 208B + 28 Cessna 408 SkyCourier + 58 ATR 42/72F); 全 Part 135 货运涡桨 ~480 架; 典型航线 MEM/ANC/EWR | 13 |
| `s5_fleet_by_payload_cn.csv` | 中国全货机机队按载荷分层 (2025 年初): ≤1t/1-3t/3-8t 全部空白; 8-10t 层仅 2 架 C909F (圆通 2024/6 首次商业货运); 18-21t 737-300/400F ~31 架; 23t 737-800BCF ~46 架; 28-39t 757-200F ~55 架; 55-60t 767-300BCF ~25 架; 80+t 747-400F/777F ~25 架 | 9 |
| `s5_fleet_by_payload_us.csv` | 美国全货机机队按载荷分层 (2024) 用于中美对比: ≤1t ~280 (FedEx Feeder 主力); 1-3t ~80 (Beech 1900 / Metroliner); 3-8t ~100 (ATR 42/72F / Cessna 408 / Saab 340F); 18-23t ~40 (Amazon 737-800BCF); 28-39t ~200 (757F FedEx+UPS); 55-60t ~310 (767F FedEx+UPS+Amazon); 60-100t ~130 (A300/A330F); 80+t ~235 (747/777/MD-11F). 合计 ~1,475 架 (中国 7 倍) | 10 |
| `s5_comparison_analysis.md` | S5 完整 review: 鄂州 245/102/86.5 三个数字口径澄清 + sec-title/sec-sub/thesis 三件套重写 (干线 hub 追上来/专用 hub 差代际/通航段空白) + 单发活塞 45%→60% 修正 + "涡桨跑物流"同口径改写 + chart scale 统一 400 | (markdown) |

### Section 6 — 成本算法 (拆解原理 + 计算器)

| 文件 | 内容 | 行数 |
|---|---|---|
| `s6_comparison_analysis.md` | S6 完整 review: Caravan 227→324 km/h 派生连带 (800km 例子 18,300→13,020; 和田-乌鲁木齐 4.8hr→3.9hr); thesis 改成本结构拆分 (Caravan vs ATR 七项占比对比); 737/757/Y-12F 来源标签错配修正; varHr/fix/cycle/PR 全翻; S7 line 1174 HH-200 速度比较修正 (+41% 错, 实际相当) + JS BE_SPEED 227→324; S5 载荷分层表新增 + C909F 段 | (markdown) |

注: S6 主表已扩充并搬至 S7a, 详见 `s7_aircraft_cost_master.csv`。

### Section 7a — 机型成本主表 + 不亏价矩阵

| 文件 | 内容 | 行数 |
|---|---|---|
| `s7_aircraft_cost_master.csv` | 11 机型成本主表 (扩充版): TP500 / Caravan UAV 首批 / Caravan 有人 / HH-200 首批 / Y-12F / CY-8 首批 / W5000 首批 / ATR42 中国首批 / C909F / 737-800BCF / 757-200F. 每行 22 列: 业载/速度/航程/MTOW + 7 项小时变动成本 (燃油/发动机+桨/机体维护/保险/人员/数据链/折旧) + 4 项起降费 (降落/装卸/停机/导航) + 吨公里成本 + 厂商公开值 + 差距解释。取证中机型 (TP500/HH-200/CY-8/W5000) 全部用首批运营估算 (×1.3-2 修正系数, 行业先例: 787/A350/ARJ21 早期入役成本) | 12 |
| `s7_breakeven_matrix.csv` | 11 机型 × 5 距离档 (500/1000/1500/2500/4000 km) 不亏价矩阵: 装载率 70% + 地面取派 4 元/kg 中位; 灰格 = 航程不够 | 12 |

### 辅助文件

| 文件 | 内容 |
|---|---|
| `ARP-NPIAS-2025-2029-AppendixA.xlsx` | FAA NPIAS 2025-2029 原始 Excel (从 FAA 官网下载, 用于 S1/S2 美国机场数据) |

---

## 数据约定

### 编码
- 所有 CSV 用 **UTF-8 BOM** 编码 (`utf-8-sig` in Python), 保证 Excel 打开不乱码

### 通用字段 (S2 引入的标准模式)
按 `source_url` 列标注每行数据的官方来源 URL。多数 CSV 含以下字段:

| 字段 | 含义 | 示例 |
|---|---|---|
| `value` 或具体名 | 数据值 | `418.80` |
| `unit` | 单位 (中文) | `亿吨`, `万吨`, `亿元`, `亿件` |
| `year` | 数据年份 | `2024` |
| `source_org` | 数据原始机构 | `交通运输部`, `CAAC`, `BEA`, `ATA` |
| `source_doc` | 具体公报/报告名 | `2024 年交通运输行业发展统计公报` |
| `source_url` | 直接 URL | `https://...` |
| `status` | 数据可信度 | `verified` / `partial` / `unverified` / `needs_update` |
| `notes` | 备注 (口径、同比、估算逻辑等) | `同比 +3.8%; 营业性公路货运量` |

### `status` 含义
- `verified` ✅ — 直接从官方原始文档 (公报、年报、统计页) 抓取或核对过
- `partial` ⚠️ — 部分核对, 主要数字 verified 但子项是基于占比反推
- `unverified` 🟡 — 估算或综合多源, 有 ±10-30% 误差
- `needs_update` 🟠 — 已知数据陈旧, 待找新源

### 单位约定
- **中国**: 亿吨, 万吨, 亿元 (人民币), 亿件, 万亿
- **美国**: short tons (短吨, 1 short ton = 0.907 公吨), $billion, $trillion
- **国际可比**: 公制吨 (metric tons / tonnes), 美元
- 跨国对比时需要转换: short ton × 0.907 → 公吨; $ × 汇率 (2024 年均 7.20) → 元

---

## 数据源优先级

按 [MEMORY.md](../../../.claude/projects/.../memory/MEMORY.md) 的 `data_source_convention` 规范:

1. **官方网站** (政府/监管机构: NBS / MOT / CAAC / 国家邮政局 / FAA / BTS / BEA / Census)
2. **行业协会** (有方法论披露: ATA / AAR / USACE / CSCMP / IATA / ACI)
3. **Wikipedia** (引用原始源, 适合作为索引)
4. **行业研报/媒体** (FreightWaves, Supply Chain Dive, Logistics Mgmt — 注明)
5. **公司年报** (USPS/UPS/FedEx/Amazon 10-K — 注明财年)

**禁用** ❌: 微信公众号、百家号、知乎、抖音、CSDN 博客、个人博客 (除非引用原始源)

---

## 交叉验证方法

跨国对比时, 即使两国统计口径不同 (中国营业性发送量 vs 美国 BTS Freight Facts), 至少要做以下几种验证:

1. **占比结构相似度**: 公路/铁路/水运/航空/管道占比是否合理 (例: 中美公路+铁路占比都 ~83%)
2. **人均量验证**: 两国人均货运、人均快递是否在同数量级 (例: 人均货运中美都 ~40 公吨/人)
3. **不同口径自洽**: 同一国不同口径数字之间比例是否合理 (例: 中国机场吞吐量 / 航空公司运输量 = 2.23 ≈ 平均每票货过 2 个机场)
4. **时间序列**: 同一指标历年趋势是否合理 (例: 美国 2020 BTS 25.1B lbs → 2021 boom → 2023 -10% → 2024 略复苏)
5. **绝对值汇率换算**: 货币类指标按汇率换算后是否相当 (例: CSCMP $2.58T × 7.20 = 18.6 万亿元 ≈ CFLP 19.0 万亿)
6. **国际机构交叉**: ICAO / IATA / OECD / World Bank 同主题数据是否对得上

具体执行见 [`s2_comparison_analysis.md`](./s2_comparison_analysis.md) 的 6 项验证示例。

---

## 工作流 (每个 section)

每节 review 时按这个流程:

1. **用户提出 challenge** (例: "为什么中国民航 2006 万吨?")
2. **Claude 找官方源** (按数据源优先级)
3. **Claude 做交叉验证** (口径相似度 / 人均 / 时间序列等)
4. **Claude 写入 / 更新 CSV** (含 `source_url` + `status`)
5. **Claude 同步更新 `index.html`** (chart 数据 + chart-desc + source 行 + insight 文本)
6. **Claude 检查其他 section 是否引用旧数据** (grep 关键词)
7. **Claude commit + push**

---

## 已知数据局限

记录在 CSV 中 `status=unverified` 或 `partial` 的项目, 主要是:

### 美国分模式精确公制吨
- BTS Freight Facts and Figures 公开页面访问受限 (.gov 域 fetch 403)
- 当前美国货运分模式数字基于 ATA 11.27B short tons + AAR 占比 10.6% + USACE/EIA 估算反推
- 误差 ±10%

### 美国国内 air cargo 2024
- BTS T-100 segment data 公开摘要不可访问
- 估算基于 BTS 2020 baseline (25.1B lbs = 1140 万吨) + Statista FedEx/UPS 2021 ton-miles + 2023 -10% + 2024 略复苏
- 估算 ~1,250 万吨 (range 1,100-1,400)
- 误差 ±20%

### 美国管道运输量
- EIA 提供 capacity (Bcf/day) 不直接给 tons/year
- 当前 ~30 亿公吨是 FAF 5.7 历史推算

### 中国管道运输量
- MOT 营业性公报不含管道
- 国家能源局给主干网络 10 万 km 但不给年运输量
- 网页处理: 中国直接不显示管道项

---

## 编辑者注意

如果 `index.html` 里改了数字, **必须同步**:
1. 该数字对应的 CSV 行 (`value` + `notes` 注明改动原因)
2. 该图表的 `<div class="source">` 行 (按规范)
3. 检查其他 section 是否也引用 (grep 旧值)

不要在 CSV 里写"我改成什么了"这种内部沟通, 只写客观数据 + 来源 + 现状。

写作风格规范见: [`MEMORY.md`](../../../.claude/projects/.../memory/MEMORY.md)
