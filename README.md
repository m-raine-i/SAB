#SAB

1. open cmd to install packages
2. type 'pip install gtts'
3. type 'pip install playsound==1.2.2 (this is vv important para basahin niya yung -audio.mp3)'
4. type 'pip install speechrecognition"

# installing pyaudio:
Option 1: type 'pip install pyaudio'
#
Try niyo muna i-run yung code para ma-check kung working ang pyaudio na na-install. Malalaman niyo na nag-work pag ni-run and nag-respond si SAB with audio. 'Yung nangyari sakin 'di nagsasalita si SAB pero sumasagot siya sa tanong sa terminal (VS Code).
#
Option 2: If it didn't work, need mag-download muna ng pyaudio wheel file (https://www.lfd.uci.edu/~gohlke/pythonlibs/) in my case, PyAudio-0.2.11-cp310-cp310-win_amd64.whl worked for me. So if nag-error sa inyo, try to download other versions.
#
after downloading, lagay niyo sa folder same with this MAIN2.PY and then type niyo sa cmd yung location ng wheel file. In my case, it's 'dir Downloads' and then 'dir vitual assistant' and then 'pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl', dito muna I navigated the wheel file kasi 'di siya magi'install pag 'di mo binuksan 'yung folder kung saan mo nilagay yung wheel file. After installing, there should be no other errors here. After this, you're good to go.
#
# other ideas what to put in chap 4-5
  record the delay of response or time of response
  #
  estimated power usage everyday, every month or annually
  #
  how many questions can SAB accomodate
  #
  how many ppl can SAB accomodate
  #
  how many languages can SAB use
  #
  chap 4 ilalagay kung saan siya ilalagay. In our case, we agreed to placing SAB in the registrar's office.
