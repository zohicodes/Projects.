{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOth2586xtTEoIORiewbsXt"
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
        "# Would ya look at that!\n",
        "Created (and generated) myself another mini-project; just a simple weather forecast python code. yes, of course, it's (should) be in a .py file 🌞\n",
        "\n"
      ],
      "metadata": {
        "id": "AUbB_uwtd58a"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fXsUkFJlY8YL"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "\n",
        "def get_weather(city):\n",
        "    api_key = 'YOUR_API_KEY'  # Sign up on OpenWeatherMap to get an API key\n",
        "    base_url = 'http://api.openweathermap.org/data/2.5/weather?'\n",
        "    complete_url = base_url + 'appid=' + api_key + '&q=' + city\n",
        "\n",
        "    response = requests.get(complete_url)\n",
        "    data = response.json()\n",
        "\n",
        "    if data['cod'] != '404':\n",
        "        main = data['main']\n",
        "        weather = data['weather'][0]\n",
        "        temperature = main['temp']\n",
        "        humidity = main['humidity']\n",
        "        description = weather['description']\n",
        "\n",
        "        print(f\"Temperature: {temperature}\")\n",
        "        print(f\"Humidity: {humidity}%\")\n",
        "        print(f\"Description: {description}\")\n",
        "    else:\n",
        "        print(\"City not found.\")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    city = input(\"Enter city name: \")\n",
        "    get_weather(city)"
      ]
    }
  ]
}