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


class Exp(psynet.experiment.Experiment):
    label = "Graphics demo"

    # asset_storage = S3Storage("psynet-tests", "graphics")
    imgdir = "/static"

    timeline = Timeline(
        NoConsent(),
        InfoPage(
            "Graphic components provide a way to display interactive visual animations to the participant.",
            time_estimate=5,
        ),
        ModularPage(
            "graphic",
            prompt=Prompt(
                text="Leandra7 Singing Bird but with Animated PNG das reinfährt!",
            ),
            control=GraphicControl(
                dimensions=[200, 200],
                viewport_width=1,

                frames=[
                    Frame(
                        [Image( "AnimatedPNG", media_id="Apng",
                                persist=True,
                                x=100,  # Adjust as necessary for centering
                                y=100,  # Adjust as necessary for centering
                                width=200,  # Set to the width of your viewport
                                height=200,  # Set to the height of your viewport
                                anchor_x=0.5,
                                anchor_y=0.5,
                            ),

                         Image( "background_image_id", media_id="background_image",
                                persist=True,
                                x=100,  # Adjust as necessary for centering
                                y=100,  # Adjust as necessary for centering
                                width=200,  # Set to the width of your viewport
                                height=200,  # Set to the height of your viewport
                                anchor_x=0.5,
                                anchor_y=0.5,
                            ),

                            Image( "AnimatedPNGG", media_id="Apng",
                                persist=True,
                                x=50,  # Adjust as necessary for centering
                                y=50,  # Adjust as necessary for centering
                                width=100,  # Set to the width of your viewport
                                height=100,  # Set to the height of your viewport
                                anchor_x=0.5,
                                anchor_y=0.5,
                            ),

                        Image( "birdONE", media_id="logorr",
                                x=200,
                                y=50,
                                width=50,
                                click_to_answer=True,
                                animations=[
                                    Animation({"x":75 }, duration=2 ),
                                    #Animation( {"x": 100,"hide": False }, duration=2 ),
                                ],
                            ),
                        ],
                    ),

                ],
                loop=True,
                media=MediaSpec(
                    image=dict(
                        logo=f"{imgdir}/logo.png",
                        logorr="/static/Birdie-APNG.png",
                        background_image="/static/World_1-FG.png",
                        Apng="static/TransparentA.png")
                    ),

            ),
            time_estimate=5,
        ),
        DebugResponsePage(),
    )
