
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class test2 {
   
    protected List<List<Object>> Quiz_List=new ArrayList<>();

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
    
    public static void main(String[] args) {
      
       test2 ql = new test2();
       
       List<List<Object>> list = new ArrayList<>();
       // 문제-1 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-1", "학생답-1", "정답-1"));
       
       // 문제-2 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-2", "학생답-2", "정답-2"));
       
       // 문제-3 에대한 각 항목 입력(문제, 학생답, 정답)
       list.add(Arrays.asList("문제-3", "학생답-3", "정답-3"));
       
       ql.setQuiz_List(list);
       
       ql.getQuiz_List().forEach(x->System.out.println(x));
   } //
}