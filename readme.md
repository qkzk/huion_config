# Installer une tablette HUION 640 sous manjaro

Disons le de but en blanc : c'est de la merde


## Tuto

1. brancher la tablette, vérifier que les leds s'allument quand on clic les boutons et approche le pen
2. Rien ne marche
3. Installer les headers pour le kernel (`$ uname -a`)  - chercher headers dans pamac et choisir la bonne version
4. Installer la librairie officieuse : https://github.com/Huion-Linux/DIGImend-kernel-drivers-for-Huion
    chercher **digimend** dans pamac.
5. installer dkms (pamac)
6. `$ sudo modprobe -r hid-kye hid-uclogic hid-polostar hid-viewsonic`
6. là normalement, après reboot la tablette est reconnue


## Limiter la tablette à un écran à la main

Par défaut elle recouvre les deux écrans et c'est inutilisable

1. Trouver quel écran utiliser : `$ xrandr` repérer le nom de l'écran : `nom_ecran`
2. `xinput` trouver le pen et son id : `pen_id`
3. `$ xinput map-to-output {pen_id} {nom_ecran}`

## Limiter la tablette à un écran avec le script

1. Changer les noms des écrans dans le script 
2. Exécuter le script avec 0 pour l'écran de gauche, `python config_tablette.py 0` et 
    1 pour l'écran de droite `python config_tablette.py 1` pour l'écran de droite


## Sources

https://github.com/Huion-Linux/DIGImend-kernel-drivers-for-Huion
https://aur.archlinux.org/packages/digimend-kernel-drivers-dkms-git
https://askubuntu.com/questions/500141/huion-h610-tablet/
https://askubuntu.com/questions/839161/limit-a-graphics-tablet-to-one-monitor


## Pb installation

==> Finished making: linux-lts419 4.19.124-1 (mer. 20 mai 2020 18:19:35)
==> Cleaning up...

Running post-transaction hooks...
Checking keyring...
Checking integrity...
Loading packages files...
Checking file conflicts...
Checking available disk space...
Installing linux-lts419-headers (4.19.124-1)...
Running post-transaction hooks...
Arming ConditionNeedsUpdate...
Updating module dependencies...
Install DKMS modules
==> Unable to install module digimend-kernel-drivers/9.r98.g00a0624 for kernel 4.19.124-1-lts419: Missing kernel modules tree.
Transaction successfully finished.
