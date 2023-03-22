import ply.lex as lex

tokens = (
    'OPCOMMENT',
    'CLCOMMENT',
    'COMMENT',
    'DOCUMENTATION',
    'DATATYPE',
    'VARIABLE',
    'SEMICOLON',
    'FUNCTION',
    'FUNCNAME',

)

states = (
    ('commentmultiline', 'exclusive'),
    ('func0', 'exclusive') # When 'function' keyword is written
)
t_ANY_ignore = ' \n\t' 

# /* Ativa o estado 'commentmultiline'
def t_OPCOMMENT(t):
    r'/\*'
    t.lexer.begin('commentmultiline')
    return t

# No estado 'commentmultiline' tudo é comentário à exceção de */
def t_commentmultiline_CLCOMMENT(t):
    r'\*/'
    t.lexer.begin('INITIAL')
    return t

# '*/' sai do modo comentário
def t_commentmultiline_DOCUMENTATION(t):
    r'[^\*\/]+'
    return t

# Linhas começadas por // são ignoradas
def t_COMMENT(t):
    r'\/\/.+\n'
    #return t

# 'char', 'int', 'float', 'bool' are types of variable definitions
def t_DATATYPE(t):
    r'(char|int|float|bool)'
    return 

# Functions can only be defined in the initial state
# Must have precedence over VARIABLE
def t_INITIAL_FUNCTION(t):
    r'function'
    t.lexer.begin('func0')
    return t

# Variables start with \w or _ and can contain numbers after
def t_VARIABLE(t):
    r'[\w_][\w_\d]*'
    return t

# Semicolon
def t_SEMICOLON(t):
    r';'
    return t

def t_func0_FUNCNAME(t):
    r'[\w_][\w_\d]*'
    return t

def t_ANY_error(t):
    print(f'Carater ilegal: {t.value[0]}')
    t.lexer.skip(1)
    

lexer = lex.lex()

data = '''
/*
Olá
*/
// Ol+a
int i;
function m'''

lexer.input(data)


while tok := lexer.token():
    print(tok)