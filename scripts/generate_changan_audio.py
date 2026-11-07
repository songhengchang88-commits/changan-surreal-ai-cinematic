import asyncio
import os
import subprocess
import edge_tts

ASSETS_DIR = r"G:\无限创造\assets"
TEMP_DIR = os.path.join(ASSETS_DIR, "temp_voices")
os.makedirs(TEMP_DIR, exist_ok=True)
FFMPEG = r"E:\MuseCanvas\tools\ffmpeg.exe"

VOICE_CONFIGS = [
    # 1. 小贩叫卖 (响亮、热情)
    {
        "text": "刚出屉的热炊饼、水晶蒸饺嘞！皮薄馅大热腾腾——！客官您尝一个！",
        "voice": "zh-CN-YunyangNeural",
        "rate": "+5%",
        "pitch": "+0Hz",
        "filename": "peddler.mp3",
        "delay_ms": 7500 # 7.5s 处小贩掀蒸笼
    },
    # 2. 孩童嬉戏欢笑 (天真、清脆)
    {
        "text": "慢点跑！等等我！快看那白汽变成大金鲤鱼飞上天啦，哈哈！快追呀！",
        "voice": "zh-CN-XiaoyiNeural",
        "rate": "+12%",
        "pitch": "+5Hz",
        "filename": "children.mp3",
        "delay_ms": 11000 # 11s 处孩童追逐欢闹
    },
    # 3. 逛街女子闲谈A (温婉、灵动)
    {
        "text": "姐姐你瞧，这摊上的蜀锦料子绣得可真水灵！待会儿再去尝尝那樊楼的蜜饯果子好不好？",
        "voice": "zh-CN-XiaoxiaoNeural",
        "rate": "+3%",
        "pitch": "+2Hz",
        "filename": "girl_a.mp3",
        "delay_ms": 16500 # 16.5s 处人物特写与市井闲谈
    },
    # 4. 逛街女子回应B (娇俏、欣喜)
    {
        "text": "好呀！听说前头天桥底下还有吐火杂耍呢，咱们快走瞧瞧去！",
        "voice": "zh-CN-XiaoxuanNeural",
        "rate": "+5%",
        "pitch": "+3Hz",
        "filename": "girl_b.mp3",
        "delay_ms": 21500 # 21.5s 处回应
    },
    # 5. 茶楼伙计迎客 (中气十足)
    {
        "text": "好嘞！二位客官里边请，上好的明前龙井、二斤热牛肉！",
        "voice": "zh-CN-YunjianNeural",
        "rate": "+5%",
        "pitch": "-2Hz",
        "filename": "waiter.mp3",
        "delay_ms": 24000 # 24s 处茶肆呼应
    }
]

async def generate_all_voices():
    print("开始生成多角色拟真语音...")
    tasks = []
    for cfg in VOICE_CONFIGS:
        out_path = os.path.join(TEMP_DIR, cfg["filename"])
        communicate = edge_tts.Communicate(
            text=cfg["text"],
            voice=cfg["voice"],
            rate=cfg["rate"],
            pitch=cfg["pitch"]
        )
        tasks.append(communicate.save(out_path))
    await asyncio.gather(*tasks)
    print("所有角色语音生成完毕！")

def mix_into_master():
    print("使用 FFmpeg 进行精确毫秒级多轨时间轴混音...")
    output_master = os.path.join(ASSETS_DIR, "宋代长安城_32秒电影级全景声_连贯原声带.mp3")
    
    # 构造 ffmpeg 混音滤镜链
    inputs = []
    delays = []
    for i, cfg in enumerate(VOICE_CONFIGS):
        inputs.extend(["-i", os.path.join(TEMP_DIR, cfg["filename"])])
        delays.append(f"[{i}:a]adelay={cfg['delay_ms']}|{cfg['delay_ms']}[a{i}]")
    
    # 连接所有轨道并混音
    in_tags = "".join(f"[a{i}]" for i in range(len(VOICE_CONFIGS)))
    filter_complex = f"{';'.join(delays)};{in_tags}amix=inputs={len(VOICE_CONFIGS)}:dropout_transition=2:normalize=0[mixed]"
    
    cmd = [
        FFMPEG, "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[mixed]",
        "-c:a", "libmp3lame",
        "-b:a", "256k",
        output_master
    ]
    
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0:
        print(f"全景声主音轨成功生成: {output_master}")
    else:
        print(f"混音失败: {res.stderr.decode('utf-8', errors='ignore')}")

if __name__ == "__main__":
    asyncio.run(generate_all_voices())
    mix_into_master()
