import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By

async def main():
    print("Cargando configuración...")
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    
    print("Iniciando navegador...")
    await client.start()
    
    print("Autenticando...")
    if not await client.authenticate():
        print("Error: No estás logueado. Por favor, corre iniciar.bat primero.")
        if client.driver: client.driver.quit()
        return

    notebook_id = "6527eba6-9510-47f5-a756-dfb004bf18ca"
    print(f"Navegando al cuaderno {notebook_id}...")
    await client.navigate_to_notebook(notebook_id)
    
    # Esperar a que cargue el cuaderno
    time.sleep(5)
    
    query = "Haz un resumen muy breve y al grano exclusivamente del capítulo uno."
    print(f"Enviando consulta: {query}")
    await client.send_message(query)
    
    print("Esperando respuesta (esto puede tardar unos segundos)...")
    time.sleep(25)
    
    try:
        # Intento con get_response nativo
        ans = await client.get_response()
        if ans:
            print("== RESPUESTA ==")
            print(ans)
            return
    except Exception as e:
        print("get_response falló, usando método manual:", e)
        
    try:
        # Método manual (fallback)
        response_containers = client.driver.find_elements(By.CSS_SELECTOR, "div[class*='response'], [role='article']")
        if response_containers:
            text = response_containers[-1].text.strip()
            print("== RESPUESTA ==")
            print(text)
        else:
            print("No se encontró contenedor de respuesta.")
    except Exception as e:
        print("Error extrayendo manualmente:", e)
    
    if client.driver:
        client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
