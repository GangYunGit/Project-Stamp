<template>
  <div>
    <div style="">
        <b-nav tabs justified>
        <b-nav-item><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
        <b-nav-item active><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
        <b-nav-item><router-link :to="{ name:'InitialLogin' }">Recommended</router-link></b-nav-item>
        </b-nav>
    </div>
    <div class="p-4 row" align-v="center" style="background-color: #BDFCFE; height: 70vh;">
      <div class="container justify-content-md-center p-4 col-md-6" style="background-color:#FBFEAB">
        <h2 class="p-1">후기 수정하기</h2>
        <br>
        <p>영화를 보고 느낀 점을 남겨주세요.</p>
        <b-form-textarea
        id="textarea-small"
        size="sm"
        rows="6"
        placeholder="후기는 100자를 초과할 수 없습니다."
        v-model="newReview"
      ></b-form-textarea>
        <!-- <textarea name="" id="" cols="30" rows="5" v-model="newReview"></textarea> -->
        <br>
        <b-button class='m-3' variant="outline-primary"  @click="modifyReview">수정</b-button>
        <router-link :to="{ name:'BookView' }"><b-button class='m-3' variant="outline-dark">취소</b-button></router-link>
      </div>
    </div>
    <FooterView />
  </div>
</template>

<script>
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

import FooterView from '@/components/FooterView'

const API_URL = 'http://localhost:8000'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
    name: 'ModifyView',
    components: {
      FooterView,
    },
    data() {
        return {
            newReview: null,
        }
    },
    created() {
        this.oldReview()
    },
    methods: {
        modifyReview() {
            // console.log(this.newReview)
            if (this.newReview.length > 100) {
                alert('후기는 100자 이내여야 합니다.')
            } else {
                axios({
                method: 'put',
                url: `${API_URL}/albums/${this.$route.params.pk}/review_create/`,
                data: {
                    user: this.$store.state.user_pk,
                    review: this.newReview,
                },
                // headers: {
                //     Authorization: `Token ${this.$store.state.token}`
                // },
            })
            .then(() => {
                this.$router.push({ name: 'BookView' })
            })
            .catch((error) => {
                console.log(error)
            })
            }
        },
        oldReview() {
            const albumContent = this.$store.state.albums.filter(album => {
            if (album.id === this.$route.params.pk) {
              return album
            }
          })
            this.newReview = albumContent[0].review
        },
    },
}
</script>

<style>

</style>