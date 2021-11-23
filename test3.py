import discord
import asyncio
import random

client = discord.Client()

token = "ODc1MDY3Njg5MzE0NDM1MDgz.YRQISw.oFK4YQWRVmiuVCbY5FS42tfamho"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('온새미로')
    await client.change_presence(status=discord.Status.onlien, activity=game)

@client.event
async def on_message(message):
    if message.content == ("핑크"):
        await message.channel.send("군침이 싹도노")

    if message.content == ("별난바"):
        await message.channel.send("참마 언니 내가 많이 사랑해💋")

    if message.content == ("바밤바"):
        await message.channel.send("돼지꿀꿀입냄새괴물🐷")

    if message.content == ("누가바"):
        await message.channel.send("누가바 누가바 해태 누가바!👀")

    if message.content == ("쌍쌍바"):
        await message.channel.send("달이 참… 밝죠…?🌙")

    if message.content == ("캔디바"):
        await message.channel.send("노래 좀 그만 불러🎤")

    if message.content == ("보석바"):
        await message.channel.send("도둑이 훔쳐 감 ㅅㄱ👤")

    if message.content == ("와삭바"):
        await message.channel.send("똥침시비충👆")
          
    if message.content == ("명란마요"):
        await message.channel.send("급발진 멈춰!🖐️⛔")

    if message.content == ("하지마요"):
        await message.channel.send("희귀캐✨")

    if message.content == ("울지마요"):
        await message.channel.send("헝헝헝ㅇ..흡끄륵ㄱ끅끅ㄱ끄엉엉..흡끄윽..끄헝헝..흐우앙흡끅끆ㄱ끄얶흒끕..끆껑껑..끆끆흡끅..흡꾺꾺꾹끆ㄱ끄얶흒끕..끆껑껑..끆끆흡끅..흡꾺꾺꾹ㄱ끄엉..헝헝헝ㅇ..흡끄륵ㄱ끅끅ㄱ끄엉엉..흡끄윽..😭")
    
    if message.content == ("치킨마요"):
        await message.channel.send("치킨 사주세요🍗")

    if message.content == ("퍼플"):
        await message.channel.send("싸갈쓰가바갈쓰🤬")

    if message.content == ("그린"):
        await message.channel.send("채티 감성 푸흐-🥀")

    if message.content == ("레드"):
        await message.channel.send("영롱쓰한 와인🍷")

    if message.content == ("블루"):
        await message.channel.send("이중인격자👥")

    if message.content == ("보벳"):
        await message.channel.send("하...당신...지금 ‘’오타쿠’’를 ‘’무시’’하는 건가요?! 『오타쿠』는 원래 ‘’무언가에 열중하는 사람’’이라는 뜻..이랄까..? 암튼 당신네들 「멸칭」이랑은 상관없다고!! 무튼 당신네들...이렇게 나온다면 나도 참는 건 절대로 「무리」..한 번만 더 그러면 정말로 부.숴.버.릴.거.야.🔥")

    if message.content == ("따우"):
        await message.channel.send("이과생🏥")

    if message.content == ("케케하우스"):
        await message.channel.send("온새미로 공식 시체⚰️")

    if message.content == ("참치마요"):
        await message.channel.send("여신✨ 라고 할 ㅃ ㅓㄴ.")

    if message.content == "온새미로 임베드":
        embed = discord.Embed(title="온새미로 임베드", description="[온새미로 유튜브](https://www.youtube.com/channel/UCf2C7brwcccGuquxoxpbZSw)", color=0x00ff00)
        embed.set_footer(text="구독자 500명을 원합니다.")
        await message.channel.send(embed=embed)
    
    if message.content == "뽑기":
        ran = random.randint(1,14)
        if ran == 14:
            d = "신대장 당첨"
        if ran == 1:
            d = "아츠무 당첨"
        if ran == 2:
            d = "메구미 당첨"
        if ran == 3:
            d = "바쿠고 당첨"
        if ran == 4:
            d = "참치마요 당첨"
        if ran == 5:
            d = "트기 당첨"
        if ran == 6:
            d = "희님 당첨"
        if ran == 7:
            d = "애송 당첨"
        if ran == 8:
            d = "빌리 당첨"
        if ran == 9:
            d = "뇨꾸 당첨"
        if ran == 10:
            d = "도내 당첨"
        if ran == 11:
            d = "마시 당첨"
        if ran == 12:
            d = "령구 당첨"
        if ran == 13:
            d = "뀨 당첨"
        await message.channel.send(d)

client.run(token)