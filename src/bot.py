"""
navigator
"""
__version__ = "0.0.0"

import asyncio
import uvicorn
from fastapi import FastAPI
import gspread

from pyppeteer import launch
from config import settings, logger

# gc = gspread.service_account()
# sht1 = gc.open_by_key(settings.gsheetkey)
# val = worksheet.get('E2').first()

async def navigator():
    while True:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(settings.url)
        content = await page.evaluate('document.body.textContent', force_expr=False)
        data = content[1997:2005]
        # await page.click(settings.check_identifier)
        data = data.split('+')
        data_process = int(data[0]) + int(data[1])
        logger.debug(data_process)
        
        await page.keyboard.type(settings.text)
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')

        await page.keyboard.type(f"{data_process}")

        await page.click(settings.selector1)
        await page.screenshot({'path': 'loaded.png','fullPage': 'True'})
        await asyncio.sleep(5)
        await page.click(settings.selector2)
        await asyncio.sleep(5)
        await page.screenshot({'path': 'success.png','fullPage': 'True'})
        await browser.close()
        await asyncio.sleep(7200)

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
    """Launch Talky"""
    uvicorn.run(app, host=settings.host, port=int(settings.port))
    