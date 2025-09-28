import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class App {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(8080);
        System.out.println("Server started at http://localhost:8080");

        while (true) {
            Socket client = server.accept();
            try (BufferedWriter out = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()))) {
                String response = "Hello from minimal Java HTTP server 🚀";
                String httpResponse = "HTTP/1.1 200 OK\r\n" +
                                      "Content-Length: " + response.getBytes().length + "\r\n" +
                                      "Content-Type: text/plain\r\n" +
                                      "\r\n" +
                                      response;

                out.write(httpResponse);
                out.flush();
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                client.close();
            }
        }
    }
}
