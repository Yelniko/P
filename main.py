from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

model_1 = 'Elements/Models/Block'
grass_texture = load_texture('Elements/Textures/Grass_Block.png')
stone_texture = load_texture('Elements/Textures/Stone_Block.png')
brick_texture = load_texture('Elements/Textures/Brick_Block.png')
dirt_texture = load_texture('Elements/Textures/Dirt_Block.png')
wood_texture = load_texture('Elements/Textures/Wood_Block.png')
arm_texture = load_texture('Elements/Textures/Arm_Texture.png')
punch_sound = Audio('Elements/Audio/Punch_Sound.wav')
breaking_sound = Audio('Elements/Audio/cloth1.mp3')
sound = Audio('Elements/Audio/fon.mp3')
block_pick = 1


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), textures=grass_texture, model=model_1):
        super().__init__(parent=scene,
                         position=position,
                         model=model,
                         origin_y=.5,
                         texture=textures,
                         color=color.color(0, 0, random.uniform(.9, 1.0)),
                         scale=0.5
                         )

    def input(self, key):
        if key == 'left mouse down':
            raycast(camera.world_position, camera.forward, distance=5)
            if self.hovered:
                punch_sound.play()
                if block_pick == 1:
                    Voxel(position=self.position + mouse.normal, textures=grass_texture)
                if block_pick == 2:
                    Voxel(position=self.position + mouse.normal, textures=stone_texture)
                if block_pick == 3:
                    Voxel(position=self.position + mouse.normal, textures=brick_texture)
                if block_pick == 4:
                    Voxel(position=self.position + mouse.normal, textures=dirt_texture)
                if block_pick == 5:
                    Voxel(position=self.position + mouse.normal, textures=wood_texture)
        if key == 'right mouse down' and mouse.hovered_entity:
            destroy(mouse.hovered_entity)
            breaking_sound.play()


for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))


def update():
    global block_pick
    if held_keys["1"]:
        block_pick = 1
    if held_keys["2"]:
        block_pick = 2
    if held_keys["3"]:
        block_pick = 3
    if held_keys["4"]:
        block_pick = 4
    if held_keys["5"]:
        block_pick = 5
    if player.y < -10:
        player.y = 100
        player.x = 0
        player.z = 0


sound.volume = 0.1
sound.play()

player = FirstPersonController()
sky = Sky()
app.run()
