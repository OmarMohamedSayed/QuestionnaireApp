<template>
  <v-card
    flat
    class="mt-5"
  >
    <v-form>
      <v-card-text class="pt-3">
        <v-row>
          <v-col
            cols="12"
            sm="4"
            md="6"
            class="d-none d-sm-flex justify-center position-relative"
          >
            <v-img
              contain
              max-width="170"
              src="@/assets/images/3d-characters/pose-m-1.png"
              class="character"
            ></v-img>
          </v-col>
          <v-col
            cols="12"
            sm="8"
            md="6"
          >
            <v-container fluid>
              <v-subheader>
                <h1>{{question}}</h1>
              </v-subheader>
              <v-list>
                <template v-for="(item, index) in items">
                  <v-list-item
                    v-if="item.Choice_text"
                    :key="item.Choice_text"
                  >
                        <v-checkbox
                          v-model="selected"
                          :label="item.Choice_text"
                          :value="item.Choice_text"
                        ></v-checkbox>
                  </v-list-item>

                  <v-divider
                    v-if="index < 2"
                    :key="index"
                  ></v-divider>
                </template>
              </v-list>
            </v-container>
          </v-col>
        </v-row>
      </v-card-text>
      
      <div class="pa-3 text-center">
        <v-card-text>
          <v-btn
            color="primary"
            class="me-3 mt-2"
            @click='insertQuestionData'
          >
            التالي
          </v-btn>
          <v-btn
            color="secondary"
            outlined
            class="mt-2"
            @click='$emit("clicked", 1)'
          >
            السابق
          </v-btn>
        </v-card-text>
      </div>
    </v-form>
    <v-snackbar
        v-model="notificationbar"
        absolute
        centered
        color="success"
        elevation="24"
        text
        >
          <h2 class="text-lg-center">{{ notificationtext }}</h2>
    </v-snackbar>

  </v-card>
</template>

<script>
import { ref } from '@vue/composition-api'

export default {
  created() {
     this.getQuestion()
    },
  methods: {
    async getQuestion(){
      var res = await this.$store.dispatch("question")
      if(res != []){
        this.question = res["question_text"]
        this.items = res["choice"]
        this.questionID = res["id"]
      }
    },
    async insertQuestionData(){
      var req = await this.$store.state.accountData
      if(this.selected !== [""] && this.selected !== [] ){
        var select =[]
        for(var i in this.selected){
            select.push({
              "customersolutions": this.selected[i],
              "question": this.questionID,
            })
        }

        req["customeranswer"] = select
        var res = await this.$store.dispatch("newcustomer",req)
        this.notificationbar= true
        this.notificationtext = res
        if(res == "تم ادخال المعلومات"  ){
          this.$emit("analysis",this.questionID)
          this.$emit("clicked", 3)
        }
        
      }else {
        this.$store.dispatch("newcustomer",req)
        if(res == "تم ادخال المعلومات"  ){
          this.$emit("analysis",this.questionID)
          this.$emit("clicked", 3)
        }
      }
    }
  },
  data () {
      return {
        valid:true,
        selected: [],
        inset: true,
        question:"",
        questionID:"",
        notificationbar: false,
        notificationtext: "",
        items: [],
      }
  },
}
</script>

<style lang="scss" scoped>

.character {
  position: absolute;
  top: 40px;
}
</style>
