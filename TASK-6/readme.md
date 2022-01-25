# Task-6.2 solution description

Storing Point coordinate pair as tuple can be implemented
modifying only Point class.
Old variables for x and y coordinate is replaces with single
self.__pos(x,y). This is tuple with two elements.

- First element (index 0) is x coordinate
- Second element (index 1) is y coordinate

Point class still expects two parameters: one for x and second for y coordinate.

Accordingly to made modification Point class methods that use coordinates are modified using self.\_\_pos[0] to reference x coordinate and self.\_\_[1] to reference y coordinate.

___

New class Polygon is created to ease drawing polygons. This is class **is not** abstract class and can be used to draw shapes directly.

Polygon class expects single parameter - list of Point objects.

Polygon class _draw methods main goal is to connect all point in __points list. It is done executing such steps:

- lifting pen (for moving to star position (first point))
- moving to first point
- putting pen down
- iterating trough all the points and moving to their location
- going to the first point to close the polygon
- lifting pen up

---

Center polygon class is most complicated of Polygon convenience classes. This class expects two arguments in constructor.

- _center_ - Point object that specifies center of the polygon to be drawn
- _radius_ - number of vertices for the polygon

 Some basic trigonometry is utilized to calculate coordinates of the vertices for the polygon. To perform mathematical functions python Math module is used.

After coordinates for all vertices are calculated and saved in single list, this list is passed to Polygon parent class init function.

---

Triangle class is similar to Polygon class. Only difference is that it expects three points fot construction. These points are passed to Polygon constructor as list to draw triangle.

Rectangle class expects two points needed to define rectangle. First one for the bottom left point and second for top right.Using these coordinates remaining two point coordinates can be calculated and rectangle drawn.

Octagon class ir child of **centerPolygon** class. Octagon expects center point (Point object) and radius.

---

Test is written so that Line objects are used to create + shape. In I quadrant rectangle is drawn, in II triangle, in III octagon, IV quadrant is used for centerPolygon that can have random number of vertices (between 3 and 7)
