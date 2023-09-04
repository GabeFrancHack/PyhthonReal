#V is the number of grapevines that will fit in the row.
#R is the length of the row, in feet.
#E is the amount of space, in feet, used by an end-post assembly.
#S is the space between vines, in feet.

R=int(input('the length of the row in feet:'))
E=int(input('the amount of space, in feet, used by an end-post assembly:'))
S=float(input('the space between vines, in feet.:'))
V=(R-(2*E))/S
print('the number of grapevines that will fit in the row',V,)