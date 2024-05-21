import random
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Arcade Game"
PLAYER_SCALING = 0.5
COIN_SCALING = 0.2
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Variables to hold game objects
        self.player_sprite = None
        self.coin_list = None
        self.all_sprites_list = None
        
        self.score = 0
        
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        # Create the sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        # Set up the player
        self.player_sprite = arcade.Sprite("player_image.png", PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)
        
        # Create the coins
        for i in range(50):
            coin = arcade.Sprite("coin_image.png", COIN_SCALING)
            
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            # Add the coin to the lists
            self.coin_list.append(coin)
            self.all_sprites_list.append(coin)
        
    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        
        # Display the score
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        
    def on_update(self, delta_time):
        self.all_sprites_list.update()
        
        # Check for collisions
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            
def main():
    game = MyGame()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
