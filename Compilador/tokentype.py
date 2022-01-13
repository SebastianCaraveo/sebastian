# definir todos los tokens enumerarlos
import enum
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE  = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    ##KEYWORDS
    
    LABEL = 101
    GOTO = 102
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 100
    ENDWHILE = 111
    DECLARA = 112
    #AUX
    COMO = 115
    #SPEEDS
    PRIMERA = 120
    SEGUNDA = 121
    TERCERA = 122
    CUARTA =123
    QUINTA = 124
    SEXTA = 125
    NEUTRAL = 126
    #ACTIONS
    ENCENDER = 130
    APAGAR = 131
    ACELERAR = 132
    FRENAR = 133
    PRINT = 134
    #ALERTS
    IZQ = 140
    DER = 141
    CORTAS = 142
    LARGAS = 143
    ESTACIONARIAS = 145
    #DATATYPE
    ENTERO = 150
    TEXTO = 151
    DECIMAL = 152
    BOOLEAN = 153
    
    
    #OPERADORES 
    EQ= 201
    PLUS =202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT =  208
    LTEQ= 209
    GT = 210
    GTEQ = 211
