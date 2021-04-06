import streamlit as st
import seaborn as sns
import pandas as pd
from PIL import Image
import pickle
import datetime as dt
import base64
import numpy as np
import streamlit.components.v1 as components

import psycopg2
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

des=[]
#stt.set_theme({'primary': '#1b3668'})

st.title("Health Care Application")
with st.sidebar:
    components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://assets7.lottiefiles.com/packages/lf20_mR5H7A.json"  background="transparent"  speed="1"  style="width: 300px; height: 250px;"  loop  autoplay></lottie-player>

       
       """,
    height=250,
     )
    
st.sidebar.header("Welcome")
select=st.sidebar.selectbox("Select",['Home','Diabetes','Heart','Kidney','Patient_Details','Language and Libraries and Cloud'])

if select=='Home':

    st.header("Homepage")
    st.subheader("This Application allows user to know whether he/she has")
    
    st.subheader("`Diabetes`,`Heart` and `Kidney` Disease.")
    file_ = open("healthcare.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="700" alt="cat gif">',
    unsafe_allow_html=True,
      )
    

    #col1, col2, col3 = st.beta_columns([4,3,3])

    #with col1:
        ##st.header("Diabetes")
        #st.image("image.jpg", use_column_width=True)

    #with col2:
        #st.header("Heart")
        #st.image("H.jpg", use_column_width=True)
    #with col3:
        #st.header("Kidney")
        #st.image("K.jpg", use_column_width=True)
    #img=Image.open("C:/Users/USER/Downloads/healthcare.gif")
    #st.image(img, format = 'GIF')
    #st.write("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)")
    #st.write("![Answers](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gehealthcare.com%2Farticle%2Fhealthcare-needs-moonshots-this-is-what-a-digital-one-looks-like&psig=AOvVaw0nwxr3rpSODPYTOeoienCo&ust=1613660765559000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLiCzIOZ8e4CFQAAAAAdAAAAABAD)")
    
    #st.markdown('<img src="C:/Users/USER/Downloads/healthcare.gif"/>', unsafe_allow_html=True)
    #st.markdown(
    #f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    #unsafe_allow_html=True,
       # )
    #img=Image.open("C:/Users/USER/Downloads/healthcare.gif")
    #st.image(img,width=700,caption="Health care")

    
if select=='Diabetes':
    
    D=st.sidebar.selectbox("Diabetes Section",['About Diabetes','Actual Dataset','Used Dataset','Diabetes Prediction'])
    img1=Image.open('images/DD.jpg')
    st.sidebar.image(img1,width=310)
    
    if D=='About Diabetes':
        st.header("Diabetes")
        st.markdown(""" **Diabetes mellitus**, commonly known as **diabetes**, is a metabolic disease that causes high blood sugar. The hormone insulin moves sugar from the blood into your cells to be stored or used for energy. With diabetes, your body either doesn’t make enough insulin or can’t effectively use the insulin it does make.""")
        
        st.markdown("""Untreated high blood sugar from diabetes can damage your nerves, eyes, kidneys, and other organs.""")
        st.markdown("""There are a few different types of diabetes:""")
        st.markdown("""*  **Type 1 diabetes** an **autoimmune disease**. The immune system attacks and destroys cells in the **pancreas**, where insulin is made. It’s unclear what causes this attack. About **10 percent** of people with diabetes have this type.""")
        st.markdown("""*  **Type 2 diabetes** occurs when your body becomes resistant to **insulin**, and sugar builds up in your blood.""")
        st.markdown("""*  **Prediabetes** occurs when your blood sugar is higher than normal, but it’s not high enough for a diagnosis of type 2 diabetes.""")
        st.markdown("""*  **Gestational** diabetes is high blood sugar during pregnancy. Insulin-blocking hormones produced by the placenta cause this type of diabetes.""")
        st.markdown(""" A rare condition called **diabetes insipidus** is not related to diabetes mellitus, although it has a similar name. It’s a different condition in which your kidneys remove too much fluid from your body.""")

        st.header("Symptoms of diabetes")
        st.markdown("""Diabetes symptoms are caused by rising blood sugar.""")
        st.subheader("General symptoms")
        st.markdown("""The general symptoms of diabetes include:""")
        st.markdown("""
                    * increased hunger
                    * increased thirst
                    * weight loss
                    * frequent urination
                    * blurry vision
                    * extreme fatigue
                    * sores that don’t heal
                    """)


        st.subheader("Symptoms in men")
        st.markdown(""" In addition to the general symptoms of diabetes, men with diabetes may have a decreased sex drive, erectile dysfunction (ED), and poor muscle strength. """)
        st.subheader("Symptoms in women")
        st.markdown("""Women with diabetes can also have symptoms such as urinary tract infections, yeast infections, and dry, itchy skin.""")
        st.subheader("Type 1 diabetes")
        st.markdown("""Symptoms of type 1 diabetes can include:""")
        st.markdown("""
                    * extreme hunger
                    * increased thirst
                    * unintentional weight loss
                    * frequent urination
                    * blurry vision
                    * tiredness
                    
                    """)
       
        st.subheader("Type 2 diabetes")
        st.markdown("""Symptoms of type 2 diabetes can include:""")
        st.markdown("""
                    * increased hunger
                    * increased thirst
                    * increased urination
                    * blurry vision
                    * tiredness
                    * sores that are slow to heal
                    
                    """)
        st.markdown("""It may also cause recurring infections. This is because elevated glucose levels make it harder for the body to heal.""")
        st.subheader("Gestational diabetes")
        st.markdown("""Most women with gestational diabetes don’t have any symptoms. The condition is often detected during a routine blood sugar test or oral glucose tolerance test that is usually performed between the 24th and 28th weeks of gestation. In rare cases, a woman with gestational diabetes will also experience increased thirst or urination.""")
        
        st.header("Treatment of diabetes")
        st.markdown("""Doctors treat diabetes with a few different medications. Some of these drugs are taken by mouth, while others are available as injections.""")
        st.subheader("Type 1 diabetes")
        st.markdown("""Insulin is the main treatment for type 1 diabetes. It replaces the hormone your body isn’t able to produce.""")
        st.markdown("""There are four types of insulin that are most commonly used. They’re differentiated by how quickly they start to work, and how long their effects last:""")
        st.markdown("""
                   * Rapid-acting insulin starts to work within 15 minutes and its effects last for 3 to 4 hours.
                   * Short-acting insulin starts to work within 30 minutes and lasts 6 to 8 hours.
                   * Intermediate-acting insulin starts to work within 1 to 2 hours and lasts 12 to 18 hours.
                   * Long-acting insulin starts to work a few hours after injection and lasts 24 hours or longer.

             """)
        st.subheader("Type 2 diabetes")
        st.markdown("""Diet and exercise can help some people manage type 2 diabetes. If lifestyle changes aren’t enough to lower your blood sugar, you’ll need to take medication""")
        st.markdown("""These drugs lower your blood sugar in a variety of ways:""")
        st.markdown("""
                       
                 | Types of drug       | How they work          | Example(s)  |
                 | ------------- |:-------------:| -----:|
                 | Alpha-glucosidase inhibitors     | Slow your body’s breakdown of sugars and starchy foods | Acarbose (Precose) and miglitol (Glyset) |
                 | Thiazolidinediones | Help insulin work better | Pioglitazone (Actos) and rosiglitazone (Avandia) |
                 | SGLT2 inhibitors | Release more glucose into the urine | Canagliflozin (Invokana) and dapagliflozin (Farxiga)  |
                   """)
        
        st.subheader("Gestational diabetes")
        st.markdown("""You’ll need to monitor your blood sugar level several times a day during pregnancy. If it’s high, dietary changes and exercise may or may not be enough to bring it down.""")
        st.markdown("""According to the Mayo Clinic, about 10 to 20 percent of women with gestational diabetes will need insulin to lower their blood sugar. Insulin is safe for the growing baby.""")
        st.header("Diabetes prevention")
        st.markdown("""Type 1 diabetes isn’t preventable because it’s caused by a problem with the immune system. Some causes of type 2 diabetes, such as your genes or age, aren’t under your control either.""")
        st.markdown("""Yet many other diabetes risk factors are controllable. Most diabetes prevention strategies involve making simple adjustments to your diet and fitness routine.""")
        st.markdown("""If you’ve been diagnosed with prediabetes, here are a few things you can do to delay or prevent type 2 diabetes:""")
        st.markdown("""
                      * Get at least 150 minutes per week of aerobic exercise, such as walking or cycling.
                      * Cut saturated and trans fats, along with refined carbohydrates, out of your diet.
                      * Eat more fruits, vegetables, and whole grains.
                      * Eat smaller portions.
                      * Try to lose 7 percentTrusted Source of your body weight if you’re overweight or obese.

                    """)
        st.header("Diabetes in pregnancy")
        st.markdown("""Women who’ve never had diabetes can suddenly develop gestational diabetes in pregnancy. Hormones produced by the placenta can make your body more resistant to the effects of insulin.  """)
        
        st.markdown(""" Some women who had diabetes before they conceived carry it with them into pregnancy. This is called pre-gestational diabetes.  """)
        
        st.markdown("""Gestational diabetes should go away after you deliver, but it does significantly increase your risk for getting diabetes later. """)
        st.markdown(""" About half of women with gestational diabetes will develop type 2 diabetes within 5 to 10 years of delivery, according to the International Diabetes Federation (IDF).""")
        st.markdown(""" Having diabetes during your pregnancy can also lead to complications for your newborn, such as jaundice or breathing problems.""")
    if D=="Actual Dataset":
        st.header("Dataset")
        #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='diabetes_patient')
        conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")
        cur = conn.cursor()
        cur.execute("select  * from diabetes_patients")
        outputs=cur.fetchall()
        cols=cur.description
        for i in range(0,len(cols)):
            des.append(cols[i][0])
            #st.write(des)
        print("executed")
        df1=pd.DataFrame(outputs,columns=des)
        #st.write(len(df1))
        number=st.number_input("select the rows ",10,len(df1))
        df1=df1.head(number)
        st.table(df1)

        if st.checkbox("Show shape"):
            data=df1.shape
            radio=st.radio("Show rows and columns",("Rows" , "Columns"))
            if radio=="Rows":
                st.write(data[0])
            elif radio=="Columns":
                st.write(data[1])
            else:
                st.write(df1.shape)
        if st.checkbox('selectcolumns'):
            column=df1.columns.tolist()
            selected=st.multiselect("show",column)
            new_df=df1[selected]
            st.dataframe(new_df)
        
        if st.checkbox("Summary"):
            st.write(df1.describe().T)
        if st.checkbox("data types"):
            st.write(df1.dtypes)
        st.subheader("Data visualisation ")
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        #correlation
        if st.checkbox("Correlation"):
            st.write(sns.heatmap(df1.corr(),annot=True))
            st.pyplot()
        if st.checkbox("Pairplot"):
            st.write(sns.pairplot(df1.iloc[:,:5]))
            st.pyplot()
        
        conn.close()


    if D=="Used Dataset":
        
        st.header("Dataset used for Predicting Diabetes")
        data1=pd.read_csv("D.csv")
        data1=data1.iloc[:,2:]
        number1=st.number_input("select rows",10,len(data1))
        st.table(data1.head(number1))

        st.subheader("Columns description")

        st.markdown("""


              * **Pregnancies:** Number of times pregnant
              * **Glucose:** Plasma glucose concentration over 2 hours in an oral glucose tolerance test
              * **BloodPressure:** Diastolic blood pressure (mm Hg)
              * **SkinThickness:** Triceps skin fold thickness (mm)
              * **Insulin:** 2-Hour serum insulin (mu U/ml)
              * **BMI:** Body mass index (weight in kg/(height in m)2)
              * **DiabetesPedigreeFunction:** Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)
              * **Age:** Age (years)
              * **Outcome:** Class variable (0 if non-diabetic, 1 if diabetic)







            """)
        

    if D=="Diabetes Prediction":
        #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='diabetes_patient')
        conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

        cur = conn.cursor()
        sql = "INSERT INTO d_details (Id, Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,dia_or_not,Date,Time) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        st.header("Diabetes Prediction")

        df=pd.read_csv("D.csv")
        df=df.iloc[:,2:]
        st.write(df.head())
        ids=st.text_input("enter the patient Id:")
        p = st.number_input("enter the pregnancy:")
        g = st.number_input("enter the glucose:")
        bp= st.number_input("enter the bloodpressure:")
        sti= st.number_input("enter the skinthickness:")
        ins = st.number_input("enter the insulin:")
        bmi= st.number_input("enter the bmi:")
        dpf = st.number_input("enter the diabetespedigreefunction:")
        a= st.number_input("enter the age:")
        output=[]
        lst=[p,g,bp,sti,ins,bmi,dpf,a]
        
        
        
        print(p,g,bp,sti,ins,bmi,dpf,a)
        #inserts=[ids,p,g,bp,sti,ins,bmi,dpf,a]
        #print(inserts)
        dates=dt.datetime.now()
        dates=str(dates)
        dates=dates.split()
        #print(dates[0])
        #print(dates[1])
        output.append(lst)
        with open("model1","rb")as f:
            model=pickle.load(f)
        button=st.button("predict")
        if button:
            outcome=model.predict(output)
            print(type(ids),type(p),type(g),type(bp),type(sti),type(ins),type(bmi),type(dpf),type(a),type(dates[0]),type(dates[1]))
            print(dates[0],dates[1])
        #st.write(outcome)
        #st.write()
            if(outcome==1):
                #st.write(outcome)
                
                print(outcome[0])
                ids=int(ids)
                cur.execute(sql,(ids,p,g,bp,sti,ins,bmi,dpf,a,outcome[0],dates[0],dates[1]))
                conn.commit()
                conn.close()
                st.write("Diabetic")
            else:
                ids=int(ids)
                print(outcome[0])
                cur.execute(sql,(ids,p,g,bp,sti,ins,bmi,dpf,a,outcome[0],dates[0],dates[1]))
                
                conn.commit()
                conn.close()
                st.write("Non-Diabetic")
if select=="Heart":
     H=st.sidebar.selectbox("Heart Disease Section",['About Heart Disease','Actual Dataset','Used Dataset','Heart Disease Prediction'])

     img1=Image.open("images/H1.jpg")
     st.sidebar.image(img1,width=300)
     if H=="About Heart Disease":
         st.header("Heart Disease")
         st.markdown('''
          Heart disease is the leading cause of death in the United States, according to the Centers for Disease Control and Prevention (CDC)Trusted Source. In the United States, 1 in every 4 deaths in is the result of a heart disease. That’s about 610,000 people who die from the condition each year.
          
          ''')
         st.markdown('''
         Heart disease doesn’t discriminate. It’s the leading cause of death for several populations, including white people, Hispanics, and Black people. Almost half of Americans are at risk for heart disease, and the numbers are rising.

         ''')
         st.header("Different types of Heart Disease")
         st.markdown("""Heart disease encompasses a wide range of cardiovascular problems. Several diseases and conditions fall under the umbrella of heart disease. Types of heart disease include:""")
         st.markdown("""
                      * **Arrhythmia.** An arrhythmia is a heart rhythm abnormality.
                      * **Atherosclerosis.** Atherosclerosis is a hardening of the arteries.
                      * **Cardiomyopathy.** This condition causes the heart’s muscles to harden or grow weak.
                      * **Congenital heart defects.** Congenital heart defects are heart irregularities that are present at birth.
                      * **Coronary artery disease (CAD).** CAD is caused by the buildup of plaque in the heart’s arteries. It’s sometimes called ischemic heart disease.
                      * **Heart infections.** Heart infections may be caused by bacteria, viruses, or parasites.
           """)
         st.markdown("""The term cardiovascular disease may be used to refer to heart conditions that specifically affect the blood vessels.""")
         st.header("What are the symptoms of heart disease?")
         st.markdown("Different types of heart disease may result in a variety of different symptoms")
         st.subheader("Arrhythmias")
         st.markdown("""Arrhythmias are abnormal heart rhythms. The symptoms you experience may depend on the type of arrhythmia you have — heartbeats that are too fast or too slow. Symptoms of an arrhythmia include:""")
         st.markdown("""
                  * lightheadedness
                  * fluttering heart or racing heartbeat
                  * slow pulse
                  * fainting spells
                  * dizziness
                  * chest pain

                      """)
         st.subheader("Atherosclerosis")
         st.markdown(""" Atherosclerosis reduces blood supply to your extremities. In addition to chest pain and shortness of breath, symptoms of atherosclerosis include:  """)
     
         st.markdown("""

                  * coldness, especially in the limbs
                  * numbness, especially in the limbs
                  * unusual or unexplained pain
                  * weakness in your legs and arms
 
                """)
         st.subheader("Congenital heart defects ")
         st.markdown(""" Congenital heart defects are heart problems that develop when a fetus is growing. Some heart defects are never diagnosed. Others may be found when they cause symptoms, such as:  """)
     
         st.markdown("""
                     * blue-tinged skin
                     * swelling of the extremities
                     * shortness of breath or difficulty breathing
                     * fatigue and low energy
                     * irregular heart rhythm
                     """)

         st.subheader("Heart infections")
         st.markdown(""" The term heart infection may be used to describe conditions such as endocarditis or myocarditis. Symptoms of a heart infection include:     """)
     
         st.markdown("""
                      * chest pain
                      * chest congestion or coughing
                      * fever
                      * chills
                      * skin rash
                      """)
         st.header("What are the symptoms of heart disease in women?")
         st.markdown("""Women often experience different signs and symptoms of heart disease than men, specifically with regards to CAD and other cardiovascular diseases.""")
         st.markdown(""" In fact, a 2003 study looked at the symptoms most often seen in women who’d experienced a heart attack. The top symptoms didn’t include “classic” heart attack symptoms such as chest pain and tingling. Instead, the study reported that women were more likely to say they experienced anxiety, sleep disturbances, and unusual or unexplained fatigue.   """)
         st.markdown("""Common heart disease symptoms in women include: """)
         st.markdown("""
                        * dizziness
                        * paleness
                         * shortness of breath or shallow breathing
                         * lightheadedness
                         * fainting or passing out
                         * anxiety
                         * nausea
                         * vomiting
                         * jaw pain
                         * neck pain
                         * back pain
                         * indigestion or gaslike pain in the chest and stomach
                         * cold sweats
                         """)
         st.header("What causes heart disease?")
         st.markdown("""Heart disease is a collection of diseases and conditions that cause cardiovascular problems. Each type of heart disease is caused by something entirely unique to that condition. Atherosclerosis and CAD result from plaque buildup in the arteries. Other causes of heart disease are described below.""")
         st.subheader("Arrhythmia causes")
         st.markdown("""
                     * diabetes
                     * CAD
                     * heart defects, including congenital heart defects
                     * medications, supplements, and herbal remedies
                     * high blood pressure (hypertension)
                     * excessive alcohol or caffeine use
                     * substance use disorders
                     * stress and anxiety  
                     *  existing heart damage or disease
                         """)
         st.subheader("Cardiomyopathy causes")
         st.markdown("""Several types of cardiomyopathy exist. Each type is the result of a separate condition.""")
         st.markdown("""
                   * **Dilated cardiomyopathy.** It’s unclear what causes this most common type of cardiomyopathy, which leads to a weakened heart. It may be the result of previous damage to the heart, such as the kind caused by drugs, infections, and heart attack. It may also be an inherited condition or the result of uncontrolled blood pressure
                   * **Hypertrophic cardiomyopathy.** This type of heart disease leads to a thicker heart muscle. It’s usually inherited.
                   * **Restrictive cardiomyopathy. It’s often unclear what leads to this type of cardiomyopathy, which results in rigid heart walls. Possible causes may include scar tissue buildup and a type of abnormal protein buildup known as amyloidosis.""")
         st.header("How is heart disease diagnosed?")
         st.markdown("""Your doctor may order several types of tests and evaluations to make a heart disease diagnosis. Some of these tests can be performed before you ever show signs of heart disease. Others may be used to look for possible causes of symptoms when they develop.""")
         st.subheader("Physical exams and blood tests")
         st.markdown("""The first thing your doctor will do is perform a physical exam and take an account of the symptoms you’ve been experiencing. Then they’ll want to know your family and personal medical history. Genetics can play a role in some heart diseases. If you have a close family member with heart disease, share this information with your doctor.""")
         st.markdown("""Blood tests are frequently ordered. This is because they can help your doctor see your cholesterol levels and look for signs of inflammation.""")
         st.header("Noninvasive tests")
         st.markdown("""A variety of noninvasive tests may be used to diagnose heart disease.""")
         st.markdown("""
                    * **Electrocardiogram (ECG or EKG).** This test can monitor your heart’s electrical activity and help your doctor spot any irregularities.
                    * **Echocardiogram.** This ultrasound test can give your doctor a close picture of your heart’s structure.
                    * **Stress test.** This exam is performed while you complete a strenuous activity, such as walking, running, or riding a stationary bike. During the test, your doctor can monitor your heart’s activity in response to changes in physical exertion.
                     * **Carotid ultrasound.** To get a detailed ultrasound of your carotid arteries, your doctor may order this ultrasound test.
                     * **Holter monitor.** Your doctor may ask you to wear this heart rate monitor for 24 to 48 hours. It allows them to get an extended view of your heart’s activity.
                     * **Tilt table test.** If you’ve recently experienced fainting or lightheadedness when standing up or sitting down, your doctor may order this test. During it, you’re strapped to a table and slowly raised or lowered while they monitor your heart rate, blood pressure, and oxygen levels.
                     * **CT scan.** This imaging test gives your doctor a highly-detailed X-ray image of your heart.
                     * **Heart MRI.** Like a CT scan, a heart MRI can provide a very detailed image of your heart and blood vessels.
                  """)
     if H=="Actual Dataset":
         st.header("Dataset")
         #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='heart_patients')
         conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

         cur = conn.cursor()
         cur.execute("select  * from heart_patients")
         outputs=cur.fetchall()
         cols=cur.description
         for i in range(0,len(cols)):
             des.append(cols[i][0])
             #st.write(des)
         print("executed")
         df1=pd.DataFrame(outputs,columns=des)
         #st.write(len(df1))
         number=st.number_input("select the rows ",10,len(df1))
         df1=df1.head(number)
         st.table(df1)

         if st.checkbox("Show Shape"):
             st.write(df1.shape)
         if st.checkbox("Show shape"):
            data=df1.shape
            radio=st.radio("Show rows and coulmns",("Rows" , "Columns"))
            if radio=="Rows":
                
                st.write(data[0])
            elif radio=="Columns":
                st.write(data[1])
            else:
                st.write(df1.shape)
         if st.checkbox('selectcolumns'):
             column=df1.columns.tolist()
             selected=st.multiselect("show",column)
             new_df=df1[selected]
             st.dataframe(new_df)
        
         if st.checkbox("Summary"):
             st.write(df1.describe().T)
         if st.checkbox("data types"):
             st.write(df1.dtypes)
         st.subheader("Data visualisation ")
        
         st.set_option('deprecation.showPyplotGlobalUse', False)
         #correlation
         if st.checkbox("Correlation"):
             st.write(sns.heatmap(df1.corr(),annot=True))
             st.pyplot()
         if st.checkbox("Pairplot"):
            st.write(sns.pairplot(df1.iloc[:,:5]))
            st.pyplot()
                
         conn.close()
     if H=="Used Dataset":
         st.header("Dataset used for Predicting Heart Disease")
         data1=pd.read_csv("cleve1.csv")
         data1=data1.iloc[:,2:]
         number1=st.number_input("select rows",10,len(data1))
         st.table(data1.head(number1))

         st.subheader("Columns description")
         st.markdown("""
               * **Age:** displays the age of the individual.
               * **Sex:** displays the gender of the individual using the following format :
                          1 = male ,
                          0 = female
               * **Chest-pain type:** displays the type of chest-pain experienced by the individual using the following format :
                      1 = typical angina,
                      2 = atypical angina,
                      3 = non — anginal pain,
                      4 = asymptotic
               * **Resting Blood Pressure:** displays the resting blood pressure value of an individual in mmHg (unit)
               * **Serum Cholestrol:** displays the serum cholesterol in mg/dl (unit),
               * **Fasting Blood Sugar:** compares the fasting blood sugar value of an individual with 120mg/dl.
                           If fasting blood sugar > 120mg/dl then : 1 (true),
                           else : 0 (false)
               * **Resting ECG :** displays resting electrocardiographic results :
                            0 = normal,
                            1 = having ST-T wave abnormality,
                            2 = left ventricular hyperthrophy,
               * **Max heart rate achieved :** displays the max heart rate achieved by an individual.
               * **Exercise induced angina :**
                            1 = yes,
                            0 = no
               * **ST depression induced by exercise relative to rest:** displays the value which is an integer or float.
               * **Peak exercise ST segment :**
                            1 = upsloping,
                            2 = flat,
                            3 = downsloping
               * **Number of major vessels (0–3) colored by flourosopy :** displays the value as integer or float.
               * **Thal : displays the thalassemia :**
                            3 = normal,
                            6 = fixed defect,
                            7 = reversible defect
               * **Diagnosis of heart disease :** Displays whether the individual is suffering from heart disease or not :
                            0 = absence,
                            1, 2, 3, 4 = present.

                       """)
     if H=="Heart Disease Prediction":
         #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='heart_patients')
         conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

         cur = conn.cursor()

         sql = "INSERT INTO h_details (Id, age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,h_or_not,Date,Time) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
         #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
         st.header("Heart Disease Prediction")
         global morf
         df=pd.read_csv("cleve1.csv")
         df=df.iloc[:,2:]
         st.write(df.head())
         ids=st.text_input("enter the patient Id:")
         p = st.number_input("enter the age:")
         #g = st.number_input("enter the sex:")
         #morf=st.radio("Select",("Male","Female"))
         
              
             
         morf=st.radio("Select",("Male","Female"))
         if morf=="Male":
             morf=1
         else:
             morf=0
         st.write(morf)
                 
    
    
         cps=st.selectbox("Select Chest-Pain type",("Typical angina","Atypical angina","Non-anginal pain","Asymptotic"))
         if cps=="Typical angina":
             cps=1
         if cps=="Atypical angina":
             cps=2
         if cps=="Non-anginal pain":
             cps=3
         if cps=="Asymptotic":
             cps=4
         st.write(cps)
                
         restbp= st.number_input("enter the Resting bloodpressure:")
         ch= st.number_input("enter the Serum Cholestrol:")
         fb=st.radio("Select Fating Blood Sugar",("Greaterthan120mg","None"))
         if fb=="Greaterthan120mg":
             fb=1
         else:
             fb=0
         st.write(fb)


         recg=st.selectbox("Select",("Normal","ST-T wave abnormality","Left ventricular hyperthrophy"))
         if recg=="Normal":
             recg=0
         if recg=="ST-T wave abnormality":
             recg=1
         if recg=="Left ventricular hyperthrophy":
             recg=2
         st.write(recg)
         mht=st.number_input("Enter Max Heart Rate")


         exan=st.radio("Select Exercise induced angina",("Yes","No"))
         if exan=="Yes":
             exan=1
         else:
             exan=0
         st.write(exan)

         olds=st.number_input("ST depression induced by exercise relative to rest")
         pk=st.selectbox("Select Peak exercise ST segment",("upsloping","flat","downsloping"))
         if pk=="upsloping":
             pk=1
         if pk=="flat":
             pk=2
         if pk=="downsloping":
             pk=3
         st.write(pk)
         fo=st.number_input("Enter the Number of major vessels (0–3) colored by flourosopy")
         tha=st.radio("Select thalassemia",("Normal","Fixed defect","Reversible defect"))
         if tha=="Normal":
             tha=3
         if tha=="Fixed defect":
             tha=6
         if tha=="Reversible defect":
             tha=7
         st.write(tha)
         lst=[ids,p,morf,cps,restbp,ch,fb,recg,mht,exan,olds,pk,fo,tha]
         print(lst)
         output=[]
         lsts=[p,morf,cps,restbp,ch,fb,recg,mht,exan,olds,pk,fo,tha]
         output.append(lsts)
         
         
             
         

                 
         
         #output=[]
         #lst=[p,g,bp,sti,ins,bmi,dpf,a]
         #inserts=[ids,p,g,bp,sti,ins,bmi,dpf,a]
         #print(inserts)
         dates=dt.datetime.now()
         dates=str(dates)
         dates=dates.split()
         #print(dates[0])
         #print(dates[1])
         #output.append(lst)
         
         with open("Heart_model","rb")as f:
             
             model=pickle.load(f)
         button=st.button("predict")
         if button:
             
             outcome=model.predict(output)
             #st.write(outcome)
         #st.write()
           
             if(outcome==1):
                 #st.write(outcome)
                 #print(outcome[0])
                 ids=int(ids)
                 print(ids,p,morf,cps,restbp,ch,fb,recg,mht,exan,olds,pk,fo,tha,outcome[0],dates[0],dates[1])
                 cur.execute(sql,(ids,p,morf,cps,restbp,ch,fb,recg,mht,exan,olds,pk,fo,tha,outcome[0],dates[0],dates[1]))
                 conn.commit()
                 conn.close()
                 st.markdown(""" ## Heart Disease""")
             else:
                 ids=int(ids)
                 #print(outcome[0])
                 cur.execute(sql,(ids,p,morf,cps,restbp,ch,fb,recg,mht,exan,olds,pk,fo,tha,outcome[0],dates[0],dates[1]))
                
                 conn.commit()
                 conn.close()
                 st.markdown(""" ## No Heart Disease""")
