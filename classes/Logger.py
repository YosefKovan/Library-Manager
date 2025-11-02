import time

class Logger:

    @staticmethod
    def action_type(action_type, details):

        match action_type:
            case "INFO" :
                 print(f"[INFO] {details} | Time : ", time.ctime())
            case "ERROR" :
                print(f"[Error] Error Occurred - {details} | Time : ", time.ctime())