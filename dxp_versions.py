import sys
import xml.etree.ElementTree as ET
import zipfile

if len(sys.argv) != 2:
    print("missing dxp file, maybe?")
    sys.exit(1)

namespaces = {
    'sf': 'http://www.spotfire.com/schemas/Document1.0.xsd'
}

versions = set()
zf = zipfile.ZipFile(sys.argv[1])
descriptors = [fi.filename for fi in zf.filelist if fi.filename.endswith('AnalysisDocument.xml')] 
for fname in descriptors:
    try:
        xml = ET.parse(zf.open(fname))
        r = xml.getroot()
        versions.update(t.attrib['AssemblyName'] for t in r.findall('.//sf:TypeObject', namespaces=namespaces))
    except:
        pass # http://i.imgur.com/WQf0cM2.jpg

print('\n'.join(versions))