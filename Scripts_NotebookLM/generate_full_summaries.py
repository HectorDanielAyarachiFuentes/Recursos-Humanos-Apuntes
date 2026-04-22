import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By

async def ask_and_save(client, query, filename):
    print(f"💬 Consultando: {query}")
    await client.send_message(query)
    
    # NotebookLM puede tardar en generar respuestas largas. 
    # Usaremos una espera progresiva para capturar la respuesta final.
    max_wait = 120
    stable_wait = 5
    start_time = time.time()
    last_len = 0
    stable_since = time.time()
    
    print("⏳ Esperando respuesta completa...")
    
    while time.time() - start_time < max_wait:
        # Usar el método del cliente para obtener la respuesta limpia
        current_ans = await client.get_response(wait_for_completion=False)
        
        if len(current_ans) > last_len:
            last_len = len(current_ans)
            stable_since = time.time()
        elif len(current_ans) == last_len and last_len > 100:
            if time.time() - stable_since >= stable_wait:
                # La respuesta se estabilizó
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(current_ans)
                print(f"✅ Guardado: {filename} ({len(current_ans)} caracteres)")
                return True
        
        time.sleep(2)
    
    return False

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        # UNIDAD 1 - Resumen Integral
        q1 = """Haz un resumen extremadamente detallado de la UNIDAD 1 de Desarrollo Gerencial basado en el programa. 
        Incluye a TODOS los autores mencionados (como Lazatti, Gore, etc.) y desarrolla cada tema y categoría del programa. 
        Sé preciso, usa un lenguaje fácil de entender y organiza por autor/texto."""
        await ask_and_save(client, q1, "Desarrollo Gerencial/Resumen_Unidad_1.md")
        
        # UNIDAD 2 - Resumen Integral
        q2 = """Haz un resumen extremadamente detallado de la UNIDAD 2 de Desarrollo Gerencial basado en el programa. 
        Incluye a TODOS los autores mencionados (como Crissien Castillo, Longo, etc.) y desarrolla cada tema y categoría. 
        Sé preciso y organiza por autor/texto."""
        await ask_and_save(client, q2, "Desarrollo Gerencial/Resumen_Unidad_2.md")

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
