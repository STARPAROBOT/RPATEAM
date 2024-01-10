from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = AppiumOptions()
options.load_capabilities({
	"appium:deviceName": "192.168.25.6:35499",
	"platformName": "Android",
	"appium:appPackage": "com.samsungpop.android.mpop",
	"appium:appActivity": "com.samsungpop.phonelib.SSSmartActivity",
	#"appium:ensureWebviewsHavePages": True,
	#"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	#"appium:connectHardwareKeyboard": True
})


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

wait = WebDriverWait(driver, 20)
sleep(6)

