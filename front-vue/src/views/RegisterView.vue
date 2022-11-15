<template>
  <div>
    <h1>회원가입</h1>
    <ul class="tab-pane fade" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
      <form>

        <!-- Name input -->
        <div class="form-outline mb-4">
          <input type="text" id="registerName" class="form-control" />
          <label class="form-label" for="registerName">Name</label>
        </div>

        <!-- Username input -->
        <div class="form-outline mb-4">
          <input type="text" id="registerUsername" class="form-control" />
          <label class="form-label" for="registerUsername">Username</label>
        </div>

        <!-- Email input -->
        <div class="form-outline mb-4">
          <input type="email" id="registerEmail" class="form-control" />
          <label class="form-label" for="registerEmail">Email</label>
        </div>

        <!-- Password input -->
        <div class="form-outline mb-4">
          <input type="password" id="registerPassword" class="form-control" />
          <label class="form-label" for="registerPassword">Password</label>
        </div>

        <!-- Repeat Password input -->
        <div class="form-outline mb-4">
          <input type="password" id="registerRepeatPassword" class="form-control" />
          <label class="form-label" for="registerRepeatPassword">Repeat password</label>
        </div>

        <!-- Checkbox -->
        <div class="form-check d-flex justify-content-center mb-4">
          <input class="form-check-input me-2" type="checkbox" value="" id="registerCheck" checked
            aria-describedby="registerCheckHelpText" />
          <label class="form-check-label" for="registerCheck">
            I have read and agree to the terms
          </label>
        </div>

        <!-- Submit button -->
        <button type="submit" class="btn btn-primary btn-block mb-3">Sign in</button>
      </form>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'RegisterView',
}
</script>

<style>

</style>