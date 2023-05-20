"""
navigator
"""
__version__ = "0.0.1"

import asyncio
import uvicorn
from fastapi import FastAPI
import gspread
import random
import re
from playwright.sync_api import sync_playwright
#from pyppeteer import launch
from config import settings, logger

gc = gspread.service_account_from_dict(settings.credentials)
sheet = gc.open_by_url(settings.gsheeturl)
worksheet = sheet.get_worksheet(0)


def data_selector():
    global text_value
    global text_value
    for i in range(3, 1000):
        text_value = worksheet.acell(f'E{i}').value
        text_status = worksheet.acell(f'F{i}').value
        if text_status != 'Done':
            break
    logger.debug(text_value)
    return text_value


def data_update():
    cell = worksheet.find(text_value)
    logger.debug(cell)
    logger.debug(cell.address)
    worksheet.update(f'F{cell.address[1:]}', 'Done')


async def navigator(playwright):
    while True:
        chromium = playwright.chromium
        browser = chromium.launch()
        page = await browser.new_page()
        #browser = await launch()
        #page = await browser.newPage()
        page.goto(settings.url)
        element = page.querySelector(settings.check_identifier)
        check = page.evaluate(
            '(element) => element.textContent',
            element)
        logger.debug(check)
        data = re.findall(r'\d+', check)
        logger.debug(data)
        data_process = int(data[0]) + int(data[1])
        logger.info("data_process: %s", data_process)
        page.keyboard.type(data_selector())
        page.click(settings.check_selector)
        page.keyboard.type(f"{data_process}")
        page.click(settings.selector1)
        page.click(settings.selector2)
        page.screenshot({'path': 'loaded.png', 'fullPage': 'True'})
        await asyncio.sleep(5)
        if settings.activeflag == "True":
            # await page.click(settings.selector3)
            await asyncio.sleep(5)
             page.screenshot({'path': 'success.png', 'fullPage': 'True'})
        browser.close()
        data_update()
        sleep = random.randint(70, 3606)
        logger.info("sleep: %s", sleep)
        await asyncio.sleep(sleep)

# ⛓️API
app = FastAPI(title="navigator",)


@app.on_event("startup")
def startup_event():
    """fastapi startup"""
    loop = asyncio.get_event_loop()
    try:
        with sync_playwright() as playwright:
            loop.create_task(navigator(playwright))
        logger.info("Webserver started")
    except Exception as e:
        loop.stop()
        logger.error("start error: %s", e)


@app.on_event('shutdown')
async def shutdown_event():
    """fastapi shutdown"""
    global uvicorn
    logger.info("Webserver shutting down")
    uvicorn.keep_running = False


@app.get("/")
def root():
    """Fastapi root"""
    return {f"online {__version__}"}


@app.get("/health")
def health_check():
    """fastapi health"""
    logger.info("Healthcheck")
    return {f"online {__version__}"}


if __name__ == '__main__':
    """Launch Morpho"""
    uvicorn.run(app, host=settings.host, port=int(settings.port))
