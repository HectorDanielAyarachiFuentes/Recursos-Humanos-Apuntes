import asyncio
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate():
        print("⚠️ Se requiere iniciar sesión manualmente.")
        input("Por favor, ve a la ventana de Chrome, pon tu correo y clave. Cuando veas tus notebooks, vuelve aquí y presiona ENTER...")
        print("Reintentando autenticación...")
        if not await client.authenticate():
            print("Error de autenticación final.")
            return
    ans = await client.chat("Por favor, extrae todos los autores y sus temas/textos correspondientes para la Unidad 1 y la Unidad 2 detallados en el programa de estudio. Devuelve el resultado en formato markdown y asegúrate de mencionar las categorías.")
    print("RESULT:", ans)
    if client.driver:
        client.driver.quit()

asyncio.run(main())
