/*
 * Konami-JS ~
 * :: Now with support for touch events and multiple instances for
 * :: those situations that call for multiple easter eggs!
 * Code: https://github.com/snaptortoise/konami-js
 * Copyright (c) 2009 George Mandis (georgemandis.com, snaptortoise.com)
 * Version: 1.6.2 (7/17/2018)
 * Licensed under the MIT License (http://opensource.org/licenses/MIT)
 * Tested in: Safari 4+, Google Chrome 4+, Firefox 3+, IE7+, Mobile Safari 2.2.1+ and Android
 */

// This code has been edited to remove the word "k o_n a'mi as much as possible"

var Mooncake = function (callback) {
    var mooncake = {
        addEvent: function (obj, type, fn, ref_obj) {
            if (obj.addEventListener)
                obj.addEventListener(type, fn, false);
            else if (obj.attachEvent) {
                // IE
                obj["e" + type + fn] = fn;
                obj[type + fn] = function () {
                    obj["e" + type + fn](window.event, ref_obj);
                }
                obj.attachEvent("on" + type, obj[type + fn]);
            }
        },
        removeEvent: function (obj, eventName, eventCallback) {
            if (obj.removeEventListener) {
                obj.removeEventListener(eventName, eventCallback);
            } else if (obj.attachEvent) {
                obj.detachEvent(eventName);
            }
        },
        input: "",
        pattern: "38384040373937396665",
        keydownHandler: function (e, ref_obj) {
            if (ref_obj) {
                mooncake = ref_obj;
            } // IE
            mooncake.input += e ? e.keyCode : event.keyCode;
            if (mooncake.input.length > mooncake.pattern.length) {
                mooncake.input = mooncake.input.substr((mooncake.input.length - mooncake.pattern.length));
            }
            if (mooncake.input === mooncake.pattern) {
                mooncake.code(mooncake._currentLink);
                mooncake.input = '';
                e.preventDefault();
                return false;
            }
        },
        load: function (link) {
            this._currentLink = link;
            this.addEvent(document, "keydown", this.keydownHandler, this);
            this.iphone.load(link);
        },
        unload: function () {
            this.removeEvent(document, 'keydown', this.keydownHandler);
            this.iphone.unload();
        },
        code: function (link) {
            window.location = link
        },
        iphone: {
            start_x: 0,
            start_y: 0,
            stop_x: 0,
            stop_y: 0,
            tap: false,
            capture: false,
            orig_keys: "",
            keys: ["UP", "UP", "DOWN", "DOWN", "LEFT", "RIGHT", "LEFT", "RIGHT", "TAP", "TAP"],
            input: [],
            code: function (link) {
                mooncake.code(link);
            },
            touchmoveHandler: function (e) {
                if (e.touches.length === 1 && mooncake.iphone.capture === true) {
                    var touch = e.touches[0];
                    mooncake.iphone.stop_x = touch.pageX;
                    mooncake.iphone.stop_y = touch.pageY;
                    mooncake.iphone.tap = false;
                    mooncake.iphone.capture = false;
                    mooncake.iphone.check_direction();
                }
            },
            touchendHandler: function () {
                mooncake.iphone.input.push(mooncake.iphone.check_direction());
                
                if (mooncake.iphone.input.length > mooncake.iphone.keys.length) mooncake.iphone.input.shift();
                
                if (mooncake.iphone.input.length === mooncake.iphone.keys.length) {
                    var match = true;
                    for (var i = 0; i < mooncake.iphone.keys.length; i++) {
                        if (mooncake.iphone.input[i] !== mooncake.iphone.keys[i]) {
                            match = false;
                        }
                    }
                    if (match) {
                        mooncake.iphone.code(mooncake._currentLink);
                    }
                }
            },
            touchstartHandler: function (e) {
                mooncake.iphone.start_x = e.changedTouches[0].pageX;
                mooncake.iphone.start_y = e.changedTouches[0].pageY;
                mooncake.iphone.tap = true;
                mooncake.iphone.capture = true;
            },
            load: function (link) {
                this.orig_keys = this.keys;
                mooncake.addEvent(document, "touchmove", this.touchmoveHandler);
                mooncake.addEvent(document, "touchend", this.touchendHandler, false);
                mooncake.addEvent(document, "touchstart", this.touchstartHandler);
            },
            unload: function () {
                mooncake.removeEvent(document, 'touchmove', this.touchmoveHandler);
                mooncake.removeEvent(document, 'touchend', this.touchendHandler);
                mooncake.removeEvent(document, 'touchstart', this.touchstartHandler);
            },
            check_direction: function () {
                x_magnitude = Math.abs(this.start_x - this.stop_x);
                y_magnitude = Math.abs(this.start_y - this.stop_y);
                x = ((this.start_x - this.stop_x) < 0) ? "RIGHT" : "LEFT";
                y = ((this.start_y - this.stop_y) < 0) ? "DOWN" : "UP";
                result = (x_magnitude > y_magnitude) ? x : y;
                result = (this.tap === true) ? "TAP" : result;
                return result;
            }
        }
    }

    typeof callback === "string" && mooncake.load(callback);
    if (typeof callback === "function") {
        mooncake.code = callback;
        mooncake.load();
    }

    return mooncake;
};


if (typeof module !== 'undefined' && typeof module.exports !== 'undefined') {
    module.exports = Mooncake;
} else {
    if (typeof define === 'function' && define.amd) {
        define([], function() {
            return Mooncake;
        });
    } else {
        window.Mooncake = Mooncake;
    }
}
