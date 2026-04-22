import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By

async def ask_and_save_deep(client, author_query, filename):
    print(f"📖 Extrayendo resumen profundo U2: {author_query}")
    await client.send_message(f"Haz un resumen MUY EXTENSO Y COMPLETO del texto de {author_query} para la UNIDAD 2. No hagas una lista de temas, desarrolla cada concepto, categoría y explicación del autor de forma detallada para que sirva como apunte de estudio completo. Incluye ejemplos si el autor los menciona.")
    
    max_wait = 180
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
        # Autores Unidad 2 - Extracción Individual Profunda
        autores_u2 = [
            ("FRANCISCO LONGO sobre 'Institucionalizar la gerencia pública'", "Resumen_U2_Longo_Gerencia_Publica_DETALLADO.md"),
            ("LAZATTI sobre 'Anatomía de las organizaciones y funciones del management'", "Resumen_U2_Lazatti_Anatomia_Management_DETALLADO.md"),
            ("CRISSIEN CASTILLO sobre 'Gerencia del Siglo XXI'", "Resumen_U2_Crissien_Castillo_SigloXXI_DETALLADO.md"),
            ("Los textos sobre 'Estrategias Gerenciales (Las 5 P de Mintzberg)'", "Resumen_U2_Mintzberg_Estrategias_5P_DETALLADO.md")
        ]
        
        for query, file in autores_u2:
            await ask_and_save_deep(client, query, file)
            time.sleep(5)

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
