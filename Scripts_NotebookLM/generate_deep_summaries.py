import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By

async def ask_and_save_deep(client, author_query, filename):
    print(f"📖 Extrayendo resumen profundo: {author_query}")
    await client.send_message(f"Haz un resumen MUY EXTENSO Y COMPLETO del texto de {author_query}. No hagas una lista de temas, desarrolla cada concepto, categoría y explicación del autor de forma detallada para que sirva como apunte de estudio completo.")
    
    max_wait = 180 # Más tiempo para respuestas largas
    stable_wait = 8
    start_time = time.time()
    last_len = 0
    stable_since = time.time()
    
    while time.time() - start_time < max_wait:
        current_ans = await client.get_response(wait_for_completion=False)
        if len(current_ans) > last_len:
            last_len = len(current_ans)
            stable_since = time.time()
        elif len(current_ans) == last_len and last_len > 500:
            if time.time() - stable_since >= stable_wait:
                with open(f"Desarrollo Gerencial/{filename}", "w", encoding="utf-8") as f:
                    f.write(current_ans)
                print(f"✅ Finalizado: {filename} ({len(current_ans)} caracteres)")
                return True
        time.sleep(3)
    return False

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        # Autores Unidad 1 - Extracción Individual Profunda
        autores_u1 = [
            ("LAZATTI sobre 'Funciones Gerenciales'", "Resumen_U1_Lazatti_DETALLADO.md"),
            ("GORE sobre 'La educación en la empresa / Desarrollo Gerencial'", "Resumen_U1_Gore_DETALLADO.md"),
            ("CLAD sobre la 'Carta Iberoamericana de Innovación en la Gestión Pública'", "Resumen_U1_CLAD_DETALLADO.md")
        ]
        
        for query, file in autores_u1:
            await ask_and_save_deep(client, query, file)
            # Pequeña pausa entre consultas para no saturar
            time.sleep(5)

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
