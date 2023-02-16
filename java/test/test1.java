package Quiz;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QuizList {
    protected List<List<Object>> Quiz_List=new ArrayList<>();

    public List<List<Object>> getQuiz_List() {
        return Quiz_List;
    }

    public void setQuiz_List(List<List<Object>> Quiz_list) {
        this.Quiz_List.add(new ArrayList(Arrays.asList("1+1")));       //1열
        this.Quiz_List.add(new ArrayList(Arrays.asList("권지용")));

        this.Quiz_List.get(0).add(1,"g");
        this.Quiz_List.get(0).add(2,"h");

        this.Quiz_List.get(1).add(1,"하");
        this.Quiz_List.get(1).add(1,"대");
//        this.Quiz_List.get(0).get(1).add("h");
//        this.Quiz_List.get(0).add(Arrays.asList("g"));   //2열
//        this.Quiz_List.get(1).add(new ArrayList(Arrays.asList("ㅏ")));
    }
}