from os import system
from time import sleep


def main():
    while True:
        system("cls")
        print ("-----Decodificador------")
        print ("1) Tipo R\n2) Tipo I\n3) Tipo J\n4) Salir")
        tipo = int(input("Elije un tipo de instrucción: "))
        if tipo==1:
            instruccion = tipo_R()
            documento(instruccion)
            continue
        elif tipo==2:
            instruccion = tipo_I()
            documento(instruccion)
            continue
        elif tipo==3:
            instruccion = tipo_J()
            documento(instruccion)
        elif tipo==4:
            break


#funcion que "construye" la instruccion en formato R y la regresa
def tipo_R():
    #formato de cada instruccion, en el orden exacto que indica la sentencia print a que viene despues
    instrucciones = [
        {'Op':'000000','Sh':'00000','Fuc':'100000'},
        {'Op':'000000','Sh':'00000','Fuc':'100010'},
        {'Op':'011100','Sh':'00000','Fuc':'000010'},
        {'Op':'000000','Sh':'00000','Fuc':'011010'},
        {'Op':'000000','Sh':'00000','Fuc':'100101'},
        {'Op':'000000','Sh':'00000','Fuc':'101010'},
        {'Op':'000000','Sh':'00000','Fuc':'100100'},
        {'Op':'000000','Sh':'00011','Fuc':'011010'},
        {'Op':'000000','Sh':'00000','Fuc':'100110'},
        {'Op':'000000','Sh':'00000','Fuc':'000000'},
        {'Op':'000000','Sh':'00000','Fuc':'000111'},
        {'Op':'000000','Sh':'00000','Fuc':'100111'},
        {'Op':'000000','Sh':'00000','Fuc':'000100'}
    ]
    print("\n1) ADD \n2) SUB \n3) MUL\n4) DIV\n5) OR\n6) SLT\n7) AND\n8) MOD\n9) XOR\n10) NOP\n11) SRAV\n12) NOR\n13) SLLV")
    sel=int(input("Elije la instrucción a decodificar: "))
    #si el usuario selecciona "No Operacion" (NOP) la instruccion será solo ceros y esta funcion se acaba aqui
    if sel==10:
        return ("0"*32 + "\n")
    #toma el diccionario correspondiente de la lista de istrucciones dependiendo de la entrada del usuario
    for i, j in enumerate(instrucciones, 1):
        if sel == i:
            inst=j
    #pregunta al usuario las direcciones necesarias y usa una funcion para transformarlas a binario
    Rs=decimal_a_binario(int(input("Introduzca la direccion del operando 1: ")), 5)
    Rt=decimal_a_binario(int(input("Introduzca la direccion del operando 2: ")), 5)
    Rd=decimal_a_binario(int(input("Introduzca la direccion del resultado: ")), 5)
    instruccion = (inst['Op'] + Rs + Rt + Rd + inst['Sh'] + inst['Fuc'] + '\n')
    #regresa el codigo de 32 bits de la instruccion
    return instruccion


def tipo_I():
    instrucciones = [
        {'Op':'001000', 'rs':'', 'rt':'', 'value':'immediate'},
        {'Op':'001010', 'rs':'', 'rt':'', 'value':'immediate'},
        {'Op':'001100', 'rs':'', 'rt':'', 'value':'immediate'},
        {'Op':'001101', 'rs':'', 'rt':'', 'value':'immediate'},
        {'Op':'101011', 'rs':'', 'rt':'', 'value':'offset'},
        {'Op':'100011', 'rs':'', 'rt':'', 'value':'offset'},
        {'Op':'000100', 'rs':'', 'rt':'', 'value':'offset'}
    ]
    print("\n1) ADDI \n2) SLTI \n3) ANDI\n4) ORI\n5) SW\n6) LW\n7) BEQ")   
    sel = int(input("Elige la instruccion a decodificar: "))
    for i, j in enumerate(instrucciones, 1):
        if sel == i:
            inst = j
    inst['rs']=str(decimal_a_binario(int(input("Introduzca la direccion del operando 1: ")), 5))
    inst['rt']=str(decimal_a_binario(int(input("Introduzca la direccion resultado: ")), 5))
    inst['value']=str(decimal_a_binario(int(input("Introduzca la constante o direccion: ")), 16))
    instruccion = (inst['Op'] + inst['rs'] + inst['rt'] + inst['value'] + '\n')
    return instruccion
    
def tipo_J():
    instrucciones = [
        {'Op':'000010','value':'offset'},
        {'Op':'000011','value':'offset'}
    ]
    print("\n1) J \n2) Jal")
    sel=int(input("Elige la instruccion a decodificar: "))
    for i, j in enumerate(instrucciones, 1):
        if sel == i:
            inst = j
    inst['value']=str(decimal_a_binario(int(input("Introduzca la direccion: ")), 26))
    instruccion = (inst['Op'] + inst['value'] + '\n')
    return instruccion

def decimal_a_binario(decimal, bits):
    if decimal <= 0:
        return ("0"*bits)
    if decimal >= (2**bits):
        return ("1"*bits)
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    binario = ("0"*(bits-len(binario)) + binario)
    return binario


def documento(inst):
    with open("InstMemory.mem", "a") as file:
        file.write(inst)

main()
