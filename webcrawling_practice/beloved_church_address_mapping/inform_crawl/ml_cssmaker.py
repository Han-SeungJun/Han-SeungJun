# The function that makes css selectors in order to go in a local church web page.
def css_selector_maker(_table, _row, _column):
    """
    The function that making the css selector key in order to each local church web page.
    
    _table  (type : int) -> css_var1, The variable that in other to distinguish the type of local church group.
    
        if _table = 2 -> The direct control local church.    (직할지교회)
           _table = 3 -> the Others local church in Korea.   (지방지교회)
           _table = 4 -> The local church in foreign contry. (해외지교회)
        
    _row    (type : int) -> css_var2, The variable that in order to collected one by one row in each table.
    
    _column (type : int) -> css_var3, The variable that in order to collected one by one element in each row.
        
    """

    area_css1 = "body > div.sub_container > div > table:nth-child("
    css_var1 = _table
    area_css2 = ") > tbody > tr:nth-child("
    css_var2 = _row
    area_css3 = ") > td:nth-child("
    css_var3 = _column
    area_css4 = ") > a"
    
    return area_css1 + str(css_var1) + area_css2 + str(_row) + area_css3 + str(_column) + area_css4
