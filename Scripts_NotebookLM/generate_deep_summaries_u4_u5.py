import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config

async def ask_and_save_deep(client, query, filename):
    print(f"📖 Extrayendo resumen profundo: {query}")
    await client.send_message(query)
    
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
        queries = [
            ("Haz un resumen MUY EXTENSO Y COMPLETO de todos los textos obligatorios de la UNIDAD 4 según el 'programa DG 2024.pdf'. Para cada autor, desarrolla todos sus conceptos, etapas y explicaciones de forma detallada para que sirva como apunte de estudio universitario.", "Resumen_U4_Completo_DETALLADO.md"),
            ("Haz un resumen MUY EXTENSO Y COMPLETO de todos los textos obligatorios de la UNIDAD 5 según el 'programa DG 2024.pdf'. Para cada autor, desarrolla todos sus conceptos, técnicas y explicaciones de forma detallada para que sirva como apunte de estudio universitario.", "Resumen_U5_Completo_DETALLADO.md")
        ]
        
        for q, f in queries:
            await ask_and_save_deep(client, q, f)
            time.sleep(5)

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
