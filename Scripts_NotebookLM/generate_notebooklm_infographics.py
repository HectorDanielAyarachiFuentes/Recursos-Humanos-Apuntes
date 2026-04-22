import asyncio
import time
import os
from notebooklm_mcp.client import NotebookLMClient
from notebooklm_mcp.config import load_config

async def ask_and_save_infographic(client, topic, filename):
    print(f"📊 Generando infografía NotebookLM: {topic}")
    
    query = f"Genera una INFOGRAFÍA EN FORMATO DE TEXTO (usa muchos emojis, viñetas, estadísticas clave, secciones cortas y visuales) sobre: {topic}. Debe tener el mismo estilo que la herramienta 'Infografía' del Studio."
    await client.send_message(query)
    
    max_wait = 180
    stable_wait = 6
    start_time = time.time()
    last_len = 0
    stable_since = time.time()
    
    while time.time() - start_time < max_wait:
        current_ans = await client.get_response(wait_for_completion=False)
        if len(current_ans) > last_len:
            last_len = len(current_ans)
            stable_since = time.time()
        elif len(current_ans) == last_len and last_len > 200:
            if time.time() - stable_since >= stable_wait:
                with open(f"Desarrollo Gerencial/Infografias_Texto_NotebookLM/{filename}", "w", encoding="utf-8") as f:
                    f.write(current_ans)
                print(f"✅ Finalizado: {filename} ({len(current_ans)} caracteres)")
                return True
        time.sleep(3)
    return False

async def main():
    # Crear carpeta
    os.makedirs("Desarrollo Gerencial/Infografias_Texto_NotebookLM", exist_ok=True)
    
    config = load_config("Scripts_NotebookLM/notebooklm-config.json")
    client = NotebookLMClient(config)
    await client.start()
    if not await client.authenticate(): return

    try:
        queries = [
            # GENERALES POR UNIDAD
            ("Cómo se enlazan los textos y autores de la UNIDAD 1 (Lazatti, Gore, CLAD)", "Info_U1_Integradora.md"),
            ("Cómo se enlazan los textos y autores de la UNIDAD 2 (Longo, Lazatti, Crissien Castillo, Mintzberg)", "Info_U2_Integradora.md"),
            ("Cómo se enlazan los textos de la UNIDAD 3 (Dessler, Lazatti)", "Info_U3_Integradora.md"),
            ("Cómo se enlazan los textos de la UNIDAD 4 sobre Liderazgo", "Info_U4_Integradora.md"),
            ("Cómo se enlazan los textos de la UNIDAD 5 sobre Competencias", "Info_U5_Integradora.md"),
            
            # UNIDAD 1
            ("El texto de LAZATTI sobre 'Funciones Gerenciales' (U1)", "Info_U1_Lazatti.md"),
            ("El texto de GORE sobre 'La educación en la empresa' (U1)", "Info_U1_Gore.md"),
            ("La 'Carta Iberoamericana de Innovación en la Gestión Pública' (U1)", "Info_U1_CLAD.md"),
            
            # UNIDAD 2
            ("El texto de LONG sobre 'Institucionalizar la gerencia pública' (U2)", "Info_U2_Longo.md"),
            ("El texto de LAZATTI sobre 'Anatomía de las organizaciones y management' (U2)", "Info_U2_Lazatti.md"),
            ("El texto de CRISSIEN CASTILLO sobre 'Gerencia del Siglo XXI' (U2)", "Info_U2_Crissien.md"),
            ("Las 5 P de la Estrategia de Mintzberg (U2)", "Info_U2_Mintzberg.md"),
            
            # UNIDAD 3
            ("El texto de DESSLER sobre 'Cómo desarrollar gerentes' (U3)", "Info_U3_Dessler.md"),
            ("El texto de LAZATTI sobre 'Etapas del desarrollo gerencial' (U3)", "Info_U3_Lazatti.md"),
            
            # UNIDAD 4
            ("El texto de William Klemm sobre 'Liderazgo Creativo e Innovación' (U4)", "Info_U4_Klemm.md"),
            ("El texto de Lazatti y Tahilade sobre 'Liderazgo Gerencial' (U4)", "Info_U4_Lazatti_Tahilade.md"),
            
            # UNIDAD 5
            ("Competencias directivas en escenarios globales de Puga y Martínez (U5)", "Info_U5_Puga.md"),
            ("Estrategias para desarrollar competencias gerenciales de Ramírez Luz (U5)", "Info_U5_Ramirez.md"),
            ("La 'Guía Referencial Iberoamericana de Competencias Laborales' del CLAD (U5)", "Info_U5_Guia_CLAD.md"),
            ("La Revolución de las Competencias: Talento y Empleabilidad de Human Age (U5)", "Info_U5_HumanAge.md"),
            ("Desarrollo de Competencias Gerenciales de aula global (U5)", "Info_U5_AulaGlobal.md")
        ]
        
        for q, f in queries:
            await ask_and_save_infographic(client, q, f)
            time.sleep(3) # Pausa entre preguntas

    finally:
        if client.driver: client.driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
