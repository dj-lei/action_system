from body.body import Body


class Person(Body):
    def __init__(self):
        super().__init__()
        self.action = {
            'thigh_L': [],
            'thigh_R': []
        }

        self.body = Body()

        self.thigh_L = self.body.thigh_L
        self.shin_L = self.body.thigh_L.shin
        self.foot_L = self.body.thigh_L.shin.foot
        self.toe_L = self.body.thigh_L.shin.foot.toe

        self.thigh_R = self.body.thigh_R
        self.shin_R = self.body.thigh_R.shin
        self.foot_R = self.body.thigh_R.shin.foot
        self.toe_R = self.body.thigh_R.shin.foot.toe

    def walk(self):
        # thigh_R support -> motion
        thigh_R_data = [
            (2680, 0, 0, 0.5),
            (0, 0, 0, 0.5),
            (2200, 0, 0, -1),
            (0, 0, 0, 0.1),
            (-200, 0, 0, -2)
        ]

        for keyframe in thigh_R_data:
            self.thigh_R.estimate(keyframe)
        # shin_R support -> 

        # toe_L friction -> trigger root bone move 

    def run(self):
        pass