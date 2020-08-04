FREECADPATH = '/usr/lib/freecad/lib' # path to your FreeCAD.so or FreeCAD.dll file
import sys
sys.path.append(FREECADPATH)
import FreeCAD as fc

def main():
    fnm = './testCopy.FCStd'
    doc = fc.newDocument('testing')
    box = doc.addObject("Part::Box", "myBox")
    
    doc.recompute()
    doc.saveCopy(fnm)
    fc.closeDocument('testing')

# This lets you import the script without running it
if __name__=='__main__':
    main()