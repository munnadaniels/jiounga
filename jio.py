a
    ?Зa.(  ?                   @   s  d dl mZ d dlZd dlZd dlZd dlZd dlZd dlZd dlZe	Z
ej?e
?Zej?e?Zej?e?Zed Zed Zed Zed Zed Zed Zed	 Zed
 Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Ze dk?rz
e?  W n$ e!?y   e"d? e?#?  Y n0 dS )?    )?unicode_literalsNz/binaries/aria2c.exez/binaries/yt-dlp.exez/binaries/mkvmerge.exez/outputz/tempz/temp/video.mp4z/temp/subtitle.srtz/output/c                 C   s"  |}|| d | d }|? dd?? dd?? dd?? d	d?? d
d?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? dd?? d d?? d!d?? d"d?? d#d?}t|? t?t| d$d%d&d'd(d)d*td+|g? td,? d S )-N?.?.JIO.WEB-DL.H.264-SKS.mp4?mp4?mkv?132?130p?248?240p?300?464?696?360p?896?480p?1328?720p?2492?4192?1080p?8192?12192?15192?2160p?18192Z232Z448?864?6192Z1728Z2428Z3128Z4128Z6128Z8128Z9192?--max-connection-per-server=16?--max-tries=0?--summary-interval=0?--console-log-level=error?--allow-overwrite=true?--download-result=hide?--dir?-oz
Done .....)?replace?print?
subprocess?run?	aria2cexe?output)?mp4url?name?se?qual?number?new_name?old_name? r2   ?jio.py?TB   sf    N??????????????????
r4   c                 C   s?  ?z?|? d?}|d }|}|dk?r`d| d | d }|?dd??d	d??d
d??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd?}t|? t?t|dddd d!d"td#d$g? t?t| ddd%d&dd!d"td#d'g? td(? t?td)d*d+d,t| d-d.d/d0d1d2t	d-d.d3d4t
g? td5? t?t	? t?t
? td6? ?n8d| d | d }|?dd??d	d??d
d??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd?}t|? t?t|dddd d!d"td#d$g? t?t| ddd%d&dd!d"td#d'g? td(? t?td)d*d+d,t| d-d.d/d0d1d2t	d-d.d3d4t
g? td5? t?t	? t?t
? td6? W n?   |}t|? d| d | d7 }|?d8d9??dd??d	d??d
d??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd??dd?}t|? t?t| ddd%d&dd!d"td#|g? td6? Y n0 d S ):N?_?   Zeng? r   z.JIO.WEB-DL.H.264.Esub-SKS.mkvZ112r   r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r!   z--quiet=truer"   r#   r$   zsubtitle.srtr   r    z	video.mp4z
Merging .....?--quietz--ui-language?enz--outputz
--languagez0:engz--default-trackz0:yesz--compressionz0:nonez--track-orderz0:0,1:0,2:0,3:0,4:0z
Deleting temp files.....z
All Done .....r   r   r   )?splitr%   r&   r'   r(   r)   ?temp?mkvmergeexe?direc?invideo?insub?os?remover*   )r+   r,   r.   ?suburlZsubt?langr1   r0   r2   r2   r3   ?Ran+   s?    

|?	?
2

|?	?
2

??
rD   c                 C   s?   ddi}t jd|  d | |d??? }|d d d ?d	d
?}|d }|d d d ?d?d }|d d d ?d?}|d d d }d|d  d |d  d | d }	t?tdd|	dg? td? t	t
d??}
t| |
|? d S )Nr@   ?iOS?7https://prod.media.jio.com/apis/common/v3/metamore/get/?/??headers?episodesr   r,   ?.mp4r7   ?subtitle?|?thumb?idz3http://jiobeats.cdn.jio.com/vod/_definst_/smil:vod/r6   ?   ?.smil/index.m3u8r8   ?--no-warnings?-F??
Quality Codes: 112=130p, 132=130p, 248=240p, 300=240p, 464=240p, 696=360p, 896=480p, 1328=720p, 2492=720p, 4192=1080p, 6192=1080p, 8192=1080p, 12192=1080p, 15192=2160p, 18192=2160pz/
Please Select Quality From Availale Streams : )?requests?get?jsonr%   r:   r'   r(   ?youtubedlexer&   ?str?input?	jio_serie)?	series_id?	seriesnumrI   ?metadatar,   ?seriesr-   ?date?ids?hls_urlr.   r2   r2   r3   ?
jio_series|   s,    ?
????rc   c                 C   s  ddi}t jd|  d | |d??? }tdt|d ??D ]?}|d | d ?d	d
?}|d | d ?d?d }|?dd
?}|d d d ?d?d }|d | d ?d?}	|d | d }
d}d| d |	d  d |	d  d |
 d | d	 }t|||||? q8d S )Nr@   rE   rF   rG   rH   r   rJ   r,   rK   r7   rL   rM   ??ZimagerO   ?sldhnecdnems02.cdnsrv.jio.com?https://?)/jiobeats.cdn.jio.com/content/entry/data/r6   r5   )rU   rV   rW   ?range?lenr%   r:   r4   )r\   r.   r]   rI   r^   ?ir,   r/   r-   r`   ra   ?mainurlr+   r2   r2   r3   r[   ?   s4    ?
??????r[   c                 C   s:  ddi}t jd|  |d??? }z|d }W n   td? d}Y n0 z$|d }d	}d
| d t|? }W n   g }td? Y n0 |d }|?d?}|d }	|d }
dt|	? d t|
? d |  d }t?tdd|dg? td? tt	d??}d	}d
| d t|	? d t|
? d |  d | d }t
||||? d S )Nr@   rE   rF   rH   r,   z
Name not found?outZsrtre   rf   rg   z
No subtitle foundrN   rG   r6   rP   z9http://jiobeats.cdn.jio.com/vod/_definst_/smil:vodpublic/rQ   r8   rR   rS   rT   z4
Please Enter Quality Codes From Availale Streams : r5   rK   )rU   rV   rW   r&   rY   r:   r'   r(   rX   rZ   rD   )Zmovie_idrI   r^   r,   ?subrk   rB   ?anyrO   ?f1?f2rb   r.   r+   r2   r2   r3   ?	jio_movie?   s2    

$4rq   c                  C   s?   d} t j| d?}|jdtdd? |jdtdd? |?? }|j}|j}d|v r`|?d	?}|d
 }n|}|dkr?ttd??}t	||? n|dkr?t
|? d S )Nz	Bigg Boss)?description?typezVideo type [series].)rs   ?help?linkzVideo [Link/id]rf   rG   ?   r_   z
 Please Enter Season Number: Zmovie)?argparse?ArgumentParser?add_argumentrY   ?
parse_argsrs   ru   r:   rZ   rc   rq   )rr   ?parser?argsZv_typeru   rO   r]   r2   r2   r3   ?main?   s     

r}   ?__main__z	Exiting..)$Z
__future__r   rU   ?sysr@   Zos.path?globrw   r'   ?__file__ZcurrentFile?path?realpathZrealPath?dirnameZdirPath?basenameZdirNamer)   rX   r<   r*   r;   r>   r?   r=   r4   rD   rc   r[   rq   r}   ?__name__?KeyboardInterruptr&   ?exitr2   r2   r2   r3   ?<module>   s>   Q

