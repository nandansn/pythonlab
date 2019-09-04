'''
try:
    stmt-1
    stmt-2
    stmt-3
    try:
        stmt-4
        stmt-5
        stmt-6
    except expression as identifier:
        stmt-7
    finally:
        stmt-8
    stmt-9
except expression as identifier:
    stmt-10
finally:
    stmt-11

stmt-12

1. if no exception:
    stmt-1,2,3,4,5,6,8,9,11,12. will be executed.
2. If exception in statement -2 and corresponding except block matched.:
    stmt-1,10,11,12 will be executed. finally of the inner try will not be executed. 
3. If exception in statement -2 and corresponding except block not matched.
    stmt-1,stmt-11. this is abnormal termination, stamt-12 will not be executed.

4. if exception in stnt-5 and corresponding inner except block matched.
    stmt -1,2,3,4,5,7,8,9,11,12 will be executed. normal termination.
5. if exception in stmt-5 and inner except block not matched. but outer excpet block matched.
    stmt -1,2,3,4,5,8,10,11,12.  outer except will take care. but before going outer block, inner finally should be executed. 
    normal  termination
6.if exception in stmt-5 and inner and outer except block not matched. 
    stmt -1,2,3,4,5,8,11 abnormal termination.
7.if exception in stmt-7 and inner and corresponding inner except block matched.
    stmt -1,2,3,[4,5,6 may or may not executed],7,8,10,11,12. stsmt-7 in inner excpet block, i
    if there is an exception in inner except block, outer except block has to handle it.

8. if exception in stmt-7 and inner and corresponding inner except block not matched.
    stmt -1,2,3,4,5,6,7,8,11 stsmt-7 in inner excpet block, 
    if there is an exception in inner except block, outer except block didn't handle so abnormal termination.

8. if exception in stmt-8 and inner and corresponding inner except block matched.
    stmt -1,2,3,[4,5,6,7 may or may not executed],7,8,10,11,12 - if outer except block matched. normal termination

9. if exception in stmt-9 and corresponding except block matched.
    stmt -1,2,3,4,5,6,8,9,10,11,12 normal termination.

10. if exception in stmt-10.
    stmt -[1,2,3,4,5,67,8,9 may or may not be executed],10, 11 abnormal termination

11. if exception in stmt-11/12.
    stmt -[1,2,3,4,5,6,7,8,9.10 may or may not be executed], 11/12 abnormal termination

'''