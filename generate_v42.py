#!/usr/bin/env python3
"""V4.2 新增音频生成 — edge-tts 高质量版"""
import asyncio, os
from edge_tts import Communicate

AUDIO_DIR = "/Users/a1234/WorkBuddy/2026-05-16-task-11/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# 新增音频列表：(音色, 文字, 文件名)
NEW_AUDIO = [
    # ★ 庆祝/互动语音（10条）
    ("zh-CN-YunxiNeural",   "戴周翰，牛到讲方言！太厉害了！",         "25_zhouhan_dialect.mp3"),
    ("zh-CN-XiaoyiNeural",   "戴雨晗，猴赛雷！你是最棒的！",           "26_yuhan_hesile.mp3"),
    ("en-US-JennyNeural",    "Come on! Let's go!",                     "27_come_on.mp3"),
    ("zh-CN-XiaoxiaoNeural", "一起加油！我们是最强的！",              "28_together_fight.mp3"),
    ("zh-CN-YunjianNeural",  "再接再厉，勇往掉队！不对不对，是勇往直前！", "29_keep_going.mp3"),
    ("zh-CN-YunjianNeural",  "哎呀，战机没油了！快去吃道具！",        "30_no_fuel.mp3"),
    ("zh-CN-YunxiNeural",    "火箭弹来啦！发射！轰！",                "31_rocket_coming.mp3"),
    ("zh-CN-YunxiNeural",    "霹雳战车解锁！地面部队加入战场！",     "32_tank_unlocked.mp3"),
    ("zh-CN-XiaoxiaoNeural",  "周泽森，来个空翻炸弹怎么样？",          "33_zesen_flip_bomb.mp3"),
    # ★ 雷霆战机激活语音
    ("zh-CN-XiaoxiaoNeural", "雷霆战机激活！满屏战机闪烁！",           "34_thunder_activated.mp3"),
    # ★ 随机被击中音效（5条）
    ("zh-CN-YunjianNeural",  "哎哟，被揍了！",                         "hit_01_aiyo.mp3"),
    ("zh-CN-YunxiNeural",    "啊！你居然打到我了！",                   "hit_02_how_dare_you.mp3"),
    ("zh-CN-YunjianNeural",  "好痛！等我报仇！",                       "hit_03_seek_revenge.mp3"),
    ("zh-CN-YunxiNeural",    "呼叫支援！有人偷袭！",                   "hit_04_call_backup.mp3"),
    ("zh-CN-YunxiNeural",    "启动毁灭装置！玉石俱焚！",              "hit_05_destruction.mp3"),
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
    tasks = [generate_one(v, t, f) for v, t, f in NEW_AUDIO]
    await asyncio.gather(*tasks)
    print(f"\n🎉 V4.2 新增音频完成！共 {len(NEW_AUDIO)} 条")

asyncio.run(main())
