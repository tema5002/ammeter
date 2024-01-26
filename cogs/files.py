import disnake, datetime, os
from disnake.ext import commands
from temalib import openfile, get_file_path
from embed_lists_maker import *

class Files(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    save_file_cooldowns = {} # dictionary to store save_file user cooldowns
    send_file_cooldowns = {} # dictionary to store send_file user cooldowns

    @commands.slash_command(name="file_data", description="Returns information about attached file")
    async def file_data_handler(self, ctx, file: disnake.Attachment):
        embed = disnake.Embed(title="File Data", color=0x00FF00)

        filename = file.filename
        size = file.size
        url = file.url
        content_type = file.content_type
        duration = file.duration
        waveform = file.waveform

        embed.add_field(name="Filename",       value=filename)
        embed.add_field(name="Size",           value=f"{size} bytes")
        embed.add_field(name="Content Type",   value=content_type)
        embed.add_field(name="URL",            value=url, inline = False)
        if duration:
            embed.add_field(name="Duration",   value=f"{duration} seconds")
        if waveform:
            embed.add_field(name="Waveform",   value=waveform)

        await ctx.send(embed=embed)

    @commands.slash_command(name="save_file", description="saves file to a folder on my laptop")
    async def file_saver(self, ctx, file: disnake.Attachment, filename: str):
        await ctx.response.defer()
        trusteds = openfile("save_file_trusteds.txt").read().split("\n")
        trusteds = [int(t.split("#")[0].strip()) for t in trusteds]
        if not ctx.author.id in trusteds:
            await ctx.send("you must be in trusted list to use this command", ephemeral=True)
        elif file.size > 4*1024*1024:
            await ctx.send(f"this file weights more than **4** MB! (~**{math.ceil(file.size/1024)}** KB)")
        else:
            now = datetime.datetime.now()
            last_used = self.save_file_cooldowns.get(ctx.author.id)

            if last_used is not None:
                # time since last use
                when_used = (now - last_used).total_seconds()

                if when_used < 60:
                    await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(60 - when_used)} seconds", ephemeral=True)
                    return

            self.save_file_cooldowns[ctx.author.id] = now

            if "." in file.filename:
                filepath = get_file_path(os.path.dirname(__file__), "shitpost", filename+file.filename[file.filename.rfind("."):])
            else:
                filepath = get_file_path(os.path.dirname(__file__), "shitpost", filename)
            try:
                await file.save(filepath)
                await ctx.send(f"File saved successfully in '{filepath}'.")
                channel = self.bot.get_channel(1187779030892675193)
                await channel.send(f"**{ctx.author.name}** `{ctx.author.id}` added file {filename}")
            except Exception as e:
                await ctx.send(f"An error occurred while saving the file: {e}")

    @commands.slash_command(name="list_files", description="lists all files saved with /save_file")
    async def list_files(self, ctx):
        files = os.listdir("shitpost")
        embed=make_list_embed(1, files)
        await ctx.send(embed=embed, components=make_list_components(1, len(files)))

    @commands.slash_command(name="send_file", description="sends any file saved using with /save_file")
    async def send_file(self, ctx, filename: str):
        await ctx.response.defer()
        if not filename in os.listdir("shitpost"):
            await ctx.send(f"file `{filename}` doesnt exist", ephemeral=True)
        else:
            now = datetime.datetime.now()
            last_used = self.send_file_cooldowns.get(ctx.author.id)

            if last_used is not None:
                # time since last use
                when_used = (now - last_used).total_seconds()

                if when_used < 20:
                    await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {(20 - when_used):.2f} seconds")
                    return

            self.send_file_cooldowns[ctx.author.id] = now
            file_path = get_file_path(os.path.dirname(__file__), "shitpost", filename)
            await ctx.send(filename, file=disnake.File(file_path))

    @commands.slash_command(name="sort", description="Sort file")
    async def sort_file(self, ctx, file: disnake.Attachment):
        await ctx.response.defer()
        if file.size > 128*1024:
            await ctx.send(f"this file weights more than **128** KB! (~**{math.ceil(file.size/1024)}** KB)")
            return
        fn = file.filename
        extension = fn[fn.rfind(".")+1:]
        if extension != "txt":
            await ctx.send(f"this is not a txt file :skull: ({extension})")
            return

        await file.save(get_file_path(__file__, "temp", "input.txt"))
        with editfile(get_file_path(__file__, "temp", "output.txt")) as output:
            for every in sorted(openfile(get_file_path(__file__, "temp", "input.txt")).readlines()): output.write(every)
        await ctx.send(fn, file=disnake.File(get_file_path(__file__, "temp", "output.txt")))

def setup(bot): bot.add_cog(Files(bot))