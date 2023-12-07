import tkinter as tk
from tkinter import PhotoImage
from math import sqrt
from PIL import Image, ImageDraw, ImageTk

def hex_to_rgb(hex_code):
    # Convert hex code to RGB tuple
    return tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))

def calculate_luminance(hex_code):
    # Calculate the luminance (brightness) of a color
    r, g, b = hex_to_rgb(hex_code)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
    return luminance

def get_contrast_color(hex_code):
    # Choose white or black text color based on the luminance of the background color
    luminance = calculate_luminance(hex_code)
    return "#000000" if luminance > 0.5 else "#FFFFFF"

class TableApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.cell_size = (15, 3)
        self.image = None

        # Create and set up the Tkinter window
        self.setup_gui()

    def setup_gui(self):
        # Set the title of the window
        self.root.title("Table App")

        # Create dictionaries to store hex codes and column indices based on families
        family_hex_mapping = {}
        family_column_mapping = {}

        # Iterate through each family in the sorted data
        for family, family_data in self.sort_families_by_color_wheel():
            # If the family is not yet in the mappings, create a new column for it
            if family not in family_hex_mapping:
                family_hex_mapping[family] = {}
                family_column_mapping[family] = len(family_hex_mapping) - 1

            # Iterate through each entry in the sorted family data
            for row_num, entry in enumerate(family_data):
                name = entry["Name"]
                hex_code = entry["Hex"]

                # Store the hex code for the current family and name
                family_hex_mapping[family][name] = hex_code

                # Calculate contrast text color based on background color
                text_color = get_contrast_color(hex_code)

                # Create labels for each name in the table with colored background and bold text
                name_label = tk.Label(self.root, text=name, width=self.cell_size[0], height=self.cell_size[1],
                                      bg=hex_code, fg=text_color, font=("Arial", 10, "bold"))
                name_label.grid(row=row_num, column=family_column_mapping[family], sticky='w')

        # Create a button to save the table as a PNG image
        save_button = tk.Button(self.root, text="Save as PNG", command=self.save_table_as_image)
        save_button.grid(row=len(self.data) + 1, column=0, columnspan=len(family_column_mapping), pady=10)

    def save_table_as_image(self):
        # Update the Tkinter window to ensure all labels are drawn
        self.root.update()

        # Create an image with the same size as the Tkinter window
        image = Image.new("RGB", (self.root.winfo_width(), self.root.winfo_height()), "white")
        draw = ImageDraw.Draw(image)

        # Convert the Tkinter window content to an image
        img = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.update()

        # Draw the Tkinter window content on the image
        image.paste(img, (0, 0))

        # Save the image as a PNG file
        image.save("table.png")

    def sort_families_by_color_wheel(self):
        # Sort families based on color wheel (red component of RGB)
        sorted_families = sorted(self.data.items(), key=lambda x: hex_to_rgb(x[1][0]["Hex"])[0])
        return sorted_families

