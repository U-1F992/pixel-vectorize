import pixel_vectorize

import xml.etree.ElementTree

if __name__ == "__main__":
    svg = pixel_vectorize.convert([[(0, 0, 0)]])
    print(xml.etree.ElementTree.tostring(svg, encoding="utf-8").decode("utf-8"))
