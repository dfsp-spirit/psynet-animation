# pylint: disable=unused-import,abstract-method,unused-argument,no-member

import psynet.experiment
from psynet.asset import LocalStorage, S3Storage  # noqa
from psynet.graphics import (
    Animation,
    Circle,
    Ellipse,
    Frame,
    GraphicControl,
    GraphicPrompt,
    Image,
    Path,
    Rectangle,
    Text,
)
from psynet.modular_page import (
    AudioMeterControl,
    AudioRecordControl,
    ModularPage,
    Prompt,
)
from psynet.page import DebugResponsePage, InfoPage
from psynet.timeline import MediaSpec, Timeline
from psynet.consent import NoConsent

from typing import List, Dict

def get_bird_image_dict(colors: List[str], imgdir: str) -> Dict[str, str]:

    if not isinstance(colors, list):
        raise ValueError("colors must be a list")
    if not isinstance(imgdir, str):
        raise ValueError("imgdir must be a string")

    image = {}
    for color in colors:
        image[f"bird{color}_singing"] = f"{imgdir}/bird{color}_singing.png"
        image[f"bird{color}_sitting"] = f"{imgdir}/bird{color}_sitting.png"
    return image


class Exp(psynet.experiment.Experiment):
    label = "Graphics demo"

    # asset_storage = S3Storage("psynet-tests", "graphics")
    imgdir = "/static"
    graphic_width = 100
    graphic_height = 100

    consentPage = NoConsent()
    infoPage = InfoPage(
            "Graphic components provide a way to display interactive visual animations to the participant.",
            time_estimate=5,
        )

    bird_page = ModularPage(
        "birdgraphic",
        prompt=Prompt(
            text="Click the green bird!",
        ),
        control=GraphicControl(
            dimensions=[graphic_width, graphic_height],
            viewport_width=1,

            frames=[
                # The birds start at the left and right.
                # They move towards the center (and close to each other).
                Frame(
                    [
                        Image("gray_sit", media_id="birdgray_sitting",
                            persist=False,
                            x=10,
                            y=50,
                            width=10,
                            animations=[
                                Animation({ "x":40 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),

                        Image("green_sit", media_id="birdgreen_sitting",
                            persist=False,
                            x=90,
                            y=50,
                            width=10,
                            click_to_answer=True,
                            animations=[
                                Animation({"x":55 }, duration=3.0),
                            ],
                        ),
                    ],
                    duration=4.0,
                ),
                # The birds start singing together.
                # They move up and down a little bit.
                Frame(
                    [
                        Image("gray_sing", media_id="birdgray_singing",
                            persist=False,
                            x=40,
                            y=50,
                            width=10,
                            animations=[
                                Animation({"y": 52 }, duration=1.0),
                                Animation({"y": 50 }, duration=1.0),
                            ],
                            loop_animations=True,
                        ),
                        Image("green_sing", media_id="birdgreen_singing",
                            persist=False,
                            x=55,
                            y=50,
                            width=10,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 52 }, duration=1.0),
                                Animation({"y": 50 }, duration=1.0),
                            ],
                            loop_animations=True,
                        ),
                    ],
                    duration=4.0,
                ),
                # The birds fly away together, upwards out of the screen.
                Frame(
                    [
                        Image("gray_fly", media_id="birdgray_sitting",
                            persist=False,
                            x=40,
                            y=50,
                            width=10,
                            animations=[
                                Animation({"y": -20 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                        Image("green_fly", media_id="birdgreen_sitting",
                            persist=False,
                            x=55,
                            y=50,
                            width=10,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": -20 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                    ],
                    duration=3.0,
                ),
                # The birds come down again and land.
                Frame(
                    [
                        Image("gray_fly", media_id="birdgray_sitting",
                            persist=False,
                            x=20,
                            y=-20,
                            width=10,
                            animations=[
                                Animation({"y": 50 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                        Image("green_fly", media_id="birdgreen_sitting",
                            persist=False,
                            x=80,
                            y=-20,
                            width=10,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 50 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                    ],
                )

            ],
            loop=True,
            media=MediaSpec(
                image=get_bird_image_dict(["gray", "green"], imgdir),
            ),
        ),
        time_estimate=5,
    )

    robot_page = ModularPage(
        "robotgraphic",
        prompt=Prompt(
            text="Click one of the robots!",
        ),
        control=GraphicControl(
            dimensions=[graphic_width, graphic_height],
            viewport_width=1,

            frames=[
                # The robots start at the left and right.
                # They move towards the center (and close to each other).
                Frame(
                    [
                        Image("r1walk", media_id="rwalk",
                            persist=False,
                            x=10,
                            y=50,
                            width=20,
                            height=20,
                            click_to_answer=True,
                            animations=[
                                Animation({ "x":40, "width":40, "height":40 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),

                        Image("r2walk", media_id="r2walk",
                            persist=False,
                            x=90,
                            y=50,
                            width=20,
                            height=20,
                            click_to_answer=True,
                            animations=[
                                Animation({"x":55, "width":40, "height":40}, duration=3.0),
                            ],
                        ),
                    ],
                    duration=4.0,
                ),
                # The robots start singing together.
                # They move up and down a little bit.
                Frame(
                    [
                        Image("r1sing", media_id="rsing",
                            persist=False,
                            x=40,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 52 }, duration=1.0),
                                Animation({"y": 50 }, duration=1.0),
                            ],
                            loop_animations=True,
                        ),
                        Image("r2sing", media_id="r2sing",
                            persist=False,
                            x=55,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 52 }, duration=1.0),
                                Animation({"y": 50 }, duration=1.0),
                            ],
                            loop_animations=True,
                        ),
                    ],
                    duration=4.0,
                ),
                # The robots walk away together, upwards out of the screen.
                Frame(
                    [
                        Image("r1walkup", media_id="rwalk",
                            persist=False,
                            x=40,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": -20, "width":20, "height":20}, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                        Image("r2walkup", media_id="r2walk",
                            persist=False,
                            x=55,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": -20, "width":20, "height":20}, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                    ],
                    duration=3.0,
                ),
                # The robots come down again.
                Frame(
                    [
                        Image("r1walkdown", media_id="rwalk",
                            persist=False,
                            x=20,
                            y=-20,
                            width=20,
                            height=20,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 50, "width":40, "height":40 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                        Image("r2walkdown", media_id="r2walk",
                            persist=False,
                            x=80,
                            y=-20,
                            width=20,
                            height=20,
                            click_to_answer=True,
                            animations=[
                                Animation({"y": 50, "width":40, "height":40 }, duration=2.0),
                            ],
                            loop_animations=False,
                        ),
                    ],
                    duration=2.0,
                ),
                # The robots stand still, doing nothing in particular.
                Frame(
                    [
                        Image("r1stand", media_id="rstand",
                            persist=False,
                            x=20,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[]
                        ),
                        Image("r2stand", media_id="r2stand",
                            persist=False,
                            x=80,
                            y=50,
                            width=40,
                            click_to_answer=True,
                            animations=[]
                        ),
                    ],
                    duration=4.0,
                ),
            ],
            loop=True,
            media=MediaSpec(
                image={ "rstand": f"{imgdir}/robot_standing.png",
                         "rwalk": f"{imgdir}/robot_walking.png",
                         "rsing": f"{imgdir}/robot_singing.png",
                         "r2stand": f"{imgdir}/robot2_standing.png",
                         "r2walk": f"{imgdir}/robot2_walking.png",
                         "r2sing": f"{imgdir}/robot2_singing.png",
                      },
            ),
        ),
        time_estimate=17,
    )

    timeline = Timeline(
        consentPage,
        #infoPage,
        bird_page,
        robot_page

    )
