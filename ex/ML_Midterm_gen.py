from genquiz.generator import *
from numpy import mean, exp
# import pandas as pd

# load students list
students = Student('student.xlsx')

Session_test = 'pretest'  #
# Session_test = 'posttest'
if Session_test == 'pretest':
    start_session = 1
    stop_session = 20
else:
    start_session = 11
    stop_session = 20

Q_score = 0.5
Per_session = 10  # number of quizes per session
session = 1  # number of lecteruer
len_quiz_per_session = stop_session - start_session + 1

Question_1 = 'One-versus-All algorithm มีการทำงานอย่างไร'
Sol_list_1 = ['Training ด้วย Hypothesis เท่ากับจำนวน Class โดยพิจารณา Class ที่สนใจเป็น Positive Class',
              'Training ด้วย Hypothesis เท่ากับจำนวน Class โดยพิจารณา Class ที่สนใจเป็น Negative Class',
              'Train Hypothesis โดยให้ค่าน้ำหนัก Class ต่างกัน',
              'ปรับ Hyperparameter ให้เหมาะสมกับจำนวน Class']
ans_1 = 'Training ด้วย Hypothesis เท่ากับจำนวน Class โดยพิจารณา Class ที่สนใจเป็น Positive Class'

Question_2 = 'ปัญหา High variance เกิดได้จากสาเหตุยกเว้นข้อใด'
Sol_list_2 = ['จำนวน feature มากเกินไป',
              'polynomial function ถูกกำหนดด้วย order สูงเกินไป',
              'polynomial function ถูกกำหนดด้วย order ต่ำเกินเกินไป',
              'กำหนด hypothesis function ด้วย quadratic function']
ans_2 = 'polynomial function ถูกกำหนดด้วย order ต่ำเกินเกินไป'

Question_3 = 'ปัญหา High Bias เกิดได้จากสาเหตุยกเว้นข้อใด'
Sol_list_3 = ['จำนวน feature น้อยเกินไป',
              'polynomial function ถูกกำหนดด้วย order ต่ำเกินไป',
              'polynomial function ถูกกำหนดด้วย order สูงเกินเกินไป',
              'กำหนด hypothesis function ด้วย cubic function']
ans_3 = 'polynomial function ถูกกำหนดด้วย order สูงเกินเกินไป'

Question_4 = 'ปัญหา High variance มีลักษณะอย่างไร'
Sol_list_4 = ['ลักษณะ Hypothesis มีความแปรผันไปตาม Training data และแปรผันห่างจาก Test data',
              'ลักษณะ Hypothesis มีความแปรผันไปตาม Training data และ Test data',
              'ลักษณะ Hypothesis ไม่ผันตาม Training data และแปรผันห่างจาก Test data',
              'ไม่มีข้อถูก']
ans_4 = 'ลักษณะ Hypothesis มีความแปรผันไปตาม Training data และแปรผันห่างจาก Test data'

Question_5 = 'ปัญหา Underfitting มีลักษณะอย่างไร'
Sol_list_5 = ['Hypothesis มีความเชื่อต่อการเปลี่ยนแปลงของข้อมูลในเชิงเดี่ยวมากเกินไป',
              'Hypothesis มีความเชื่อต่อการแปรผันของข้อมูลมาเกินไป',
              'Hypothesis สามารถใช้ได้ดีกับ Test data',
              'Hypothesis มีความเป็น Generalization']
ans_5 = 'Hypothesis มีความเชื่อต่อการเปลี่ยนแปลงของข้อมูลในเชิงเดี่ยวมากเกินไป'

Question_6 = 'การ penalize สามารถทำได้กับสิ่งใด'
Sol_list_6 = ['parameter',
              'hyperparameter',
              'regularization parameter',
              'feature']
ans_6 = 'parameter'

Question_7 = 'Regularization มีผลต่อ parameter ในลักษณะใด'
Sol_list_7 = ['เปลี่ยนแปลงอิทธิพลของ feature ที่ส่งผลต่อ hypothesis',
              'เปลี่ยนแปลงอิทธิพลของ parameter ที่ส่งผลต่อ hypothesis',
              'เปลี่ยนแปลงอิทธิพลของ hyperparameter ที่ส่งผลต่อ hypothesis',
              'ไม่มีข้อถูก']
