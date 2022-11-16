from deeppavlov import build_model
def model():

    model = build_model('squad_bert', download=True)
    res_list = model(['DeepPavlov is a library for NLP and dialog systems.'], ['What is DeepPavlov?'])

    print ("\n" +"Input: List[context, question] -> ['DeepPavlov is a library for NLP and dialog systems.'], ['What is DeepPavlov?']")
    print("Output: List[answer, start_character, logit] -> ",  res_list)
    print("Output: Only answer -> ", only_res(res_list))

def only_res(res):
    return res[0]

if __name__ == '__main__':
    model()


