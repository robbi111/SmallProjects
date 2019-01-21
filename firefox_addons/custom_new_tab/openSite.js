let urlList = ["https://www.edn.com",
            "https://www.elektroniknet.de",
            "https://www.elektronikpraxis.vogel.de",
            "https://www.electronicsweekly.com",
            "https://www.eevblog.com"]

let urlName = "default"
urlName = urlList[Math.floor(Math.random() * urlList.length)]

window.open(urlName, "_self")