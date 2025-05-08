import json

effect_array = []
questions_array = []
with open('../app/src/main/res/raw/questions.json', "r",encoding='utf8') as my_file:
    for line in my_file:
        questions_array.append(line.replace("\n", ""))

with open('../app/src/main/res/raw/effect.json', "r",encoding='utf8') as my_file: 
    for line in my_file:
        json_acceptable_string = line.replace("\n", "").replace("'", "\"")
        effect_array.append(json.loads(json_acceptable_string))

pre_string = '\App\Models\Questoes::insert('
pos_string = ');'
string_carregada = ''
for item in range(0,len(questions_array)):
    string_carregada += "\n['desc_questao' =>'{}','econ' => {},'dipl' => {},'govt'=> {},'scty' =>{}],".format(questions_array[item],effect_array[item]["econ"],effect_array[item]["dipl"],effect_array[item]["govt"],effect_array[item]["scty"])
    
string_carregada[:len(string_carregada)-1]
final = pre_string+string_carregada[:len(string_carregada)-1]+pos_string
print(final)
