import discord
from discord.ext import commands
from Token import tokencode

# Configurar intents para el bot
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot con un prefijo para comandos
bot = commands.Bot(command_prefix="$", intents=intents)

# Función para enviar una imagen
async def sendimage(ctx, name):
    with open(f"C6/imagenes/{name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

# Comando de saludo
@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

# Comando de despedida
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def Ayudareciclaje(ctx):
    await ctx.send("""Tienes una lista de 5 elementos:
    - Madera
    - Cartón
    - Plástico
    - Metales
    - Vidrio""")

@bot.command()
async def Vidrio(ctx):
    await ctx.send("""El vidrio puede ser utilizado para:
    - Almacenamiento: Úsalo para guardar alimentos, especias o líquidos. Ejemplo: frascos y botellas.
    - Arte: Conviértelo en joyería o piezas creativas. Ejemplo: usa fragmentos para collares o vitrales.
    - Reciclaje: Recógelo para ser reprocesado y convertirlo en nuevos envases o materiales
    - DATO CURIOSO: El vidrio tarda 4000 años en degradarse.""")   
    await sendimage(ctx, "vidrio.jfif")

@bot.command()
async def Carton(ctx):
    await ctx.send("""El cartón puede ser utilizado para:
    - Almacenamiento: Crea cajas organizadoras o reutiliza las existentes. Ejemplo: almacena documentos o juguetes.
    - Manualidades: Haz decoraciones, maquetas o juguetes. Ejemplo: diseña figuras, marcos o casitas de cartón.
    - Aislamiento: Úsalo como material temporal para proteger ventanas o pisos. Ejemplo: coloca capas en áreas frías o húmedas.
    - DATO CURIOSO: El carton tarda 1 año en degradarse.""")
    await sendimage(ctx, "carton.webp")
    
@bot.command()
async def Plastico(ctx):
    await ctx.send("""El plástico puede ser utilizado para:
    - Decoración: Úsalo en manualidades para crear adornos, lámparas o cuadros. Ejemplo: diseña flores o mosaicos con tapas de plástico.
    - Reciclaje: Clasifica el plástico por tipo y llévalo a un centro de reciclaje para darle un nuevo uso.
    - Jardinería: Conviértelo en macetas, regaderas o protectores de plantas. Ejemplo: corta botellas plásticas para hacer pequeños invernaderos.
    - DATO CURIOSO: El plástico tarda 150 años en degradarse.""")
    await sendimage(ctx, "Plastico.jfif")
    
@bot.command()   
async def Metales(ctx):
    await ctx.send("""Los metales puede ser utilizado para:
    - Fabricación de nuevos productos: Fundirlos para fabricar latas, herramientas, o componentes industriales.
    - Reparación: Usarlos en soldaduras o para reparar objetos metálicos existentes.
    - Reventa: Llevarlos a centros de reciclaje que los compren para su reutilización.
    - DATO CURIOSO: 
    Hierro y acero: De 50 a más de 500 años, dependiendo de la exposición a la humedad y el oxígeno
    Aluminio: Alrededor de 200-500 años, ya que forma una capa protectora de óxido que ralentiza su descomposición.""")
    await sendimage(ctx, "Metales.jpeg")



bot.run(tokencode)