if select=="Kidney":
     K=st.sidebar.selectbox("Kidney Disease Section",['About Kidney Disease','Actual Dataset','Used Dataset','Kidney Disease Prediction'])

     img1=Image.open("images/K1.jpg")
     st.sidebar.image(img1,width=300)
     if K=="About Kidney Disease":
         st.header("Chronic Kidney Disease")
         st.markdown("""
                  Chronic kidney disease, also called chronic kidney failure, describes the gradual loss of kidney function. Your kidneys filter wastes and excess fluids from your blood, which are then excreted in your urine. When chronic kidney disease reaches an advanced stage, dangerous levels of fluid, electrolytes and wastes can build up in your body.

              """)
         st.markdown("""
                    In the early stages of chronic kidney disease, you may have few signs or symptoms. Chronic kidney disease may not become apparent until your kidney function is significantly impaired.
                 
                 """)

         st.markdown("""

                  Treatment for chronic kidney disease focuses on slowing the progression of the kidney damage, usually by controlling the underlying cause. Chronic kidney disease can progress to end-stage kidney failure, which is fatal without artificial filtering (dialysis) or a kidney transplant.
                  
                    """)
         st.subheader("Symptoms")
         st.markdown("""Signs and symptoms of chronic kidney disease develop over time if kidney damage progresses slowly. Signs and symptoms of kidney disease may include:""")
         st.markdown("""
                        * Nausea
                        * Vomiting
                        * Loss of appetite
                        * Fatigue and weakness
                        * Sleep problems
                        * Changes in how much you urinate
                        * Decreased mental sharpness
                        * Muscle twitches and cramps
                        * Swelling of feet and ankles
                        * Persistent itching
                        * Chest pain, if fluid builds up around the lining of the heart
                        * Shortness of breath, if fluid builds up in the lungs
                        * High blood pressure (hypertension) that's difficult to control
            """)
         st.subheader("Causes")

         st.markdown(""" Chronic kidney disease occurs when a disease or condition impairs kidney function, causing kidney damage to worsen over several months or years.   """)
         st.markdown("""  Diseases and conditions that cause chronic kidney disease include: """)
         st.markdown("""

                     * Type 1 or type 2 diabetes
                     * High blood pressure
                     *  Glomerulonephritis (gloe-mer-u-low-nuh-FRY-tis), an inflammation of the kidney's filtering units (glomeruli)
                     * Interstitial nephritis (in-tur-STISH-ul nuh-FRY-tis), an inflammation of the kidney's tubules and surrounding structures
                     * Polycystic kidney disease
                     * Prolonged obstruction of the urinary tract, from conditions such as enlarged prostate, kidney stones and some cancers
                     * Vesicoureteral (ves-ih-koe-yoo-REE-tur-ul) reflux, a condition that causes urine to back up into your kidneys
                     * Recurrent kidney infection, also called pyelonephritis (pie-uh-low-nuh-FRY-tis)

                    """)
         st.subheader("Risk Factors")
         st.markdown(""" Factors that may increase your risk of chronic kidney disease include:""")
         st.markdown("""

                     * Diabetes
                     * High blood pressure
                     * Heart and blood vessel (cardiovascular) disease
                     * Smoking
                     * Obesity
                     * Being African-American, Native American or Asian-American
                     * Family history of kidney disease
                     * Abnormal kidney structure
                      * Older age
                   """)
         st.subheader("Complications")
         st.markdown("""Chronic kidney disease can affect almost every part of your body. Potential complications may include:""")
         st.markdown("""
                              * Fluid retention, which could lead to swelling in your arms and legs, high blood pressure, or fluid in your lungs (pulmonary edema)
                              * A sudden rise in potassium levels in your blood (hyperkalemia), which could impair your heart's ability to function and may be life-threatening
                              * Heart and blood vessel (cardiovascular) disease
                              * Weak bones and an increased risk of bone fractures
                              *  Anemia
                              * Decreased sex drive, erectile dysfunction or reduced fertility
                              * Damage to your central nervous system, which can cause difficulty concentrating, personality changes or seizures
                              * Decreased immune response, which makes you more vulnerable to infection
                              * Pericarditis, an inflammation of the saclike membrane that envelops your heart (pericardium)
                              * Pregnancy complications that carry risks for the mother and the developing fetus
                              * Irreversible damage to your kidneys (end-stage kidney disease), eventually requiring either dialysis or a kidney transplant for survival

                              """)
         st.subheader("Prevention")
         st.markdown("""To reduce your risk of developing kidney disease:""")
         st.markdown("""
               *  **Follow instructions on over-the-counter medications.** When using nonprescription pain relievers, such as aspirin, ibuprofen (Advil, Motrin IB, others) and acetaminophen (Tylenol, others), follow the instructions on the package. Taking too many pain relievers could lead to kidney damage and generally should be avoided if you have kidney disease. Ask your doctor whether these drugs are safe for you.
               *  **Maintain a healthy weight.** If you're at a healthy weight, work to maintain it by being physically active most days of the week. If you need to lose weight, talk with your doctor about strategies for healthy weight loss. Often this involves increasing daily physical activity and reducing calories.
               *  **Don't smoke.** Cigarette smoking can damage your kidneys and make existing kidney damage worse. If you're a smoker, talk to your doctor about strategies for quitting smoking. Support groups, counseling and medications can all help you to stop.
               *  **Manage your medical conditions with your doctor's help.** If you have diseases or conditions that increase your risk of kidney disease, work with your doctor to control them. Ask your doctor about tests to look for signs of kidney damage.

                    """)
     if K=="Actual Dataset":
         st.header("Dataset")
         #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='kidney_patients')
         conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")
         cur = conn.cursor()
         cur.execute("select  * from kidney_patients")
         outputs=cur.fetchall()
         cols=cur.description
         for i in range(0,len(cols)):
             des.append(cols[i][0])
         #st.write(des)
         print("executed")
         df1=pd.DataFrame(outputs,columns=des)
         #st.write(len(df1))
         number=st.number_input("select the rows ",10,len(df1))
         df1=df1.head(number)
         st.table(df1)

         #if st.checkbox("Show Shape"):
             #st.write(df1.shape)
         if st.checkbox("Show shape"):
            data=df1.shape
            radio=st.radio("Show rows and coulmns",("Rows" , "Columns"))
            if radio=="Rows":
                st.write(data[0])
            elif radio=="Columns":
                st.write(data[1])
            else:
                st.write(df1.shape)
         if st.checkbox('selectcolumns'):
             column=df1.columns.tolist()
             selected=st.multiselect("show",column)
             new_df=df1[selected]
             st.dataframe(new_df)
        
         if st.checkbox("Summary"):
             st.write(df1.describe().T)
         if st.checkbox("data types"):
             st.write(df1.dtypes)
         st.subheader("Data visualisation ")
        
         st.set_option('deprecation.showPyplotGlobalUse', False)
         #correlation
         if st.checkbox("Correlation"):
             st.write(sns.heatmap(df1.corr(),annot=True))
             st.pyplot()
         if st.checkbox("Pairplot"):
             st.write(sns.pairplot(df1.iloc[:,:5]))
             st.pyplot()
                
         conn.close()
             
     if K=="Used Dataset":
         st.header("Dataset used for Predicting Kidney Disease")
         data1=pd.read_csv("kid.csv")
         #data1=data1.iloc[:,1:]
         #data1=data1.iloc[:,:-1]
         data1=data1[['age', 'bp', 'al', 'pcc', 'bgr', 'bu', 'sc', 'hemo', 'pcv', 'htn', 'dm','appet', 'class']]
         number1=st.number_input("select rows",10,len(data1))
         st.table(data1.head(number1))

         st.subheader("Columns description")
         st.markdown("""
          * **Id- patient Id's**,
          * **bp- blood_pressure**,
          * **sg- specific_gravity**,
          * **al- albumin**,
          * **su- sugar**,
          * **rbc- red_blood_cells**,
          * **pc- pus_cell**,
          * **pcc- pus_cell_clumps**,
          * **ba- bacteria**,
          * **bgr- blood_glucose_random**,
          * **bu-  blood_urea**,
          * **sc- serum_creatinine**,
          * **sod- sodium**,
          * **pot- potassium**,
          * **hemo- haemoglobin**,
          * **pcv- packed_cell_volume**,
          * **wc- white_blood_cell_count**,
          * **rc- red_blood_cell_count**,
          * **htn- hypertension**,
          * **dm- diabetes_mellitus**,
          * **cad- coronary_artery_disease**,
          * **appet-  appetite**
          * **pe- pedal_edema**
          * **ane-  anemia**  

                 """)
         
     if K=="Kidney Disease Prediction":
         
         #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='kidney_patients')
         conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

         cur = conn.cursor()

         sql = "INSERT INTO k_details (Id, Age,BloodPressure,Albumin,pus_cell_clumps,blood_glucose_random,blood_urea,serum_creatinine,haemoglobin,packed_cell_volume,hypertension,diabetes_mellitus,appetite,kd_or_not,Date,Time) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
         #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
         st.header("Kidney Disease Prediction")

         df=pd.read_csv("kid.csv")
         df=df[['age', 'bp', 'al', 'pcc', 'bgr', 'bu', 'sc', 'hemo', 'pcv', 'htn', 'dm','appet', 'class']]
         st.write(df.head())
         ids=st.text_input("enter the patient id")
         a=st.number_input("Enter the patient Age")
         b=st.number_input("Enter the Blood Pressure")
         #b=st.number_input("Emter the Specific gravity")
         c=st.number_input("Enter the Albumin")
         #d=st.number_input("Enter the Sugar")
         #e=st.number_input("Enter the Red blood cells ")
         #f1=st.number_input("Enter the Pus cell")
         d=st.number_input("Enter the Pus cell clumps")
         #h=st.number_input("Enter the Bacteria")
         e=st.number_input("Enter the Blood glucose")
         f1=st.number_input("Enter the Blood urea")
         g=st.number_input("Enter the Serum creatinine")
         #l=st.number_input("Enter the Sodium amount")
         #m=st.number_input("Enter the Potassium amount")
         h=st.number_input("Enter the haemoglobin")
         i=st.number_input("Enter the packed cell volume")
         #p=st.number_input("Enter the white blood cell count")
         #q=st.number_input("Enter the red_blood_cell_count")
         j=st.number_input("Enter the hypertension")
         k=st.number_input("Enter the diabetes_mellitus")
         #t=st.number_input("Enter the coronary_artery_disease")
         l=st.number_input("Enter the appetite")
         #v=st.number_input("Enter the pedal_edema")
         #w=st.number_input("Enter the anemia")

         lst=[a,b,c,d,e,f1,g,h,i,j,k,l]
         print(len(lst))
         dates=dt.datetime.now()
         dates=str(dates)
         dates=dates.split()
         output=[]
         output.append(lst)
         with open("Kidney_model","rb") as f:
             models=pickle.load(f)
         if st.button("Predict"):
             outcome=models.predict(output)
             #st.write(outcome)
             
             if(outcome==1):
                 
                 #st.write(outcome)
                 #print(outcome[0])
                 ids=int(ids)
                 #print(ids,a,bp,b,c,d,e,f1,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,outcome[0],dates[0],dates[1])
                 cur.execute(sql,(ids,a,b,c,d,e,f1,g,h,i,j,k,l,outcome[0],dates[0],dates[1]))
                 conn.commit()
                 conn.close()
                 st.markdown(""" ## Kidney Disease""")
             else:
                 ids=int(ids)
                 #print(outcome[0])
                 cur.execute(sql,(ids,a,b,c,d,e,f1,g,h,i,j,k,l,outcome[0],dates[0],dates[1]))
                
                 conn.commit()
                 conn.close()
                 st.markdown(""" ## No Kidney Disease""")
