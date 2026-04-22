import asyncio
import time
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    
    print("🚀 Iniciando navegador...")
    await client.start()
    
    print("🔑 Autenticando...")
    if not await client.authenticate():
        print("❌ Error: Se requiere autenticación manual.")
        return

    try:
        query = "Lista detalladamente los autores y temas de la Unidad 1 y la Unidad 2 según el programa de estudio en este notebook. Organízalo por unidad y menciona las categorías."
        print(f"💬 Enviando consulta: {query}")
        await client.send_message(query)
        
        print("⏳ Esperando respuesta (y extrayendo contenido bruto)...")
        # Esperar un tiempo fijo para que genere
        time.sleep(20)
        
        # Extraer el HTML de la página para buscar el contenido manualmente
        html = client.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # Guardar HTML para debug si falla
        with open("page_debug.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        # Buscar el último mensaje que no sea el del usuario
        # En NotebookLM los mensajes suelen estar en contenedores específicos
        # Vamos a intentar encontrar el bloque de texto más grande que parezca una respuesta
        
        paragraphs = soup.find_all(['p', 'div', 'span'])
        long_texts = []
        for p in paragraphs:
            t = p.get_text().strip()
            if len(t) > 100 and "Unidad 1" in t:
                long_texts.append(t)
        
        if long_texts:
            # El más largo suele ser el resumen
            ans = max(long_texts, key=len)
            print("\n✅ Contenido extraído con éxito!")
            
            with open("syllabus_data.txt", "w", encoding="utf-8") as f:
                f.write(ans)
        else:
            print("⚠️ No se encontró el texto esperado usando búsqueda por palabras clave.")
            # Intentar el método del cliente como última opción
            ans = await client.get_response(wait_for_completion=False)
            print(f"Respuesta del cliente: {ans[:100]}...")
            
    except Exception as e:
        print(f"❌ Error durante el proceso: {e}")
    finally:
        if client.driver:
            client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
