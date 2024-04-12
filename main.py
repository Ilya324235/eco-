import discord
import random
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name='tips')
async def tips(ctx):
    await ctx.send(':seedling: :shield: **Сохранение природы** :shield::seedling: \n является крайне важным аспектом нашей жизни, поскольку от нее зависит наше благосостояние, здоровье и даже выживание на планете. Природа предоставляет нам не только жизненно важные ресурсы, такие как чистый воздух, питьевая вода и продовольствие, но и играет ключевую роль в поддержании биологического разнообразия, которое обеспечивает устойчивость экосистем. Очень важно понимать, что наши действия влияют на природу, и сохранение ее в целостности является залогом не только благополучия текущего поколения, но и будущих поколений. В ответе нашей заботы и ответственности за природу заключается обеспечение устойчивого и здорового будущего для всего живого на Земле.')
    with open('images/lap.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(':electric_plug:**Экономь энергию**:zap:\n 1) Используй энергоэффективные лампочки. \n 2) Выключай свет, когда он не нужен.\n 3) Отключай бытовую технику от сети, когда она не используется.:gear:')
    with open('images/lamp.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(':recycle:**Отказ от пластиковых бутылок**:recycle:: \n 1) Используй многоразовые бутылки для воды. \n 2) Вместо пластиковых бутылок выбирай напитки в стекле или бумажных упаковках.\n 3) Использу бутылки по нескольу раз.')
    with open('images/btlk.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Помни**, что деревья :evergreen_tree: играют важную роль в поддержании экологического баланса, и твои усилия по их посадке вносят вклад в сохранение природы. :palm_tree:')
    with open('images/tr.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Открывай**:park:для себя красоту местной флоры и фауны :deciduous_tree:. \n Посещай национальные парки, резерваты и ботанические сады. Это поможет тебе ценить красоту и уникальность местной природы, а также содействовать ее сохранению.')
    with open('images/der.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Сокращай**:earth_americas:использование химических удобрений и пестицидов.\n  Выбирай экологически безопасные методы земледелия и садоводства. Твои действия по устранению токсинов из окружающей среды будут способствовать сохранению здоровья почвы и водных источников.:droplet:')
    with open('images/udob3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command(name='musor')
async def sort(ctx):
    await ctx.send(':seedling: :shield: **Сохранение природы** :shield::seedling: \n является крайне важным аспектом нашей жизни, поскольку от нее зависит наше благосостояние, здоровье и даже выживание на планете. Природа предоставляет нам не только жизненно важные ресурсы, такие как чистый воздух, питьевая вода и продовольствие, но и играет ключевую роль в поддержании биологического разнообразия, которое обеспечивает устойчивость экосистем. Очень важно понимать, что наши действия влияют на природу, и сохранение ее в целостности является залогом не только благополучия текущего поколения, но и будущих поколений. В ответе нашей заботы и ответственности за природу заключается обеспечение устойчивого и здорового будущего для всего живого на Земле.')
    with open('images/lap.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(':electric_plug:**Экономь энергию**:zap:\n 1) Используй энергоэффективные лампочки. \n 2) Выключай свет, когда он не нужен.\n 3) Отключай бытовую технику от сети, когда она не используется.:gear:')
    with open('images/lamp.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(':recycle:**Отказ от пластиковых бутылок**:recycle:: \n 1) Используй многоразовые бутылки для воды. \n 2) Вместо пластиковых бутылок выбирай напитки в стекле или бумажных упаковках.\n 3) Использу бутылки по нескольу раз.')
    with open('images/btlk.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Помни**, что деревья :evergreen_tree: играют важную роль в поддержании экологического баланса, и твои усилия по их посадке вносят вклад в сохранение природы. :palm_tree:')
    with open('images/tr.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Открывай**:park:для себя красоту местной флоры и фауны :deciduous_tree:. \n Посещай национальные парки, резерваты и ботанические сады. Это поможет тебе ценить красоту и уникальность местной природы, а также содействовать ее сохранению.')
    with open('images/der.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('**Сокращай**:earth_americas:использование химических удобрений и пестицидов.\n  Выбирай экологически безопасные методы земледелия и садоводства. Твои действия по устранению токсинов из окружающей среды будут способствовать сохранению здоровья почвы и водных источников.:droplet:')
    with open('images/udob3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            await ctx.send(get_class(model="keras_model.h5", labels="labels.txt", image=f"images/{file_name}"))
    else:
        await ctx.send('вы забыли картинку')

bot.run("token")