if __name__ == "__main__":
    # Provide the data as a dictionary
    data = {
  "Azure": [
    {"Name": "Azure", "Hex": "#007FFF"},
    {"Name": "Baby Blue", "Hex": "#73B9FF"},
    {"Name": "Cetecean", "Hex": "#001A33"},
    {"Name": "Cornflower", "Hex": "#BFDFFF"},
    {"Name": "Marine", "Hex": "#007189"},
    {"Name": "Moonstone", "Hex": "#537CA6"},
    {"Name": "Overcast", "Hex": "#537CA6"},
    {"Name": "Prussian", "Hex": "#003366"},
    {"Name": "Sapphire", "Hex": "#0059B3"}
  ],
  "Blue": [
    {"Name": "Blue", "Hex": "#0000FF"},
    {"Name": "Cobalt", "Hex": "#0000B3"},
    {"Name": "Deepfreeze", "Hex": "#5353A6"},
    {"Name": "Denim", "Hex": "#7373FF"},
    {"Name": "Frost", "Hex": "#8C8CD9"},
    {"Name": "Haze", "Hex": "#535872"},
    {"Name": "Ice", "Hex": "#BFBFFF"},
    {"Name": "Midnight", "Hex": "#000033"},
    {"Name": "Navy", "Hex": "#000066"}
  ],
  "Brown": [
    {"Name": "Brown", "Hex": "#80642D"},
    {"Name": "Bark", "Hex": "#594724"},
    {"Name": "Camel", "Hex": "#B39C59"},
    {"Name": "Cream", "Hex": "#F5F5DC"},
    {"Name": "Leather", "Hex": "#99823D"},
    {"Name": "Sand", "Hex": "#E6C973"},
    {"Name": "Mud", "Hex": "#403522"},
    {"Name": "Parchment", "Hex": "#FFEFBF"},
    {"Name": "Tan", "Hex": "#CCB266"}
  ],
  "Chartreuse": [
    {"Name": "Avocado", "Hex": "#336600"},
    {"Name": "Chartreuse", "Hex": "#80FF00"},
    {"Name": "Craggy-Dew", "Hex": "#B3E912"},
    {"Name": "Filth", "Hex": "#7CA653"},
    {"Name": "Menthol", "Hex": "#B9FF73"},
    {"Name": "Nyanza", "Hex": "#DFFFBF"},
    {"Name": "Orc", "Hex": "#59B300"},
    {"Name": "Putrescence", "Hex": "#B3D98D"},
    {"Name": "Swamp", "Hex": "#193300"}
  ],
  "Cyan": [
    {"Name": "Cyan", "Hex": "#00FFFF"},
    {"Name": "Celeste", "Hex": "#BFFFFF"},
    {"Name": "Crystal", "Hex": "#8DD9D9"},
    {"Name": "Electricity", "Hex": "#73FFFF"},
    {"Name": "Mariana", "Hex": "#003333"},
    {"Name": "Ocean", "Hex": "#53A6A6"},
    {"Name": "Skobeloff", "Hex": "#006666"},
    {"Name": "Strream", "Hex": "#2AC6B6"},
    {"Name": "Teal", "Hex": "#00B3B3"}
  ],
  "Fuschia": [
    {"Name": "Bubblegum", "Hex": "#FFBFCF"},
    {"Name": "Flamingo", "Hex": "#FF73B9"},
    {"Name": "Fuschia", "Hex": "#FF007F"},
    {"Name": "Kobi", "Hex": "#D98DB3"},
    {"Name": "Lust", "Hex": "#B30059"},
    {"Name": "Raisin", "Hex": "#330019"},
    {"Name": "Rouge", "Hex": "#A6537C"},
    {"Name": "Tyrian", "Hex": "#660033"},
    {"Name": "Valentine", "Hex": "#FFBFDF"}
  ],
  "Green": [
    {"Name": "Celadon", "Hex": "#8DD98D"},
    {"Name": "Chateau", "Hex": "#53A653"},
    {"Name": "Enerakd", "Hex": "#00B300"},
    {"Name": "Grass", "Hex": "#227330"},
    {"Name": "Hunter", "Hex": "#006600"},
    {"Name": "Mind", "Hex": "#73FF73"},
    {"Name": "Nori", "Hex": "#003300"},
    {"Name": "Pistachio", "Hex": "#BFFFBF"},
    {"Name": "Green", "Hex": "#00FF00"}
  ],
  "Greyscale": [
    {"Name": "Black", "Hex": "#191919"},
    {"Name": "Charcoal", "Hex": "#4D4D4D"},
    {"Name": "Grey", "Hex": "#B3B3B3"},
    {"Name": "Gunmetal", "Hex": "#666666"},
    {"Name": "Shadow", "Hex": "#333333"},
    {"Name": "Steel", "Hex": "#999999"},
    {"Name": "Wisp", "Hex": "#E6E6E6"},
    {"Name": "Silver", "Hex": "#CCCCCC"},
    {"Name": "Slate", "Hex": "#808080"},
    {"Name": "White", "Hex": "#FFFFFF"}
  ],
  "Magenta": [
    {"Name": "Bruise", "Hex": "#A653A6"},
    {"Name": "Cottoncandy", "Hex": "#FFBFFF"},
    {"Name": "Eggplant", "Hex": "#330033"},
    {"Name": "Orchid", "Hex": "#D98DD9"},
    {"Name": "Plum", "Hex": "#660066"},
    {"Name": "Thistle", "Hex": "#E6C3DD"},
    {"Name": "Magenta", "Hex": "#FF00FF"},
    {"Name": "Pink", "Hex": "#FF73FF"},
    {"Name": "Purple", "Hex": "#B200B3"}
  ],
  "Orange": [
    {"Name": "Cantaloupe", "Hex": "#FFB973"},
    {"Name": "Bronze", "Hex": "#331900"},
    {"Name": "Dirt", "Hex": "#A67C53"},
    {"Name": "Gold", "Hex": "#FFC000"},
    {"Name": "Latte", "Hex": "#D9B38D"},
    {"Name": "Peache", "Hex": "#FFDFBF"},
    {"Name": "Terracotta", "Hex": "#663300"},
    {"Name": "Windosr", "Hex": "#B35900"},
    {"Name": "Orange", "Hex": "#FF7F00"},
    {"Name": "Tangerine", "Hex": "#FFA424"}
  ],
  "Red": [
    {"Name": "Brick", "Hex": "#994326"},
    {"Name": "Burn", "Hex": "#330000"},
    {"Name": "Edocha", "Hex": "#A65353"},
    {"Name": "Gore", "Hex": "#B30000"},
    {"Name": "Incense", "Hex": "#D98D8D"},
    {"Name": "Salmon", "Hex": "#FFBFBF"},
    {"Name": "Scab", "Hex": "#660000"},
    {"Name": "Tulip", "Hex": "#FF7373"},
    {"Name": "Red", "Hex": "#FF0000"}
  ],
  "Spring": [
    {"Name": "Aquamarine", "Hex": "#73FFB9"},
    {"Name": "Jungle", "Hex": "#00331A"},
    {"Name": "Lagoon", "Hex": "#00B359"},
    {"Name": "Seafoam", "Hex": "#BFFFDF"},
    {"Name": "Shamrock", "Hex": "#53A67C"},
    {"Name": "Spring", "Hex": "#00FF80"},
    {"Name": "Turquoise", "Hex": "#8DD9B3"},
    {"Name": "Forest", "Hex": "#006633"}
  ],
  "Violet": [
    {"Name": "Dusk", "Hex": "#8F4EA5"},
    {"Name": "Eminence", "Hex": "#330066"},
    {"Name": "Indigo", "Hex": "#5900B3"},
    {"Name": "Lavender", "Hex": "#DFBFFF"},
    {"Name": "Lilac", "Hex": "#B973FF"},
    {"Name": "Mauuve", "Hex": "#B38DD9"},
    {"Name": "Twlight", "Hex": "#190033"},
    {"Name": "Violet", "Hex": "#8000FF"},
    {"Name": "Royalty", "Hex": "#7C53A6"}
  ],
  "Yellow": [
    {"Name": "Buttermilk", "Hex": "#FFFFBF"},
    {"Name": "Canary", "Hex": "#FFFF73"},
    {"Name": "Citron", "Hex": "#B2B300"},
    {"Name": "Drab", "Hex": "#333300"},
    {"Name": "Khaki", "Hex": "#D9D98D"},
    {"Name": "Mold", "Hex": "#A6A653"},
    {"Name": "Mustard", "Hex": "#F0F032"},
    {"Name": "Olive", "Hex": "#666600"},
    {"Name": "Yellow", "Hex": "#FFFF00"}
  ]
}

    # Create the Tkinter root window
    root = tk.Tk()

    # Create an instance of the TableApp class
    table_app = TableApp(root, data)

    # Run the Tkinter event loop
    root.mainloop()
