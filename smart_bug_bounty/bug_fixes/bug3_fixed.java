import java.util.HashMap;
import java.util.Map;

public class bug3_fixed {
    static class Document {
        final String owner;
        final String content;
        Document(String owner, String content) {
            this.owner = owner;
            this.content = content;
        }
    }

    static String readDocument(Map<String, Document> docs, String user, String id) {
        Document document = docs.get(id);
        if (document == null) return "NOT_FOUND";
        if (document.owner == null || !document.owner.equals(user)) return "ACCESS_DENIED";
        return document.content;
    }

    public static void main(String[] args) {
        Map<String, Document> docs = new HashMap<>();
        docs.put("doc-1", new Document("alex", "Alex's private notes"));
        System.out.println(readDocument(docs, "sam", "doc-1"));
    }
}
