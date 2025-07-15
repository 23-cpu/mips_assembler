def parser(instruction):
    comments_removed = instruction.split("#",1)
    
    if len(comments_removed) > 1:
        del comments_removed[-1]
    else:
        comments_removed = instruction
    print(comments_removed)
        
    
        
            



parser("sub $s1, $s2 , $s3 #new instruction")
parser("beq $s0, $s1, loop")
