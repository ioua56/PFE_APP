package com.example.ServiceDiscovery2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class ServiceDiscovery2Application {

	public static void main(String[] args) {
		SpringApplication.run(ServiceDiscovery2Application.class, args);
	}

}
