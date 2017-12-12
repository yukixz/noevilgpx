#!/usr/bin/env python3

import re
import sys
from eviltransform import gcj2wgs_exact


def transform(src, dst):
    latlon = re.compile('lat="(\d+\.\d+)" lon="(\d+\.\d+)"')
    try:
        rfile = open(src, 'r')
        wfile = open(dst, 'w', newline='')
        for line in rfile:
            m = latlon.search(line)
            if m is not None:
                gcjlat, gcjlon = m.group(1, 2)
                wgslat, wgslon = gcj2wgs_exact(float(gcjlat), float(gcjlon))
                line = line.replace(gcjlat, str(round(wgslat, 6)))
                line = line.replace(gcjlon, str(round(wgslon, 6)))
            wfile.write(line)
    except Exception as err:
        raise err
    finally:
        rfile.close()
        wfile.close()


if __name__ == '__main__':
    transform(sys.argv[1], sys.argv[2])
