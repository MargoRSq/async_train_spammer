import io
import aiohttp

from time import time
from typing import List
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger, PdfFileReader
from svglib.svglib import svg2rlg

async def svg2pdf(url: str) -> List:
    start = time()
    mergedObject = PdfFileMerger()

    svgs = await parse_svgs(url)
    for svg in svgs:
        svg = io.BytesIO(svg)
        drawing = svg2rlg(svg)
        pdf = io.BytesIO(renderPDF.drawToString(drawing))

        mergedObject.append(PdfFileReader(pdf))

    with io.BytesIO() as byte_f:
        mergedObject.write(byte_f)
        bytes_value = byte_f.getvalue()
    return [bytes_value, time() - start, len(svgs)]

async def parse_svgs(url: str) -> list:
    session = aiohttp.ClientSession()
    svg_array = []
    page_num = 1
    first_request = await session.get(url + str(page_num))
    status = first_request.status

    while status == 200:
            resp = await session.get(url + str(page_num))
            status = resp.status
            page_num += 1
            if status == 200:
                svg_array.append(await resp.read())
    await session.close()
    return svg_array
