import asyncio
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.initialize()
    ans = await client.chat("Por favor, extrae todos los autores y sus temas/textos correspondientes para la Unidad 1 y la Unidad 2 detallados en el programa de estudio. Devuelve el resultado en formato markdown y asegúrate de mencionar las categorías.")
    print("RESULT:", ans)

asyncio.run(main())
