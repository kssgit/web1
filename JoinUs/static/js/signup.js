
$('#join-form').submit(function () {

  let email_pat = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
  if (!email_pat.test(email)) {
    alert("이메일 형식에 맞게 쓰세요!!")
    return;
  }
  alert("로그인 성공!")
});