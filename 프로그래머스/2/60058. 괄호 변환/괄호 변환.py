def solution(p):
    def is_correct(input_string):
        count = 0
        for s in input_string:
            if s == "(":
                count += 1

            if s == ")":
                count -= 1

            if count < 0:
                return False

        return True

    def recursive(string):
        if string == "":
            return ""
        start_val = 0
        for i in range(1, len(string)+1):
            u = string[start_val:i]
            v = string[i:]
            if u.count(")") == u.count("("):

                u_is_correct = is_correct(u)
                if u_is_correct:
                    correct_v = recursive(v)
                    return u + correct_v
                else:
                    correct_v = recursive(v)
                    correct_u = "("
                    correct_u = correct_u + correct_v + ")"
                    for i in range(1, len(u)-1):
                        if u[i] == "(":
                            correct_u = correct_u + ")"
                        elif u[i] == ")":
                            correct_u = correct_u + "("

                    return correct_u

                break

    return recursive(p)