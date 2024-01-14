"""
This is the main class of the project, it describes what is a orbiting body, that
in our case is a star.
"""

import math
CONSTANTE_G = 1

class OrbitingBody:
    """
    loren ipsum
    """

    def __init__(self, mass, velocity_x, velocity_y, coordenate_x, coordenate_y):
        """
        Insertion 
        """
        self.mass = mass
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.coordenate_x = coordenate_x
        self.coordenate_y = coordenate_y

    def calculate_distance_square(self, other_body):
        """
        This method calculates the square of euclidean distance 
        """
        diferenca_x = self.coordenate_x - other_body.coordenate_x
        diferenca_y = self.coordenate_y - other_body.coordenate_y
        distancia_local = math.pow(diferenca_x, 2) + math.pow(diferenca_y, 2)
        return distancia_local
    
    def calculate_gravitacional_force(self, other_body):
        """
        This method of the 
        """
        distance_square = self.calculate_distance_square(other_body)
        numerador = (self.mass)*(other_body.mass)
        gravitational_force = CONSTANTE_G*numerador/distance_square
        return gravitational_force


    def module_unitary_projection_axis_x(self, other_body):
        """
        hhh
        """
        distance = math.sqrt(self.calculate_distance_square(other_body))
        u_x = self.coordenate_x/distance
        return u_x
    

    def module_unitary_projection_axis_y(self, other_body):
        """
        hhh
        """
        distance = math.sqrt(self.calculate_distance_square(other_body))
        u_y = self.coordenate_y/distance
        return u_y
    

    def force_in_axis_x(self, other_body):
        """
        fofoca 
        """
        force = self.calculate_gravitacional_force(other_body)
        force_x = force*self.module_unitary_projection_axis_x(other_body)
        return force_x
    

    def force_in_axis_y(self, other_body):
        """
        fofoca 
        """
        force = self.calculate_gravitacional_force(other_body)
        force_y = force*self.module_unitary_projection_axis_y(other_body)
        return force_y


    def variation_dx(self, other_body):
        """
        Vx = Vx + Ax.dt
        x = x + Vx.dt
        """
        dx = dx_
        return 1


    def variation_dy(self, other_body):
        """
        """
        return 1

   
if __name__ == "__main__":
    print("Teste funcionando")
    corpo_1 = OrbitingBody(0, 10, 10)
    corpo_2 = OrbitingBody(0, 5, 2)
    print(corpo_1.square_of_distance(corpo_2))
