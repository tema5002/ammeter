import disnake

def make_list_embed(page, list):
    pages = (len(list)+9)//10
    description=""
    list = list[10*(page-1):]
    if page != pages: list = list[:10]
    for every in list:
        description+=f"- {every}\n"
    return disnake.Embed(title=f"Page {page}/{pages}", description=description)

def make_list_components(page, pages):
    components = []
    if page != 1:
        components+=[disnake.ui.Button(label="<", style=disnake.ButtonStyle.secondary, custom_id=f"UPDATELISTEMBED;{page-1}")]
    if page != pages:
        components+=[disnake.ui.Button(label=">", style=disnake.ButtonStyle.secondary, custom_id=f"UPDATELISTEMBED;{page+1}")]
    return components