ans_7 = 'เปลี่ยนแปลงอิทธิพลของ feature ที่ส่งผลต่อ hypothesis'

Question_8 = 'ข้อใดเป็นคุณสมบัติของ Discriminative Learning'
Sol_list_8 = ['Hypothesis ถูก Learning โดยอ้างอิงจาก feature ที่ทำให้เกิด Class นั้น ๆ',
              'Hypothesis ถูก Learning โดยอ้างอิงจาก Class ที่ทำให้เกิด feature นั้น ๆ',
              'Hypothesis ถูก Learning โดยอ้้างอิงจากการแปรผันของ feature',
              'Hypothesis ถูก Learning โดยอ้้างอิงจากการแปรผันของ Class']
ans_8 = 'Hypothesis ถูก Learning โดยอ้างอิงจาก feature ที่ทำให้เกิด Class นั้น ๆ'

Question_9 = 'Learning algorithm ชนิดใดมีคุณลักษณะของ hypothesis เป็นเส้นโค้งใด ๆ แทนคุณลักษณะข้อมูล'
Sol_list_9 = ['Linear Regression',
              'Logistic Regression',
              'K-nearest Neighbor',
              'Naive Bayes']
ans_9 = 'Linear Regression'

Question_10 = 'Learning algorithm ชนิดใดมีคุณลักษณะของ hypothesis เป็น Decision Boundary แทนคุณลักษณะของกลุ่มข้อมูล'
Sol_list_10 = ['Linear Regression',
               'Logistic Regression',
               'K-nearest Neighbor',
               'Naive Bayes']
ans_10 = 'Logistic Regression'

Question_11 = 'Learning algorithm ชนิดใดมีคุณลักษณะของ hypothesis เป็นการกระจายตัวของกลุ่มข้อมูล'
Sol_list_11 = ['Linear Regression',
               'Logistic Regression',
               'K-nearest Neighbor',
               'Naive Bayes']
ans_11 = 'Naive Bayes'

Question_12 = 'ข้อใดเป็นคุณสมบัติของ Discriminative Learning'
Sol_list_12 = ['Hypothesis ถูก Learning โดยอ้างอิงจาก feature ที่ทำให้เกิด Class นั้น ๆ',
               'Hypothesis ถูก Learning โดยอ้างอิงจาก Class ที่ทำให้เกิด feature นั้น ๆ',
               'Hypothesis ถูก Learning โดยอ้้างอิงจากการแปรผันของ feature',
               'Hypothesis ถูก Learning โดยอ้้างอิงจากการแปรผันของ Class']
ans_12 = 'Hypothesis ถูก Learning โดยอ้างอิงจาก Class ที่ทำให้เกิด feature นั้น ๆ'

Question_13 = 'Learning algorithm ชนิดใดที่ใช้ objective funtion ด้วย Maximization'
Sol_list_13 = ['Linear Regression',
               'Logistic Regression',
               'K-nearest Neighbor',
               'Naive Bayes']
ans_13 = 'Naive Bayes'

Question_14 = 'Lazy Learner มีการเรียนรู้อย่างไร'
Sol_list_14 = ['ปรับ parameter ด้วยวิธีการ Optimization',
               'ปรับ hyperparameter ด้วยวิธีการ Optimization',
               'เก็บข้อมูลและ normalized ข้อมูล',
               'ปรับ hyperparameter ด้วยวิธีการ Trial and Error']
ans_14 = 'เก็บข้อมูลและ normalized ข้อมูล'

Question_15 = 'ขั้นตอนใดของ Machine Learning ใช้ธีการ Trial and Error'
Sol_list_15 = ['3',
               '4',
               '5',
               '6']
ans_15 = '6'

Question_16 = 'ขั้นตอนใดของ Machine Learning เป็นการจัดการ Outlier'
Sol_list_16 = ['1',
               '2',
               '3',
               '4']
ans_16 = '2'

Question_17 = 'ปัญหาของ Outlier คืออะไร'
Sol_list_17 = ['ทำให้ hypothesis มีความแปรผันต่างจากชุดข้อมูลส่วนใหญ่',
               'ทำให้ hypothesis เกิดความทิฐิต่อชุดข้อมูล',
               'ทำให้การเรียนรู้ข้อมูลไม่สำเร็จเนื่องจาก outlier ทำให้ข้อมูลสุญหาย',
               'ทำให้การเรียนรู้ของข้อมูลลู่เข้าสู่ค่าเป้าหมายสูง']
