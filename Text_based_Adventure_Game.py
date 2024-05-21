{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM/lrUL7ndc3pOfXb/Tn/of"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Text-based Adventure Game\n",
        "\n",
        "This is a simple text-based adventure game written in Python. The player can navigate through different rooms by typing commands.\n",
        "\n",
        "## How to Play\n",
        "\n",
        "- Run the `game.py` script to start the game.\n",
        "- Type commands like `north`, `south`, `east`, `west` to move between rooms.\n",
        "- Type `exit` to end the game.\n",
        "\n",
        "## Rooms\n",
        "\n",
        "- **Kitchen**: You are in a kitchen. There is a delicious smell of food.\n",
        "- **Hall**: You are in the hall. It is dark and cold.\n",
        "- **Bedroom**: You are in a cozy bedroom with a soft bed.\n",
        "- **Garden**: You are in a beautiful garden with blooming flowers.\n",
        "\n",
        "Enjoy exploring the rooms!\n"
      ],
      "metadata": {
        "id": "p7BLOlqav_Iq"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pPHZ53_Nvqbd"
      },
      "outputs": [],
      "source": [
        "text_based_game/\n",
        "├── game.py\n",
        "└── README.md"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Room:\n",
        "    def __init__(self, name, description):\n",
        "        self.name = name\n",
        "        self.description = description\n",
        "        self.exits = {}\n",
        "\n",
        "    def set_exit(self, direction, room):\n",
        "        self.exits[direction] = room\n",
        "\n",
        "    def get_exit(self, direction):\n",
        "        return self.exits.get(direction)\n",
        "\n",
        "    def __str__(self):\n",
        "        return f\"{self.name}\\n\\n{self.description}\\n\"\n",
        "\n",
        "def create_rooms():\n",
        "\n",
        "    kitchen = Room(\"Kitchen\", \"You are in a kitchen. There is a delicious smell of food.\")\n",
        "    hall = Room(\"Hall\", \"You are in the hall. It is dark and cold.\")\n",
        "    bedroom = Room(\"Bedroom\", \"You are in a cozy bedroom with a soft bed.\")\n",
        "    garden = Room(\"Garden\", \"You are in a beautiful garden with blooming flowers.\")\n",
        "\n",
        "\n",
        "    kitchen.set_exit(\"south\", hall)\n",
        "    hall.set_exit(\"north\", kitchen)\n",
        "    hall.set_exit(\"east\", bedroom)\n",
        "    bedroom.set_exit(\"west\", hall)\n",
        "    bedroom.set_exit(\"south\", garden)\n",
        "    garden.set_exit(\"north\", bedroom)\n",
        "\n",
        "    return kitchen\n",
        "\n",
        "def play_game():\n",
        "    current_room = create_rooms()\n",
        "    print(\"Welcome to the adventure game!\")\n",
        "    print(\"Type 'exit' to end the game.\")\n",
        "    print(current_room)\n",
        "\n",
        "    while True:\n",
        "        command = input(\"> \").strip().lower()\n",
        "        if command == \"exit\":\n",
        "            print(\"Thanks for playing!\")\n",
        "            break\n",
        "        elif command in current_room.exits:\n",
        "            current_room = current_room.get_exit(command)\n",
        "            print(current_room)\n",
        "        else:\n",
        "            print(\"Invalid command. Try 'north', 'south', 'east', 'west', or 'exit'.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    play_game()"
      ],
      "metadata": {
        "id": "-HYT6C5Uvwwi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}