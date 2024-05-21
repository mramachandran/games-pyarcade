from PIL import Image, ImageDraw, ImageFont

# Function to create a simple square image with a specified color
def create_square_image(size, color):
    image = Image.new("RGBA", (size, size), color)
    return image

# Create a placeholder image for the player sprite (a blue square)
player_image = create_square_image(50, "blue")
player_image.save("player_image.png")

# Create a placeholder image for the coin sprite (a yellow circle)
coin_image = create_square_image(30, "yellow")
draw = ImageDraw.Draw(coin_image)
draw.ellipse((0, 0, 30, 30), fill="red")
coin_image.save("coin_image.png")
