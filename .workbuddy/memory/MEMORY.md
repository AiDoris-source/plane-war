# MEMORY.md - 长期记忆

## 项目记录

### 飞机大战游戏 (2026-05-16)
- 单文件 HTML5 Canvas 飞机大战游戏
- 路径：`/Users/a1234/WorkBuddy/2026-05-16-task-11/plane-war.html`
- 技术栈：纯原生 JS + Canvas，无外部依赖
- V1功能：3种敌机、道具系统、粒子爆炸、视差星空、霓虹UI
- V2升级：Web Audio API合成10种音效、Boss闯关系统(30秒一关+Boss战+追踪弹+激光+狂暴模式)
- V3升级：4种新敌机(zigzag/bomber/stealth/formation)+导弹技能+Boss解锁挂载武器(侧翼炮/等离子炮/EMP)
- V3.1重构：导弹改自动随弹发射(删X键)+5级子弹升级系统(power道具永久升级)+doubleFire改临时+1级
- V3.2升级：算术挑战(10以内加减法+Web Speech API语音)+3种难度模式(简单/正常/挑战)+localStorage持久化
- V3.3升级：答题修复(答错可重新输入)+5种新敌机(Boss击败解锁:splitter/charger/shielder/swarm/elite)+激励语音+虚拟数字键盘
- V3.4升级：去掉激励语音(音质差)+答题3次错误=Game Over(显示"很遗憾，游戏结束")+庆祝语音改"周泽森太棒了，继续加油"+高质量TTS(Google/Microsoft语音优先)+难度选择改大按钮可点击
- V3.5修复：庆祝语音改用百度在线TTS(new Audio()+tts.baidu.com)+Web Speech API双通道+需HTTP服务器访问(http://localhost:8080)+Boss击败展示页延长(120→240帧)
- V3.6升级：8种随机庆祝语音(celebrationMessages数组)+战机变形升级(每3Boss触发，transformLevel，Player.draw()3级视觉特效：L1蓝光环/L2金翼/L3电弧)+答题范围扩展至20以内加减法
- V3.7优化：变形时机从Boss击败时→答题正确后触发(STATE.TRANSFORM专用3秒3阶段动画)+音效修复(iframe AudioContext resume+首次交互解锁)+TTS增加有道备用+庆祝文字气泡
- V3.7.1修复：庆祝语音优先级改为Web Speech API优先(在线TTS降为备用)+合成庆祝音增强(上升音阶+胜利和弦+闪光音效)+庆祝气泡延长至150帧
- 部署：GitHub Pages 线上地址 https://aidoris-source.github.io/plane-war/
- 仓库：https://github.com/AiDoris-source/plane-war (GitHub用户名: AiDoris-source)
- 分支策略：`main`分支=线上封存版(GitHub Pages读取)，`dev`分支=后续升级开发，v3.7 tag已打
- 局域网访问：`python3 -m http.server 8080 --bind 0.0.0.0`，iPad访问 http://192.168.1.16:8080/plane-war.html
- 已通过QA验证（V1: P0触屏+10秒崩溃; V2: P0 Boss触发+P1帧计数+激光冷却; V3: P1 onBossDefeated+P2关卡清理+P3 Boss.id; V3.1: 0 P0/P1）
- 关键模式：帧计数器(pendingAttacks)替代setTimeout、hasHit碰撞冷却、stageTimer控制敌机生成、enemyIdCounter统一ID、bossesDefeated解锁新敌机
