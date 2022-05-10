<template>
<div class="container-fluid">
  <label for="name">请输入要删除的主机名</label>
  <input type="text" v-model="name">
  <p></p>
  <button class="btn btn-success" @click="sub">提交</button>
</div>
</template>

<script>
import config from "@/config";

export default {
  name: "del_host",
  data() {
    return {
      name: ''
    }
  },
  methods: {
    sub() {
      this.$http.get(config.Mini_URL + '/deletehost/' + this.name).then(res => {
        if (res.status === 200) {
          window.alert('删除成功！')
        }
      }).catch(() => {
        window.alert('删除失败！请检查输入是否正确')
      })
    }
  }
}
</script>

<style scoped>

</style>