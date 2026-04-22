import asyncio
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config
import time
from selenium.webdriver.common.by import By

async def ask_and_save(client, query, filename):
    print(f"💬 Consultando: {query}")
    await client.send_message(query)
    time.sleep(30)
    
    try:
        selectors = ["div[class*='response']", "[role='article']", ".message-content"]
        for selector in selectors:
            elements = client.driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                text = elements[-1].text.strip()
                if len(text) > 50:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(text)
                    print(f"✅ Guardado: {filename}")
                    return True
    except Exception as e:
        print(f"⚠️ Error: {e}")
    return False

async def main():
    config = load_config("notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        q = "Basado EXCLUSIVAMENTE en el 'programa DG 2024.pdf', haz una lista muy detallada de los autores y sus textos correspondientes para la UNIDAD 4 y para la UNIDAD 5. Sé muy específico."
        await ask_and_save(client, q, "Desarrollo Gerencial/autores_u4_u5.txt")
    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
