from core.controllers.planes.planes_controller import PlanesController

test_plane = PlanesController()
test_plane.create('"boeing"', '"888"', 400, 300, 50)
# print(test_plane.select())
