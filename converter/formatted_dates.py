import re
from datetime import datetime

def remove_extra_zeros(fecha_str: str) -> str:
    nueva_fecha_str = fecha_str
    # Eliminar los últimos '000000' de los milisegundos
    if '000000' in fecha_str:
        nueva_fecha_str = fecha_str.replace('000000', '')
    return nueva_fecha_str

def convertir_fecha(fecha_str):
    # Formato de entrada
    formato_entrada = '%y/%m/%d %I:%M:%S,%f %p'
    # Formato de salida
    formato_salida = '%d/%m/%Y %H:%M:%S,%f'

    # Convertir cadena a objeto datetime
    fecha_obj = datetime.strptime(fecha_str, formato_entrada)
    # Convertir objeto datetime a cadena en el nuevo formato
    nueva_fecha_str = fecha_obj.strftime(formato_salida)

    return nueva_fecha_str

# Ejemplos de fechas
fechas = [
    '18/03/24 03:35:44,443000000 PM',
    '18/03/24 03:35:44,379000000 PM',
    '18/03/24 03:35:44,008000000 PM',
    '18/03/24 03:35:38,739000000 PM',
    '18/03/24 03:35:38,251000000 PM',
    '18/03/24 03:35:38,111000000 PM',
    '18/03/24 03:35:29,076000000 PM',
    '18/03/24 03:35:27,346000000 PM',
    '18/03/24 03:35:27,314000000 PM',
    '18/03/24 03:35:24,683000000 PM',
    '18/03/24 03:35:23,827000000 PM',
    '18/03/24 03:35:23,046000000 PM',
    '18/03/24 03:35:21,712000000 PM',
    '18/03/24 03:35:21,087000000 PM',
    '18/03/24 03:30:31,566000000 PM',
    '18/03/24 03:30:31,566000000 PM',
    '18/03/24 03:30:31,563000000 PM',
    '18/03/24 03:30:31,523000000 PM',
    '18/03/24 03:26:12,820000000 PM',
    '18/03/24 03:26:09,152000000 PM',
    '18/03/24 03:26:07,388000000 PM',
    '18/03/24 03:25:37,316000000 PM',
    '15/04/24 10:16:29,911000000 AM',
    '15/04/24 10:16:28,459000000 AM',
    '15/04/24 10:16:27,943000000 AM',
    '15/04/24 10:14:59,466000000 AM',
    '15/04/24 10:14:59,459000000 AM',
    '15/04/24 10:14:59,451000000 AM',
    '15/04/24 10:14:59,365000000 AM',
    '15/04/24 10:13:30,290000000 AM',
    '16/04/24 09:06:48,230000000 AM',
    '16/04/24 09:06:48,169000000 AM',
    '16/04/24 09:06:48,068000000 AM',
    '16/04/24 09:06:47,793000000 AM',
    '16/04/24 09:06:47,758000000 AM',
    '16/04/24 09:06:47,657000000 AM',
    '16/04/24 09:06:47,252000000 AM',
    '16/04/24 09:06:46,938000000 AM',
    '16/04/24 09:06:46,933000000 AM',
    '16/04/24 09:06:46,720000000 AM',
    '16/04/24 09:06:46,029000000 AM',
    '16/04/24 09:06:45,222000000 AM',
    '16/04/24 09:06:41,804000000 AM',
    '16/04/24 09:06:41,264000000 AM',
    '16/04/24 09:03:45,325000000 AM',
    '16/04/24 09:03:45,315000000 AM',
    '16/04/24 09:03:45,314000000 AM',
    '16/04/24 09:03:45,210000000 AM',
    '16/04/24 09:01:23,905000000 AM',
    '16/04/24 09:01:22,323000000 AM',
    '16/04/24 09:01:20,331000000 AM',
    '16/04/24 09:00:53,176000000 AM',
    '12/04/24 09:12:06,535000000 AM',
    '12/04/24 09:12:06,471000000 AM',
    '12/04/24 09:12:01,654000000 AM',
    '12/04/24 09:12:01,441000000 AM',
    '12/04/24 09:12:01,275000000 AM',
    '12/04/24 09:12:01,059000000 AM',
    '12/04/24 09:12:01,016000000 AM',
    '12/04/24 09:12:00,971000000 AM',
    '12/04/24 09:12:00,532000000 AM',
    '12/04/24 09:11:59,707000000 AM',
    '12/04/24 09:11:58,640000000 AM',
    '12/04/24 09:11:57,838000000 AM',
    '12/04/24 09:11:57,042000000 AM',
    '12/04/24 09:11:56,642000000 AM',
    '12/04/24 09:08:02,018000000 AM',
    '12/04/24 09:08:01,872000000 AM',
    '12/04/24 09:08:01,871000000 AM',
    '12/04/24 09:08:00,674000000 AM',
    '12/04/24 09:06:55,302000000 AM',
    '12/04/24 09:06:53,929000000 AM',
    '12/04/24 09:06:38,612000000 AM',
    '03/04/24 04:44:53,543000000 PM',
    '03/04/24 04:44:51,837000000 PM',
    '03/04/24 04:44:51,626000000 PM',
    '03/04/24 04:44:13,565000000 PM',
    '03/04/24 04:44:13,565000000 PM',
    '03/04/24 04:44:13,562000000 PM',
    '03/04/24 04:44:13,521000000 PM',
    '03/04/24 04:43:07,983000000 PM',
    '15/04/24 11:08:49,432000000 AM',
    '15/04/24 11:08:49,313000000 AM',
    '15/04/24 11:08:48,906000000 AM',
    '15/04/24 11:08:48,872000000 AM',
    '15/04/24 11:08:48,832000000 AM',
    '15/04/24 11:08:48,088000000 AM',
    '15/04/24 11:08:47,366000000 AM',
    '15/04/24 11:08:47,243000000 AM',
    '15/04/24 11:08:45,309000000 AM',
    '15/04/24 11:08:44,604000000 AM',
    '15/04/24 11:08:42,594000000 AM',
    '15/04/24 11:08:40,639000000 AM',
    '15/04/24 11:08:39,101000000 AM',
    '15/04/24 11:08:38,796000000 AM',
    '15/04/24 11:06:18,690000000 AM',
    '15/04/24 11:06:18,684000000 AM',
    '15/04/24 11:06:18,679000000 AM',
    '15/04/24 11:06:18,603000000 AM',
    '15/04/24 11:04:09,951000000 AM',
    '15/04/24 01:45:32,357000000 PM',
    '15/04/24 01:45:32,103000000 PM',
    '15/04/24 01:45:32,074000000 PM',
    '15/04/24 01:45:31,304000000 PM',
    '15/04/24 01:45:31,244000000 PM',
    '15/04/24 01:45:31,017000000 PM',
    '15/04/24 01:45:30,191000000 PM',
    '15/04/24 01:45:30,191000000 PM',
    '15/04/24 01:45:30,184000000 PM',
    '15/04/24 01:45:29,424000000 PM',
    '15/04/24 01:45:28,700000000 PM',
    '15/04/24 01:45:27,837000000 PM',
    '15/04/24 01:45:26,819000000 PM',
    '15/04/24 01:45:26,355000000 PM',
    '15/04/24 01:44:54,642000000 PM',
    '15/04/24 01:44:54,635000000 PM',
    '15/04/24 01:44:54,635000000 PM',
    '15/04/24 01:44:54,589000000 PM',
    '15/04/24 12:52:13,897000000 PM',
    '15/04/24 12:52:13,888000000 PM',
    '15/04/24 12:52:13,883000000 PM',
    '15/04/24 12:52:13,800000000 PM',
    '15/04/24 12:51:26,289000000 PM'
]

# Eliminar los microsegundos de las fechas y formatearla como 'DD/MM/AAAA hh:mm:ss'
for fecha in fechas:
    nueva_fecha = remove_extra_zeros(fecha)
    # print(nueva_fecha)
    fecha_formateada = convertir_fecha(nueva_fecha)
    print(fecha_formateada)
