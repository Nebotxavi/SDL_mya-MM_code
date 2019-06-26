from xml.etree import ElementTree as ET
import os
import zipfile
import shutil


def main():
    # Find the target WSXZ file.
    for file in os.listdir():
        if file.endswith('mya_MM_xliff.wsxz'):
            burma_file = file

            temp_loc = 'temp_' + burma_file

            # Unzip target file.
            zipObj = zipfile.ZipFile(burma_file)
            to_rezip = zipObj.namelist()
            zipObj.extractall(temp_loc)

            zipObj.close()

            # Find the target files and modify them.
            for content in os.listdir(temp_loc):

                if content.endswith('.xlf'):
                    ET.register_namespace('iws', 'http://www.idiominc.com/ws/asset')
                    ET.register_namespace('', 'urn:oasis:names:tc:xliff:document:1.2')
                    xmlFile = ET.parse(os.path.join(temp_loc, content))
                    xmlFile.find('.//{urn:oasis:names:tc:xliff:document:1.2}file').attrib['target-language'] = 'my-MM'
                    xmlFile.write(os.path.join(temp_loc, content), encoding='utf-8', xml_declaration=True)

                if content == 'terminology_data.tbx':
                    ET.register_namespace('xml', 'http://www.w3.org/XML/1998/namespace')
                    xmlFile = ET.parse(os.path.join(temp_loc, content))
                    for node in xmlFile.findall('.//langSet'):
                        if node.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'mya-MM':
                            node.attrib['{http://www.w3.org/XML/1998/namespace}lang'] = 'my-MM'
                    xmlFile.write(os.path.join(temp_loc, content), encoding='utf-8', xml_declaration=True)

                if content == 'xcs.xml':
                    ET.register_namespace('', 'x-schema:TBXdsV1-0.xml')
                    xmlFile = ET.parse(os.path.join(temp_loc, content))
                    xmlFile.find('.//{x-schema:TBXdsV1-0.xml}langCode').text = 'my-MM'
                    xmlFile.write(os.path.join(temp_loc, content), encoding='utf-8', xml_declaration=True)

            # Rezip the files.
            re_zip = zipfile.ZipFile(burma_file, 'w')
            os.chdir(temp_loc)
            for f in to_rezip:
                re_zip.write(f, compress_type=zipfile.ZIP_DEFLATED)
            re_zip.close()

            # Remove the temp folder.
            os.chdir('..')
            shutil.rmtree(os.path.join(temp_loc))


if __name__ == '__main__':
    main()
