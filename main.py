from bbcon import *
from behaviour import *
from arbitrator import *

from avoid_collision import *
from bull import *
from follow_line import *

from sensob import *
from motob import *
from zumo_button import *

def main():
    print("Waiting for press")
    ZumoButton().wait_for_press()
    print("Button pressed...")

    ultrasonic = UltraSonic()
    ultrasonic.update()
    ultrasonic.update()
    camera = Camera()
    reflect = Reflect()

    motob = Motob()
    arbitrator = Arbitrator()

    avoid_collision = AvoidCollision()
    avoid_collision.add_sensob(ultrasonic)

    bull = Bull()
    bull.add_sensob(camera)

    follow_line = FollowLine()
    follow_line.add_sensob(reflect)

    motob_array = [motob]
    sensob_array = [ultrasonic, camera, reflect]

    bbcon = Bbcon(sensob_array, motob_array, arbitrator, [], [])
    bbcon.add_behaviour(avoid_collision)
    bbcon.add_behaviour(bull)
    bbcon.add_behaviour(follow_line)

    bbcon.update_all_behaviours()

    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()