ans_17 = 'ทำให้ hypothesis มีความแปรผันต่างจากชุดข้อมูลส่วนใหญ่'

Question_18 = 'การปรับปรุง Cost function ของ Logistic Regression มีเป้าหมายอย่างไร'
Sol_list_18 = ['เพื่อทำให้ Cost function มีคุณสมบัติเป็น Convex function',
               'เพื่อทำให้ Cost function ลู้เข้าสู่จุด Minimum ได้เร็วขึ้น',
               'เพื่อทำให้ Cost function ลู้เข้าสู่จุด Minimum ได้ช้าลง',
               'เพื่อทำให้สามารถใช้ Objective function เป็นการ Minimization ได้']
ans_18 = 'เพื่อทำให้ Cost function มีคุณสมบัติเป็น Convex function'

Question_19 = 'เป้าหมายของการทำ Cross-validation คืออะไร'
Sol_list_19 = ['เพื่อทำสอบความเหมาะสมต่อชุดข้อมูลที่หลากหลาย',
               'เพื่อทดสอบประสิทธิภาพของ Model จำนวนหลายครั้งและหาค่าเฉลี่ยของประสิทธิภาพ',
               'เพื่อทดสอบประสิทธิภาพของ Model โดยการแบ่งชุดข้อมูลทดสอบออกจากชุดเรียนรู้',
               'เพื่อเรียนรู้ Model หลายครั้ง']
ans_19 = 'เพื่อทำสอบความเหมาะสมต่อชุดข้อมูลที่หลากหลาย'

Question_20 = 'ค่าใดแสดงถึงตวามหมาะสมของ Model ต่อชุดข้อมูล'
Sol_list_20 = ['Accuracy',
               'Precision',
               'Recall',
               'R-Square']
ans_20 = 'R-Square'

