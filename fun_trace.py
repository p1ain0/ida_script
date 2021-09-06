import idaapi
import idautils

def bp_delete(address):
    idaapi.del_bpt(address)

def color_function(function):
    idc.set_color(function, CIC_FUNC, 0x555555)
    bp_delete(function)
    
def bp(address, condition):
    idaapi.add_bpt(address, 4, BPT_DEFAULT)
    bpt = idaapi.bpt_t()
    idaapi.get_bpt(address, bpt)
    bpt.elang = 'Python'
    bpt.condition = condition
    idaapi.update_bpt(bpt)
    
def bp_function():
    for function in idautils.Functions():
        bp(function, 'color_function(' + str(function) + ')')
        
def color_clean():
    for function in idautils.Functions():
            idc.set_color(function, CIC_FUNC, 0xFFFFFF)
    bp_delete(function)

bp_function()