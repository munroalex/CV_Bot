from numpy.core.numerictypes import ScalarType
import cv2 as cv
import numpy as np
import pyautogui
import time
from windowcapture import Cycle


########################################################
###  Mission 1 - A Beacon Beckons  ***
########################################################
def m1_phase_1():
    if Cycle.if_needle("arnon_station.png") < 0.8:
        print("Incorrect Station")
        exit()
    sister_alitura = Cycle.screenshot("alitura.png")
    Cycle.double_click(sister_alitura)
    time.sleep(10)
    Cycle.accept()
    Cycle.manarq_set_destination()
    Cycle.undock()


def m1_phase_2():
    Cycle.emsar_jump()
    Cycle.manarq_jump()
    Cycle.warp_to()


def m1_phase_3():
    battleship_wreck = Cycle.screenshot("battleship_wreck.png")
    Cycle.right_click(battleship_wreck)
    Cycle.approach()


def m1_phase_4():
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m1():
    print("m1_phase_1")
    m1_phase_1()
    print("m1_phase_2")
    m1_phase_2()
    print("m1_phase_3")
    m1_phase_3()
    print("m1_phase_4")
    m1_phase_4()


########################################################
###  Mission 2 - Agent Enquiry  ***
########################################################
def m2_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.set_destination_blue()


def m2_phase_2():
    Cycle.tar_jump()
    Cycle.warp_to()
    Cycle.start_conversation()


def m2():
    print("m2_phase_1")
    m2_phase_1()
    print("m2_phase_2")
    m2_phase_2()


########################################################
###  Mission 3 - Of Interest ***
########################################################
def m3_phase_1():
    Cycle.accept()
    Cycle.set_destination_blue()
    Cycle.manarq_jump()
    Cycle.warp_to()


def m3_phase_2():
    Cycle.launch_em_drones()
    Cycle.autotarget()
    Cycle.frigate_target("set_destination_blue.png")
    Cycle.return_drones()


def m3_phase_3():
    Cycle.set_destination_blue()
    Cycle.tar_jump()
    Cycle.warp_to()


def m3_phase_4():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m3():
    print("m3_phase_1")
    m3_phase_1()
    print("m3_phase_2")
    m3_phase_2()
    print("m3_phase_3")
    m3_phase_3()
    print("m3_phase_4")
    m3_phase_4()


########################################################
###  Mission 4 - Retrieving Red ***
########################################################
def m4_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.warp_to()


def m4_phase_2():
    Cycle.launch_em_drones()
    Cycle.autotarget()
    Cycle.frigate_target("warp_to.png")
    Cycle.return_drones()


def m4_phase_3():
    Cycle.warp_to()


def m4_phase_4():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m4():
    print("m4_phase_1")
    m4_phase_1()
    print("m4_phase_2")
    m4_phase_2()
    print("m4_phase_3")
    m4_phase_3()
    print("m4_phase_4")
    m4_phase_4()


########################################################
###  Mission 5 - Alerting Alitura ***
########################################################
def m5_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.set_destination_blue()


def m5_phase_2():
    Cycle.manarq_jump()
    Cycle.emsar_jump()
    Cycle.arnon_jump()
    Cycle.dock()


def m5_phase_3():
    Cycle.start_conversation()


def m5():
    print("m5_phase_1")
    m5_phase_1()
    print("m5_phase_2")
    m5_phase_2()
    print("m5_phase_3")
    m5_phase_3()


########################################################
###  Mission 6 - Jet-Canning a Janitor ***
########################################################
def m6_phase_1():
    Cycle.accept()
    Cycle.undock()


def m6_phase_2():
    Cycle.warp_to()


def m6_phase_3():
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    Cycle.frigate_target("container.png")
    Cycle.return_drones()
    Cycle.loot_container()


def m6_phase_4():
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m6():
    print("m6_phase_1")
    m6_phase_1()
    print("m6_phase_2")
    m6_phase_2()
    print("m6_phase_3")
    m6_phase_3()
    print("m6_phase_4")
    m6_phase_4()


########################################################
###  Mission 7 - Chivvying a Chef ***
########################################################
def m7_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m7_phase_2():
    Cycle.warp_to()
    Cycle.loot_container()
    Cycle.dock()


