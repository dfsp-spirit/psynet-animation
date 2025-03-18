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
    #imgdir = "/animations"
    imgdir = "/static"

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
                dimensions=[200, 200],
                viewport_width=1,

                frames=[
                    Frame(
                        [Image("Gray", media_id="birdgray",
                                persist=True,
                                x=100,
                                y=100,
                                width=200,
                                height=200,
                                anchor_x=0.5,
                                anchor_y=0.5,
                                animations=[
                                    Animation({"x":75 }, duration=2 ),
                                ],

                            ),

                         Image("Green", media_id="birdgreen",
                                persist=True,
                                x=500,
                                y=100,
                                width=200,
                                height=200,
                                anchor_x=0.5,
                                anchor_y=0.5,
                                animations=[
                                    Animation({"x":300 }, duration=2 ),
                                ],
                            ),
                        ],
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
