# It appended Africa local church in the list.
def africa_local_church_crawler(_list, positions, addresses, local_name):
    """
    position (type : array) -> collected in the each position
    
    addrss (type : array) -> address fitted in each position.
    """
    for position, address in zip(positions, addresses):
        if str(address) == "":
            pass
        else:
            address += str(local_name)
        _list.append({
            "위치":position, "주소":address, "전화번호":" (대략적 위치)"
        })
    return _list