def m7_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m7():
    print("m7_phase_1")
    m7_phase_1()
    print("m7_phase_2")
    m7_phase_2()
    print("m7_phase_3")
    m7_phase_3()


########################################################
###  Mission 8 - Delivering a Doctor ***
########################################################
def m8_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("ransom_money.png")
    Cycle.undock()


def m8_phase_2():
    Cycle.warp_to()
    Cycle.open_container()
    Cycle.open_cargohold()
    Cycle.move_to_container("ransom_money.png", "dead_drop.png")

    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()


def m8_phase_3():
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m8():
    print("m8_phase_1")
    m8_phase_1()
    print("m8_phase_2")
    m8_phase_2()
    print("m8_phase_3")
    m8_phase_3()


########################################################
###  Mission 9 - Engineering a Rescue ***
########################################################
def m9_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m9_phase_2():
    Cycle.warp_to()
    Cycle.loot_container()
    Cycle.dock()


def m9_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m9():
    print("m9_phase_1")
    m9_phase_1()
    print("m9_phase_2")
    m9_phase_2()
    print("m9_phase_3")
    m9_phase_3()


########################################################
###  Mission 10 - Going Gallente ***
########################################################
def m10_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m10_phase_2():
    Cycle.set_destination_blue()
    Cycle.emsar_jump()
    Cycle.manarq_jump()
    Cycle.ourapheh_jump()
    Cycle.botane_jump()
    Cycle.dodixie_jump()
    Cycle.athinard_jump()
    Cycle.ethernity_jump()
    Cycle.harerget_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m10():
    print("m10_phase_1")
    m10_phase_1()
    print("m10_phase_2")
    m10_phase_2()


########################################################
###  Mission 11 - Studying the Scene ***
########################################################
def m11_phase_1():
    Cycle.accept()
    Cycle.undock()


def m11_phase_2():
    Cycle.warp_to()
    Cycle.loot_container()
    Cycle.dock()


def m11_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m11():
    print("m11_phase_1")
    m11_phase_1()
    print("m11_phase_2")
    m11_phase_2()
    print("m11_phase_3")
    m11_phase_3()


########################################################
###  Mission 12 - Rendering Assistance ***
########################################################
def m12_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("antibiotics.png")
    time.sleep(3)
    Cycle.undock()


def m12_phase_2():
    Cycle.warp_to()
    Cycle.open_container()
    time.sleep(90)
    Cycle.move_to_container("antibiotics.png", "colonial_supply.png")
    time.sleep(3)


def m12_phase_3():
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m12():
    print("m12_phase_1")
    m12_phase_1()
    print("m12_phase_2")
    m12_phase_2()
    print("m12_phase_3")
    m12_phase_3()


########################################################
###  Mission 13 - Lair of the Snakes ***
########################################################
def m13_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.warp_to()


