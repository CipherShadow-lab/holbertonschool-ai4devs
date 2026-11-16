import java.util.*;
public class TestBug3Fixed {
    public static void main(String[] args) {
        Map<String, bug3_fixed.Document> docs = new HashMap<>();
        docs.put("doc-1", new bug3_fixed.Document("alex", "private"));
        check("private", bug3_fixed.readDocument(docs,"alex","doc-1"));
        check("ACCESS_DENIED", bug3_fixed.readDocument(docs,"sam","doc-1"));
        check("NOT_FOUND", bug3_fixed.readDocument(docs,"alex","missing"));
        check("ACCESS_DENIED", bug3_fixed.readDocument(docs,null,"doc-1"));
        System.out.println("4 Java tests passed");
    }
    static void check(String expected, String actual) {
        if (!expected.equals(actual)) throw new AssertionError(expected+" != "+actual);
    }
}
