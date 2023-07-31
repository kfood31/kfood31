# :plate_with_cutlery: K-Food31 Project
K-Food31 은 딥러닝 기반의 한식 사진 분류 및 추천 서비스입니다.  
외국인 유저에게 31가지의 K-Food 정보와 함께, 한국인들의 찐맛집을 소개하는 모델  

<img src="https://img.shields.io/badge/Python-3.9.10-blue?logo=python"> 

~~ 🔺소개란 수정🔺 ~~

~~ 🔺streamlit 구현 사진 추가🔺 ~~

---
## 📙 목차
### [개요](#개요)
### [데이터셋](#데이터셋)
### [사용 모델](#사용-모델)
### [주요 기능](#주요-기능)
---

## 개요
> <b> 프로젝트 주제 </b> : 외국인 대상 k-food 이미지 분석 및 식당 추천 서비스  
> <b> 서비스명 </b> : kfood31  
> <b> 팀명 </b> : kfood31  
> <b> 개발 기간 </b> : 23.06.23-23.08.07 (약 7주)
<br/>

## 데이터셋

- **음식 데이터셋**  
  ① Image Classification & Detection 을 위해 31가지 카테고리로 구성  
  ② 웹사이트 (Google, Daum, Naver, Instagram, 만개의 레시피) 크롤링 및 [AI-Hub](https://aihub.or.kr/) 데이터 이용  
  ③ 🔺31가지 카테고리*약 2000?장, 총 ~~ 장의 사진 이미지 수집🔺  
  ④ 🔺Train/Test Dataset🔺

  
- **리뷰 데이터셋**  
  ① [식신](https://www.siksinhot.com/) 웹사이트 기준 각 카테고리별 첫페이지 식당 수집  
  ② [네이버 플레이스](map.naver.com) 리뷰 탭 - 사진 포함 리뷰 최대 500개씩 수집
<br/>

## 사용 모델
- **Image Classification** : EffiecientNetV0
- **Object Detection** : YOLOV8
- **Sentiment Analysis** : BERT & Transformers by Hugging Face
<br/>

## 주요 기능
🔺추가🔺

