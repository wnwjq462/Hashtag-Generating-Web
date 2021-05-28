# #️⃣Hashtag Generating Web

## 프로젝트 개요

2021년 YBIGTA 신입기수 프로젝트로 진행하였던, 해시태그 자동 생성 프로그램을 이용하여 개인 프로젝트로 웹 서비스를 구현해보았다. 

## 기술 스택 / 프로젝트 과정

- Hashtag Generator

유저가 업로드한 사진과 비슷한 사진을 찾아주기 위한 Classifier 를 KNN 모델을 이용하여 구현 해주었고, 비슷한 사진들이 각각 가진 해시태그를 이용하여 Word2Vec 으로 태그를 전환하고 확장해주었다.

자세한 내용은 Github: [https://github.com/wnwjq462/Instagram-hashtag-generator](https://github.com/wnwjq462/Instagram-hashtag-generator) 에 기술되어 있음

- Socket 통신

전에 만들어두었던 파이썬 모델과 웹 서버를 연결하기 위해 Socket 통신을 해주었다. 웹 서버로 부터, 사진에 대한 정보를 받아서, 파이썬 서버가 모델을 이용하여 해시태그를 자동으로 생성해 주어, 그 해시태그들을 응답으로 보내줌.

- Web
    - HTML(Thymeleaf), CSS, Javascript

    간단한 웹 페이지 구성을 위해, 프론트엔드는 인스타그램 템플릿을 활용했다. 인스타그램 형식을 아예 따라가는 것은 아니기에 약간의 html, css 파일만 변경해주었다.

    - Java Spring Boot

    유저가 메인 페이지에서 해시태그를 생성할 파일을 올리면, Controller 에서 Service의 filehandler 를 통해 파일을 처리해주고, SocketClient 클래스를 통해 파이썬 모델과 Socket 통신을 한다. 처리해준 파일을 보내고, 응답으로 생성된 해시태그들을 받는다. 이를 다시 메인페이지로 리다이렉트 해주며 보여준다.

## 시연 화면

- 첫 페이지

    ![https://raw.githubusercontent.com/wnwjq462/Hashtag-Generating-Web/master/demonstration/demonstration_1.png](https://raw.githubusercontent.com/wnwjq462/Hashtag-Generating-Web/master/demonstration/demonstration_1.png)

- 파일 선택 시

    ![https://raw.githubusercontent.com/wnwjq462/Hashtag-Generating-Web/master/demonstration/demonstration_2.png](https://raw.githubusercontent.com/wnwjq462/Hashtag-Generating-Web/master/demonstration/demonstration_2.png)

- Generate 버튼을 클릭 한 후

    ![https://github.com/wnwjq462/Hashtag-Generating-Web/blob/master/demonstration/demonstartion_3.png?raw=true](https://github.com/wnwjq462/Hashtag-Generating-Web/blob/master/demonstration/demonstartion_3.png?raw=true)