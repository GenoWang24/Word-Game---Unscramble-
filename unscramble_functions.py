# Move constants
SHIFT = 'S'
FLIP = 'F'
CHECK = 'C'

# Constant for hint functions
HINT_MODE_SECTION_LENGTH = 3
def get_section_start(section_num: int, section_len: int) -> int:
    """Return the starting index of the section corresponding to section_num
    if the length of a section is section_len.

    >>> get_section_start(1, 3)
    0
    >>> get_section_start(2, 3)
    3
    >>> get_section_start(3, 3)
    6
    >>> get_section_start(4, 3)
    9
    """
    return (section_num-1) * section_len
def is_valid_move(move_option: str) -> bool:
    
    """Return TRUE if and only if the parameter matches one of the three moves 
        that are considered valid.
        
        >>> is_valid_move('shift')
        True
        >>> is_valid_move('flip')
        True
        >>> is_valid_move('check')
        True
        >>> is_valid_move('cancel')
        False
        """  
    if move_option == 'shift':
        return True
    elif move_option == 'flip':
        return True
    elif move_option == 'check':
        return True
    else:
        return False
def get_num_sections(section_answer: str,  section_len: int)-> int:
    """Return the number of sections in the answer string.
    
    >>> get_num_sections('genoisbad', 3)
    3
    >>> get_num_sections('genoisnice', 5)
    2
    """
    return len(section_answer) // section_len
def is_valid_section(section_num: int, section_answer: str, 
                     section_len: int)-> bool:
    """Return if and only if the parameter represents a section number that is 
    valid for the given answer 
    string and section length.
    
    >>> is_valid_sections(4, 'genoisnice' , 5)
    false
    >>> is_valid_sections(2, 'genoisnice' , 5)
    true
    """
    if len(section_answer)/section_len == section_num:
        return True
    else:
        return False
def check_section(game_state: str, section_answer: str, section_num: int, 
                  section_len: int)-> bool:
    """Return True if and only if the specified section in the game state match
    es the same section in the answer string
    
    >>> check_section('genooocl', 'genocool', 1, 2)
    True
    >>> check_section( 'imabad', 'iambad',  2, 3)
    True
    >>> check_section('genooocl',  'genocool',  2,  2)
    False
    """
    start_index=(section_num-1) * section_len
    end_index=start_index+section_len
    
    if game_state[start_index : end_index]==section_answer[start_index : 
                                                           end_index]:
        return True
    else:
        return False  
def change_section(game_state: str, section_move: str, section_num: int, 
                   section_len: int)->str:
    """Return a new string that reflects the updated game state after applying 
    the given move to the specified section
    
    >>> change_section('genolooc', 'F', 2, 4)
    'genocool'
    >>> change_section('genoenic', 'S', 2, 4)
    'genonice'
    """
    start_index=(section_num-1) * section_len
    end_index=start_index+section_len    
   
    if section_move=='F':
        return game_state[0:start_index]+ game_state[end_index-1]+\
               game_state[(start_index+1):(end_index-1)]+\
               game_state[start_index]+game_state[end_index:]
    elif section_move=='S':
        return game_state[0:start_index]+ game_state[(start_index+1):end_index]\
               +game_state[start_index]+game_state[end_index:]
    else:
        return 'none'
def section_needs_flip(game_state: str, section_answer: str, 
                       section_num: int)-> bool:
    """ Return if and only if the specified section in the game state will never
    match the same section in the answer string without doing a FLIP move
   
    >>> section_needs_flip('geterd', 'getred', 2)
    True
    >>> section_needs_flip('getedr', 'getred', 2)
    False
    >>> section_needs_flip('getdre', 'getred', 2)
    False
    >>>
    """
    section_len=3
    start_index=(section_num-1) * section_len
    end_index=start_index+ section_len       
    if game_state[(start_index+1):]+ game_state[start_index]==\
       section_answer[start_index:(end_index)]:
        return False
    elif game_state[(end_index-1)]+game_state[start_index:(end_index-1)]==\
         section_answer[start_index:(end_index)]:
        return False
    else:
        return True
def get_move_hint(game_state: str, section_answer: str, section_num: int)-> str:
    """Return a move that will help the player rearrange the specified section 
    correctly either SHIFT or FLIP
    
    >>> get_move_hint('geterd', 'getred', 2)
    'F'
    >>> get_move_hint('getedr', 'getred', 2)
    'S'
    >>> get_move_hint('getdre', 'getred', 2)
    'S'
    """
    section_len=3
    start_index=(section_num-1) * section_len
    end_index=start_index+ section_len  
    
    if game_state[(start_index+1):]+game_state[start_index]==\
       section_answer[start_index:(end_index)]:
        return 'S'
    elif game_state[(end_index-1)]+game_state[start_index: (end_index-1)]==\
         section_answer[start_index:(end_index)]:
        return 'S'
    else:
        return 'F'