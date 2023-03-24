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
    'FUNCPARAMS',
    'OPCURLBRACE',
    'CLCURLBRACE',
    'WHILE',
    'CONDOPERATOR',
    'ARITOPERATOR',
    'ATRIBOPERATOR',
    'PROGRAM',
    'PROGRAMNAME',
    'FOR',
    'ITERATOR',
    'IN',
    'LIST',
    'FUNCEXEC',
    'FUNCARGS',
    'COMMA',
    'ARRVAR',
    'ARRAY',
    'ARRAYACCESS',
    'IF'
)

states = (
    ('commentmultiline', 'exclusive'),
    ('func0', 'exclusive'), # When 'function' keyword is written
    ('func1', 'exclusive'), # When function name is written
    ('program0', 'exclusive'),
    ('for0', 'exclusive'),
    ('funcexec0','exclusive')
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
    return t

# Functions can only be defined in the initial state
# Must have precedence over VARIABLE
def t_INITIAL_FUNCTION(t):
    r'function'
    t.lexer.begin('func0')
    return t

# Start of a program (keyword program)
def t_PROGRAM(t):
    r'program'
    t.lexer.begin('program0')
    return t

# For-loop keyword 
def t_FOR(t):
    r'for'
    t.lexer.begin('for0')
    return t

# If keyword
def t_IF(t):
    r'if'
    return t

# While keyword
def t_WHILE(t):
    r'while'
    return t

# Execution of a function (Ex: sum(  )
def t_FUNCEXEC(t):
    r'[\w_][\w_\d]*(?=\()'
    t.lexer.begin('funcexec0')
    return t

# Definition of a variable which holds an array: Ex: a[2]
def t_ARRVAR(t):
    r'[\w_][\w_\d]*\[\d+\]'
    return t

# Access an array index using a variable
def t_ARRAYACCESS(t):
    r'[\w_][\w_\d]*\[[\w_][\w_\d]*\]'
    return t

# Variables start with \w or _ and can contain numbers after
def t_INITIAL_VARIABLE(t):
    r'[\w_][\w_\d]*'
    return t

# Semicolon
def t_SEMICOLON(t):
    r';'
    return t

# Name of a function is like a variable but only in the func0 state
def t_func0_FUNCNAME(t):
    r'[\w_][\w_\d]*'
    t.lexer.begin('func1')
    return t

# Params start and end with ()
def t_func1_FUNCPARAMS(t):
    r'\(.*\)'
    t.lexer.begin('INITIAL')
    return t

# An array Ex: '{1,2,3,4}'
def t_ARRAY(t):
    r'\{\d+?(,\d+)*\}'
    return t

# Open curly braces
def t_OPCURLBRACE(t):
    r'{'
    return t

# Close curly braces
def t_CLCURLBRACE(t):
    r'}'
    return t

# Operator to do comparisons : <, >, =, >=, <=
def t_CONDOPERATOR(t):
    r'(?:>|<|==|<=|>=)'
    return t

# Arithmetic Operator: +, -, *, /
def t_ARITOPERATOR(t):
    r'(?:\+|\-|\*|\/)'
    return t

# '=' is the operator for attriibutions
def t_ATRIBOPERATOR(t):
    r'='
    return t

# Name of a program (must be in the program0 state)
def t_program0_PROGRAMNAME(t):
    r'[\w_][\w_\d]*'
    t.lexer.begin('INITIAL')
    return t

# In keyword (iterations)
def t_for0_IN(t):
    r'in'
    t.lexer.begin('INITIAL')
    return t 

# Variable to iterate (Ex: for i in [1,2,3,4])
def t_for0_ITERATOR(t):
    r'[\w_][\w_\d]*'
    return t

# Recognize lists (still to improve)
def t_LIST(t):
    r'\[\d+?(?:\.\.|)?\d+?\]'
    return t

# The arguments (values passed in) to a function call
def t_funcexec0_FUNCARGS(t):
    r'\(.+\)'
    t.lexer.begin('INITIAL')
    return t

# Comma to separate attribs
def t_COMMA(t):
    r','
    return t

# Error function for ANY state
def t_ANY_error(t):
    print(f'Carater ilegal: {t.value[0]}')
    t.lexer.skip(1)


    

lexer = lex.lex()

data = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer.input(data)


while tok := lexer.token():
    print(tok)