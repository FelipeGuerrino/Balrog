import discord, random
from discord.ext import commands

class DiceConverter(commands.Converter):        
    async def convert(self, ctx, argument):
        """Converte :argument para o tipo Dice"""
        def check(a):
            """Checa se o prefixo de :argument é d, D ou o número de dados"""
            if a.startswith('d') or a.startswith('D'):
                return f"1{a}"
            elif isinstance(int(argument[0]), int) == True and argument[1] == 'd' or argument[1] == 'D':
                return a
        argument = check(argument)
        
        return [ int(argument[0]), int(argument[2:]) ]
        
class BonusConverter(commands.Converter):
    async def convert(self, ctx, argument):
        """Converte :argument para o tipo Bonus"""
        if argument.startswith('+'):
            return int(argument[1:])

        raise commands.BadArgument(message=None)

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r', 'rolar', 'dados', 'dices'])
    async def roll(self, ctx, dice : DiceConverter, bonus : BonusConverter=0):
            """Escolhe um número aleatório com base no valor informado pelo usuário
               Por ex: /r d(x) => (y)
               Se for informado um valor antes do prefixo 'd', será utilizado como multiplicador
               Por ex: /r 2d(x) => (y)+(z)

               Parâmetro opcional: bonus = adiciona o valor com o número rolado
               Por ex: /r d(x) +1 => (y+1)
            """
            if dice[1] < 101:
                lista = [i for i in range(1, dice[1]+1)]
                res = random.choices(lista, k=dice[0])
            
                if dice[0]==1:
                    await ctx.send(f"{sum(res)} + {bonus}")  
                    await ctx.send(sum(res) + bonus)
                else:
                    await ctx.send(f"{res} + {bonus}")
                    await ctx.send(sum(res) + bonus)

           
            else:
                await ctx.send('Tá louco mermão??? :japanese_goblin:')




    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Monke :monkey_face:')


        
def setup(bot):
    bot.add_cog(Dice(bot))