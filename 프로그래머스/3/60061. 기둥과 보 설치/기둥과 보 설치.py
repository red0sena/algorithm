def solution(n, build_frame):
    # Store structures: set of (x, y, a) where a is 0 (pillar) or 1 (beam)
    structures = set()
    
    def can_install_pillar(x, y):
        # Pillar can be installed if:
        # 1. On the ground (y == 0)
        # 2. On top of another pillar
        # 3. On either end of a beam
        return (y == 0 or 
                (x, y-1, 0) in structures or 
                (x, y, 1) in structures or 
                (x-1, y, 1) in structures)
    
    def can_install_beam(x, y):
        # Beam can be installed if:
        # 1. One end is on a pillar
        # 2. Both ends are connected to other beams
        return ((x, y-1, 0) in structures or 
                (x+1, y-1, 0) in structures or 
                ((x-1, y, 1) in structures and (x+1, y, 1) in structures))
    
    def can_remove(x, y, a):
        # Temporarily remove the structure
        structures.remove((x, y, a))
        # Check if all remaining structures are valid
        for sx, sy, sa in structures:
            if sa == 0 and not can_install_pillar(sx, sy):
                structures.add((x, y, a))
                return False
            if sa == 1 and not can_install_beam(sx, sy):
                structures.add((x, y, a))
                return False
        structures.add((x, y, a))
        return True
    
    # Process each operation
    for x, y, a, b in build_frame:
        if b == 1:  # Install
            if a == 0 and can_install_pillar(x, y):
                structures.add((x, y, a))
            elif a == 1 and can_install_beam(x, y):
                structures.add((x, y, a))
        else:  # Delete
            if (x, y, a) in structures and can_remove(x, y, a):
                structures.remove((x, y, a))
    
    # Convert set to sorted list for result
    result = sorted(list(structures), key=lambda x: (x[0], x[1], x[2]))
    return result