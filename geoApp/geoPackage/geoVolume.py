'''
    package name: geoPackage
    module name: geoArea
    This module contains functions to compute volume of:
    cuboid, sphere
'''
def volumeSphere(radius):
    '''
    Objective: to compute the volume of a sphere
    Input Parameters: radius
    Return Value: volume of a sphere
    '''
    volume=(4/3)*(3.14)*(radius**3)
    return volume
def volumeCuboid(length,breadth,height):
    '''
    Objective: to compute the volume of a 
    Input Parameters: length,breadth,height
    Return Value: volume of a cuboid
    '''
    volume=length*breadth*height
    return volume

def main():
    radius=int(input('enter radius'))
    print('Volume of the sphere is : ',volumeSphere(radius))
if __name__=='__main__':
    main()
    
    

    
