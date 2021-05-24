# PIA-PC
PIA de PC
Este script multitarea contiene scripts de python, bash y powershell, con el proposito de tener todo en uno

Las herramientas son estas: A). WebScraping, B). HaveIBeenPwned, C). EXIF Data Viewer, D). HashObtainer, E). Powershell y F). Servidor

Existen cuatro opciones:  '-U', '--URL' que es para la URL de la pagina web,
                          '-E', '--EMail', que es para el Correo electronico'
                          '-C', '--Carpeta', que es el nombre que se le asignará a la carpeta
                          '-D', '--Directorio', que es el directorio donde se encuentra los archivos


pero no todas se deben usar para cada uno de los scripts, hay algunos que no reciben argumentos, en seguida se le mostrara cuales se usan en cual:
                                     main.py A [-U] [-C]
                                     main.py B [-E]
                                     main.py C [-D]
                                     main.py D [-C] [-D]
                                     main.py E
                                     main.py F
                                     
Si usted llegase a ejecutar el script con una opcion que no es simplemente le saldra un error y no pasara a mas
