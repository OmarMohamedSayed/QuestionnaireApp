<template>
  <v-card
    flat
  >
    <v-form 
      class="multi-col-validation mt-6"
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-card-text>
        <v-row>
          <v-col
            md="6"
            cols="12"
          >
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="البريد الألكتروني"
              required
              outlined
              dense
            ></v-text-field>
          </v-col>

          <v-col
            md="6"
            cols="12"
          >
            <v-text-field
              v-model="name"
              label="الاسم بالكامل"
              dense
              outlined
              :counter="25"
              :rules="nameRules"
              required
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            md="6"
          >
            <v-text-field
              v-model="number"
              label="رقم التليفون"
              :counter="11"
              :rules="numberRules"
              dense
              type="number"
              outlined
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            md="4"
          >
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="date"
                  label="تاريخ الميلاد"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  outlined
                  dense
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date"
                :active-picker.sync="activePicker"
                :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                min="1950-01-01"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col
            cols="12"
            md="2"
          >
            <v-select
              v-model="gender"
              :items="genderitems"
              :rules="[v => !!v || 'الرجاء إدخال النوع الخاص بك']"
              label="النوع"
              required
              outlined
              dense
            ></v-select>
          </v-col>
          <v-col
            cols="12"
            md="6"
          >
            <v-text-field
              v-model="address"
              :rules="addressRules"
              label="العنوان"
              :counter="40"
              dense
              outlined
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="6"
          >
            <v-select
              v-model="nationality"
              :items="this.countries"
              :rules="[v => !!v || 'الرجاء إدخال جنسيتك']"
              label="جنسية"
              required
              outlined
              dense
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
      <div class="pa-3">

        <v-card-text>
          <v-row>
            <v-col cols="12">
              <div class="text-center">
                <v-btn
                  color="primary"
                  class="me-3 mt-4"
                  :disabled="!this.valid"
                  @click='validate'
                >
                  التالي
                </v-btn>
                <v-btn
                  color="secondary"
                  outlined
                  class="mt-4"
                  type="reset"
                  @click.prevent="reset"
                >
                  إعاده
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </div>
    </v-form>
    
  </v-card>
</template>

<script>

export default {
  props: {
    accountData: {
      type: Object,
      default: () => {},
    },
  },
  data () {
      return {
        valid: true,
        name: '',
        nameRules: [
          v => !!v || 'الرجاء إدخال اسمك',
          v => (v && v.length <= 25) || 'يجب أن يكون الاسم أقل من 25 حرفًا',
        ],
        email: '',
        emailRules: [
          v => !!v || 'الرجاء إدخال البريد الإلكتروني الخاص بك',
          v => /.+@.+\..+/.test(v) || 'يجب ان يكون البريد الاكتروني صحيح',
        ],
        number:'',
        numberRules: [
          v => (v && v.length == 11) || 'يجب أن يكون رقم الهاتف صحيح',
        ],
        address:'',
        addressRules:[
              v => (v && v.length <= 40) || 'يجب أن يكون العنوان أقل من 40 حرفًا',
        ],
        activePicker: null,
        date: null,
        menu: false,
        gender: null,
        genderitems: [
          'ذكر',
          'أنثى',
        ],
        nationality:null,
        countries: [
          'بنغلاديش',
          'باربادوس',
          'باربادوس',
          'البرازيل',
          'فرنسا',
          'مصر'
        ],
      }
    },
    watch: {
      menu (val) {
        val && setTimeout(() => (this.activePicker = 'YEAR'))
      },
    },
    methods: {
      save (date) {
        this.$refs.menu.save(date)
      },

      validate () {
        if(this.$refs.form.validate()){
          var accountData = {
            "name": this.name,
            "email": this.email,
            "phone_number": this.number,
            "address": this.address,
            "nationality": this.nationality,
            "birthday": this.date,
            "gender": this.gender,
            "customeranswer": []
          }
          this.$store.commit('SET_ACCOUNT_DATA',accountData)
          this.$emit("clicked", 2)
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      
    },
  setup() {
    return {
    }
  },
}
</script>
