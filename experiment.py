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
    graphic_width = 100
    graphic_height = 100

    consentPage = NoConsent()
    infoPage = InfoPage(
            "Graphic components provide a way to display interactive visual animations to the participant.",
            time_estimate=5,
        )

    timeline = Timeline(
        consentPage,
        #infoPage,
        ModularPage(
            "graphic",
            prompt=Prompt(
                text="Click the green bird!",
            ),
            control=GraphicControl(
                dimensions=[graphic_width, graphic_height],
                viewport_width=1,

                frames=[
                    Frame(
                        [
                            Circle(
                                    "circle2",95,10,radius=2,
                                    attributes={"fill": "rgb(255,180,90)"},
                                ),
                            Image("Gray", media_id="birdgray",
                                    persist=True,
                                    x=10,
                                    y=50,
                                    width=20,
                                    animations=[
                                        Animation({"x":40 }, duration=2.0),
                                    ],
                                    #loop_animations=True,

                                ),

                            Image("Green", media_id="birdgreen",
                                    persist=True,
                                    x=90,
                                    y=50,
                                    width=20,
                                    click_to_answer=True,
                                    animations=[
                                        Animation({"x":55 }, duration=3.0),
                                    ],
                                ),
                        ],
                        duration=5.0,
                    ),

                ],
                loop=True,
                media=MediaSpec(
                    image={ # Use the keys of this dict as 'media_id' to refer to images in frames above
                        "birdgray" : f"{imgdir}/birdgray_animated.png",
                        "birdgreen" : f"{imgdir}/birdgreen_animated.png",
                        "birdorange" : f"{imgdir}/birdorange_animated.png",
                    },
                ),
            ),
            time_estimate=5,
        )
    )
