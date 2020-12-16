# -*- coding: utf-8 -*-
import time
import MD6470 as MD
global open_limit # 割
global open_now 
global difference # movementを実行する回数
open_now = 0 # 割


def stopStat(timeOut): 
    sTime = time.time()
    while True:
        try:
            statMD = (MD.getStatus(0) |MD.getStatus(1))
            if not(statMD & 0x0060):        # if both motor STOP, exit
                sStat = True
                break
            elif time.time() - sTime > timeOut:
                sStat = False
                break
        except KeyboardInterrupt:
            sStat = False
            break
    return sStat


def open(open_limit):
    print(open_now)
    difference = open_limit - open_now
    movement(difference)
    return open_limit


def close():
    movement(-10)


def movement(difference):
    print(difference)
    MD.open()        # ドライバー設定
    MD.resetDevice(2)    #　初期化
    time.sleep(0.1)
    MD.setKval(2, 0x29, 0x29, 0x29, 0x29)    # トルクコントロールパラメー
    MD.setMoveVal(2, 0x1A, 0x1A, 0x14, 0x00, 0x027)    #モーションパラメータ設定
    sSpd = 13333    # sSpd = 1回転/sec = 1.0 * 200step  / 0.015step/s = 13,333
    sStp = 25600    # 1回転 = 200 * 128 = 25,600 steps
    
    MD.resetAbsPos(2)    # ２台同時、絶対位置リセット
    MD.goToAbsPos(2,15059*difference)    #15059で10cm
    if stopStat(5.0):
        print("Stopped after goToDirAbsPos")
        
    MD.close()    # ドライバーの設定解除


def main():
    #open_now = open(5)
    #print(open_now)
    close()


if __name__ == '__main__':
    main()