cnt_stu = 0
# sum_score = 0
for student_id, student_name in students:
    all_question = []
    all_solution = []
    cnt_stu += 1
    print(cnt_stu)
    print(student_id)

    # paan gen quiz
    # ran_quiz1 = random.sample(range(1, len_quiz_per_session), Per_session)
    q_num = 0
    start_ans = 2
    letters = ['a', 'b', 'c', 'd']

    for i in range(1):  # range(start_session-1, stop_session):
        ran_quiz = random.sample(range(start_session, stop_session), Per_session)
        # print(ran_quiz)
        for j in ran_quiz:
            q_num += 1
            q_num_text = str(q_num) + ': '
            question = [Text(q_num_text)]
            img_path = None
            img_ans_list = None
            alter_question = None
            Img_ques = 'No'  # yes when answer is image
            defaultImgSize = 4

            if j == 1:
                q_text = Question_1
                Sol_list = Sol_list_1
                ans = ans_1
            elif j == 2:
                q_text = Question_2
                Sol_list = Sol_list_2
                ans = ans_2
            elif j == 3:
                q_text = Question_3
                Sol_list = Sol_list_3
                ans = ans_3
            elif j == 4:
                q_text = Question_4
                Sol_list = Sol_list_4
                ans = ans_4
            elif j == 5:
                q_text = Question_5
                Sol_list = Sol_list_5
                ans = ans_5
            elif j == 6:
                q_text = Question_6
                Sol_list = Sol_list_6
                ans = ans_6
            elif j == 7:
                q_text = Question_7
                Sol_list = Sol_list_7
                ans = ans_7
            elif j == 8:
                q_text = Question_8
                Sol_list = Sol_list_8
                ans = ans_8
            elif j == 9:
                q_text = Question_9
                Sol_list = Sol_list_9
                ans = ans_9
            elif j == 10:
                q_text = Question_10
                Sol_list = Sol_list_10
                ans = ans_10

            elif j == 11:
                q_text = Question_11
                # img_path = Fig_11
                Sol_list = Sol_list_11
                ans = ans_11
            elif j == 12:
                q_text = Question_12
                Sol_list = Sol_list_12
                # img_path = Fig_12
                ans = ans_12
            elif j == 13:
                q_text = Question_13
                # alter_question = Alter_Ques_13
                Sol_list = Sol_list_13
                ans = ans_13
            elif j == 14:
                q_text = Question_14
                # img_path = Fig_14
                Sol_list = Sol_list_14
                ans = ans_14
            elif j == 15:
                q_text = Question_15
                # img_path = Fig_15
                # defaultImgSize = 2
                Sol_list = Sol_list_15
                ans = ans_15
            elif j == 16:
                q_text = Question_16
                Sol_list = Sol_list_16
                ans = ans_16
            elif j == 17:
                q_text = Question_17
                Sol_list = Sol_list_17
                ans = ans_17
            elif j == 18:
                q_text = Question_18
                Sol_list = Sol_list_18
                ans = ans_18
            elif j == 19:
                q_text = Question_19
                Sol_list = Sol_list_19
                ans = ans_19
            elif j == 20:
                q_text = Question_20
                Sol_list = Sol_list_20
                ans = ans_20

            question.append(Text(q_text+ ' ( '+ str(Q_score) +' คะแนน)' ))
            if alter_question is not None:
                for alter in alter_question:
                    question.append(Text(alter))

            if img_path is not None:
                figure = ShowFigure(img_path, width=defaultImgSize)  # 4 inches width
                question.append(figure)

            if Img_ques == 'No':
                for ii, jj in zip(letters, Sol_list):
                    add_choice = ii + ': ' + jj
                    question.append(Text(add_choice))
                    if jj == ans:
                        sol = ii
                        # print(sol)
            elif Img_ques == 'Yes':
                for ii, jj, kk in zip(letters, Sol_list, img_ans_list):
                    add_choice = ii + ': '
                    question.append(Text(add_choice))
                    defaultImgSize = 1
                    figure = ShowFigure(kk, width=defaultImgSize)  # 4 inches width
                    question.append(figure)
                    if jj == ans:
                        sol = ii
                        # print(sol)

            Ans_pos = 'B' + str(start_ans)
            # print(q_num_text)
            # print(Ans_pos)
            # print(Q_score)
            # print('ans ', sol)
            # sum_score+=Q_score
            solution = Solution(sol, Ans_pos, score=Q_score)
            all_question.append(question)
            all_solution.append(solution)
            start_ans += 3

    # Question Sentence 1
    q_num += 1
    q_num_text = str(q_num) + ': '
    question = [Text(q_num_text)]
    Weight = [63, 72, 84, 67, 75]
    mean_Weight = mean(Weight)
    max_Weight = max(Weight)
    min_Weight = min(Weight)
    Height = [1.60, 1.83, 1.65, 1.57, 1.68]
    mean_Height = mean(Height)
    max_Height = max(Height)
    min_Height = min(Height)
    BMI = [24.61, 21.49, 30.85, 27.18, 26.57]
    ran_pos = random.sample(range(0, len(Weight)), len(Weight))
    Q_Weight = [Weight[i] for i in ran_pos]
    Q_Height = [Height[i] for i in ran_pos]
    Q_BMI = [BMI[i] for i in ran_pos]
    text_add1 = Text(
        'จงใช้ชุดข้อมูลต่อไปนี้เพื่อออกแบบ Hypothesis ของ Linear Regression เมื่อกำหนดให้ {method} เมื่อคำนวณจำนวน 2 Epoch Learning Rate = 0.01'
        'และทำนายค่า BMI เมื่อ {Fat}  (10 คะแนน)',
        {'method': ['θ\N{SUBSCRIPT ZERO}  = 26.490 θ\N{SUBSCRIPT ONE}  = 6.220 และ θ\N{SUBSCRIPT TWO}  = -6.320',
                    'θ\N{SUBSCRIPT ZERO}  = 26.710 θ\N{SUBSCRIPT ONE}  = 6.380 และ θ\N{SUBSCRIPT TWO}  = -6.140',
                    'θ\N{SUBSCRIPT ZERO}  = 26.680 θ\N{SUBSCRIPT ONE}  = 6.330 และ θ\N{SUBSCRIPT TWO}  = -6.080',
                    ],
         'Fat': ['Weight = 67 kg และ Height = 1.65 m',
                 'Weight = 62 kg และ Height = 1.75 m',
                 'Weight = 65 kg และ Height = 1.70 m']
         })
    question.append(text_add1)
    table_add1 = Table({'Weight (kg)': Q_Weight,
                        'Height (m)': Q_Height,
                        'BMI': Q_BMI})
    question.append(table_add1)

    # find solution of question 1
    # print(text_add1)
    if text_add1.random_list['method'] == 'θ\N{SUBSCRIPT ZERO}  = 26.490 θ\N{SUBSCRIPT ONE}  = 6.220 และ θ\N{SUBSCRIPT TWO}  = -6.320':
        theta_0_0 = 26.4865
        theta_1_0 = 6.2212
        theta_2_0 = -6.3208
        theta_0_1 = 26.4831
        theta_1_1 = 6.2223
        theta_2_1 = -6.3217
        error_1 = 0.1848
    elif text_add1.random_list['method'] == 'θ\N{SUBSCRIPT ZERO}  = 26.710 θ\N{SUBSCRIPT ONE}  = 6.380 และ θ\N{SUBSCRIPT TWO}  = -6.140':
        theta_0_0 = 26.7043
        theta_1_0 = 6.3809
        theta_2_0 = -6.1411
        theta_0_1 = 26.6987
        theta_1_1 = 6.3818
        theta_2_1 = -6.1422
        error_1 = 0.2820
    elif text_add1.random_list['method'] == 'θ\N{SUBSCRIPT ZERO}  = 26.710 θ\N{SUBSCRIPT ONE}  = 6.380 และ θ\N{SUBSCRIPT TWO}  = -6.140':
        theta_0_0 = 26.6746
        theta_1_0 = 6.3310
        theta_2_0 = -6.0812
        theta_0_1 = 26.6693
        theta_1_1 = 6.3319
        theta_2_1 = -6.0823
        error_1 = 0.2776


    if text_add1.random_list['Fat'] == 'Weight = 67 kg และ Height = 1.65 m':
        x1_new = 67
        x2_new = 1.65
    elif text_add1.random_list['Fat'] == 'Weight = 62 kg และ Height = 1.75 m':
        x1_new = 62
        x2_new = 1.75
    elif text_add1.random_list['Fat'] == 'Weight = 65 kg และ Height = 1.70 m':
        x1_new = 65
        x2_new = 1.70

    norm_x1 = (x1_new - mean_Weight) / (max_Weight - min_Weight)
    norm_x2 = (x2_new - mean_Height) / (max_Height - min_Height)
    pred_BMI = theta_0_1 + (theta_1_1 * norm_x1) + (theta_2_1 * norm_x2)

    sol_list = [theta_0_0,
                theta_1_0,
                theta_2_0,
                theta_0_1,
                theta_1_1,
                theta_2_1,
                error_1,
                pred_BMI]
    score_list = [1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  2,
                  2]

    all_question.append(question)
    for k in range(len(sol_list)):
        Ans_pos = 'C' + str(start_ans)
        Q_score = score_list[k]
        solution = Solution(sol_list[k], Ans_pos, score=Q_score)
        all_solution.append(solution)
        start_ans += 1
        # print(q_num_text)
        # print(Ans_pos)
        # print(score_list[k])
        # print('ans ', sol_list[k])
        # sum_score += Q_score

    # Question Sentence 2
    # Method to make predictions
    def Logis_predict(Q_Weight, Q_Height, b0, b1, b2):
        mean_Weight = mean(Q_Weight)
        max_Weight = max(Q_Weight)
        min_Weight = min(Q_Weight)
        mean_Height = mean(Q_Height)
        max_Height = max(Q_Height)
        min_Height = min(Q_Height)
        norm_W = []
        norm_H = []
        for x1, x2 in zip(Q_Weight, Q_Height):
            norm_W.append((x1 - mean_Weight) / (max_Weight - min_Weight))
            norm_H.append((x2 - mean_Height) / (max_Height - min_Height))

        return np.array([1 / (1 + exp(-1 * b0 + -1 * b1 * x1 + -1 * b2 * x2)) for x1, x2 in zip(norm_W, norm_H)])

    start_ans += 2
    q_num += 1
    q_num_text = str(q_num) + ': '
    question = [Text(q_num_text)]
    text_add2 = Text(
        'จากข้อมูลดังต่อไปนี้ จงทำนายว่าข้อมูลแต่ละลำดับเป็นคนอ้วนหรือผอม เมื่อกำหนดให้ hypothesis ของ Logistic Regression'
        ' มีค่า {LO_method} และเมื่อ h(x) มีค่ามากกว่าหรือเท่ากับ 1 กำหนดให้เป็น Positive Class ซึ่งแทนคนอ้วน (5 คะแนน)',
        {'LO_method': [
            'θ\N{SUBSCRIPT ZERO}  = 1.5705  θ\N{SUBSCRIPT ONE}  = 11.2847 และ θ\N{SUBSCRIPT TWO}  = -7.5422',
            'θ\N{SUBSCRIPT ZERO}  = 1.5680 θ\N{SUBSCRIPT ONE}  = 11.5850 และ θ\N{SUBSCRIPT TWO}  = -7.2240',
            'θ\N{SUBSCRIPT ZERO}  = 1.6400 θ\N{SUBSCRIPT ONE}  = 11.8910 และ θ\N{SUBSCRIPT TWO}  = -7.9600'
        ]
         })

    if text_add2.random_list['LO_method'] == 'θ\N{SUBSCRIPT ZERO}  = 1.5705  θ\N{SUBSCRIPT ONE}  =  11.2847 และ θ\N{SUBSCRIPT TWO}  = -7.5422':
        b0 = 1.5705
        b1 = 11.2847
        b2 = -7.5422
    elif text_add2.random_list['LO_method'] ==  'θ\N{SUBSCRIPT ZERO}  = 1.5680 θ\N{SUBSCRIPT ONE}  = 11.5850 และ θ\N{SUBSCRIPT TWO}  = -7.2240':
        b0 = 1.5680
        b1 = 11.5850
        b2 = -7.2240
    elif text_add2.random_list['LO_method'] == 'θ\N{SUBSCRIPT ZERO}  = 1.6400 θ\N{SUBSCRIPT ONE}  = 11.8910 และ θ\N{SUBSCRIPT TWO}  = -7.9600':
        b0 = 1.6400
        b1 = 11.8910
        b2 = -7.9600

    hx_logis = Logis_predict(Q_Weight, Q_Height, b0, b1, b2)
    logis_ans = [round(i) for i in hx_logis]

    alter_text = 'หมายเหตุ หากผลลัพธ์ที่ได้เป็น Positive class ให้เติมคำในคำตอบด้วยเลข 1 และหากผลลัพธ์ที่ได้เป็น Negative class ให้เติมคำในคำตอบด้วยเลข 0'
    question.append(text_add2)
    question.append(table_add1)
    question.append(Text(alter_text))

    score_list = [1,
                  1,
                  1,
                  1,
                  1]
    question.append(np.sum(score_list))
    all_question.append(question)
    for k in range(len(logis_ans)):
        Ans_pos = 'B' + str(start_ans)
        Q_score = 1
        solution = Solution(logis_ans[k], Ans_pos, score=Q_score)
        all_solution.append(solution)
        start_ans += 1
        # print(q_num_text)
        # print(Ans_pos)
        # print(Q_score)
        # print('ans ', logis_ans[k])
        # sum_score += Q_score

    # Question Sentence 3
    start_ans += 2
    q_num += 1
    q_num_text = str(q_num) + ': '
    question = [Text(q_num_text)]
    text_add3 = Text(
        'จากข้อมูลดังต่อไปนี้ จงทำนายว่าข้อมูลต่อไปนี้ {Fat} เป็นคนอ้วนหรือผอม โดยวิธี K-nearest Neighbor เมื่อกำหนดค่า K คือ'
        ' {KNN_method} และหากกำหนดให้ค่า BMI มากกว่า 22 แทนคนอ้วน (2 คะแนน)',
        {'KNN_method': [
                        '3'],
         'Fat': ['Weight = 67 kg และ Height = 1.65 m',
                 'Weight = 62 kg และ Height = 1.75 m',
                 'Weight = 65 kg และ Height = 1.70 m']

         })
    alter_text = 'หมายเหตุ หากผลลัพธ์ที่ได้เป็นคนอ้วนให้เติมคำในคำตอบด้วยเลข 1 และหากผลลัพธ์ที่ได้เป็นคนผอมให้เติมคำในคำตอบด้วยเลข 0'
    question.append(text_add3)
    question.append(table_add1)
    question.append(Text(alter_text))

    def KNN_predict(Q_Weight, Q_Height, x1_new, x2_new):
        mean_Weight = mean(Q_Weight)
        max_Weight = max(Q_Weight)
        min_Weight = min(Q_Weight)
        mean_Height = mean(Q_Height)
        max_Height = max(Q_Height)
        min_Height = min(Q_Height)
        norm_x1_new = ((x1_new - mean_Weight) / (max_Weight - min_Weight))
        norm_x2_new = ((x2_new - mean_Height) / (max_Height - min_Height))
        dist = []
        for x1, x2 in zip(Q_Weight, Q_Height):
            norm_W = ((x1 - mean_Weight) / (max_Weight - min_Weight))
            norm_H = ((x2 - mean_Height) / (max_Height - min_Height))
            dist.append(np.sqrt(((norm_W-norm_x1_new)**2)+((norm_H-norm_x2_new)**2)))

        return dist
    if text_add3.random_list['Fat'] == 'Weight = 67 kg และ Height = 1.65 m':
        x1_new = 67
        x2_new = 1.65
    elif text_add3.random_list['Fat'] == 'Weight = 62 kg และ Height = 1.75 m':
        x1_new = 62
        x2_new = 1.75
    elif text_add3.random_list['Fat'] == 'Weight = 65 kg และ Height = 1.70 m':
        x1_new = 65
        x2_new = 1.70

    dist = KNN_predict(Q_Weight, Q_Height, x1_new, x2_new)
    idx = sorted(range(len(dist)), key=lambda k: dist[k])
    KNN_BMI = [Q_BMI[i] for i in idx[:3] if Q_BMI[i] > 22]
    if len(KNN_BMI) >= 2:
        sol = 1
    else:
        sol = 0

    Ans_pos = 'B' + str(start_ans)
    Q_score = 2
    all_question.append(question)
    solution = Solution(sol, Ans_pos, score=Q_score)
    all_solution.append(solution)
    # print(q_num_text)
    # print(Ans_pos)
    # print(Q_score)
    # print('ans ', sol)
    # sum_score += Q_score

    # Question Sentence 4
    start_ans += 3
    q_num += 1
    q_num_text = str(q_num) + ': '
    question = [Text(q_num_text)]
    text_add4 = Text(
        'จากข้อมูลดังต่อไปนี้ จงทำนายว่าข้อมูลต่อไปนี้ {Fat} ประมาณค่าBMI โดยวิธี K-nearest Neighbor เมื่อกำหนดค่า K คือ'
        ' {KNN_method} (2 คะแนน)',
        {'KNN_method': [
                        '3'],
         'Fat': ['Weight = 67 kg และ Height = 1.65 m',
                 'Weight = 62 kg และ Height = 1.75 m',
                 'Weight = 65 kg และ Height = 1.70 m']

         })
    alter_text = 'หมายเหตุ หากผลลัพธ์ที่ได้เป็นคนอ้วนให้เติมคำในคำตอบด้วยเลข 1 และหากผลลัพธ์ที่ได้เป็นคนผอมให้เติมคำในคำตอบด้วยเลข 0'
    question.append(text_add4)
    question.append(table_add1)
    Pred_KNN_BMI = [Q_BMI[i] for i in idx[:3]]
    sol = np.sum(Pred_KNN_BMI)/len(Pred_KNN_BMI)

    Ans_pos = 'B' + str(start_ans)
    Q_score = 2
    all_question.append(question)
    solution = Solution(sol, Ans_pos, score=Q_score)
    all_solution.append(solution)

    # print(q_num_text)
    # print(Ans_pos)
    # print(Q_score)
    # print('ans ', sol)
    # sum_score += Q_score

    # Question Sentence 5
    q_num += 1
    q_num_text = str(q_num) + ': '
    question = [Text(q_num_text)]
    text_add5 = Text(
        'จงเขียนฟังก์ชันสำหรับการ update parameter (θ) ของ Logistic Regression เป็น pseudo code '
        'โดยฟังก์ชันสามารถกำหนดจำนวน feature ของ input ได้และให้ output คือ list ของ parameter (θ)'
        ' โดยให้นักศึกษาทำลงในกระดาษทดและแนบมาในการส่งคำตอบ (6 คะแนน)')
    question.append(text_add5)
    all_question.append(question)

    # print(sum_score)

    Quiz(student_id,
         student_name,
         all_question,
         all_solution,
         question_path='./Midterm_exam',
         solution_path='./Midterm_sol'
         )
