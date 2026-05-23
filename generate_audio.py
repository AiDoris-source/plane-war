#!/usr/bin/env python3
"""批量生成游戏庆祝语音 (edge-tts 高质量版)"""
import asyncio, os
from edge_tts import Communicate

AUDIO_DIR = "/Users/a1234/WorkBuddy/2026-05-16-task-11/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# 24条庆祝语 + 对应音色
CELEBRATIONS = [
    # 周泽森专属（活泼女声 XiaoXiao）
    ("zh-CN-XiaoxiaoNeural", "周泽森，你真棒！继续加油！", "01_zesen_1.mp3"),
    ("zh-CN-XiaoxiaoNeural", "周泽森，太牛了！无人能挡！", "02_zesen_2.mp3"),
    ("zh-CN-XiaoxiaoNeural", "周泽森，你就是天才！", "03_zesen_3.mp3"),
    # 戴周翰专属（阳刚男声 Yunxi）
    ("zh-CN-YunxiNeural", "戴周翰，宇宙最强！所向披靡！", "04_zhouhan_1.mp3"),
    ("zh-CN-YunxiNeural", "戴周翰出击，敌人全部逃跑！", "05_zhouhan_2.mp3"),
    ("zh-CN-YunxiNeural", "戴周翰大魔王驾到！颤抖吧！", "06_zhouhan_3.mp3"),
    ("zh-CN-YunxiNeural", "戴周翰来了，全屏清空！无敌！", "07_zhouhan_4.mp3"),
    # 戴雨晗专属（甜美女声 Xiaoyi）
    ("zh-CN-XiaoyiNeural", "戴雨晗，神机妙算！太厉害了！", "08_yuhan_1.mp3"),
    ("zh-CN-XiaoyiNeural", "戴雨晗出马，一个顶俩！", "09_yuhan_2.mp3"),
    ("zh-CN-XiaoyiNeural", "戴雨晗闪亮登场！全场欢呼！", "10_yuhan_3.mp3"),
    ("zh-CN-XiaoyiNeural", "戴雨晗无敌美少女战士！", "11_yuhan_4.mp3"),
    # 通用中文（活泼）
    ("zh-CN-XiaoxiaoNeural", "太酷啦！雷霆出击！火力全开！", "12_generic_1.mp3"),
    ("zh-CN-XiaoxiaoNeural", "完美通关！你是无敌战神！", "13_generic_2.mp3"),
    ("zh-CN-XiaoxiaoNeural", "哇！太厉害了！再来一次！", "14_generic_3.mp3"),
    ("zh-CN-YunxiNeural", "王牌飞行员！星际霸主！势不可挡！", "15_generic_4.mp3"),
    # 英文祝福（活力男声 Guy）
    ("en-US-GuyNeural", "Unstoppable! You are the champion!", "16_english_1.mp3"),
    ("en-US-GuyNeural", "No one can stop you! Legendary!", "17_english_2.mp3"),
    ("en-US-GuyNeural", "Absolute domination! Godlike!", "18_english_3.mp3"),
    ("en-US-JennyNeural", "Mission accomplished, hero! You rock!", "19_english_4.mp3"),
    ("en-US-JennyNeural", "Too easy! Too strong! Amazing!", "20_english_5.mp3"),
    # 更多中文（调皮搞怪风格）
    ("zh-CN-YunjianNeural", "嘿嘿，这波操作太骚了！", "21_fun_1.mp3"),
    ("zh-CN-YunjianNeural", "厉害厉害，五体投地！", "22_fun_2.mp3"),
    ("zh-CN-XiaoxiaoNeural", "太强了吧！敌人已经吓跑了！", "23_fun_3.mp3"),
    ("zh-CN-YunxiNeural", "绝杀！完美收官！再来一局！", "24_fun_4.mp3"),
]

async def generate_one(voice, text, filename):
    out = os.path.join(AUDIO_DIR, filename)
    if os.path.exists(out):
        print(f"⏭️  已存在: {filename}")
        return
    try:
        comm = Communicate(text, voice)
        await comm.save(out)
        size = os.path.getsize(out)
        print(f"✅ {filename} ({size//1024}KB)")
    except Exception as e:
        print(f"❌ 失败: {filename} → {e}")

async def main():
    tasks = [generate_one(v, t, f) for v, t, f in CELEBRATIONS]
    await asyncio.gather(*tasks)
    print("\n🎉 全部完成！")

asyncio.run(main())
