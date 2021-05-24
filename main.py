#!/usr/bin/env python3

import argparse
import subprocess
import sys
import WebScraping
import EXIFDataViewer
import HashObtainer
import Servidor
import Cliente


def main():
    parser = argparse.ArgumentParser(prog='PIA',
                                     description='Script multitarea de ciberseguridad',
                                     usage='\n'
                                     'main.py A [-U] [-C]\n'
                                     'main.py B [-E]\n'
                                     'main.py C [-D]\n'
                                     'main.py D [-C] [-D]\n'
                                     'main.py E \n'
                                     'main.py F [-M]\n')
    parser.add_argument(
        'script', help='Elija el script a ejecutar: '
        'A). WebScraping, B). HaveIBeenPwned, C). EXIF Data Viewer, '
        'D). HashObtainer, E). Powershell',
        type=str, choices=['A', 'B', 'C', 'D', 'E', 'F'])

    parser.add_argument('-U', '--URL', help='URL de la pagina web')
    parser.add_argument('-E', '--EMail',
                        help='Correo electronico')
    parser.add_argument('-C', '--Carpeta',
                        help='Nombre que se le asignará a la carpeta')
    parser.add_argument('-D', '--Directorio',
                        help='Directorio donde se encuentra los archivos')
    parser.add_argument('-M', '--Modo',
                        help='S para Servidor, c para Cliente')

    try:
        args = parser.parse_args()
        if args.script == 'A':
            WebScraping.FuncionWS(args.URL, args.Carpeta)
        elif args.script == 'B':
            subprocess.call("./checkemail.sh " + str(args.EMail), shell=True)
        elif args.script == 'C':
            EXIFDataViewer.printMeta(args.Directorio)
        elif args.script == 'D':
            HashObtainer.FuncionHO(args.Directorio, args.Carpeta)
        elif args.script == 'E':
            p = subprocess.Popen(["powershell.exe",
                                  "C:\\Users\\ur\\Desktop\\PIA\\E1Script.ps1"],
                                 stdout=sys.stdout)
            p.communicate()
        elif args.script == 'F':
            #Servidor
            print("hola")
    except:
        print("main: falta un operando\nPruebe 'main -h' o 'main --help' para más información.")


if __name__ == "__main__":
    main()