if select=="Patient_Details":
    des=[]
    st.header("Diabetes Patient Details")
    #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='diabetes_patient')
    conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

    cur = conn.cursor()
    cur.execute("select  * from d_details")
    outputs=cur.fetchall()
    cols=cur.description
    for i in range(0,len(cols)):
        des.append(cols[i][0])
    #st.write(des)
    print("executed")
    df1=pd.DataFrame(outputs,columns=des)
    #st.write(len(df1))
    #number=st.number_input("select the rows ",10,len(df1))
    df1=df1
    st.table(df1)
    dess=[]
    st.header("Heart Patient Details")
    #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='heart_patients')
    conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

    cur = conn.cursor()
    cur.execute("select  * from h_details")
    outputss=cur.fetchall()
    cols=cur.description
    for i in range(0,len(cols)):
        dess.append(cols[i][0])
    #st.write(des)
    print("executed")
    df1=pd.DataFrame(outputss,columns=dess)
    #st.write(len(df1))
    #number=st.number_input("select the rows ",10,len(df1))
    df1=df1
    st.table(df1)

    de=[]
    st.header("Kidney Patient Details")
    #conn=pymysql.connect( host='localhost', user='root',password = "1234", db='kidney_patients')
    conn = psycopg2.connect(database = "ddh71vtuoav358", user = "rysgupirvzoyjj", password = "319d7912d34dff38fb4c1b6494c43fba95c43d161126697df24d3bde83485502", host = "ec2-23-21-229-200.compute-1.amazonaws.com", port = "5432")

    cur = conn.cursor()
    cur.execute("select  * from k_details")
    outpu=cur.fetchall()
    cols=cur.description

    for i in range(0,len(cols)):
        de.append(cols[i][0])
    #st.write(des)
    print("executed")
    df1=pd.DataFrame(outpu,columns=de)
    #st.write(len(df1))
    #number=st.number_input("select the rows ",10,len(df1))
    #df1['kd_or_not'].style.highlight_max(axis=0)
    st.table(df1)
    conn.close()
    
