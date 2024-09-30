from PIL import Image
import os

def create_gif(image_paths, output_gif_path, duration=500):
    """Creates a GIF from a list of image paths."""

    images = [Image.open(image_path) for image_path in image_paths]
    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=duration,
        loop=0  # 0 means infinite loop
    )

if __name__ == "__main__":

    #prompt user for name of directory
    d_input = input("What directory will you be using?")
    #put that input into a directory datatype
    directory = os.listdir(d_input)
    #create a list for file names
    picList = []
    for i in directory:
      picList.append(i)
      
    # Replace with your image paths
    image_paths = picList

    # Output GIF path
    output_gif_path = "output.gif"

    # Create the GIF
    create_gif(image_paths, output_gif_path)

    print(f"GIF created and saved at {output_gif_path}")
