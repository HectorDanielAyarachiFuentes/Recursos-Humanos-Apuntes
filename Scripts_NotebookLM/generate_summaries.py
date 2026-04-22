import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By

async def ask_and_save(client, query, filename):
    print(f"💬 Consultando: {query}")
    await client.send_message(query)
    # Esperar un poco más para que NotebookLM responda
    time.sleep(25)
    
    # NotebookLM suele usar selectores con 'p' dentro de contenedores de mensaje
    # Vamos a capturar todo el texto del contenedor de la última respuesta
    try:
        # Buscamos el último contenedor de mensaje del asistente
        # Basado en la estructura típica de NotebookLM
        response_containers = client.driver.find_elements(By.CSS_SELECTOR, "div[class*='response'], [role='article']")
        if response_containers:
            text = response_containers[-1].text.strip()
            if len(text) > 50:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"✅ Guardado en {filename}")
                return True
    except Exception as e:
        print(f"⚠️ Error extrayendo: {e}")
    
    print(f"❌ No se pudo guardar {filename}")
    return False

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        # Lazatti - Unidad 1
        q1 = "Haz un resumen detallado y preciso (mínimo 500 palabras) del texto de LAZATTI sobre 'Funciones Gerenciales' para la Unidad 1. Organízalo por las categorías mencionadas en el texto y asegúrate de que sea fácil de entender."
        await ask_and_save(client, q1, "Resumen_U1_Lazatti_Funciones_Gerenciales.md")
        
        # Gore - Unidad 1
        q2 = "Haz un resumen detallado (mínimo 500 palabras) del texto de GORE sobre 'La educación en la empresa' o 'Desarrollo Gerencial' para la Unidad 1. Enfócate en las etapas y categorías clave."
        await ask_and_save(client, q2, "Resumen_U1_Gore_Desarrollo_Gerencial.md")

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
