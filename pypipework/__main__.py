FREECADPATH = '/snap/freecad/16/opt/local/FreeCAD-0.18/lib' # path to your FreeCAD.so or FreeCAD.dll file
import sys
sys.path.append(FREECADPATH)

def import_fcstd():
    try:
        import FreeCAD
    except ValueError:
        print('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
    else:
        print('SUCCESS')

def main():
    import_fcstd()  

# This lets you import the script without running it
if __name__=='__main__':
    main()