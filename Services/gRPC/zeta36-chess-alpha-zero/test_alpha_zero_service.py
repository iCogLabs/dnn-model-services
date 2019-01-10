import sys
import grpc

# import the generated classes
import service.service_spec.alpha_zero_pb2_grpc as grpc_bt_grpc
import service.service_spec.alpha_zero_pb2 as grpc_bt_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Service ONE - Arithmetic
        endpoint = input("Endpoint (localhost:{}): ".format(registry["alpha_zero_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["alpha_zero_service"]["grpc"])

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        default = "play"
        grpc_method = input("Method (play): ") if not test_flag else default
        if grpc_method == "":
            grpc_method = default

        default = ""
        uid = input("UID (empty): ") if not test_flag else default
        if uid == "":
            uid = default

        default = "e2e4"
        move = input("Move (e2e4): ") if not test_flag else default
        if move == "":
            move = default

        default = ""
        cmd = input("CMD (empty): ") if not test_flag else default
        if cmd == "":
            cmd = default

        stub = grpc_bt_grpc.AlphaZeroStub(channel)
        request = grpc_bt_pb2.Input(uid=uid,
                                    cmd=cmd,
                                    move=move)

        if grpc_method == "play":
            response = stub.play(request)
            print("\nresponse:")
            print("UID: {}".format(response.uid))
            print("board: \n{}".format(response.board))
            print("status: {}".format(response.status))
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)