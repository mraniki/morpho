"""
navigator
"""
__version__ = "0.1.6"

import asyncio
import uvicorn
from fastapi import FastAPI
import gspread
from gspread import BackoffClient
import random
import re
from playwright.async_api import async_playwright
from config import settings, logger

gc = gspread.service_account_from_dict(
    settings.credentials,
    client_factory=BackoffClient)
sheet = gc.open_by_url(settings.gsheeturl)
worksheet = sheet.get_worksheet(0)


def data_selector():
    global text_value
    global text_value
    try:
        logger.info("Searching Text")
        for i in range(3, 1000):
            text_value = worksheet.acell(f'E{i}').value
            text_status = worksheet.acell(f'F{i}').value
            if text_status != 'Done':
                if text_value != '#ERROR!':
                    break
        logger.info("Text selected: %s", text_value)
        return text_value
    except Exception as e:
        logger.error("data_selector issue: %s", e)


def data_update():
    try:
        logger.info("Spreasheet to be updated")
        cell = worksheet.find(text_value)
        worksheet.update(f'F{cell.address[1:]}', 'Done')
        logger.info("Spreasheet updated")
    except Exception as e:
        logger.error("data_update issue: %s", e)
        pass


async def navigator():
    while True:
        async with async_playwright() as playwright:

            chromium = playwright.chromium
            browser = await chromium.launch()
            page = await browser.new_page()
            await page.goto(settings.url)
            element = await page.query_selector(settings.check_identifier)
            check = await page.evaluate(
                '(element) => element.textContent',
                element)
            logger.debug(check)
            data = re.findall(r'\d+', check)
            logger.info(data)
            data_process = int(data[0]) + int(data[1])
            logger.info("Control: %s", data_process)
            input = data_selector()
            await page.keyboard.type(input)
            logger.info("Text captured")
            await page.locator(settings.check_selector).click()
            await page.keyboard.type(f"{data_process}")
            logger.info("check captured")
            await page.locator(settings.selector1).click()
            await page.locator(settings.selector2).click()
            logger.info("checkbox captured")
            await page.screenshot(path="loaded.png", full_page=True)
            await asyncio.sleep(5)
            try:
                if settings.activeflag == "True":
                    logger.info("Submitting")
                    await page.locator(settings.selector3).click()
                    await asyncio.sleep(5)
                    await page.screenshot(path="success.png", full_page=True)
                    data_update()
                    logger.info("Submit Done")
                    await browser.close()
                else:
                    logger.info("skipping submission")
                sleep = random.randint(settings.sleeping_low, settings.sleeping_high)
                logger.info("sleeping: %s", sleep)
                await asyncio.sleep(sleep)
            except Exception as e:
                logger.error("Bot issue: %s", e)

# ⛓️API
app = FastAPI(title="navigator",)


@app.on_event("startup")
def startup_event():
    """fastapi startup"""
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(navigator())
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
