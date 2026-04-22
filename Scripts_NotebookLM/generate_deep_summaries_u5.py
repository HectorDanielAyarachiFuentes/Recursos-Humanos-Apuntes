import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config

async def ask_and_save_deep(client, author_query, filename):
    print(f"📖 Extrayendo resumen profundo U5: {author_query}")
    query = f"Haz un resumen MUY EXTENSO Y COMPLETO del texto de {author_query} para la UNIDAD 5. No hagas una lista de temas, desarrolla cada concepto, categoría y explicación de forma detallada para que sirva como apunte de estudio universitario completo."
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
    config = load_config("Scripts_NotebookLM/notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        autores_u5 = [
            ("Puga Villareal Julián y Martínez Cerda Luis sobre 'Competencias directivas en escenarios globales'", "Resumen_U5_Puga_Martinez_Competencias_Globales_DETALLADO.md"),
            ("Ramírez Luz sobre 'Estrategias para desarrollar competencias gerenciales'", "Resumen_U5_Ramirez_Luz_Estrategias_DETALLADO.md"),
            ("la 'Guía Referencial Iberoamericana de Competencias Laborales en el Sector Público'", "Resumen_U5_Guia_Referencial_Competencias_Publico_DETALLADO.md"),
            ("el documento 'La Revolución de las Competencias: Talento, Empleabilidad y Tecnología. SERIE HUMAN AGE'", "Resumen_U5_Revolucion_Competencias_HumanAge_DETALLADO.md"),
            ("el documento 'Desarrollo de Competencias Gerenciales' (e-learning de aula global)", "Resumen_U5_Aula_Global_Desarrollo_Competencias_DETALLADO.md")
        ]
        
        for q, f in autores_u5:
            await ask_and_save_deep(client, q, f)
            time.sleep(5)

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
