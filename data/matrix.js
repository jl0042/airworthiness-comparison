
(function() {
  const dom = document.getElementById('chart-matrix');
  if (!dom) return;
  const chart = echarts.init(dom);
  const colorMap = {"strict": "#B8584A", "partial": "#C8B99A", "na": "#D4CEC7", "new": "#8A9B90"};
  const labelMap = {
    'strict': '严格要求',
    'partial': '部分 / 宽松',
    'na': '不适用 / 整删',
    'new': '新增',
  };
  const valueColor = {1: colorMap.na, 2: colorMap.partial, 3: colorMap.strict, 4: colorMap.new};
  const tooltips = {"0,0": {"model": "CCAR-23", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "23.2200–2270 完整结构章: 包线 / 载荷 / 强度 / 耐久 / 设计构造"}, "1,0": {"model": "CCAR-25", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "25.301+ 结构, 加 25.571 损伤容限和疲劳评定 (运输类必做)"}, "2,0": {"model": "CCAR-27", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "27.301+ 强度 / 27.547 主旋翼桨毂 / 27.571 疲劳评定"}, "3,0": {"model": "CCAR-29", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "29.301+ + 29.547 关键件 + 29.571 疲劳评定 (运输类更严)"}, "4,0": {"model": "UMR", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "UMR.2200–2270 完整对应 23 编号; 限制载荷系数下调"}, "5,0": {"model": "UPL", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "UPL.2200–2270 同上"}, "6,0": {"model": "AEC", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "AEC.2200–2270 完整结构章 (11 条, V2000CG)"}, "7,0": {"model": "PEU", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "PEU.C000+ 结构 (15 条, EH216-S 复用 UMR/UPL 编号风格但前缀不同)"}, "8,0": {"model": "HY", "dim": "结构强度与限制载荷", "color": "strict", "tooltip": "HY.301–670 结构 + HY.671–780 操纵 (~80 条, 基于 CCAR-25 旧编号)"}, "0,1": {"model": "CCAR-23", "dim": "飞行性能与失速", "color": "strict", "tooltip": "23.2100–2165 失速速度 / 失速警告 / 操稳 / 振动抖振"}, "1,1": {"model": "CCAR-25", "dim": "飞行性能与失速", "color": "strict", "tooltip": "25.103+ 失速速度, 25.251 振动抖振 (运输类全包线)"}, "2,1": {"model": "CCAR-27", "dim": "飞行性能与失速", "color": "strict", "tooltip": "27.49+ 性能 / 27.143 操纵性 / 27.171 稳定性"}, "3,1": {"model": "CCAR-29", "dim": "飞行性能与失速", "color": "strict", "tooltip": "29.51+ A 类性能 / 29.143 操纵 / 29.171 稳定 (运输类更严)"}, "4,1": {"model": "UMR", "dim": "飞行性能与失速", "color": "partial", "tooltip": "UMR.2100–2165: 飞行剖面替失速, 操纵性保留"}, "5,1": {"model": "UPL", "dim": "飞行性能与失速", "color": "partial", "tooltip": "UPL.2100–2165: 最小安全速度替失速, 加 2116 飞行形态转换"}, "6,1": {"model": "AEC", "dim": "飞行性能与失速", "color": "partial", "tooltip": "AEC.2100–2165 飞行性能 (12 条, 跟 UPL 同体系: 最小安全速度)"}, "7,1": {"model": "PEU", "dim": "飞行性能与失速", "color": "partial", "tooltip": "PEU.B000+ 飞行性能 (12 条, 含正常/运行/限制三种飞行包线)"}, "8,1": {"model": "HY", "dim": "飞行性能与失速", "color": "strict", "tooltip": "HY.21–300 性能 / 操稳 / 失速 (33 条, 沿用 CCAR-25 严格度)"}, "0,2": {"model": "CCAR-23", "dim": "设计与构造 / 应急乘员保护", "color": "strict", "tooltip": "23.2315 撤离设施 / 23.2320 乘员环境 / 23.2325 防火"}, "1,2": {"model": "CCAR-25", "dim": "设计与构造 / 应急乘员保护", "color": "strict", "tooltip": "25.803 90秒撤离演示 / 25.851 灭火器 / 25.853 内饰防火"}, "2,2": {"model": "CCAR-27", "dim": "设计与构造 / 应急乘员保护", "color": "strict", "tooltip": "27.561+ 应急着陆 / 27.853 防火"}, "3,2": {"model": "CCAR-29", "dim": "设计与构造 / 应急乘员保护", "color": "strict", "tooltip": "29.803 90秒撤离演示 / 29.807 防火 (运输类加严)"}, "4,2": {"model": "UMR", "dim": "设计与构造 / 应急乘员保护", "color": "na", "tooltip": "无乘员: 撤离 / 物理环境 / 应急出口章节整删; 新增伞降"}, "5,2": {"model": "UPL", "dim": "设计与构造 / 应急乘员保护", "color": "na", "tooltip": "同 UMR; 加鸟撞 / 外挂物 / 外部货物载荷"}, "6,2": {"model": "AEC", "dim": "设计与构造 / 应急乘员保护", "color": "partial", "tooltip": "AEC.2300–2350 设计与构造 (12 条, 不载人不写撤离)"}, "7,2": {"model": "PEU", "dim": "设计与构造 / 应急乘员保护", "color": "partial", "tooltip": "PEU.D000+ 设计构造 + PEU.C070 应急情况 (载人 2 座, 写应急但不要求撤离演示)"}, "8,2": {"model": "HY", "dim": "设计与构造 / 应急乘员保护", "color": "partial", "tooltip": "HY.783+ 设计与构造 (7 条, 试行版简化)"}, "0,3": {"model": "CCAR-23", "dim": "动力装置 / 能源系统", "color": "strict", "tooltip": "23.2400–2440 动力装置基础 + 23.2700–2710 电推进 (3 条)"}, "1,3": {"model": "CCAR-25", "dim": "动力装置 / 能源系统", "color": "strict", "tooltip": "25.901+ 动力装置 + 25.1309 系统冗余 (双 / 三冗余)"}, "2,3": {"model": "CCAR-27", "dim": "动力装置 / 能源系统", "color": "strict", "tooltip": "27.901+ 动力装置 / 27.961 燃油系统"}, "3,3": {"model": "CCAR-29", "dim": "动力装置 / 能源系统", "color": "strict", "tooltip": "29.901+ + 29.1309 系统冗余 (运输类多发要求加严)"}, "4,3": {"model": "UMR", "dim": "动力装置 / 能源系统", "color": "new", "tooltip": "E 章基础保留 + H 章 40 条电动发动机 + I 章 24 条螺旋桨"}, "5,3": {"model": "UPL", "dim": "动力装置 / 能源系统", "color": "new", "tooltip": "同 UMR; 共 60+ 条电推进细则 (台架试验 / 持久演示)"}, "6,3": {"model": "AEC", "dim": "动力装置 / 能源系统", "color": "partial", "tooltip": "AEC.2400–2425 动力装置 (6 条, 全电动); 没单列电动发动机章"}, "7,3": {"model": "PEU", "dim": "动力装置 / 能源系统", "color": "partial", "tooltip": "PEU.E000+ 动力 (8 条, 全电动); 没单列电动发动机章"}, "8,3": {"model": "HY", "dim": "动力装置 / 能源系统", "color": "strict", "tooltip": "HY.901–1300 动力装置 (65 条, 燃油涡轮为主, 跟 CCAR-25 同体系)"}, "0,4": {"model": "CCAR-23", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "23.2500–2560 系统 / HIRF / 电源 / 闪电防护 / 数据记录"}, "1,4": {"model": "CCAR-25", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "25.1309 双三冗余 + EWIS 子节 (运输类必做)"}, "2,4": {"model": "CCAR-27", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "27.1011 飞行仪表 / 27.1317 HIRF"}, "3,4": {"model": "CCAR-29", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "29.1309 系统冗余 + 持续适航文件"}, "4,4": {"model": "UMR", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "F 章基础保留 + 新增 EWIS / 网络安保 / 电子围栏 / DAA"}, "5,4": {"model": "UPL", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "同 UMR"}, "6,4": {"model": "AEC", "dim": "仪表 / 设备 / 网络安保", "color": "partial", "tooltip": "AEC.2500–2525 设备 (6 条, 重点在电源 / 灯光)"}, "7,4": {"model": "PEU", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "PEU.F000+ 设备 (16 条, 载客比 V2000CG 写得更细)"}, "8,4": {"model": "HY", "dim": "仪表 / 设备 / 网络安保", "color": "strict", "tooltip": "HY.1301–1500 设备 (44 条, 沿用 CCAR-25 风格)"}, "0,5": {"model": "CCAR-23", "dim": "营运限制 / 飞行手册", "color": "strict", "tooltip": "23.2600–2625 飞行机组界面 / 仪表标记 / 飞行手册"}, "1,5": {"model": "CCAR-25", "dim": "营运限制 / 飞行手册", "color": "strict", "tooltip": "25.1501+ 营运限制 + 25.1529 持续适航文件"}, "2,5": {"model": "CCAR-27", "dim": "营运限制 / 飞行手册", "color": "strict", "tooltip": "27.1501+ 标记 / 27.1505 飞行手册"}, "3,5": {"model": "CCAR-29", "dim": "营运限制 / 飞行手册", "color": "strict", "tooltip": "29.1501+ 同上 (运输类有详细操作限制)"}, "4,5": {"model": "UMR", "dim": "营运限制 / 飞行手册", "color": "partial", "tooltip": "驾驶舱章节整删, 飞行手册 / 持续适航保留并改写"}, "5,5": {"model": "UPL", "dim": "营运限制 / 飞行手册", "color": "partial", "tooltip": "同 UMR"}, "6,5": {"model": "AEC", "dim": "营运限制 / 飞行手册", "color": "partial", "tooltip": "AEC.2600–2625 使用限制 (6 条)"}, "7,5": {"model": "PEU", "dim": "营运限制 / 飞行手册", "color": "partial", "tooltip": "PEU.G000+ 营运 (6 条)"}, "8,5": {"model": "HY", "dim": "营运限制 / 飞行手册", "color": "strict", "tooltip": "HY.1501–1999 营运 + 飞行手册 (81 条, 最详细的一节)"}, "0,6": {"model": "CCAR-23", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "无对应 (TCAS 是营运指南, 非适航必备)"}, "1,6": {"model": "CCAR-25", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "同上"}, "2,6": {"model": "CCAR-27", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "同上"}, "3,6": {"model": "CCAR-29", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "同上"}, "4,6": {"model": "UMR", "dim": "探测与避撞 DAA + 电子围栏", "color": "new", "tooltip": "UMR.2570 电子围栏 + UMR.2580 探测与避让 (机载必备)"}, "5,6": {"model": "UPL", "dim": "探测与避撞 DAA + 电子围栏", "color": "new", "tooltip": "UPL.2570 / 2580 同上"}, "6,6": {"model": "AEC", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "AEC 没单列 DAA 条款 (V2000CG 走低空隔离空域)"}, "7,6": {"model": "PEU", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "PEU 没单列 DAA (EH216-S 预设航线全自动)"}, "8,6": {"model": "HY", "dim": "探测与避撞 DAA + 电子围栏", "color": "na", "tooltip": "HY 试行版没单列 DAA"}, "0,7": {"model": "CCAR-23", "dim": "C2 指挥控制链路", "color": "na", "tooltip": "无对应 (有人机不需要)"}, "1,7": {"model": "CCAR-25", "dim": "C2 指挥控制链路", "color": "na", "tooltip": "同上"}, "2,7": {"model": "CCAR-27", "dim": "C2 指挥控制链路", "color": "na", "tooltip": "同上"}, "3,7": {"model": "CCAR-29", "dim": "C2 指挥控制链路", "color": "na", "tooltip": "同上"}, "4,7": {"model": "UMR", "dim": "C2 指挥控制链路", "color": "new", "tooltip": "L 章 5 条: 链路性能 / 监控 / 安保 / 持续适航"}, "5,7": {"model": "UPL", "dim": "C2 指挥控制链路", "color": "new", "tooltip": "L 章同 UMR"}, "6,7": {"model": "AEC", "dim": "C2 指挥控制链路", "color": "new", "tooltip": "AEC.2700–2745 数据链路 (10 条, V2000CG 重点)"}, "7,7": {"model": "PEU", "dim": "C2 指挥控制链路", "color": "new", "tooltip": "PEU.H000+ 数据链路 (9 条, 载客的关键)"}, "8,7": {"model": "HY", "dim": "C2 指挥控制链路", "color": "partial", "tooltip": "HY.2000+ 系统安全 (含链路, 16 条) — 没像 UMR/UPL/AEC/PEU 那样独立成章"}, "0,8": {"model": "CCAR-23", "dim": "地面站 / 遥控台", "color": "na", "tooltip": "无对应 (驾驶舱在机内)"}, "1,8": {"model": "CCAR-25", "dim": "地面站 / 遥控台", "color": "na", "tooltip": "同上"}, "2,8": {"model": "CCAR-27", "dim": "地面站 / 遥控台", "color": "na", "tooltip": "同上"}, "3,8": {"model": "CCAR-29", "dim": "地面站 / 遥控台", "color": "na", "tooltip": "同上"}, "4,8": {"model": "UMR", "dim": "地面站 / 遥控台", "color": "new", "tooltip": "R 章 21 条: 机组界面 / 通信 / 电源 / 防火 / 应急撤离 (地面)"}, "5,8": {"model": "UPL", "dim": "地面站 / 遥控台", "color": "new", "tooltip": "R 章同 UMR"}, "6,8": {"model": "AEC", "dim": "地面站 / 遥控台", "color": "new", "tooltip": "AEC.2800+ 地面控制站 (9 条)"}, "7,8": {"model": "PEU", "dim": "地面站 / 遥控台", "color": "new", "tooltip": "PEU.J000+ 地面控制站 (11 条)"}, "8,8": {"model": "HY", "dim": "地面站 / 遥控台", "color": "na", "tooltip": "HY 没有独立地面站章 (大型货运试行版没专门写)"}};
  const models = ["CCAR-23", "CCAR-25", "CCAR-27", "CCAR-29", "UMR", "UPL", "AEC", "PEU", "HY"];
  const dims = ["结构强度与限制载荷", "飞行性能与失速", "设计与构造 / 应急乘员保护", "动力装置 / 能源系统", "仪表 / 设备 / 网络安保", "营运限制 / 飞行手册", "探测与避撞 DAA + 电子围栏", "C2 指挥控制链路", "地面站 / 遥控台"];
  chart.setOption({
    grid: {left: 180, right: 24, top: 60, bottom: 24, containLabel: false},
    tooltip: {
      position: 'top',
      formatter: function(p) {
        const key = p.data[0] + ',' + p.data[1];
        const t = tooltips[key];
        if (!t) return '';
        return `<b>${t.model} × ${t.dim}</b><br>` +
               `<span style="color:${valueColor[p.data[2]]};font-weight:600">● ${labelMap[t.color]}</span><br>` +
               `<span style="font-size:12px;color:#6E6660;display:block;max-width:280px;white-space:normal;line-height:1.6;margin-top:4px">${t.tooltip}</span>`;
      },
      backgroundColor: '#FDFBF8',
      borderColor: '#D4CEC7',
      borderWidth: 1,
      textStyle: {color: '#2A2520', fontSize: 12, fontFamily: 'Noto Serif SC'}
    },
    xAxis: {
      type: 'category',
      data: models,
      position: 'top',
      axisLabel: {
        color: '#2A2520',
        fontSize: 12,
        fontFamily: 'IBM Plex Mono',
        fontWeight: 600,
        letterSpacing: 1,
      },
      axisLine: {show: false},
      axisTick: {show: false},
      splitArea: {show: false}
    },
    yAxis: {
      type: 'category',
      data: dims,
      inverse: true,
      axisLabel: {
        color: '#2A2520',
        fontSize: 13,
        fontFamily: 'Noto Serif SC',
        fontWeight: 400,
        align: 'right',
        margin: 12,
      },
      axisLine: {show: false},
      axisTick: {show: false}
    },
    series: [{
      type: 'heatmap',
      data: [[0, 0, 3], [1, 0, 3], [2, 0, 3], [3, 0, 3], [4, 0, 3], [5, 0, 3], [6, 0, 3], [7, 0, 3], [8, 0, 3], [0, 1, 3], [1, 1, 3], [2, 1, 3], [3, 1, 3], [4, 1, 2], [5, 1, 2], [6, 1, 2], [7, 1, 2], [8, 1, 3], [0, 2, 3], [1, 2, 3], [2, 2, 3], [3, 2, 3], [4, 2, 1], [5, 2, 1], [6, 2, 2], [7, 2, 2], [8, 2, 2], [0, 3, 3], [1, 3, 3], [2, 3, 3], [3, 3, 3], [4, 3, 4], [5, 3, 4], [6, 3, 2], [7, 3, 2], [8, 3, 3], [0, 4, 3], [1, 4, 3], [2, 4, 3], [3, 4, 3], [4, 4, 3], [5, 4, 3], [6, 4, 2], [7, 4, 3], [8, 4, 3], [0, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 2], [5, 5, 2], [6, 5, 2], [7, 5, 2], [8, 5, 3], [0, 6, 1], [1, 6, 1], [2, 6, 1], [3, 6, 1], [4, 6, 4], [5, 6, 4], [6, 6, 1], [7, 6, 1], [8, 6, 1], [0, 7, 1], [1, 7, 1], [2, 7, 1], [3, 7, 1], [4, 7, 4], [5, 7, 4], [6, 7, 4], [7, 7, 4], [8, 7, 2], [0, 8, 1], [1, 8, 1], [2, 8, 1], [3, 8, 1], [4, 8, 4], [5, 8, 4], [6, 8, 4], [7, 8, 4], [8, 8, 1]],
      label: {
        show: true,
        color: '#FDFBF8',
        fontSize: 10,
        fontFamily: 'IBM Plex Mono',
        formatter: function(p) {
          const key = p.data[0] + ',' + p.data[1];
          const t = tooltips[key];
          return labelMap[t.color];
        }
      },
      itemStyle: {
        borderColor: '#FDFBF8',
        borderWidth: 2,
        color: function(p) { return valueColor[p.data[2]] || colorMap.na; }
      },
      emphasis: {
        itemStyle: { borderColor: '#2A2520', borderWidth: 2 }
      }
    }]
  });
  window.addEventListener('resize', () => chart.resize());
})();
