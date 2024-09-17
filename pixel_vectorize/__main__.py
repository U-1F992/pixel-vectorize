from .module import convert

import argparse
import typing
import xml.etree.ElementTree

import PIL.Image  # type: ignore


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)
    args = parser.parse_args()

    img = PIL.Image.open(args.input)
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    w, h = img.size
    svg = convert(
        [
            [
                typing.cast(
                    tuple[int, int, int, int],
                    img.getpixel((x, y)),
                )
                for x in range(w)
            ]
            for y in range(h)
        ]
    )
    print(xml.etree.ElementTree.tostring(svg, "utf-8").decode("utf-8"))


if __name__ == "__main__":
    main()
