//=============================================================================
// main.js
//=============================================================================

"use strict";

function main() {
    const path = require("path");
    const { app, BrowserWindow, Menu } = require("electron");

    // Keep a global reference of the window object, if you don't, the window will
    // be closed automatically when the JavaScript object is garbage collected.
    let mainWindow;

    function createWindow() {
        // Create the browser window.
        mainWindow = new BrowserWindow({
            width: 816,
            height: 624,
            webPreferences: {
                nodeIntegration: true,
                contextIsolation: false
            }
        });

        // and load the index.html of the app.
        mainWindow.loadFile("index.html");

        // Emitted when the window is closed.
        mainWindow.on("closed", function() {
            // Dereference the window object, usually you would store windows
            // in an array if your app supports multi windows, this is the time
            // when you should delete the corresponding element.
            mainWindow = null;
        });
    }

    // This method will be called when Electron has finished
    // initialization and is ready to create browser windows.
    // Some APIs can only be used after this event occurs.
    app.on("ready", createWindow);

    // Quit when all windows are closed.
    app.on("window-all-closed", function() {
        // On OS X it is common for applications and their menu bar
        // to stay active until the user explicitly quits with Cmd + Q
        if (process.platform !== "darwin") {
            app.quit();
        }
    });

    app.on("activate", function() {
        // On OS X it's common to re-create a window in the app when the
        // dock icon is clicked and there are no other windows open.
        if (mainWindow === null) {
            createWindow();
        }
    });
}

if (typeof process === "object") {
    // Node.js detected
    main();
} else {
    // Browser detected
    const { Graphics, Utils, DataManager } = window;
    
    window.addEventListener("DOMContentLoaded", () => {
        Utils.isNwjs = () => false;
        Utils.isMobileDevice = () => false;
        
        Graphics.initialize();
        Graphics.boxWidth = 816;
        Graphics.boxHeight = 624;
        Graphics.setLoadingImage("img/system/Loading.png");
        
        DataManager.loadDatabase();
        Scene_Boot.prototype.start.call(new Scene_Boot());
    });
}