from picamera2 import Picamera2

LARGEUR = 640
HAUTEUR = 480

class Camera():
    def __init__(self):
        self.picam2 = Picamera2()

        config = self.picam2.create_video_configuration(
            main={"format": "YUV420", "size": (LARGEUR, HAUTEUR)},
            controls={
                "FrameDurationLimits": (33333, 33333),
                "NoiseReductionMode": 0,
                "Sharpness": 0.0,
                "AwbEnable": False,
                "AeEnable": False,
            }
        )

        self.picam2.configure(config)
        self.picam2.start(show_preview=False)

        self.picam2.set_controls({
            "ExposureTime": 8000,
            "AnalogueGain": 1.0,
            "ColourGains": (1.5, 1.5)
        })

    def capture(self):
        return self.picam2.capture_array()