def m13_phase_2():
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    max_loc = Cycle.screenshot("serpentis_research_laboratory.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("lock_target.png")
    Cycle.left_click(max_loc)
    pyautogui.press("f")
    Cycle.frigate_target("start_conversation.png")
    Cycle.return_drones()


def m13_phase_3():
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m13():
    print("m13_phase_1")
    m13_phase_1()
    print("m13_phase_2")
    m13_phase_2()
    print("m13_phase_3")
    m13_phase_3()


########################################################
###  Mission 14 - Data Retrieval ***
########################################################
def m14_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.warp_to()


def m14_phase_2():
    Cycle.loot_container()
    Cycle.dock()


def m14_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m14():
    print("m14_phase_1")
    m14_phase_1()
    print("m14_phase_2")
    m14_phase_2()
    print("m14_phase_3")
    m14_phase_3()


########################################################
###  Mission 15 - Crossing Enemy Lines ***
########################################################
def m15_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m15_phase_2():
    Cycle.set_destination_blue()
    Cycle.claysson_jump()
    Cycle.stetille_jump()
    Cycle.adiere_jump()
    Cycle.auberulle_jump()
    Cycle.unel_jump()
    Cycle.tennen_jump()
    Cycle.hatakani_jump()
    Cycle.dock()
    # This automatically completes the mission
    Cycle.start_conversation()


def m15():
    print("m15_phase_1")
    m15_phase_1()
    print("m15_phase_2")
    m15_phase_2()


########################################################
###  Mission 16 - Passive Observation ***
########################################################
def m16_phase_1():
    Cycle.accept()
    Cycle.undock()


def m16_phase_2():
    Cycle.warp_to()
    Cycle.acceleration_gate()
    max_loc = Cycle.screenshot("hollow_asteroid.png")
    Cycle.right_click(max_loc)
    Cycle.approach()
    time.sleep(20)


def m16_phase_3():
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m16():
    print("m16_phase_1")
    m16_phase_1()
    print("m16_phase_2")
    m16_phase_2()
    print("m16_phase_3")
    m16_phase_3()


########################################################
###  Mission 17 - House of Records ***
########################################################
def m17_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m17_phase_2():
    Cycle.set_destination_blue()
    Cycle.tennen_jump()
    Cycle.unel_jump()
    Cycle.chainelant_jump()
    Cycle.dock()


def m17_phase_3():
    Cycle.open_hangar()
    Cycle.move_to_cargo("hidden_data_sheets.png")
    time.sleep(5)
    Cycle.undock()


def m17_phase_4():
    Cycle.set_destination_blue()
    Cycle.unel_jump()
    Cycle.tennen_jump()
    Cycle.hatakani_jump()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m17():
    print("m17_phase_1")
    m17_phase_1()
    print("m17_phase_2")
    m17_phase_2()
    print("m17_phase_3")
    m17_phase_3()
    print("m17_phase_4")
    m17_phase_4()


########################################################
###  Mission 18 - Mercenary Distractions ***
########################################################
def m18_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m18_phase_2():
    Cycle.warp_to()
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()


def m18_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m18():
    print("m18_phase_1")
    m18_phase_1()
    print("m18_phase_2")
    m18_phase_2()
    print("m18_phase_3")
    m18_phase_3()


########################################################
###  Mission 19 - An Economy Under Threat ***
########################################################
def m19_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("farming_supplies.png")
    Cycle.undock()


def m19_phase_2():
    Cycle.warp_to()
    Cycle.acceleration_gate()
    Cycle.open_container()
    Cycle.open_cargohold()
    Cycle.move_to_container("farming_supplies.png", "storage_warehouse.png")


def m19_phase_3():
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m19():
    print("m19_phase_1")
    m19_phase_1()
    print("m19_phase_2")
    m19_phase_2()
    print("m19_phase_3")
    m19_phase_3()


########################################################
###  Mission 20 - Every Drone Inside ***
########################################################
def m20_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.warp_to()


def m20_phase_2():
    Cycle.acceleration_gate()
    max_loc = Cycle.screenshot("frigate_target.png")
    Cycle.right_click(max_loc)
    Cycle.approach()
    Cycle.launch_em_drones()
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()


def m20_phase_3():
    Cycle.start_conversation()
    Cycle.complete_mission()


def m20():
    print("m20_phase_1")
    m20_phase_1()
    print("m20_phase_2")
    m20_phase_2()
    print("m20_phase_3")
    m20_phase_3()


########################################################
###  Mission 21 - A Sense of Dread ***
########################################################
def m21_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m21_phase_2():
    Cycle.set_destination_blue()
    Cycle.kassigainen_jump()
    Cycle.synchelle_jump()
    Cycle.pakhshi_jump()
    Cycle.tar_jump()
    Cycle.manarq_jump()
    Cycle.emsar_jump()
    Cycle.arnon_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m21():
    print("m21_phase_1")
    m21_phase_1()
    print("m21_phase_2")
    m21_phase_2()


########################################################
###  Mission 22 - Royal Jelly ***
########################################################
def m22_phase_1():
    Cycle.accept()
    Cycle.undock()


def m22_phase_2():
    Cycle.warp_to()
    Cycle.loot_container()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m22():
    print("m22_phase_1")
    m22_phase_1()
    print("m22_phase_2")
    m22_phase_2()


########################################################
###  Mission 23 - Nature Pictures ***
########################################################
def m23_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m23_phase_2():
    Cycle.set_destination_blue()
    Cycle.emsar_jump()
    Cycle.manarq_jump()
    Cycle.ourapheh_jump()
    Cycle.atlangeins_jump()
    Cycle.dock()


def m23_phase_3():
    Cycle.open_hangar()
    Cycle.move_to_cargo("encoded_data.png")
    Cycle.undock()


def m23_phase_4():
    Cycle.set_destination_blue()
    Cycle.ourapheh_jump()
    Cycle.manarq_jump()
    Cycle.emsar_jump()
    Cycle.arnon_jump()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m23():
    print("m23_phase_1")
    m23_phase_1()
    print("m23_phase_2")
    m23_phase_2()
    print("m23_phase_3")
    m23_phase_3()
    print("m23_phase_4")
    m23_phase_4()


########################################################
###  Mission 24 - Tracking or Scanning ***
########################################################


def m24_phase_1():
    Cycle.request_mission()
    max_loc = Cycle.screenshot("bag_of_blood.png")
    Cycle.left_click(max_loc)
    time.sleep(10)
    max_loc = Cycle.screenshot("accept_this_choice.png")
    Cycle.left_click(max_loc)
    time.sleep(10)


########################################################
###  Mission 25b - Bag of Blood ***
########################################################


def m25b_phase_1():
    Cycle.undock()
    Cycle.set_destination_blue()
    Cycle.laurvier_jump()
    Cycle.attyn_jump()
    Cycle.dock()


def m25b_phase_2():
    Cycle.open_hangar()
    Cycle.move_to_cargo("wolf_dna.png")
    time.sleep(5)
    Cycle.undock()


def m25b_phase_3():
    Cycle.set_destination_blue()
    Cycle.laurvier_jump()
    Cycle.arnon_jump()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m25b():
    print("m25b_phase_1")
    m25b_phase_1()
    print("m25b_phase_2")
    m25b_phase_2()
    print("m25b_phase_3")
    m25b_phase_3()


########################################################
###  Mission 26b - Planting the Body ***
########################################################
def m26b_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("burgan.png")
    time.sleep(5)
    Cycle.undock()


def m26b_phase_2():
    Cycle.warp_to()
    Cycle.launch_em_drones()
    Cycle.open_container()
    time.sleep(60)
    Cycle.open_cargohold()
    Cycle.move_to_container("burgan.png", "burgan_hideout.png")
    Cycle.return_drones()
    time.sleep(5)
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m26b():
    print("m26b_phase_1")
    m26b_phase_1()
    print("m26b_phase_2")
    m26b_phase_2()


########################################################
###  Mission 27b - Chasing a Nightmare ***
########################################################
def m27b_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m27b_phase_2():
    Cycle.warp_to()
    Cycle.acceleration_gate()
    time.sleep(40)
    Cycle.acceleration_gate()
    time.sleep(40)
    Cycle.acceleration_gate()
    time.sleep(40)
    Cycle.acceleration_gate()
    time.sleep(40)


def m27b_phase_3():
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m27b():
    print("m27b_phase_1")
    m27b_phase_1()
    print("m27b_phase_2")
    m27b_phase_2()
    print("m27b_phase_3")
    m27b_phase_3()


########################################################
###  Mission 28 - Burning Down the Hive ***
########################################################
def m28_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.warp_to()


def m28_phase_2():
    Cycle.acceleration_gate()
    time.sleep(40)
    Cycle.acceleration_gate()
    time.sleep(40)
    Cycle.launch_em_drones()
    max_loc = Cycle.screenshot("frigate_target.png")
    Cycle.right_click(max_loc)
    Cycle.approach()
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m28():
    print("m28_phase_1")
    m28_phase_1()
    print("m28_phase_2")
    m28_phase_2()


########################################################
###  Mission 29 - It's Not Over Yet ***
########################################################
def m29_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m29_phase_2():
    Cycle.set_destination_blue()
    Cycle.emsar_jump()
    Cycle.manarq_jump()
    Cycle.tar_jump()
    Cycle.pakhshi_jump()
    Cycle.renyn_jump()
    Cycle.du_annes_jump()
    Cycle.balle_jump()
    Cycle.aufay_jump()
    Cycle.deltole_jump()
    Cycle.colelie_jump()
    Cycle.bei_jump()
    Cycle.uttindar_jump()
    Cycle.hek_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m29():
    print("m29_phase_1")
    m29_phase_1()
    print("m29_phase_2")
    m29_phase_2()


########################################################
###  Mission 30 - An Eye on Everything ***
########################################################
def m30_phase_1():
    Cycle.accept()
    Cycle.undock()


def m30_phase_2():
    Cycle.warp_to()
    time.sleep(20)
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m30():
    print("m30_phase_1")
    m30_phase_1()
    print("m30_phase_2")
    m30_phase_2()


########################################################
###  Mission 31 - The Use of Force ***
########################################################
def m31_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m31_phase_2():
    Cycle.set_destination_blue()
    Cycle.eystur_jump()
    Cycle.lustrevik_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m31():
    print("m31_phase_1")
    m31_phase_1()
    print("m31_phase_2")
    m31_phase_2()


########################################################
###  Mission 32 - Goading the Leader ***
########################################################
def m32_phase_1():
    Cycle.accept()
    Cycle.undock()
    Cycle.warp_to()


def m32_phase_2():
    Cycle.launch_kinetic_drones()

    max_loc = Cycle.screenshot("auxiliary_power_array.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("lock_target.png")
    Cycle.left_click(max_loc)
    max_loc = Cycle.screenshot("auxiliary_power_array.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("approach.png")
    Cycle.left_click(max_loc)
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m32():
    print("m32_phase_1")
    m32_phase_1()
    print("m32_phase_2")
    m32_phase_2()


########################################################
###  Mission 33 - Hunting the Lieutenants ***
########################################################
def m33_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m33_phase_2():
    Cycle.warp_to()
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()

    max_loc = Cycle.screenshot("habitation_module.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("lock_target.png")
    Cycle.left_click(max_loc)
    max_loc = Cycle.screenshot("habitation_module.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("approach.png")
    Cycle.left_click(max_loc)
    for i in range(0, 90):
        time.sleep(1)
        pyautogui.press("f")


def m33_phase_3():
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m33():
    print("m33_phase_1")
    m33_phase_1()
    print("m33_phase_2")
    m33_phase_2()
    print("m33_phase_3")
    m33_phase_3()


########################################################
###  Mission 34 - Valuable Cargo ***
########################################################
def m34_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m34_phase_2():
    Cycle.set_destination_blue()
    Cycle.eystur_jump()
    Cycle.hek_jump()
    Cycle.dock()
    Cycle.start_conversation()


def m34():
    print("m34_phase_1")
    m34_phase_1()
    print("m34_phase_2")
    m34_phase_2()


########################################################
###  Mission 35 - Marked for Death ***
########################################################
def m35_phase_1():
    Cycle.accept()
    Cycle.undock()


def m35_phase_2():
    Cycle.warp_to()
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    max_loc = Cycle.screenshot("amarr_tactical.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("lock_target.png")
    Cycle.left_click(max_loc)
    max_loc = Cycle.screenshot("amarr_tactical.png")
    Cycle.right_click(max_loc)
    max_loc = Cycle.screenshot("approach.png")
    Cycle.left_click(max_loc)
    for i in range(0, 120):

        time.sleep(1)
        pyautogui.press("f")


def m35_phase_3():
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m35():
    print("m35_phase_1")
    m35_phase_1()
    print("m35_phase_2")
    m35_phase_2()
    print("m35_phase_3")
    m35_phase_3()


########################################################
###  Mission 36 - Thwarting the Succession ***
########################################################
def m36_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m36_phase_2():
    Cycle.warp_to()
    Cycle.launch_kinetic_drones()
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")


def m36_phase_3():
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m36():
    print("m36_phase_1")
    m36_phase_1()
    print("m36_phase_2")
    m36_phase_2()
    print("m36_phase_3")
    m36_phase_3()


########################################################
###  Mission 37 - Certificate of Death ***
########################################################
def m37_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m37_phase_2():
    Cycle.set_destination_blue()
    Cycle.eystur_jump()
    Cycle.lustrevik_jump()
    Cycle.onga_jump()
    Cycle.gyng_jump()
    Cycle.frarn_jump()
    Cycle.rens_jump()
    Cycle.odatrik_jump()
    Cycle.jark_jump()
    Cycle.sasta_jump()
    Cycle.tanoo_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m37():
    print("m37_phase_1")
    m37_phase_1()
    print("m37_phase_2")
    m37_phase_2()


########################################################
###  Mission 38 - A Matter of Decorum ***
########################################################
def m38_phase_1():
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("mizras_doll.png")
    Cycle.undock()


def m38_phase_2():
    Cycle.warp_to()
    Cycle.open_container()
    Cycle.move_to_container("mizras_doll.png", "mizra_family_hovel.png")
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m38():
    print("m38_phase_1")
    m38_phase_1()
    print("m38_phase_2")
    m38_phase_2()


########################################################
###  Mission 39 - New Friends ***
########################################################
def m39_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.set_destination_blue()


def m39_phase_2():
    Cycle.sasta_jump()
    Cycle.lashesih_jump()
    Cycle.lisudeh_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m39():
    print("m39_phase_1")
    m39_phase_1()
    print("m39_phase_2")
    m39_phase_2()


########################################################
###  Mission 40 - Recovery ***
########################################################
def m40_phase_1():
    Cycle.accept()
    Cycle.undock()


def m40_phase_2():
    Cycle.warp_to()
    Cycle.launch_em_drones()
    Cycle.approach_and_target("relic.png")
    time.sleep(200)


def m40_phase_3():
    max_loc = Cycle.screenshot("relic_analyzer.png")
    Cycle.left_click(max_loc)
    time.sleep(20)
    hacked = False
    while hacked == False:
        time.sleep(5)
        if Cycle.if_needle("system_core.png") > 0.85:
            max_loc = Cycle.screenshot("system_core.png")
            Cycle.left_click(max_loc)
        elif Cycle.if_needle("encrypted_node.png") > 0.85:
            max_loc = Cycle.screenshot("encrypted_node.png")
            Cycle.left_click(max_loc)
        elif Cycle.if_needle("relic_node.png") > 0.75:
            max_loc = Cycle.screenshot("relic_node.png")
            Cycle.left_click(max_loc)
        elif Cycle.if_needle("relic_node_2.png") > 0.75:
            max_loc = Cycle.screenshot("relic_node_2.png")
            Cycle.left_click(max_loc)
        elif Cycle.if_needle("relic_node_3.png") > 0.75:
            max_loc = Cycle.screenshot("relic_node_2.png")
            Cycle.left_click(max_loc)
        elif Cycle.if_needle("firewall_node.png") > 0.85:
            max_loc = Cycle.screenshot("firewall_node.png")
            Cycle.left_click(max_loc)
        else:
            hacked = True
            break

    Cycle.loot_container()


def m40_phase_4():
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m40():
    print("m40_phase_1")
    m40_phase_1()
    print("m40_phase_2")
    m40_phase_2()
    print("m40_phase_3")
    m40_phase_3()
    print("m40_phase_4")
    m40_phase_4()


########################################################
###  Mission 41 - Of Quiet Nights Long Past ***
########################################################
def m41_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m41_phase_2():
    Cycle.warp_to()
    Cycle.launch_em_drones()
    Cycle.frigate_target("container.png")
    Cycle.return_drones()
    Cycle.loot_container()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m41():
    print("m41_phase_1")
    m41_phase_1()
    print("m41_phase_2")
    m41_phase_2()


########################################################
###  Mission 42 - Revelations ***
########################################################
def m42_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m42_phase_2():
    Cycle.set_destination_blue()
    Cycle.lashesih_jump()
    Cycle.sasta_jump()
    Cycle.tanoo_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m42():
    print("m42_phase_1")
    m42_phase_1()
    print("m42_phase_2")
    m42_phase_2()


########################################################
###  Mission 43 - A Call to Trial ***
########################################################
def m43_phase_1():
    Cycle.accept()
    Cycle.undock()


def m43_phase_2():
    Cycle.warp_to()
    Cycle.launch_em_drones()
    Cycle.frigate_target("start_conversation.png")
    Cycle.return_drones()
    Cycle.start_conversation()
    Cycle.complete_remotely()


def m43():
    print("m43_phase_1")
    m43_phase_1()
    print("m43_phase_2")
    m43_phase_2()


########################################################
###  Mission 44 - Brothers and Sisters ***
########################################################
def m44_phase_1():
    Cycle.request_mission()
    Cycle.accept_remotely()
    Cycle.set_destination_blue()


def m44_phase_2():
    Cycle.sasta_jump()
    Cycle.jark_jump()
    Cycle.odatrik_jump()
    Cycle.trytedald_jump()
    Cycle.ivar_jump()
    Cycle.ameinaka_jump()
    Cycle.arlulf_jump()
    Cycle.alf_jump()
    Cycle.illuin_jump()
    Cycle.hjortur_jump()
    Cycle.evettullur_jump()
    Cycle.tratokard_jump()
    Cycle.getugaud_jump()
    Cycle.josekorn_jump()
    time.sleep(30)
    Cycle.nifflung_jump()
    Cycle.hakeri_jump()
    Cycle.irgrus_jump()
    Cycle.pakhshi_jump()
    Cycle.tar_jump()
    Cycle.manarq_jump()
    Cycle.emsar_jump()
    Cycle.arnon_jump()
    Cycle.dock()
    # This will automatically complete the mission
    Cycle.start_conversation()


def m44():
    print("m44_phase_1")
    m44_phase_1()
    print("m44_phase_2")
    m44_phase_2()


########################################################
###  Mission 45 - A Stranger's\Face ***
########################################################
def m45_phase_1():
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("altered_identity.png")
    Cycle.undock()


def m45_phase_2():
    Cycle.set_destination_blue()
    Cycle.emsar_jump()
    Cycle.manarq_jump()
    Cycle.tolle_jump()
    Cycle.aydoteaux_jump()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m45():
    print("m45_phase_1")
    m45_phase_1()
    print("m45_phase_2")
    m45_phase_2()


########################################################
###  Mission 46 - The Sisters and the Spy ***
########################################################
def m46_phase_1():
    Cycle.request_mission()
    max_loc = Cycle.screenshot("arnon_destination.png")
    Cycle.right_click(max_loc)
    Cycle.set_destination()
    Cycle.undock_yellow()


def m46_phase_2():
    Cycle.tolle_jump()
    Cycle.manarq_jump()
    Cycle.emsar_jump()
    Cycle.arnon_jump()
    max_loc = Cycle.screenshot("arnon_destination.png")
    Cycle.right_click(max_loc)
    Cycle.dock_rc()


def m46_phase_3():
    max_loc = Cycle.screenshot("alitura.png")
    Cycle.double_click(max_loc)
    Cycle.accept()
    Cycle.open_hangar()
    Cycle.move_to_cargo("tahaki.png")
    Cycle.undock()


def m46_phase_4():
    Cycle.warp_to()
    Cycle.open_container()
    Cycle.move_to_container("tahaki.png", "soct_luxury.png")
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m46():
    print("m46_phase_1")
    m46_phase_1()
    print("m46_phase_2")
    m46_phase_2()
    print("m46_phase_3")
    m46_phase_3()
    print("m46_phase_4")
    m46_phase_4()


########################################################
###  Mission 47 - Sealing the Deal ***
########################################################
def m47_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m47_phase_2():
    Cycle.warp_to()
    Cycle.launch_kinetic_drones()
    Cycle.approach_and_target("society_spy.png")
    time.sleep(5)
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m47():
    print("m47_phase_1")
    m47_phase_1()
    print("m47_phase_2")
    m47_phase_2()


########################################################
###  Mission 48 - Chasing Shadows ***
########################################################
def m48_phase_1():
    Cycle.request_mission()
    Cycle.accept()
    Cycle.undock()


def m48_phase_2():
    Cycle.warp_to()
    Cycle.launch_em_drones()
    Cycle.approach_and_target("kritsan.png")
    time.sleep(5)
    Cycle.autotarget()
    Cycle.frigate_target("dock.png")
    Cycle.return_drones()
    Cycle.dock()
    Cycle.start_conversation()
    Cycle.complete_mission()


def m48():
    print("m48_phase_1")
    m48_phase_1()
    print("m48_phase_2")
    m48_phase_2()


########################################################
###  Mission 48 - Chasing Shadows ***
########################################################
def m49_phase_1():
    Cycle.request_mission()

