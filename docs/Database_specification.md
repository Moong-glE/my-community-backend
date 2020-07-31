# Database

## 1. User

- Id (PK)
- Email
- Password
- Name
- StudentId
- ProfileImage
- Dept_Id (FK, 1)
- Article_Ids (FK, N)
- Comment_Ids (FK, N)
- Group_Ids (FK, N)



## 2. Dept

- Id (PK)
- Name
- University
- User_Ids (FK, N)
- Board_Ids (FK, N)
- Group_Ids (FK, N)



## 3. Board

- Id (PK)
- Name
- IsHidden
- Dept_Id (FK, 1)
- Group_Id (FK, 1, Nullable)
- Article_Ids (FK, N)
- Manager_Ids (FK, N)



## 4. Article

- Id (PK)
- Title
- Contents
- Type
- Writer (FK, 1)
- Board_Id (FK, 1)
- LikeBy (FK, N)
- File_Ids (FK, N)
- Comment_Ids (FK, N)
- Vote_Id (FK, 1, Nullable)
- Calander_Id (FK, 1, Nullable)
- Survey_Id (FK, 1, Nullable)



## 5. ArticleFile

- Id (PK)
- File
- Article_Id (FK, 1)



## 6. Comment

- Id (PK, FK, N)
- Contents
- Writer (FK, 1)
- Article_Id (FK, 1)
- Parent_Id (FK, 1)
- LikeBy (FK, N)



## 7. Group

- Id (PK)
- Name
- Description
- Dept_Id (FK, 1)
- Board_Ids (FK, N)
- User_Ids (FK, N)
- Manager_Id (FK, 1)



## 8. DeptApply & GroupApply

- Id (PK)
- RepliedAt
- IsAccepted
- RejectMsg
- Reviewer_Id (FK, 1)
- Dept_Id (FK, 1) || Group_Id (FK, 1)
- User_Id (FK, 1)



## 9. Vote

- Id (PK)
- Question
- ExpiredAt
- IsExpired
- Article_Id (FK, 1)
- Answer_Ids (FK, N)
- AnswerItems (List)



## 10. VoteAnswer

- Id (PK)
- User_Id (FK, 1)
- Vote_Id (FK, 1)
- Answers (List)



## 11. Calander

- Id (PK)
- Description
- StartAt
- EndAt
- Article_Id (FK, 1)



## 12. Survey

- Id (PK)
- Question_Ids (FK, N)
- ExpiredAt
- isExpired
- Article_Id (FK, 1)



## 13. SurveyQuestion

- Id (PK)
- Question
- Survey_Id (FK, 1)
- Answer_Ids (FK, N)



## 13. SurveyAnswer

- Id (Pk)
- Answer
- User_Id (FK, 1)
- Question_Id (FK, 1)