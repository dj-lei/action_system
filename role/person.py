from body.body import Body


class Person(Body):
    def __init__(self) -> None:
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

        self.thigh_L = ('support', 0, 0, 0, 0)
        self.shin_L = ('support', 0, 0, 0, 0)
        self.foot_L = ('support', 0, 0, 0, 0)
        self.toe_L = ('friction', 0, 0, 0, 0)

        self.thigh_R = self.body.thigh_R
        self.shin_R = self.body.thigh_R.shin
        self.foot_R = self.body.thigh_R.shin.foot
        self.toe_R = self.body.thigh_R.shin.foot.toe
        
        self.thigh_R = ('support', 0, 0, 0, 0)
        self.shin_R = ('support', 0, 0, 0, 0)
        self.foot_R = ('support', 0, 0, 0, 0)
        self.toe_R = ('friction', 0, 0, 0, 0)

    def walk(self):
        # thigh_R support -> motion
        self.thigh_R = ('motion', -0.3, 0, 0, 30) 
        # shin_R support -> 

        # toe_L friction -> trigger root bone move 
        self.toe_L = freeze

    def run(self):
        pass