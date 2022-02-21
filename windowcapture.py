import pyautogui
import numpy as np
import cv2 as cv
import time
import random


class Cycle:
    def __init__(self):
        pass

    def screenshot(needle):
        shot = pyautogui.screenshot()
        open_cv_image = np.array(shot)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        needle_img = cv.imread(needle, cv.IMREAD_UNCHANGED)
        needle_result = cv.matchTemplate(open_cv_image, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(needle_result)
        return max_loc

    def right_click(max_loc):
        pyautogui.moveTo(
            x=max_loc[0] + random.randrange(5, 10),
            y=max_loc[1] + random.randrange(5, 10),
        )
        time.sleep(1)
        pyautogui.click(button="right")
        time.sleep(1)

    def left_click(max_loc):
        pyautogui.moveTo(
            x=max_loc[0] + random.randrange(5, 10),
            y=max_loc[1] + random.randrange(5, 10),
        )
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

    def double_click(max_loc):
        pyautogui.moveTo(
            x=max_loc[0] + random.randrange(5, 10),
            y=max_loc[1] + random.randrange(5, 10),
        )
        time.sleep(1)
        pyautogui.click(clicks=2)
        time.sleep(10)

    #######################################
    ####      EVE SPECIFIC       ####
    ######################################
    # MISC
    def open_hangar():
        time.sleep(5)
        print("Opening Hangar")
        item_hangar = False
        while item_hangar == False:
            time.sleep(5)
            if Cycle.if_needle("item_hangar.png") < 0.9:
                print("False")
                with pyautogui.hold("alt"):
                    pyautogui.press("c")
            else:
                print("True")
                item_hangar = True
                max_loc = Cycle.screenshot("item_hangar.png")
                Cycle.left_click(max_loc)
                time.sleep(10)

    def open_cargohold():
        time.sleep(5)
        print("Opening Cargohold")
        max_loc = Cycle.screenshot("cargohold.png")
        Cycle.left_click(max_loc)
        time.sleep(10)

    def move_to_cargo(needle):
        time.sleep(5)
        print("Moving to Cargo")
        max_loc = Cycle.screenshot(needle)
        pyautogui.moveTo(x=max_loc[0] + 10, y=max_loc[1] + 10)
        time.sleep(1)

        max_loc = Cycle.screenshot("cargohold.png")
        x = max_loc[0] + 10
        y = max_loc[1] + 10
        pyautogui.dragTo(x, y, 2, button="left")
        time.sleep(10)

    def move_to_container(needle, location):
        time.sleep(5)
        print("Moving to Container")
        Cycle.open_cargohold()
        max_loc = Cycle.screenshot(needle)
        pyautogui.moveTo(x=max_loc[0] + 10, y=max_loc[1] + 10)
        time.sleep(1)

        max_loc = Cycle.screenshot(location)
        x = max_loc[0] + 10
        y = max_loc[1] + 10
        pyautogui.dragTo(x, y, 2, button="left")
        time.sleep(5)

    def if_needle(needle):
        time.sleep(5)
        shot = pyautogui.screenshot()
        open_cv_image = np.array(shot)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        needle_img = cv.imread(needle, cv.IMREAD_UNCHANGED)
        needle_result = cv.matchTemplate(open_cv_image, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(needle_result)
        time.sleep(2)
        print(max_val)
        return max_val

    def loot_container():
        time.sleep(5)
        print("Looting Container")
        max_loc = Cycle.screenshot("container.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("open_cargo.png")
        Cycle.left_click(max_loc)
        loot = False
        while loot == False:
            time.sleep(1)
            if Cycle.if_needle("loot_all.png") > 0.9:
                loot = True
                max_loc = Cycle.screenshot("loot_all.png")
                Cycle.left_click(max_loc)
                time.sleep(10)

    def open_container():
        time.sleep(5)
        print("Opening Container")
        container = False
        while container == False:
            time.sleep(1)
            if Cycle.if_needle("container.png") > 0.9:
                container = True
                max_loc = Cycle.screenshot("container.png")
                Cycle.right_click(max_loc)
                max_loc = Cycle.screenshot("open_cargo.png")
                Cycle.left_click(max_loc)
                time.sleep(120)

    # TRAVEL
    def warp_to():
        time.sleep(5)
        print("Warping")
        warp_to = False
        while warp_to == False:
            time.sleep(1)
            if Cycle.if_needle("warp_to.png") > 0.9:
                warp_to = True
                max_loc = Cycle.screenshot("warp_to.png")
                Cycle.left_click(max_loc)
                time.sleep(60)

    def set_destination_blue():
        time.sleep(5)
        print("Setting Destination")
        set_destination = False
        while set_destination == False:
            time.sleep(1)
            if Cycle.if_needle("set_destination_blue.png") > 0.9:
                set_destination = True
                max_loc = Cycle.screenshot("set_destination_blue.png")
                Cycle.left_click(max_loc)
                time.sleep(1)

    def set_destination():
        time.sleep(5)
        print("Setting Destination")
        max_loc = Cycle.screenshot("set_destination.png")
        Cycle.left_click(max_loc)

    def jump():
        print("Jumping")
        jump = False
        while jump == False:
            time.sleep(1)
            if Cycle.if_needle("jump.png") > 0.9:
                jump = True
                max_loc = Cycle.screenshot("jump.png")
                Cycle.left_click(max_loc)

    def undock():
        time.sleep(5)
        print("Undocking")
        undock = False
        while undock == False:
            time.sleep(1)
            if Cycle.if_needle("undock.png") > 0.9:
                undock = True
                max_loc = Cycle.screenshot("undock.png")
                Cycle.left_click(max_loc)

    def undock_yellow():
        time.sleep(5)
        print("Undocking")
        max_loc = Cycle.screenshot("undock_yellow.png")
        Cycle.left_click(max_loc)

    def dock():
        time.sleep(5)
        print("Docking")
        dock = False
        while dock == False:
            time.sleep(1)
            if Cycle.if_needle("dock.png") > 0.9:
                dock = True
                time.sleep(10)
                max_loc = Cycle.screenshot("dock.png")
                Cycle.left_click(max_loc)

    def dock_rc():
        time.sleep(5)
        print("Docking")
        max_loc = Cycle.screenshot("dock_rc.png")
        Cycle.left_click(max_loc)

    def acceleration_gate():
        time.sleep(10)
        print("Taking Acceleration Gate")
        max_loc = Cycle.screenshot("acceleration_gate.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("activate_gate.png")
        Cycle.left_click(max_loc)
        max_loc = Cycle.screenshot("mwd.png")
        Cycle.left_click(max_loc)
        time.sleep(60)

    def approach():
        time.sleep(5)
        print("Approaching")
        max_loc = Cycle.screenshot("approach.png")
        Cycle.left_click(max_loc)
        max_loc = Cycle.screenshot("mwd.png")
        Cycle.left_click(max_loc)
        time.sleep(60)

    # AGENT INTERACTION
    def start_conversation():
        time.sleep(5)
        print("Starting Conversation")
        start_convo = False
        while start_convo == False:
            time.sleep(5)
            if Cycle.if_needle("start_conversation.png") > 0.65:
                start_convo = True
                max_loc = Cycle.screenshot("start_conversation.png")
                Cycle.left_click(max_loc)

    def accept():
        time.sleep(5)
        print("Accepting")
        accept = False
        while accept == False:
            time.sleep(2)
            if Cycle.if_needle("accept.png") > 0.65:
                accept = True
                max_loc = Cycle.screenshot("accept.png")
                Cycle.left_click(max_loc)

    def accept_remotely():
        time.sleep(5)
        print("Accepting")
        accept_remotely = False
        while accept_remotely == False:
            time.sleep(2)
            if Cycle.if_needle("accept_remotely.png") > 0.65:
                accept_remotely = True
                max_loc = Cycle.screenshot("accept_remotely.png")
                Cycle.left_click(max_loc)
                time.sleep(15)

    def request_mission():
        time.sleep(5)
        print("Requesting")
        request_mission = False
        while request_mission == False:
            time.sleep(2)
            if Cycle.if_needle("request_mission.png") > 0.65:
                request_mission = True
                max_loc = Cycle.screenshot("request_mission.png")
                Cycle.left_click(max_loc)
                time.sleep(5)

    def complete_mission():
        time.sleep(5)
        print("Completing")
        complete_mission = False
        while complete_mission == False:
            time.sleep(2)
            if Cycle.if_needle("complete_mission.png") > 0.65:
                complete_mission = True
                complete_mission = Cycle.screenshot("complete_mission.png")
                Cycle.left_click(complete_mission)
                time.sleep(5)

    def complete_remotely():
        time.sleep(5)
        print("Completing")
        complete_remotely = False
        while complete_remotely == False:
            time.sleep(1)
            if Cycle.if_needle("complete_remotely.png") > 0.65:
                complete_remotely = True
                complete_mission = Cycle.screenshot("complete_remotely.png")
                Cycle.left_click(complete_mission)
                time.sleep(15)

    # COMBAT
    def launch_em_drones():
        time.sleep(5)
        print("Launching Drones")
        max_loc = Cycle.screenshot("em_drones.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("launch_drones.png")
        Cycle.left_click(max_loc)
        time.sleep(5)

    def launch_kinetic_drones():
        time.sleep(5)
        print("Launching Drones")
        max_loc = Cycle.screenshot("kinetic_drones.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("launch_drones.png")
        Cycle.left_click(max_loc)
        time.sleep(5)

    def return_drones():
        time.sleep(5)
        print("Returning Drones")
        max_loc = Cycle.screenshot("local_space.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("return_drones.png")
        Cycle.left_click(max_loc)
        # Wait fro drones to return
        time.sleep(15)

    def autotarget():
        time.sleep(5)
        max_loc = Cycle.screenshot("autotarget.png")
        Cycle.left_click(max_loc)

    def frigate_target(needle):
        time.sleep(5)
        set_destination = False
        while set_destination == False:
            time.sleep(1)
            Cycle.approach_and_target("frigate_target.png")
            pyautogui.press("f")
            if Cycle.if_needle(needle) > 0.9:
                set_destination = True

    def approach_and_target(needle):
        time.sleep(5)
        max_loc = Cycle.screenshot(needle)
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("lock_target.png")
        Cycle.left_click(max_loc)
        max_loc = Cycle.screenshot(needle)
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("approach.png")
        Cycle.left_click(max_loc)

    ##########################################################################################      LOCATION SPECIFIC       ###
    #######################################################################################
    def manarq_jump():
        time.sleep(5)
        manarq = False
        while manarq == False:
            if Cycle.if_needle("manarq.png") > 0.8:
                time.sleep(90)
                manarq = True
        max_loc = Cycle.screenshot("manarq.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def manarq_set_destination():
        time.sleep(5)
        max_loc = Cycle.screenshot("manarq.png")
        Cycle.right_click(max_loc)
        max_loc = Cycle.screenshot("set_destination.png")
        Cycle.left_click(max_loc)

    def tar_jump():
        time.sleep(5)
        tar = False
        while tar == False:
            if Cycle.if_needle("tar.png") > 0.8:
                time.sleep(10)
                tar = True
        max_loc = Cycle.screenshot("tar.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def emsar_jump():
        time.sleep(5)
        emsar1 = False
        while emsar1 == False:
            if Cycle.if_needle("emsar1.png") > 0.8:
                time.sleep(10)
                emsar1 = True
        max_loc = Cycle.screenshot("emsar1.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def arnon_jump():
        time.sleep(5)
        arnon = False
        while arnon == False:
            if Cycle.if_needle("arnon.png") > 0.8:
                time.sleep(90)
                arnon = True
        max_loc = Cycle.screenshot("arnon.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def ourapheh_jump():
        time.sleep(5)
        ourapheh2 = False
        while ourapheh2 == False:
            if Cycle.if_needle("ourapheh2.png") > 0.8:
                time.sleep(10)
                ourapheh2 = True
        max_loc = Cycle.screenshot("ourapheh2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def botane_jump():
        time.sleep(5)
        botane = False
        while botane == False:
            if Cycle.if_needle("botane.png") > 0.8:
                time.sleep(10)
                botane = True
        max_loc = Cycle.screenshot("botane.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def dodixie_jump():
        time.sleep(5)
        dodixie = False
        while dodixie == False:
            if Cycle.if_needle("dodixie.png") > 0.8:
                time.sleep(10)
                dodixie = True
        max_loc = Cycle.screenshot("dodixie.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def athinard_jump():
        time.sleep(5)
        athinard = False
        while athinard == False:
            if Cycle.if_needle("athinard.png") > 0.8:
                time.sleep(10)
                athinard = True
        max_loc = Cycle.screenshot("athinard.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def ethernity_jump():
        time.sleep(5)
        ethernity = False
        while ethernity == False:
            if Cycle.if_needle("ethernity.png") > 0.8:
                time.sleep(10)
                ethernity = True
        max_loc = Cycle.screenshot("ethernity.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def harerget_jump():
        time.sleep(5)
        harerget = False
        while harerget == False:
            if Cycle.if_needle("harerget.png") > 0.8:
                time.sleep(90)
                harerget = True
        max_loc = Cycle.screenshot("harerget.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def claysson_jump():
        time.sleep(5)
        claysson = False
        while claysson == False:
            if Cycle.if_needle("claysson.png") > 0.8:
                time.sleep(10)
                claysson = True
        max_loc = Cycle.screenshot("claysson.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def stetille_jump():
        time.sleep(5)
        stetille = False
        while stetille == False:
            if Cycle.if_needle("stetille.png") > 0.8:
                time.sleep(10)
                stetille = True
        max_loc = Cycle.screenshot("stetille.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def adiere_jump():
        time.sleep(5)
        adiere = False
        while adiere == False:
            if Cycle.if_needle("adiere.png") > 0.8:
                time.sleep(10)
                adiere = True
        max_loc = Cycle.screenshot("adiere.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def auberulle_jump():
        time.sleep(5)
        auberulle = False
        while auberulle == False:
            if Cycle.if_needle("auberulle.png") > 0.8:
                time.sleep(10)
                auberulle = True
        max_loc = Cycle.screenshot("auberulle.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def unel_jump():
        time.sleep(5)
        unel = False
        while unel == False:
            if Cycle.if_needle("unel2.png") > 0.8:
                time.sleep(10)
                unel = True
        max_loc = Cycle.screenshot("unel2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def tennen_jump():
        time.sleep(5)
        tennen = False
        while tennen == False:
            if Cycle.if_needle("tennen.png") > 0.8:
                time.sleep(10)
                tennen = True
        max_loc = Cycle.screenshot("tennen.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def hatakani_jump():
        time.sleep(5)
        hatakani = False
        while hatakani == False:
            if Cycle.if_needle("hatakani.png") > 0.8:
                time.sleep(90)
                hatakani = True
        max_loc = Cycle.screenshot("hatakani.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def chainelant_jump():
        time.sleep(5)
        chainelant = False
        while chainelant == False:
            if Cycle.if_needle("chainelant.png") > 0.8:
                time.sleep(90)
                chainelant = True
        max_loc = Cycle.screenshot("chainelant.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def kassigainen_jump():
        time.sleep(5)
        kassigainen = False
        while kassigainen == False:
            if Cycle.if_needle("kassigainen.png") > 0.8:
                time.sleep(10)
                kassigainen = True
        max_loc = Cycle.screenshot("kassigainen.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def synchelle_jump():
        time.sleep(5)
        synchelle = False
        while synchelle == False:
            if Cycle.if_needle("synchelle.png") > 0.8:
                time.sleep(10)
                synchelle = True
        max_loc = Cycle.screenshot("synchelle.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def pakhshi_jump():
        time.sleep(5)
        pakhshi = False
        while pakhshi == False:
            if Cycle.if_needle("pakhshi.png") > 0.8:
                time.sleep(10)
                pakhshi = True
        max_loc = Cycle.screenshot("pakhshi.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def atlangeins_jump():
        time.sleep(5)
        atlangeins = False
        while atlangeins == False:
            if Cycle.if_needle("atlangeins.png") > 0.8:
                time.sleep(90)
                atlangeins = True
        max_loc = Cycle.screenshot("atlangeins.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def laurvier_jump():
        time.sleep(5)
        laurvier = False
        while laurvier == False:
            if Cycle.if_needle("laurvier.png") > 0.8:
                time.sleep(10)
                laurvier = True
        max_loc = Cycle.screenshot("laurvier.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def attyn_jump():
        time.sleep(5)
        attyn = False
        while attyn == False:
            if Cycle.if_needle("attyn.png") > 0.8:
                time.sleep(90)
                attyn = True
        max_loc = Cycle.screenshot("attyn.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def renyn_jump():
        time.sleep(5)
        renyn = False
        while renyn == False:
            if Cycle.if_needle("renyn.png") > 0.8:
                time.sleep(10)
                renyn = True
        max_loc = Cycle.screenshot("renyn.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def du_annes_jump():
        time.sleep(5)
        du_annes = False
        while du_annes == False:
            if Cycle.if_needle("du_annes.png") > 0.8:
                time.sleep(10)
                du_annes = True
        max_loc = Cycle.screenshot("du_annes.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def balle_jump():
        time.sleep(5)
        balle = False
        while balle == False:
            if Cycle.if_needle("balle2.png") > 0.8:
                time.sleep(10)
                balle = True
        max_loc = Cycle.screenshot("balle2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def aufay_jump():
        time.sleep(5)
        aufay = False
        while aufay == False:
            if Cycle.if_needle("aufay.png") > 0.8:
                time.sleep(10)
                aufay = True
        max_loc = Cycle.screenshot("aufay.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def deltole_jump():
        time.sleep(5)
        deltole = False
        while deltole == False:
            if Cycle.if_needle("deltole2.png") > 0.8:
                time.sleep(10)
                deltole = True
        max_loc = Cycle.screenshot("deltole2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def colelie_jump():
        time.sleep(5)
        colelie = False
        while colelie == False:
            if Cycle.if_needle("colelie.png") > 0.8:
                time.sleep(10)
                colelie = True
        max_loc = Cycle.screenshot("colelie.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def bei_jump():
        time.sleep(5)
        bei = False
        while bei == False:
            if Cycle.if_needle("bei2.png") > 0.8:
                time.sleep(10)
                bei = True
        max_loc = Cycle.screenshot("bei2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def uttindar_jump():
        time.sleep(5)
        uttindar = False
        while uttindar == False:
            if Cycle.if_needle("uttindar.png") > 0.8:
                time.sleep(10)
                uttindar = True
        max_loc = Cycle.screenshot("uttindar.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def hek_jump():
        time.sleep(5)
        hek = False
        while hek == False:
            if Cycle.if_needle("hek.png") > 0.8:
                time.sleep(90)
                hek = True
        max_loc = Cycle.screenshot("hek.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def eystur_jump():
        time.sleep(5)
        eystur = False
        while eystur == False:
            if Cycle.if_needle("eystur.png") > 0.8:
                time.sleep(10)
                eystur = True
        max_loc = Cycle.screenshot("eystur.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def lustrevik_jump():
        time.sleep(5)
        lustrevik = False
        while lustrevik == False:
            if Cycle.if_needle("lustrevik.png") > 0.8:
                time.sleep(90)
                lustrevik = True
        max_loc = Cycle.screenshot("lustrevik.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def onga_jump():
        time.sleep(5)
        onga = False
        while onga == False:
            if Cycle.if_needle("onga2.png") > 0.8:
                time.sleep(10)
                onga = True
        max_loc = Cycle.screenshot("onga2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def gyng_jump():
        time.sleep(5)
        gyng = False
        while gyng == False:
            if Cycle.if_needle("gyng.png") > 0.8:
                time.sleep(10)
                gyng = True
        max_loc = Cycle.screenshot("gyng.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def frarn_jump():
        time.sleep(5)
        frarn = False
        while frarn == False:
            if Cycle.if_needle("frarn.png") > 0.8:
                time.sleep(10)
                frarn = True
        max_loc = Cycle.screenshot("frarn.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def rens_jump():
        time.sleep(5)
        rens = False
        while rens == False:
            if Cycle.if_needle("rens2.png") > 0.8:
                time.sleep(10)
                rens = True
        max_loc = Cycle.screenshot("rens2.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def odatrik_jump():
        time.sleep(5)
        odatrik = False
        while odatrik == False:
            if Cycle.if_needle("odatrik.png") > 0.8:
                time.sleep(10)
                odatrik = True
        max_loc = Cycle.screenshot("odatrik.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def jark_jump():
        time.sleep(5)
        jark = False
        while jark == False:
            if Cycle.if_needle("jark.png") > 0.8:
                time.sleep(10)
                jark = True
        max_loc = Cycle.screenshot("jark.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def sasta_jump():
        time.sleep(5)
        sasta = False
        while sasta == False:
            if Cycle.if_needle("sasta.png") > 0.8:
                time.sleep(10)
                sasta = True
        max_loc = Cycle.screenshot("sasta.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def tanoo_jump():
        time.sleep(5)
        tanoo = False
        while tanoo == False:
            if Cycle.if_needle("tanoo.png") > 0.8:
                time.sleep(90)
                tanoo = True
        max_loc = Cycle.screenshot("tanoo.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def lashesih_jump():
        time.sleep(5)
        lashesih = False
        while lashesih == False:
            if Cycle.if_needle("lashesih.png") > 0.8:
                time.sleep(10)
                lashesih = True
        max_loc = Cycle.screenshot("lashesih.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def lisudeh_jump():
        time.sleep(5)
        lisudeh = False
        while lisudeh == False:
            if Cycle.if_needle("lisudeh.png") > 0.8:
                time.sleep(90)
                lisudeh = True
        max_loc = Cycle.screenshot("lisudeh.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def trytedald_jump():
        time.sleep(5)
        trytedald = False
        while trytedald == False:
            if Cycle.if_needle("trytedald.png") > 0.8:
                time.sleep(10)
                trytedald = True
        max_loc = Cycle.screenshot("trytedald.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def ivar_jump():
        time.sleep(5)
        ivar = False
        while ivar == False:
            if Cycle.if_needle("ivar.png") > 0.8:
                time.sleep(10)
                ivar = True
        max_loc = Cycle.screenshot("ivar.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def ameinaka_jump():
        time.sleep(5)
        ameinaka = False
        while ameinaka == False:
            if Cycle.if_needle("ameinaka.png") > 0.8:
                time.sleep(10)
                ameinaka = True
        max_loc = Cycle.screenshot("ameinaka.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def arlulf_jump():
        time.sleep(5)
        arlulf = False
        while arlulf == False:
            if Cycle.if_needle("arlulf.png") > 0.8:
                time.sleep(10)
                arlulf = True
        max_loc = Cycle.screenshot("arlulf.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def alf_jump():
        time.sleep(5)
        alf = False
        while alf == False:
            if Cycle.if_needle("alf.png") > 0.8:
                time.sleep(10)
                alf = True
        max_loc = Cycle.screenshot("alf.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def illuin_jump():
        time.sleep(5)
        illuin = False
        while illuin == False:
            if Cycle.if_needle("illuin.png") > 0.8:
                time.sleep(10)
                illuin = True
        max_loc = Cycle.screenshot("illuin.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def hjortur_jump():
        time.sleep(5)
        hjortur = False
        while hjortur == False:
            if Cycle.if_needle("hjortur.png") > 0.8:
                time.sleep(10)
                hjortur = True
        max_loc = Cycle.screenshot("hjortur.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def evettullur_jump():
        time.sleep(5)
        evettullur = False
        while evettullur == False:
            if Cycle.if_needle("evettullur.png") > 0.8:
                time.sleep(10)
                evettullur = True
        max_loc = Cycle.screenshot("evettullur.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def tratokard_jump():
        time.sleep(5)
        tratokard = False
        while tratokard == False:
            if Cycle.if_needle("tratokard.png") > 0.8:
                time.sleep(10)
                tratokard = True
        max_loc = Cycle.screenshot("tratokard.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def getugaud_jump():
        time.sleep(5)
        getugaud = False
        while getugaud == False:
            if Cycle.if_needle("getugaud.png") > 0.8:
                time.sleep(10)
                getugaud = True
        max_loc = Cycle.screenshot("getugaud.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def josekorn_jump():
        time.sleep(5)
        josekorn = False
        while josekorn == False:
            if Cycle.if_needle("josekorn.png") > 0.8:
                time.sleep(10)
                josekorn = True
        max_loc = Cycle.screenshot("josekorn.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def nifflung_jump():
        time.sleep(5)
        nifflung = False
        while nifflung == False:
            if Cycle.if_needle("nifflung.png") > 0.8:
                time.sleep(10)
                nifflung = True
        max_loc = Cycle.screenshot("nifflung.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def hakeri_jump():
        time.sleep(5)
        hakeri = False
        while hakeri == False:
            if Cycle.if_needle("hakeri.png") > 0.8:
                time.sleep(10)
                hakeri = True
        max_loc = Cycle.screenshot("hakeri.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def irgrus_jump():
        time.sleep(5)
        irgrus = False
        while irgrus == False:
            if Cycle.if_needle("irgrus.png") > 0.8:
                time.sleep(10)
                irgrus = True
        max_loc = Cycle.screenshot("irgrus.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def tolle_jump():
        time.sleep(5)
        tolle = False
        while tolle == False:
            if Cycle.if_needle("tolle.png") > 0.8:
                time.sleep(10)
                tolle = True
        max_loc = Cycle.screenshot("tolle.png")
        Cycle.right_click(max_loc)
        Cycle.jump()

    def aydoteaux_jump():
        time.sleep(5)
        aydoteaux = False
        while aydoteaux == False:
            if Cycle.if_needle("aydoteaux.png") > 0.8:
                time.sleep(90)
                aydoteaux = True
        max_loc = Cycle.screenshot("aydoteaux.png")
        Cycle.right_click(max_loc)
        Cycle.jump()
