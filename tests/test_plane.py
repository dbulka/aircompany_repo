from core.controllers.planes.planes_controller import PlanesController

test_plane = PlanesController()
test_plane.create('"boeing"', '"888"', 400, 300, 50)
# test_plane.update('777', 450, 350, 75, 1)
# test_plane.delete(1)
print(test_plane.read())