if select=="Language and Libraries and Cloud":
    st.header("Programming Language , Libraries and Cloud")

    col1, col2 = st.beta_columns(2)
    image='images/pythons.jpg'
    original = Image.open(image)
    #col1.header("Original")
    col1.image(original, use_column_width=True)

    image='images/stream.jpg'
    original = Image.open(image)
    #col2.header("Old")
    col2.image(original, use_column_width=True)

    coll, coll2 = st.beta_columns(2)

    image='images/anaconda-meta.jpg'
    original = Image.open(image)
    #coll.header("Original")
    coll.image(original, use_column_width=True)

    image='images/jupy.jpg'
    original = Image.open(image)
    #coll2.header("Old")
    coll2.image(original, use_column_width=True)



    col, co2 = st.beta_columns(2)
    image='images/pan.jpg'
    original = Image.open(image)
    #coll.header("Original")
    col.image(original, use_column_width=True)

    image='images/num.jpg'
    original = Image.open(image)
    #coll2.header("Old")
    co2.image(original, use_column_width=True)


    c1, c2 = st.beta_columns(2)
    image='images/images.jpg'
    original = Image.open(image)
    #coll.header("Original")
    c1.image(original, use_column_width=True)

    image='images/pot.jpg'
    original = Image.open(image)
    #coll2.header("Old")
    c2.image(original, use_column_width=True)

    image="images/her.jpg"
    original=Image.open(image)
    st.image(original,use_column_width=True)




    st.write(" ")

    st.write(" ")


    
    st.write(" ")

    st.write(" ")


    
    st.write(" ")

    st.write(" ")


    

    st.write("Made with love    :sparkling_heart::sparkling_heart::sparkling_heart::sparkling_heart::sparkling_heart::sparkling_heart::sparkling_heart:")
    
    components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_wJStSx.json"  background="transparent"  speed="1"  style="width: 500px; height: 300px;"  loop  autoplay></lottie-player>

    """,
    height=600,
     )




         
         
         


        
                

         
         

        
         



