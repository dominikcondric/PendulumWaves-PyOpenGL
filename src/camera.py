import glm

class PerspectiveCamera:
    def __init__(self, position: glm.vec3):
        self.position = position
        self.center = glm.vec3(0., 0., 0.)
        self.up = glm.vec3(0., 1., 0.)
        self.near_plane = 0.1
        self.far_plane = 50.
        self.aspect_ratio = 1024. / 769.
        self.fov = 45.

    def project(self) -> glm.mat4:
        return glm.perspective(self.fov, self.aspect_ratio, self.near_plane, self.far_plane)
        
    def lookAt(self) -> glm.mat4:
        return glm.lookAt(self.position, self.center, self.up)
