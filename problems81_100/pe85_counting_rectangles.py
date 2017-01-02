# #####################################################################
# =====================================================================

"""
	USING COMBINATORICS:
	CREATING A RECTANGLE IS NOTHING MORE THAN PLACING TWO VERTICALS AND TWO HORIZONAL
	LINES. 
	SUPPOSE WE HAVE M X N RECTANGLE THEN WE HAVE (M+1) HORIZONTAL AND (N+1) VERTICALS
	SO WE NEED TWO OF EACH OF THEM TO FORM RECTANGLE.
	THERE ARE m+1 C 2 * n+1 C 2 WAYS OF DOING IT. THIS GIVES THE COUNT OF ALL RECTANGLES.
	SIMPLIFYING THE EXPRESSION WE GET, m*(m+1)/2 * n*(n+1)/2

	NOW COMES THE ROLE OF LIMIT ON M,N
	LETS TAKE M=2000 THEN IF N=1, WE HAVE RECTS= 2001*1000=2001000

"""

closest_area=0
closest_rect=0
target=2000000

x=2000
y=1

while x>=y:
	rects=(x*y*(x+1)*(y+1))/4
	if abs(target-rects)<abs(target-closest_rect):
		closest_rect=rects
		closest_area=x*y
	if rects>target:
		x-=1
	else: y+=1

# print closest_area
# print closest_rect