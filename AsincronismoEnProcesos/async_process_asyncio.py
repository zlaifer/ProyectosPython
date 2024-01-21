import asyncio
import datetime

async def sumar_process(valor1, valor2):
    # Aquí va tu código asíncrono
    await asyncio.sleep(2)
    suma = valor1 + valor2
    print(f"La suma de [{valor1}] y [{valor2}] = [{suma}]")
    
async def multiplicar_process(valor1, valor2):
    # Aquí va tu código asíncrono
    await asyncio.sleep(5)
    suma = valor1 * valor2
    print(f"La multiplicación de [{valor1}] y [{valor2}] = [{suma}]")  

async def main():
    print("<================================================================>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio del Proceso => [{fecha_inicio}]")
    

    # Prueba 1 - Ejecución de las tareas -> Forma incorrecta de hacer uso de los await
    await sumar_process(3, 4)
    await multiplicar_process(3, 4)
    
    # Prueba 2 - Ejecución de las tareas en paralelo -> Forma correcta usando asyncio
    # Crea una lista de tareas asíncronas
    tareas = [simulate_async_process(duration) for duration in [sumar_process(3, 4), multiplicar_process(3, 4)]]
    # await asyncio.gather(*tareas)
    # for tarea in tareas:
    #     print(f"Completed: {tarea.result()}")
    
    fecha_fin = datetime.datetime.now()
    diferencia = (fecha_fin - fecha_inicio).total_seconds()
    print(f"Fecha/hora de finlaización del Proceso  => [{fecha_fin}]")
    print(f"El proceso demoró => [{diferencia}]")
    print("<================================================================>")

# Ejecuta el programa principal
asyncio.run(main())