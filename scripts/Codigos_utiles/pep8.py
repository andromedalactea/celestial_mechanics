m3_km3= 10**9 #m^3 a km^3
G = c.G.value # m^3/(kg s^2)
GM2M=1/(G/m3_km3) #GM masa en Kg
#Encontremos la masa del sol con una buena precisión
#Codigo de la clase poara importar la libreria de SPICE la cual contiene la data necesaria para encontrar la masa del sol
!wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/gm_de440.tpc -O gm_de440.tpc
spy.furnsh('gm_de440.tpc')
n,dato=spy.bodvrd(f'sun','GM',1) #obteniendo la información de la base de datos

M_sun=dato*GM2M #conversión de unidades a 
M_sun