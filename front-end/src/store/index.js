import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accountData:[],
  },
  mutations: {
    SET_ACCOUNT_DATA (state, payload) {
      state.accountData = payload
    },
  },
  actions: {
    async newcustomer(context,data){
      var res = ""
      await axios.post(`${process.env.VUE_APP_API_ACCOUNT}`,data).then(response => {
        if(response.status == 201){
          res = "تم ادخال المعلومات" 
        }
        else {
          res = "تم تسجيل البريد الإلكتروني من قبل ، يرجى إدخال بريد جديد"
        }
      })
      .catch(error => {
        res = "تم تسجيل البريد الإلكتروني من قبل ، يرجى إدخال بريد جديد"
      });
      return res
    },
    async question(context){
      var res = []
      await axios.get(`${process.env.VUE_APP_API_QUESTIONS}`).then(response => {
        if(response.status == 200){
          res = response.data
          
          var result;
          var count = 0;
          if(res){
            for (var item in res){
                if (Math.random() < 1/++count)
                  result = res[item];
            }
            res = result
          }
          else {
          res = ["لا يوجد سؤال"]
          }
        }
        else {
          res = ["يوجد خطأ"]
        }
      })
      .catch(error => {
        res = "يوجد خطأ"
      });
      return res
    },
    async answerscounter(context,question_id){
      var res = ""
      await axios.get(`${process.env.VUE_APP_API_CUSTOMERANSWERS}${question_id}`).then(response => {
        if(response.status == 200){
          res = response.data
        }
        else {
          res = "يوجد خطأ"
        }
      })
      .catch(error => {
        res = "يوجد خطأ"
      });
      return res
    },

  },
})
