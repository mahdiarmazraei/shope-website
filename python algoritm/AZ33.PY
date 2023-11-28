<!doctype html>
<html>
    <head>
        <title>BingX-Ethereum Contract Trading | Derivatives Trading</title>
        <meta data-n-head="1" charset="utf-8">
        <meta data-n-head="1" name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
        <meta data-n-head="1" data-hid="dns-prefetch" http-equiv="x-dns-prefetch-control" content="on">
        <meta data-n-head="1" data-hid="X-UA-Compatible" http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta data-n-head="1" data-hid="format-detection" name="format-detection" content="telephone=no">
        <meta data-n-head="1" data-hid="apple-mobile-web-app-capable" name="apple-mobile-web-app-capable" content="yes">
        <meta data-n-head="1" data-hid="apple-mobile-web-app-status-bar-style" name="apple-mobile-web-app-status-bar-style" content="black">
        <link data-n-head="1" rel="preconnect" href="https://api-app.qq-os.com" crossorigin="true">
        <link data-n-head="1" rel="preconnect" href="https://fpnpmcdn.net" crossorigin="true">
        <link data-n-head="1" rel="preconnect" href="https://use1.fptls.com" crossorigin="true">
        <link data-n-head="1" rel="preconnect" href="https://fp.bingx.com" crossorigin="true">
        <link data-n-head="1" rel="dns-prefetch" href="https://bin.bb-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="https://api-app.qq-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="https://api-app.bit-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="wss://ws-app.qq-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="wss://ws-app.bit-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="wss://ws-spot.qq-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="wss://ws-spot.bit-os.com">
        <link data-n-head="1" rel="dns-prefetch" href="https://static-app.bingx.com">
        <link data-n-head="1" rel="dns-prefetch" href="https://arms-retcode-sg-aliyuncs.com">
        <link data-n-head="1" rel="dns-prefetch" href="https://bb-client.log-global.aliyuncs.com">
        <link data-n-head="1" rel="favicon" type="image/x-icon" href="https://bin.bb-os.com/favicon.png">
        <script data-n-head="1" data-hid="gtm-script">
            if (!window._gtm_init) {
                window._gtm_init = 1;
                (function(w, n, d, m, e, p) {
                    w[d] = (w[d] == 1 || n[d] == 'yes' || n[d] == 1 || n[m] == 1 || (w[e] && w[e][p] && w[e][p]())) ? 1 : 0
                }
                )(window, navigator, 'doNotTrack', 'msDoNotTrack', 'external', 'msTrackingProtectionEnabled');
                (function(w, d, s, l, x, y) {
                    w[x] = {};
                    w._gtm_inject = function(i) {
                        if (w.doNotTrack || w[x][i])
                            return;
                        w[x][i] = 1;
                        w[l] = w[l] || [];
                        w[l].push({
                            'gtm.start': new Date().getTime(),
                            event: 'gtm.js'
                        });
                        var f = d.getElementsByTagName(s)[0]
                          , j = d.createElement(s);
                        j.crossOrigin = 'true';
                        j.defer = true;
                        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + '&gtm_auth=eksEGPDft-66AUhHYSpj1Q&gtm_preview=env-22&gtm_cookies_win=x';
                        f.parentNode.insertBefore(j, f);
                    }
                }
                )(window, document, 'script', 'dataLayer', '_gtm_ids', '_gtm_inject')
            }
        </script>
        <link href="https://bin.bb-os.com/_nuxt/css/52b58e3.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/0c6d038.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/c465067.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/17009d3.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/c0e3c8f.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/5bbc4f0.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/4e3e20c.css" rel="stylesheet" crossorigin="anonymous">
        <link href="https://bin.bb-os.com/_nuxt/css/3430cb4.css" rel="stylesheet" crossorigin="anonymous">
    </head>
    <body>
        <noscript data-n-head="1" data-hid="gtm-noscript" data-pbody="true">
            <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PTSTFV8&gtm_auth=eksEGPDft-66AUhHYSpj1Q&gtm_preview=env-22&gtm_cookies_win=x" height="0" width="0" style="display:none;visibility:hidden" title="gtm"></iframe>
        </noscript>
        <div id="__nuxt">
            <div class="bx-global-indicator" id="bx-page-indicator">
                <div class="bx-global-loading-box">
                    <div class="bx-global-svg"></div>
                </div>
            </div>
            <style>
                .bx-global-indicator {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    z-index: 9999;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #fff;
                }

                .bx-global-indicator.dark {
                    background-color: #000;
                }

                .bx-global-loading-box {
                    width: fit-content;
                    padding: 16px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    border-radius: 6px;
                    background-color: #f4f5f6;
                }

                .bx-global-indicator.dark .bx-global-loading-box {
                    background-color: #141519;
                }

                @media screen and (max-width: 750px) {
                    .bx-global-loading-box {
                        padding: 0;
                    }
                }

                .bx-global-svg {
                    width: 40px;
                    height: 40px;
                    background-image: url('https://static-app.bb-os.com/fe-common/assets/imgs/logo-light.svg');
                    background-repeat: no-repeat;
                    background-size: cover;
                }

                .bx-global-indicator.dark .bx-global-svg {
                    background-image: url('https://static-app.bb-os.com/fe-common/assets/imgs/logo-dark.svg');
                }

                @media screen and (max-width: 750px) {
                    .bx-global-svg {
                        width: 48px;
                        height: 48px;
                    }
                }
            </style>
            <script>
                function _getCookie(name) {
                    var nameEQ = name + "=";
                    var ca = document.cookie.split(';');
                    for (var i = 0; i < ca.length; i++) {
                        var c = ca[i];
                        while (c.charAt(0) == ' ')
                            c = c.substring(1, c.length);
                        if (c.indexOf(nameEQ) == 0)
                            return c.substring(nameEQ.length, c.length);
                    }
                    return null;
                }
                function _initTheme() {
                    var _theme = _getCookie('theme') || 'light';
                    var _el = document.getElementById('bx-page-indicator');
                    try {
                        _el.classList.add(_theme);
                    } catch (e) {
                        console.log(e)
                    }
                }
                _initTheme();
            </script>
        </div>
        <script>
            window.__NUXT__ = (function(a) {
                return {
                    config: {
                        ENV: "production",
                        SENTRY_DEBUG: false,
                        SENTRY_DSN: "https:\u002F\u002F066d70241c7c25ec7f87a5a15087d833@front-log.great-api.com\u002F3",
                        SENTRY_ENVIRONMENT: "prod",
                        SENTRY_RELEASE: "4.73.13-prod",
                        _app: {
                            basePath: a,
                            assetsPath: a,
                            cdnURL: "https:\u002F\u002Fbin.bb-os.com\u002F_nuxt\u002F"
                        }
                    }
                }
            }("\u002F"))
        </script>
        <script src="https://bin.bb-os.com/_nuxt/0968716.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/b890be2.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/81f0864.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/ae24be9.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/c2e3ea0.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/026fc62.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/95f6b2b.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/731f459.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/f35b835.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/05597ff.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/bc22528.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/ca85649.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/cb0b125.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/a65148d.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/405e65a.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/2a27808.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/776d6ab.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/e09adf2.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/ecabcbd.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/00ea77a.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/610416f.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/a72baf9.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/565a5b6.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/df407ba.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/7d1b37b.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/0b08374.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/6624779.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/a889ad3.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/904e53b.js" crossorigin="anonymous"></script>
        <script src="https://bin.bb-os.com/_nuxt/143f0fc.js" crossorigin="anonymous"></script>
    </body>
</html>

