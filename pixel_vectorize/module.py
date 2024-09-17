import typing
import xml.etree.ElementTree


def convert(
    pixels: "typing.Sequence[typing.Sequence[tuple[int, int, int]]] | typing.Sequence[typing.Sequence[tuple[int, int, int, int]]]",
) -> xml.etree.ElementTree.Element:
    height = len(pixels)
    width = len(pixels[0]) if height > 0 else 0
    has_opacity = len(pixels[0][0]) == 4 if height > 0 and width > 0 else False

    svg = xml.etree.ElementTree.Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        width=f"{width}",
        height=f"{height}",
        viewBox=f"0 0 {width} {height}",
    )

    for y in range(height):
        for x in range(width):
            pixel = pixels[y][x]

            if has_opacity:
                assert len(pixel) == 4
                r, g, b, a = pixel
                opacity = a / 255.0
            else:
                assert len(pixel) == 3
                r, g, b = pixel
                opacity = 1.0

            xml.etree.ElementTree.SubElement(
                svg,
                "rect",
                x=str(x),
                y=str(y),
                width="1",
                height="1",
                fill=f"rgb({r},{g},{b})",
                opacity=str(opacity),
            )

    return svg
