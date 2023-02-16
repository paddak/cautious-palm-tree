package Quiz;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QuizList {
   
    protected List<List<Object>> Quiz_List = new ArrayList<>();

    public List<List<Object>> getQuiz_List() {
        return Quiz_List;
    }

    public void setQuiz_List(List<List<Object>> Quiz_list) {

       // before
 //       this.Quiz_List.add(new ArrayList(Arrays.asList("1+1")));       //1열
 //       this.Quiz_List.add(new ArrayList(Arrays.asList("권지용")));

//        this.Quiz_List.get(0).add(Arrays.asList("g"));   //2열
        
        // this.Quiz_List.get(0).add("학생답");
        // this.Quiz_List.get(0).get(1).add("정답");
//     
        // this.Quiz_List.get(0).get(1).add("k");
//        this.Quiz_List.get(1).add(new ArrayList(Arrays.asList("ㅏ")));
       
       // after
         this.Quiz_List = Quiz_list;
   }
    
    public void setQuiz_List(List<List<Object>> Quiz_list) {

       // before
 //       this.Quiz_List.add(new ArrayList(Arrays.asList("1+1")));       //1열
 //       this.Quiz_List.add(new ArrayList(Arrays.asList("권지용")));

//        this.Quiz_List.get(0).add(Arrays.asList("g"));   //2열
        
        // this.Quiz_List.get(0).add("학생답");
        // this.Quiz_List.get(0).get(1).add("정답");
//     
        // this.Quiz_List.get(0).get(1).add("k");
//        this.Quiz_List.get(1).add(new ArrayList(Arrays.asList("ㅏ")));
       
       // after
         this.Quiz_List = Quiz_list;
   }

    
    public static void main(String[] args) {
      
       QuizList ql = new QuizList();
       
       List<List<Object>> list = new ArrayList<>();
       
       ////////// 문항과 정답안 우선 입력
       
       // 문제-1 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-1", null, "정답-1"));
       
       // 문제-2 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-2", null, "정답-2"));
       
       // 문제-3 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-3", null, "정답-3"));
       
       ql.setQuiz_List(list);
       
       // 문항/학생답/정답 나열
       System.out.println(ql.getQuiz_List().get(0));
       System.out.println(ql.getQuiz_List().get(1));
       System.out.println(ql.getQuiz_List().get(2));
       // ql.getQuiz_List().forEach(x->System.out.println(x));
       
       
       System.out.println("\n/////////////////////////////////////////////\n");
       
       ////////// 시험을 치루면서 학생답이 입력됨
       List<List<Object>> list2 = ql.getQuiz_List();
       
       // 문제-1 ~ 3에 학생답 입력
       list2.get(0).set(1, "학생답-1"); // 문제-1 학생답 입력
       list2.get(1).set(1, "학생답-2"); // 문제-2 학생답 입력
       list2.get(2).set(1, "학생답-3"); // 문제-3 학생답 입력
       
       list2.forEach(x->System.out.println(x));
       
       ///// 이후에는 위의 데이터를 기초로 하여 채점 등의 액션이 있을 수 있겠습니다.
   } //
}