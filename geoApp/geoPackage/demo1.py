import geoVolume
from geoVolume import volumeSphere

def main():
    print('fn call prefixed by module name: geoVolume.volumeSphere(2) :',geoVolume.volumeSphere(2))
    print('direct call to fn volumeSphere: volumeSphere(2): ',volumeSphere(2))
    
if __name__=='__main__':
    main()
