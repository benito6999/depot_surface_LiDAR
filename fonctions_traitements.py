from osgeo import gdal
import os
import whitebox



def resampling_cubic_spline(input, output, size):

    # Création des répertoire de sortie
    head_output = os.path.dirname(output)
    if not os.path.exists(head_output):
        os.makedirs(head_output)

    # ouverture des images et extraction des dimensions
    print('Ouverture {}'.format(input))
    dataset = gdal.Open(input, gdal.GA_ReadOnly)
    largeur, hauteur = (dataset.RasterXSize, dataset.RasterYSize)
    proj = dataset.GetProjection()

    # Resampling
    print('Resampling...')
    warp_object = gdal.WarpOptions(width=largeur / size, height=hauteur / size, resampleAlg=3, srcSRS=proj, dstSRS=proj)
    gdal.Warp(destNameOrDestDS=output, srcDSOrSrcDSTab=input, options=warp_object)
    print('Terminé')
    print()



def breachDepression(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création des répertoire de sortie
    head_output = os.path.dirname(output)
    if not os.path.exists(head_output):
        os.makedirs(head_output)

    # Création du MNT corrigé
    print('Creation du MNT corrigé')
    wbt.breach_depressions(dem, output)
    print('Terminé')
    print()


def relative_TPI(input, output, size):

    wbt = whitebox.WhiteboxTools()
    RUST_BACKTRACE = 1

    # Création des répertoire de sortie
    path = os.path.dirname(input)
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Répertoire de travail
    wbt.set_working_dir(path)
    wbt.verbose = False

    # Création du Relative TPI
    print('Création du TPI relatif...')
    wbt.relative_topographic_position(input, output, size, size)
    print('Terminé')
    print()


def SCA (dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du SCA
    print('Création du SCA...')
    wbt.fd8_flow_accumulation(dem, output, out_type='specific contributing area')
    print('Terminé')
    print()


def slope(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    print('Création de la pente...')
    wbt.slope(dem, output)
    print('Terminé')
    print()


def TWI(slope, sca, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du TWI
    print('Création du TWI...')
    wbt.wetness_index(sca, slope, output)
    print('Terminé')
    print()


def fpdems(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Filtrage
    print('Filtrage du mnt...')
    wbt.feature_preserving_smoothing(dem, output)
    print('Terminé')
    print()


def gdal_translate_32to64(input, output):

    # Création des répertoire de sortie
    head_output = os.path.dirname(output)
    if not os.path.exists(head_output):
        os.makedirs(head_output)

    # ouverture des images et extraction des dimensions
    print('Ouverture {}'.format(input))
    dataset = gdal.Open(input, gdal.GA_ReadOnly)
    largeur, hauteur = (dataset.RasterXSize, dataset.RasterYSize)

    # Resampling
    print('Resampling...')
    translate_object = gdal.TranslateOptions(width=largeur, height=hauteur, outputType=gdal.GDT_Float64)
    gdal.Translate(destName=output, srcDS=input, options=translate_object)
    print('Terminé')
    print()


def CircularVarofAspect(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du CircularVarianceOfAspect
    print('Creation du CircularVarianceOfAspect...')
    wbt.circular_variance_of_aspect(dem, output)
    print('Terminé')
    print()


def EdgeDensity(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du Edge Density
    print('Creation du EdgeDensity...')
    wbt.edge_density(dem, output)
    print('Terminé')
    print()


def sphericalStdDevNormals(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du Spherical Standard Deviation of Normals
    print('Creation du Spherical Standard Deviation of Normals...')
    wbt.spherical_std_dev_of_normals(dem, output)
    print('Terminé')
    print()


def plan_curvature(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du plan curvature
    print('Creation du plan curvature...')
    wbt.plan_curvature(dem, output)
    print('Terminé')
    print()


def profile_curvature(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du profile curvature
    print('Creation du profile curvature...')
    wbt.profile_curvature(dem, output)
    print('Terminé')
    print()


def tan_curvature(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du tan curvature
    print('Creation du tan curvature...')
    wbt.tangential_curvature(dem, output)
    print('Terminé')
    print()


def Downslope_Ind(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Création du Downslope Index
    print('Creation du Downslope Index...')
    wbt.downslope_index(dem, output)
    print('Terminé')
    print()


def AverNormVectAngDev(dem, output):

    wbt = whitebox.WhiteboxTools()
    wbt.verbose = False

    # Création du répertoire de sortie
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    # Average Normal Vector Angular Deviation
    print('Creation du Average Normal Vector Angular Deviation ...')
    wbt.average_normal_vector_angular_deviation(dem, output)
    print('Terminé')
    print()