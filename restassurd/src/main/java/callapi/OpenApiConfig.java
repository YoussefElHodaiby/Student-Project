package callapi;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.servers.Server;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

@Configuration
public class OpenApiConfig {
    
    @Value("${server.port:8080}")
    private String serverPort;
    
    @Bean
    public OpenAPI studentApiDoc() {
        Server apiServer = new Server()
            .url("http://localhost:" + serverPort)
            .description("Local API Server");
            
        return new OpenAPI()
                .servers(List.of(apiServer))
                .info(new Info()
                        .title("Student Management API")
                        .description("REST API for managing student records")
                        .version("1.0"));
    }
}
