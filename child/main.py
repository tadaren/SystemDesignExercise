import server
import StepMotor4


def main():
    server.run(StepMotor4.open, StepMotor4.close)


if __name__ == '__main__':
    main()